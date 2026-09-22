# Digital Support and Security T Level

An organised, browsable study-guide library for the **T Level Technical Qualification in Digital Support and Security (Level 3)** — Pearson's specification, first teaching September 2025 (built from spec version 1.1, August 2026).

This is an **independent, unofficial** revision resource. It paraphrases and reorganises the official specification for easier browsing and searching — it is not a substitute for the real thing, and nothing here should be treated as assessment-authoritative. Always check the [official specification PDF](https://qualifications.pearson.com/content/dam/pdf/TLevels/digital-support-and-security/2025/specification-and-sample-assessment-materials/digital-dss-specification.pdf) for anything that matters for exams or coursework.

## Two ways to use this repo

1. **Browse the files directly** — everything lives under [`content/`](content/), organised into clearly named folders and files so you can go straight to the topic you need (see the map below).
2. **Browse the wiki site** — [`docs/`](docs/) is a static, Wikipedia-style website (built for GitHub Pages) with a search bar and a sidebar directory tree, showing the exact same files as `content/` in a more navigable form. See [Website](#website) below.

## Content map

| Folder | What's in it |
|---|---|
| [`content/00-overview/`](content/00-overview/) | What a T Level is, qualification structure & weighting, student progression/careers, grading |
| [`content/01-core-component/`](content/01-core-component/) | The knowledge every student studies: Core Paper 1, Core Paper 2, Employer Set Projects, core scheme of assessment |
| [`content/02-occupational-specialisms/`](content/02-occupational-specialisms/) | The four specialisms students choose between: **Digital Infrastructure**, **Network Cabling**, **Digital Support**, **Cyber Security** — each with its own security, technical-skills and sources-of-knowledge content areas |
| [`content/03-appendices/`](content/03-appendices/) | General English/maths/digital competency frameworks, command word taxonomy, diagram notation |
| [`content/sources-and-further-reading.md`](content/sources-and-further-reading.md) | Links to primary/official sources and related apprenticeship standards |

Every markdown file starts with a `# Title` and an italic breadcrumb line so you always know where you are, and ends with a **Key terms** glossary and **Related pages** links to jump around the library.

## Website

The `docs/` folder is a small, dependency-free static site (plain HTML/CSS/JS) designed to look and feel like a minimal wiki:

- a **search bar** (top) that full-text searches every page,
- a **sidebar** directory tree mirroring `content/`, always highlighting the folder/file path you're currently viewing,
- an **article pane** that renders the markdown pages themselves.

It reads its page list and content straight from `docs/content/`, a generated mirror of the repo's `content/` folder — so the website always shows the same material as the file library, just easier to navigate.

### Building/updating the site

After adding, editing or removing anything in `content/`, regenerate the site data:

```bash
python3 tools/build_site.py
```

This copies every file from `content/` into `docs/content/` and rebuilds `docs/assets/data/manifest.json` (directory tree) and `docs/assets/data/search-index.json` (search index).

### Viewing it locally

```bash
cd docs
python3 -m http.server 8000
# then open http://localhost:8000
```

### Publishing it

GitHub Pages isn't switched on for this repo yet. To enable it: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main`, folder: `/docs`**. Once enabled, the site will be live at `https://<username>.github.io/Digital-Suport-and-security-T-levle/`.

## Contributing / editing

- Add new topics as new `.md` files under the right `content/` subfolder, following the existing template (H1 title, breadcrumb, sections, Key terms, Related pages).
- Re-run `python3 tools/build_site.py` after any content change so the website stays in sync.
- Keep filenames lowercase, hyphenated, and numbered where order matters (e.g. `01-`, `02-`) so both the repo file listing and the sidebar sort sensibly.
