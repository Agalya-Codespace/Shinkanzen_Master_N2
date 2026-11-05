from _h import *
DAY = 18

NOTE = "Real CD track. The book prints no script or answer for this one, so the script below was transcribed from the CD and checked by sensei; the answer is sensei's."
BOOK = "Real CD track. Script and answer are printed in the book."
N4 = ["1", "2", "3", "4"]

def pick(id, q, opts, ans, explain, keys=None):
    return mcq(id, q, opts, ans, explain, keys=keys or N4)

def table(title, head, rows, note=None, explain=None):
    b = {"type": "table", "title": title, "head": head, "rows": rows}
    if note: b["note"] = note
    if explain: b["explain"] = explain
    return b

SECTION = {
 "book": "chokai",
 "title": "実力養成編　Ⅵ「統合理解」のスキルを学ぶ　問題形式と内容・1 2人以上の人の話を整理する",
 "source": "新完全マスター聴解 N2 · 実力養成編 Ⅵ 問題形式と内容・Ⅵ-1 · pp.85–89 · CD B31–B36",
 "blocks": [
  items("Ⅵ「統合理解」のスキルを学ぶ　問題形式と内容", [
   ("まとまりのある話を聞いて、いくつかの情報を比べたりまとめたりして、答えを選びます。以下のような問題形式があります。",
    ["Sensei: 統合理解 = JLPT 聴解 問題5, the last and hardest part. You hear a longer talk and must COMPARE or COMBINE information.",
     "Thanglish: Idhu listening-la final boss. Notes eduthaa dhaan pass pannalaam — memory-la vechukka mudiyaadhu."]),
   ("**1**　状況説明文を聞く → 2人以上の人の話を聞く → 質問文と選択肢を聞く → 答えを選ぶ",
    "Type 1: a conversation of 2+ people (often 3). Question AND options are only spoken — nothing printed. So write notes per speaker."),
   ("**2**　状況説明文を聞く → 2種類の話を聞く → 2つの質問文を聞く → 問題用紙にある選択肢から答えを選ぶ",
    "Type 2: first an announcement/explanation, then two people discuss it. Two questions. The options ARE printed — read them before the audio starts."),
   ("どちらも質問は話の後に示されます。\n1の問題では、選択肢が書いてありません。\n2の問題では、選択肢が書いてあります。\n統合理解問題では、これまで学んだスキルを組み合わせて使いながら、問題を解いていきます。",
    "In both types the question comes AFTER the talk. Use every skill so far: catch keywords, track 賛成／反対, notice the final decision."),
  ]),

  items("1　2人以上の人の話を整理する", [
   ("この問題形式では2人以上の人の話を整理して聞きますが、最初に質問がないので、話を聞きながら質問になりそうな点を考えていかなければなりません。そこで、まず「何について話しているか」をつかみます。そして、質問になりそうな点を考えながら大事な情報を聞き取ります。そのとき、出された意見が賛成か反対かに注意しながら話を整理するとよいでしょう。",
    ["Sensei: No question first, so you must guess what will be asked. Step 1: what's the topic? Step 2: for each person, what do they want, and do they agree (賛成 さんせい) or disagree (反対 はんたい)?",
     "Thanglish: Moonu per pesuvaanga. Paper-la moonu column podunga — ovvoru aal enna solraanga, yes-aa no-aa. Last-la yaaru opinion win aagudhu? Adhu dhaan answer."]),
   ("・何について話しているか\n・出された意見の整理（賛成か反対か）", "Two things to catch."),
  ]),

  # ---------- 例題1 ----------
  audio("☆例題1　①　CD B31", "b31", "話を聞いて、まとめましょう。　ア．何について話していますか。　イ．3人はどんな意見を言っていますか。下の表にまとめてください。", tts=False, note=BOOK),
  group("例題1　①", [
   fill("d18c-e1-a", "ア．何について話していますか。　%%", ["テレビを買い換えるかどうか", "テレビを買い替えるかどうか", "テレビの買い換え", "テレビ"], "Book's answer: テレビを買い換えるかどうか."),
  ], scored=False),
  table("イ．3人の意見（答え・本）", ["男の人1（子供）", "女の人（お母さん）", "男の人2（お父さん）"], [
   ["買い換えよう", "古い →", "→ まだ見られる"],
   ["いいのが出ている／録画できるのもある", "", "→ 録画は要らない"],
   ["", "修理もお金がかかる／新しいのは電気代が安い・環境に優しい", "→ 今のテレビの電気代もたいしたことはない／捨てるのにお金が要る"],
   ["", "映らなくなったら考える", ""],
  ], note="Arrows show who answers whom.", explain="Thanglish: Paiyan 'puthusu vaangalaam', amma 'pazhasu aayiduchu, current bill kammi', appa ovvoru point-kkum 'vendaam'. Last-la amma: 'suthamaa theriyaama ponaa appo paakalaam'."),
  audio("例題1　②　CD B32", "b32", "次に、質問と選択肢を聞いて、最も良いものを選んでください。", tts=False, note=BOOK),
  group("例題1　②", [
   pick("d18c-e1-q", "テレビについてどうすることにしましたか。", ["録画もできるテレビに買い換える", "電気代の安いテレビに買い換える", "今のテレビを修理する", "今のテレビをこのまま使う"], 3,
    ["Book's answer: 4.",
     "「テレビ」について「買い換えよう」と言った後、それについて賛成する意見と反対する意見が次々と出ているので、「テレビを買い換えるかどうか」がこの話の中心だと考えられます（ア）。出てきた意見は表のように整理できます（イ）。お父さんの最後の反対意見に対して、さらに反対する意見は出ていません。また、最後に「全然映らなくなったら考えようか」と言っていることから、「今のテレビをこのまま使う」という考えがわかります。"]),
  ]),
  script("例題1　スクリプト（本）", [
   ("家族3人がテレビについて話しています。", ""),
   ("男1：あー、まただ。ね、テレビ、またおかしいよ。そろそろ[[買い換えよう]]よ。", "Son starts the topic: buy a new TV. 買い換える(かいかえる) = replace by buying."),
   ("女　：ああ、最近、ときどき{線|せん}が入るのよね。もう古いからねえ。", "Mum agrees a bit: lines on the screen, it's old."),
   ("男2：古くても、まだ見られるよ。", "Dad: 反対 — it still works."),
   ("男1：最近はいいのが出てるんだよね。1台で{録画|ろくが}もできるものとか。", "Son: new ones can record."),
   ("男2：おれは録画は要らないよ。", "Dad: 反対 — I don't need recording."),
   ("女　：そうね、お父さんは使わないわね。でも、修理するのもお金がかかるでしょう？　買い換えてもいいんじゃない？　新しいのは電気代も安くて、環境に{優|やさ}しいわよ。", "Mum: repairs cost money too; new ones save electricity."),
   ("男2：テレビの電気代なんてたいしたことはないじゃないか。捨てるにもお金が要るし。", "Dad: 反対 — electricity is nothing; even throwing it out costs money."),
   ("男1：まあね。", "Son gives in."),
   ("女　：じゃ、そのうち[[全然映らなくなったら考えようか]]。", "Final decision: keep using it until it completely stops → answer 4."),
  ], extra=[text("答え　①ア．テレビを買い換えるかどうか　イ．（上の表）　②4", "答え（本）")]),

  # ---------- 練習1 (1) ----------
  audio("練習1 (1)　①　CD B33", "b33", "話を聞いて、まとめましょう。　ア．何について話していますか。　イ．3人はどんな意見を言っていますか。", tts=False, note=NOTE),
  group("練習1 (1)　①", [
   fill("d18c-r1-1a", "ア．何について話していますか。　%%", ["男の人の昼ご飯", "昼ご飯", "昼ごはん", "男の人の昼ごはん", "昼ご飯をどうするか", "カップラーメン"], "Model: 男の人の昼ご飯（毎日カップラーメンを食べていること）."),
  ], scored=False),
  table("イ．3人の意見（モデル）", ["女の人1", "男の人", "女の人2"], [
   ["毎日カップラーメン → そろそろやめたら？", "毎日違う種類を食べている", ""],
   ["", "", "カップラーメンはカップラーメン／味が濃い・栄養が偏る"],
   ["", "わかってるけど、弁当を作るのは大変／外食は金がかかる", ""],
   ["作るのが面倒ならコンビニ弁当を／栄養バランスもいいし安い", "買いに行くのが面倒／昼は混んでいる", ""],
   ["", "手作りはおいしそう／それぐらいならできるかも、やってみようかな", "おにぎりを作ったら？／前の日のご飯を温めて握るだけ、好きなものを入れられる"],
  ], note="Sensei's model notes from the CD. Which woman says which line is sensei's best reading of the voices; the answer doesn't depend on it."),
  audio("練習1 (1)　②　CD B34", "b34", "次に、質問と選択肢を聞いて、最も良いものを選んでください。", tts=False, note=NOTE),
  group("練習1 (1)　②", [
   pick("d18c-r1-1q", "男の人はこれから昼ご飯をどうしようと思っていますか。", ["カップラーメンを買う", "弁当を作る", "コンビニ弁当を買う", "おにぎりを作る"], 3,
    ["Sensei's answer: 4.",
     "He rejects each idea: 弁当 → 作るの大変; コンビニ弁当 → 買いに行くのが面倒. For おにぎり he finally says それぐらいならできるかも。やってみようかな → he'll try making rice balls.",
     "Thanglish: Ovvoru idea-kkum 'mudiyaadhu' sonnaan, last-la onigiri-kku mattum 'try pannuren'. Adhu dhaan answer."]),
  ]),
  script("練習1 (1)　スクリプト（CDから）", [
   ("学校で友達3人が話しています。", ""),
   ("女1：あれ？　また昼ご飯カップラーメン？　毎日だね。そろそろやめたら？", "Topic: his lunch is always cup noodles."),
   ("男　：いや、毎日違う種類のを食べてるんだよ。ほら、今日はキムチラーメン。", "Excuse: a different flavour every day."),
   ("女2：違う種類って言っても、カップラーメンはやっぱりカップラーメンよ。味が濃いし、栄養が{偏|かたよ}るし。", "反対: strong taste, unbalanced nutrition. 偏る(かたよる) = be unbalanced."),
   ("男　：それはわかってるんだけど、弁当作るの大変だろう。毎日外食じゃ{金|かね}がかかるし。", "Packed lunch = too much work; eating out = expensive."),
   ("女1：作るのが面倒なら、コンビニで買ったら？　最近のコンビニ弁当、栄養バランスもいいし、それに安いよ。", "Idea 2: convenience-store bento."),
   ("男　：買いに行くのが面倒なんだ。昼の時間は結構混んでるし。", "反対: going to buy is a pain; crowded at lunch."),
   ("女2：じゃあ、おにぎりでも作ったら？　ほら、これ、朝作ったの。簡単よ。前の日のご飯をレンジで温めて{握|にぎ}るだけ。中に好きなもの入れられるよ。", "Idea 3: make rice balls — just reheat yesterday's rice and shape it."),
   ("男　：へー、手作りっておいしそうだね。うーん、そっか。[[それぐらいならできるかも。やってみようかな。]]", "Decision → 4 おにぎりを作る."),
  ], extra=[text("答え　①ア．男の人の昼ご飯　②4", "答え")]),

  # ---------- 練習1 (2) ----------
  audio("練習1 (2)　①　CD B35", "b35", "話を聞いて、まとめましょう。　ア．何について話していますか。　イ．3人はどんな意見を言っていますか。", tts=False, note=NOTE),
  group("練習1 (2)　①", [
   fill("d18c-r1-2a", "ア．何について話していますか。　%%", ["夏休みの旅行", "夏休みの予定", "夏休みにどこへ行くか", "夏休み", "旅行"], "Model: 夏休みにどこへ旅行に行くか."),
  ], scored=False),
  table("イ．3人の意見（モデル）", ["男の人1（お父さん）", "女の人（お母さん）", "男の人2（子供）"], [
   ["夏休みの予定を考えないと／涼しいところでのんびりしたい", "ニュージーランドに行きたい（その時期涼しい）", "いいね、海外に一度行ってみたかった"],
   ["休めるのはせいぜい4日、海外はね", "そんなに短いの？　沖縄とか北海道なら？", ""],
   ["北海道か、涼しくてのんびりできそう", "韓国もいいわね、お買い物して", "韓国なら近いよ"],
   ["海外は言葉がわからない／他人の決めたスケジュールで過ごしたくない", "", "ツアーで行けばいい"],
   ["涼しいところでおいしいものを食べよう", "じゃあ調べてみるわ", "じゃあ国内か"],
  ], note="Sensei's model notes from the CD. The speaker labels are sensei's best reading of the voices; the answer doesn't depend on them."),
  audio("練習1 (2)　②　CD B36", "b36", "次に、質問と選択肢を聞いて、最も良いものを選んでください。", tts=False, note=NOTE),
  group("練習1 (2)　②", [
   pick("d18c-r1-2q", "家族はどこに行くことにしましたか。", ["ニュージーランド", "韓国", "北海道", "沖縄"], 2,
    ["Sensei's answer: 3.",
     "Overseas is out: only 4 days off, Dad doesn't speak the language and won't do a tour → じゃあ国内か. Of 沖縄 and 北海道, the one they called 涼しくてのんびりできそう is 北海道, and they finish with 涼しいところでおいしいもの食べよう. Okinawa is hot in summer.",
     "Thanglish: NZ, Korea = foreign → cut. Japan-kulla 'cool place' = Hokkaido."]),
  ]),
  script("練習1 (2)　スクリプト（CDから）", [
   ("家族3人が夏休みについて話しています。", ""),
   ("男1：夏休みの予定、そろそろ考えないとなあ。どこか涼しいところでのんびりしたいね。", "Key condition: 涼しい・のんびり."),
   ("女　：そうね。私、ニュージーランドに行きたいわ。その時期、涼しいでしょ。", "Mum: New Zealand (winter there)."),
   ("男2：いいね。海外には一度行ってみたかったんだ。", "Kid agrees."),
   ("女　：1週間ぐらい休めるの？", ""),
   ("男1：いや、せいぜい4日だし、海外はね。", "反対: only 4 days."),
   ("女　：まあ、そんなに短いの？　じゃあ、沖縄とか北海道なら行けるかしら。", "Two domestic ideas."),
   ("男1：北海道か。涼しくてのんびりできそうだね。", "Dad likes Hokkaido."),
   ("男2：ねえ、韓国なら近いよ。", "Kid tries again: Korea."),
   ("女　：韓国もいいわねえ。お買い物して……", ""),
   ("男1：でも、海外は言葉がわからないからなあ。", "反対: language."),
   ("男2：ツアーで行けばいいじゃない。", ""),
   ("男1：いやあ、休みの日まで他人の決めたスケジュールで過ごしたくないよ。", "反対: no tours."),
   ("男2：うーん、じゃあ国内か。", "Kid gives up overseas."),
   ("男1：[[涼しいところで]]おいしいもの食べよう。", "→ 北海道."),
   ("女　：そうね。じゃあ、調べてみるわ。", ""),
  ], extra=[text("答え　①ア．夏休みにどこへ行くか　②3", "答え")]),
 ],
}
