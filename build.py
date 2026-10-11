"""Rebuild the portable HTML after editing sketchbook.template.html or assets."""
from pathlib import Path
import base64
from PIL import Image

ROOT = Path(__file__).resolve().parent
def data_url(path, mime):
    return f"data:{mime};base64," + base64.b64encode((ROOT / path).read_bytes()).decode()

html = (ROOT / "sketchbook.template.html").read_text(encoding="utf-8")
web_html = html
web_dir = ROOT / "assets" / "web"
web_dir.mkdir(parents=True, exist_ok=True)
for token, path, mime in [
    ("FONT", "assets/fonts/Caveat.ttf", "font/ttf"),
    ("COVER", "assets/cover-author.png", "image/png"),
    ("BACK_COVER", "assets/back-cover.png", "image/png"),
    ("ROSES", "assets/roses.png", "image/png"),
    ("SUNLIGHT", "assets/sunlight.png", "image/png"),
    ("HAWK", "assets/hawk.png", "image/png"),
    ("TREE", "assets/tree.png", "image/png"),
]:
    html = html.replace(f"__{token}__", data_url(path, mime))
    if mime == "image/png":
        # Compress delivery assets; preserve the original PNG artwork and portable HTML.
        optimized = web_dir / (Path(path).stem + ".webp")
        with Image.open(ROOT / path) as original:
            image = original.convert("RGB")
            image.thumbnail((768, 1152), Image.Resampling.LANCZOS)
            image.save(optimized, "WEBP", quality=88, method=6)
        web_html = web_html.replace(f"__{token}__", f"assets/{optimized.name}")
    else:
        web_html = web_html.replace(f"__{token}__", data_url(path, mime))
# Retain the font license in the standalone artifact.
license_text = (ROOT / "assets/fonts/OFL.txt").read_text(encoding="utf-8")
html = html.replace("</head>", "<!-- Embedded Caveat font license:\n" + license_text + "\n-->\n</head>")
web_html = web_html.replace("</head>", "<!-- Embedded Caveat font license:\n" + license_text + "\n-->\n</head>")
(ROOT / "index.html").write_text(html, encoding="utf-8")
print(f"Built index.html ({len(html.encode()) / 1024 / 1024:.1f} MB)")
(ROOT / "web.html").write_text(web_html, encoding="utf-8")
web_bytes = len(web_html.encode()) + sum(p.stat().st_size for p in web_dir.glob("*.webp"))
print(f"Built web.html plus delivery artwork ({web_bytes / 1024 / 1024:.1f} MB total)")
