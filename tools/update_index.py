"""Rewrite the <script> list in index.html to load every data/dayNN-*.js file."""
import pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
order = ["kanji", "goi", "bunpo", "dokkai", "chokai"]
files = sorted(root.glob("data/day*-*.js"), key=lambda p: (p.name[:5], order.index(p.stem.split("-")[1])))
tags = "\n".join('<script src="data/%s"></script>' % p.name for p in files)
html = (root / "index.html").read_text(encoding="utf-8")
html = re.sub(r'<script src="data/plan.js"></script>.*?<script src="js/app.js"></script>',
              '<script src="data/plan.js"></script>\n' + tags + '\n<script src="js/app.js"></script>', html, flags=re.S)
(root / "index.html").write_text(html, encoding="utf-8")
print(len(files), "data files")
