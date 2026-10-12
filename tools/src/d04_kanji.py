from _h import *
DAY = 4
TITLE = "健康と趣味"
INTRO = "Today: Kanji 第15–17回 (ステップ2 starts), Goi 健康・趣味・娯楽, Bunpo ～だけではなく・～について, Dokkai 比喩・疑問提示文, Chokai 音の変化や縮約形."

NUMS = "①②③④⑤⑥⑦"

def step2(n, cd, counts, answers, box, ii, iii, iv, v, explain=None):
    """One ステップ2 round: Ⅰ CD dictation, Ⅱ complete with box kanji, Ⅲ same kanji in □, Ⅳ read/write, Ⅴ choose."""
    p = "d4k-%d" % n
    out = [{
        "type": "dictation", "id": "k%d" % n, "title": "第%d回" % n,
        "lead": "Ⅰ　ＣＤを聞いて、指示された数の漢字を使って文を書きなさい。CD%d" % cd,
        "audio": "audio/kanji/cd%02d.mp3" % cd, "audioLabel": "CD %d · 漢字 N2" % cd,
        "counts": counts, "answers": answers,
        "note": "Each sentence is read twice. Type it, press Check, or open Answer. Model answers come from the CD and use exactly the number of kanji the book asks for.",
    }]
    if explain: out[0]["explain"] = explain
    ch = []
    for i, (q, word, yomi, ex) in enumerate(ii):
        ch.append(fill("%s-2%d" % (p, i + 1), NUMS[i] + q, word, ex))
        ch.append(fill("%s-2%dy" % (p, i + 1), "　↳ 読み方：%%", yomi))
    g = group("第%d回　Ⅱ　%s" % (n, box[0]), ch, lead=box[1]); g["plainKeys"] = ["lead"]
    out.append(g)
    ch = []
    for i, (q, kanji, reads, ex) in enumerate(iii):
        ch.append(fill("%s-3%d" % (p, i + 1), NUMS[i] + q + "　□＝%%", kanji, ex))
        for L, w, y in reads:
            ch.append(fill("%s-3%s" % (p, L), "　↳ " + L + "　[[" + w + "]] の読み方：%%", y))
    out.append(group("第%d回　Ⅲ　□には同じ漢字が入ります。漢字と＿＿の部分の読み方を書きなさい。" % n, ch,
                     lead="First type the one kanji that fits both □, then the readings of the underlined words."))
    ch = [fill("%s-4%s" % (p, L), q, ans, ex, suffix=suf) for L, q, ans, ex, suf in iv]
    out.append(group("第%d回　Ⅳ　＿＿の部分の漢字には読み仮名を、平仮名には漢字を（送り仮名も）書きなさい。" % n, ch,
                     lead="Underlined kanji → type the reading. Underlined hiragana → type the kanji (with okurigana)."))
    ch = [dict(mcq("%s-5%s" % (p, k), q, opts, ans, ex, keys=["1", "2", "3", "4"]), noRubyU=True, plainKeys=["opts"]) for k, q, opts, ans, ex in v]
    out.append(group("第%d回　Ⅴ　＿＿の部分の漢字、または読み方を選びなさい。" % n, ch))
    return out

WORDS = [
 ("第15回", [["気分","きぶん","feeling"],["横になる","よこになる","to lie down"],["広場","ひろば","square; plaza"],["中央","ちゅうおう","centre"],["時計台","とけいだい","clock tower"],["上り","のぼり","up train"],["下り","くだり","down train"],["間違える","まちがえる","to mistake"],["解く","とく","to solve"],["加える","くわえる","to add"],["温める","あたためる","to warm up"],["過ぎる","すぎる","to pass"],["返す","かえす","to return (a thing)"],["各自","かくじ","each person"],["各地","かくち","every region"],["体育館","たいいくかん","gymnasium"],["教育","きょういく","education"],["感心な","かんしんな","admirable"],["感動する","かんどうする","to be moved"],["絵画","かいが","paintings"],["貝","かい","shellfish"],["生","なま","raw"],["鳥","とり","bird"],["王子","おうじ","prince"],["物語","ものがたり","tale"],["一億円","いちおくえん","100 million yen"],["角","かど","corner"],["明らか","あきらか","clear; obvious"],["様子","ようす","situation; state"],["強引に","ごういんに","forcibly"],["改めて","あらためて","again (another time)"],["格好","かっこう","appearance; outfit"],["果たして","はたして","really (?) ; as expected"],["自ら","みずから","oneself; personally"]]),
 ("第16回", [["大通り","おおどおり","main street"],["薬局","やっきょく","pharmacy"],["年中","ねんじゅう","all year round"],["特売","とくばい","special sale"],["花火","はなび","fireworks"],["見物","けんぶつ","sightseeing; watching"],["橋","はし","bridge"],["日課","にっか","daily routine"],["活気","かっき","liveliness"],["意外な","いがいな","unexpected"],["経営する","けいえいする","to manage (a business)"],["以降","いこう","from … onward"],["三角形","さんかくけい","triangle"],["角度","かくど","angle"],["お正月","おしょうがつ","New Year"],["月日","つきひ","time; days and months"],["記入する","きにゅうする","to fill in"],["記事","きじ","article"],["共通","きょうつう","common"],["共同","きょうどう","shared; joint"],["各々","おのおの","each"],["長所","ちょうしょ","strong point"],["過去","かこ","the past"],["会議","かいぎ","meeting"],["長引く","ながびく","to drag on"],["器具","きぐ","appliance"],["お住まい","おすまい","residence"],["無料","むりょう","free of charge"],["体温計","たいおんけい","thermometer"],["計る","はかる","to measure (time)"],["玉","たま","ball; bead"],["過ぎ去る","すぎさる","to pass by"],["大木","たいぼく","big tree"],["転がる","ころがる","to roll"],["足る","たる","to be worthy of"]]),
 ("第17回", [["広告","こうこく","advertisement"],["効果","こうか","effect"],["軽く","かるく","lightly"],["日記","にっき","diary"],["時代","じだい","era; days"],["改める","あらためる","to revise"],["育つ","そだつ","to grow up"],["結ぶ","むすぶ","to tie"],["光る","ひかる","to shine"],["用いる","もちいる","to use"],["水泳","すいえい","swimming"],["泳ぐ","およぐ","to swim"],["方向","ほうこう","direction"],["向かう","むかう","to head for"],["決める","きめる","to decide"],["決心","けっしん","determination"],["期待する","きたいする","to expect"],["待つ","まつ","to wait"],["形","かたち","shape"],["長方形","ちょうほうけい","rectangle"],["過ごす","すごす","to spend (time)"],["方角","ほうがく","direction"],["事件","じけん","incident"],["限り","かぎり","as far as"],["可決","かけつ","approval (of a bill)"],["私鉄","してつ","private railway"],["起こす","おこす","to cause; to start"],["位","くらい","place (digit)"],["以外","いがい","except"],["共に","ともに","together"],["欠ける","かける","to be missing"],["球","たま","ball"],["後","のち","later; (weather) then"]]),
]

SECTION = {
 "book": "kanji",
 "title": "ステップ2　第15回～第17回",
 "source": "新完全マスター漢字 N2 · pp.18–23 · 375まで · CD16–CD18 · this PDF has no answer pages, so answers are sensei's, checked word by word",
 "blocks": [
  wordlist("📋 今日の漢字リスト · Today's kanji words", WORDS,
   "Every answer word from today's Ⅱ–Ⅴ, plus key words from the CD sentences. Hide a column to test yourself; tap a striped cell to peek.",
   ["Step 2 aarambam! Ippo 5 types of question: Ⅰ CD, Ⅱ box-la irukkira kanji vechu sentence complete, Ⅲ rendu word-la common kanji, Ⅳ read/write, Ⅴ JLPT-style choose.",
    "Special readings kavanam: 各々(おのおの), 大木(たいぼく — だいぼく illa), 見物(けんぶつ), 晴れ後曇り(のち), 自ら(みずから), 足る(たる)."]),

  *step2(15, 16, [4, 8, 7], [
    "気分が悪いのならしばらくそこに横になっていなさい。",
    "広場の中央に大きな時計台がある。",
    "上りと下りの電車を間違えて乗ってしまった。"],
   ("□の中の漢字を使って、文を完成させなさい。＿＿部分の読み方も書きなさい。",
    "Box: 帰（例）・温・返・加・解・過. 例：{今日|きょう}は{妻|つま}の{誕生日|たんじょうび}なので、{早|はや}く{家|いえ}へ帰ろう（かえろう）。 Use each kanji once, in the right form."), [
    ("勉強不足で、こんな易しい問題も%%ことができない。", ["解く"], ["とく"], "解(と)く = to solve. 問題を解く = solve a problem."),
    ("この料理は酒を%%と、もっとおいしくなります。", ["加える"], ["くわえる"], "加(くわ)える = add. Rice wine serthaa innum taste."),
    ("寒かったでしょう。今、スープを%%ますから。", ["温め"], ["あたため"], "温(あたた)める = warm up (food, liquid). 暖める is for rooms/air."),
    ("約束の時間を%%たのに、まだ友達は来ない。", ["過ぎ"], ["すぎ"], "過(す)ぎる = (time) pass."),
    ("電車に忘れたかばんの中には、先生に%%大切な本が入っていた。", ["返す"], ["かえす"], "返(かえ)す = give back. 帰す = send someone home — different kanji!"),
   ], [
    ("昼食は[[□自]]、持参のこと。／全国[[□地]]を旅行する。", ["各"], [("c", "□自", ["かくじ"]), ("d", "□地", ["かくち"])],
     "各 = かく: 各自(かくじ) = each person; 各地(かくち) = various places."),
    ("雨が降っていたので、[[体□館]]でバスケットをした。／国の発展を支えるのは[[教□]]だ。", ["育"], [("e", "体□館", ["たいいくかん"]), ("f", "教□", ["きょういく"])],
     "育 = いく: 体育館(たいいくかん) = gym; 教育(きょういく) = education."),
    ("彼は、遅刻も欠席も一度もない[[□心な]]学生だ。／映画を見て[[□動した]]のは、久しぶりだ。", ["感"], [("g", "□心な", ["かんしん", "かんしんな"]), ("h", "□動した", ["かんどう", "かんどうした"])],
     "感 = かん: 感心(かんしん)な = admirable; 感動(かんどう)する = be moved."),
   ], [
    ("a", "①父は[[絵画]]を集めるのが趣味です。", ["かいが"], "絵画(かいが) = paintings. 絵 = かい here, not え.", None),
    ("b", "②取ったばかりの[[かい]]を…", ["貝"], "かい = 貝 (shellfish).", None),
    ("c", "…[[生]]で食べた。", ["なま"], "生(なま) = raw.", None),
    ("d", "③これは[[とり]]に変えられてしまった…", ["鳥"], "とり = 鳥 (bird).", None),
    ("e", "…[[王子]]の…", ["おうじ"], "王子(おうじ) = prince. おうし illa — じ.", None),
    ("f", "…[[物語]]です。", ["ものがたり"], "物語(ものがたり) = tale, story.", None),
    ("g", "④駅前にできるマンションは[[いちおくえん]]するらしい。", ["一億円"], "いちおくえん = 一億円 (100 million yen).", None),
    ("h", "⑤机の[[角]]にぶつけた腕が痛い。", ["かど"], "角(かど) = corner (of a desk, street). かく = angle; つの = horn.", None),
    ("i", "⑥書類のサインが本人のものであることは[[あきらか]]だ。", ["明らか"], "あきらか = 明らか (obvious). Okurigana らか.", None),
    ("j", "⑦そちらの[[様子]]が分かったらメールで知らせてください。", ["ようす"], "様子(ようす) = state, how things are.", None),
   ], [
    ("1", "①私には無理な仕事なのに、[[ごういんに]]頼まれてしまった。", ["号引に", "強引に", "強飲に", "合員に"], 1, "Answer 2 強引(ごういん)に = forcibly. 強 = ごう here (強盗 ごうとう too)."),
    ("2", "②A：田中はただ今、外出しておりますが。B：それでは、日を[[あらためて]]参ります。", ["改めて", "変めて", "新めて", "更めて"], 0, "Answer 1 改(あらた)めて = again, another time. 新(あたら)しい is a different verb."),
    ("3", "③あの人は、いつもおかしな[[かっこう]]をしている。", ["格好", "活行", "格行", "活好"], 0, "Answer 1 格好(かっこう) = appearance. 格好いい = cool!"),
    ("4", "④「席は必ず取れる。約束する。」と言っていたが、[[果たして]]取れたのだろうか。", ["かたして", "はてたして", "はたして", "くだたして"], 2, "Answer 3 果(は)たして = really? (doubt). 果物(くだもの) is a special reading."),
    ("5", "⑤彼女は「[[自ら]]学ぶことの楽しさが分かりました。」と言った。", ["じから", "わたしから", "しから", "みずから"], 3, "Answer 4 自(みずか)ら = by oneself."),
   ]),

  *step2(16, 17, [8, 8], [
    "大通りにある薬局は年中特売をしている。",
    "花火を見物する人で橋の上は動けないほどだった。"],
   ("AとBの漢字を組み合わせて、文を完成させなさい。＿＿部分の読み方も書きなさい。",
    "A: 学（例）・意・以・日・活・経　　B: 校（例）・外・気・課・営・降. 例：{日本|にほん}へ{来|き}てから{日本語|にほんご}学校（がっこう）で{日本語|にほんご}を{勉強|べんきょう}しています。 Make a two-kanji word: one from A + one from B."), [
    ("私は朝のランニングを%%にしている。", ["日課"], ["にっか"], "日課(にっか) = daily routine. 日 = にっ (sound change)."),
    ("この村は若者が都会に出てしまったので、%%がなくなった。", ["活気"], ["かっき"], "活気(かっき) = liveliness. 活 = かっ."),
    ("思いもしなかった%%な結果となった。", ["意外"], ["いがい"], "意外(いがい)な = unexpected. 以外 (except) is a different word — Ⅴ in 第17回!"),
    ("私の父は会社を%%している。", ["経営"], ["けいえい"], "経営(けいえい) = run a business."),
    ("明日は胃の検査がありますから、夜8時%%は何も食べないでください。", ["以降"], ["いこう"], "以降(いこう) = from … onward."),
   ], [
    ("[[三□形]]の三つの[[□度]]を合わせると、180度になる。", ["角"], [("a", "三□形", ["さんかくけい"]), ("b", "□度", ["かくど"])],
     "角 = かく: 三角形(さんかくけい) = triangle; 角度(かくど) = angle. 形 = けい here."),
    ("{年|ねん}に1度、[[お正□]]には家族が集まる。／「[[□日]]の流れるのは早いものだ。」とよく言う。", ["月"], [("c", "お正□", ["おしょうがつ"]), ("d", "□日", ["つきひ"])],
     "月 = がつ / つき: お正月(おしょうがつ); 月日(つきひ) = time passing."),
    ("ここに、あなたの名前と住所を[[□入して]]ください。／今朝の新聞に、昨日の列車事故の[[□事]]が載っている。", ["記"], [("e", "□入して", ["きにゅう", "きにゅうして"]), ("f", "□事", ["きじ"])],
     "記 = き: 記入(きにゅう) = fill in; 記事(きじ) = article."),
    ("彼とは[[□通]]の話題が多く、話が合う。／学生寮はふろとトイレが[[□同]]だ。", ["共"], [("g", "□通", ["きょうつう"]), ("h", "□同", ["きょうどう"])],
     "共 = きょう: 共通(きょうつう) = common; 共同(きょうどう) = shared."),
   ], [
    ("a", "①今回の計画を進めるに当たっては、[[各々]]の…", ["おのおの"], "各々(おのおの) = each one. Special reading!", None),
    ("b", "…[[長所]]を発揮してほしい。", ["ちょうしょ"], "長所(ちょうしょ) = strong point. Opposite 短所(たんしょ).", None),
    ("c", "②[[過去]]のことはもう思い出したくない。", ["かこ"], "過去(かこ) = the past. 去 = こ here.", None),
    ("d", "③[[会議]]が…", ["かいぎ"], "会議(かいぎ) = meeting.", None),
    ("e", "…[[長引いて]]パーティーに出席できなかった。", ["ながび", "ながびいて"], "長引(ながび)く = drag on. 引 = び (rendaku).", "いて"),
    ("f", "④父は、電気[[きぐ]]の修理の仕事をしている。", ["器具"], "きぐ = 器具 (appliance, tool).", None),
    ("g", "⑤[[お住まい]]はどちらですか。", ["す", "おすまい"], "お住(す)まい = (your) residence.", None),
    ("h", "…[[無料]]で配達させていただきます。", ["むりょう"], "無料(むりょう) = free of charge. 無 = む here.", None),
    ("i", "⑥[[体温計]]で熱を測ると、38度もあった。", ["たいおんけい"], "体温計(たいおんけい) = thermometer.", None),
    ("j", "⑦時計は{時|とき}を[[計る]]機械だ。", ["はか", "はかる"], "計(はか)る = measure (time, numbers). 測る = length/temperature, 量る = weight.", "る"),
   ], [
    ("1", "①この人形の目は、ガラスの[[たま]]でできている。", ["円", "丸", "球", "玉"], 3, "Answer 4 玉(たま) = bead, ball (glass eye bead). 球 = sports ball (第17回 Ⅴ④)."),
    ("2a", "②台風が[[過ぎ去った]]あと、…　(1)", ["すぎさった", "すぎいった", "すぎきった", "すぎちった"], 0, "Answer 1 過(す)ぎ去(さ)る = pass by. 去る = さる."),
    ("2b", "…風で倒された[[大木]]が…　(2)", ["たいぼく", "だいぼく", "たいもく", "だいもく"], 0, "Answer 1 大木(たいぼく) = big tree. 木 = ぼく here."),
    ("2c", "…何本も[[転がって]]いた。　(3)", ["ごろがって", "ころがって", "こどがって", "ことがって"], 1, "Answer 2 転(ころ)がる = roll."),
    ("3", "③国民の代表として信頼するに[[足る]]人物が首相に選ばれるべきだ。", ["たする", "たりる", "たる", "そくる"], 2, "Answer 3 足(た)る = (old form of 足りる) be worthy of. ～に足る人物 = a person worthy of ～."),
   ]),

  *step2(17, 18, [6, 5, 10], [
    "広告は新聞よりテレビの方が効果があるようだ。",
    "コンサートに行く前にどこかで軽く食べて行こう。",
    "日記を読んで楽しかった学生時代を思い出した。"],
   ("□の中の漢字を使って、文を完成させなさい。＿＿部分の読み方も書きなさい。",
    "Box: 結・育・改・用・光. Use each kanji once, in the right form."), [
    ("この規則は現状に合わないので、%%ことになった。", ["改める"], ["あらためる"], "改(あらた)める = revise, change."),
    ("生活は苦しかったが、子供たちは明るく%%てくれた。", ["育っ"], ["そだっ"], "育(そだ)つ = grow up → 育ってくれた."),
    ("短いひもを何本も%%で長いひもを作る。", ["結ん"], ["むすん"], "結(むす)ぶ = tie → 結んで."),
    ("北の空に明るく%%ているのが北極星です。", ["光っ"], ["ひかっ"], "光(ひか)る = shine → 光っている."),
    ("この公式を%%と問題が簡単に解けますよ。", ["用いる"], ["もちいる"], "用(もち)いる = use (formal). Reading kavanam: もちいる."),
   ], [
    ("弟は[[水□]]大会で500メートルを[[□いだ]]。", ["泳"], [("a", "水□", ["すいえい"]), ("b", "□いだ", ["およいだ", "およ"])],
     "泳 = えい / およ(ぐ): 水泳(すいえい); 泳いだ(およいだ)."),
    ("北の[[方□]]に[[□かって]]、まっすぐ2キロほど進んでください。", ["向"], [("c", "方□", ["ほうこう"]), ("d", "□かって", ["むかって", "む"])],
     "向 = こう / む(かう): 方向(ほうこう); 向かって(むかって)."),
    ("彼は「留学は十分考えて[[□めた]]ことだから。」と言って、両親が反対しても[[□心]]を変えようとしなかった。", ["決"], [("e", "□めた", ["きめた", "き"]), ("f", "□心", ["けっしん"])],
     "決 = き(める) / けつ→けっ: 決めた; 決心(けっしん)."),
    ("いいお返事が頂けることを[[期□して]][[□って]]います。", ["待"], [("g", "期□して", ["きたい", "きたいして"]), ("h", "□って", ["まって", "ま"])],
     "待 = たい / ま(つ): 期待(きたい)して; 待って(まって)."),
   ], [
    ("a", "①はがきのような[[形]]を、…", ["かたち"], "形(かたち) = shape.", None),
    ("b", "…[[長方形]]という。", ["ちょうほうけい"], "長方形(ちょうほうけい) = rectangle. 形 = けい in shapes: 三角形, 正方形.", None),
    ("c", "②夏休みを海外で[[すごした]]。", ["過ごした"], "すごす = 過ごす (spend time).", None),
    ("d", "③学校はここから北の[[方角]]にある。", ["ほうがく"], "方角(ほうがく) = direction. 角 = かく → がく.", None),
    ("e", "④その[[じけん]]について、…", ["事件"], "じけん = 事件 (incident).", None),
    ("f", "…知っている[[かぎり]]のことを話してほしい。", ["限り"], "かぎり = 限り (as far as …).", None),
    ("g", "⑤賛成多数により[[かけつ]]します。", ["可決"], "かけつ = 可決 (approve a motion). Opposite 否決(ひけつ).", None),
    ("h", "⑥[[私鉄]]の…", ["してつ"], "私鉄(してつ) = private railway. 私 = し here.", None),
    ("i", "…労働者の組合がストを[[おこした]]。", ["起こした"], "おこす = 起こす (cause, start a strike).", None),
    ("j", "⑦十の[[位]]で四捨五入してください。", ["くらい"], "位(くらい) = digit place. 十の位 = tens place. (い in 3位.)", None),
   ], [
    ("1", "①好き嫌いがあまりなく、チーズ[[いがい]]なら何でも食べられる。", ["位外", "以外", "意外", "移外"], 1, "Answer 2 以外(いがい) = except. 意外 = unexpected (第16回)."),
    ("2", "②親友の田中さんと私は、学生時代、[[ともに]]スポーツをした仲です。", ["友に", "供に", "緒に", "共に"], 3, "Answer 4 共(とも)に = together. 共 again from 第16回 Ⅲ!"),
    ("3", "③メンバーのうちの一人が[[欠けても]]、試合には出場できない。", ["かけても", "ぬけても", "さけても", "とけても"], 0, "Answer 1 欠(か)ける = be missing."),
    ("4", "④遠くまで飛んでいったゴルフの[[球]]を見失ってしまった。", ["きゅう", "あな", "たま", "だま"], 2, "Answer 3 球(たま) = ball. On'yomi きゅう (野球)."),
    ("5", "⑤明日の天気は、晴れ[[後]]曇りとなるでしょう。", ["あと", "のち", "うしろ", "ご"], 1, "Answer 2 後(のち). Weather forecast: 晴れ後曇り = sunny, later cloudy."),
   ]),
 ]
}
