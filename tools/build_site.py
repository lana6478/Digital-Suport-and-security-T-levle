#!/usr/bin/env python3
"""
Build the docs/ GitHub Pages site from the /content markdown library.

What it does:
  1. Mirrors every file under content/ into docs/content/ (the site fetches
     pages from here at runtime, so the site always shows exactly what's in
     the repo's content library).
  2. Mirrors shared images from assets/img/ into docs/assets/img/.
  3. Generates docs/assets/data/manifest.json - a flat list of every page
     (path + title) used to build the sidebar directory tree.
  4. Generates docs/assets/data/search-index.json - page path/title/plain-text
     used by the in-browser search box.

Run this after adding/editing/removing any file under content/:
    python3 tools/build_site.py
"""
import json
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(ROOT, "content")
IMG_SRC_DIR = os.path.join(ROOT, "assets", "img")
DOCS_DIR = os.path.join(ROOT, "docs")
DOCS_CONTENT_DIR = os.path.join(DOCS_DIR, "content")
DOCS_IMG_DIR = os.path.join(DOCS_DIR, "assets", "img")
DATA_DIR = os.path.join(DOCS_DIR, "assets", "data")

TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


def extract_title(md_text, fallback):
    m = TITLE_RE.search(md_text)
    if m:
        return m.group(1).strip()
    return fallback


def markdown_to_plaintext(md_text):
    text = md_text
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)  # code blocks
    text = re.sub(r"`([^`]*)`", r"\1", text)                  # inline code
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)         # images
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)      # links -> label
    text = re.sub(r"<figcaption>(.*?)</figcaption>", r"\1", text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)                       # raw HTML tags (e.g. <figure>/<img>)
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)  # heading markers
    text = re.sub(r"[*_>#|-]", " ", text)                      # markdown punctuation
    text = re.sub(r"\s+", " ", text).strip()
    return text


def main():
    if not os.path.isdir(CONTENT_DIR):
        raise SystemExit(f"No content/ directory found at {CONTENT_DIR}")

    if os.path.isdir(DOCS_CONTENT_DIR):
        shutil.rmtree(DOCS_CONTENT_DIR)
    os.makedirs(DOCS_CONTENT_DIR, exist_ok=True)
    os.makedirs(DATA_DIR, exist_ok=True)

    if os.path.isdir(IMG_SRC_DIR):
        if os.path.isdir(DOCS_IMG_DIR):
            shutil.rmtree(DOCS_IMG_DIR)
        shutil.copytree(IMG_SRC_DIR, DOCS_IMG_DIR)

    manifest = []
    search_index = []

    for dirpath, dirnames, filenames in os.walk(CONTENT_DIR):
        dirnames.sort()
        for filename in sorted(filenames):
            if not filename.endswith(".md"):
                continue
            src_path = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(src_path, CONTENT_DIR).replace(os.sep, "/")

            dest_path = os.path.join(DOCS_CONTENT_DIR, rel_path)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copyfile(src_path, dest_path)

            with open(src_path, "r", encoding="utf-8") as f:
                md_text = f.read()

            fallback_title = filename[:-3].replace("-", " ").title()
            title = extract_title(md_text, fallback_title)
            plain_text = markdown_to_plaintext(md_text)

            manifest.append({"path": rel_path, "title": title})
            search_index.append({"path": rel_path, "title": title, "text": plain_text})

    manifest.sort(key=lambda item: item["path"])
    search_index.sort(key=lambda item: item["path"])

    with open(os.path.join(DATA_DIR, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=0)

    with open(os.path.join(DATA_DIR, "search-index.json"), "w", encoding="utf-8") as f:
        json.dump(search_index, f, ensure_ascii=False, indent=0)

    print(f"Built site data for {len(manifest)} pages.")
    print(f"  Mirrored content -> {DOCS_CONTENT_DIR}")
    print(f"  Mirrored images -> {DOCS_IMG_DIR}")
    print(f"  Wrote {os.path.join(DATA_DIR, 'manifest.json')}")
    print(f"  Wrote {os.path.join(DATA_DIR, 'search-index.json')}")


if __name__ == "__main__":
    main()
