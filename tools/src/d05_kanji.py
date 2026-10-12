from _h import *
DAY = 5
TITLE = "旅行と自然"
INTRO = "Today: Kanji 第18–20回, Goi 旅行・交通・自然, Bunpo ～を基準にして・～に関連して, Dokkai 主張表現, Chokai 即時応答 starts."

NUMS = "①②③④⑤⑥⑦"

def step2(n, cd, counts, answers, box, ii, iii, iv, v, explain=None):
    """One ステップ2 round: Ⅰ CD dictation, Ⅱ complete with box kanji, Ⅲ same kanji in □, Ⅳ read/write, Ⅴ choose."""
    p = "d%dk-%d" % (DAY, n)
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
    if isinstance(iii, dict): out.append(iii); iii = None
    ch = []
    for i, (q, kanji, reads, ex) in enumerate(iii or []):
        ch.append(fill("%s-3%d" % (p, i + 1), NUMS[i] + q + "　□＝%%", kanji, ex))
        for L, w, y in reads:
            ch.append(fill("%s-3%s" % (p, L), "　↳ " + L + "　[[" + w + "]] の読み方：%%", y))
    if ch: out.append(group("第%d回　Ⅲ　□には同じ漢字が入ります。漢字と＿＿の部分の読み方を書きなさい。" % n, ch,
                     lead="First type the one kanji that fits both □, then the readings of the underlined words."))
    ch = [fill("%s-4%s" % (p, L), q, ans, ex, suffix=suf) for L, q, ans, ex, suf in iv]
    out.append(group("第%d回　Ⅳ　＿＿の部分の漢字には読み仮名を、平仮名には漢字を（送り仮名も）書きなさい。" % n, ch,
                     lead="Underlined kanji → type the reading. Underlined hiragana → type the kanji (with okurigana)."))
    ch = [dict(mcq("%s-5%s" % (p, k), q, opts, ans, ex, keys=["1", "2", "3", "4"]), noRubyU=True, plainKeys=["opts"]) for k, q, opts, ans, ex in v]
    out.append(group("第%d回　Ⅴ　＿＿の部分の漢字、または読み方を選びなさい。" % n, ch))
    return out

WORDS = [
 ("第18回", [["強い","つよい","strong"],["光","ひかり","light"],["夏","なつ","summer"],["売り出す","うりだす","to put on sale"],["あっという間に","あっというまに","in an instant"],["売り切れる","うりきれる","to sell out"],["空港","くうこう","airport"],["山林","さんりん","mountain forest"],["目次","もくじ","table of contents"],["生産","せいさん","production"],["国際","こくさい","international"],["限界","げんかい","limit"],["無限","むげん","unlimited"],["在学中","ざいがくちゅう","while enrolled"],["現在","げんざい","now; at present"],["解答","かいとう","answer (to a problem)"],["理解","りかい","understanding"],["合同","ごうどう","joint"],["合理化","ごうりか","rationalization"],["特長","とくちょう","strong point; feature"],["町長","ちょうちょう","town mayor"],["根","ね","root"],["土","つち","soil"],["取り入れる","とりいれる","to take in"],["今学期","こんがっき","this term"],["試験","しけん","exam"],["課","か","lesson; unit"],["痛い","いたい","painful"],["指","ゆび","finger"],["血","ち","blood"],["決して","けっして","never"],["港","みなと","harbour"],["指す","さす","to point"],["効く","きく","to take effect"],["通じる","つうじる","to run through; to connect"],["文明","ぶんめい","civilization"]]),
 ("第19回", [["西向き","にしむき","facing west"],["部屋","へや","room"],["夕方","ゆうがた","evening"],["暑い","あつい","hot (weather)"],["泣く","なく","to cry"],["妹","いもうと","younger sister"],["笑う","わらう","to laugh; to smile"],["失う","うしなう","to lose"],["示す","しめす","to show"],["死ぬ","しぬ","to die"],["試す","ためす","to try"],["資本","しほん","capital"],["資料","しりょう","materials; documents"],["形式","けいしき","form; formality"],["結婚式","けっこんしき","wedding"],["感情","かんじょう","emotion"],["事情","じじょう","circumstances"],["商売","しょうばい","business; trade"],["商品","しょうひん","goods"],["原料","げんりょう","raw material"],["原始的","げんしてき","primitive"],["王","おう","king"],["教師","きょうし","teacher"],["長年","ながねん","many years"],["研究","けんきゅう","research"],["実","み","fruit; result"],["結ぶ","むすぶ","to bear (fruit)"],["三勝","さんしょう","three wins"],["勝ち","かち","win"],["手術","しゅじゅつ","surgery"],["治す","なおす","to cure"],["向こう","むこう","over there"],["四つ角","よつかど","crossroads"],["初歩","しょほ","the basics"],["険しい","けわしい","steep"],["目指す","めざす","to aim for"]]),
 ("第20回", [["海","うみ","sea"],["深い","ふかい","deep"],["泳ぐ","およぐ","to swim"],["危ない","あぶない","dangerous"],["受験科目","じゅけんかもく","exam subjects"],["数学","すうがく","mathematics"],["政治","せいじ","politics"],["社説","しゃせつ","editorial"],["助手","じょしゅ","assistant"],["果実","かじつ","fruit"],["身分","みぶん","social status"],["一昨年","おととし","the year before last"],["暗記","あんき","memorization"],["合格","ごうかく","passing (an exam)"],["改正","かいせい","revision (of a law)"],["真空","しんくう","vacuum"],["雪","ゆき","snow"],["初めて","はじめて","for the first time"],["屋根","やね","roof"],["男性","だんせい","man"],["願う","ねがう","to wish; to pray for"],["元日","がんじつ","New Year's Day"],["寺","てら","temple"],["神社","じんじゃ","shrine"],["静かな","しずかな","quiet"],["お座り","おすわり","please sit"],["笑顔","えがお","smiling face"],["人種","じんしゅ","race (of people)"],["日光","にっこう","sunlight"],["差す","さす","(sun) to shine in"],["酒場","さかば","bar; pub"]]),
]

III20 = group("第20回　Ⅲ　□に漢字を入れて、文の意味を表す言葉を完成させなさい。読み方も書きなさい。", [
  fill("d5k-20-3%d" % i if L == "k" else "d5k-20-3%dy" % i, q, a, ex) for i, (L, q, a, ex) in enumerate([
   ("k", "（例）学校で、勉強する所＝□□　→　教室（きょうしつ）", ["教室"], "Example: 教室(きょうしつ) = classroom."),
  ]) ] + [x for i, (q, word, yomi, ex) in enumerate([
   ("①去年のその前の年＝□□年", ["一昨"], ["おととし", "いっさくねん"], "一昨年 = the year before last. Daily speech: おととし; formal: いっさくねん. Both OK."),
   ("②文字などに書いたものを見なくても言えるように覚えること＝□記", ["暗"], ["あんき"], "暗記(あんき) = learning by heart. 暗 = dark → 'paakkaama' sollradhu."),
   ("③試験などにパスすること＝合□", ["格"], ["ごうかく"], "合格(ごうかく) = passing. 合 = ごう here (not あい)."),
   ("④法律や規則を直してよくすること＝□{正|せい}", ["改"], ["かいせい"], "改正(かいせい) = revision of a law. 改 = change (改める)."),
   ("⑤空気などの物質が全く存在しない状態＝□{空|くう}", ["真"], ["しんくう"], "真空(しんくう) = vacuum. 真 = complete, true."),
  ], 1) for x in (fill("d5k-20-3%d" % i, q + "　□＝%%", word, ex), fill("d5k-20-3%dy" % i, "　↳ 読み方：%%", yomi))],
  lead="Type the missing kanji for □ (all of them, in order), then the reading of the whole word.")
III20["children"] = III20["children"][1:]  # drop the 例 (already answered in the book)
III20["children"].insert(0, text("（例）学校で、勉強する所＝{教|きょう}{室|しつ}（きょうしつ）"))

SECTION = {
 "book": "kanji",
 "title": "ステップ2　第18回～第20回",
 "source": "新完全マスター漢字 N2 · pp.24–29 · 435まで · CD19–CD21 · this PDF has no answer pages, so answers are sensei's, checked word by word",
 "blocks": [
  wordlist("📋 今日の漢字リスト · Today's kanji words", WORDS,
   "Every answer word from today's Ⅱ–Ⅴ, plus key words from the CD sentences. Hide a column to test yourself; tap a striped cell to peek.",
   ["Innaiku 3 rounds. Special readings kavanam: 一昨年(おととし), 長年(ながねん — ちょうねん illa), 元日(がんじつ), 四つ角(よつかど), 初歩(しょほ), 笑顔(えがお), 酒場(さかば).",
    "Same sound, different kanji: さす = 指す (point) / 差す (sun shines, umbrella); きく = 聞く / 効く (medicine works) / 利く."]),

  *step2(18, 19, [5, 7], [
    "強い{光|ひかり}は目に悪いので、夏はサングラスをかけるようにしている。",
    "昨日売り出されたコンピューターはあっという間に売り切れた。"],
   ("AとBの漢字を組み合わせて、文を完成させなさい。＿＿部分の読み方も書きなさい。",
    "A: 生・目・国・空・山　　B: 際・次・林・産・港. Make a two-kanji word: one from A + one from B."), [
    ("%%のロビーは、出迎えや見送りの人で込んでいた。", ["空港"], ["くうこう"], "空港(くうこう) = airport. 空 + 港."),
    ("この県は面積の大部分が%%で平野がないため、{米|こめ}はあまり取れない。", ["山林"], ["さんりん"], "山林(さんりん) = mountain forest. Plains illa, adhanaala rice kammi."),
    ("本の内容は%%を見れば大体分かります。", ["目次"], ["もくじ"], "目次(もくじ) = table of contents."),
    ("この工場では、1日に1,000台の車が%%されている。", ["生産"], ["せいさん"], "生産(せいさん) = production."),
    ("世界の学者が集まって%%会議が開かれた。", ["国際"], ["こくさい"], "国際(こくさい) = international. 国際会議 = international conference."),
   ], [
    ("社会に出て自分の能力の[[□界]]を知る。／資源は[[無□]]ではありません。大切にしましょう。", ["限"], [("a", "□界", ["げんかい"]), ("b", "無□", ["むげん"])],
     "限 = げん: 限界(げんかい) = limit; 無限(むげん) = unlimited."),
    ("私がA大学に[[□学中]]、お世話になったB教授は、[[現□]]は作家として活躍している。", ["在"], [("c", "□学中", ["ざいがくちゅう"]), ("d", "現□", ["げんざい"])],
     "在 = ざい: 在学中(ざいがくちゅう) = while a student there; 現在(げんざい) = now."),
    ("問題の[[□答]]を見たけれど、[[理□]]できなかった。", ["解"], [("e", "□答", ["かいとう"]), ("f", "理□", ["りかい"])],
     "解 = かい: 解答(かいとう) = answer to a problem; 理解(りかい) = understanding."),
    ("専門学校が[[□同]]で説明会を開く。／今のやり方は無駄が多いので、もっと[[□理化]]したい。", ["合"], [("g", "□同", ["ごうどう"]), ("h", "□理化", ["ごうりか"])],
     "合 = ごう: 合同(ごうどう) = joint; 合理化(ごうりか) = make efficient."),
    ("この商品は今までの物にはない[[特□]]があります。／[[町□]]と町の予算について話し合う。", ["長"], [("i", "特□", ["とくちょう"]), ("j", "町□", ["ちょうちょう"])],
     "長 = ちょう: 特長(とくちょう) = strong point (特徴 = feature, any kind); 町長(ちょうちょう) = town mayor."),
   ], [
    ("a", "①植物は[[根]]から…", ["ね"], "根(ね) = root.", None),
    ("b", "…[[土]]の中の水や養分を…", ["つち"], "土(つち) = soil.", None),
    ("c", "…[[取り入れる]]。", ["とりいれる"], "取(と)り入(い)れる = take in. Book box shows 'り　れる', so the kanji readings are と and い.", None),
    ("d", "②[[今学期]]の…", ["こんがっき"], "今学期(こんがっき) = this term. 今 = こん, 学 = がっ.", None),
    ("e", "…[[試験]]は、…", ["しけん"], "試験(しけん) = exam.", None),
    ("f", "…教科書の始めから5[[か]]までです。", ["課"], "か = 課 (lesson unit). 第5課 = lesson 5.", None),
    ("g", "③[[痛い]]と思ったら、…", ["いた", "いたい"], "痛(いた)い = painful.", "い"),
    ("h", "…[[指]]から…", ["ゆび"], "指(ゆび) = finger.", None),
    ("i", "…[[血]]が出ていた。", ["ち"], "血(ち) = blood. One sound only!", None),
    ("j", "④この事は[[決して]]人には言わないでください。", ["けっ", "けっして"], "決(けっ)して + negative = never.", "して"),
   ], [
    ("1a", "①[[港]]へ行く道を聞くと、…　(1)", ["こう", "うみ", "みなと", "わん"], 2, "Answer 3 港(みなと) = harbour. On'yomi こう (空港)."),
    ("1b", "…駅員は地図を[[さして]]説明してくれた。　(2)", ["示して", "差して", "目して", "指して"], 3, "Answer 4 指(さ)す = point with a finger. 差す = umbrella / sunlight."),
    ("2", "②この薬はお茶と一緒に飲むと[[きかない]]から、必ず{水|みず}かお湯で飲んでください。", ["聞かない", "利かない", "働かない", "効かない"], 3, "Answer 4 効(き)く = (medicine) works. 利く = function (e.g. 気が利く)."),
    ("3a", "③鉄道や電話が[[通じ]]、…　(1)", ["つうじ", "とおじ", "かよいじ", "とうじ"], 0, "Answer 1 通(つう)じる = connect, run through."),
    ("3b", "…ヨーロッパの[[文明]]を取り入れたことで、日本の近代化が進んだ。　(2)", ["もんめい", "ぶんめい", "ふんみょう", "ぶんみょう"], 1, "Answer 2 文明(ぶんめい) = civilization."),
   ]),

  *step2(19, 20, [8, 3], [
    "西向きの部屋なので、夏の夕方は暑くてたまらない。",
    "さっきまで泣いていた妹がもう笑っている。"],
   ("□の中の漢字を使って、文を完成させなさい。＿＿部分の読み方も書きなさい。",
    "Box: 示・試・失・死・効. Use each kanji once, in the right form."), [
    ("彼は仕事で大きなミスをして、社長の信頼を%%た。", ["失っ"], ["うしなっ"], "失(うしな)う → 失った = lost (trust). Reading blank has た printed, so type うしなっ."),
    ("具体的な数字や図を%%て説明すると分かりやすい。", ["示し"], ["しめし"], "示(しめ)す → 示して = showing."),
    ("{生|せい}あるものは、必ず%%。", ["死ぬ"], ["しぬ"], "死(し)ぬ = die. 'Uyir ulladhu ellam oru naal sagum.'"),
    ("この薬は、頭痛によく%%。", ["効く"], ["きく"], "効(き)く = (medicine) works."),
    ("エンジンがちゃんと動くかどうか%%てみよう。", ["試し"], ["ためし"], "試(ため)す → 試してみよう = let's try."),
   ], [
    ("500万円を[[□本]]にして小さな会社を始めた。／明日の会議の[[□料]]を用意しておいてください。", ["資"], [("a", "□本", ["しほん"]), ("b", "□料", ["しりょう"])],
     "資 = し: 資本(しほん) = capital; 資料(しりょう) = materials."),
    ("伝統的な[[形□]]を重視した[[結婚□]]は、今の若者に人気がない。", ["式"], [("c", "形□", ["けいしき"]), ("d", "結婚□", ["けっこんしき"])],
     "式 = しき: 形式(けいしき) = formality; 結婚式(けっこんしき) = wedding."),
    ("日本人は喜びや悲しみなどの[[感□]]をあまり表さないと言われている。／家庭の[[事□]]で進学をあきらめた。", ["情"], [("e", "感□", ["かんじょう"]), ("f", "事□", ["じじょう"])],
     "情 = じょう: 感情(かんじょう) = emotion; 事情(じじょう) = circumstances."),
    ("品物は安くていいし、客には親切だし、あの店の主人は本当に[[□売]]が上手だ。／姉は会社で新しい[[□品]]を開発する仕事をしている。", ["商"], [("g", "□売", ["しょうばい"]), ("h", "□品", ["しょうひん"])],
     "商 = しょう: 商売(しょうばい) = business; 商品(しょうひん) = goods."),
    ("ナイロンは石油を[[□料]]として作られている。／水道もガスもない山の中での[[□始的]]な生活もいいものだ。", ["原"], [("i", "□料", ["げんりょう"]), ("j", "□始的", ["げんしてき"])],
     "原 = げん: 原料(げんりょう) = raw material; 原始的(げんしてき) = primitive."),
   ], [
    ("a", "①世界には[[おう]]のいる国がいくつかある。", ["王"], "おう = 王 (king).", None),
    ("b", "②[[きょうし]]になることが私の夢でした。", ["教師"], "きょうし = 教師 (teacher).", None),
    ("c", "③[[長年]]の…", ["ながねん"], "長年(ながねん) = many years. ちょうねん illa!", None),
    ("d", "…[[けんきゅう]]が…", ["研究"], "けんきゅう = 研究 (research).", None),
    ("e", "…[[実]]を…", ["み"], "実(み) = fruit. 実を結ぶ = bear fruit (efforts pay off).", None),
    ("f", "…[[結んだ]]。", ["むす", "むすんだ"], "結(むす)ぶ → 結んだ.", "んだ"),
    ("g", "④このゲームは先に[[三勝]]したほうが…", ["さんしょう"], "三勝(さんしょう) = three wins.", None),
    ("h", "…[[勝ち]]です。", ["か", "かち"], "勝(か)ち = win.", "ち"),
    ("i", "⑤何とか[[しゅじゅつ]]をしないで…", ["手術"], "しゅじゅつ = 手術 (surgery). Hard to say — しゅ-じゅ-つ.", None),
    ("j", "…薬だけで[[治したい]]。", ["なお", "なおしたい"], "治(なお)す = cure (an illness). 直す = fix (a thing).", "したい"),
   ], [
    ("1a", "①[[向こう]]に見える…　(1)", ["むっこう", "むうこう", "むこう", "むきこう"], 2, "Answer 3 向(む)こう = over there."),
    ("1b", "…[[四つ角]]は車が多くて危ない。　(2)", ["よつかど", "よっつかど", "よつかく", "よっつかく"], 0, "Answer 1 四(よ)つ角(かど) = crossroads."),
    ("2", "②フランス語は[[初歩]]を勉強しただけです。", ["しょうほ", "しょほ", "しょほう", "しょうほう"], 1, "Answer 2 初歩(しょほ) = the basics. Short vowels!"),
    ("3a", "③私たちは[[険しい]]{山道|やまみち}を、…　(1)", ["けんしい", "きびしい", "あやしい", "けわしい"], 3, "Answer 4 険(けわ)しい = steep. 厳しい = きびしい (strict)."),
    ("3b", "…頂上を[[目指して]]進んだ。　(2)", ["もくしして", "もくさして", "めさして", "めざして"], 3, "Answer 4 目指(めざ)す = aim for. さ → ざ."),
   ]),

  *step2(20, 21, [4, 12], [
    "ここの海はすぐ深くなるので、泳ぐのは危ない。",
    "私が受けた大学は受験科目が英語と数学だけだった。"],
   ("AとBの漢字を組み合わせて、文を完成させなさい。＿＿部分の読み方も書きなさい。",
    "A: 政・助・社・身・果　　B: 説・分・実・手・治. Make a two-kanji word: one from A + one from B."), [
    ("彼は民主的で清潔な%%家を目指している。", ["政治"], ["せいじ"], "政治家(せいじか) = politician. 治 = じ here."),
    ("新聞の%%には、新聞社の主張が表れている。", ["社説"], ["しゃせつ"], "社説(しゃせつ) = editorial."),
    ("資料の整理を手伝ってくれる%%を求めている。", ["助手"], ["じょしゅ"], "助手(じょしゅ) = assistant."),
    ("いちごやレモンの%%酒が若い女性に人気だ。", ["果実"], ["かじつ"], "果実(かじつ) = fruit. 果実酒 = fruit liqueur."),
    ("昔は、愛し合っていても%%が違うと結婚できなかった。", ["身分"], ["みぶん"], "身分(みぶん) = social status."),
   ], III20, [
    ("a", "①[[ゆき]]を見るのは…", ["雪"], "ゆき = 雪 (snow).", None),
    ("b", "…[[はじめて]]だ。", ["初めて"], "はじめて = 初めて (first time). 始めて = start — different!", None),
    ("c", "[[やね]]にも地面にも積もっている。", ["屋根"], "やね = 屋根 (roof).", None),
    ("d", "②日本でも進んで育児をする[[男性]]が増えている。", ["だんせい"], "男性(だんせい) = man.", None),
    ("e", "③「初もうで」というのは、その{年|とし}1{年|ねん}の家族の健康を[[ねがって]]、…", ["願って"], "ねがう = 願う (wish, pray).", None),
    ("f", "…[[元日]]に…", ["がんじつ"], "元日(がんじつ) = New Year's Day. 元 = がん here.", None),
    ("g", "…[[てら]]や…", ["寺"], "てら = 寺 (temple). With お: お寺.", None),
    ("h", "…[[神社]]にお参りすることです。", ["じんじゃ"], "神社(じんじゃ) = shrine.", None),
    ("i", "④[[しずかな]]秋の夜は読書を楽しむ。", ["静かな"], "しずかな = 静かな.", None),
    ("j", "⑤前のほうの方は、どうか[[おすわり]]ください。", ["お座り"], "おすわり = お座り (polite: please sit).", None),
   ], [
    ("1", "①親の[[笑顔]]は子供を安心させる。", ["わらいがお", "えみがお", "えがお", "えかお"], 2, "Answer 3 笑顔(えがお) = smiling face. Special reading!"),
    ("2", "②ニューヨークには、様々な[[人種]]の人々がいる。", ["じんしゅ", "じんしゅう", "じんじゅ", "にんしゅ"], 0, "Answer 1 人種(じんしゅ) = race."),
    ("3a", "③この植物は[[日光]]に当てるとよくないので、…　(1)", ["じつこう", "じっこう", "にちこう", "にっこう"], 3, "Answer 4 日光(にっこう) = sunlight (also the town Nikko)."),
    ("3b", "…日の[[差さない]]所に移そう。　(2)", ["かさない", "ささない", "いさない", "ほさない"], 1, "Answer 2 差(さ)す = (sun) shines in."),
    ("4", "④一人で[[酒場]]で飲むのも、またいいものだ。", ["さけば", "さかば", "さけじょう", "さかじょう"], 1, "Answer 2 酒場(さかば) = pub. 酒 → さか in compounds (酒屋 さかや)."),
   ]),
 ]
}
