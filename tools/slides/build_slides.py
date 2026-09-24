#!/usr/bin/env python3
"""
Build the lesson-slide PowerPoint decks and link them into the wiki.

This file is identical in every T Level study-guide repo; site-specific
settings live in decks/__init__.py.

What it does:
  1. Renders every deck defined in tools/slides/decks/*.py to a .pptx under
     content/05-teaching-resources/slides/.
  2. Writes content/05-teaching-resources/01-lesson-slides.md, an index of
     every deck grouped by area.
  3. Adds (or refreshes) a "Teaching resources" table on each topic page,
     between the <!-- teaching-resources:start/end --> markers, listing the
     decks that cover that page.
  4. Adds (or refreshes) a "Lesson slides for this section" link at the end
     of the matching section of text on each page, between
     <!-- lesson-slide:start/end --> markers. decks/placement.py says which
     sections each deck belongs under.

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
from decks import ALL_DECKS, AREA_ORDER, SITE  # noqa: E402
try:
    from decks.explain import EXPLAIN  # noqa: E402
except ImportError:
    EXPLAIN = {}
from decks.placement import PLACEMENT  # noqa: E402

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


INLINE_START = "<!-- lesson-slide:start -->"
INLINE_END = "<!-- lesson-slide:end -->"
HEADING_RE = re.compile(r"^(#{2,3})\s+(.*?)\s*$")
NUMBER_RE = re.compile(r"(\d+)\.(\d+)(?:\s*[\u2013-]\s*(\d+)\.(\d+))?\s")


def heading_numbers(text):
    """Spec numbers a heading covers: '1.8\u20131.9 Disaster...' -> {'1.8', '1.9'}."""
    m = NUMBER_RE.match(text + " ")
    if not m:
        return set()
    area, first = m.group(1), int(m.group(2))
    last = int(m.group(4)) if m.group(4) and m.group(3) == area else first
    return {f"{area}.{n}" for n in range(first, last + 1)}


def inline_positions(lines, targets):
    """Line indexes to insert a deck's inline link before (end of each section run)."""
    heads = [(i, HEADING_RE.match(l).group(2)) for i, l in enumerate(lines) if HEADING_RE.match(l)]
    next_head = {}
    for k, (i, _) in enumerate(heads):
        next_head[i] = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
    positions = []
    if "top" in targets:
        first_h2 = next((i for i, l in enumerate(lines) if l.startswith("## ")), len(lines))
        positions.append(first_h2)
    numbered = [(i, heading_numbers(t)) for i, t in heads if heading_numbers(t)]
    wanted = {t for t in targets if re.fullmatch(r"\d+\.\d+", t)}
    run_end = None
    for i, nums in numbered:
        if nums & wanted:
            run_end = i
        elif run_end is not None:
            positions.append(next_head[run_end])
            run_end = None
    if run_end is not None:
        positions.append(next_head[run_end])
    for t in targets:
        if t != "top" and not re.fullmatch(r"\d+\.\d+", t):
            for i, text in heads:
                if text.startswith(t):
                    positions.append(next_head[i])
    return positions


def inject(page, decks):
    path = os.path.join(CONTENT_DIR, page)
    with open(path, encoding="utf-8") as f:
        md = f.read()
    # Remove anything a previous build added, then add it all back fresh.
    md = re.sub(re.escape(INLINE_START) + r".*?" + re.escape(INLINE_END) + r"\n\n", "", md, flags=re.DOTALL)
    md = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\n\n?", "", md, flags=re.DOTALL)

    lines = md.split("\n")
    inserts = {}
    for d in decks:
        targets = PLACEMENT.get(d["file"], {}).get(page, [])
        for pos in inline_positions(lines, targets):
            if d not in inserts.setdefault(pos, []):
                inserts[pos].append(d)
    for pos in sorted(inserts, reverse=True):
        quote = "\n>\n".join(
            f"> **Lesson slides for this section:** [{d['title']}]({rel_link(page, SLIDES_REL + '/' + d['file'])}) "
            f"(PowerPoint, {d['_slides']} slides)"
            for d in inserts[pos]
        )
        block = [INLINE_START, quote, INLINE_END, ""]
        # keep a blank line between the section text and the link
        if pos > 0 and lines[pos - 1].strip():
            block.insert(0, "")
        lines[pos:pos] = block
    md = "\n".join(lines)

    block = section_for_page(page, decks)
    # Place the table just before "Key terms" (or "Related pages"), so it sits
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
        f"*{SITE['name']} \u2192 Teaching Resources \u2192 Lesson Slides*",
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
        f"check the [official specification]({SITE['spec_url']}) for anything assessment-critical.",
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
        "## Related pages",
        "",
    ]
    out += [f"- [{page_title(p)}]({rel_link(INDEX_REL, p)})" for p in SITE["related"]]
    out.append("")
    with open(os.path.join(CONTENT_DIR, INDEX_REL), "w", encoding="utf-8") as f:
        f.write("\n".join(out))


def main():
    only = set(sys.argv[1:])
    out_dir = os.path.join(CONTENT_DIR, SLIDES_REL)
    ids = set()
    # Attach each topic's explanation and quick-check questions (decks/explain/)
    # to the matching slide, by deck file and slide title.
    for d in ALL_DECKS:
        extra = EXPLAIN.get(d["file"], {})
        titles = {sl.get("title") for sl in d["slides"]}
        for t in extra:
            if t not in titles:
                raise SystemExit(f"Explanation for unknown slide {t!r} in {d['file']}")
        for sl in d["slides"]:
            if sl.get("title") in extra:
                sl["explain"] = extra[sl["title"]]["explain"]
                sl["check"] = extra[sl["title"]].get("check")

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
