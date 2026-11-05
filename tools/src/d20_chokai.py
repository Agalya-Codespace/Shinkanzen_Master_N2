from _h import *
from d20_chokai_a import NOTE, N4, pick, S, M1, M2, M3
DAY = 20

N3 = ["1", "2", "3"]

M3_5 = [
 audio("問題3　5番　CD B63", "b63", None, tts=False, note=NOTE),
 pick("d20c-3-5", "5番（質問と選択肢はCDで聞きます）", N4, 0,
  ["Sensei's answer: 1.", "Question: この講演会のテーマは何ですか。 1 日本人の食生活の変化　2 1950年以降の食事の内容　3 日本人がとっている栄養　4 外国から入ってきた料理の特徴",
   "He talks about what Japanese people eat (rice → meat, dairy, oil) AND how they eat (times differ, families eat together less) → both = 食生活の変化. 2 covers only the 中身 part; 4 is only one detail.",
   "Thanglish: '食事の中身だけでなく食事の取り方も' — rendu-um cover panra word = 食生活. Adhaan 1."]),
 S("5番　スクリプト（CDから）", [
  ("講演会で先生が話しています。", ""),
  ("先生：日本では「ご飯」という言葉が、白い米だけでなく食事そのものを指すことからもわかるように、昔からたくさんの米を食べていました。", "指す(さす) = to refer to."),
  ("それが、1950年ごろからアメリカなど外国からさまざまな食べ物が入ってきて、{米|こめ}の消費量はぐんと減り、肉や乳製品を多く取るようになりました。それに伴って料理法も変化したため、多くの油を使うようになっています。", "消費量(しょうひりょう) = amount consumed. 乳製品(にゅうせいひん) = dairy. 〜に伴って = along with."),
  ("また、生活スタイルの変化により、食事の時間が平日と週末で違う、家族そろって食卓を囲む機会が減るなど、[[食事の中身だけでなく食事の取り方も昔とは大きく異なっています]]。この講演会では、このようなことをお話ししたいと思います。", "食卓を囲む = sit around the table together. → 食生活の変化."),
  ("この講演会のテーマは何ですか。\n1　日本人の食生活の変化\n2　1950年以降の食事の内容\n3　日本人がとっている栄養\n4　外国から入ってきた料理の特徴", ""),
 ], "答え　1"),
]

def Q4(n, track, prompt, opts, ans, explain):
    lines = [(prompt, "")] + [("%d　%s" % (i + 1, o), "") for i, o in enumerate(opts)]
    return [
     audio("問題4　%d番　CD %s" % (n, track.upper()), track, None, tts=False, note=NOTE),
     pick("d20c-4-%d" % n, "%d番（文と返事はCDで聞きます）" % n, N3, ans, explain, keys=N3),
     S("%d番　スクリプト（CDから）" % n, lines, "答え　%d" % (ans + 1)),
    ]

M4 = [
 audio("問題4　説明　CD B64", "b64", "問題4では、まず文を聞いてください。それから、それに対する返事を聞いて、1から3の中から、最もよいものを一つ選んでください。", tts=False, note="Real CD track (instructions)."),
 text("問題4 = 即時応答. One short line, then three replies. Decide quickly: who is talking to whom (polite or casual), and what the first line really means (request? complaint? news?).", "問題4　即時応答",
  ["Thanglish: Mudhal line-oda 'feeling' enna nu catch pannunga — request-aa, sorry-aa, surprise-aa. Adhukku match aagura reply dhaan answer. Keigo mistakes (ご覧くださいました maadhiri) irundha adhu wrong option."]),
] \
 + Q4(1, "b65", "お忙しいところすみません。ご相談したいことがあるんですが、今ちょっとよろしいでしょうか。",
      ["ええ、お構いなく。なんでしょう。", "ええ、どういたしまして。なんでしょう。", "ええ、かまいませんよ。なんでしょう。"], 2,
      ["Sensei's answer: 3.", "よろしいでしょうか = is it OK? → かまいませんよ (sure, no problem).", "お構いなく = 'please don't trouble yourself' (said when offered tea). どういたしまして = reply to thanks. Both don't fit."]) \
 + Q4(2, "b66", "最初は引き受けなきゃよかったかなと思ったんだけど…",
      ["やっぱり引き受けないほうがいいでしょ。", "やっぱり引き受けたらよかったでしょ。", "やっぱり引き受けてよかったでしょ。"], 2,
      ["Sensei's answer: 3.", "引き受けなきゃよかった = I wish I hadn't taken it on. 〜んだけど… = 'but (now it's OK)'. So the friend says: see, it was good you took it on → 引き受けてよかったでしょ.",
       "2 引き受けたらよかった = 'you should have taken it' — but they already did. Thanglish: 'Mudhalla regret, aana ippo nalla dhaan' → 3."]) \
 + Q4(3, "b67", "どうも、すっかりご無沙汰してしまって。お変わりありませんか。",
      ["ええ、ご苦労様です。", "ごめんください。", "ええ、相変わらずです。"], 2,
      ["Sensei's answer: 3.", "ご無沙汰(ごぶさた) = I haven't been in touch for a long time. お変わりありませんか = are you well as always? → 相変わらずです (same as ever).",
       "ご苦労様 = thanks for your work. ごめんください = 'excuse me' at someone's door."]) \
 + Q4(4, "b68", "あの、できたらこの荷物、ここで夕方まで預かっといてほしいんですけど。",
      ["そうですか。じゃあ、よろしくお願いします。", "わかりました。何時に取りに来ますか。", "じゃあ、できたらご連絡します。"], 1,
      ["Sensei's answer: 2.", "預かっといて = 預かっておいて (please keep it for me). The listener accepts and asks when they'll come to pick it up.",
       "1 is what the person ASKING would say. 3 misuses できたら (here できたら = if possible, not 'when it's ready')."]) \
 + Q4(5, "b69", "この間お話ししたものの実物をお持ちしたんですが。",
      ["あ、もう拝見しましたよ。", "ええ、もうご覧くださいましたよ。", "ええ、もうお見えになりましたよ。"], 0,
      ["Sensei's answer: 1.", "'I brought the actual thing we talked about.' → 'Oh, I've already seen it.' 拝見する = humble 見る, used for MY action → correct.",
       "2 ご覧くださいました is not real keigo for your own action. 3 お見えになる = 来る (someone has come). Thanglish: keigo check pannunga — en action-kku 謙譲語 (拝見)."]) \
 + Q4(6, "b70", "あれ、それ持ってっちゃっていいんですか。",
      ["うん、すごくいいんじゃないかな。", "うん、持ってっちゃったよ。", "うん、持ってってって言われたんだ。"], 2,
      ["Sensei's answer: 3.", "持ってっちゃっていい？ = is it OK to take that away? → 'Yes, I was told 持ってって (take it).' 持ってってって = 持っていって＋って (quote).",
       "1 answers 'is it good?'. 2 says 'I already took it', which doesn't answer 'may you?'."]) \
 + Q4(7, "b71", "今日、うっかりいつもの電車に乗るところだったよ。",
      ["ああ、そこから乗ったんだね。", "間違えてたら大変だったね。", "えー、いつものに乗っちゃったの。"], 1,
      ["Sensei's answer: 2.", "〜るところだった = almost did (but didn't). So they did NOT get on. → 'It would have been bad if you'd made that mistake.'",
       "3 thinks they actually got on — wrong. Thanglish: 'ところだった' = kittathatta nadandhirukkum, aana nadakkala."]) \
 + Q4(8, "b72", "この仕事、私にやらせていただけないでしょうか。",
      ["あ、そうですか。じゃあ、差し上げます。", "はい、そうですね。じゃあ、お疲れ様でした。", "わかりました。じゃあ、お願いします。"], 2,
      ["Sensei's answer: 3.", "やらせていただけないでしょうか = could you please let me do it? → OK, please do (お願いします).",
       "差し上げます = I'll give (an object) — wrong for a job. お疲れ様でした = said after work is finished."]) \
 + Q4(9, "b73", "英語の勉強、し直そうと思ってるの。書くのはともかくとして、会話ぐらいはね。",
      ["そうだね。書く練習は必要だよね。", "そうだね。話せると楽しいもんね。", "そうだね。会話なんて勉強しなくてもね。"], 1,
      ["Sensei's answer: 2.", "〜はともかくとして = leaving aside ~. She wants at least conversation. → 'Yes, it's fun when you can speak.'",
       "1 talks about writing (she put that aside). 3 says no need to study conversation — opposite."]) \
 + Q4(10, "b74", "え、タレントになりたい？　笑わせないでくれよ。",
      ["いいえ、大まじめよ。", "いいえ、笑ってなんかいないわよ。", "いいえ、すごく面白いのよ。"], 0,
      ["Sensei's answer: 1.", "笑わせないでくれよ = don't make me laugh (= you can't be serious). → No, I'm completely serious (大まじめ).",
       "Thanglish: 'Comedy pannaadha' nu solraar — 'illa, naan serious-aa dhaan solren' = 大まじめよ."]) \
 + Q4(11, "b75", "これ、使ってもらえるとありがたいんだけど。",
      ["えっ、本当にいいんですか。じゃあ、遠慮なく。", "いいえ、どうぞ。よかったらこれもいかがですか。", "どういたしまして。もう使わないものなんで。"], 0,
      ["Sensei's answer: 1.", "使ってもらえるとありがたい = I'd be glad if you used this (= please take it). → Really? Then I won't hold back (遠慮なく).",
       "2 and 3 are lines for the GIVER, not the receiver."]) \
 + Q4(12, "b76", "山田先生とお昼をご一緒したんだけど、今日に限って財布忘れちゃってさ。ご迷惑かけちゃったよ。",
      ["昼食代を払わされたんですか。", "一緒に探してくださったんですか。", "ごちそうしてもらったんですか。"], 2,
      ["Sensei's answer: 3.", "今日に限って = today of all days. Forgot wallet → 迷惑をかけた → the teacher paid → ごちそうしてもらったんですか.",
       "1 払わされた = was made to pay — but HE had no wallet. 2 searching isn't mentioned."])

M5 = [
 audio("問題5　説明　CD B77", "b77", "問題5では、長めの話を聞きます。", tts=False, note="Real CD track (instructions)."),
 text("問題5 = 統合理解. 1番: a longer talk among several people, question and options only on the CD. 2番・3番: an explanation + a conversation, two questions, options printed (see Ⅵ-2).", "問題5　統合理解",
  ["Thanglish: 2番, 3番-la printed options pakkathula notes podunga — 'yaar enna choose panraanga' nu man/woman separate-aa track pannunga."]),

 audio("問題5　1番　CD B78", "b78", None, tts=False, note=NOTE),
 pick("d20c-5-1", "1番（質問と選択肢はCDで聞きます）", N4, 2,
  ["Sensei's answer: 3.", "Question: 先生が机といすを丸く並べる一番の理由は何ですか。 1 授業中寝ている人を見つけやすいから　2 しゃべっている人を注意しやすいから　3 生徒同士でいろいろ話し合ってほしいから　4 先生も話し合いに参加したいから",
   "The teacher: お互いに話し合うことで理解を深めていく勉強スタイル / 自分たちで問題点を探していくことも必要. 1 is the girl's idea; 4 is mentioned but is not the main reason."]),
 S("1番　スクリプト（CDから）", [
  ("クラスで生徒2人と先生が話しています。", ""),
  ("男子生徒：先生、ちょっといいですか。", ""),
  ("先生：何ですか、上田君。", ""),
  ("男子生徒：あのー、こんなふうに机といすを丸く並べるの、よくないと思うんですよ。黒板見るとき首をねじらなきゃいけないんで、首が痛くなってしまうんです。", "ねじる = to twist."),
  ("先生：うーん、この授業は話し合いが多いからね。", ""),
  ("女子生徒：こうすれば先生も円の中に座って参加できるし、みんなの顔が見られていいと思いますけど。こうすると、授業中寝る人もいなくなりますし。", "→ 1 and 4 are HER points."),
  ("男子生徒：ですけど、おしゃべりが多すぎますよ。勉強のときはちゃんと前を向いてやったほうが…。", ""),
  ("女子生徒：おしゃべりしている人も、みんなで注意したらいいと思います。", ""),
  ("先生：勉強の仕方にはいろいろなスタイルがあるんだよね。[[お互いに話し合うことで理解を深めていく勉強スタイル]]もあると思うよ。みんなが前を向いていたら、意見が言いにくくなるんじゃないかな。", "→ 3."),
  ("女子生徒：そう思います。私もこのほうが話しやすいです。", ""),
  ("先生：先生の話を聞くだけじゃなくて、[[自分たちで問題点を探していくことも必要]]だよ。", ""),
  ("先生が机といすを丸く並べる一番の理由は何ですか。\n1　授業中寝ている人を見つけやすいから\n2　しゃべっている人を注意しやすいから\n3　生徒同士でいろいろ話し合ってほしいから\n4　先生も話し合いに参加したいから", ""),
 ], "答え　3"),

 audio("問題5　2番　CD B79", "b79", None, tts=False, note=NOTE),
 group("2番　特急電車", [
  pick("d20c-5-2a", "質問1　男の人は何号車に乗りますか。", ["1号車","2号車","3号車","4号車"], 0,
   ["Sensei's answer: 1 (1号車).", "He has a 自由席 ticket (自由席はあっちだね) and wants to smoke. 自由席 = 1–3号車; smoking cars = 1, 4, 10号車. Both → 1号車.",
    "Thanglish: 自由席 list (1,2,3) + 喫煙 list (1,4,10) — rendu-layum irukkuradhu 1 mattum."]),
  pick("d20c-5-2b", "質問2　女の人は何号車に乗りますか。", ["1号車","2号車","3号車","4号車"], 1,
   ["Sensei's answer: 2 (2号車).", "私、隣の車両のドアの近くに座ってる → the car next to 1号車, still 自由席 and non-smoking → 2号車."]),
 ], "Notes: 自由席 1〜3号車 ／ グリーン車 4〜6 ／ 指定席 7〜10 ／ 喫煙 1・4・10号車"),
 S("2番　スクリプト（CDから）", [
  ("駅のホームで、男の人と女の人がこれから特急電車に乗ります。", ""),
  ("アナウンス：お客様にお知らせいたします。まもなく1番線に、11時ちょうど発、特急「雪国12号」が参ります。この電車は10両編成で、グリーン車は4号車から6号車、指定席は7号車から10号車、[[自由席は{前|まえ}寄りの3両、1号車から3号車]]までとなっております。[[おたばこが吸える車両は1号車、4号車、10号車]]です。そのほかは全席禁煙となっております。", "〜両編成(りょうへんせい) = a train of ~ cars. 前寄り = toward the front."),
  ("男：えーっと、雪国12号。[[自由席]]はあっちだね。たばこ吸える車両は…っと。", ""),
  ("女：ええっ、喫煙席に乗るの？　いやよ、私気持ち悪くなっちゃうもん。ねえ、着くまで我慢できない？", "我慢(がまん) = to put up with."),
  ("男：1時間ぐらいならいいけど、3時間もなあ。喫煙席があるから喫煙ルームもないみたいだし。今日は別々の車両でいい？", ""),
  ("女：どうせずっと本読んでるんでしょ。", "どうせ = anyway."),
  ("男：まあね。じゃあ、自由席の喫煙車両はあっちだね。", "→ 1号車."),
  ("女：私、[[隣の車両]]のドアの近くに座ってるから、降りる前には来てよ。", "→ 2号車."),
  ("男：わかった。", ""),
  ("質問1　男の人は何号車に乗りますか。\n質問2　女の人は何号車に乗りますか。", ""),
 ], "答え　質問1　1　／　質問2　2"),

 audio("問題5　3番　CD B80", "b80", None, tts=False, note=NOTE),
 group("3番　あいさつについて街で話を聞く", [
  pick("d20c-5-3a", "質問1　女の学生はどのグループに入りますか。", ["Aグループ","Bグループ","Cグループ","Dグループ"], 1,
   ["Sensei's answer: 2 (Bグループ).", "She first says ママさん言葉かな (B), wavers toward C (お年寄り), and ends: 女同士なら話もしやすいし、子供のことなんかも聞きたい → the mothers in the park = B."]),
  pick("d20c-5-3b", "質問2　男の学生はどのグループに入りますか。", ["Aグループ","Bグループ","Cグループ","Dグループ"], 0,
   ["Sensei's answer: 1 (Aグループ).", "He first wants 同世代 (D), but she says 学生言葉ならこれから先たくさん聞くんじゃないの → それもそうだね. Then: 将来日本で働くことを考えて店のおじさんたちと → 商店街 = A.",
    "Thanglish: Mudhal choice change aagudhu — kadaisi-la sonna group dhaan answer."]),
 ], "Notes: A 商店街・お店の人 ／ B 公園・お母さん ／ C 市民会館・お年寄り ／ D 専門学校・学生"),
 S("3番　スクリプト（CDから）", [
  ("日本語学校で先生が話しています。", ""),
  ("先生：明日は教室での勉強ではなく、実際に街に出て日本人と話をします。4つのグループに分かれて、それぞれ違う立場の人に会って話をしてきてください。テーマはあいさつについてです。", "立場(たちば) = position, standpoint."),
  ("[[Aグループは商店街]]に行って、お店の人とお話をしてきてください。友達とお客さんとではあいさつが違うかもしれませんね。", ""),
  ("[[Bグループは公園]]に行って、子供を遊ばせているお母さんたちに話を聞いてください。お母さんたちは毎日子供と話す時間が多いですよね。そんな中で、自分も子供みたいな話し方になることはないかというのは面白いテーマですよ。", ""),
  ("[[Cグループは市民会館]]へ行って、お年寄りと話してみてください。昔と今とではあいさつに違いがあるかどうか聞いてみても面白いですね。", "お年寄り(としより) = elderly people."),
  ("[[Dグループ]]は、近くに専門学校がありますから、そこの学生さんに聞いてきてください。友達同士のあいさつとか、今の流行のあいさつは何か、皆さんも興味があるでしょう。", "流行(りゅうこう) = trend."),
  ("今日は好きなグループに入って、明日どんな質問をするか、グループの人と相談してください。", ""),
  ("女：どうしようかなあ。やっぱり、いつか自分も同じ立場になるから、ママさん言葉かな。あ、でも、おじいさんやおばあさんたちとも話してみたいから、迷うなあ。", ""),
  ("男：僕は何といっても、同世代の人がどう話すか興味があるね。", "同世代(どうせだい) = same generation → D (for now)."),
  ("女：でも、学生言葉ならこれから先たくさん聞くんじゃないの？", ""),
  ("男：それもそうだね。じゃあ、[[将来日本で働くことを考えて、店のおじさんたちと話をしてみる]]かな。", "→ A."),
  ("女：私はやっぱりこっちかな。[[女同士なら話もしやすいし、子供のことなんかも聞きたいし]]。", "→ B."),
  ("質問1　女の学生はどのグループに入りますか。\n質問2　男の学生はどのグループに入りますか。", ""),
 ], "答え　質問1　2　／　質問2　1"),
]

SECTION = {
 "book": "chokai",
 "title": "模擬試験",
 "source": "新完全マスター聴解 N2 · 模擬試験 · pp.96–103 · CD B45–B80",
 "blocks": [
  text("Today is the full mock test: 問題1 課題理解, 問題2 ポイント理解, 問題3 概要理解, 問題4 即時応答, 問題5 統合理解 — the same five parts as the real JLPT N2 聴解. Play each track once, answer, then open the script.",
   "模擬試験の進め方",
   ["Sensei: The book has no answer key or script for the 模擬試験, so every script here was transcribed from the CD and checked by me; every answer is marked as sensei's.",
    "Thanglish: Real exam maadhiri — oru dharavai mattum kelunga, pause pannaadheenga. Apram dhaan script open pannunga. Wrong-aa pona idathula 'enna word miss pannen' nu paarunga.",
    "ひらがな: まず いっかいだけ きいて こたえましょう。それから スクリプトを よんで、ききとれなかった ことばを かくにん しましょう。"]),
 ] + M1 + M2 + M3 + M3_5 + M4 + M5,
}
