"""Add {漢字|かな} furigana markup to plain Japanese with Open JTalk's dictionary (pip install pyopenjtalk).
Text already inside {..|..} is left alone, so a hand-written reading always wins.
[[..]] and **..** markers are kept."""
import re, pyopenjtalk

KANJI = r"[㐀-鿿々〆ヶ]"
JP = re.compile(r"[㐀-鿿々〆ヶぁ-んァ-ヺ]")
NUM = re.compile(r"[〇一二三四五六七八九十百千万]")
def kata2hira(s): return "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in s)

def ruby_word(surface, reading):
    """Split one dictionary word into kanji runs with readings, keeping okurigana as plain text."""
    if not re.search(KANJI, surface): return surface
    parts = re.findall(KANJI + "+|[^㐀-鿿々〆ヶ]+", surface)
    pat = "".join("(.+?)" if re.match(KANJI, p) else "(" + re.escape(kata2hira(p)) + ")" for p in parts)
    m = re.fullmatch(pat, reading)
    if not m: return "{%s|%s}" % (surface, reading)
    return "".join("{%s|%s}" % (p, g) if re.match(KANJI, p) else p for p, g in zip(parts, m.groups()))

FIX = {"語": "ご", "静": "しず", "次": "つぎ", "夜": "よる", "日本": "にほん", "日本人": "にほんじん", "日本語": "にほんご"}

def furi_plain(text):
    """Annotate with the full sentence as context. Each Open JTalk word is located in the original
    text (within a small window); anything it normalised (digits, ASCII symbols) is copied through plain."""
    nodes = pyopenjtalk.run_frontend(text)
    fw = lambda x: "".join("\u3000" if c == " " else chr(ord(c) + 0xFEE0) if "!" <= c <= "~" else c for c in x)
    ntext = fw(text)  # same length as text; Open JTalk reports ASCII as full-width
    out, pos = [], 0
    for nd in nodes:
        s = nd["string"]
        if not s: continue
        k = ntext.find(fw(s), pos, pos + len(s) + 60)
        if k >= 0 and JP.search(text[pos:k]): k = -1  # never jump over Japanese text
        if k < 0:
            # digits that Open JTalk turned into kanji numerals: "2人" → 二人 (フタリ)
            if NUM.search(s):
                pat = "".join("[0-9０-９,，.．]+" if NUM.fullmatch(g) else re.escape(g) for g in re.findall(NUM.pattern + "+|.", s))
                m = re.match(r"([^㐀-鿿々〆ヶぁ-んァ-ヺ0-9０-９]*)(" + pat + ")", text[pos:])
                if m:
                    out.append(m.group(1)); raw = m.group(2)
                    r = kata2hira(nd["read"])
                    out.append("{%s|%s}" % (raw, r) if re.search(KANJI, raw) else raw)
                    pos += len(m.group(0))
            continue  # other normalised tokens ("(" as （): their raw text is copied later
        if k > pos: out.append(text[pos:k])
        r = FIX.get(s) or kata2hira(nd["read"]).replace("ヴ", "ゔ")
        raw = text[k:k + len(s)]
        out.append(raw if (r == "、" or not r or r == s or not re.search(KANJI, raw)) else ruby_word(raw, r))
        pos = k + len(s)
    out.append(text[pos:])
    return "".join(out)

# Joins Open JTalk splits into the right reading (numbers + counters, set phrases).
POST = {"1{人|ひと}": "{1人|ひとり}", "2{人|ひと}": "{2人|ふたり}", "2{人|にん}": "{2人|ふたり}", "1{人|にん}": "{1人|ひとり}", "{一|いち}{歩|ほ}": "{一歩|いっぽ}", "{三|さん}{分|ふん}": "{三分|さんぷん}", "{一|いち}{分|ふん}": "{一分|いっぷん}",
        "{六|ろく}{分|ふん}": "{六分|ろっぷん}", "{十|じゅう}{分|ふん}": "{十分|じゅっぷん}", "{今晩|こんばん}{中|ちゅう}": "{今晩中|こんばんじゅう}",
        "{今日|きょう}{中|ちゅう}": "{今日中|きょうじゅう}", "{一|いち}{日|にち}{中|ちゅう}": "{一日中|いちにちじゅう}", "{世界|せかい}{中|ちゅう}": "{世界中|せかいじゅう}",
        "{一|いち}{回|かい}": "{一回|いっかい}", "{六|ろく}{回|かい}": "{六回|ろっかい}", "{八|はち}{回|かい}": "{八回|はっかい}", "{十|じゅう}{回|かい}": "{十回|じゅっかい}",
        "{一|いち}{本|ほん}": "{一本|いっぽん}", "{三|さん}{本|ほん}": "{三本|さんぼん}", "{一|いち}{杯|はい}": "{一杯|いっぱい}", "{一|いち}{冊|さつ}": "{一冊|いっさつ}",
        "{一|いち}{緒|しょ}": "{一緒|いっしょ}", "{三|さん}{階|かい}": "{三階|さんがい}", "{一|いち}{個|こ}": "{一個|いっこ}", "{一|いち}{歳|さい}": "{一歳|いっさい}",
        "{八|はち}{歳|さい}": "{八歳|はっさい}", "{十|じゅう}{歳|さい}": "{十歳|じゅっさい}", "{二十|にじゅう}{歳|さい}": "{二十歳|はたち}", "{一|いち}{週|しゅう}": "{一週|いっしゅう}",
        "{一|いち}{泊|はく}": "{一泊|いっぱく}", "{一|いち}{件|けん}": "{一件|いっけん}", "{一|いち}{軒|けん}": "{一軒|いっけん}", "{一|いち}{分|ぶん}": "{一分|いちぶん}"}

def post(t):
    for a, b in POST.items(): t = t.replace(a, b)
    t = t.replace("{辞書|じしょ}{形|がた}", "{辞書形|じしょけい}").replace("{辞書|じしょ}{形|かたち}", "{辞書形|じしょけい}")
    t = re.sub(r"(?<=[ぁ-んァ-ン])\{形\|(?:かたち|がた)\}", "{形|けい}", t)  # て形・ない形・う形 = けい
    # book grammar labels like ［名］［動］［イ形］ stay plain
    return re.sub(r"［[^［］]*］", lambda m: re.sub(r"\{([^{}|]+)\|[^{}]+\}", r"\1", m.group(0)), t)

def _annotate(clean):
    return post(furi_plain(clean)) if re.search(KANJI, clean) else clean

def _with_markers(seg, skip_underlined):
    """Annotate a run of text that may contain [[ ]] / ** markers, using the whole run as context."""
    toks = re.split(r"(\[\[|\]\]|\*\*)", seg)
    clean, marks, inside, skip_spans, pos, start = "", [], False, [], 0, 0
    for t in toks:
        if t in ("[[", "]]", "**"):
            marks.append((len(clean), t))
            if t == "[[": inside, start = True, len(clean)
            if t == "]]": skip_spans.append((start, len(clean))); inside = False
        else:
            clean += t
    if skip_underlined and skip_spans:
        # annotate outside the quiz targets only, each piece with its own context
        out, last = [], 0
        cuts = sorted(skip_spans)
        pieces = []
        for a, b in cuts:
            pieces.append((last, a, True)); pieces.append((a, b, False)); last = b
        pieces.append((last, len(clean), True))
        ann = []
        for a, b, do in pieces:
            ann.append((a, b, _annotate(clean[a:b]) if do else clean[a:b]))
    else:
        ann = [(0, len(clean), _annotate(clean))]
    # re-insert markers by walking annotated text and counting base characters
    res, mi = [], 0
    marks.sort(key=lambda m: m[0])
    for a, b, txt in ann:
        cpos = a
        i = 0
        while i < len(txt):
            while mi < len(marks) and marks[mi][0] == cpos: res.append(marks[mi][1]); mi += 1
            m = re.match(r"\{([^{}|]+)\|([^{}]+)\}", txt[i:])
            if m:
                base = m.group(1)
                inner = [k for k in range(mi, len(marks)) if cpos < marks[k][0] < cpos + len(base)]
                if inner:  # a marker falls inside this ruby word: split the word as plain base + ruby on whole word is lost; keep base plain around marker
                    j = cpos
                    for ch in base:
                        while mi < len(marks) and marks[mi][0] == j: res.append(marks[mi][1]); mi += 1
                        res.append(ch); j += 1
                else:
                    res.append(m.group(0))
                cpos += len(base); i += len(m.group(0))
            else:
                res.append(txt[i]); cpos += 1; i += 1
        while mi < len(marks) and marks[mi][0] == cpos and cpos == b and b != len(clean): res.append(marks[mi][1]); mi += 1
    while mi < len(marks): res.append(marks[mi][1]); mi += 1
    return "".join(res)

def furi(text, skip_underlined=False):
    """skip_underlined: leave [[..]] text without readings (kanji-reading quizzes)."""
    if not re.search(KANJI, text): return text
    pieces = re.split(r"(\{[^{}|]+\|[^{}]+\}|\n|[①-⑳]|（[　 ]*）)", text)  # circled numbers and blanks break context
    res = []
    for p in pieces:
        if (p.startswith("{") and "|" in p) or not re.search(KANJI, p): res.append(p); continue
        res.append(_with_markers(p, skip_underlined) if re.search(KANJI, p) else p)
    return "".join(res)

if __name__ == "__main__":
    import sys
    for line in sys.stdin: print(furi(line.rstrip("\n")))
