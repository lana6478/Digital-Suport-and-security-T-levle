#!/usr/bin/env python3
"""
Build the lesson-slide PowerPoint decks and link them into the wiki.

What it does:
  1. Renders every deck defined in tools/slides/decks/*.py to a .pptx under
     content/05-teaching-resources/slides/.
  2. Writes content/05-teaching-resources/01-lesson-slides.md, an index of
     every deck grouped by area.
  3. Adds (or refreshes) a "Teaching resources" table on each topic page,
     between the <!-- teaching-resources:start/end --> markers, listing the
     decks that cover that page.

Requires python-pptx:
    pip install python-pptx

Then run from the repository root, followed by the normal site build:
    python3 tools/slides/build_slides.py
    python3 tools/build_site.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

import render  # noqa: E402
from decks import ALL_DECKS, AREA_ORDER  # noqa: E402

CONTENT_DIR = os.path.join(ROOT, "content")
RES_DIR_REL = "05-teaching-resources"
SLIDES_REL = RES_DIR_REL + "/slides"
INDEX_REL = RES_DIR_REL + "/01-lesson-slides.md"

START = "<!-- teaching-resources:start -->"
END = "<!-- teaching-resources:end -->"
BANNED = ["\u2014", "\u2013"]  # no em or en dashes anywhere in the decks


def page_title(rel):
    with open(os.path.join(CONTENT_DIR, rel), encoding="utf-8") as f:
        m = re.search(r"^#\s+(.+?)\s*$", f.read(), re.MULTILINE)
    return m.group(1) if m else rel


def check_dashes(obj, where):
    if isinstance(obj, str):
        for d in BANNED:
            if d in obj:
                raise SystemExit(f"Dash character {d!r} found in {where}: {obj[:80]!r}")
    elif isinstance(obj, dict):
        for k, v in obj.items():
            check_dashes(v, f"{where}.{k}")
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            check_dashes(v, f"{where}[{i}]")


def rel_link(from_page, target):
    """Relative link from one content/ file to another."""
    return os.path.relpath(target, os.path.dirname(from_page)).replace(os.sep, "/")


def section_for_page(page, decks):
    lines = [
        START,
        "## Teaching resources",
        "",
        "Ready-made lesson slides for this topic. Each PowerPoint includes learning objectives, "
        "a starter, teaching slides, a quiz with answers, an activity and an exit ticket, with "
        "teacher notes on every slide. Download it and adapt it for your class.",
        "",
        "| Lesson slides | Covers | Slides |",
        "|---|---|---|",
    ]
    for d in decks:
        link = rel_link(page, SLIDES_REL + "/" + d["file"])
        lines.append(f"| [{d['title']} (PowerPoint)]({link}) | {d['spec']} | {d['_slides']} |")
    lines += ["", "See [all lesson slides](" + rel_link(page, INDEX_REL) + ") for every topic.", END]
    return "\n".join(lines)


def inject(page, decks):
    path = os.path.join(CONTENT_DIR, page)
    with open(path, encoding="utf-8") as f:
        md = f.read()
    block = section_for_page(page, decks)
    if START in md:
        md = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, md, flags=re.DOTALL)
    else:
        # Place it just before "Key terms" (or "Related pages"), so it sits
        # under the topic content but above the page's closing lists.
        for anchor in ("\n## Key terms", "\n## Related pages", "\n## Further reading"):
            if anchor in md:
                md = md.replace(anchor, "\n" + block + "\n" + anchor, 1)
                break
        else:
            md = md.rstrip("\n") + "\n\n" + block + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(md)


def write_index(decks):
    out = [
        "# Lesson Slides",
        "",
        "*Digital Support and Security T Level → Teaching Resources → Lesson Slides*",
        "",
        "Free, editable PowerPoint lesson decks for every topic in the qualification, written to match "
        "the revision notes on this site. Each deck covers one subject, so you can pick up exactly the "
        "lesson you need. Every deck follows the same shape:",
        "",
        "- **Learning objectives and a starter** to open the lesson.",
        "- **Teaching slides** that follow the specification's own numbering.",
        "- **A quiz with an answer slide** to check understanding.",
        "- **A timed activity** with success criteria.",
        "- **An exit ticket** that links students back to the revision notes.",
        "",
        "Every slide has **teacher notes** in the speaker notes pane. The decks are unofficial: "
        "check the [official specification](https://qualifications.pearson.com/content/dam/pdf/TLevels/"
        "digital-support-and-security/2025/specification-and-sample-assessment-materials/"
        "digital-dss-specification.pdf) for anything assessment-critical.",
        "",
    ]
    for area in AREA_ORDER:
        group = [d for d in decks if d["area"] == area["key"]]
        if not group:
            continue
        out += [f"## {area['heading']}", ""]
        if area.get("blurb"):
            out += [area["blurb"], ""]
        out += ["| Lesson slides | Covers | Revision notes |", "|---|---|---|"]
        for d in group:
            link = rel_link(INDEX_REL, SLIDES_REL + "/" + d["file"])
            notes = "<br>".join(
                f"[{page_title(p)}]({rel_link(INDEX_REL, p)})" for p in d["pages"]
            )
            out.append(f"| [{d['title']}]({link}) | {d['spec']} | {notes} |")
        out.append("")
    out += [
        "## Editing or adding decks",
        "",
        "The decks are generated from short content files in the repository's "
        "`tools/slides/decks/` folder. To change a deck, edit its content file and run "
        "`python3 tools/slides/build_slides.py` followed by `python3 tools/build_site.py`. "
        "See the [Developers page](../04-help-and-about/02-developers.md) for details.",
        "",
        "## Related pages",
        "",
        "- [Core Component overview](../01-core-component/00-overview.md)",
        "- [Occupational Specialisms overview](../02-occupational-specialisms/00-overview.md)",
        "- [Help](../04-help-and-about/01-help.md)",
        "",
    ]
    with open(os.path.join(CONTENT_DIR, INDEX_REL), "w", encoding="utf-8") as f:
        f.write("\n".join(out))


def main():
    only = set(sys.argv[1:])
    out_dir = os.path.join(CONTENT_DIR, SLIDES_REL)
    ids = set()
    for d in ALL_DECKS:
        if d["file"] in ids:
            raise SystemExit("Duplicate deck file " + d["file"])
        ids.add(d["file"])
        check_dashes(d, d["file"])

    total = 0
    for d in ALL_DECKS:
        d["page"] = d["pages"][0]
        d["page_title"] = page_title(d["page"])
        dest = os.path.join(out_dir, d["file"])
        if only and d["file"] not in only:
            # keep the slide count for the page tables without rebuilding
            from pptx import Presentation
            d["_slides"] = len(Presentation(dest).slides) if os.path.exists(dest) else "?"
            continue
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        d["_slides"] = render.Deck(d).build(dest)
        total += 1
        print(f"  {d['_slides']:>2} slides  {d['file']}")

    by_page = {}
    for d in ALL_DECKS:
        for p in d["pages"]:
            by_page.setdefault(p, []).append(d)
    for page, decks in by_page.items():
        inject(page, decks)
    write_index(ALL_DECKS)

    print(f"Built {total} decks; linked from {len(by_page)} pages.")
    if render.WARNINGS:
        print("\nPossible overflow (check these slides):")
        for w in render.WARNINGS:
            print("  " + w)


if __name__ == "__main__":
    main()
