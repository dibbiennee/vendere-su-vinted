#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1800, 2700
BG      = (14, 68, 76)
BG2     = (10, 54, 61)
CREAM   = (242, 237, 227)
WHITE   = (255, 255, 255)
MINT    = (127, 199, 206)
SOFT    = (200, 224, 226)
TEAL    = (11, 118, 128)

S = "/System/Library/Fonts/Supplemental/"
F_HEAD  = S + "Trebuchet MS Bold.ttf"
F_HEADR = S + "Trebuchet MS.ttf"
F_SERIF = S + "Georgia Italic.ttf"
F_SERIFB= S + "Georgia Bold.ttf"
f = lambda p, s: ImageFont.truetype(p, s)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# fascia inferiore leggermente più scura, per profondità
d.rectangle([0, 1560, W, H], fill=BG2)

M = 170  # margine

def tracked(draw, xy, text, font, fill, tracking):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking
    return x

# ---- occhiello
tracked(d, (M, 300), "GUIDA OPERATIVA", f(F_HEAD, 40), MINT, 11)

# ---- titolo
ft = f(F_HEAD, 196)
d.text((M - 8, 430), "VENDERE", font=ft, fill=WHITE)
d.text((M - 8, 640), "SU VINTED", font=ft, fill=WHITE)

# ---- filetto
d.rectangle([M, 900, M + 190, 910], fill=MINT)

# ---- sottotitolo
fs = f(F_SERIF, 58)
for i, line in enumerate(["La guida completa per trasformare", "l'armadio in un business"]):
    d.text((M, 985 + i * 78), line, font=fs, fill=SOFT)

# ---- cartellino (layer ruotato)
tw, th = 620, 740
tag = Image.new("RGBA", (tw, th), (0, 0, 0, 0))
td = ImageDraw.Draw(tag)
cut = 128
td.polygon([(cut, 0), (tw, 0), (tw, th), (0, th), (0, cut)], fill=CREAM)
td.line([(0, cut), (cut, 0)], fill=(206, 197, 180), width=4)
# foro
hx, hy, r = 78, 78, 27
td.ellipse([hx - r, hy - r, hx + r, hy + r], fill=BG2, outline=(198, 188, 170), width=6)
# simbolo
fe = f(F_SERIFB, 300)
bb = td.textbbox((0, 0), "€", font=fe)
td.text(((tw - (bb[2] - bb[0])) / 2 - bb[0], (th - (bb[3] - bb[1])) / 2 - bb[1] + 40), "€",
        font=fe, fill=TEAL)
td.line([(140, th - 130), (tw - 140, th - 130)], fill=(216, 208, 192), width=4)

ang = -9
tag = tag.rotate(ang, expand=True, resample=Image.BICUBIC)
tx, ty = W - tag.width - 165, 1320
img.paste(tag, (tx, ty), tag)

# cordino: singola diagonale dal foro verso l'alto a sinistra
import math
hole = (tx + 118, ty + 128)
d.line([hole, (hole[0] - 330, hole[1] - 250)], fill=MINT, width=6)
d.ellipse([hole[0] - 340, hole[1] - 262, hole[0] - 316, hole[1] - 238], fill=MINT)

# ---- piede
d.rectangle([M, 2330, M + 90, 2337], fill=MINT)
tracked(d, (M, 2400), "EDIZIONE 2026", f(F_HEAD, 40), MINT, 9)
d.text((M, 2480), "15 capitoli · checklist operative · template pronti all'uso",
       font=f(F_HEADR, 38), fill=(150, 186, 190))

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cover.png")
img.save(out, dpi=(300, 300))
print("scritto:", out, img.size)
