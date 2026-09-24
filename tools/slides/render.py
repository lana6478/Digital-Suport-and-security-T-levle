"""
Slide renderer for the T Level lesson-slide decks.

This file is identical in every T Level study-guide repo; everything
site-specific (name, URL, areas and their colours) comes from SITE and
AREAS in decks/__init__.py.

Turns a plain-Python deck spec (see decks/*.py) into a styled .pptx lesson
deck using python-pptx. Every deck gets the same lesson shape:

    title -> objectives + starter -> content slides -> quiz -> answers
    -> activity -> exit ticket

Content slide types (the "type" key of each entry in a deck's "slides"):
    bullets   title, bullets, callout (key idea panel on the right)
    cards     title, cards [(heading, body), ...]  (2 to 6 cards)
    process   title, steps [(label, detail), ...]  (3 to 7 steps), optional caption
    compare   title, left (heading, [bullets]), right (heading, [bullets])
    table     title, header [...], rows [[...], ...]
    terms     title (optional), terms [(term, definition), ...]

Every slide takes an optional "notes" string for the teacher.

A slide can also carry "explain" ({text, example}) and "check" ([(q, a)]),
attached by build_slides.py from decks/explain/. The deck then shows an
explanation slide first, the summary slide, then a quick-check slide with
the answers in the speaker notes.
"""
import math
import re

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

# Palette taken from the website's own artwork and styles.
NAVY = RGBColor(0x03, 0x30, 0x6E)
BLUE = RGBColor(0x06, 0x45, 0xAD)
ICE = RGBColor(0xEA, 0xF3, 0xFF)
SKY = RGBColor(0xA9, 0xC8, 0xF0)
TEXT = RGBColor(0x20, 0x21, 0x22)
MUTED = RGBColor(0x54, 0x59, 0x5D)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LINE = RGBColor(0xD5, 0xDD, 0xE8)

from decks import SITE, AREAS as _AREAS  # noqa: E402

# One accent colour per area of the course, set in decks/__init__.py.
AREAS = {
    key: {
        "label": a["label"],
        "accent": RGBColor.from_string(a["accent"]),
        "on_accent": WHITE if a.get("light_text") else TEXT,
    }
    for key, a in _AREAS.items()
}

HEAD_FONT = "Cambria"
BODY_FONT = "Calibri"
SITE_URL = SITE["url"]

W = 13.333
H = 7.5
MARGIN = 0.6

# Every overflow risk the fitter could not solve is collected here so the
# build can report it instead of silently shipping cut-off text.
WARNINGS = []


# ---------------------------------------------------------------- text fitting

def _lines_needed(text, width_in, size_pt, char_w=0.5):
    """Rough line count for text in Calibri at size_pt in a box width_in wide."""
    chars_per_line = max(1, int(width_in * 72 / (size_pt * char_w)))
    total = 0
    for para in text.split("\n"):
        total += max(1, math.ceil(len(para) / chars_per_line))
    return total


def fit_size(paras, width_in, height_in, max_pt, min_pt, spacing=0.35, char_w=0.5, indent_in=0.0):
    """Largest font size (pt) at which paras fit the box, by estimate."""
    # Hyphenated words can wrap at the hyphen, so measure the pieces.
    longest = max((len(w) for p in paras for w in re.split(r"[\s-]+", p) if w), default=1)
    size = max_pt
    while size >= min_pt:
        # A single word wider than the box would be broken mid-word.
        if longest * size * char_w * 1.1 / 72 > width_in - indent_in:
            size -= 1
            continue
        height = 0.0
        for p in paras:
            lines = _lines_needed(p, width_in - indent_in, size, char_w)
            height += lines * size * 1.2 / 72
        height += (len(paras) - 1) * size * spacing / 72
        if height <= height_in:
            return size
        size -= 1
    return None


# ---------------------------------------------------------------- primitives

def _fill(shape, color):
    shape.fill.solid()
    shape.fill.fore_color.rgb = color


def _no_line(shape):
    shape.line.fill.background()


def rect(slide, x, y, w, h, color, shape=MSO_SHAPE.RECTANGLE, line=None):
    s = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    _fill(s, color)
    if line:
        s.line.color.rgb = line
        s.line.width = Pt(1)
    else:
        _no_line(s)
    s.shadow.inherit = False
    if s.has_text_frame:
        s.text_frame.text = ""
    return s


def rounded(slide, x, y, w, h, color, line=None, radius=0.08):
    s = rect(slide, x, y, w, h, color, MSO_SHAPE.ROUNDED_RECTANGLE, line)
    s.adjustments[0] = radius
    return s


def text(slide, x, y, w, h, content, size=16, color=TEXT, bold=False, font=BODY_FONT,
         align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, italic=False, margin=0.0):
    """Add a text box. content is a string (paragraphs split on \\n)."""
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    tf.vertical_anchor = anchor
    for side in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, side, Inches(margin))
    for i, para in enumerate(content.split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        run = p.add_run()
        run.text = para
        f = run.font
        f.size = Pt(size)
        f.bold = bold
        f.italic = italic
        f.name = font
        f.color.rgb = color
    return tb


def bullet_list(slide, x, y, w, h, items, max_pt=24, min_pt=12, color=TEXT, where="",
                bullet_color=BLUE):
    """Bulleted list with real paragraph bullets, auto-sized to the box."""
    # Bold "Label:" prefixes run wider than plain text, so estimate generously.
    size = fit_size(items, w, h * 0.92, max_pt, min_pt, spacing=0.45, indent_in=0.3, char_w=0.53)
    if size is None:
        size = min_pt
        WARNINGS.append(f"{where}: bullet list may overflow ({len(items)} items)")
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    for side in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, side, Inches(0))
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(size * 0.45)
        _set_bullet(p, bullet_color)
        _add_rich(p, item, size, color)
    return tb


def _add_rich(p, item, size, color):
    """Add a run, making any 'Label:' prefix bold."""
    label, sep, rest = item.partition(": ")
    if sep and len(label) <= 40 and len(label.split()) <= 5:
        parts = [(label + ":", True), (" " + rest, False)]
    else:
        parts = [(item, False)]
    for chunk, bold in parts:
        run = p.add_run()
        run.text = chunk
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.name = BODY_FONT
        run.font.color.rgb = color


def _set_bullet(p, color):
    """Give a paragraph a real round bullet with a hanging indent."""
    from pptx.oxml.ns import qn
    from lxml import etree

    pPr = p._p.get_or_add_pPr()
    pPr.set("marL", str(int(Inches(0.3))))
    pPr.set("indent", str(int(-Inches(0.3))))
    for tag in ("a:buClr", "a:buFont", "a:buChar", "a:buNone"):
        for el in pPr.findall(qn(tag)):
            pPr.remove(el)
    buClr = etree.SubElement(pPr, qn("a:buClr"))
    srgb = etree.SubElement(buClr, qn("a:srgbClr"))
    srgb.set("val", str(color))
    buFont = etree.SubElement(pPr, qn("a:buFont"))
    buFont.set("typeface", "Arial")
    buChar = etree.SubElement(pPr, qn("a:buChar"))
    buChar.set("char", "•")


def badge(slide, x, y, d, label, fill, fg, size=None):
    """The deck motif: a filled circle carrying a number or letter."""
    c = rect(slide, x, y, d, d, fill, MSO_SHAPE.OVAL)
    tf = c.text_frame
    for side in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, side, Inches(0))
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = str(label)
    run.font.size = Pt(size or max(10, int(d * 30)))
    run.font.bold = True
    run.font.name = BODY_FONT
    run.font.color.rgb = fg
    return c


# ---------------------------------------------------------------- deck class

class Deck:
    def __init__(self, spec):
        self.spec = spec
        self.area = AREAS[spec["area"]]
        self.prs = Presentation()
        self.prs.slide_width = Inches(W)
        self.prs.slide_height = Inches(H)
        self.blank = self.prs.slide_layouts[6]
        self.count = 0
        props = self.prs.core_properties
        props.title = spec["title"]
        props.subject = SITE["name"] + ": " + spec["unit"]
        props.author = SITE["author"]
        props.keywords = "T Level; " + SITE["short"] + "; lesson slides; " + spec["spec"]

    # -- frame shared by all content slides
    def _slide(self, title, notes=None, dark=False):
        s = self.prs.slides.add_slide(self.blank)
        self.count += 1
        bg = s.background.fill
        bg.solid()
        bg.fore_color.rgb = NAVY if dark else WHITE
        where = f"{self.spec['file']} slide {self.count}"
        if title is not None:
            kicker = f"{self.area['label'].upper()}  ·  {self.spec['unit']}"
            text(s, MARGIN, 0.35, W - 2 * MARGIN, 0.3, kicker, size=11, bold=True,
                 color=SKY if dark else MUTED)
            size = fit_size([title], W - 2 * MARGIN, 0.85, 32, 24, char_w=0.52)
            if size is None:
                size = 24
                WARNINGS.append(f"{where}: title too long")
            text(s, MARGIN, 0.62, W - 2 * MARGIN, 0.9, title, size=size, bold=True,
                 font=HEAD_FONT, color=WHITE if dark else NAVY, anchor=MSO_ANCHOR.MIDDLE)
        if not dark:
            text(s, MARGIN, H - 0.45, 9, 0.3,
                 f"{SITE['name']}  ·  {self.spec['title']}",
                 size=10, color=MUTED)
            text(s, W - MARGIN - 1, H - 0.45, 1, 0.3, str(self.count), size=10,
                 color=MUTED, align=PP_ALIGN.RIGHT)
        if notes:
            s.notes_slide.notes_text_frame.text = notes
        return s, where

    # -- fixed lesson slides
    def title_slide(self):
        sp = self.spec
        s, _ = self._slide(None, notes=sp.get("intro_notes"), dark=True)
        # Motif: overlapping circles on the right.
        for (cx, cy, d, col) in ((9.4, 1.1, 3.6, BLUE), (10.9, 3.5, 2.6, self.area["accent"]),
                                 (8.9, 4.4, 1.5, SKY)):
            rect(s, cx, cy, d, d, col, MSO_SHAPE.OVAL)
        text(s, MARGIN, 1.0, 8, 0.4, self.area["label"].upper(), size=14, bold=True,
             color=self.area["accent"])
        size = fit_size([sp["title"]], 8.0, 2.4, 44, 30, char_w=0.52) or 30
        text(s, MARGIN, 1.5, 8.0, 2.5, sp["title"], size=size, bold=True, font=HEAD_FONT,
             color=WHITE, anchor=MSO_ANCHOR.BOTTOM)
        text(s, MARGIN, 4.2, 8.0, 0.5, sp["unit"], size=18, color=SKY)
        text(s, MARGIN, 4.7, 8.0, 0.5, "Specification reference: " + sp["spec"], size=14, color=SKY)
        text(s, MARGIN, 6.3, 8.2, 0.7,
             SITE["name"] + "  ·  Lesson slides\n"
             "Unofficial teaching resource. Check the official " + SITE["awarding_body"] + " specification for assessment detail.",
             size=11, color=SKY)

    def objectives_slide(self):
        sp = self.spec
        s, where = self._slide("Learning objectives", notes=sp.get("objectives_notes"))
        objs = sp["objectives"]
        text(s, MARGIN, 1.65, 7.4, 0.4, "By the end of this lesson you should be able to:", size=16,
             color=MUTED, italic=True)
        top, gap = 2.2, 0.15
        row_h = min(1.0, (6.6 - top - gap * (len(objs) - 1)) / len(objs))
        for i, obj in enumerate(objs):
            y = top + i * (row_h + gap)
            badge(s, MARGIN, y + (row_h - 0.5) / 2, 0.5, i + 1, self.area["accent"],
                  self.area["on_accent"], size=16)
            size = fit_size([obj], 6.6, row_h, 20, 13) or 13
            text(s, MARGIN + 0.75, y, 6.6, row_h, obj, size=size, anchor=MSO_ANCHOR.MIDDLE)
        # Starter panel
        rounded(s, 8.5, 1.65, 4.23, 4.95, ICE)
        text(s, 8.8, 1.9, 3.6, 0.4, "STARTER", size=13, bold=True, color=BLUE)
        size = fit_size([sp["starter"]], 3.6, 3.9, 22, 14, char_w=0.52) or 14
        text(s, 8.8, 2.4, 3.6, 4.0, sp["starter"], size=size, font=HEAD_FONT, color=NAVY)

    def quiz_slides(self):
        qs = self.spec["quiz"]
        s, where = self._slide("Check your understanding",
                               notes="Give students a few minutes to answer on mini whiteboards or paper, "
                                     "then reveal the answers on the next slide.")
        self._numbered_rows(s, [q for q, _ in qs], where, top=1.75)
        s, where = self._slide("Answers", notes="Talk through any answers the class found difficult.")
        self._numbered_rows(s, [f"{q}\n{a}" for q, a in qs], where, top=1.75, answers=True)

    def _numbered_rows(self, s, items, where, top, answers=False):
        gap = 0.18
        avail = H - 0.7 - top
        row_h = (avail - gap * (len(items) - 1)) / len(items)
        for i, item in enumerate(items):
            y = top + i * (row_h + gap)
            badge(s, MARGIN, y + 0.02, 0.45, i + 1, self.area["accent"], self.area["on_accent"], size=14)
            if answers:
                q, a = item.split("\n", 1)
                size = fit_size([q, a], W - 2 * MARGIN - 0.75, row_h, 18, 10, spacing=0.1)
                if size is None:
                    size = 10
                    WARNINGS.append(f"{where}: answer row {i + 1} may overflow")
                tb = text(s, MARGIN + 0.75, y, W - 2 * MARGIN - 0.75, row_h, q, size=size, color=MUTED)
                p = tb.text_frame.add_paragraph()
                r = p.add_run()
                r.text = a
                r.font.size = Pt(size)
                r.font.bold = True
                r.font.name = BODY_FONT
                r.font.color.rgb = NAVY
            else:
                size = fit_size([item], W - 2 * MARGIN - 0.75, row_h, 22, 12)
                if size is None:
                    size = 12
                    WARNINGS.append(f"{where}: question {i + 1} may overflow")
                text(s, MARGIN + 0.75, y, W - 2 * MARGIN - 0.75, row_h, item, size=size)

    def activity_slide(self):
        act = self.spec["activity"]
        s, where = self._slide("Activity: " + act["title"], notes=act.get("notes"))
        # Timing chip
        rounded(s, MARGIN, 1.65, 2.2, 0.5, self.area["accent"], radius=0.5)
        text(s, MARGIN, 1.65, 2.2, 0.5, act.get("time", "20 minutes"), size=14, bold=True,
             color=self.area["on_accent"], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(s, MARGIN + 2.4, 1.65, 5.2, 0.5, act.get("format", "Pairs"), size=14, italic=True,
             color=MUTED, anchor=MSO_ANCHOR.MIDDLE)
        steps = act["steps"]
        top = 2.45
        gap = 0.12
        row_h = min(0.95, (6.7 - top - gap * (len(steps) - 1)) / len(steps))
        for i, st in enumerate(steps):
            y = top + i * (row_h + gap)
            badge(s, MARGIN, y + (row_h - 0.42) / 2, 0.42, i + 1, BLUE, WHITE, size=13)
            size = fit_size([st], 6.5, row_h, 17, 11)
            if size is None:
                size = 11
                WARNINGS.append(f"{where}: activity step {i + 1} may overflow")
            text(s, MARGIN + 0.65, y, 6.5, row_h, st, size=size, anchor=MSO_ANCHOR.MIDDLE)
        rounded(s, 8.5, 1.65, 4.23, 5.0, ICE)
        text(s, 8.8, 1.9, 3.6, 0.4, "SUCCESS CRITERIA", size=13, bold=True, color=BLUE)
        bullet_list(s, 8.8, 2.45, 3.65, 4.0, act["success"], max_pt=18, min_pt=11,
                    where=where + " success criteria")

    def exit_slide(self):
        sp = self.spec
        page_url = SITE_URL + "#/" + sp.get("revise_page", sp["page"])
        s, where = self._slide("Exit ticket", notes=sp.get("exit_notes",
                               "Students answer on a sticky note or in the chat before leaving."),
                               dark=True)
        prompts = sp["exit"]
        top = 1.8
        for i, pr in enumerate(prompts):
            y = top + i * 1.05
            badge(s, MARGIN, y + 0.1, 0.55, i + 1, self.area["accent"], self.area["on_accent"], size=17)
            size = fit_size([pr], 7.2, 0.9, 20, 14) or 14
            text(s, MARGIN + 0.85, y, 7.2, 0.9, pr, size=size, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        rounded(s, 9.0, 1.8, 3.73, 3.2, BLUE)
        text(s, 9.3, 2.05, 3.2, 0.4, "REVISE THIS TOPIC", size=13, bold=True, color=SKY)
        text(s, 9.3, 2.5, 3.2, 0.6, "Revision notes for this lesson are on the study wiki:",
             size=14, color=WHITE)
        revise = sp.get("revise_title", sp["page_title"])
        size = fit_size([revise], 3.2, 1.6, 20, 13, char_w=0.55) or 13
        text(s, 9.3, 3.2, 3.2, 1.6, revise, size=size, bold=True, font=HEAD_FONT,
             color=WHITE)
        text(s, MARGIN, 6.2, W - 2 * MARGIN, 0.6, page_url, size=12, color=SKY)

    # -- content slide types
    def add(self, sl):
        kind = sl["type"]
        getattr(self, "_" + kind)(sl)

    def _bullets(self, sl):
        s, where = self._slide(sl["title"], sl.get("notes"))
        callout = sl.get("callout")
        width = 7.3 if callout else W - 2 * MARGIN
        bullet_list(s, MARGIN, 1.75, width, 5.0, sl["bullets"], where=where)
        if callout:
            rounded(s, 8.5, 1.75, 4.23, 4.85, NAVY)
            badge(s, 8.8, 2.05, 0.6, "!", self.area["accent"], self.area["on_accent"], size=20)
            text(s, 8.8, 2.85, 3.6, 0.4, "KEY IDEA", size=13, bold=True, color=SKY)
            size = fit_size([callout], 3.6, 3.3, 22, 13, char_w=0.52)
            if size is None:
                size = 13
                WARNINGS.append(f"{where}: callout may overflow")
            text(s, 8.8, 3.3, 3.6, 3.2, callout, size=size, font=HEAD_FONT, color=WHITE)

    def _cards(self, sl):
        s, where = self._slide(sl["title"], sl.get("notes"))
        cards = sl["cards"]
        n = len(cards)
        cols = {1: 1, 2: 2, 3: 3, 4: 2, 5: 3, 6: 3}.get(n, 3)
        rows = math.ceil(n / cols)
        gap = 0.3
        top = 1.75
        avail_w = W - 2 * MARGIN
        avail_h = H - 0.75 - top
        cw = (avail_w - gap * (cols - 1)) / cols
        ch = (avail_h - gap * (rows - 1)) / rows
        for i, (head, body) in enumerate(cards):
            r, c = divmod(i, cols)
            x = MARGIN + c * (cw + gap)
            y = top + r * (ch + gap)
            rounded(s, x, y, cw, ch, ICE, radius=0.06)
            badge(s, x + 0.25, y + 0.25, 0.5, i + 1, self.area["accent"], self.area["on_accent"], size=15)
            hsize = fit_size([head], cw - 1.05, 0.55, 19, 13, char_w=0.55) or 13
            text(s, x + 0.9, y + 0.22, cw - 1.1, 0.56, head, size=hsize, bold=True, color=NAVY,
                 anchor=MSO_ANCHOR.MIDDLE)
            bh = ch - 1.1
            size = fit_size([body], cw - 0.5, bh, 20, 10)
            if size is None:
                size = 10
                WARNINGS.append(f"{where}: card '{head}' may overflow")
            text(s, x + 0.25, y + 0.95, cw - 0.5, bh, body, size=size)

    def _process(self, sl):
        s, where = self._slide(sl["title"], sl.get("notes"))
        steps = sl["steps"]
        n = len(steps)
        caption = sl.get("caption")
        gap = 0.15
        avail_w = W - 2 * MARGIN
        sw = (avail_w - gap * (n - 1)) / n
        d = 0.7
        max_body = (3.9 if caption else 4.6) - 1.3
        # one size for every step so the row reads evenly
        size = min((fit_size([dt], sw - 0.3, max_body, 18, 10) or 10) for _, dt in steps)
        lsize = min((fit_size([lb], sw - 0.1, 0.75, 17, 10, char_w=0.55) or 10) for lb, _ in steps)
        need = max(
            _lines_needed(dt, sw - 0.3, size) * size * 1.2 / 72 for _, dt in steps
        )
        if need > max_body:
            WARNINGS.append(f"{where}: process step text may overflow")
        box_h = min(max_body, need + 0.15) + 0.3
        # centre the whole diagram in the content area
        block = d + 1.0 + box_h + (0.9 if caption else 0)
        top = max(1.85, 1.75 + (H - 0.75 - 1.75 - block) / 2)
        rect(s, MARGIN + sw / 2, top + d / 2 - 0.02, avail_w - sw, 0.04, SKY)
        box_y = top + d + 1.0
        for i, (label, detail) in enumerate(steps):
            x = MARGIN + i * (sw + gap)
            badge(s, x + (sw - d) / 2, top, d, i + 1, self.area["accent"], self.area["on_accent"], size=20)
            text(s, x, top + d + 0.15, sw, 0.8, label, size=lsize, bold=True, color=NAVY,
                 align=PP_ALIGN.CENTER)
            rounded(s, x, box_y, sw, box_h, ICE, radius=0.06)
            text(s, x + 0.15, box_y + 0.15, sw - 0.3, box_h - 0.3, detail, size=size)
        if caption:
            csize = fit_size([caption], avail_w, 0.6, 16, 12) or 12
            text(s, MARGIN, box_y + box_h + 0.3, avail_w, 0.6, caption, size=csize, italic=True,
                 color=MUTED)

    def _compare(self, sl):
        s, where = self._slide(sl["title"], sl.get("notes"))
        gap = 0.4
        cw = (W - 2 * MARGIN - gap) / 2
        top = 1.75
        for i, (head, items) in enumerate((sl["left"], sl["right"])):
            x = MARGIN + i * (cw + gap)
            head_bg = NAVY if i == 0 else BLUE
            rounded(s, x, top, cw, 0.7, head_bg, radius=0.15)
            hsize = fit_size([head], cw - 0.5, 0.6, 20, 13, char_w=0.55) or 13
            text(s, x + 0.25, top, cw - 0.5, 0.7, head, size=hsize, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE)
            rounded(s, x, top + 0.85, cw, H - 0.75 - top - 0.85, ICE, radius=0.04)
            bullet_list(s, x + 0.3, top + 1.1, cw - 0.6, H - 0.75 - top - 1.35, items,
                        max_pt=22, min_pt=11, where=f"{where} column {i + 1}")

    def _table(self, sl):
        s, where = self._slide(sl["title"], sl.get("notes"))
        header, rows = sl["header"], sl["rows"]
        ncols = len(header)
        top = 1.75
        avail_h = H - 0.8 - top - (0.6 if sl.get("caption") else 0)
        widths = sl.get("widths") or [1] * ncols
        total = sum(widths)
        col_w = [(W - 2 * MARGIN) * w / total for w in widths]
        # font size: fit the longest cell per column into its row height
        row_h = avail_h / (len(rows) + 1)
        size = 16
        while size > 10:
            ok = all(
                _lines_needed(str(cell), col_w[j] - 0.2, size) * size * 1.2 / 72 <= max(row_h, 0.4) - 0.1
                and max(len(w) for w in str(cell).split() or ["x"]) * size * 0.55 / 72 <= col_w[j] - 0.2
                for row in [header] + rows for j, cell in enumerate(row)
            )
            if ok:
                break
            size -= 1
        else:
            WARNINGS.append(f"{where}: table text small, may overflow")
        shape = s.shapes.add_table(len(rows) + 1, ncols, Inches(MARGIN), Inches(top),
                                   Inches(W - 2 * MARGIN), Inches(avail_h))
        tbl = shape.table
        for j, w in enumerate(col_w):
            tbl.columns[j].width = Inches(w)
        for i in range(len(rows) + 1):
            tbl.rows[i].height = Inches(avail_h / (len(rows) + 1))
        for i, row in enumerate([header] + rows):
            for j, val in enumerate(row):
                cell = tbl.cell(i, j)
                cell.fill.solid()
                cell.fill.fore_color.rgb = NAVY if i == 0 else (ICE if i % 2 == 0 else WHITE)
                cell.margin_left = cell.margin_right = Inches(0.1)
                cell.vertical_anchor = MSO_ANCHOR.MIDDLE
                tf = cell.text_frame
                tf.word_wrap = True
                p = tf.paragraphs[0]
                p.text = ""
                r = p.add_run()
                r.text = str(val)
                r.font.size = Pt(size)
                r.font.name = BODY_FONT
                r.font.bold = i == 0 or j == 0
                r.font.color.rgb = WHITE if i == 0 else (NAVY if j == 0 else TEXT)
        if sl.get("caption"):
            text(s, MARGIN, H - 1.25, W - 2 * MARGIN, 0.5, sl["caption"], size=13, italic=True, color=MUTED)

    def _terms(self, sl):
        s, where = self._slide(sl.get("title", "Key terms"), sl.get("notes"))
        terms = sl["terms"]
        cols = 2
        rows = math.ceil(len(terms) / cols)
        gap = 0.25
        top = 1.75
        cw = (W - 2 * MARGIN - gap) / cols
        rh = (H - 0.75 - top - gap * (rows - 1)) / rows
        for i, (term, definition) in enumerate(terms):
            r, c = divmod(i, cols)
            x = MARGIN + c * (cw + gap)
            y = top + r * (rh + gap)
            rounded(s, x, y, cw, rh, ICE, radius=0.08)
            size = fit_size([term + "  " + definition], cw - 0.5, rh - 0.2, 19, 10)
            if size is None:
                size = 10
                WARNINGS.append(f"{where}: term '{term}' may overflow")
            tb = text(s, x + 0.25, y + 0.1, cw - 0.5, rh - 0.2, "", size=size, anchor=MSO_ANCHOR.MIDDLE)
            p = tb.text_frame.paragraphs[0]
            p.runs[0].text = term
            p.runs[0].font.bold = True
            p.runs[0].font.color.rgb = NAVY
            r2 = p.add_run()
            r2.text = "  " + definition
            r2.font.size = Pt(size)
            r2.font.name = BODY_FONT
            r2.font.color.rgb = TEXT

    # -- whole deck
    def _explain(self, sl):
        """A text-led slide that explains the topic before its summary slide."""
        ex = sl["explain"]
        s, where = self._slide(sl["title"], ex.get("notes"))
        paras = [p.strip() for p in ex["text"].split("\n\n") if p.strip()]
        example = ex.get("example")
        width = 7.35 if example else W - 2 * MARGIN
        top, height = 1.7, H - 0.75 - 1.7
        size = fit_size(paras, width, height, 22, 12, spacing=0.6)
        if size is None:
            size = 12
            WARNINGS.append(f"{where}: explanation text may overflow")
        tb = s.shapes.add_textbox(Inches(MARGIN), Inches(top), Inches(width), Inches(height))
        tf = tb.text_frame
        tf.word_wrap = True
        for side in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
            setattr(tf, side, Inches(0))
        for i, para in enumerate(paras):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.space_after = Pt(size * 0.6)
            _add_rich(p, para, size, TEXT)
        if example:
            rounded(s, 8.5, top, 4.23, height - 0.1, NAVY)
            badge(s, 8.8, top + 0.3, 0.6, "e.g.", self.area["accent"], self.area["on_accent"], size=13)
            text(s, 8.8, top + 1.1, 3.6, 0.4, ex.get("example_label", "EXAMPLE"), size=13, bold=True, color=SKY)
            esize = fit_size([example], 3.6, height - 1.8, 19, 12, char_w=0.52)
            if esize is None:
                esize = 12
                WARNINGS.append(f"{where}: example may overflow")
            text(s, 8.8, top + 1.55, 3.6, height - 1.8, example, size=esize, font=HEAD_FONT, color=WHITE)

    def _check(self, sl):
        """Two or three quick questions straight after a topic; answers go in the notes."""
        qs = sl["check"]
        title = "Quick check: " + sl["title"]
        if len(title) > 60:
            title = "Quick check"
        notes = "Answers:\n" + "\n".join(f"{i + 1}. {a}" for i, (_, a) in enumerate(qs))
        s, where = self._slide(title, notes)
        gap = 0.25
        top = 1.8
        avail = H - 1.3 - top
        row_h = min(1.3, (avail - gap * (len(qs) - 1)) / len(qs))
        for i, (q, _) in enumerate(qs):
            y = top + i * (row_h + gap)
            badge(s, MARGIN, y + 0.05, 0.55, i + 1, self.area["accent"], self.area["on_accent"], size=16)
            size = fit_size([q], W - 2 * MARGIN - 0.9, row_h, 24, 14)
            if size is None:
                size = 14
                WARNINGS.append(f"{where}: check question {i + 1} may overflow")
            text(s, MARGIN + 0.9, y, W - 2 * MARGIN - 0.9, row_h, q, size=size)
        text(s, MARGIN, H - 1.1, W - 2 * MARGIN, 0.4,
             "Answer on mini whiteboards or in your book. Answers are in the speaker notes.",
             size=13, italic=True, color=MUTED)

    def build(self, path):
        self.title_slide()
        self.objectives_slide()
        for sl in self.spec["slides"]:
            if sl.get("explain"):
                self._explain(sl)
            self.add(sl)
            if sl.get("check"):
                self._check(sl)
        self.quiz_slides()
        self.activity_slide()
        self.exit_slide()
        self.prs.save(path)
        return self.count
