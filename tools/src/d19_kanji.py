from _h import *
DAY = 19
TITLE = "言葉の構成と情報検索"
INTRO = "Today: Kanji 広がる漢字の知識3–4 (言葉の構成・音の変化), Goi 7章 3・4課, Bunpo 第3部 7–10課, Dokkai 第3部 情報検索, Chokai Ⅵ-2・確認問題."

P = "d19k"

WORDS = [
 ("3 言葉の構成", [["日光","にっこう","sunlight"],["親友","しんゆう","best friend"],["読書","どくしょ","reading"],["見物","けんぶつ","sightseeing"],["移動","いどう","moving"],["学習","がくしゅう","learning"],["左右","さゆう","left and right"],["父母","ふぼ","father and mother"],["故郷","こきょう","home town"],
  ["損得","そんとく","loss and gain"],["美人","びじん","beautiful woman"],["善良","ぜんりょう","good, honest"],["登山","とざん","mountain climbing"],["晴天","せいてん","fine weather"],["生死","せいし","life and death"],["身体","しんたい","body"],["着席","ちゃくせき","taking a seat"],["退職","たいしょく","retirement"],["良心","りょうしん","conscience"],["増減","ぞうげん","increase and decrease"],["救助","きゅうじょ","rescue"]]),
 ("否定の意味の漢字", [["不便","ふべん","inconvenient"],["無料","むりょう","free of charge"],["化粧品","けしょうひん","cosmetics"],["未満","みまん","under, less than"],["否決","ひけつ","voting down"],["未知","みち","unknown"],["無断","むだん","without permission"],["不順","ふじゅん","unseasonable"],["無知","むち","ignorance"],["否認","ひにん","denial"],["未婚","みこん","unmarried"],["非婚","ひこん","choosing not to marry"],["不良","ふりょう","bad, poor"],["法案","ほうあん","bill (law)"],["刑事","けいじ","detective"]]),
 ("4 音の変化", [["学科","がっか","department, subject"],["学級","がっきゅう","class"],["学校","がっこう","school"],["日記","にっき","diary"],["発表","はっぴょう","announcement"],["散歩","さんぽ","walk"],["作家","さっか","writer"],["一家","いっか","a family"],["一種","いっしゅ","a kind"],["一致","いっち","agreement"],["一方","いっぽう","one side; meanwhile"],["一般","いっぱん","general"],["結果","けっか","result"],["雑誌","ざっし","magazine"],["決定","けってい","decision"],["失敗","しっぱい","failure"],["出発","しゅっぱつ","departure"],["心配","しんぱい","worry"]]),
]

TYPES = ["a　□→■", "b　□←■", "c　□＋■", "d　□と■／□↔■"]
NEG1 = ["{未満|みまん}", "{否決|ひけつ}", "{未知|みち}", "{無断|むだん}", "{不順|ふじゅん}"]
NEG2 = ["{無知|むち}", "{否認|ひにん}", "{未婚|みこん}", "{非婚|ひこん}", "{不良|ふりょう}"]

def C(id, q, opts, ans, ex):
    return dict(mcq(id, q, opts, ans, ex, keys=[""] * len(opts)), plainKeys=["opts"])

SECTION = {
 "book": "kanji",
 "title": "広がる広げる漢字の知識　3 言葉の構成・4 音の変化",
 "source": "新完全マスター漢字 N2 · pp.112–115 · quiz answers are printed upside down in the book (p.113); your PDF has no p.114, so the 音の変化 lesson starts on p.115",
 "blocks": [
  wordlist("📋 今日の漢字リスト · Today's kanji words", WORDS,
   "Every word from today's pages. Hide a column to test yourself; tap a striped cell to peek.",
   ["Today you learn HOW two-kanji words are built, so you can guess words you've never seen.",
    "Four types: a 日光 = 日の光 (first modifies second); b 読書 = 書を読む (second is the object of the first); c 移動 = 移る＋動く (two similar meanings); d 左右 = 左と右 (pair / opposites).",
    "Sound change: 学＋校 → がっこう. When the first kanji ends in く・ち・つ and the second starts with か・さ・た・は行, you often get a small っ; は行 then turns into ぱ行 (発表 はっぴょう). After ん, は行 → ぱ行 too (散歩 さんぽ)."]),

  text("◆基本の四つのタイプ\na　□→■　□の／が／修飾■\nb　□←■　■を□\nc　□＋■　□て、■。\nd　□と■／□↔■　□と■（対になる語）", "広がる広げる漢字の知識　3　言葉の構成",
   ["Sensei: Split the word into its two kanji and ask 'how are they connected?'",
    "a □→■: the first describes the second. 日光 = 日の光 (sun's light). 美人 = 美しい人.",
    "b □←■: read it backwards — ■を□. 読書 = 書を読む. 登山 = 山に登る. Many verb+object words (like Chinese) are this type.",
    "c □＋■: two kanji with similar meaning. 移動 = 移って動く. 身体 = 身＋体.",
    "d □と■: a pair or opposites. 左右, 父母, 損得, 生死, 増減.",
    "Thanglish: Rendu kanji-um eppadi connect aagudhu nu paarunga — 'oda' (a), 'ah pannu' reverse (b), same meaning (c), pair (d)."]),

  group("Ⅰ　下線の言葉について、例にならって□に言葉を書きましょう。", [
   text("a（例）[[日光]]と水がなければ植物は育たない。　→　［日］の　→　［光］"),
   fill(P + "-1a1", "{親友|しんゆう}の結婚式でスピーチをした。　→　［%%］しい　→　［　］", ["親"], "Book: 親しい → 友(達). 親友 = a close friend."),
   fill(P + "-1a2", "　　→　［親］しい　→　［%%］", ["友", "友達"], "Book: 友（達）."),
   text("b（例）秋は[[読書]]の季節だ。　→　［読む］　←　［書］を　（書＝本の意味）"),
   fill(P + "-1b1", "家族で祭りの{見物|けんぶつ}に出かけた。　→　［%%］　←　［　］を", ["見る"], "Book: 見る ← 物を. 見物 = watching (sights, festivals)."),
   fill(P + "-1b2", "　　→　［見る］　←　［%%］を", ["物"], "Book: 物."),
   text("c（例）荷物が多い時は車での[[移動]]が便利だ。　→　［移る］　＋　［動く］"),
   fill(P + "-1c1", "日本語の{学習|がくしゅう}は面白い。　→　［%%］＋［　］", ["学ぶ"], "Book: 学ぶ ＋ 習う."),
   fill(P + "-1c2", "　　→　［学ぶ］＋［%%］", ["習う"], "Book: 習う."),
   text("d（例）[[左右]]をよく見てから道を渡ってください。　→　［左］と［右］"),
   fill(P + "-1d1", "{故郷|こきょう}の{父母|ふぼ}に手紙を書いた。　→　［%%］と［　］", ["父"], "Book: 父 と 母."),
   fill(P + "-1d2", "　　→　［父］と［%%］", ["母"], "Book: 母."),
  ], lead="Type each box. Key (book, p.113): a 親しい 友（{達|たち}）　b 見る 物　c 学ぶ 習う　d 父 母"),

  group("【クイズ1】次の下線の言葉は、上のa～dのどれになりますか。", [
   C(P + "-q1-1", "①[[{損得|そんとく}]]ばかり考えて行動する人にはなりたくない。", TYPES, 3, "Book: d. 損 (loss) と 得 (gain) — opposites."),
   C(P + "-q1-2", "②祖母は若いころこの町で評判の[[{美人|びじん}]]だった。", TYPES, 0, "Book: a. 美しい人."),
   C(P + "-q1-3", "③あの人はだれもが認める[[{善良|ぜんりょう}]]な人だ。", TYPES, 2, "Book: c. 善い＋良い — two similar meanings."),
   C(P + "-q1-4", "④[[{登山|とざん}]]に行く時は動きやすい服装がいい。", TYPES, 1, "Book: b. 山に登る (read backwards)."),
  ], lead="Key (book): ①d ②a ③c ④b"),

  group("【クイズ2】言葉の構成が同じものを結びましょう。", [
   C(P + "-q2-1", "①運動会は[[{晴天|せいてん}]]に恵まれた。", ["a 父は60歳で{退職|たいしょく}した。", "b 自分の{良心|りょうしん}に従って行動する。", "c 収入の{増減|ぞうげん}は景気に影響される。", "d 火事で逃げ遅れた人を{救助|きゅうじょ}する。"], 1, "Book: ①b. 晴天 = 晴れた天, 良心 = 良い心 — both type a (modifier → noun)."),
   C(P + "-q2-2", "②適切な判断が[[{生死|せいし}]]を分ける。", ["a 退職", "b 良心", "c 増減", "d 救助"], 2, "Book: ②c. 生↔死, 増↔減 — opposites (type d)."),
   C(P + "-q2-3", "③[[{身体|しんたい}]]の調子を整える。", ["a 退職", "b 良心", "c 増減", "d 救助"], 3, "Book: ③d. 身＋体, 救う＋助ける — similar meanings (type c)."),
   C(P + "-q2-4", "④皆さん、[[{着席|ちゃくせき}]]してください。", ["a 退職", "b 良心", "c 増減", "d 救助"], 0, "Book: ④a. 席に着く, 職を退く — verb + object (type b)."),
  ], lead="Key (book): ①b ②c ③d ④a"),

  items("◆否定の意味の漢字", [
   ("否定の意味の漢字＋■\n不（■ではない。■しない。）／無（■がない。）／未（まだ、■ない。）／{否|ひ}（■しない。）／非（■ではない。）",
    ["不 (ふ／ぶ) = not ■ / doesn't ■. 無 (む) = there's no ■. 未 (み) = not ■ yet. 否 (ひ) = doesn't ■ (refuses). 非 (ひ) = is not ■.",
     "Thanglish: 不 = illa, 無 = edhuvum illa, 未 = innum illa, 否 = maatten (reject), 非 = adhu illa."]),
   ("（例1）私の家は駅から遠いので[[不便]]だ。　［不］＋［便］{利|り}→便利ではない", "不便 = not convenient."),
   ("（例2）申し込み順に100名様に限り新発売の{化粧品|けしょうひん}を[[無料]]で差し上げます。　［無］＋［料］金→料金が要らない", "無料 = no charge."),
  ]),
  group("【クイズ3】□の中から適当な言葉を選んで（　）に入れて、文を読みましょう。", [
   text("a {未満|みまん}　b {否決|ひけつ}　c {未知|みち}　d {無断|むだん}　e {不順|ふじゅん}\n（例）{二十歳|はたち}（ a ）の人は、お酒を飲んではいけません。→ 二十歳{未満|みまん}"),
   C(P + "-q3-1", "①その{法案|ほうあん}は、反対多数で（　）された。", NEG1, 1, "Book: b 否決. 否決される = be voted down."),
   C(P + "-q3-2", "②天候（　）のため、野菜が育たなくて、農家は困っている。", NEG1, 4, "Book: e 不順. 天候不順 = unseasonable weather."),
   C(P + "-q3-3", "③地球上の（　）の世界を旅したい。", NEG1, 2, "Book: c 未知. 未知の世界 = the unknown world."),
   C(P + "-q3-4", "④彼は、会社の資料を（　）で外に持ち出したと疑われている。", NEG1, 3, "Book: d 無断. 無断で = without permission."),
   text("f {無知|むち}　g {否認|ひにん}　h {未婚|みこん}　i {非婚|ひこん}　j {不良|ふりょう}"),
   C(P + "-q3-5", "⑤体調（　）のため、休ませていただきます。", NEG2, 4, "Book: j 不良. 体調不良 = feeling unwell."),
   C(P + "-q3-6", "⑥{刑事|けいじ}は彼が盗んだと疑ったが、彼はあくまで（　）した。", NEG2, 1, "Book: g 否認. 否認する = deny (a charge)."),
   C(P + "-q3-7a", "⑦30代の女性のうち5人に一人が（　）だが、…", NEG2, 2, "Book: h 未婚 = not (yet) married."),
   C(P + "-q3-7b", "⑦…一生結婚しないという（　）の道を選ぶ人も増えている。", NEG2, 3, "Book: i 非婚 = choosing never to marry. 未婚 = not yet; 非婚 = by choice, not."),
   C(P + "-q3-8", "⑧法律のことは全く（　）なので、アドバイスをしてくださいませんか。", NEG2, 0, "Book: f 無知. 無知 = no knowledge."),
  ], lead="Key (book, p.113): ①b ②e ③c ④d ⑤j ⑥g ⑦h i ⑧f"),

  text("漢字を二つ使って言葉を作る時、読み方の音が変わることがあります。\n例えば、ガ㋗＋㋕ ⇒ ガッカ（{学|がく}＋{科|か} ⇒ {学科|がっか}）／ガ㋗＋㋖ュウ ⇒ ガッキュウ（{学|がく}＋{級|きゅう} ⇒ {学級|がっきゅう}）／ガ㋗＋㋙ウ ⇒ ガッコウ（{学|がく}＋{校|こう} ⇒ {学校|がっこう}）\n前の漢字の終わりの音が㋗で、後の漢字の始めの音がカ行（カ、キ、ク、ケ、コ）の時は、㋗は小さい㋡になります。\nこのほかにも、音が変わることがあります。\n（例）ニ㋠＋㋖ ⇒ ニッキ（{日|にち}＋{記|き} ⇒ {日記|にっき}）／ハ㋡＋㋪ョウ ⇒ ハッピョウ（{発|はつ}＋{表|ひょう} ⇒ {発表|はっぴょう}）／サ㋦＋㋭ ⇒ サンポ（{散|さん}＋{歩|ほ} ⇒ {散歩|さんぽ}）",
   "広がる広げる漢字の知識　4　音の変化",
   ["Sensei: Japanese doesn't like 'gaku-kou' — it squeezes it to がっこう. Rule: first kanji ends in ク／チ／ツ + second starts with カ／サ／タ／ハ行 → small っ.",
    "And when the second one starts with ハ行 after っ or ん, it becomes ぱ行: 発＋表 = はっぴょう, 散＋歩 = さんぽ, 心＋配 = しんぱい.",
    "Thanglish: Vaai-la vegamaa sonnaa automatic-aa っ varum. 'Gaku-kou' illa, 'gakkou'. Exam-la 'じっけん／じつげん' maadhiri trap irukkum — げ is not カ行 so no っ!"]),
  {"type": "table", "title": "音の変化のルール", "rowHead": True,
   "head": ["前の字の終わりの音＼後の字の始めの音", "カ行（小さい「ッ」）", "サ行（小さい「ッ」）", "タ行（小さい「ッ」）", "ハ行（小さい「ッ」）", "ハ行→パ行"],
   "rows": [
    ["ク", "{作家|さっか}", "―", "―", "―", "―"],
    ["チ", "{一家|いっか}", "{一種|いっしゅ}", "{一致|いっち}", "{一方|いっぽう}", "{一方|いっぽう}、{一般|いっぱん}"],
    ["ツ", "{結果|けっか}", "{雑誌|ざっし}", "{決定|けってい}", "{失敗|しっぱい}", "{失敗|しっぱい}、{発表|はっぴょう}、{出発|しゅっぱつ}"],
    ["ン", "―", "―", "―", "―", "{散歩|さんぽ}、{心配|しんぱい}"],
   ],
   "note": "Left four columns: the end sound ク・チ・ツ becomes a small「ッ」. Last column: after that「ッ」(or after ン), the ハ行 sound turns into パ行.",
   "explain": ["ク row: 作(さく)＋家(か) = さっか. Only カ行 in the book's table.",
               "チ row: 一(いち) + 家・種・致・方 → いっか・いっしゅ・いっち・いっぽう. 一般 = いっぱん.",
               "ツ row: 結(けつ)果 けっか, 雑(ざつ)誌 ざっし, 決(けつ)定 けってい, 失(しつ)敗 しっぱい, 発(はつ)表 はっぴょう, 出(しゅつ)発 しゅっぱつ.",
               "ン row: no small っ, only ハ→パ: 散(さん)歩(ほ) さんぽ, 心(しん)配(はい) しんぱい."]},
  group("Try it: 読み方を書きましょう", [
   fill(P + "-r1", "{学|がく}＋{科|か} ⇒ 学科　%%", ["がっか"], "がく＋か → がっか."),
   fill(P + "-r2", "{学|がく}＋{級|きゅう} ⇒ 学級　%%", ["がっきゅう"], "がく＋きゅう → がっきゅう."),
   fill(P + "-r3", "{日|にち}＋{記|き} ⇒ 日記　%%", ["にっき"], "にち＋き → にっき."),
   fill(P + "-r4", "{発|はつ}＋{表|ひょう} ⇒ 発表　%%", ["はっぴょう"], "はつ＋ひょう → はっぴょう (っ + ぴ)."),
   fill(P + "-r5", "{散|さん}＋{歩|ほ} ⇒ 散歩　%%", ["さんぽ"], "さん＋ほ → さんぽ."),
   fill(P + "-r6", "{一|いち}＋{般|はん} ⇒ 一般　%%", ["いっぱん"], "いち＋はん → いっぱん."),
   fill(P + "-r7", "{出|しゅつ}＋{発|はつ} ⇒ 出発　%%", ["しゅっぱつ"], "しゅつ＋はつ → しゅっぱつ."),
  ], lead="Practice from the book's examples (sensei's drill). Type the reading in hiragana."),
 ],
}
