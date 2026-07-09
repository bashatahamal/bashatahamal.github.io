"""Generate the B. monogram favicon: deep green circle, Charter/Georgia 'B', gold dot.

Usage (needs Pillow: pip install pillow):
    python3 scripts/make_favicon.py
Writes favicon.ico, assets/v2/favicon-512.png, assets/v2/apple-touch-icon.png.
"""
import os
from PIL import Image, ImageDraw, ImageFont

GREEN = (14, 110, 85, 255)      # #0e6e55
GOLD = (161, 111, 11, 255)      # #a16f0b
PAPER = (250, 249, 247, 255)    # #faf9f7

S = 512
img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
d.ellipse([8, 8, S - 8, S - 8], fill=GREEN)

font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Bold.ttf", 330)
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

out = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
img.save(f"{out}/assets/v2/favicon-512.png")
img.resize((180, 180), Image.LANCZOS).save(f"{out}/assets/v2/apple-touch-icon.png")
img.save(f"{out}/favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
print("written")
