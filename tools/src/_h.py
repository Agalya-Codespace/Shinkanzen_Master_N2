"""Helpers for writing day sources compactly."""
CIRC = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮"

def fill(id, q, ans, explain="", suffix=None, prefix=None, note=None):
    b = {"type": "fill", "id": id, "q": q, "ans": ans if isinstance(ans, list) else [ans]}
    if suffix: b["suffix"] = suffix
    if prefix: b["prefix"] = prefix
    if note: b["ansNote"] = note
    if explain: b["explain"] = explain
    return b

def mcq(id, q, opts, ans, explain="", keys=None):
    b = {"type": "mcq", "id": id, "q": q, "opts": opts, "ans": ans, "keys": keys or ["1", "2", "3", "4"][:len(opts)]}
    if explain: b["explain"] = explain
    return b

def group(title, children, lead=None, explain=None, scored=True):
    b = {"type": "group", "title": title, "children": children, "scored": scored}
    if lead: b["lead"] = lead
    if explain: b["explain"] = explain
    return b

def text(t, title=None, explain=None):
    b = {"type": "text", "t": t}
    if title: b["title"] = title
    if explain: b["explain"] = explain
    return b

def items(title, its, lead=None, explain=None):
    b = {"type": "items", "title": title, "items": [i if isinstance(i, dict) else {"t": i[0], "explain": i[1]} for i in its]}
    if lead: b["lead"] = lead
    if explain: b["explain"] = explain
    return b

def wordlist(title, groups, lead, explain=None):
    b = {"type": "wordlist", "title": title, "lead": lead, "groups": [{"h": h, "words": w} for h, w in groups]}
    if explain: b["explain"] = explain
    return b

def kanji_round(day, n, cd, counts, answers, fills, table_note=None, explain=None):
    """One 第n回 page of the Kanji book: CD dictation + Ⅱ reading/writing."""
    assert len(counts) == len(answers)
    blocks = [{
        "type": "dictation", "id": "k%d" % n, "title": "第%d回" % n,
        "lead": "Ⅰ　ＣＤを聞いて、指示された数の漢字を使って文を書きなさい。数字も漢字で書きます。CD%d" % cd,
        "audio": "audio/kanji/cd%02d.mp3" % cd, "audioLabel": "CD %d · 漢字 N2" % cd,
        "counts": counts, "answers": answers,
        "note": "Each sentence is read twice. Type it, press Check, or open Answer. Model answers come from the CD and use exactly the number of kanji the book asks for.",
    }]
    if explain: blocks[0]["explain"] = explain
    blocks.append(group("第%d回　Ⅱ　＿＿の部分の漢字には読み仮名を、平仮名には漢字を（送り仮名も）書きなさい。" % n, fills,
                        lead=table_note or "Underlined kanji → type the reading. Underlined hiragana → type the kanji (with okurigana)."))
    return blocks

def match(id, label, options, pairs, explain=""):
    """連語 matching: pairs = [(left, option_index)]."""
    b = {"type": "select", "id": id, "q": label, "options": options, "items": [{"left": l, "ans": a} for l, a in pairs]}
    if explain: b["explain"] = explain
    return b

def choose(id, q, opts, ans, explain=""):
    """Choose from a small word box (no number keys)."""
    return mcq(id, q, opts, ans, explain, keys=[""] * len(opts))

def goi_drills(p, intro_story, intro_fills, renngo, imi, ruigi, gokeisei, jissen):
    """Standard Ⅱ 基本練習 + Ⅲ 実践練習 blocks of a Goi 課 (p = id prefix like 'd2g2')."""
    return [
        group("Ⅱ．基本練習　■1 導入練習", intro_fills,
              lead="言葉と例文の中から適当なものを（　）に入れて、文を完成させなさい。始め、または終わりの何文字かはヒントとして示してあります。（Type the whole word, kanji or hiragana.）",
              explain=intro_story),
        group("■2 連語　語と語のつながりや使い方を覚えよう。", renngo, lead="例のように適当な言葉を線で結びなさい。"),
        group("■3 意味　基本的な意味を確認しよう。", imi, lead="［　］の中から適当な言葉を選んで、（　）に入れなさい。"),
        group("■4 類義　似た意味の言葉はどれですか。", ruigi, lead="＿＿の言葉に意味が近いほうを選びなさい。"),
        group("■5 語形成　接辞や複合語を覚えよう。", gokeisei, lead="正しいものに○を付けなさい。"),
        group("Ⅲ．実践練習　／20点", jissen, lead="JLPT-style. Choose from 1・2・3・4."),
    ]

ABC = ["a", "b", "c"]

def bq(id, q, opts, ans, explain=""):
    """Bunpo a/b/c question."""
    return mcq(id, q, opts, ans, explain, keys=ABC[:len(opts)] if len(opts) <= 3 else ["a", "b", "c", "d"])

def ex(jp, th):
    return {"jp": jp, "th": th}

def gram(no, id, title, meaning, intro, pattern, exs, wrong, check, explain, examples, form, caution, tag=None):
    """A grammar point: Sensei's teach panel first, then the book's meaning/examples/接続/注意.
    wrong = [(ng, ok, th)], check = [(q, opts, ans, explain)], examples = [(t, explain)]."""
    b = {"type": "grammar", "no": str(no), "id": id,
         "teach": {"intro": intro, "pattern": pattern, "examples": exs,
                   "wrong": [{"ng": a, "ok": b_, "th": c} for a, b_, c in wrong],
                   "check": [{"q": q, "opts": o, "ans": a, "explain": e, "keys": ABC[:len(o)]} for q, o, a, e in check]},
         "title": title, "meaning": meaning,
         "explain": explain if isinstance(explain, list) else [explain],
         "examples": [{"t": t, "explain": e} for t, e in examples],
         "form": form, "caution": caution}
    if tag: b["tag"] = tag
    return b

def audio(title, track, t=None, label=None, tts=True, note=None):
    """Chokai track block. track like 'a03' or 'b12'."""
    b = {"type": "audio", "title": title, "src": "audio/chokai/%s.mp3" % track,
         "label": label or ("%s · computer read-aloud of the book script" % track.upper() if tts else "CD %s" % track.upper())}
    if t: b["t"] = t
    if note: b["note"] = note
    return b

def script(label, lines, title="◆スクリプト", lead="Tap 💡 on each line: sensei explains it.", extra=None):
    """Reveal with a script: lines = [(jp, thanglish)]; extra = more blocks inside (answer explanation)."""
    ch = [{"type": "items", "title": title, "lead": lead, "items": [{"t": a, "explain": b} for a, b in lines]}]
    return {"type": "reveal", "label": label, "children": ch + (extra or [])}
