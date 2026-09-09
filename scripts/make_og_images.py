"""Generate 1200x630 social-share (og:image) cards for every project and post,
plus one default card for the homepage / writing index, from the design
system's og-image / og-image-project templates (light theme only, since a
static og:image can't respond to the viewer's color scheme).

Fonts are vendored in assets/v2/fonts/, so output is byte-reproducible across
machines; nothing is read from the host's font directories.

Usage (needs Pillow, fontTools, brotli, pyyaml):
    pip install pillow fonttools brotli pyyaml
    python3 scripts/make_og_images.py

Writes images/og/<slug>.png (projects), images/og/writing/<slug>.png (posts),
images/og/default.png (homepage / writing index fallback). Rerun any time a
project/post title, summary, tags, or date changes; the front matter's
`ogImage:` field points at the resulting file and does not need to change.
"""
import glob
import io
import os
import re
import yaml
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.path.join(ROOT, "assets", "v2", "fonts")

W, H = 1200, 630
PAD_X, PAD_Y = 84, 72
CONTENT_W = W - 2 * PAD_X

BG = (250, 249, 247, 255)
INK = (29, 28, 26, 255)
DEK = (85, 83, 77, 255)
KICKER = (10, 90, 70, 255)
GOLD = (161, 111, 11, 255)
TAG_BORDER = (227, 224, 217, 255)
TAG_TEXT = (85, 83, 77, 255)
DOMAIN = (128, 124, 116, 255)
DOT_GREEN = (14, 110, 85, 255)

DOMAIN_TEXT = "bashatahamal.github.io"


# ------------------------------------------------------------------- fonts

def _woff2_to_ttf_bytes(path):
    from fontTools.ttLib import TTFont
    font = TTFont(path)
    font.flavor = None
    buf = io.BytesIO()
    font.save(buf)
    buf.seek(0)
    return buf


_CHARTER_CACHE = {}


def charter(size, bold=False):
    key = ("bold" if bold else "regular", size)
    if key not in _CHARTER_CACHE:
        name = "charter_bold.woff2" if bold else "charter_regular.woff2"
        buf = _woff2_to_ttf_bytes(os.path.join(FONT_DIR, name))
        _CHARTER_CACHE[key] = ImageFont.truetype(buf, size)
    return _CHARTER_CACHE[key]


# Monospace is vendored (assets/v2/fonts/CascadiaMono.ttf) rather than probed
# from the host, so these cards render identically on Windows, macOS, Linux and
# in the Docker container. Probing used to pick Consolas / Menlo / DejaVu Sans
# Mono depending on where the script ran, which silently rewrote every card's
# metadata row whenever it was regenerated somewhere new.
#
# The file is Microsoft's Cascadia Mono, shipped unmodified under the SIL Open
# Font License (see "Cascadia Mono license.txt" beside it). It is a variable
# font, so the weights come from its named instances. Note this font is used
# ONLY here, for rendering these PNGs; the site itself keeps the system mono
# stack that the design system calls for.
MONO_FILE = "CascadiaMono.ttf"

_MONO_CACHE = {}


def mono(size, bold=False):
    key = ("bold" if bold else "regular", size)
    if key not in _MONO_CACHE:
        path = os.path.join(FONT_DIR, MONO_FILE)
        if not os.path.exists(path):
            raise SystemExit(
                "Missing vendored monospace font: %s. "
                "It should be committed alongside the Charter woff2 files." % path
            )
        font = ImageFont.truetype(path, size)
        font.set_variation_by_name("Bold" if bold else "Regular")
        _MONO_CACHE[key] = font
    return _MONO_CACHE[key]


# -------------------------------------------------------------------- text

def wrap(draw, text, font, max_width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if not cur or draw.textlength(trial, font=font) <= max_width:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_title(draw, text, max_width, start_size, min_size, max_lines, bold=True):
    size = start_size
    while size >= min_size:
        font = charter(size, bold=bold)
        lines = wrap(draw, text, font, max_width)
        if len(lines) <= max_lines:
            return font, lines
        size -= 4
    font = charter(min_size, bold=bold)
    lines = wrap(draw, text, font, max_width)[:max_lines]
    last, ell = lines[-1], "…"
    while draw.textlength(last + ell, font=font) > max_width and len(last) > 1:
        last = last[:-1]
    lines[-1] = last.rstrip() + ell
    return font, lines


def line_height(font):
    ascent, descent = font.getmetrics()
    return ascent + descent


# ------------------------------------------------------------------- card

def draw_kicker(draw, cursor_y, text):
    font = mono(22, bold=True)
    text_w = draw.textlength(text, font=font)
    draw.rectangle([PAD_X, cursor_y, PAD_X + text_w, cursor_y + 2], fill=GOLD)
    y = cursor_y + 2 + 18
    draw.text((PAD_X, y), text, font=font, fill=KICKER)
    return y + line_height(font)


def draw_title(draw, cursor_y, lines, font):
    lh = line_height(font)
    for line in lines:
        draw.text((PAD_X, cursor_y), line, font=font, fill=INK)
        cursor_y += int(lh * 1.12)
    return cursor_y


def draw_dek(draw, cursor_y, lines, font):
    lh = line_height(font)
    for line in lines:
        draw.text((PAD_X, cursor_y), line, font=font, fill=DEK)
        cursor_y += int(lh * 1.3)
    return cursor_y


def draw_tags(draw, cursor_y, tags):
    font = mono(19, bold=True)
    x = PAD_X
    pad_x, pad_y, gap, radius = 20, 8, 12, 999
    bottom = cursor_y
    for tag in tags[:3]:
        label = tag.upper()
        tw = draw.textlength(label, font=font)
        th = line_height(font)
        box = [x, cursor_y, x + tw + 2 * pad_x, cursor_y + th + 2 * pad_y]
        draw.rounded_rectangle(box, radius=radius, outline=TAG_BORDER, width=2)
        draw.text((x + pad_x, cursor_y + pad_y), label, font=font, fill=TAG_TEXT)
        x = box[2] + gap
        bottom = box[3]
    return bottom


def draw_footer(draw):
    name_font = charter(40, bold=True)
    dot_font = charter(40, bold=True)
    domain_font = mono(20)
    y = H - PAD_Y - line_height(name_font)
    draw.text((PAD_X, y), "Basha", font=name_font, fill=INK)
    name_w = draw.textlength("Basha", font=name_font)
    draw.text((PAD_X + name_w, y), ".", font=dot_font, fill=DOT_GREEN)
    domain_w = draw.textlength(DOMAIN_TEXT, font=domain_font)
    draw.text((W - PAD_X - domain_w, y + 10), DOMAIN_TEXT, font=domain_font, fill=DOMAIN)


def make_card(kicker_text, title_text, dek_text=None, tags=None):
    img = Image.new("RGB", (W, H), BG[:3])
    draw = ImageDraw.Draw(img)

    cursor = PAD_Y
    cursor = draw_kicker(draw, cursor, kicker_text)
    cursor += 28

    has_dek = bool(dek_text)
    title_font, title_lines = fit_title(
        draw, title_text, CONTENT_W,
        start_size=84 if has_dek else 76,
        min_size=48,
        max_lines=2 if has_dek else 3,
    )
    cursor = draw_title(draw, cursor, title_lines, title_font)

    if dek_text:
        cursor += 20
        dek_font = charter(32, bold=False)
        full_dek_lines = wrap(draw, dek_text, dek_font, CONTENT_W)
        dek_lines = full_dek_lines[:3]
        if len(full_dek_lines) > 3:
            last, ell = dek_lines[-1], "…"
            while draw.textlength(last + ell, font=dek_font) > CONTENT_W and len(last) > 1:
                last = last[:-1]
            dek_lines[-1] = last.rstrip() + ell
        cursor = draw_dek(draw, cursor, dek_lines, dek_font)

    if tags:
        cursor += 32
        draw_tags(draw, cursor, tags)

    draw_footer(draw)
    return img


# --------------------------------------------------------------- front matter

def read_front_matter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    return yaml.safe_load(m.group(1)) or {}


# -------------------------------------------------------------------- main

def main():
    og_dir = os.path.join(ROOT, "images", "og")
    writing_dir = os.path.join(og_dir, "writing")
    os.makedirs(writing_dir, exist_ok=True)

    for path in sorted(glob.glob(os.path.join(ROOT, "projects", "*.md"))):
        fm = read_front_matter(path)
        # rstrip: project permalinks end in a slash (projects/berning/) so that
        # both URL forms resolve; without this the slug comes back empty.
        slug = fm["permalink"].rstrip("/").split("/")[-1]
        card = make_card(
            kicker_text=f"Work · {fm['date']}",
            title_text=fm["title"],
            dek_text=fm.get("summary"),
            tags=fm.get("labels"),
        )
        out = os.path.join(og_dir, f"{slug}.png")
        card.save(out)
        print("wrote", os.path.relpath(out, ROOT))

    for path in sorted(glob.glob(os.path.join(ROOT, "_posts", "*.md"))):
        fm = read_front_matter(path)
        basename = os.path.basename(path)
        slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", basename)[:-3]
        card = make_card(
            kicker_text=f"Writing · {fm['date']}",
            title_text=fm["title"],
        )
        out = os.path.join(writing_dir, f"{slug}.png")
        card.save(out)
        print("wrote", os.path.relpath(out, ROOT))

    default_card = make_card(
        kicker_text="Software Engineer, AI/LLM Systems",
        title_text="Basha Tahamal",
    )
    out = os.path.join(og_dir, "default.png")
    default_card.save(out)
    print("wrote", os.path.relpath(out, ROOT))


if __name__ == "__main__":
    main()
