from _h import *
DAY = 4

def hear(id, q, ans, explain, n=3):
    return mcq(id, q, ABC[:n], ans, explain, keys=[""] * n)

OWN = "⚠ The book prints no script or answer for this CD track, so sensei made this practice set in the same format. The audio is a computer read-aloud, not the real CD."

TABLE = [
 ["「～ちゃう」「～じゃう」\n例 {食|た}べちゃう／{飲|の}んじゃった", "「～てしまう」「～でしまう」\n例 {食|た}べてしまう／{飲|の}んでしまった"],
 ["「～ちゃ」「～じゃ」\n例 {書|か}いちゃ／{読|よ}んじゃ／それじゃ", "「～ては」「～では」\n例 {書|か}いては／{読|よ}んでは／それでは"],
 ["「～（なく）ちゃ」「～（な）きゃ」\n例 しなくちゃ／{帰|かえ}らなきゃ", "「～（なく）ては」「～（な）ければ」\n例 しなくては／{帰|かえ}らなければ"],
 ["「～てる」「～でる」\n例 {待|ま}ってる／{込|こ}んでる", "「～ている」「～でいる」\n例 {待|ま}っている／{込|こ}んでいる"],
 ["「～てく」「～でく」\n例 {連|つ}れてく／{遊|あそ}んでく", "「～ていく」「～でいく」\n例 {連|つ}れていく／{遊|あそ}んでいく"],
 ["「～とく」「～どく」\n例 {置|お}いとく／{飲|の}んどく", "「～ておく」「～でおく」\n例 {置|お}いておく／{飲|の}んでおく"],
 ["「ん」\n例 なんない／{足|た}んない／{何|なに}やってんの／{寝|ね}らんない／{食|た}べるもん／{嫌|いや}んなる／いちんち", "「ら」「る」「れ」「の」「に」\n例 ならない／{足|た}らない（{足|た}りない）／{何|なに}やってるの／{寝|ね}られない／{食|た}べるもの／{嫌|いや}になる／いちにち"],
 ["＋「っ」\n例 とっても／すっごく／ばっかり／{高|たか}くって", "－「っ」\n例 とても／すごく／ばかり／{高|たか}くて"],
 ["＋「ん」\n例 あんまり／おんなじ", "－「ん」\n例 あまり／おなじ"],
]

W21 = [  # (frame before, contracted heard, answers, frame after, thanglish)
 ("まだ", "あいてるよ", ["開いているよ", "あいているよ", "開いている", "あいている"], "。", "Book's 例: 開いてる → 開いている (～てる = ～ている)."),
 ("大変。この書類", "忘れてきちゃった", ["忘れてきてしまった", "わすれてきてしまった"], "。", "～ちゃった = ～てしまった. 'Aiyo, indha document-a maranthu vittutten.'"),
 ("", "何やってんの", ["何をやっているの", "何やっているの", "なにをやっているの", "なにやっているの"], "？", "やってんの = やっているの (る→ん, ている→てる). 'Enna pannitu irukka?'"),
 ("さっき、課長に", "怒られちゃった", ["怒られてしまった", "おこられてしまった"], "。", "～ちゃった = ～てしまった. 'Boss kitta thittu vaangiten.'"),
 ("さっきの話、", "言っちゃだめだよ", ["言ってはだめだよ", "いってはだめだよ", "言ってはだめ", "言ってはいけないよ"], "。", "～ちゃだめ = ～てはだめ. 'Andha vishayatha yaar kittayum sollaadha.'"),
 ("これ、さっさと", "やんなきゃ", ["やらなければ", "やらなければならない", "やらなければいけない"], "。", "やんなきゃ = やらなきゃ (ら→ん) = やらなければ. 'Seekiram mudikkanum.'"),
 ("チケット、", "持ってる", ["持っている", "もっている"], "？", "持ってる = 持っている. 'Ticket vechirukkiya?'"),
 ("これ、", "読んじゃだめ", ["読んではだめ", "よんではだめ", "読んではいけない"], "？", "～じゃだめ = ～ではだめ. 'Idha padikka koodaadha?'"),
 ("この荷物、ここに", "置いとくね", ["置いておくね", "おいておくね", "置いておく"], "。", "～とく = ～ておく. 'Indha luggage-a inga vechiduren.'"),
 ("これ、できるだけ早く", "出さなくちゃ", ["出さなくては", "ださなくては", "出さなくてはいけない", "出さなくてはならない"], "。", "～なくちゃ = ～なくては. 'Idha seekiram submit pannanum.'"),
 ("今から会社に", "戻ってくよ", ["戻っていくよ", "もどっていくよ", "戻っていく"], "。", "～てく = ～ていく. 'Ippo office-ku thirumbi poren.'"),
]

W22 = [  # (first line, a, b, c, ans, thanglish)
 ("男：このケーキ、食べちゃっていい？", "うん、どうぞ。", "うん、食べてたよ。", "ううん、まだ食べてない。", 0,
  "食べちゃっていい？ = 食べてしまってもいい？ (Can I eat it all?) → うん、どうぞ."),
 ("女：宿題、まだやってないの？早くやんなきゃ。", "うん、もう終わっちゃった。", "わかってるよ。今やるところ。", "やんなくてよかったね。", 1,
  "やってないの = やっていないの. やんなきゃ = やらなければ. 'Homework innum pannaliya? Seekiram pannanum' → 'Theriyum, ippo dhaan panna poren.'"),
 ("男：駅まで送ってこうか？", "ありがとう、助かる。", "うん、送っといたよ。", "え、もう着いちゃったの？", 0,
  "送ってこうか = 送っていこうか (Shall I take you to the station?) → ありがとう."),
 ("女：この本、明日までに読んどいてね。", "え、もう読んじゃったの？", "うん、読んどいてくれてありがとう。", "わかった、今夜読んどく。", 2,
  "読んどいて = 読んでおいて (please read it in advance) → 今夜読んどく (I'll read it tonight)."),
 ("男：あんまり無理しちゃだめだよ。", "うん、無理しちゃった。", "ありがとう、気をつける。", "え、無理じゃないの？", 1,
  "あんまり = あまり. 無理しちゃだめ = 無理してはだめ (Don't overdo it) → ありがとう、気をつける."),
 ("女：窓、開けっぱなしで出かけちゃった。", "早く閉めに帰んなきゃ。", "開けといてくれたの？", "出かけなくちゃね。", 0,
  "開けっぱなし = left open. 出かけちゃった = 出かけてしまった. Reply: 帰んなきゃ = 帰らなければ (We must go back and close it)."),
 ("男：このパソコン、すっごく高くって買えないよ。", "じゃ、買っちゃおうよ。", "もうちょっと安いのにしたら？", "高くなくてよかったね。", 1,
  "すっごく = すごく. 高くって = 高くて. Too expensive → suggest a cheaper one."),
]

def opts_line(a, b, c): return "a　" + a + "　　b　" + b + "　　c　" + c

SECTION = {
 "book": "chokai",
 "title": "実力養成編　Ⅰ 音声の特徴に慣れる　2 音の変化や{縮約形|しゅくやくけい}",
 "source": "新完全マスター聴解 N2 · 実力養成編 Ⅰ-2 · pp.16–17 · CD A10–A11 (read-aloud)",
 "blocks": [
  text("話すときは音が省略されたり、書いたものとは違った音になったりすることがあります。特に親しい人との話し方に多いです。",
   "2　音の変化や{縮約形|しゅくやくけい}",
   ["縮約形(しゅくやくけい) = contracted forms. Friends kooda pesumbodhu Japanese words surungidum: 食べてしまった → 食べちゃった.",
    "N2 listening-la casual conversations-la idhu romba varum. Kettappove original form-a manasula maathanum."]),
  {"type": "table", "title": "変化した形・{縮約形|しゅくやくけい}　→　元の形", "rows": TABLE,
   "explain": "Left = spoken (contracted). Right = original. Most important: ちゃう/じゃう (てしまう), ちゃ/じゃ (ては/では), なきゃ/なくちゃ (なければ/なくては), てる (ている), てく (ていく), とく (ておく), and ら/る/れ/の/に → ん."},

  audio("練習2-1　CD A10", "a10", "文を聞いて、変化した形ではない、元の形を書いてください。",
   note="⚠ The printed frames are the book's. The book prints no script, so the endings you hear are sensei's own sentences; the key below matches this read-aloud, not the real CD."),
  group("練習2-1", [fill("d4c-21-%d" % i, ("（例）" if i == 0 else "(%d)　" % i) + w[0] + "%%", w[2], "Heard: 「" + w[1] + "」. " + w[4], suffix=w[3]) for i, w in enumerate(W21)],
   lead="Type the original (元の形) of what you hear, e.g. {開|あ}いているよ. Kanji or hiragana both OK."),
  script("練習2-1　スクリプトと答え · open after you answer",
   [(("（例）" if i == 0 else "(%d)　" % i) + w[0] + "**" + w[1] + "**" + w[3] + "　→　" + w[2][1 if i == 0 else 0], w[4]) for i, w in enumerate(W21)]),

  audio("練習2-2　CD A11", "a11", "文を聞いて、それに対する返事の文を聞き、最もよいものを選んでください。", note=OWN),
  group("練習2-2", [hear("d4c-22-%d" % i, "（例）" if i == 0 else "(%d)" % i, w[4], "Answer %s. %s" % ("abc"[w[4]], w[5])) for i, w in enumerate(W22)]),
  script("練習2-2　スクリプトと答え · open after you answer",
   [(("（例）" if i == 0 else "(%d)　" % i) + w[0] + "\n" + opts_line(w[1], w[2], w[3]), "Answer %s. %s" % ("abc"[w[4]], w[5])) for i, w in enumerate(W22)],
   extra=[text("答え　（例）a　(1) b　(2) a　(3) c　(4) b　(5) a　(6) b", "答え", "Ovvoru line-layum contracted form irukku. Original form-a manasula maathi purinjikkonga.")]),
 ],
}
