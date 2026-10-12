"""Build data/dayNN-BOOK.js from tools/src/dNN_BOOK.py, adding furigana to Japanese text fields.
Usage: python3 tools/build_day.py tools/src/d02_kanji.py [...]
Each source module defines DAY (int), TITLE (str, optional), INTRO (optional) and SECTION (dict with book/title/source/blocks)."""
import sys, json, runpy, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).parent))
sys.path.insert(0, str(pathlib.Path(__file__).parent / "src"))
from furi import furi

RUBY_KEYS = {"t", "q", "opts", "options", "left", "title", "lead", "paras", "answers", "sub", "meaning", "form",
             "caution", "label", "jp", "ng", "ok", "intro_jp"}
def walk(x, key=None, quiz=False):
    if isinstance(x, dict):
        q = quiz or bool(x.get("noRubyU")) or (x.get("type") == "fill" and re.match(r"d\d+k-", x.get("id", "")))
        return {k: walk(v, k, q) for k, v in x.items() if k != "noRubyU"}
    if isinstance(x, list):
        return [walk(v, key, quiz) for v in x]
    if isinstance(x, str) and key in RUBY_KEYS:
        return furi(x, skip_underlined=quiz)
    return x

def kana_of(rubied):
    t = re.sub(r"\{([^{}|]+)\|([^{}]+)\}", r"\2", rubied)
    return re.sub(r"\[\[|\]\]|\*\*", "", t)

def add_kana(x):
    """Teach examples without a hand-written 'kana' get one from the reviewed furigana."""
    if isinstance(x, dict):
        if "jp" in x and "th" in x and "kana" not in x:
            x["kana"] = kana_of(x["jp"])
        for v in x.values(): add_kana(v)
    elif isinstance(x, list):
        for v in x: add_kana(v)
    return x

root = pathlib.Path(__file__).resolve().parent.parent
for src in (sys.argv[1:] if __name__ == "__main__" else []):
    m = runpy.run_path(src)
    day, sec = m["DAY"], add_kana(walk(m["SECTION"]))
    head = {"title": m.get("TITLE", ""), "intro": m.get("INTRO", ""), "sections": []}
    out = root / "data" / ("day%02d-%s.js" % (day, sec["book"]))
    js = ("/* Day %d · %s. Built from %s by tools/build_day.py (furigana added automatically). */\n"
          "window.N2_DAYS = window.N2_DAYS || {};\n"
          "window.N2_DAYS[%d] = window.N2_DAYS[%d] || %s;\n"
          "if (%s) window.N2_DAYS[%d].title = %s;\n"
          "if (%s) window.N2_DAYS[%d].intro = %s;\n"
          "window.N2_DAYS[%d].sections.push(%s);\n") % (
        day, sec["book"], pathlib.Path(src).name, day, day, json.dumps(head, ensure_ascii=False),
        json.dumps(bool(head["title"])), day, json.dumps(head["title"], ensure_ascii=False),
        json.dumps(bool(head["intro"])), day, json.dumps(head["intro"], ensure_ascii=False),
        day, json.dumps(sec, ensure_ascii=False, indent=1))
    out.write_text(js, encoding="utf-8")
    print("wrote", out.relative_to(root))
