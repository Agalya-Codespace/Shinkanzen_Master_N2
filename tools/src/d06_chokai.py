from _h import *
DAY = 6

OWN = "⚠ The book prints no script or answer for this CD track, so sensei made this practice set in the same format. The audio is a computer read-aloud, not the real CD."

C1 = [  # (label, yes, no, script, ans 0=happened 1=didn't, thanglish)
 ("（例）", "{遅刻|ちこく}した", "{遅刻|ちこく}していない", "今朝、寝坊して、会議に遅刻しちゃったよ。", 0, "～ちゃった = ～てしまった → it really happened. Book 例 answer: 遅刻した."),
 ("(1)", "{負|ま}けた", "{負|ま}けていない", "昨日の試合、あと少しで負けるところだったよ。", 1, "辞書形 + ところだった = almost happened, but didn't. They didn't lose."),
 ("(2)", "{間|ま}に{合|あ}った", "{間|ま}に{合|あ}っていない", "駅まで走ったから、なんとか電車に間に合ってよかった。", 0, "～て～た (間に合ってよかった) → it happened."),
 ("(3)", "{参加|さんか}した", "{参加|さんか}していない", "週末のボランティア、参加したかったんだけど、仕事が入っちゃって。", 1, "～たかったんだけど = wanted to, but couldn't. Didn't join."),
 ("(4)", "{行|い}った", "{行|い}っていない", "北海道、行ってよかったよ。景色が最高だった。", 0, "～てよかった → he went."),
 ("(5)", "{電話|でんわ}をかけた", "{電話|でんわ}をかけていない", "お客さんに電話をかけようとしたら、ちょうど向こうからかかってきたんだ。", 1, "～ようとしたら = just as I was about to ～ → the customer called first. He didn't call."),
 ("(6)", "{頼|たの}まれた", "{頼|たの}まれていない", "部長に頼まれて、来週の会議の資料を作ることになったんだ。", 0, "頼まれて…ことになった → he really was asked."),
 ("(7)", "{入|い}れた", "{入|い}れていない", "かばんに財布、入れたつもりだったんだけど、机の上に置いてきちゃった。", 1, "た形 + つもりだった = thought I had, but actually didn't."),
 ("(8)", "{出|で}かけた", "{出|で}かけていない", "妻なら、今、買い物に出かけたところです。", 0, "た形 + ところだ = has just done it → she went out."),
 ("(9)", "{座|すわ}った", "{座|すわ}っていない", "電車で座ろうと思ってたんだけど、お年寄りが乗ってきたから、ずっと立ってたよ。", 1, "～ようと思ってたんだけど = planned to, but didn't. He stood the whole time."),
 ("(10)", "なくした", "なくしていない", "大事な書類、なくすところだったよ。タクシーに忘れそうになってね。", 1, "なくすところだった / 忘れそうになって = almost. He didn't lose it."),
]

D_EX = [
 ("例1", "これ、{昨日|きのう}{買|か}った[[の]]。", "（＝「昨日買った」ことを報告する）", "の↘ (falling) = telling."),
 ("例2", "{来週|らいしゅう}のパーティー、{来|こ}ない[[の]]？", "（＝「来ない」かどうか聞く）", "の↗ (rising) = asking."),
 ("例3", "{今日|きょう}は、お{弁当|べんとう}、{要|い}らない。", "（＝「要らない」ことを報告する）", "ない↘ = 'I don't need it.'"),
 ("例4", "あの{映画|えいが}、{一緒|いっしょ}に{見|み}ない？", "（＝「見る」かどうか聞く）", "ない↗ = invitation 'won't you watch?'"),
 ("例5", "リーさん、{今日|きょう}{休|やす}む[[って]]。", "（＝「休む」ことを報告する）", "って↘ = 'I heard he's off.' (reporting)"),
 ("例6", "え？　{休|やす}む[[って]]？", "（＝「休む」ことを確認するために聞く）", "って↗ = 'Did you say off?' (checking)"),
 ("例7", "さっき{食|た}べてきた[[んだ]]。", "（＝「食べてきた」ことを報告する）", "んだ = explaining/telling."),
 ("例8", "あ、{携帯電話|けいたいでんわ}、{替|か}えた[[んだ]]。", "（＝「替えた」ことを確認する）", "あ、～んだ = 'Oh, so you changed it!' (noticing/checking)."),
]

RP, KI, KK = "{報告|ほうこく}している{文|ぶん}", "{聞|き}いている{文|ぶん}", "{確認|かくにん}している{文|ぶん}"
D1 = [  # (script, opts, ans, thanglish)
 ("この本、もう読んだの？", [RP, KI], 1, "読んだの？↗ — rising の = asking."),
 ("わたし、その映画、見てない。", [RP, KI], 0, "見てない↘ — telling 'I haven't seen it.'"),
 ("あ、雨、降ってきたんだ。", [RP, KK], 1, "あ、～んだ = noticing (like 例8) → checking."),
 ("昨日、駅で山田さんに会ったんだ。", [RP, KK], 0, "～んだ↘ = telling news (like 例7)."),
 ("田中さん、来月結婚するって。", [RP, KI], 0, "って↘ = reporting what you heard (like 例5)."),
 ("え？　来月結婚するって？", [RP, KI], 1, "え？…って↗ = checking/asking (like 例6)."),
 ("週末、一緒に買い物に行かない？", [RP, KI], 1, "行かない↗ = invitation question (like 例4)."),
 ("あした、会社、行かない。", [RP, KI], 0, "行かない↘ = 'I'm not going.' (like 例3)"),
 ("このケーキ、自分で作ったの。", [RP, KI], 0, "作ったの↘ = 'I made it myself.' (like 例1)"),
 ("コーヒー、飲まない？", [RP, KI], 1, "飲まない↗ = offering/asking."),
]

E_TABLE = [
 ["{機能|きのう}", "{表現|ひょうげん}", "{例文|れいぶん}"],
 ["{質問|しつもん}（{確認|かくにん}）", "～っけ", "あれ、{試験|しけん}って{木曜日|もくようび}だっけ。"],
 ["{質問|しつもん}（{確認|かくにん}）", "～の？", "あ、{佐藤|さとう}さんって、{結婚|けっこん}してるの？"],
 ["{提案|ていあん}", "～たらどう？\n～たほうがいい", "こっちの{色|いろ}にしたらどう？\nもっと{大|おお}きくしたほうがいいよ。"],
 ["{指示|しじ}", "～なくちゃ／～なきゃ\n～ないと", "もっときれいに{書|か}かなくちゃ。\nそろそろ{行|い}かないと。"],
 ["{申|もう}し{出|で}", "～ましょう(か)", "{荷物|にもつ}、{持|も}ちましょうか。"],
 ["{誘|さそ}い", "～ませんか／～ましょう", "{一緒|いっしょ}に{行|い}きませんか。"],
 ["{感想|かんそう}", "～といったら／～っていったら", "{休日|きゅうじつ}の{混雑|こんざつ}っていったらすごいよ。"],
 ["{感想|かんそう}", "～なんて", "4{月|がつ}に{雪|ゆき}が{降|ふ}るなんて。"],
 ["{報告|ほうこく}", "～(んだ)って", "{田中|たなか}さん、{会社|かいしゃ}{辞|や}めるんだって。"],
 ["{報告|ほうこく}", "～ちゃう／じゃう（＝てしまう）", "あ、{忘|わす}れちゃった。"],
]

O1 = ["{確認|かくにん}", "{感想|かんそう}", "{報告|ほうこく}"]
O2 = ["{質問|しつもん}", "{指示|しじ}", "{申|もう}し{出|で}"]
O3 = ["{質問|しつもん}", "{提案|ていあん}", "{報告|ほうこく}"]
O4 = ["{指示|しじ}", "{申|もう}し{出|で}", "{誘|さそ}い"]
E1 = [  # (script, opts, ans, thanglish)
 ("あれ、会議って3時からだっけ。", O1, 0, "～だっけ = checking something you half-remember → 確認."),
 ("あの店のラーメンのおいしさといったら、ほかの店とは比べられないよ。", O1, 1, "～といったら = 'talking of ～, wow!' → 感想."),
 ("山田さん、来月から大阪に転勤するんだって。", O1, 2, "～んだって = 'I heard that ～' → 報告."),
 ("こんな簡単な問題を間違えるなんて。", O1, 1, "～なんて = surprise/feeling → 感想."),
 ("あ、傘、電車に忘れてきちゃった。", O1, 2, "～ちゃった = ～てしまった → 報告."),
 ("その荷物、重そうですね。お持ちしましょうか。", O2, 2, "お持ちしましょうか = 'Shall I carry it?' → 申し出."),
 ("この字、もっと丁寧に書かなくちゃ。読めないよ。", O2, 1, "～なくちゃ to someone = 'you must ～' → 指示."),
 ("あれ、佐藤さんって、もう帰ったの？", O2, 0, "～の？ = question → 質問."),
 ("そんなに疲れてるなら、少し休んだらどう？", O3, 1, "～たらどう？ → 提案."),
 ("今度の日曜日、一緒に映画を見に行きませんか。", O4, 2, "～ませんか with 一緒に → 誘い."),
]

def plain(s): return s
def ab(opts, i): return opts[i]

SECTION = {
 "book": "chokai",
 "title": "実力養成編　Ⅱ「即時応答」のスキルを学ぶ　1 最初の文を理解する（1-C・1-D・1-E）",
 "source": "新完全マスター聴解 N2 · 実力養成編 Ⅱ-1 · pp.22–26 · CD A15–A20 (read-aloud)",
 "blocks": [
  text("意見、報告、感想を理解するときは、説明されている出来事が実際に起こったかどうかを考えることも大切です。特に、タ形が使われていても実際には起こっていないことを表す表現に気をつけます。",
   "1-C「起こったか、起こっていないか」に注意して聞く",
   ["Past form (た形) kettaalum, adhu nadandhudhunu artham illa! 'Pōga nenachen, aanaa pōgala' maadhiri.",
    "Below list-a nalla memorise pannunga: left = nadandhudhu, right = nadakkala."]),
  items("【実際に起こった】", [
   ("・～て～た　　例　行っ[[て]]よかっ[[た]]。", "～てよかった, ～て困った → it happened."),
   ("・（タ形）ところだ　　例　帰った[[ところだ]]。", "た形 + ところだ = has just done it."),
  ]),
  items("【実際には起こっていない】", [
   ("・～そうだった／そうになった　　例　泣き[[そうだった]]。／落ち[[そうになった]]。", "Almost cried / almost fell — but didn't."),
   ("・～たかった／てほしかった（けど）　　例　会い[[たかったん]]だけど。／見に来[[てほしかった]]な。", "Wanted to (but didn't) / wished you'd come (but you didn't)."),
   ("・（辞書形／タ形）つもりだった　　例　返す[[つもりだった]]。／入れた[[つもりだった]]。", "Meant to return it / thought I'd put it in — but no."),
   ("・（辞書形）ところだった　　例　忘れる[[ところだった]]。", "Almost forgot."),
   ("・～ようと思っていた（けど）　　例　渡そう[[と思ってたん]]だけど。", "I was going to hand it over, but…"),
   ("・～ようとしたら　　例　出[[ようとしたら]]雨が降ってきた。", "Just as I tried to go out, it rained → didn't go out (yet)."),
  ], explain="Trap: 帰ったところだ = happened; 忘れるところだった = didn't happen. Dictionary form + ところだった = 'almost'."),

  audio("練習1-C　CD A15", "a15", "男の人の話を聞いて、実際はどちらか選んでください。", note=OWN),
  group("練習1-C", [mcq("d6c-1c-%d" % i, w[0], [w[1], w[2]], w[4], "Answer: %s. %s" % ([w[1], w[2]][w[4]], w[5]), keys=["", ""]) for i, w in enumerate(C1)],
   lead="Tap what really happened."),
  script("練習1-C　スクリプトと答え · open after you answer",
   [(w[0] + "　" + w[3], "Answer: %s. %s" % ([w[1], w[2]][w[4]], w[5])) for w in C1],
   extra=[text("答え　（例）遅刻した　(1) 負けていない　(2) 間に合った　(3) 参加していない　(4) 行った　(5) 電話をかけていない　(6) 頼まれた　(7) 入れていない　(8) 出かけた　(9) 座っていない　(10) なくしていない", "答え")]),

  text("同じ表現でも、イントネーションによって意味が変わることがあります。イントネーションに注意して、何かを報告している文なのか、相手に聞いている文なのかを理解する必要があります。",
   "1-D イントネーションに注意して聞く",
   ["Same words, different tone: ↘ = telling (報告), ↗ = asking (聞く) or checking (確認).",
    "The read-aloud voice does raise the end for questions (？), but softly. Listen to the last syllable carefully; the script below shows ？ marks after you answer."]),
  audio("1-D　例1～例8　CD A16", "a16", "例1～例8を聞いてください。", label="A16 · computer read-aloud of the book's examples"),
  items("1-D　例", [(w[0] + "　" + w[1] + "　" + w[2], w[3]) for w in D_EX]),

  audio("例題1-D　CD A17", "a17", "文を聞いてください。どちらですか。", label="A17 · computer read-aloud of the book's script"),
  group("例題1-D", [
   mcq("d6c-1d-e1", "(1)", [RP, KI], 1, "Book answer: 聞いている文. 文末を上げて、相手に新聞がどこにあるか聞いています。", keys=["", ""]),
   mcq("d6c-1d-e2", "(2)", [RP, KI], 0, "Book answer: 報告している文. 文末を下げて、「知らない」ということを報告しています。", keys=["", ""]),
  ]),
  script("例題1-D　スクリプトと答え（本）", [
   ("(1)　{新聞|しんぶん}、{知|し}らない？", "答え：聞いている文。(1)は、文末を上げて、相手に新聞がどこにあるか聞いています。"),
   ("(2)　それ、{知|し}らない。", "答え：報告している文。(2)は、文末を下げて、「知らない」ということを報告しています。"),
  ]),

  audio("練習1-D　CD A18", "a18", "文を聞いてください。どちらですか。", note=OWN),
  group("練習1-D", [mcq("d6c-1d-%d" % (i + 1), "(%d)" % (i + 1), w[1], w[2], "Answer: %s. %s" % (w[1][w[2]], w[3]), keys=["", ""]) for i, w in enumerate(D1)],
   lead="報告 (telling) or 聞く／確認 (asking / checking)?"),
  script("練習1-D　スクリプトと答え · open after you answer",
   [("(%d)　" % (i + 1) + w[0], "Answer: %s. %s" % (w[1][w[2]], w[3])) for i, w in enumerate(D1)],
   extra=[text("答え　(1) 聞いている　(2) 報告　(3) 確認　(4) 報告　(5) 報告　(6) 聞いている　(7) 聞いている　(8) 報告　(9) 報告　(10) 聞いている", "答え")]),

  text("ここでは、最初の文を聞いて、その機能をすぐに判断する練習をします。会話でよく使われる次のような表現に注意します。",
   "1-E 会話でよく使われる表現に注意して聞く",
   ["機能(きのう) = function. First line kettavudane: idhu question-aa, suggestion-aa, offer-aa, invitation-aa, feeling-aa, news-aa?",
    "Endings dhaan clue: っけ (checking), たらどう (suggest), なくちゃ (instruct), ましょうか (offer), ませんか (invite), なんて/といったら (feeling), んだって/ちゃった (report)."]),
  {"type": "table", "title": "1-E　機能・表現・例文", "rows": E_TABLE,
   "explain": "Table-a memorise pannunga. N2 問題4-la idhu dhaan base: function purinjaa, reply easy-aa choose pannalaam."},

  audio("例題1-E　CD A19", "a19", "文を聞いてください。どれですか。", label="A19 · computer read-aloud of the book's script"),
  group("例題1-E", [mcq("d6c-1e-e", "（例題）", O1, 0, "Book answer: 確認. ～だっけ = checking.", keys=["", "", ""])]),
  script("例題1-E　スクリプトと答え（本）", [("{小林|こばやし}さん、あしたから{出張|しゅっちょう}だっけ。", "答え：確認")]),

  audio("練習1-E　CD A20", "a20", "文を聞いてください。どれですか。", note=OWN),
  group("練習1-E", [mcq("d6c-1e-%d" % (i + 1), "(%d)" % (i + 1), w[1], w[2], "Answer: %s. %s" % (w[1][w[2]], w[3]), keys=["", "", ""]) for i, w in enumerate(E1)],
   lead="Tap the function of the sentence."),
  script("練習1-E　スクリプトと答え · open after you answer",
   [("(%d)　" % (i + 1) + w[0], "Answer: %s. %s" % (w[1][w[2]], w[3])) for i, w in enumerate(E1)],
   extra=[text("答え　(1) 確認　(2) 感想　(3) 報告　(4) 感想　(5) 報告　(6) 申し出　(7) 指示　(8) 質問　(9) 提案　(10) 誘い", "答え")]),
 ],
}
