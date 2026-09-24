"""
Deck content for the lesson slides, one module per area of the course.

Each deck is a dict with:
    area        core | shared | cyber | di | ds | nc   (sets colour and label)
    file        output path under content/05-teaching-resources/slides/
    title       deck title
    unit        short location, e.g. "Core Paper 1"
    spec        specification sections covered, e.g. "1.1, 1.2, 2.7"
    pages       content/ pages the deck is linked from (first = main page)
    objectives  3 to 4 learning objectives
    starter     starter question
    slides      teaching slides (see render.py for the slide types)
    quiz        list of (question, answer)
    activity    {title, time, format, steps, success, notes}
    exit        3 exit-ticket prompts

Never use em or en dashes in deck text; the build refuses them.
"""
SITE = {
    "name": "Digital Support and Security T Level",
    "short": "Digital Support and Security",
    "url": "https://lana6478.github.io/Digital-Suport-and-security-T-levle/",
    "author": "Samuel O'Connell",
    "awarding_body": "Pearson",
    "spec_url": "https://qualifications.pearson.com/content/dam/pdf/TLevels/digital-support-and-security/"
                "2025/specification-and-sample-assessment-materials/digital-dss-specification.pdf",
    # pages listed under "Related pages" on the Lesson Slides index
    "related": [
        "01-core-component/00-overview.md",
        "02-occupational-specialisms/00-overview.md",
        "04-help-and-about/01-help.md",
    ],
}

# Areas of the course: label shown on slides, accent colour (hex), and
# light_text for accents dark enough to need white numbers on them.
AREAS = {
    "core": {"label": "Core Component", "accent": "F2B705"},
    "shared": {"label": "Occupational Specialisms", "accent": "4EA1FF"},
    "cyber": {"label": "Cyber Security", "accent": "E0463A", "light_text": True},
    "di": {"label": "Digital Infrastructure", "accent": "33C17A"},
    "ds": {"label": "Digital Support", "accent": "4EA1FF"},
    "nc": {"label": "Network Cabling", "accent": "F2B705"},
}

from . import core, shared, cyber, di, ds, nc  # noqa: E402

ALL_DECKS = core.DECKS + shared.DECKS + cyber.DECKS + di.DECKS + ds.DECKS + nc.DECKS

AREA_ORDER = [
    {"key": "core", "heading": "Core Component",
     "blurb": "Core Paper 1, Core Paper 2 and the Employer Set Project. Every student studies these."},
    {"key": "shared", "heading": "Occupational Specialisms: shared topics",
     "blurb": "The security content that Digital Infrastructure, Digital Support and Network Cabling "
              "share, plus sources of knowledge, which all four specialisms study."},
    {"key": "cyber", "heading": "Cyber Security specialism", "blurb": ""},
    {"key": "di", "heading": "Digital Infrastructure specialism", "blurb": ""},
    {"key": "ds", "heading": "Digital Support specialism", "blurb": ""},
    {"key": "nc", "heading": "Network Cabling specialism", "blurb": ""},
]
