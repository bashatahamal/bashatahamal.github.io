"""Generate the B. monogram favicon: deep green circle, Newsreader 'B', gold dot.

Usage (needs Pillow + fontTools + brotli: pip install pillow fonttools brotli):
    python3 scripts/make_favicon.py
Writes favicon.ico, assets/v2/favicon-512.png, assets/v2/apple-touch-icon.png.

Uses the repo's own self-hosted assets/v2/fonts/newsreader_600.woff2 (converted
to TTF in-memory) rather than an OS font path, so this runs the same on any
platform.
"""
import io
import os
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

GREEN = (14, 110, 85, 255)      # #0e6e55
GOLD = (161, 111, 11, 255)      # #a16f0b
PAPER = (250, 249, 247, 255)    # #faf9f7

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_display_font(size):
    src = os.path.join(ROOT, "assets", "v2", "fonts", "newsreader_600.woff2")
    ttf = TTFont(src)
    ttf.flavor = None
    buf = io.BytesIO()
    ttf.save(buf)
    buf.seek(0)
    return ImageFont.truetype(buf, size)


S = 512
img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
d.ellipse([8, 8, S - 8, S - 8], fill=GREEN)

font = load_display_font(330)
# Letter B centered, nudged left to leave room for the gold dot
bbox = d.textbbox((0, 0), "B", font=font)
w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
x = (S - w) / 2 - bbox[0] - 30
y = (S - h) / 2 - bbox[1] - 8
d.text((x, y), "B", font=font, fill=PAPER)

# Gold period after the B, sitting on the baseline
dot_r = 34
dot_cx = x + w + 62
dot_cy = y + bbox[3] - dot_r
d.ellipse([dot_cx - dot_r, dot_cy - dot_r, dot_cx + dot_r, dot_cy + dot_r], fill=GOLD)

img.save(f"{ROOT}/assets/v2/favicon-512.png")
img.resize((180, 180), Image.LANCZOS).save(f"{ROOT}/assets/v2/apple-touch-icon.png")
img.save(f"{ROOT}/favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
print("written")
