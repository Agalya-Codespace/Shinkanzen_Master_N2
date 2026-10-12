"""Bundle the site into one self-contained HTML file (for sharing a preview).
Usage: python3 tools/build_preview.py OUT.html [AUDIO_MAP.json]
AUDIO_MAP.json optionally maps site audio paths (audio/kanji/cd01.mp3) to hosted URLs.
The output has no <html>/<head>/<body> wrapper, because the preview host adds its own."""
import json, re, sys, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
index = (root / "index.html").read_text(encoding="utf-8")
css = (root / "css/style.css").read_text(encoding="utf-8")
scripts = re.findall(r'<script src="([^"]+)"></script>', index)
fonts = re.search(r'<link rel="stylesheet" href="(https://fonts[^"]+)">', index).group(1)
header = re.search(r'(<header.*?</header>)', index, re.S).group(1)

parts = [
    "<title>Shinkanzen N2 · 20 Days</title>",
    '<link rel="stylesheet" href="%s">' % fonts,
    "<style>\n%s\n</style>" % css,
    header,
    '<main id="main"></main>',
]
audio_map = json.loads(pathlib.Path(sys.argv[2]).read_text()) if len(sys.argv) > 2 else {}
for s in scripts:
    js = (root / s).read_text(encoding="utf-8")
    for path, url in audio_map.items():
        js = js.replace('"%s"' % path, json.dumps(url))
    parts.append("<script>\n%s\n</script>" % js)
pathlib.Path(sys.argv[1]).write_text("\n".join(parts), encoding="utf-8")
print("wrote", sys.argv[1])
