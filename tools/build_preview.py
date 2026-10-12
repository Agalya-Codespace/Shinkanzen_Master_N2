"""Bundle the site into one self-contained HTML file (for sharing a preview).
Usage: python3 tools/build_preview.py OUT.html
The output has no <html>/<head>/<body> wrapper, because the preview host adds its own."""
import re, sys, pathlib

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
for s in scripts:
    parts.append("<script>\n%s\n</script>" % (root / s).read_text(encoding="utf-8"))
pathlib.Path(sys.argv[1]).write_text("\n".join(parts), encoding="utf-8")
print("wrote", sys.argv[1])
