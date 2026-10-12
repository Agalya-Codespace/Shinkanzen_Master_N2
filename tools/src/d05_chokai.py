from _h import *
DAY = 5

OWN = "⚠ The book prints no script or answer for this CD track, so sensei made this practice set in the same format. The audio is a computer read-aloud, not the real CD."
MF = ["{男|おとこ}", "{女|おんな}"]

TABLE = [
 ["許可求め", "～させて＋ほしいんだけど／ください／くださいませんか／もらえる？／もらえない？／もらえませんか／いただきたいんですが／いただけませんか／くれない？／くれませんか\n～ても＋いい？／いいですか／いいでしょうか／よろしいでしょうか", "依頼", "～て＋ほしいんだけど／ください／くださいませんか／もらえる？／もらえない？／もらえませんか／いただきたいんですが／いただけませんか／くれない？／くれませんか／くれる（もらえる）と{助|たす}かるんですが（ありがたいんですが）"],
 ["{申|もう}し{出|で}", "～ましょうか／～ようか／～ますね", "{提案|ていあん}・{指示|しじ}", "～たら＋どう？／どうですか\n～ば＋いいんじゃない？／いいと{思|おも}います\n～たほうがいいですよ"],
]

A1 = [  # (verb, script line, ans index into options, thanglish)
 ("例　{用意|ようい}する", "男：明日の会議の資料、用意してもらえる？", 1, "～てもらえる？ = request (依頼) → the listener (woman) prepares. Book 例 answer: 女."),
 ("(1)　{予約|よやく}する", "男：土曜日のレストラン、僕が予約しとこうか。", 0, "～とこうか = ～ておこうか (申し出, offer) → the speaker (man) books it."),
 ("(2)　{使|つか}う", "男：そのパソコン、ちょっと使わせてもらえない？", 0, "使わせてもらえない？ = ～させてもらう (permission) → the man uses it."),
 ("(3)　{試|ため}す", "男：この新しいソフト、一度試してみたらどう？", 1, "～たらどう？ = suggestion (提案) → the woman tries it."),
 ("(4)　{直|なお}す", "男：この報告書、ここだけ直してくれると助かるんだけど。", 1, "～てくれると助かる = polite request → the woman fixes it."),
 ("(5)　{置|お}く", "男：この荷物、しばらくここに置かせてもらってもいいですか。", 0, "置かせてもらっても いいですか = asking permission → the man puts it there."),
 ("(6)　{電話|でんわ}する", "男：鈴木さんに、あとでお客さんに電話してもらうように、伝えといてくれる？", 2, "鈴木さんに…電話してもらうように伝えて = tell Suzuki to phone. The woman only passes the message; Suzuki makes the call."),
]

B1 = [  # (options, script, ans, thanglish)
 ("例", ["いい", "よくない"], "女：その服、すごくいいんじゃない？", 0, "いいんじゃない？ (ん + rising) = 'I think it's good'. Book 例 answer: いい."),
 ("(1)", ["{安|やす}い", "{安|やす}くない"], "女：このかばん、セールって書いてあるけど、あんまり安くないんじゃない？", 1, "安くないんじゃない？ = I think it's NOT cheap. The ～んじゃない part = 'I think'; the opinion is what comes before it: 安くない."),
 ("(2)", ["{話|はな}せる", "{話|はな}せない"], "女：田中さんって、アメリカに住んでたから、英語が話せるんじゃないかと思うけど。", 0, "話せるんじゃないかと思う = I think he CAN speak. か is there → positive guess."),
 ("(3)", ["{便利|べんり}だ", "{便利|べんり}ではない"], "女：駅から遠いし、近くに店もないし、そのアパートは便利じゃないと思います。", 1, "便利じゃないと思います = no ん, no か → plain negative: not convenient."),
 ("(4)", ["{田中|たなか}さんだ", "{田中|たなか}さんではない"], "女：あそこに立ってる人、田中さんじゃないと思う。田中さんはもっと背が高いから。", 1, "田中さんじゃないと思う (no か) = it's NOT Tanaka. The reason (he's taller) confirms it."),
 ("(5)", ["これだ", "これではない"], "女：ずっと探してたかぎって、これなんじゃない？", 0, "これなんじゃない？ (なん + rising) = 'isn't it this one?' = I think it IS this one."),
]

SECTION = {
 "book": "chokai",
 "title": "実力養成編　Ⅱ「即時応答」のスキルを学ぶ　問題形式と内容／1 最初の文を理解する（1-A・1-B）",
 "source": "新完全マスター聴解 N2 · 実力養成編 Ⅱ · pp.18–21 · CD A12–A14 (read-aloud)",
 "blocks": [
  text("質問、報告、依頼などの短い文を聞いた後、すぐにそれに合う答え方を考えます。\n短い文を聞く → 3つの選択肢を聞く → 答えを選ぶ\n\n最初に聞く文は次のようなものです。\n・質問する、依頼する、申し出る、許可を求める\n・何かについての意見・感想・主張を述べる、説明する\n・謝る、お礼を言う、褒める、あいさつする\n実際に会話に参加しているつもりで、これらの文に対する返事を選びます。",
   "問題形式と内容",
   ["即時応答(そくじおうとう) = quick response. JLPT 問題4: oru short line kekkum, udane 3 replies (a/b/c) kekkum, best reply choose pannanum. Picture-um illa, text-um illa!",
    "First line types: question, request (依頼), offer (申し出), asking permission (許可を求める), opinion/comment, apology, thanks, praise, greeting.",
    "Tip: neenga andha conversation-la irukkeenga-nu nenachu, 'naan enna solluven?'-nu think pannunga."]),
  text("最初の文を聞くときは、次のような点に注意して聞きます。\n・だれが（話し手と聞き手のどちらが）それをするか\n・その話題について話し手はどう思っているか\n・その出来事は起こったか、起こっていないか\nそのほか、会話でよく使われる表現やイントネーションに注意して聞くことが大切です。",
   "1　最初の文を理解する",
   ["First line-la 3 vishayam check pannunga: (1) yaar seyyaporaanga — speaker-a, listener-a? (2) speaker-oda opinion yes-a no-a? (3) nadandhudhaa, innum nadakkalaiyaa?",
    "Today: 1-A (who does it) and 1-B (what does the speaker think)."]),

  {"type": "table", "title": "1-A「だれがするか」を聞き取る　·　話し手がする（左）／聞き手がする（右）", "rows": TABLE,
   "explain": ["Left = the SPEAKER does it: ～させてもらえる？ (let me ～), ～てもいい？ (may I ～), ～ましょうか／～ようか (shall I ～ — offer).",
               "Right = the LISTENER does it: ～てもらえる？／～てくれない？ (please ～), ～たらどう？／～ばいいんじゃない？／～たほうがいい (suggestion).",
               "Key trick: させて (causative) = I do. て only = you do. 使わせてもらえる？ = can I use it. 使ってもらえる？ = can you use it."]},
  text("＊「～ておく」が一緒に使われる場合、「～とく」「～ときます」「～といて」「～とこう」のように音が変化します。（→「Ⅰ 音声の特徴に慣れる」）\n例　置いといてもらえる？／買っときましょうか。",
   explain="Day 4 contractions again: 置いといて = 置いておいて (listener puts it), 買っときましょうか = 買っておきましょうか (speaker offers to buy)."),

  audio("練習1-A　CD A12", "a12", "会話を聞いてください。男の人が女の人に話しています。だれがしますか。", note=OWN),
  group("練習1-A", [mcq("d5c-1a-%d" % i, w[0], MF + (["{鈴木|すずき}さん"] if i == 6 else []), w[2], "Answer: %s. %s" % (["男", "女", "鈴木さん"][w[2]], w[3]), keys=[""] * (3 if i == 6 else 2)) for i, w in enumerate(A1)],
   lead="Tap who does the action: 男 (the man speaking) or 女 (the woman listening)."),
  script("練習1-A　スクリプトと答え · open after you answer",
   [(w[0] + "　" + w[1], "Answer: %s. %s" % (["男", "女", "鈴木さん"][w[2]], w[3])) for w in A1],
   extra=[text("答え　（例）女　(1) 男　(2) 男　(3) 女　(4) 女　(5) 男　(6) 鈴木さん", "答え")]),

  text("意見や報告などの文を理解するときは、その話題について話し手がそうだと思っているか、違うと思っているかに注意します。中でも間違えやすい表現に「～じゃない（と思います）」と「～んじゃない（かと思います）」があります。",
   "1-B「話し手はどう思っているか」を聞き取る",
   "Speaker 'yes' nenaikkiraaraa 'no' nenaikkiraaraa? Biggest trap: じゃない vs んじゃない."),
  audio("1-B　例1・例2　CD A13", "a13", "例1　これじゃない。／これじゃないと思います。\n例2　これなんじゃない？／これなんじゃないかと思います。", label="A13 · computer read-aloud of the book's examples"),
  items("じゃない と んじゃない", [
   ("例1の「これじゃない」は「これではない」という否定の意味で、文末が下がります。", "これじゃない↘ = 'it's not this' (negative). Falling tone."),
   ("例2の「これなんじゃない？」は反対に「これだ」という肯定の意味で、文末が上がります。", "これなんじゃない？↗ = 'isn't it this?' = I think it IS this (positive). Rising tone, and ん/なん is there."),
   ("「と思う」に続くときは、イントネーションが同じなので、「か」があるかないかに注意して聞きます。", "With と思う the tone is the same, so listen for か: じゃないと思う = not; んじゃないかと思う = yes, I think so."),
   ("・おいしいんじゃないの？　＝　おいしいと思う\n・行ったんじゃないかな。　＝　行ったと思う\n・できないんじゃないでしょうか。　＝　できないと思う",
    "Other forms of んじゃない: んじゃないの？／んじゃないかな／んじゃないでしょうか — all = 'I think ～'. The opinion is the part BEFORE ん."),
  ], explain="Read-aloud audio can't always make the rising tone clearly, so in today's practice listen hardest for ん (なん) and か. That's also the safest way in the real exam."),

  audio("練習1-B　CD A14", "a14", "文を聞いてください。女の人の意見と合うのはどちらですか。", note=OWN),
  group("練習1-B", [mcq("d5c-1b-%d" % i, w[0], w[1], w[3], "Answer: %s. %s" % (w[1][w[3]], w[4]), keys=["", ""]) for i, w in enumerate(B1)],
   lead="Tap the option that matches the woman's opinion."),
  script("練習1-B　スクリプトと答え · open after you answer",
   [(w[0] + "　" + w[2], "Answer: %s. %s" % (w[1][w[3]], w[4])) for w in B1],
   extra=[text("答え　（例）いい　(1) 安くない　(2) 話せる　(3) 便利ではない　(4) 田中さんではない　(5) これだ", "答え")]),
 ],
}
