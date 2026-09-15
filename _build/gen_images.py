#!/usr/bin/env python3
"""Generates every image the template references: favicon set at root paths,
author avatars, casino logo wordmarks, OG image and the org logo."""
from PIL import Image, ImageDraw, ImageFont
import os, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "images")
os.makedirs(os.path.join(IMG, "authors"), exist_ok=True)
os.makedirs(os.path.join(IMG, "casino-logos"), exist_ok=True)

NAVY = (14, 23, 41, 255); NAVY2 = (30, 42, 68, 255)
GOLD = (233, 185, 73, 255); WHITE = (255, 255, 255, 255)
MUT = (159, 176, 212, 255)

def font(sz, bold=True):
    for p in ("/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
              "/System/Library/Fonts/Helvetica.ttc",
              "/Library/Fonts/Arial.ttf"):
        if os.path.exists(p):
            try: return ImageFont.truetype(p, sz)
            except Exception: pass
    return ImageFont.load_default()

def centre(d, box, text, f, fill):
    x0, y0, x1, y1 = box
    l, t, r, b = d.textbbox((0, 0), text, font=f)
    d.text((x0 + (x1-x0-(r-l))/2 - l, y0 + (y1-y0-(b-t))/2 - t), text, font=f, fill=fill)

# ---------------------------------------------------------------- favicon
S = 768
fav = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(fav)
d.rounded_rectangle((0, 0, S-1, S-1), radius=int(S*.22), fill=NAVY)
# two gold chevrons + white triangle — the template's logo mark
sw = int(S*.085)
for dx in (0.10, 0.34):
    d.line([(S*dx, S*.24), (S*(dx+0.20), S*.5), (S*dx, S*.76)], fill=GOLD, width=sw, joint="curve")
d.polygon([(S*.60, S*.20), (S*.90, S*.5), (S*.60, S*.80)], fill=WHITE)
for sz in (16, 32, 48, 96, 144, 192, 512):
    fav.resize((sz, sz), Image.LANCZOS).save(os.path.join(ROOT, f"favicon-{sz}x{sz}.png"))
fav.resize((180, 180), Image.LANCZOS).save(os.path.join(ROOT, "apple-touch-icon.png"))
fav.resize((64, 64), Image.LANCZOS).save(os.path.join(ROOT, "favicon.ico"),
                                          sizes=[(16,16),(32,32),(48,48),(64,64)])
open(os.path.join(ROOT, "favicon.svg"), "w").write(
 '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 192 192" role="img" aria-label="CasinoKiwi">'
 '<rect width="192" height="192" rx="42" fill="#0E1729"/>'
 '<path d="M19 46 L58 96 L19 146" fill="none" stroke="#E9B949" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>'
 '<path d="M65 46 L104 96 L65 146" fill="none" stroke="#E9B949" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>'
 '<path d="M115 38 L173 96 L115 154 Z" fill="#ffffff"/></svg>')

# ---------------------------------------------------------------- org logo 400x120
logo = Image.new("RGBA", (400, 120), NAVY)
d = ImageDraw.Draw(logo)
for dx in (14, 52):
    d.line([(dx, 34), (dx+26, 60), (dx, 86)], fill=GOLD, width=11, joint="curve")
d.polygon([(100, 30), (140, 60), (100, 90)], fill=WHITE)
d.text((158, 34), "CASINO", font=font(30), fill=WHITE)
d.text((158, 68), "KIWI", font=font(30), fill=GOLD)
logo.save(os.path.join(IMG, "logo.png"))

# ---------------------------------------------------------------- OG 1200x630
og = Image.new("RGBA", (1200, 630), NAVY)
d = ImageDraw.Draw(og)
d.rectangle((0, 0, 1200, 8), fill=GOLD)
for dx in (70, 128):
    d.line([(dx, 70), (dx+40, 110), (dx, 150)], fill=GOLD, width=17, joint="curve")
d.polygon([(198, 62), (258, 110), (198, 158)], fill=WHITE)
d.text((70, 230), "Best Online Casinos NZ", font=font(72), fill=WHITE)
d.text((70, 320), "Tested with real NZD deposits", font=font(46), fill=GOLD)
d.text((70, 400), "Payout speed · NZD banking · honest bonus terms", font=font(32, False), fill=MUT)
d.text((70, 540), "casinokiwi.co.nz  ·  18+  ·  Gamble responsibly", font=font(26, False), fill=MUT)
og.convert("RGB").save(os.path.join(IMG, "og-casinokiwi.jpg"), quality=88)

# Author avatars are real photographs in images/authors/ — not generated here.
print("images: favicons + org logo + OG image")
