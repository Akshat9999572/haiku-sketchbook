"""Rebuild the portable HTML after editing sketchbook.template.html or assets."""
from pathlib import Path
import base64

ROOT = Path(__file__).resolve().parent
def data_url(path, mime):
    return f"data:{mime};base64," + base64.b64encode((ROOT / path).read_bytes()).decode()

html = (ROOT / "sketchbook.template.html").read_text(encoding="utf-8")
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
# Retain the font license in the standalone artifact.
license_text = (ROOT / "assets/fonts/OFL.txt").read_text(encoding="utf-8")
html = html.replace("</head>", "<!-- Embedded Caveat font license:\n" + license_text + "\n-->\n</head>")
(ROOT / "index.html").write_text(html, encoding="utf-8")
print(f"Built index.html ({len(html.encode()) / 1024 / 1024:.1f} MB)")
