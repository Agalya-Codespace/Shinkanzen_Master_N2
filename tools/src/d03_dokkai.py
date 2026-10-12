from _h import *
DAY = 3

def passage(title, paras, explain, notes=None, src=None):
    b = {"type": "passage", "title": title, "paras": paras, "explain": explain}
    if notes: b["paras"] = paras + notes
    if src: b["cite"] = "（" + src + "）"
    return b

def toi(id, q, opts, ans, explain):
    return mcq(id, "【問い】" + q, opts, ans, explain)

def kaisetsu(n, theme, iikae, choices):
    its = [{"t": theme}, {"t": iikae}] + [{"t": c} for c in choices]
    return {"type": "reveal", "label": "本の解説（別冊）：練習%d" % n,
            "children": [{"type": "items", "title": "解答・解説", "items": its}]}

def T(s): return {"t": s}

SECTION = {
 "book": "dokkai",
 "title": "1. 文章のしくみを理解する　2）［言い換え］同じ意味のほかの言葉で言う",
 "source": "新完全マスター読解 N2 · 第1部 評論・解説・エッセイなど · pp.14–21 · 例題 answers in the book; 練習 answers from 別冊 解答 pp.3–4",
 "blocks": [
  items("◆言い換えとは", [
   ("「ある言葉や文」を、「同じ意味のほかの言葉や文」に変えて書いたり、「具体的な例」などで説明したりすることがある。これを「言い換え」という。",
    "Writer oru word-a vera words-la thirumba solluvaanga, illa example kuduthu explain pannuvaanga. Idhukku per 言い換え(いいかえ) = paraphrase."),
   ("言い換えて説明していることは、大事なポイントであることが多い。",
    "Rendu thadava (vera vaarthaila) sonnaa — adhu mukkiyam! Writer repeat panradhu dhaan main point."),
   ("「問い」の選択肢も、本文とは違う表現で言い換えられていることが多いので注意しよう。",
    "Exam trick: correct option-la passage-la irukka same words irukkaadhu; paraphrase pannirukkum. Same words irukka option dhaan sila samayam trap."),
  ], explain="Day 2-la 対比 (contrast) paathom. Inniki 言い換え (paraphrase). Signal words: つまり, すなわち, 「AをBと言う／呼ぶ」. Paraphrase-a '＝' pottu link pannunga."),

  passage("☆例題4　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "{数学者|すうがくしゃ}アインシュタインや、{作曲家|さっきょくか}モーツァルトは、ただ一つの能力に{恵|めぐ}まれているから「{天才|てんさい}」なのではない。方向が全く異なる二つの能力を持っているから「{天才|てんさい}」なのだ。つまり、{物事|ものごと}の細かい部分を{詳|くわ}しく見る能力と、{物事|ものごと}の全体像を大きくつかむ能力を持ちあわせているのである。{物事|ものごと}の詳細な部分を見ていこうとするのは{職人|しょくにん}的、全体像をつかもうとするのは学者的な見方と言うこともできる。この二方向の能力をどちらも{身|み}につけていることが重要な意味を持つ。",
  ], [
   "Vocabulary: 数学者(すうがくしゃ) = mathematician. 作曲家(さっきょくか) = composer. 能力(のうりょく) = ability. 恵(めぐ)まれる = be blessed with. 天才(てんさい) = genius. 異(こと)なる = differ. 物事(ものごと) = things. 詳(くわ)しく = in detail. 全体像(ぜんたいぞう) = the whole picture. 持(も)ちあわせる = have both. 詳細(しょうさい) = details. 職人(しょくにん) = craftsman. 学者(がくしゃ) = scholar. 身(み)につける = acquire.",
   "Story: Einstein, Mozart — oru ability mattum irukkradhaala genius illa. Rendu opposite direction abilities irukku. つまり (paraphrase signal!) = detail-a paakkura ability + whole picture-a pidikkura ability. Adhaye innoru thadava: 職人的 (craftsman view) + 学者的 (scholar view). Last: 'この二方向の能力' — moonaavadhu thadava same idea!",
   "Ore idea 3 thadava vera vaarthaila: 二つの能力 = 細かい部分／全体像 = 職人的／学者的 = 二方向の能力. Adhaan main point.",
  ]),
  toi("d3d-e4", "この文章の内容として最も適切なものはどれか。", [
   "人は、職人的な見方、学者的な見方という二方向の能力を身につけるべきだ。",
   "優れた能力は「天才」だけが持っているというわけではない。",
   "「天才」には物事の全体像を大きくつかむ能力がある。",
   "「天才」は異なる二方向の能力を持ちあわせている。"], 3,
   ["Answer 4. 'Genius-ku rendu direction ability irukku' — adhaan passage solradhu.",
    "1: '～べきだ' (should) — ellarum acquire pannanum-nu sollala. 2: genius illaadhavanga pathi pesave illa. 3: true dhaan, aanaa half mattum — rendu ability-um vendum. Half-correct option = trap!"]),
  {"type": "reveal", "label": "本の解説：全体をつかもう（例題4）", "children": [
   items("1）キーワードからテーマを推測する", [("能力、「天才」　→　テーマは、天才の能力？", "Keywords: 能力, 天才 → topic = genius-oda ability.")]),
   {"type": "table", "title": "2）「言い換え」に注目する", "rowHead": True, "rows": [
     ["二つの能力", "＝"],
     ["物事の細かい部分を詳しく見る能力", "物事の全体像を大きくつかむ能力"],
     ["＝職人的", "＝学者的"],
     ["＝二方向の能力", ""],
   ], "explain": "Idhu dhaan '＝' technique: same idea-va connect pannunga. Left = detail ability = 職人的. Right = whole-picture ability = 学者的. Rendum serndhu = 二方向の能力."},
   items("3）全体をまとめる", [("「天才」は、物事の細かい部分を詳しく見る（＝職人的）能力と、物事の全体像をつかむ（＝学者的）能力という、方向が異なる二つの能力をどちらも持っている。",
     "Summary: genius-ku detail ability-um whole-picture ability-um rendum irukku.")]),
   items("選択肢と比べよう", [T("1：身につけるべきだとは書かれていない。"), T("2：天才でない人については書かれていない。"),
     T("3：全体像を大きくつかむ能力だけでは足りない。"), T("4：正解")]),
   items("ポイント", [
     ("・「言い換え」になっているところは、＝などでつなごう。", "Paraphrase-a ＝ pottu connect pannunga."),
     ("・「つまり」「すなわち」など、言い換えの接続表現に注目。□をつけよう。", "つまり = in other words. すなわち = namely. Indha words-a box pannunga."),
     ("・「（A）を（B）と言う／呼ぶ」などの表現は「言い換え」。", "'A-a B-nu solluvom/koopiduvom' = paraphrase pattern. Example 5-la paarpom: 特別な場面を「ハレ」と名付けた."),
   ]),
  ]},

  passage("☆例題5　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "{江戸|えど}時代以前、人々の{普段|ふだん}の生活はとても単調で、毎日ほぼ同じ事の繰り返しだった。特に農村は{娯楽|ごらく}もほとんどなく、食生活も貧しかった。白米や酒は{贅沢品|ぜいたくひん}で、めったに口にすることができなかった。しかし、正月や祭り、結婚式などは特別な日だった。この日だけは白米や{餅|もち}を食べ、たっぷりの酒を飲む。いい着物を着て、歌や踊りに{興|きょう}じる。このような「非日常」を思い切り楽しむことで、人々は「日常」のつらさを忘れることができた。",
   "民俗学者の{柳田國男|やなぎたくにお}は、このような特別な場面を「ハレ」、それ以外の毎日の生活を「ケ」と名付けた。昔は「ハレ」と「ケ」がはっきりと分かれていて、それが人々の生活にリズムを与えていたと考えたのである。",
   "では、現在はどうか。もちろん結婚式などは今でも人生で特別な場面であろう。しかし、近代化が進んだ結果、昔は特別な日にしかできなかったこと――おいしい物を食べたり、{綺麗|きれい}な服を着るなどということは、すっかり普通のことになった。TVだ映画だカラオケだと、{娯楽|ごらく}も日常化している。現代は「ハレ」と「ケ」の{境界|きょうかい}があいまいになっているのである。",
  ], [
   "Para 1: 江戸(えど)時代 = Edo period. 単調(たんちょう) = monotonous. 繰(く)り返(かえ)し = repetition. 農村(のうそん) = farming village. 娯楽(ごらく) = entertainment. 贅沢品(ぜいたくひん) = luxury item. めったに～ない = rarely. 餅(もち) = rice cake. 興(きょう)じる = enjoy oneself in. 非日常(ひにちじょう) = the non-everyday. Munnaadi daily life boring; festival/wedding naal mattum special — white rice, sake, nalla dress, dance. Adhanaala daily kashtam maranthaanga.",
   "Para 2: 民俗学者(みんぞくがくしゃ) = folklorist. 名付(なづ)ける = name. Special day = 「ハレ」, daily life = 「ケ」. ← 'AをBと名付けた' = paraphrase pattern! リズムを与(あた)える = give rhythm.",
   "Para 3: 近代化(きんだいか) = modernization. すっかり = completely. 日常化(にちじょうか) = become everyday. 境界(きょうかい) = boundary. あいまい = vague. Ippo nalla saapadu, nalla dress — daily vishayam aayiduchu. So ハレ／ケ boundary theliva illa.",
   "Structure: 言い換え (ハレ＝非日常＝特別な日, ケ＝日常＝普段の生活) + 対比 (昔 ↔ 現在).",
  ]),
  toi("d3d-e5", "この文章の内容として最も適切なものはどれか。", [
   "昔は「日常」と「非日常」がはっきりと分かれていたが、今はその差があまりわからなくなっている。",
   "昔の生活は単調でおもしろくなかったが、今は豊かになって日常生活も楽しいものとなっている。",
   "結婚式やお正月は昔は「非日常」の場面だったが、現在では「日常」になってしまっている。",
   "現代の人々も、昔のように「ハレ」と「ケ」をはっきりと分けて生活しなければならない。"], 0,
   ["Answer 1. ハレ＝非日常, ケ＝日常 — option 1 paraphrase panni solludhu: munnaadi theliva pirinjirundhudhu, ippo boundary vague.",
    "2: 'ippo life jolly' main point illa. 3: wedding innum special-nu passage solludhu. 4: '～なければならない' ezhudhala."]),
  {"type": "reveal", "label": "本の解説：全体をつかもう（例題5）", "children": [
   items("1）キーワードからテーマを推測する", [("「非日常」「日常」「ハレ」「ケ」　→　テーマは「非日常」と「日常」？", "Keywords-la irundhu topic: non-everyday vs everyday.")]),
   {"type": "table", "title": "2）「対比」に注目する", "rowHead": True, "rows": [
     ["江戸時代以前", "…昔は「ハレ」と「ケ」がはっきりと分かれていて"],
     ["↕ 対比", ""],
     ["現在", "…現代は「ハレ」と「ケ」の境界があいまいになっている"],
   ], "explain": "Time contrast: 昔 (theliva pirinjirundhudhu) ↔ 現在 (vague)."},
   {"type": "table", "title": "3）「言い換え」に注目する", "rows": [
     ["正月や祭り、結婚式などは特別な日", "↔", "普段の生活"],
     ["「非日常」を…楽しむ", "↔", "「日常」のつらさを忘れる"],
     ["特別な場面を「ハレ」", "↔", "毎日の生活を「ケ」"],
   ], "explain": "Left column ellaam same idea (special day = 非日常 = ハレ). Right column ellaam same idea (daily life = 日常 = ケ). Idhu dhaan 言い換え."},
   items("4）全体をまとめる", [("江戸時代以前は、「ハレ」（＝非日常）と「ケ」（＝日常）がはっきり分かれていた。現代は、その境界があいまいである。", "Summary in one line: munnaadi ハレ／ケ clear; ippo vague.")]),
   items("選択肢と比べよう", [T("1：正解"),
     T("2：昔の生活がおもしろくなくて、今の生活が楽しいということではなく、「ハレ」と「ケ」が今の生活ではっきり分かれていないことが最も重要な点である。"),
     T("3：結婚式は「今でも人生で特別な場面」と書かれている。"),
     T("4：分けて生活しなければならないとは書かれていない。")]),
  ]},

  text("Ippo neenga try pannunga. Ovvoru passage-layum: (1) '＝' pottu paraphrase pairs kandupudinga, (2) つまり／と言い換える maadhiri signals-a box pannunga, (3) appram options paarunga — correct option passage-oda words-a vera words-la sollum.",
   "🎓 練習6～9"),

  passage("練習6　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "わたしたちはふつう、{視野|しや}に入っているものはみんな見ている、と思いやすいのですが、{視野|しや}に入っていても注意していなければ見えないものです。{普段|ふだん}でもそうです、自分が足を{怪我|けが}すると、町の中には足を{怪我|けが}した人が思いの{外|ほか}に多いことに気がつきます。よく{若者|わかもの}が電車に乗って老人に席を{譲|ゆず}らないといいますが、あれは老人は{網膜|もうまく}の上には{映|うつ}っていても、意識のアンテナが働いていないのだと思います。{若者|わかもの}には{同世代|どうせだい}の{若者|わかもの}がよく目についたのは、自分の経験からも分かります。",
  ], [
   "視野(しや) = field of vision. 注意(ちゅうい) = attention. 怪我(けが) = injury. 思(おも)いの外(ほか) = unexpectedly. 若者(わかもの) = young people. 席(せき)を譲(ゆず)る = give up one's seat. 網膜(もうまく) = retina. 映(うつ)る = be reflected. 意識(いしき) = awareness. 同世代(どうせだい) = same generation. 目(め)につく = catch one's eye.",
   "Story: Kannula padradhu ellaam paakkurom-nu nenaippom, aanaa attention illaati theriyaadhu. Namakku kaal-la adi pattaa, oorla kaal adipatta aalunga neraya irukkaanga-nu notice pannuvom. Young people old people-ku seat kudukkala-na — old people retina-la theriyuraanga, aanaa 'awareness antenna' work aagala.",
   "言い換え: 「視野に入っていても注意していなければ見えない」＝「網膜の上には映っていても、意識のアンテナが働いていない」.",
  ], src="安野光雅『絵のある人生』岩波書店"),
  toi("d3d-r6", "この文章の内容として最も適切なものはどれか。", [
   "若者が老人に席を譲らないのは、老人が視野に入っていないからである。",
   "{若者|わかもの}は{同世代|どうせだい}の{若者|わかもの}に対してだけ意識のアンテナを働かせているのである。",
   "目に入ったものでも、意識を働かせていないと、実は見えていないのである。",
   "我々は、何に対してでも、意識のアンテナをよく働かせなければならない。"], 2,
   ["Answer 3. '視野に入っていても注意していなければ見えない' paraphrase = '目に入ったものでも、意識を働かせていないと見えていない'.",
    "1: opposite — 視野-la irukkaanga (retina-la padraanga); awareness dhaan illa. 2: seat example oru illustration mattum, main theme illa. 4: '～なければならない' ezhudhala."]),
  kaisetsu(6, "視野について書かれた文章である。",
   "言い換えに注目する。「視野に入っていても注意していなければ見えない」＝「網膜の上には映っていても、意識のアンテナが働いていない」",
   ["1：老人が視野に入っていないからではない。（意識していないからである。）", "2：若者のことは一つの例でしかなく、この文章のテーマではない。",
    "3：正解", "4：意識のアンテナをよく働かせなければならないとは書かれていない。"]),

  passage("練習7　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "ニュースの価値や情報を決めるのは、客観的な基準やデータだけではなく、たまたまそのニュースを担当した人の感情や好き嫌いが大きく働いている。この「感情や好き嫌い」は、「{主観|しゅかん}」と言い換えることもできる。{客観|きゃっかん}の反対。つまりテレビのニュースや新聞の記事は、何を報道するかしないか、何をニュースにするかしないかを決めるその段階で、もう客観的などというレベルではない。",
  ], [
   "価値(かち) = value. 客観的(きゃっかんてき) = objective. 基準(きじゅん) = standard. たまたま = by chance. 担当(たんとう) = in charge. 感情(かんじょう) = emotion. 好(す)き嫌(きら)い = likes and dislikes. 主観(しゅかん) = subjectivity. 報道(ほうどう) = reporting. 段階(だんかい) = stage.",
   "Story: News value-a decide panradhu objective data mattum illa — andha news handle panra aaloda feelings, likes/dislikes kooda. Idha 'subjectivity'-nu sollalaam (← 'と言い換える' — book-ae paraphrase-nu solludhu!). つまり: edha report pannanum-nu choose panra stage-laye objective illa.",
   "言い換え: 感情や好き嫌い ＝ 主観. Main point: news-la choose panra stage-laye 主観 irukku.",
  ], src="森達也『世界を信じるためのメソッド　ぼくらの時代のメディア・リテラシー』イースト・プレス"),
  toi("d3d-r7", "この文章で筆者が最も言いたいことは何か。", [
   "ニュースは、その内容を選択する時点から報道する側の主観が入っている。",
   "ニュースの価値は、それが客観的であるかどうかによって決まる。",
   "ニュースの担当者は、自分の感情や好き嫌いに気をつけるべきだ。",
   "ニュースは、客観的な基準を気にせず、主観的に報道すればよい。"], 0,
   ["Answer 1. '何を報道するかしないかを決める段階で、もう客観的…ではない' = 選択する時点から主観が入っている.",
    "2: objective mattum illa-nu dhaan passage solludhu. 3: '～べきだ' advice illa. 4: writer fact solraar, 'subjective-aa report pannunga'-nu suggest pannala."]),
  kaisetsu(7, "報道には主観が含まれることについて書かれた文章である。",
   "言い換えに注目する。「感情や好き嫌い」＝主観。何を報道するか、何をニュースにするかを決める段階で客観的でなくなる。つまり、主観が入っている。",
   ["1：正解", "2：ニュースの価値は、客観的な基準やデータ、つまり客観的な要素だけで決められているのはない。",
    "3：好き嫌いに気をつけるべきだとは書かれていない。", "4：主観的に報道すればよいという提案ではない。"]),

  passage("練習8　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "人間は{何|なん}であれ、自由が好きです。「自由」とは「{自分勝手|じぶんかって}（注1）」と考えてもらってもいいでしょう。人間は{自分勝手|じぶんかって}を好みます。だが、他人の勝手になることを嫌います。{憎|にく}みます。誰もが{自分勝手|じぶんかって}に{振|ふ}る{舞|ま}おうとすると、他人の勝手と{衝突|しょうとつ}します。自分の勝手を通そうとすると、他人の勝手を{押|お}しとどめなければなりません。またどんなに自分の勝手を{押|お}し{通|とお}そうとしても、相手のほうが強力ならば、相手の勝手に{押|お}さえ{込|こ}まれてしまうことになります。「自由」になろうと思うと、やっかいだということがわかるでしょう。",
  ], [
   "何(なん)であれ = whatever it is. 自分勝手(じぶんかって) = selfish, doing as one pleases. 好(この)む = like. 他人(たにん)の勝手(かって)になる = be at someone else's whim. 憎(にく)む = hate. 振(ふ)る舞(ま)う = behave. 衝突(しょうとつ) = clash. 押(お)しとどめる = hold back. 押(お)し通(とお)す = push through. 強力(きょうりょく) = powerful. 押(お)さえ込(こ)む = suppress. やっかい = troublesome.",
   "Story: Ellarukkum freedom pidikkum. 「自由」＝「自分勝手」 (← 'と考えてもらってもいい' = paraphrase!). Ellarum avanga ishtappadi nadandhaa, mathavanga ishtaththoda clash aagum. Namma ishtam nadakkanum-na avanga ishtatha thadukkanum; avanga strong-aa irundhaa naama adangiduvom. So 'free'-aa irukkaradhu kashtam.",
   "言い換え: 自由 ＝ 自分勝手. Main point: ellarum free-aa irukka virumbuvaanga, aanaa clash aagi kashtam (やっかい).",
  ], notes=["（注1）{自分勝手|じぶんかって}：他人のことは考えず、自分の思いどおりに行動すること。"], src="鷲田小彌太『考えることが苦手な人たちへ　10代からのプチ哲学のすすめ』こう書房"),
  toi("d3d-r8", "この文章で筆者が最も言いたいことは何か。", [
   "人は皆自由になりたいと考えるが、自分勝手な行動はやめなければならない。",
   "人は何かをさせられるのは嫌だが、完全に自由になることを好むわけでもない。",
   "人が各人の自由を勝ち取るためには、ほかの人と衝突することが重要である。",
   "人は皆自由になりたいと考えるが、他人と衝突するので大変だ。"], 3,
   ["Answer 4. やっかい (troublesome) ＝ 大変だ — paraphrase! Ellarum free-aa irukka aasai, aanaa clash aagum.",
    "1: 'selfish-aa irukka koodaadhu'-nu advice illa. 2: 'complete freedom pidikkaadhu'-nu sollala — opposite. 3: clash 'mukkiyam'-nu sollala; clash dhaan problem."]),
  kaisetsu(8, "人間の自由について書かれた文章である。",
   "言い換えに注目する。「自由」＝「自分勝手」。自分勝手に振る舞おうとすると、他人の勝手と衝突する。",
   ["1：自分勝手な行動はやめなければならないとは書かれていない。", "2：完全に自由になることを好むわけでもないとは書かれていない。",
    "3：衝突の重要性を主張しているのではない。", "4：正解"]),

  passage("練習9　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "できる人と思わせるためには{下準備|したじゅんび}が必要である。しかし、実は最大の{下準備|したじゅんび}は、{何|なん}といっても「自分を知る」ことである。",
   "というのは、できないものをできるように見せるのはかなり難しいが、自分の長所を前面に出せば、できるように見せるのはそう難しくないということがある。もう一つは、人間というのは、よほど嫌いな相手でない限り、相手の短所より長所のほうに目が行くよう出来ていることが、さまざまな心理実験で明らかにされている。いわゆる「{隣|となり}の{芝生|しばふ}は青い」現象である。",
   "だから、{欠点|けってん}を{隠|かく}そうとするより、長所を目立つようにしたほうが、できる人に見えるのだ。現実に、社会のほうも、{欠点|けってん}のない{何|なん}でも{屋|や}のような人間より、多少{欠点|けってん}はあっても、長所の{抜|ぬ}きん{出|で}た人間のほうを{重用|ちょうよう}するようになってきている。",
  ], [
   "Para 1: できる人 = capable person. 下準備(したじゅんび) = preparation. 何(なん)といっても = above all. Capable-aa theriyanum-na preparation vendum; biggest preparation = 'unnai nee therinjukko'.",
   "Para 2: というのは = the reason is. 長所(ちょうしょ) = strong point. 前面(ぜんめん)に出(だ)す = put forward. よほど～ない限(かぎ)り = unless really ～. 短所(たんしょ) = weak point. 心理実験(しんりじっけん) = psychology experiment. 隣(となり)の芝生(しばふ)は青(あお)い = the grass is greener next door (others' good points catch our eye). Reason 1: theriyaadhadha therinja maadhiri kaattradhu kashtam, aanaa strong point-a munnaadi vechaa easy. Reason 2: manushanga mathavanga weak point vida strong point-a dhaan kavanippaanga.",
   "Para 3: 欠点(けってん) = flaw. 隠(かく)す = hide. 目立(めだ)つ = stand out. 何(なん)でも屋(や) = jack of all trades. 抜(ぬ)きん出(で)る = excel. 重用(ちょうよう)する = give important posts to. Flaw-a maraikkaradha vida strong point-a highlight pannaa capable-aa theriyum.",
   "言い換え: 「できる人と思わせる」＝「できる人に見える」. 長所を前面に出す ＝ 長所を目立つようにする.",
  ], src="和田秀樹『趣味・教養を「武器」に変える　和田秀樹の\"最終最強\"知的生産術』毎日新聞社"),
  toi("d3d-r9", "この文章で筆者が最も言いたいことは何か。", [
   "自分をよく分析し、欠点が目立たないようにすれば、他人からできる人と思われる。",
   "周囲の人に自分の長所も短所も理解してもらえば、できる人と思ってもらえる。",
   "できる人と思われるには、何かをするとき、十分に準備し、欠点を補う必要がある。",
   "できる人と思われるには、自分の長所を周りの人によくわかるようにするのがよい。"], 3,
   ["Answer 4. 長所を前面に出す／目立つようにする ＝ 長所を周りの人によくわかるようにする.",
    "1: opposite — 欠点を隠そうとするより… 2: 短所 理解 pannanum-nu sollala. 3: preparation OK, aanaa 欠点を補う (cover flaws) ezhudhala."]),
  kaisetsu(9, "「できる人」と思わせるにはどうすればいいかについて書かれた文章である。",
   "言い換えに注目する。「できる人と思わせる」＝「できる人に見える」。自分の長所を前面に出せば、「できる人に見える」のである。",
   ["1：欠点が目立たないようにするとは書かれていない。", "2：自分の短所を理解してもらうとは書かれていない。",
    "3：準備することは必要だが、欠点を補う必要があるとは書かれていない。", "4：正解"]),
 ],
}
