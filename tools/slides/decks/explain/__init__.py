"""
Explanations and quick-check questions, added to the teaching slides.

Each module maps deck file -> {slide title: E(text, example, check)}:
    text     the explanation, as paragraphs separated by a blank line;
             a paragraph starting "Label: " gets a bold label
    example  a short worked example or real-world case (optional)
    check    2 or 3 (question, answer) pairs asked straight after the topic

build_slides.py matches these to slides by title and refuses to build if a
title doesn't exist, so rename both together.
"""


def E(text, example=None, check=()):
    return {"explain": {"text": text, "example": example}, "check": list(check)}


# Every module in this package is loaded automatically.
import importlib as _importlib  # noqa: E402
import pkgutil as _pkgutil  # noqa: E402

EXPLAIN = {}
for _info in _pkgutil.iter_modules(__path__):
    _mod = _importlib.import_module(f"{__name__}.{_info.name}")
    for _deck, _slides in getattr(_mod, "EXPLAIN", {}).items():
        EXPLAIN.setdefault(_deck, {}).update(_slides)
