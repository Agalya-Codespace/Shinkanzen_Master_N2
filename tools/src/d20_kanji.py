from _h import *
DAY = 20
TITLE = "模擬試験とまとめ"
INTRO = "Last day! Kanji チャレンジ (音の変化・読解), then a full 模擬試験 in Goi, Bunpo, Dokkai and Chokai. Bunpo also finishes 第3部 11・12課 first."

P = "d20k"

WORDS = [
 ("チャレンジ　音の変化", [["特色","とくしょく","characteristic"],["特定","とくてい","specific"],["特許","とっきょ","patent"],["特権","とっけん","privilege"],
  ["国立","こくりつ","national"],["国産","こくさん","domestic product"],["国境","こっきょう","border"],["国連","こくれん","the UN"],
  ["出勤","しゅっきん","going to work"],["出現","しゅつげん","appearance"],["出産","しゅっさん","childbirth"],["出題","しゅつだい","setting questions"],
  ["始発","しはつ","first train"],["開発","かいはつ","development"],["反発","はんぱつ","opposition, rebound"],["先発","せんぱつ","starting first"],
  ["一方","いっぽう","one side"],["遠方","えんぽう","distant place"],["他方","たほう","the other side"],["立方","りっぽう","cube"],
  ["再発","さいはつ","recurrence"],["活発","かっぱつ","lively"],["経費","けいひ","expenses"],["実費","じっぴ","actual cost"],["決意","けつい","determination"],["決勝","けっしょう","final (match)"],
  ["分配","ぶんぱい","distribution"],["配分","はいぶん","allocation"],["観客","かんきゃく","audience"],["客観","きゃっかん","objectivity"],
  ["私有地","しゆうち","private land"],["私用","しよう","private use"],["再建","さいけん","rebuilding"],["健在","けんざい","in good health"],["同居","どうきょ","living together"],["連休","れんきゅう","consecutive holidays"],["出品","しゅっぴん","exhibiting"],["帰京","ききょう","returning to Tokyo"]]),
 ("チャレンジ　読解 例・Ⅰ", [["卸売市場","おろしうりしじょう","wholesale market"],["鮮魚","せんぎょ","fresh fish"],["水産物","すいさんぶつ","marine products"],["供給","きょうきゅう","supply"],["消費地","しょうひち","consumption area"],["総合","そうごう","general, all-round"],["解散","かいさん","breaking up"],["開催","かいさい","holding (an event)"],
  ["癒やす","いやす","heal, soothe"],["効果","こうか","effect"],["介護","かいご","nursing care"],["負担","ふたん","burden"],["高齢者","こうれいしゃ","elderly person"],["患者","かんじゃ","patient"],["衛生的","えいせいてき","hygienic"],["感染症","かんせんしょう","infectious disease"],["評判","ひょうばん","reputation"],["上々","じょうじょう","excellent"],
  ["特別養護老人ホーム","とくべつようごろうじんホーム","nursing home"],["症状","しょうじょう","symptom"],["有効性","ゆうこうせい","effectiveness"],["実証試験","じっしょうしけん","verification test"],["指摘","してき","point out"],["認知症","にんちしょう","dementia"],["孤独","こどく","loneliness"],["活躍","かつやく","activity, success"],["軽減","けいげん","reduction"]]),
 ("チャレンジ　読解 Ⅱ", [["職員","しょくいん","staff member"],["禁止","きんし","ban"],["庁内文書","ちょうないぶんしょ","internal government document"],["記載","きさい","record, mention"],["不快","ふかい","unpleasant"],["権利","けんり","right"],["明文化","めいぶんか","stipulate in writing"],["掲示","けいじ","notice, posting"],["勤務時間","きんむじかん","working hours"],["服装","ふくそう","clothing"],
  ["無精ヒゲ","ぶしょうヒゲ","stubble"],["苦情","くじょう","complaint"],["対処","たいしょ","deal with"],["憲法","けんぽう","constitution"],["容認","ようにん","approval, tolerance"],["全面禁止","ぜんめんきんし","total ban"],["違反","いはん","violation"],["可能性","かのうせい","possibility"],["配慮","はいりょ","consideration"],["侵害","しんがい","infringement"]]),
]

def AB(id, word, ans, yomi, ex):
    return group(word, [
     dict(choose(id + "a", "音が変わる？", ["A　変わる", "B　変わらない"], 0 if ans == "A" else 1, ex), plainKeys=["opts"]),
     fill(id + "b", "読み方：%%", [yomi], ex),
    ], scored=False)

def MARU(id, q, ans, ex):
    return dict(choose(id, q, ["○", "×"], 0 if ans else 1, ex), plainKeys=["opts"])

SECTION = {
 "book": "kanji",
 "title": "チャレンジ　音の変化・読解",
 "source": "新完全マスター漢字 N2 · pp.116–121 · the book prints no answers for these チャレンジ pages (only the 読解 例 is solved), so the answers below are sensei's, checked against the 原文 on p.121",
 "blocks": [
  wordlist("📋 今日の漢字リスト · Today's kanji words", WORDS,
   "Every word from today's pages. Hide a column to test yourself; tap a striped cell to peek.",
   ["Last kanji day! Two challenges: ① 音の変化 — will the sound change (っ / ぱ行) or not? ② 読解 — read a newspaper article by looking ONLY at the kanji and katakana words.",
    "Thanglish: Inniku kanji book mudiyudhu. Sound change rule-a apply panni paarunga, apram newspaper article-a 'kanji mattum' vechu guess pannunga."]),

  # ---------- 音の変化 Ⅰ ----------
  text("Ⅰ　次の言葉で、音が変わるものにA、変わらないものにBを書きなさい。下に読み方を書きなさい。\n（例）特（トク）\n　1．特色（B）とくしょく　2．特定（B）とくてい　3．特許（A）とっきょ　4．特権（A）とっけん",
   "チャレンジ　音の変化",
   ["Sensei: Remember yesterday's rule. A kanji ending in ク・キ・チ・ツ becomes small っ when the next kanji starts with カ行 (and ツ also before サ行・タ行). ツ ＋ ハ行 → っ＋パ行. ン ＋ ハ行 → ン＋パ行 (sometimes).",
    "In the example: 特(トク)＋色(しょく) → サ行 after ク: no change, とくしょく. 特＋定(てい) → タ行 after ク: no change. 特＋許(きょ) → カ行: とっきょ. 特＋権(けん) → カ行: とっけん.",
    "Thanglish: 'ku' kanji-ku apram 'ka-gyo' vandhaa dhaan っ. 'tsu' kanji-ku apram ka/sa/ta-gyo ellaathukkum っ, ha-gyo vandhaa っ + pa."]),
  group("①国（コク）", [
   AB(P + "-1-1", "1．国立", "B", "こくりつ", "国(こく)＋立(りつ): ラ行 → no change. こくりつ."),
   AB(P + "-1-2", "2．国産", "B", "こくさん", "こく＋さん: サ行 after ク → no change. こくさん."),
   AB(P + "-1-3", "3．国境", "A", "こっきょう", "こく＋きょう: カ行 after ク → っ. こっきょう."),
   AB(P + "-1-4", "4．国連", "B", "こくれん", "こく＋れん: ラ行 → no change. こくれん (= 国際連合, the UN)."),
  ], lead="Answers are sensei's (the book prints none here)."),
  group("②出（シュツ）", [
   AB(P + "-2-1", "1．出勤", "A", "しゅっきん", "しゅつ＋きん: カ行 after ツ → っ. しゅっきん."),
   AB(P + "-2-2", "2．出現", "B", "しゅつげん", "しゅつ＋げん: ガ行 (voiced) → no change. しゅつげん."),
   AB(P + "-2-3", "3．出産", "A", "しゅっさん", "しゅつ＋さん: サ行 after ツ → っ. しゅっさん."),
   AB(P + "-2-4", "4．出題", "B", "しゅつだい", "しゅつ＋だい: ダ行 (voiced) → no change. しゅつだい."),
  ]),
  group("③発（ハツ）", [
   AB(P + "-3-1", "1．始発", "B", "しはつ", "発 comes SECOND after し (not ン or っ) → stays はつ. しはつ."),
   AB(P + "-3-2", "2．開発", "B", "かいはつ", "かい＋はつ: no change. かいはつ."),
   AB(P + "-3-3", "3．反発", "A", "はんぱつ", "はん＋はつ: after ン, ハ→パ. はんぱつ."),
   AB(P + "-3-4", "4．先発", "A", "せんぱつ", "せん＋はつ: after ン, ハ→パ. せんぱつ."),
  ]),
  group("④方（ホウ）", [
   AB(P + "-4-1", "1．一方", "A", "いっぽう", "いち＋ほう: チ＋ハ行 → っ＋パ. いっぽう."),
   AB(P + "-4-2", "2．遠方", "A", "えんぽう", "えん＋ほう: after ン, ホ→ポ. えんぽう."),
   AB(P + "-4-3", "3．他方", "B", "たほう", "た＋ほう: no change. たほう."),
   AB(P + "-4-4", "4．立方", "A", "りっぽう", "りつ＋ほう: ツ＋ハ行 → っ＋パ. りっぽう."),
  ]),

  # ---------- 音の変化 Ⅱ ----------
  group("Ⅱ　下線の言葉の読み方を書きなさい。", [
   fill(P + "-2a", "①このような事件の再発（a）を防ぐための対策について、皆さんからの活発なご意見をお願いします。　a 再発：%%", ["さいはつ"], "再(さい)＋発(はつ): no change. さいはつ = recurrence."),
   fill(P + "-2b", "　b 活発：%%", ["かっぱつ"], "かつ＋はつ → かっぱつ (っ + パ). = lively, active."),
   fill(P + "-2c", "②調査を依頼された場合、調査料金のほかに、調査にかかった経費についても実費をお支払い願います。　c 経費：%%", ["けいひ"], "けい＋ひ: no change. けいひ = expenses."),
   fill(P + "-2d", "　d 実費：%%", ["じっぴ"], "じつ＋ひ → じっぴ. = actual cost."),
   fill(P + "-2e", "③絶対勝つぞという強い決意を胸にして、選手たちは決勝戦の会場に向かった。　e 決意：%%", ["けつい"], "けつ＋い: ア行 → no change. けつい = determination."),
   fill(P + "-2f", "　f 決勝：%%", ["けっしょう"], "けつ＋しょう: サ行 → っ. けっしょう(せん) = final match."),
   fill(P + "-2g", "④事業で得た収入を分配するに当たっては、事業に参加した程度に応じて配分を決めようと思う。　g 分配：%%", ["ぶんぱい"], "ぶん＋はい: after ン, ハ→パ. ぶんぱい."),
   fill(P + "-2h", "　h 配分：%%", ["はいぶん"], "はい＋ぶん: 分 is ぶん here (not ふん). はいぶん = allocation."),
   fill(P + "-2i", "⑤会場の火事で怖い思いをしたにもかかわらず、記者の質問に答える観客の発言は、冷静で客観的なものだった。　i 観客：%%", ["かんきゃく"], "かん＋きゃく: no change. かんきゃく = audience."),
   fill(P + "-2j", "　j 客観（{的|てき}）：%%", ["きゃっかん"], "きゃく＋かん → きゃっかん(てき) = objective."),
  ], lead="Type the reading in hiragana. Watch the pairs: the same two kanji in the other order can change differently (分配 ぶんぱい / 配分 はいぶん)."),

  # ---------- 音の変化 Ⅲ ----------
  group("Ⅲ　＿＿と同じ意味になるように、□から1字選んで□に入れなさい。読み方も書きなさい。", [
   text("［動　用　健　建　有］\n（例）ビルの火事で、消防自動車が3台現場に出た。⇒出［動］した。（しゅつどう）"),
   fill(P + "-3-1", "①ここは個人が持っている土地ですから、入ってはいけません。⇒{私|し}［%%］地", ["有"], "私有地(しゆうち) = land a private person owns."),
   fill(P + "-3-1y", "　読み方：%%", ["しゆうち"], "し＋ゆう＋ち: no change."),
   fill(P + "-3-2", "②会社のパソコンは、個人的な目的に使ってはいけません。⇒{私|し}［%%］禁止です。", ["用"], "私用禁止(しようきんし) = no private use."),
   fill(P + "-3-2y", "　読み方：%%", ["しようきんし"], "しよう きんし."),
   fill(P + "-3-3", "③この寺は、2年前の台風で{倒壊|とうかい}したが、昨年もう一度建てなおされた。⇒再［%%］された。", ["建"], "再建(さいけん) = rebuilt. Not 健 (health)!"),
   fill(P + "-3-3y", "　読み方：%%", ["さいけん"], "さい＋けん: no change."),
   fill(P + "-3-4", "④ご両親は、お元気でいらっしゃいますか。⇒ご［%%］在ですか。", ["健"], "ご健在(けんざい) = alive and well (polite)."),
   fill(P + "-3-4y", "　読み方：%%", ["ごけんざい", "けんざい"], "ごけんざい."),
   text("［京　連　居　品］"),
   fill(P + "-3-5", "⑤私は、大学卒業後も両親と一緒に住んでいます。⇒同［%%］しています。", ["居"], "同居(どうきょ) = living together."),
   fill(P + "-3-5y", "　読み方：%%", ["どうきょ"], "どう＋きょ."),
   fill(P + "-3-6", "⑥来週は、3日間連続している休みがあります。⇒［%%］休", ["連"], "連休(れんきゅう) = consecutive holidays."),
   fill(P + "-3-6y", "　読み方：%%", ["れんきゅう"], "れん＋きゅう."),
   fill(P + "-3-7", "⑦{展覧会|てんらんかい}に、写真を作品として出しました。⇒出［%%］しました。", ["品"], "出品(しゅっぴん) = submit a work to an exhibition. しゅつ＋ひん → しゅっぴん (sound change!)."),
   fill(P + "-3-7y", "　読み方：%%", ["しゅっぴん"], "しゅっぴん."),
   fill(P + "-3-8", "⑧社長は、来週大阪から東京へ帰ります。⇒帰［%%］します。", ["京"], "帰京(ききょう) = return to Tokyo (the capital)."),
   fill(P + "-3-8y", "　読み方：%%", ["ききょう"], "き＋きょう."),
  ], lead="Type one kanji in the box, then the reading. Answers are sensei's."),

  # ---------- 読解 例 ----------
  text("長い文章を読む時、漢字の言葉を読むことで、大体の内容が分かることがあります。知らない言葉でも、読めたり意味が分かったりする言葉もあるはずです。さあ、チャレンジしてみましょう。\n\n例）東京都{卸売市場|おろしうりしじょう}見学と{鮮魚|せんぎょ}お買い物　日帰りツアー\n①　の中はインターネットの記事の一部です。漢字と片仮名の言葉だけに注意して読んで、内容を想像しましょう。\n\n　東京都中央卸売市場…、……私たち…食生活…欠かすこと…水産物…供給…。我が国最大…消費地…抱える巨大総合卸売市場…。まずはT市場…ご案内活気…市場…お買い物…お楽しみ…。その後、T市場内…自由見学…。市場見学…後…、T…お寿司…ご昼食…。ご昼食後、解散…。最少開催人数…6。T市場見学…鮮魚お買い物日帰りツアー…ご予約…電話…お受付も…。",
   "チャレンジ　読解",
   ["Sensei: In a real newspaper you won't know every word. Trick: read only the kanji and katakana words (they carry the meaning) and guess the content.",
    "Here: 卸売市場 = wholesale market, 水産物 = seafood, 供給 = supply, 総合 = all kinds (not only fish!), 解散 = the group breaks up, 最少開催人数 = minimum number of people for the tour to run.",
    "Thanglish: Hiragana-va skip pannunga. Kanji mattum padichaa 'market tour, fish, shopping, sushi lunch, phone booking' nu story theriyum."]),
  items("②この記事の内容と合っているものに○、合っていないものに×（本の答え）", [
   ("1．（○）ここでは、魚や貝を売っている。", "→ keyword: …水産物…供給… = 「魚や貝を売っている」. ○"),
   ("2．（×）ここでは、魚や貝以外は売っていない。", "→ keyword: 巨大総合卸売市場. 総合 = they sell everything, not only fish. ×"),
   ("3．（○）ここで、買い物をしたあと見学をする。", "→ まずはT市場…お買い物… その後、T市場内…自由見学. ○"),
   ("4．（○）この日帰りツアーは、電話で予約できる。", "→ …ご予約…電話…お受付も…. ○"),
  ], lead="◆問題の解き方のヒント：記事から関係のあるキーワードを探す → 問題文とキーワードを比較する。"),

  # ---------- 読解 Ⅰ ----------
  text("以下は新聞の見出しと記事の一部です。\n①見出しを見てください。知らない漢字があっても、調べたり質問したりしないで、どんな記事か、想像してください。\n\n【見出し】ロボットに{癒|い}やし効果　介護者の負担減も",
   "Ⅰ　子ぐま型ロボット",
   ["Sensei: The headline: 'Robots have a healing effect — and reduce the carers' burden too.' 癒やし(いやし) = healing/comfort. 介護者(かいごしゃ) = carer. 負担減(ふたんげん) = burden reduction.",
    "Thanglish: Headline-la 'robot → healing effect' and 'carers-oda burden kuraiyudhu' — rendu point."]),
  group("この記事は、子ぐまの{形|かたち}をしたロボットの話だ。", [
   fill(P + "-r1a", "その［ a ］には、…　a：%%", ["ロボット"], "a = ロボット (the robot itself has the effect)."),
   fill(P + "-r1b", "高齢者を癒やす［ b ］がある。　b：%%", ["効果", "癒やし効果"], "b = 効果 (癒やし効果 in the headline)."),
   fill(P + "-r1c", "高齢者を［ c ］する人の…　c：%%", ["介護"], "c = 介護 (介護者 = a person who 介護する)."),
   fill(P + "-r1d", "…［ d ］を減らすこともできる。　d：%%", ["負担"], "d = 負担 (負担減 = 負担を減らす)."),
  ], lead="Sensei's model answers (the book prints none)."),
  text("ロボット…触れ合い…通じ…高齢者…{患者|かんじゃ}…心…{癒|い}やす「ロボットセラピー」…注目…。……ロボット…安全…衛生的…アレルギー…{感染症|かんせんしょう}…心配もない。利用者…評判…上々だ。\nA市…特別養護老人ホーム、……。…暮らすSさん（85）…お気に入り…F研究所…開発…子ぐま型のロボット…。「…、お元気ですか」…子ぐま…話しかけられ、Sさん…「元気ですよ」…ほほ{笑|え}む。\n……「ロボット…触れ合った後…、症状…よくなる」……事務主任…話す。……ロボットセラピー…有効性…{調|しら}…実証試験…進めて…。研究グループ…H教授…「ロボット…使う…介護者…負担…減る効果…大…」…{指摘|してき}…。",
   "②記事の漢字の言葉と片仮名の言葉だけに注意して読んでください。"),
  group("③記事の内容と合っているものに○、合っていないものに×", [
   MARU(P + "-r1-1", "1．このロボットは、子供のために開発された。", False, "× — it's 子ぐま型 (bear-cub shaped), but it was made for 高齢者・患者 (ロボットセラピー in an old people's home)."),
   MARU(P + "-r1-2", "2．このロボットを使うと、アレルギーや{感染症|かんせんしょう}が心配される。", False, "× — …アレルギー…感染症…心配もない. No worry."),
   MARU(P + "-r1-3", "3．このロボットを使っている人からの評判はいい。", True, "○ — 利用者…評判…上々だ. 上々 = excellent."),
   MARU(P + "-r1-4", "4．このロボットは、人と話ができる。", True, "○ — 「…、お元気ですか」…子ぐま…話しかけられ、Sさん…「元気ですよ」. The bear talks to her and she answers."),
   MARU(P + "-r1-5", "5．このロボットを使った高齢者が元気になった例がある。", True, "○ — 「ロボット…触れ合った後…、症状…よくなる」."),
   MARU(P + "-r1-6", "6．このロボットの効果の調査は、終了している。", False, "× — 実証試験…進めて… = the tests are still going on."),
  ], lead="Sensei's answers, checked against the 原文 (p.121)."),
  items("④「{癒|い}やす」は記事から考えて、どんな意味だと思いますか。", [
   ("（答えの例）心や体の苦しみ・つかれをやわらげて、楽にすること。", "癒やす(いやす) = to heal, soothe, comfort. 心を癒やす = make someone feel calm and happy. 'Manasukku nimmadhi kudukkaradhu.'"),
  ]),
  group("⑤次の言葉を読んでください。", [
   fill(P + "-r1y1", "1．高齢者　%%", ["こうれいしゃ"], "こうれいしゃ = elderly person."),
   fill(P + "-r1y2", "2．上々　%%", ["じょうじょう"], "じょうじょう = excellent (々 repeats the kanji)."),
   fill(P + "-r1y3", "3．有効性　%%", ["ゆうこうせい"], "ゆうこうせい = effectiveness."),
   fill(P + "-r1y4", "4．実証　%%", ["じっしょう"], "じつ＋しょう → じっしょう (sound change!) = proof by testing."),
   fill(P + "-r1y5", "5．介護　%%", ["かいご"], "かいご = nursing care."),
   fill(P + "-r1y6", "6．負担　%%", ["ふたん"], "ふたん = burden."),
  ]),

  # ---------- 読解 Ⅱ ----------
  text("①見出しを見てください。知らない言葉があっても、調べたり質問したりしないで、どんな記事か、想像してください。\n\n【見出し】I市職員はヒゲ禁止\n…庁内文書で「不快に思う市民も」…「伸ばすかどうか自分で決めるのは権利」との声も",
   "Ⅱ　I市職員はヒゲ禁止",
   ["Sensei: 'City I bans beards for its staff. An internal document says some citizens find them unpleasant… but some say it's your right to decide whether to grow one.'",
    "職員(しょくいん) = staff. 禁止(きんし) = ban. 庁内文書(ちょうないぶんしょ) = internal office document. 不快(ふかい) = unpleasant. 伸ばす = grow (hair). 権利(けんり) = right."]),
  group("I市の職員は、…", [
   fill(P + "-r2a", "［ a ］を…　a：%%", ["ヒゲ", "ひげ", "髭"], "a = ヒゲ."),
   fill(P + "-r2b", "［ b ］ことが禁止された。　b：%%", ["伸ばす", "のばす"], "b = 伸ばす."),
   fill(P + "-r2c", "理由は、［ c ］が…　c：%%", ["市民"], "c = 市民."),
   fill(P + "-r2d", "［ d ］に思うから。　d：%%", ["不快"], "d = 不快."),
   choose(P + "-r2e", "禁止するのは、e｛いい・しかたがない・おかしい｝という意見もある。", ["いい", "しかたがない", "おかしい"], 2, "e = おかしい. 「伸ばすかどうか自分で決めるのは権利」との声も → some people think the ban is wrong."),
  ], lead="Sensei's model answers."),
  text("I市…職員…「ヒゲ禁止」…明文化…。…18日…{掲示|けいじ}…。「勤務時間…自由…服装…いいわけではありません。…不快に思う市民…禁止……。\n……、現在ヒゲ…伸ばして…職員…ゼロ。…{無精|ぶしょう}ヒゲ…苦情…寄せられる…。…「…。苦情…対処…」…。\nしかし、{憲法|けんぽう}学者…田中{春雄|はるお}さくら大学教授…「…、きれい…整えられたヒゲ…社会的…容認されて…。全面禁止…憲法違反…可能性…」…述べている。",
   "②記事の漢字の言葉と片仮名の言葉だけに注意して読んでください。"),
  group("③記事の内容と合っているものに○、合っていないものに×", [
   MARU(P + "-r2-1", "1．I市では、市長が職員に「ヒゲを禁止する」と話した。", False, "× — it was 明文化 (written) and 掲示 (posted on the office LAN), not said by the mayor."),
   MARU(P + "-r2-2", "2．I市の担当者は、勤務時間中の服装は一定の制限があると考えている。", True, "○ — 「勤務時間…自由…服装…いいわけではありません」 = you can't wear anything you like at work."),
   MARU(P + "-r2-3", "3．市民からヒゲを伸ばした職員について、文句を言われた。", True, "○ — …無精ヒゲ…苦情…寄せられる… 苦情 = complaint = 文句."),
   MARU(P + "-r2-4", "4．ヒゲを伸ばしている職員はいるが、皆きれいに整えている。", False, "× — 現在ヒゲ…伸ばして…職員…ゼロ. Nobody has a beard now."),
   MARU(P + "-r2-5", "5．ヒゲを伸ばすことを全面的に禁止することは{憲法|けんぽう}に{違反|いはん}する可能性があると、憲法学者の一人は述べている。", True, "○ — 全面禁止…憲法違反…可能性…述べている."),
  ], lead="Sensei's answers, checked against the 原文 (p.121)."),
  items("④「{無精|ぶしょう}ヒゲ」はどんな意味だと思いますか。", [
   ("長期休みの後などに無精ヒゲになった職員に対して苦情が寄せられることがあった。", "The full sentence from the article."),
   ("（答えの例）{剃|そ}らないで、そのまま伸ばしてしまった、手入れをしていないヒゲ。", "無精(ぶしょう) = lazy. 無精ヒゲ = stubble you got because you were too lazy to shave (e.g. after a long holiday). 'Shave pannaama vandha thaadi.'"),
  ]),
  group("⑤次の言葉を読んでください。", [
   fill(P + "-r2y1", "1．庁内文書　%%", ["ちょうないぶんしょ"], "ちょうないぶんしょ."),
   fill(P + "-r2y2", "2．不快　%%", ["ふかい"], "ふかい."),
   fill(P + "-r2y3", "3．明文化　%%", ["めいぶんか"], "めいぶんか = put in writing."),
   fill(P + "-r2y4", "4．対処する　%%", ["たいしょ"], "たいしょ(する) = deal with.", suffix="する"),
   fill(P + "-r2y5", "5．容認する　%%", ["ようにん"], "ようにん(する) = accept, tolerate.", suffix="する"),
   fill(P + "-r2y6", "6．全面禁止　%%", ["ぜんめんきんし"], "ぜんめんきんし = total ban."),
  ]),

  # ---------- 原文 ----------
  {"type": "reveal", "label": "原文（p.121）を読む", "children": [
   {"type": "passage", "title": "Ⅰ「ロボットに{癒|い}やし効果　介護者の負担減も」", "paras": [
    "ロボットとの触れ合いを通じて高齢者や患者の心を癒やす「ロボットセラピー」が注目されている。{認知症|にんちしょう}の症状改善などに効果がみられる例もある。動物の癒やし効果を{狙|ねら}うアニマルセラピーに似ているが、ロボットは安全で衛生的でアレルギーや感染症の心配もない。利用者の評判も上々だ。",
    "{埼玉県|さいたまけん}{上尾市|あげおし}の特別養護老人ホーム、パストーン{浅間台|あさまだい}。ここに暮らす{坂井|さかい}ウメさん（仮名、85）のお気に入りは{富士通|ふじつう}研究所（{川崎市|かわさきし}）が開発した子ぐま型のロボットだ。「こんにちは、お元気ですか」と子ぐまに話しかけられ、坂井さんは「元気ですよ」とほほ{笑|え}む。",
    "坂井さんは要介護度3の{軽度|けいど}の認知症だが「ロボットと触れ合った後は、症状がよくなる」とパストーン浅間台の{米岡利彦|よねおかとしひこ}事務主任は話す。認知症が進んで友人が作れず、孤独な高齢者もいる。そういう人ほど「あっと驚くような改善効果がある」（米岡氏）という。",
    "パストーン浅間台ではソニー製犬型ロボット「AIBO」なども使い、ロボットセラピーの有効性を調べる実証試験を進めている。研究グループの{筑波|つくば}学院大学の{浜田利満|はまだとしみつ}教授は「ロボットを使うことで介護者の負担が減る効果は大きい」と指摘する。介護人材の不足が指摘されているが、ロボットが老人ホームなどで活躍することで負担軽減につながる可能性もある。",
    "（後略）（{川合智之|かわいともゆき}）",
   ], "cite": "（日本経済新聞　2010年5月14日）", "explain": [
    "Robot therapy: robots comfort old people and patients. Safe, hygienic, no allergies or infections. A woman (85) with mild dementia loves a bear-cub robot that greets her. Staff say her symptoms improve. Tests of effectiveness are still going on. A professor says robots greatly reduce carers' burden.",
    "Thanglish: Kanji mattum padichu guess pannadhu correct-a nu ippo full article-la check pannunga."]},
   {"type": "passage", "title": "Ⅱ　{伊勢崎市|いせさきし}職員はヒゲ禁止／庁内文書に記載「不快に思う市民も」／「人格権{侵害|しんがい}の可能性」との声も", "paras": [
    "{群馬県|ぐんまけん}{伊勢崎市|いせさきし}は、職員の「ヒゲ禁止」を明文化した。職員が{閲覧|えつらん}する庁内LANのページで18日に掲示した。不快に感じる市民に{配慮|はいりょ}したとしているが、行き過ぎを指摘する声もある。",
    "19日からクールビズに切り替えることを通知する文書の中で示した。「{執務|しつむ}時間はプライベートな時間ではなく、全くの自由な服装をして良い訳ではありません。{髭|ひげ}についても不快に思う市民もいるため禁止します」としている。",
    "職員課によると、現在ヒゲを伸ばしている職員はいない。ただ、長期休みの後などに無精ヒゲになった職員に対して苦情が寄せられることがあり、個別に注意してきた。担当者は「市役所も市民サービスの場。苦情には対処しなければならない」と話す。",
    "しかし、県弁護士会人権{擁護|ようご}委員長の{春山典勇|はるやまふみお}弁護士は「無精ヒゲはともかく、きれいに{整|ととの}えられたヒゲは社会的に容認されている。全面禁止は人格権の侵害に当たる可能性がある」と指摘する。総務省公務員課では「全国の{自治体|じちたい}の規定を{把握|はあく}しているわけではないが、{髪形|かみがた}やヒゲなどについて規定したり、規定が問題になったりした例は聞いたことがない」としている。",
    "（{木下|きのした}こゆる）",
   ], "cite": "（朝日新聞　2010年5月20日）", "explain": [
    "Isesaki City wrote a beard ban into its rules (posted on the office LAN). Reason: some citizens feel uncomfortable; work hours aren't private time. No staff have beards now, but complaints came about stubble after long holidays. A lawyer says neat beards are socially accepted and a total ban may violate personal rights.",
    "Note: the practice page used 'I市' and '憲法学者 田中春雄さくら大学教授' — the real article quotes a lawyer (弁護士) and says 人格権の侵害. The ○× answers are the same."]},
  ]},
 ],
}
