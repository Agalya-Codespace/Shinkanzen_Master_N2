from _h import *
DAY = 17

def FB(id, q, ans, explain):
    return fill(id, q, ans if isinstance(ans, list) else [ans], explain)

def PICK(id, q, opts, ans, explain, keys):
    return mcq(id, q, opts, ans, explain, keys=keys)

N4 = ["1", "2", "3", "4"]

def star(id, q, opts, ans, order, explain):
    return PICK(id, q, opts, ans, ["Answer %d. Correct order: %s" % (ans + 1, order), explain], N4)

# ================= 第2部 2課 文の組み立て-2 名詞を説明する形式 (pp.142–145) =================
K2 = [
 text("名詞を説明するには、名詞に「の」をつけて前に置く、形容詞を用いる、文の終わりを普通形にして前に置く以外に、次のような形式があります。",
  title="第2部　2課　文の組み立て-2　名詞を説明する形式",
  explain=["Sensei: When a phrase describes a NOUN, the grammar word in front changes shape. ～について + verb, but ～についての + noun. ～にもとづいて + verb, but ～にもとづいた／もとづく + noun.",
           "Thanglish: Verb-a describe pannumbodhu て-form; noun-a describe pannumbodhu の／た／辞書形. ★ questions-la idhu dhaan key clue — after ★ slot oru noun irundhaa, adhukku munnaadi の-form or た-form varum.",
           "Four patterns today: ① particle + の + noun, ② 助詞相当語 + の + noun, ③ 助詞相当語 in た-form / dictionary form + noun, ④ という・との + noun (content)."]),
 items("1　助詞＋の＋名詞", [
  ("・東京駅まで行く切符 → 東京駅**までの**［切符］", "まで + の + noun: a ticket to Tokyo Station."),
  ("・{踏|ふ}み切りで起こった事故 → 踏み切り**での**［事故］", "で + の → での: an accident at the level crossing."),
  ("・両親とした話し合い → 両親**との**［話し合い］", "と + の → との: a talk with my parents."),
  ("・母にあげる贈り物 → 母**への**［贈り物］（×　母にの贈り物）", "に cannot take の. Use へ + の → への: a present for my mother. ×にの is wrong — remember this!"),
 ]),
 items("2　助詞相当語＋の＋名詞", [
  ("・就職するにあたって必要な準備 → 就職する**にあたっての**［準備］（第1部1課）", "にあたって + verb → にあたっての + noun: preparation for getting a job."),
  ("・試験開始に際して伝える注意事項 → 試験開始**に際しての**［注意事項］（第1部1課）", "に際して → に際しての: instructions given at the start of the exam."),
  ("・新しい監督のもとで行う練習 → 新しい監督**のもとでの**［練習］（第1部8課）", "のもとで → のもとでの: practice under the new coach."),
  ("・大使館を通じて行う連絡 → 大使館**を通じての**［連絡］（第1部4課）", "を通じて → を通じての: contact through the embassy."),
  ("・親として果たす責任 → 親**としての**［責任］（第1部19課）", "として → としての: responsibility as a parent."),
 ]),
 items("3　助詞相当語のた形・辞書形＋名詞（て形 → た形）", [
  ("・民謡をもとにして作った歌 → 民謡**をもとにした**［歌］（第1部8課）", "をもとにして → をもとにした + noun: a song based on a folk song."),
  ("・経験に基づいて判断する → 経験**に基づいた**［判断］（第1部8課）", "に基づいて → に基づいた: a judgement based on experience."),
  ("・計画表に沿って作業を進める → 計画表**に沿った**作業の［進行］（第1部8課）", "に沿って → に沿った: progress of work following the schedule."),
  ("・年齢に応じて運動量を調整する → 年齢**に応じた**［運動量］の調整（第1部9課）", "に応じて → に応じた: exercise amount suited to age."),
 ]),
 items("3　助詞相当語のた形・辞書形＋名詞（て形 → 辞書形）", [
  ("・工事は5年にわたって続けられた → 5年**にわたる**［工事］（第1部4課）", "にわたって → にわたる: construction lasting five years."),
  ("・桜をはじめとしていろいろな花が咲く → 桜**をはじめとする**いろいろな［花］（第1部4課）", "をはじめとして → をはじめとする: many flowers, starting with cherry blossoms."),
  ("・事故原因に関して調べる → 事故原因**に関する**［調査］（第1部7課）", "に関して → に関する: an investigation into the cause."),
  ("・目上の人に対して礼儀正しくする → 目上の人**に対する**［礼儀］（第1部7課）", "に対して → に対する: politeness toward superiors."),
  ("・要望にこたえて予算を組み替えた → 要望**にこたえる**予算の［組み替え］（第1部7課）", "にこたえて → にこたえる: reorganising the budget in response to requests."),
  ("・創立者の精神に基づいて教育する → 創立者の精神**に基づく**［教育］（第1部8課）", "に基づいて → に基づく: education based on the founder's spirit (に基づいた is also fine)."),
  ("・政府の方針に沿って開発を計画する → 政府の方針**に沿う**［開発計画］（第1部8課）", "に沿って → に沿う: a development plan in line with government policy."),
  ("・体力向上に伴って気力も回復する → 体力向上**に伴う**気力の［回復］（第1部9課）", "に伴って → に伴う: recovery of energy that comes with better fitness."),
  ("・地震によって津波が起きた → 地震**による**［津波］（第1部16課）", "によって → による: a tsunami caused by the earthquake."),
  ("・京都において会議が開かれた → 京都**における**［会議］（第1部A）", "において → における: the conference in Kyoto."),
 ]),
 items("4　「～という・～との」＋名詞（内容を説明する場合）", [
  ("・弟が学校の窓ガラスを割った**という**［知らせ］", "という + noun = the content of the news: news that my brother broke a school window."),
  ("・リンさんは話がとても面白い**という**［評判］", "a reputation that Lin is very entertaining."),
  ("・兄が結婚する**との**［手紙］", "との = という (written style): a letter saying my brother is getting married."),
  ("＊同時に形容詞や、「その」「あの」「そんな」などでも説明する場合は、ふつうそれらを名詞のすぐ前に置く。", "Big ★ tip: if there's also an adjective or その／あの／そんな, it goes right before the noun, AFTER the という clause."),
  ("・兄が結婚するという　**うれしい**［手紙］", "という clause → adjective → noun."),
  ("・おばけが出るという　**変な**［うわさ］", "a strange rumour that a ghost appears."),
  ("・日本チームが金メダルを取ったという　**あの**［ニュース］", "that news that Japan won gold."),
 ]),
]
K2 += [
 group("練習1　どちらか適当な方を選びなさい。", [
  PICK("d17b-k2-1-1", "1　（a 現場へ　b 現場への）{直行|ちょっこう}するときは、先に知らせてください。", ["現場へ", "現場への"], 0, "Key a. Next word is a verb (直行する) → plain particle へ.", ["a", "b"]),
  PICK("d17b-k2-1-2", "2　あしたの会では（a 外国から　b 外国からの）お客様が歌ったり踊ったりするそうで、楽しみです。", ["外国から", "外国からの"], 1, "Key b. Next word is a noun (お客様) → からの.", ["a", "b"]),
  PICK("d17b-k2-1-3", "3　（a 向こうから　b 向こうからの）バスが来ますが、公園行きでしょうか。", ["向こうから", "向こうからの"], 0, "Key a. 向こうから modifies the verb 来ます (the bus is coming from over there).", ["a", "b"]),
  PICK("d17b-k2-1-4", "4　（a 母に　b 母への）プレゼントしたいと思って、花を買いに行った。", ["母に", "母への"], 0, "Key a. プレゼントしたい is a verb here (プレゼントする), so 母に.", ["a", "b"]),
  PICK("d17b-k2-1-5", "5　{本田|ほんだ}氏は有能な経営者（a として　b としての）{国|くに}の内外で知られている。", ["として", "としての"], 0, "Key a. として + 知られている (verb).", ["a", "b"]),
  PICK("d17b-k2-1-6", "6　本製品ご使用（a にあたって　b にあたっての）下記のような点にご注意ください。", ["にあたって", "にあたっての"], 0, "Key a. にあたって links to ご注意ください (verb). 下記のような点 is the object of 注意, not modified by にあたって.", ["a", "b"]),
  PICK("d17b-k2-1-7", "7　数学の歴史（a について　b についての）本を探した。", ["について", "についての"], 1, "Key b. Next word is the noun 本 → についての本.", ["a", "b"]),
  PICK("d17b-k2-1-8", "8　若者の職業意識（a に関して　b に関する）研究所で調査した結果を雑誌に発表した。", ["に関して", "に関する"], 0, "Key a. に関して goes with 調査した: 'surveyed (about young people's job attitudes) at the institute'. It's not 'an institute about…'.", ["a", "b"]),
  PICK("d17b-k2-1-9", "9　彼は有名なクラシック音楽（a をもとにして　b をもとにした）日本人向けに編曲した歌を作っています。", ["をもとにして", "をもとにした"], 0, "Key a. をもとにして goes with the verb 編曲した (arranged, based on classical music).", ["a", "b"]),
  PICK("d17b-k2-1-10", "10　この店はパーティーの予算（a に応じて　b に応じた）{献立|こんだて}が{好評|こうひょう}だ。", ["に応じて", "に応じた"], 1, "Key b. Next word is a noun (献立 = menu) → に応じた献立.", ["a", "b"]),
  PICK("d17b-k2-1-11", "11　1週間（a にわたって　b にわたる）特別研修が明日で終わる。", ["にわたって", "にわたる"], 1, "Key b. 1週間にわたる特別研修 (noun).", ["a", "b"]),
  PICK("d17b-k2-1-12", "12　電気製品は法律（a に基づいて　b に基づく）{処理|しょり}によって、リサイクルが進められる。", ["に基づいて", "に基づく"], 1, "Key b. 法律に基づく処理 (noun).", ["a", "b"]),
  PICK("d17b-k2-1-13", "13　君の言い方はお客様（a に対して　b に対する）失礼ではないですか。", ["に対して", "に対する"], 0, "Key a. に対して失礼だ — 失礼 here works as a ナ-adjective predicate (失礼ではない), not a noun being described.", ["a", "b"]),
 ], lead="Key (別冊 p.7): 1a 2b 3a 4a 5a 6a 7b 8a 9a 10b 11b 12b 13a. Rule: look at the next word. Noun → の／た／辞書形. Verb or adjective → て-form / plain particle."),
 group("練習2　次の文の＿★＿に入る最もよいものを1・2・3・4の中から一つ選びなさい。", [
  star("d17b-k2-2-1", "1　新しい店をオープンする＿＿ ＿＿ ★ ＿＿かたまってきた。", ["の","ようやく","にあたって","{方針|ほうしん}が"], 3, "にあたって → の → 方針が → ようやく", "にあたっての + noun (方針). 'The plan for opening the new shop has finally taken shape.'"),
  star("d17b-k2-2-2", "2　市民の＿＿ ＿＿ ★ ＿＿目指しています。", ["街づくりを","願いに","こたえる","しっかり"], 2, "願いに → しっかり → こたえる → 街づくりを", "にこたえる + noun (街づくり). しっかり modifies こたえる."),
  star("d17b-k2-2-3", "3　今世紀に＿＿ ＿＿ ★ ＿＿この世からなくすことだ。", ["課題の一つは","最大の","人種差別を","おける"], 0, "おける → 最大の → 課題の一つは → 人種差別を", "における + noun. 'One of the biggest issues of this century is to remove racism from the world.'"),
  star("d17b-k2-2-4", "4　今朝の新聞に、8歳の子が＿＿ ＿＿ ★ ＿＿記事が載っていた。", ["という","一人で","びっくりするような","全国を旅した"], 0, "一人で → 全国を旅した → という → びっくりするような", "という clause first, then the describing word (びっくりするような) right before the noun 記事."),
  star("d17b-k2-2-5", "5　母が日本へ来る＿＿ ＿＿ ★ ＿＿大好きな食品が数々送られてきた。", ["とともに","との","兄からの","知らせ"], 3, "との → 兄からの → 知らせ → とともに", "との知らせ (content) and 兄からの知らせ (source). 'Along with my brother's news that Mum is coming to Japan, lots of my favourite foods arrived.'"),
  star("d17b-k2-2-6", "6　地球温暖化に＿＿ ＿＿ ★ ＿＿面でも深刻な問題である。", ["経済的な","影響は","天候の変化の","よる"], 1, "よる → 天候の変化の → 影響は → 経済的な", "による + noun. 経済的な goes right before 面."),
  star("d17b-k2-2-7", "7　うちの子は、夜遅く寝て＿＿ ＿＿ ★ ＿＿習慣がついてしまった。", ["遅く起きる","困った","という","朝は"], 2, "朝は → 遅く起きる → という → 困った", "という + adjective (困った) + noun (習慣)."),
  star("d17b-k2-2-8", "8　気温の変化に＿＿ ＿＿ ★ ＿＿楽しみにもなっている。", ["景色の","人々の暮らしの","移り変わりは","伴う"], 2, "伴う → 景色の → 移り変わりは → 人々の暮らしの", "に伴う + noun. 'The change of scenery that comes with temperature changes is also a pleasure in people's lives.'"),
  star("d17b-k2-2-9", "9　母から、＿＿ ＿＿ ★ ＿＿写真とともに届いた。", ["メールが","いい香りの","という","花が咲いた"], 2, "メールが → 花が咲いた → という → いい香りの", "という clause, then the adjective phrase (いい香りの) right before 写真."),
  star("d17b-k2-2-10", "10　この週刊誌に、現地で＿＿ ＿＿ ★ ＿＿記事が載っている。", ["事実に","調べた","基づく","くわしく"], 0, "くわしく → 調べた → 事実に → 基づく", "に基づく + noun (記事). くわしく modifies 調べた."),
  star("d17b-k2-2-11", "11　マニュアル＿＿ ＿＿ ★ ＿＿できないと思います。", ["に沿った","いい営業は","だけでは","対応"], 2, "に沿った → 対応 → だけでは → いい営業は", "に沿った + noun (対応). 'Just following the manual, you can't do good sales.'"),
  star("d17b-k2-2-12", "12　現代の若者の、＿＿ ＿＿ ★ ＿＿先生はどう思われますか。", ["政治","無関心","に対する","について"], 1, "政治 → に対する → 無関心 → について", "に対する + noun (無関心), then について + 思う."),
 ], lead="Key (別冊 p.7): 1-4 2-3 3-1 4-1 5-4 6-2 7-3 8-3 9-3 10-1 11-3 12-2."),
]

# ================= 第2部 3課 文の組み立て-3 「～ない」がつく文法形式 (pp.146–147) =================
def NR(form, nai, example, ka, explain):
    return {"t": "**%s ＋ %s**　%s　（%s課）" % (form, nai, example, ka), "explain": explain}

K3 = [
 text("N2の文法形式には否定の形「～ない」がつくものが多いです。「ない」がどんな言葉とつながっているかを覚えておくと、効率的に文を組み立てることができるでしょう。",
  title="3課　文の組み立て-3　「～ない」がつく文法形式",
  explain=["Sensei: So many N2 forms end in ない. In a ★ question, if the line ends in ない, ask yourself which piece is its partner (わけが, どころでは, ようが, しか, に越したことは…). Put that pair together first.",
           "Thanglish: 'ない' paathaa udane adhoda partner-a theydu. Partner-um ない-um pakkam pakkam varum — andha rendu slot fix aanaa, meedhi rendu easy."]),
 items("ないにつながる形", [
  NR("～わけが", "ない", "あの子が事故を起こす**わけがない**。", "12", "There's no way that child caused an accident."),
  NR("～どころでは", "ない", "外は小雨**どころではない**。大荒れだ。", "12", "It's far from a light drizzle outside — it's a storm."),
  NR("～わけでは", "ない", "わたしは毎日早起きする**わけではない**。", "12", "It's not that I get up early every day."),
  NR("～というわけでは", "ない", "勉強は楽しくない**というわけではない**。", "12", "It's not that studying isn't fun."),
  NR("～というものでは", "ない", "安ければいい**というものではない**。", "12", "Cheap isn't automatically good."),
  NR("～ようが", "ない", "そんな質問には答え**ようがない**。", "18", "There's no way to answer such a question."),
  NR("～どころでは", "ない", "暑くてマラソンする**どころではない**。", "18", "It's too hot — running a marathon is out of the question."),
  NR("～しか／～よりほか", "ない", "謝って許してもらう**しかない**。／銀行からお金を借りる**よりほかない**。", "23", "The only thing to do is apologise. / There's no choice but to borrow from the bank."),
  NR("～ものでは", "ない", "人の悪口など言う**ものではない**。", "24", "You shouldn't speak ill of others."),
  NR("～ことは", "ない", "そんなに心配する**ことはありません**よ。", "24", "There's no need to worry that much."),
  NR("～てしかたが", "ない", "このごろ目が疲れ**てしかたがない**。", "25", "My eyes have been terribly tired lately."),
  NR("～わけには", "いかない", "ここで仕事を辞める**わけにはいかない**。", "18", "I can't quit my job now."),
  NR("～に", "違いない／相違ない", "この商品は売れる**に違いない**。／この治療法は効果的である**に相違ない**。", "22", "This product will surely sell. / This treatment is surely effective."),
  NR("～に", "すぎない", "ただやるべきことをやった**にすぎない**。", "23", "I only did what I had to do."),
  NR("～に", "ほかならない", "仕事は生活のため**にほかならない**。", "23", "Work is nothing but a means of living."),
  NR("～に", "越したことはない", "早めに行く**に越したことはない**。", "23", "It's best to go early."),
  NR("～て", "たまらない", "のどが渇い**てたまらない**。", "25", "I'm dying of thirst."),
  NR("～て", "ならない", "検査の結果が気になっ**てならない**。", "25", "I can't stop worrying about the test results."),
  NR("～ないでは／～ずには", "いられない", "お酒を飲ま**ないではいられない**。／おかしくて笑わ**ずにはいられなかった**。", "25", "I can't help drinking. / It was so funny I couldn't help laughing."),
  NR("～ないわけに(は)", "いかない", "病院へ行か**ないわけにはいかない**。", "25", "I have to go to the hospital."),
  NR("～ざるを", "得ない", "この説明は不十分と言わ**ざるを得ない**。", "25", "I have to say this explanation is insufficient."),
 ]),
 group("練習1　次の文の＿★＿に入る最もよいものを1・2・3・4の中から一つ選びなさい。", [
  star("d17b-k3-1", "1　これは難しい＿＿ ＿＿ ★ ＿＿ない。", ["読める","5歳の子に","わけが","漢字だから"], 0, "漢字だから → 5歳の子に → 読める → わけが", "わけがない. 'It's a hard kanji, so there's no way a 5-year-old can read it.'"),
  star("d17b-k3-2", "2　せっかくの連休に子供が＿＿ ＿＿ ★ ＿＿ずっと子供のそばにいた。", ["遊びに行く","熱を出して","ではなく","どころ"], 3, "熱を出して → 遊びに行く → どころ → ではなく", "どころではなく. 'My child got a fever on the long weekend, so going out was out of the question.'"),
  star("d17b-k3-3", "3　この病気は＿＿ ＿＿ ★ ＿＿時間をかけて体質改善をしなければならない。", ["治る","という","薬を飲めば","ものではなく"], 1, "薬を飲めば → 治る → という → ものではなく", "というものではない. 'This illness isn't one that's cured just by taking medicine.'"),
  star("d17b-k3-4", "4　知らないことは＿＿ ＿＿ ★ ＿＿友達にしつこく聞かれた。", ["ある人の","ないのに","問題について","答えようが"], 0, "答えようが → ないのに → ある人の → 問題について", "ようがない. 'Though I couldn't possibly answer what I didn't know, a friend kept asking me about someone's problem.'"),
  star("d17b-k3-5", "5　初めは単なる＿＿ ＿＿ ★ ＿＿わかって驚いた。", ["事実だと","すぎないと","うわさに","思っていたことが"], 3, "うわさに → すぎないと → 思っていたことが → 事実だと", "にすぎない. 'I was surprised to find that what I'd thought was just a rumour was true.'"),
  star("d17b-k3-6", "6　最近、最後まで＿＿ ＿＿ ★ ＿＿番組が多い。", ["おもしろい","いられない","見ずには","ような"], 3, "見ずには → いられない → ような → おもしろい", "ずにはいられない. 'Lately there are many shows so good you can't stop watching till the end.'"),
  star("d17b-k3-7", "7　今後どうなるか＿＿ ＿＿ ★ ＿＿ありませんよ。", ["今から心配する","わからない","ことを","ことは"], 0, "わからない → ことを → 今から心配する → ことは", "ことはない. 'No need to worry now about what nobody knows yet.'"),
  star("d17b-k3-8", "8　どんな時にも＿＿ ＿＿ ★ ＿＿、お金には代えられないものもある。", ["お金は","越したことは","あるに","ないが"], 1, "お金は → あるに → 越したことは → ないが", "に越したことはない. 'It's always better to have money, but some things money can't replace.'"),
  star("d17b-k3-9", "9　父が＿＿ ＿＿ ★ ＿＿わけにはいかなかった。", ["{失望|しつぼう}する","話す","本当のことを","かと思うと"], 2, "失望する → かと思うと → 本当のことを → 話す", "わけにはいかない. 'When I thought how disappointed Dad would be, I couldn't tell him the truth.'"),
  star("d17b-k3-10", "10　人生には、時間が過ぎるのを＿＿ ＿＿ ★ ＿＿ある。", ["待つ","しかない","静かに","ことも"], 1, "静かに → 待つ → しかない → ことも", "しかない. 'In life there are times when all you can do is quietly wait for time to pass.'"),
  star("d17b-k3-11", "11　この仕事が無事に＿＿ ＿＿ ★ ＿＿、{心|こころ}から感謝している。", ["チームワークが","終わったのは","ほかならず","よかったからに"], 3, "終わったのは → チームワークが → よかったからに → ほかならず", "にほかならない. 'That this job ended safely is thanks to nothing but good teamwork.'"),
  star("d17b-k3-12", "12　明日にでも＿＿ ＿＿ ★ ＿＿わけではありませんが、{慎重|しんちょう}に考えたほうがいいですよ。", ["気持ちも","という","会社を辞めたい","わからない"], 0, "会社を辞めたい → という → 気持ちも → わからない", "わからないわけではない. 'I understand wanting to quit tomorrow, but think it over carefully.'"),
 ], lead="Key (別冊 p.7): 1-1 2-4 3-2 4-1 5-4 6-4 7-1 8-2 9-3 10-2 11-4 12-1."),
]

# ================= 第3部 1課 始めと終わりが正しく対応した文 (pp.150–153) =================
P3 = [
 text("文はいくつか連なって一続きのまとまり（文章）になります。しかし、一文一文がただ並んでいるだけでは文章とは言えません。一連の文がまとまって文章という単位になるには、文がゆるやかな決まりに従ってつながっている必要があります。文章にまとまりを与えるゆるやかな決まりが「文章の文法」と呼ばれるものです。",
  title="実力養成編　第3部　文章の文法",
  explain=["Sensei: 第3部 is for JLPT 文法 問題9 (文章の文法): a passage with gaps, and you choose the connector, the ending, the こそあ word or the right voice so the passage flows.",
           "Thanglish: Oru oru sentence-um correct-aa irundhaa podhaadhu — sentences ellaam oru story maadhiri connect aaganum. That 'connection grammar' dhaan 文章の文法."]),
 text("文章にまとまりを持たせるためには、文と文とが自然につながるようにすることが大切です。その基本として、それぞれの文も始めと終わりが正しく対応していなければなりません。それには、以下のことに注意する必要があります。",
  title="1課　始めと終わりが正しく対応した文",
  explain=["Sensei: Today's lesson: the START of a sentence decides its END. If you start with 主語は (what is it?), end with a noun / adjective / verb that answers it. If you start with なぜなら, end with から(だ). If you start with ～のは (reason), end with ～ためだ.",
           "Thanglish: Aarambam-um mudivum match aaganum — 'なぜなら' sonna 'からだ'-la mudikkanum. Idhu dhaan 問題9-la romba common trap."]),
 items("A　主語と述語の対応 ── 主語と述語の関係には次の四つの型があります。長い文では主語と述語が離れていますから、注意が必要です。", [
  ("**何が(は)＋何だ。**（名詞＋名詞）　ここは50年前、静かな農村だった。／事故の原因はスピードの出しすぎである。", "Noun is noun. ここ … 農村だった; 原因 … 出しすぎである. 'The cause of the accident is speeding' — not 'speeding caused'."),
  ("**何が(は)＋どうだ。**（名詞＋イ・ナ形容詞）　富士山は雪景色が特に素晴らしい。／健康な生活をおくるには、良い生活習慣が大切だ。", "Noun + adjective. 雪景色が素晴らしい; 生活習慣が大切だ."),
  ("**何が(は)＋どうする。**（名詞＋動詞）　明日からYホールでゴッホの展覧会が開かれる。／今年は、この地方は4回も台風の被害を受けた。", "Noun + verb. 展覧会が開かれる (passive, because the exhibition is held); この地方は被害を受けた."),
  ("**何が(は)＋ある・いる。**（名詞＋ある・いる）　駅前には自転車置き場が数か所ある。／わたしは今、ゆっくりテレビを見る時間がない。", "Noun + ある／いる／ない. 置き場がある; 時間がない."),
 ]),
 items("B　文末の制限-1　決まった文末をとる表現", [
  ("**1．なぜなら・というのは・なぜかというと　＋～から(ため)である**　→第3部10課\n例・わたしは結局{国|くに}へは帰らないで、日本に残ることにした。というのは、日本の精神風土がわたしに合っていると思われたからである。", "Start with なぜなら／というのは／なぜかというと → must end with ～からだ／ためだ. 'I decided to stay in Japan. The reason is that Japan's spiritual climate seemed to suit me.'"),
  ("**2．～かというと　＋「～」を否定する文**\n例・この作家の作品がすべて歴史的なものばかりかというと、そんなことはない。中には軽いタッチの旅行案内もある。", "～かというと → followed by a denial (そんなことはない／そうではない). 'Are all his works historical? Not at all — some are light travel guides.'"),
  ("**3．～の(＝理由・原因)は　＋…から(ため)である・…である**\n例・今年の{米|こめ}の収穫量がいつもの年より少なかったのは、夏、天候が安定しなかったためである。\n・わたしは教師の道を選んだ。迷いなく選んだのは、教師だった父の影響だろう。", "～のは (the reason/cause slot) → ends in ～ためだ／からだ／(noun)だ. 'The rice harvest was smaller because the summer weather was unstable.'"),
 ]),
]
P3[-1] = items("B　文末の制限-1　決まった文末をとる表現", [
  ("**1．なぜなら・というのは・なぜかというと　＋～から(ため)である**　→第3部10課\n例・わたしは結局{国|くに}へは帰らないで、日本に残ることにした。というのは、日本の精神風土がわたしに合っていると思われたからである。", "Start with なぜなら／というのは／なぜかというと → must end with ～からだ／ためだ. 'I decided to stay in Japan. The reason is that Japan's spiritual climate seemed to suit me.'"),
  ("**2．～かというと　＋「～」を否定する文**\n例・この作家の作品がすべて歴史的なものばかりかというと、そんなことはない。中には軽いタッチの旅行案内もある。", "～かというと → followed by a denial (そんなことはない／そうではない). 'Are all his works historical? Not at all — some are light travel guides.'"),
  ("**3．～の(＝理由・原因)は　＋…から(ため)である・…である**\n例・今年の{米|こめ}の収穫量がいつもの年より少なかったのは、夏、天候が安定しなかったためである。\n・わたしは教師の道を選んだ。迷いなく選んだのは、教師だった父の影響だろう。", "～のは (the reason/cause slot) → ends in ～ためだ／からだ／(noun)だ. 'The rice harvest was smaller because the summer weather was unstable.'"),
  ("**4．～には　＋…がいる・…がある・…が多い・…が見られる**\n例・この地球上には、貧しいために教育を受けられない子供たちがいる。\n・このアンケート調査には、いくつか不十分な点がある。", "Place／thing + には → ～がいる／ある／多い／見られる (existence). 'On this earth there are children who can't get an education because of poverty.'"),
  ("**5．～には　＋…が必要だ・…が便利だ・…がかかる・…なければならない**\n例・我々は大きな仕事を頼まれた。期待に応えるにはしっかり協力し合うことが必要だ。\n・わたしの教育方針を理解してもらうには時間がかかる。丁寧に説明していかなければならない。", "Verb (dictionary) + には (= in order to) → 必要だ／便利だ／かかる／なければならない. 'To meet expectations, we need to cooperate firmly.'"),
 ])
P3 += [
 items("C　文末の制限-2　決まった文末をとる副詞", [
  ("**全く・たいして・めったに・少しも・決して・なにも・必ずしも　→ 否定**\nわたしは進学することは全く考えていない。／車の修理にはたいして費用はかからなかった。／こんな素晴らしい景色はめったに見られない。／健康についてはわたしは少しも心配していない。／わたしは料理に化学調味料は決して使いません。／なにもそんなに怒ることはないでしょう。／値段が高いものが必ずしもいいとは限らない。", "These adverbs need a negative ending. 必ずしも → とは限らない; なにも → ことはない."),
  ("**どうも・どうやら・もしかしたら・恐らく・まさか・きっと　→ 推量・否定の推量**\nあの二人はどうやら恋人同士のようだ。／もしかしたら、林さんは今日来ないかもしれない。／恐らく週末は忙しくなるだろう。／まさか林さんは不合格にはならないだろう。／彼は今ごろきっと困っているに違いない。", "Guessing adverbs → guessing endings: どうやら～ようだ, もしかしたら～かもしれない, 恐らく～だろう, まさか～ないだろう, きっと～に違いない."),
  ("**まるで・今にも　→ 様態**\n地面に桜が散って、まるで雪が降ったかのようだ。／あの子は今にも泣き出しそうな顔をしている。", "まるで～ようだ (as if); 今にも～そうだ (about to)."),
  ("**一段と・ますます・次第に・徐々に　→ 変化**\n最近、太郎は一段と大人っぽくなった。／今後、経済は次第に回復していくだろう。", "Change adverbs → change verbs: ～なる, ～ていく, ～てくる."),
  ("**いったい・果たして　→ 質問**\nいったい君は何を考えているのか。／果たしてわたしの予想は当たるだろうか。", "いったい～か (what on earth…?); 果たして～だろうか (I wonder if really…)."),
  ("**すでに　→ 完了**\nすでに会場の準備は整っている。", "すでに → ～ている／～た (already done)."),
 ]),
 group("練習1　どちらか適当な方を選びなさい。", [
  PICK("d17b-31-1-1", "1　今、一番楽しみなのは、", ["富士山に登って頂上から日の出を見たい。", "来週のパーティーで世界の各地から来た人たちと交流することだ。"], 1, "Key b. ～のは → noun ending (～ことだ). a ends in たい, which doesn't answer 'what I look forward to most is…'.", ["a", "b"]),
  PICK("d17b-31-1-2", "2　アンケートに答えた人の中には、", ["政治には全く期待できないという人もいた。", "27%の人が、政治には期待できないと答えた。"], 0, "Key a. ～の中には → ～人もいた (existence, rule B4).", ["a", "b"]),
  PICK("d17b-31-1-3", "3　都会で一人暮らしをする上で気をつけるべきことは、", ["防犯と日常の食事である。", "防犯と食事には特に注意する必要がある。"], 0, "Key a. ～ことは → noun + である (rule A).", ["a", "b"]),
  PICK("d17b-31-1-4", "4　最近の新入社員には、", ["指示を受けてからでないと行動できない傾向が見られる。", "どうも指示を待ってからでないと行動できないらしい。"], 0, "Key a. ～には → 傾向が見られる (rule B4).", ["a", "b"]),
  PICK("d17b-31-1-5", "5　この事故の原因は、", ["運転手が長時間労働のため、睡眠不足だったようだ。", "運転手の長時間労働による睡眠不足であるという。"], 1, "Key b. 原因は → (noun) である (rule A: noun = noun).", ["a", "b"]),
  PICK("d17b-31-1-6", "6　この複雑なデータを処理するには", ["パソコンを使ってすぐやってしまおう。", "パソコンを使っても半日はかかる。"], 1, "Key b. Verb + には (in order to) → かかる (rule B5).", ["a", "b"]),
 ], lead="Key (別冊 p.7): 1b 2a 3a 4a 5b 6b."),
 group("練習2　どちらか適当な方を選びなさい。", [
  text("マクラメが似合う季節になった。マクラメ編みのテーブルセンターやベルトなどが（①）。マクラメとは、ひもを何度も結び合わせて作っていく（②）。ひものような細長いものなら何でも使える。麻糸、ビニールのひも、毛糸など。材料費がそれほど（③）、道具も全く（④）、だれでも作れる。\n　マクラメ（macrame）という（⑤）、今は立派な英語になっているが、もともとは（⑥）、ミクラマ（miqrama）といい、交差して結ぶという意味である。独特の編み方、結び方はイスラム文化の中で生まれた人類の最も古い技術の（⑦）。その後、北イタリアで盛んになり、今日に伝わる。19世紀、地中海貿易の船乗りたちも、恐らく長い船上での生活に退屈し、このマクラメを（⑧）。マクラメの材料に麻糸が使われることが多いのも、もしかしたら、それが彼らにとって唯一手に入る（⑨）。", title="マクラメ"),
  PICK("d17b-31-2-1", "①", ["よく見かける", "店先に並んでいる"], 1, "Key b. Subject ～などが → needs a verb that the things themselves do: 並んでいる. (見かける needs a person as subject.)", ["a", "b"]),
  PICK("d17b-31-2-2", "②", ["工芸が美しい", "工芸のことである"], 1, "Key b. ～とは → ～のことである (definition).", ["a", "b"]),
  PICK("d17b-31-2-3", "③", ["高くないし", "安いし"], 0, "Key a. それほど needs a negative: それほど高くない.", ["a", "b"]),
  PICK("d17b-31-2-4", "④", ["使わないから", "簡単だから"], 0, "Key a. 全く needs a negative: 全く使わない.", ["a", "b"]),
  PICK("d17b-31-2-5", "⑤", ["言葉は", "言葉には"], 0, "Key a. 言葉は … 英語になっている (topic + verb).", ["a", "b"]),
  PICK("d17b-31-2-6", "⑥", ["アラビア語になって", "アラビア語で"], 1, "Key b. もともとはアラビア語で、ミクラマといい = originally, in Arabic, it was called miqrama.", ["a", "b"]),
  PICK("d17b-31-2-7", "⑦", ["一つを言う", "一つである"], 1, "Key b. 編み方、結び方は … 技術の一つである (noun = noun).", ["a", "b"]),
  PICK("d17b-31-2-8", "⑧", ["覚えたのだ", "覚えたのだろう"], 1, "Key b. 恐らく → ～だろう.", ["a", "b"]),
  PICK("d17b-31-2-9", "⑨", ["材料だったからかもしれない", "材料だったと思われる"], 0, "Key a. もしかしたら → ～かもしれない. Also ～のも → ～からだ (reason).", ["a", "b"]),
 ], lead="Key (別冊 p.7): ①b ②b ③a ④a ⑤a ⑥b ⑦b ⑧b ⑨a."),
]
P3 += [
 group("まとめ　次の文章を読んで、文章全体の内容を考えて、1から5の中に入る最もよいものを1・2・3・4から一つ選びなさい。", [
  text("　最終的に私が出版を決断した理由はただ一つ、本書を手に取って下さった方が、改めて物語の魅力を確認し、物語の役割に目覚め、「ああ、本を［1］何と素晴らしいことであろうか」と思ってくれたら、との願いが［2］。\n　もし他所の星から来た生物が、本を読んでいる人間を見たらどう思うだろう、と私は想像することがあります。小さな箱型の紙の束を手に、ただじっと座っているだけで、あるいは寝転がっているだけで、時折、一枚紙がめくられる以外変化はなく、ただ静かに時間が過ぎてゆく。いくら辛抱強く待っていても、何か新しい製品が生み出されるわけでもない。［3］何の得があって人間たちはこんな地味な営みをしているのか？　きっとそんなふうに首を［4］。\n　その時人間の心がどれほど劇的に揺さぶられているか、それは目に見えません。効果を数字によって測ることも不可能です。だからこそかけがえがないのだ、自分が自分であるための大切な証明になるのだ、ということを、くどいくらいに繰り返し語っているのが、［5］。\n（小川洋子『物語の役割』ちくまプリマー新書による）", title="本を読むということ"),
  PICK("d17b-31-m1", "［1］", ["読めば","読むことは","読んでいれば","読んでいる人は"], 1, ["Key 2.", "Start ～ことは → end 何と素晴らしいことであろうか (A: noun = noun). 'Reading books — how wonderful a thing it is!'"], N4),
  PICK("d17b-31-m2", "［2］", ["ありました","あったというのです","あったからなのです","あったはずなのです"], 2, ["Key 3.", "The sentence starts 理由はただ一つ … so it must end with ～からなのです (rule B: reason → から)."], N4),
  PICK("d17b-31-m3", "［3］", ["{一体|いったい}","確かに","どうやら","まさか"], 0, ["Key 1.", "The sentence ends with a question …のか？ → 一体 (rule C: いったい → 質問)."], N4),
  PICK("d17b-31-m4", "［4］", ["傾げたのです","傾げるでしょうか","傾げるようです","傾げるのではないでしょうか"], 3, ["Key 4.", "きっと → guessing ending: 首を傾げるのではないでしょうか (they would surely tilt their heads, puzzled). 首を傾げる = be puzzled."], N4),
  PICK("d17b-31-m5", "［5］", ["本書です","理由です","本書であきらかになります","本書の中で言いたいことです"], 0, ["Key 1.", "～のが (what repeats this idea) → 本書です: 'what keeps saying this, almost tiresomely, is this book.'"], N4),
 ], lead="Key (別冊 p.7): 1-2 2-3 3-1 4-4 5-1."),
]

# ================= 第3部 2課 時制 (pp.154–157) =================
def TF(id, q, ans, ex): return FB(id, q, ans, ex)

J2 = [
 text("文章としてのまとまりを持たせるためには、時間の流れに矛盾がないように文を続ける必要があります。また、ある時点での出来事を言っているのか、ある時間幅における状態のことを言っているのかをはっきりさせることも大切です。特に動詞の用法がポイントです。",
  title="2課　時制",
  explain=["Sensei: Japanese tense is NOT just past vs present. ～る can be future; ～た can be 'just finished' or a state (丸い形をした); ～ている can be ongoing, a result, a shape, or a record of experience.",
           "Thanglish: Big rule for 問題9: inside a ～とき／～場合／～際 clause, the tense depends on the ORDER of the two events, not on today's date. 'Hawaii-ku ponadhukku appuram uncle-a paarpen' → ハワイへ行ったとき (went first) even though it's next month!"]),
 items("A　動詞の現在形の用法", [
  ("**未来**　わたしは来年、高校を卒業する。（動きを表す動詞）", "Action verb in る-form = future: I'll graduate next year."),
  ("**現在**　彼女はトラックの運転ができる。（状態を表す動詞）／おなかが痛む。（感覚を表す動詞）／選手としてしっかり戦うことを誓います。（行動の宣言を表す動詞）", "State verbs (できる, ある), sensation verbs (痛む) and declarations (誓います) in る-form = now."),
  ("**時間に無関係**　太陽は東から上って西に沈む。", "General truth: the sun rises in the east and sets in the west."),
  ("＊形容詞文・名詞文の現在形は現在のこと・時間に無関係なことを表す。", "Adjective / noun sentences in present form = now or always."),
 ]),
 items("B　動詞の過去形の用法", [
  ("**過去**　先週、アメリカから友達が来た。", "Simple past."),
  ("**現在につながる過去**　わたしはさっきからずっとここにいた。", "Past that continues up to now: I've been here all along."),
  ("**完了の結果**　わたしは最近太った。", "Completed change whose result remains: I've put on weight."),
  ("**未来完了**　あした集合時間に遅れた人は、自分で電車で来てください。", "Future perfect: anyone who's late tomorrow (た = will have been late)."),
  ("**形状・状態**　あの丸い形をした建物は何ですか。（名詞を説明する文の中で使う）", "Shape: 丸い形をした建物 = a round-shaped building (only inside a noun-describing clause)."),
  ("**生理状態**　ああ、おなかがすいた。", "Body state now: I'm hungry (said with た)."),
  ("＊形容詞文・名詞文の過去形は過去のことを表す。", ""),
 ]),
 items("C　「～ている」の用法", [
  ("**動作・事態の継続**　日本では子供の数が減っている。", "Ongoing change: the number of children is decreasing."),
  ("**結果の存続**　電気が消えている。", "Result remains: the light is off."),
  ("**形状・様子**　この棒は先が曲がっている。", "Shape: this stick is bent at the end."),
  ("**完了**　20年後、わたしは社長になっているだろう。／3時に会場に着いた。もうみんな来ていた。", "Completed by a point in time: in 20 years I'll have become president; everyone had already come."),
  ("**経験・記録**　彼は10年前に同じ病気で入院している。", "Record of experience: he was hospitalised with the same illness ten years ago."),
 ]),
 items("D　複文の時制 ── 「わたしは［子供が熱を出した］ときは、仕事を休む。」（{主|しゅ}の文：わたしは仕事を休む／中の文：子供が熱を出した）", [
  ("「～とき・～場合・～{際|さい}」などを使った複文や、名詞を説明する文を使った複文では、中の文の時制は話している時点に関係なく、{主|しゅ}の文との時間的前後関係で決まります。（中の文に動きを表す動詞を使った場合）", "Inner clause tense = order relative to the main clause, not to now."),
  ("**a) 中の文のことが{主|しゅ}の文のことより時間的に前のとき、中の文は過去形**\n例・来月［ハワイへ行った］とき、ハワイにいる叔父を訪ねる予定だ。（行った → その後で 訪ねる）\n・［商品を間違って買った］場合、店に返品することができる。\n・以前は、［この大学に入学した］人は、全員寮に入った。", "Inner event FIRST → past form. Next month, after arriving in Hawaii, I'll visit my uncle → 行ったとき."),
  ("**b) 中の文のことが{主|しゅ}の文のことより時間的に後のとき、中の文は現在形**\n例・子供のころ、［寝る］とき、いつも母が本を読んでくれた。（読んでくれた → その後で 寝る）\n・［アメリカへ出発する］際、成田空港で写真を撮った。\n・あした［{国|くに}の母に送る］誕生日祝いを買います。", "Inner event LATER → present form, even in a past story. Mum read to me, THEN I slept → 寝るとき."),
  ("**c) {主|しゅ}の文のことと中の文のことが同時のとき、中の文は現在形（または、{主|しゅ}の文と同じ時制）**\n例・［暑い日に外で仕事をする］人は、たくさん汗をかく。（仕事をする ↔ 汗をかく 同時）\n・［わたしがパソコンで仕事をしている／していた］間、子供たちはテレビを見ていた。\n・［このマンションを買う／買った］とき、親のお金も使った。", "Same time → present (or match the main clause)."),
 ]),
 group("練習1　（　）の中の動詞を適当な形・適当な時制に変えなさい。", [
  TF("d17b-32-1-1a", "1　来週ここで留学説明会を（①行う→ %%）。", ["行う","おこなう"], "Key 行う. Future (来週) → る-form."),
  TF("d17b-32-1-1b", "（②来る→ %%）人に資料を渡すのがわたしの役目である。", ["来た","きた"], "Key 来た. People come FIRST, then I hand them materials → past form in the inner clause (rule D-a)."),
  TF("d17b-32-1-2a", "2　夜遅くその町に着いた。すでに11時を（①過ぎる→ %%）。", ["過ぎていた","すぎていた"], "Key 過ぎていた. すでに → completed state at that time (～ていた)."),
  TF("d17b-32-1-2b", "泊まることに（②する→ %%）友人宅には行かず、", ["していた"], "Key していた. The plan had been made before (state up to then)."),
  TF("d17b-32-1-2c", "安い宿に（③泊まる→ %%）。", ["泊まった","とまった"], "Key 泊まった. Simple past."),
  TF("d17b-32-1-3a", "3　その夜、わたしは12時過ぎまで（①起きる→ %%）。", ["起きていた","おきていた"], "Key 起きていた. Continuing state until 12 → ～ていた."),
  TF("d17b-32-1-3b", "雨が（②降る→ %%）。", ["降っていた","ふっていた"], "Key 降っていた. Background state."),
  TF("d17b-32-1-3c", "12時半ごろ、建物が強く揺れるのを（③感じる→ %%）。", ["感じた","かんじた"], "Key 感じた. A single event at 12:30."),
  TF("d17b-32-1-4a", "4　今朝、踏み切りで事故が（①ある→ %%）らしく、電車が20分遅れた。", ["あった"], "Key あった. Past event."),
  TF("d17b-32-1-4b", "新幹線のホームに着いたとき、（②乗る→ %%）はずだった新幹線は", ["乗る","のる"], "Key 乗る. Boarding would come AFTER arriving → present form (rule D-b)."),
  TF("d17b-32-1-4c", "もう（③出る→ %%）。", ["出ていた","でていた"], "Key 出ていた. もう → had already left (completed state)."),
  TF("d17b-32-1-5a", "5　家に（①帰る→ %%）のは12時ごろだったと思う。", ["帰った","かえった"], "Key 帰った. Past."),
  TF("d17b-32-1-5b", "子供たちはもう（②寝る→ %%）が、", ["寝ていた","ねていた"], "Key 寝ていた. もう → already asleep."),
  TF("d17b-32-1-5c", "妻はまだ本を（③読む→ %%）。", ["読んでいた","よんでいた"], "Key 読んでいた. まだ → still reading."),
  TF("d17b-32-1-5d", "テレビをつけると、学生のころ（④見る→ %%）映画を", ["見た","みた"], "Key 見た. A film I saw back as a student."),
  TF("d17b-32-1-5e", "（⑤やる→ %%）。", ["やっていた"], "Key やっていた. Was on (broadcasting) when I switched on."),
  TF("d17b-32-1-5f", "面白くて、途中でやめられず、結局明け方まで（⑥寝ない→ %%）。", ["寝なかった","ねなかった"], "Key 寝なかった."),
 ], lead="Key (別冊 p.7): 1.①行う ②来た　2.①過ぎていた ②していた ③泊まった　3.①起きていた ②降っていた ③感じた　4.①あった ②乗る ③出ていた　5.①帰った ②寝ていた ③読んでいた ④見た ⑤やっていた ⑥寝なかった"),
 group("練習2　（　）の中の動詞を適当な形・適当な時制に変えなさい。", [
  TF("d17b-32-2-1a", "1　わたしは小さいころから動物が好きだった。当時（①飼う→ %%）犬や鳥はもちろん、", ["飼っていた","かっていた"], "Key 飼っていた. Pets kept over a period."),
  TF("d17b-32-2-1b", "公園のあひるや捨て猫も（②見る→ %%）だけで飽きなかった。", ["見ている","みている"], "Key 見ている. Same time as 飽きなかった (rule D-c) — watching, I never got bored."),
  TF("d17b-32-2-1c", "興味の対象は小動物だけではなかった。（③荒れる→ %%）我が家の庭には、", ["荒れた","荒れていた","あれた","あれていた"], "Key 荒れた／荒れていた. State of the garden (overgrown)."),
  TF("d17b-32-2-1d", "名前も知らない草木がたくさん（④生える→ %%）、そこにいろいろな虫が集まってきた。", ["生えていて","はえていて"], "Key 生えていて. State + て-form linking."),
  TF("d17b-32-2-1e", "虫の観察も楽しく、時間を忘れた。その日もわたしは庭に出て、ありの観察をしていた。一生懸命食べ物を運ぶ姿が面白くて、かなり長い間（⑤見る→ %%）ような気がする。", ["見ていた","みていた"], "Key 見ていた. Continued for a long time."),
  TF("d17b-32-2-1f", "ふとそばに人の気配を感じて顔を上げると、そこに母が（⑥立つ→ %%）。", ["立っていた","たっていた"], "Key 立っていた. Result state: Mum was standing there."),
  TF("d17b-32-2-1g", "母は（⑦困る→ %%）ような顔をしていた。", ["困った","こまった"], "Key 困った. 困ったような顔 = a troubled look (た-form for a state, like 丸い形をした)."),
  TF("d17b-32-2-2a", "2　国土交通省は地球温暖化対策として、自転車に期待を（①寄せる→ %%）。", ["寄せている","よせている"], "Key 寄せている. Ongoing state."),
  TF("d17b-32-2-2b", "今まで車を（②使う→ %%）人が自転車を利用するようになれば、", ["使っていた","つかっていた"], "Key 使っていた. Up to now (今まで) → ～ていた."),
  TF("d17b-32-2-2c", "二酸化炭素が出るのを大きく減らすことが（③できる→ %%）。", ["できる"], "Key できる. Possibility (state verb, present)."),
  TF("d17b-32-2-2d", "だが、現在、自転車利用者のための対策が（④遅れる→ %%）。", ["遅れている","おくれている"], "Key 遅れている. 現在 → current state."),
  TF("d17b-32-2-2e", "自転車事故なども（⑤増える→ %%）ことから、", ["増えている","ふえている"], "Key 増えている. Ongoing change."),
  TF("d17b-32-2-2f", "国土交通省はようやく自転車道路の整備に（⑥乗り出す→ %%）。", ["乗り出した","のりだした"], "Key 乗り出した. ようやく → finally started (completed)."),
 ], lead="Key (別冊 p.7): 1.①飼っていた ②見ている ③荒れた／荒れていた ④生えていて ⑤見ていた ⑥立っていた ⑦困った　2.①寄せている ②使っていた ③できる ④遅れている ⑤増えている ⑥乗り出した"),
]
J2 += [
 group("まとめ　次の文章を読んで、文章全体の内容を考えて、1から5の中に入る最もよいものを1・2・3・4から一つ選びなさい。", [
  text("　ここにある小説は、作者である「わたし」の手を離れて久しいものばかりです。\n　［1］その瞬間に、すでに小説は作者にとって、「自分から離れていってしまったもの」になっています。\n　作者から［2］小説は、読者の元へと、ゆっくり運ばれてゆきます。たとえば大きな客船に乗って、堂々と海の波を割りひらきながら読者の皆さんのところへと運ばれる本もあるでしょう。ひっそりと夜の道を［3］しなやかな動物の背に乗って、選ばれた読者にだけ運ばれる本もあるにちがいない。（略）\n　どんなふうに運ばれた小説も、読者にとっては大切なものです。もしかしたら、作者にとってよりも、読者にとっての方が、より大切なものかもしれない。\n　わたし自身、自分の作ったものはさきほど［4］ようにどんどん忘れていってしまうけれど、大好きで読みついできたよその作者の小説についてならば、どの頁にどんな言葉があって、登場人物の誰がどんな服をどんな場面で着ていて、どんな時に悲しんでどんな時に喜んだかということを、つぶさに［5］のです。\n　小説というものは、書かれることも大事だけれど、読んでもらうことも、きっとものすごく大事なのです。\n（川上弘美『はじめての文学　川上弘美』文藝春秋　刊）", title="小説が読者に運ばれるまで"),
  PICK("d17b-32-m1", "［1］", ["書き上がる","書き上がった","書き上がっている","書き上がっていた"], 1, ["Key 2.", "書き上がった その瞬間 = the moment it's finished. The finishing comes first, then 'already it's left the author' → た-form in the noun clause (D-a)."], N4),
  PICK("d17b-32-m2", "［2］", ["離れる","離れた","離れている","離れていた"], 1, ["Key 2.", "作者から離れた小説 = the novel that has left the author (leaving comes first, then it's carried to readers)."], N4),
  PICK("d17b-32-m3", "［3］", ["走る","走った","走りながら","走るとき"], 0, ["Key 1.", "夜の道を走るしなやかな動物 = a supple animal running along the night road (same time, general description → dictionary form)."], N4),
  PICK("d17b-32-m4", "［4］", ["書く","書いた","書いてきた","書いていた"], 1, ["Key 2.", "さきほど書いたように = as I wrote a moment ago (simple past)."], N4),
  PICK("d17b-32-m5", "［5］", ["覚える","覚えた","覚えている","覚えていた"], 2, ["Key 3.", "つぶさに覚えている = I remember in detail (a state that continues now → ～ている)."], N4),
 ], lead="Key (別冊 p.7): 1-2 2-2 3-1 4-2 5-3."),
]

SECTION = {
 "book": "bunpo",
 "title": "第2部 2課 名詞を説明する形式・3課「～ない」がつく文法形式／第3部 1課 始めと終わり・2課 時制",
 "source": "新完全マスター文法 N2 · 第2部 2・3課 · 第3部 1・2課 · pp.142–157 · answers from 別冊 解答 p.7",
 "blocks": [*K2, *K3, *P3, *J2],
}
