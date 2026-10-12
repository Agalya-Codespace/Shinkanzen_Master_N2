"""Report Japanese fields that still contain kanji without furigana (proofreading aid)."""
import sys, re, json
sys.path.insert(0, __import__("os").path.dirname(__file__))
from build_day import RUBY_KEYS
K = re.compile(r"[㐀-鿿々]")
def walk(x, key=None, quiz=False):
    if isinstance(x, dict):
        q = quiz or (x.get("type") == "fill" and re.match(r"d\d+k-", x.get("id", "")))
        for k, v in x.items(): walk(v, k, q)
    elif isinstance(x, list):
        for v in x: walk(v, key, quiz)
    elif isinstance(x, str) and key in RUBY_KEYS:
        t = re.sub(r"\{[^{}|]+\|[^{}]+\}", "", x)
        if quiz: t = re.sub(r"\[\[.*?\]\]", "", t)
        t = re.sub(r"［[^］]*］", "", t)
        if K.search(t): print("  bare:", x[:90])
for f in sys.argv[1:]:
    s = open(f, encoding="utf-8").read()
    print(f)
    walk(json.loads(s[s.index("sections.push(") + 14: s.rindex(")")]))
