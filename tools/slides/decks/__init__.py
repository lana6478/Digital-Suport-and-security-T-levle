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
from . import core, shared, cyber, di, ds, nc

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
