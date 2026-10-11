"""Generate the favicon, app icons and Open Graph image for angardigital.com.

Usage (from the repository root):
    python3 tools/generate_images.py

Requires Pillow (pip install Pillow). Outputs are written to the site root and assets/img/.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "tools" / "fonts"
IMG = ROOT / "assets" / "img"

BG = "#f7f5f0"
TEXT = "#191a17"
MUTED = "#55554e"
LINE = "#e2ded3"
ACCENT = "#1d5c47"

DISPLAY = FONTS / "Fraunces-144-SemiBold.ttf"
DISPLAY_MEDIUM = FONTS / "Fraunces-72-Medium.ttf"
BODY = FONTS / "HankenGrotesk-Medium.ttf"


def icon(size: int, rounded: bool = True) -> Image.Image:
    """Accent square with a cream 'A', drawn at 4x and downsampled for clean edges."""
    s = size * 4
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if rounded:
        d.rounded_rectangle((0, 0, s - 1, s - 1), radius=int(s * 0.22), fill=ACCENT)
    else:
        d.rectangle((0, 0, s, s), fill=ACCENT)
    font = ImageFont.truetype(str(DISPLAY), int(s * 0.72))
    left, top, right, bottom = d.textbbox((0, 0), "A", font=font)
    x = (s - (right - left)) / 2 - left
    y = (s - (bottom - top)) / 2 - top
    d.text((x, y), "A", font=font, fill=BG)
    return img.resize((size, size), Image.LANCZOS)


def diamond(d: ImageDraw.ImageDraw, cx: float, cy: float, r: float) -> None:
    d.polygon([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], fill=ACCENT)


def og_image() -> Image.Image:
    w, h = 1200, 630
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    pad = 80

    # Wordmark
    mark_font = ImageFont.truetype(str(DISPLAY), 40)
    diamond(d, pad + 13, pad + 24, 13)
    d.text((pad + 40, pad), "Angar", font=mark_font, fill=TEXT)
    aw = d.textlength("Angar ", font=mark_font)
    d.text((pad + 40 + aw, pad), "Digital", font=ImageFont.truetype(str(DISPLAY_MEDIUM), 40), fill=MUTED)

    # Headline
    head_font = ImageFont.truetype(str(DISPLAY_MEDIUM), 76)
    lines = [("We design and publish", TEXT), ("mobile apps", ACCENT), ("and online products.", TEXT)]
    y = 215
    for text, color in lines:
        d.text((pad, y), text, font=head_font, fill=color)
        y += 88

    # Footer line
    d.line((pad, h - 110, w - pad, h - 110), fill=LINE, width=2)
    small = ImageFont.truetype(str(BODY), 26)
    d.text((pad, h - 88), "Digital products studio", font=small, fill=MUTED)
    url = "angardigital.com"
    d.text((w - pad - d.textlength(url, font=small), h - 88), url, font=small, fill=MUTED)
    return img


def main() -> None:
    IMG.mkdir(parents=True, exist_ok=True)
    icon(32).save(IMG / "favicon-32.png")
    icon(192).save(IMG / "icon-192.png")
    icon(512).save(IMG / "icon-512.png")
    # iOS applies its own rounded mask, so the touch icon is a full square.
    icon(180, rounded=False).convert("RGB").save(ROOT / "apple-touch-icon.png")
    icon(48).save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    og_image().save(IMG / "og-image.png", optimize=True)
    print("Images generated.")


if __name__ == "__main__":
    main()
