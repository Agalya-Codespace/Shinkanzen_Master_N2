from _h import *
DAY = 10
TITLE = "自然と科学"
INTRO = "Today: Kanji 第31–33回, Goi 自然・科学・技術, Bunpo ～できない・～を見て評価すると, Dokkai 例を問う, Chokai 課題理解 3・4 条件."

NUMS = "①②③④⑤⑥⑦"

def step2(n, cd, counts, answers, box, ii, iii, iv, v, explain=None, vtitle="漢字、または読み方を選びなさい。"):
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
    out.append(group("第%d回　Ⅴ　＿＿の部分の%s" % (n, vtitle), ch))
    return out

WORDS = [
 ("第31回", [["島国","しまぐに","island country"],["囲む","かこむ","to surround"],["引っ越し","ひっこし","moving house"],["鋭い","するどい","sharp"],["永い","ながい","long (time); 永い眠り = death"],["汚い","きたない","dirty; messy"],["偉い","えらい","great; admirable"],["易しい","やさしい","easy"],["延びる","のびる","to be extended"],["延長","えんちょう","extension"],["移す","うつす","to move (sth)"],["移転","いてん","relocation"],["地域","ちいき","region"],["区域","くいき","zone"],["血液","けつえき","blood"],["液体","えきたい","liquid"],["通貨","つうか","currency"],["貨物","かもつ","freight"],["河","かわ","big river"],["印","しるし","mark"],["胃炎","いえん","gastritis"],["煙","けむり","smoke"],["お菓子","おかし","sweets"],["衣食住","いしょくじゅう","food, clothing and shelter"],["押さえる","おさえる","to hold down"],["永遠","えいえん","eternity"],["愛","あい","love"],["奥","おく","the back; inner part"],["偉大","いだい","great"],["画家","がか","painter"],["欧米","おうべい","Europe and America"],["栄える","さかえる","to prosper"],["運河","うんが","canal"]]),
 ("第32回", [["一日","いちにち","one day"],["十五個","じゅうごこ","fifteen (pieces)"],["共に","ともに","together with"],["公害","こうがい","pollution"],["隠す","かくす","to hide"],["異なる","ことなる","to differ"],["汚す","よごす","to make dirty"],["換える","かえる","to replace"],["習慣","しゅうかん","custom; habit"],["慣れる","なれる","to get used to"],["観客","かんきゃく","audience"],["観光","かんこう","sightseeing"],["正確","せいかく","accurate"],["確かめる","たしかめる","to make sure"],["乾く","かわく","to dry"],["乾電池","かんでんち","dry-cell battery"],["割合","わりあい","proportion"],["役割","やくわり","role"],["株","かぶ","root (of a plant); stock"],["皆さん","みなさん","everyone"],["羽","はね","wing; feather"],["快晴","かいせい","clear weather"],["干す","ほす","to dry (in the sun)"],["血圧","けつあつ","blood pressure"],["食塩","しょくえん","table salt"],["革","かわ","leather"],["靴","くつ","shoes"],["灰色","はいいろ","grey"],["管","くだ","tube"],["額","ひたい","forehead"],["羽根","はね","feather"],["平仮名","ひらがな","hiragana"],["壊す","こわす","to break"]]),
 ("第33回", [["子供連れ","こどもづれ","with children"],["家族","かぞく","family"],["技術","ぎじゅつ","technology"],["進歩","しんぽ","progress"],["追い付く","おいつく","to catch up"],["祈る","いのる","to pray"],["居る","いる","to be (somewhere)"],["叫ぶ","さけぶ","to shout"],["吸う","すう","to breathe in"],["救う","すくう","to save"],["割る","わる","to break (glass etc.)"],["許可","きょか","permission"],["許す","ゆるす","to allow; forgive"],["疑う","うたがう","to suspect"],["疑問","ぎもん","doubt; question"],["要求","ようきゅう","demand"],["求める","もとめる","to seek"],["演技","えんぎ","acting"],["演説","えんぜつ","speech"],["供給","きょうきゅう","supply"],["給料","きゅうりょう","salary"],["荷物","にもつ","luggage; parcel"],["甘い","あまい","sweet"],["詰まる","つまる","to be packed"],["基本","きほん","basics"],["応用","おうよう","application"],["含む","ふくむ","to contain"],["寄せる","よせる","to send in; bring near"],["寄付","きふ","donation"],["金額","きんがく","amount of money"],["物価","ぶっか","prices"],["仮定","かてい","assumption"],["換気","かんき","ventilation"],["異常","いじょう","abnormality"],["旧館","きゅうかん","old building"],["案内","あんない","guidance; showing around"],["目印","めじるし","landmark"],["汗","あせ","sweat"],["岸","きし","shore; bank"],["丸","まる","circle"],["分割","ぶんかつ","division into parts"]]),
]

SECTION = {
 "book": "kanji",
 "title": "ステップ3　第31回～第33回",
 "source": "新完全マスター漢字 N2 · pp.60–65 · 650まで · CD32–CD34 · this PDF has no answer pages, so answers are sensei's, checked word by word",
 "blocks": [
  wordlist("📋 今日の漢字リスト · Today's kanji words", WORDS,
   "Every answer word from today's Ⅱ–Ⅴ, plus key words from the CD sentences. Hide a column to test yourself; tap a striped cell to peek.",
   ["Same kanji, different words: 羽(はね) wing vs 羽根(はね) feather; 河(かわ) big river vs 川(かわ); 革(かわ) leather vs 皮(かわ) skin. Sound same, kanji vera — careful!",
    "Kun-yomi verbs today: 隠す, 異なる, 汚す, 換える, 祈る, 叫ぶ, 吸う, 救う, 割る, 含む, 寄せる, 詰まる, 押さえる, 栄える. Okurigana-vum serthu learn pannunga."]),

  *step2(31, 32, [6, 11], [
    "日本は海に囲まれた島国である。",
    "良い部屋が見つかったので、今度の土曜日に引っ越しをする。"],
   ("□の中の漢字を使って、文を完成させなさい。＿＿部分の読み方も書きなさい。（すべて形容詞です）",
    "Box: 易・汚・暖・鋭・偉・永. All are i-adjectives. One kanji is not used."), [
    ("口には出さなくても、子供の観察力には%%ものがある。", ["鋭い"], ["するどい"], "鋭(するど)い = sharp. 観察力が鋭い = sharp eye for detail."),
    ("去年の春、祖父は%%眠りについた。", ["永い"], ["ながい"], "永(なが)い眠りにつく = die (polite way). 永い is used for very long time; 長い is the everyday one."),
    ("このノートは眠い時に書いたので、字が%%て読めない。", ["汚く"], ["きたなく"], "汚(きたな)い → 汚くて = messy, so can't read."),
    ("親に頼らずに大学に行くなんて、君は%%よ。", ["偉い"], ["えらい"], "偉(えら)い = admirable. 君は偉い = you're great."),
    ("見ていると%%そうに思えるが、自分でやってみると大変だ。", ["易し"], ["やさし"], "易(やさ)しい → 易しそう = looks easy. 暖 is the one left over."),
   ], [
    ("野球の試合が[[□びた]]ため、放送時間が{30分|さんじゅっぷん}[[□長された]]。", ["延"], [("a", "□びた", ["のびた", "の"]), ("b", "□長された", ["えんちょう", "えんちょうされた"])],
     "延 = の(びる) / えん: 試合が延びる = the game runs long; 延長(えんちょう) = extension."),
    ("事務所を郊外に[[□した]]ので、[[□転]]の通知を送った。", ["移"], [("c", "□した", ["うつした", "うつ"]), ("d", "□転", ["いてん"])],
     "移 = うつ(す) / い: 移す = move (something); 移転(いてん) = relocation of an office."),
    ("アジアは雨の多い[[地□]]だ。／ここからは危険[[区□]]ですから入らないでください。", ["域"], [("e", "地□", ["ちいき"]), ("f", "区□", ["くいき"])],
     "域 = いき: 地域(ちいき) = region; 区域(くいき) = zone."),
    ("人間は[[血□]]の3{分|ぶん}の1を失うと死んでしまう。／これは、普通の温度で[[□体]]になる金属です。", ["液"], [("g", "血□", ["けつえき"]), ("h", "□体", ["えきたい"])],
     "液 = えき: 血液(けつえき) = blood; 液体(えきたい) = liquid. 血 = けつ in compounds."),
    ("ドルは世界で通用する[[通□]]だ。／現在、[[□物]]の輸送には主にトラックが使われている。", ["貨"], [("i", "通□", ["つうか"]), ("j", "□物", ["かもつ"])],
     "貨 = か: 通貨(つうか) = currency; 貨物(かもつ) = freight — 物 = もつ here, like 荷物(にもつ)."),
   ], [
    ("a", "①{地図帳|ちずちょう}を開いて、{四大|しだい}文明の発生した大きな[[河]]に…", ["かわ"], "河(かわ) = big river. 黄河(こうが) uses が.", None),
    ("b", "…[[印]]を付けた。", ["しるし"], "印(しるし) = mark. 目印(めじるし) = landmark.", None),
    ("c", "②ストレスによる[[胃炎]]で1週間入院した。", ["いえん"], "胃炎(いえん) = gastritis. 炎 = えん (inflammation).", None),
    ("d", "③遠くに見えるあの黒い[[煙]]は何だろう。", ["けむり"], "煙(けむり) = smoke. 禁煙(きんえん) = no smoking.", None),
    ("e", "④私の母は[[お菓子]]作りが得意だ。", ["かし", "おかし"], "お菓子(おかし) = sweets. The box already prints お, so type かし.", None),
    ("f", "⑤[[衣食住]]が足りているからといって、文化的な生活だとは限らない。", ["いしょくじゅう"], "衣食住(いしょくじゅう) = clothes, food, home.", None),
    ("g", "⑥大きな荷物を持って通るので、ドアを[[押さえて]]いてください。", ["お", "おさえて"], "押(お)さえる = hold (the door) open/still.", "さえて"),
    ("h", "⑦二人は神の前で[[えいえん]]の…", ["永遠"], "えいえん = 永遠 (eternity).", None),
    ("i", "…[[あい]]を誓った。", ["愛"], "あい = 愛 (love).", None),
    ("j", "⑧{廊下|ろうか}の[[奥]]は祖母の部屋になっている。", ["おく"], "奥(おく) = the far end, inside.", None),
   ], [
    ("1a", "①ピカソは20世紀の[[いだいな]]…　(1)", ["違大な", "偉大な", "緯大な", "韋大な"], 1, "Answer 2 偉大(いだい)な = great. 偉い(えらい) same kanji."),
    ("1b", "…[[画家]]だ。　(2)", ["かくや", "がや", "かくか", "がか"], 3, "Answer 4 画家(がか) = painter."),
    ("2", "②日本人と[[欧米]]人の感情表現は異なると言われている。", ["おうべ", "おうべい", "おおべえ", "おおべい"], 1, "Answer 2 欧米(おうべい) = Europe and America. 米 = べい (アメリカ)."),
    ("3", "③1,000年前京都は日本の都として[[さかえて]]いた。", ["栄えて", "営えて", "和えて", "盛えて"], 0, "Answer 1 栄(さか)える = prosper. 盛ん(さかん) uses 盛, but さかえる is 栄."),
    ("4", "④この[[運河]]が開通して、船での運送が便利になった。", ["うんが", "うんこう", "うんか", "うんごう"], 0, "Answer 1 運河(うんが) = canal. 河 = が in compounds."),
   ]),

  *step2(32, 33, [8, 11], [
    "漢字を一日に十五個ずつ覚えることにしている。",
    "経済の成長と共に公害が社会問題となった。"],
   ("□の中の漢字を使って、文を完成させなさい。＿＿部分の読み方も書きなさい。（すべて訓読みの動詞です）",
    "Box: 隠・異・汚・割・換. All are kun-yomi verbs. One kanji is not used."), [
    ("彼はいい所だけ見せて弱点を%%うとする傾向がある。", ["隠そ"], ["かくそ"], "隠(かく)す → 隠そうとする = try to hide."),
    ("その大会には、%%文化を持つたくさんの人々が参加した。", ["異なる"], ["ことなる"], "異(こと)なる = differ. 異なる文化 = different cultures."),
    ("転んで、洗濯したばかりの服を%%てしまった。", ["汚し"], ["よごし"], "汚(よご)す = make dirty. 汚い(きたない) same kanji, different reading!"),
    ("目覚まし時計の電池が切れたので、%%てください。", ["換え"], ["かえ"], "換(か)える = replace. 電池を換える. 割 is the one left over (it comes in Ⅲ⑤)."),
   ], [
    ("外国の生活[[習□]]に[[□れる]]には時間がかかる。", ["慣"], [("a", "習□", ["しゅうかん"]), ("b", "□れる", ["なれる", "な"])],
     "慣 = かん / な(れる): 習慣(しゅうかん) = custom; 慣れる = get used to."),
    ("この競技場には5万人の[[□客]]が入れます。／こちらへは[[□光]]ではなく仕事で参りました。", ["観"], [("c", "□客", ["かんきゃく"]), ("d", "□光", ["かんこう"])],
     "観 = かん: 観客(かんきゃく) = spectators; 観光(かんこう) = sightseeing."),
    ("もう一度、[[正□な]]出発時間を[[□かめて]]おきたい。", ["確"], [("e", "正□な", ["せいかく", "せいかくな"]), ("f", "□かめて", ["たしかめて", "たし"])],
     "確 = かく / たし(かめる): 正確(せいかく)な = exact; 確かめる = check."),
    ("植木の土が[[□いて]]いたので、たっぷり水をやった。／[[□電池]]は普通のごみと一緒に捨ててはいけません。", ["乾"], [("g", "□いて", ["かわいて", "かわ"]), ("h", "□電池", ["かんでんち"])],
     "乾 = かわ(く) / かん: 土が乾く = soil dries; 乾電池(かんでんち) = dry battery."),
    ("20年後には、65歳以上の人の[[□合]]が20パーセントを超えるという。／彼は家庭での自分の[[役□]]を全く理解していない。", ["割"], [("i", "□合", ["わりあい"]), ("j", "役□", ["やくわり"])],
     "割 = わり: 割合(わりあい) = ratio; 役割(やくわり) = role."),
   ], [
    ("a", "①花の[[株]]を分けて庭に植えた。", ["かぶ"], "株(かぶ) = plant root clump. Also 'stock' (株式).", None),
    ("b", "②[[皆さん]]の率直なご意見をお聞かせください。", ["みな"], "皆(みな)さん = everyone.", "さん"),
    ("c", "③1羽の鳥が[[羽]]を広げて飛び立とうとしている。", ["はね"], "羽(はね) = wing. As a counter it is わ (1羽 = いちわ).", None),
    ("d", "④台風が去って明日は朝から[[快晴]]らしい。", ["かいせい"], "快晴(かいせい) = perfectly clear sky.", None),
    ("e", "⑤このケーキには[[干した]]果物が入っている。", ["ほ"], "干(ほ)す = dry. 干した果物 = dried fruit.", "した"),
    ("f", "⑥父は[[血圧]]が高いので、…", ["けつあつ"], "血圧(けつあつ) = blood pressure.", None),
    ("g", "…[[食塩]]の取り過ぎに注意している。", ["しょくえん"], "食塩(しょくえん) = table salt. 塩 alone = しお.", None),
    ("h", "⑦質のいい[[革]]で作られた…", ["かわ"], "革(かわ) = leather.", None),
    ("i", "…[[靴]]は、履きやすい。", ["くつ"], "靴(くつ) = shoes.", None),
    ("j", "⑧[[灰色]]の目をした女性の絵が壁に飾ってある。", ["はいいろ"], "灰色(はいいろ) = grey.", None),
   ], [
    ("1", "①病気の重い患者には、鼻から[[管]]を通して栄養を取らせることもある。", ["くだ", "ぐだ", "つづ", "つつ"], 0, "Answer 1 管(くだ) = tube. 血管(けっかん) uses かん."),
    ("2", "②熱があるかどうか、[[額]]に手を当ててみた。", ["ひたい", "のど", "がく", "ほお"], 0, "Answer 1 額(ひたい) = forehead. 金額(きんがく) uses がく."),
    ("3", "③きれいな[[羽根]]のついた帽子を買った。", ["うね", "はね", "ばね", "けね"], 1, "Answer 2 羽根(はね) = feather."),
    ("4", "④1週間あれば、[[平仮名]]は完全に覚えられるでしょう。", ["ひらかな", "ひらがな", "ひらかめい", "ひらがめい"], 1, "Answer 2 平仮名(ひらがな). か becomes が."),
    ("5", "⑤カメラを落として[[壊して]]しまった。", ["くずして", "こわして", "いたして", "ならして"], 1, "Answer 2 壊(こわ)す = break."),
   ]),

  *step2(33, 34, [9, 8], [
    "休みの日の公園は子供連れの家族でいっぱいだ。",
    "技術の進歩があまりにも速いため、追い付いていけない人もいる。"],
   ("□の中の漢字を使って、文を完成させなさい。＿＿部分の読み方も書きなさい。",
    "Box: 叫・救・吸・割・祈・居. Use each kanji once, in the right form."), [
    ("近くの神社で、生まれたばかりの赤ん坊の成長を%%た。", ["祈っ"], ["いのっ"], "祈(いの)る → 祈った = prayed for."),
    ("雨が降ったので、日曜日は{一日中|いちにちじゅう}{家|いえ}に%%た。", ["居"], ["い"], "居(い)る → 居た = stayed. Usually written いる, but the kanji is 居."),
    ("突然だれかが「キャー、助けて」と%%だ。", ["叫ん"], ["さけん"], "叫(さけ)ぶ → 叫んだ = shouted."),
    ("朝の新鮮な空気を胸一杯に%%た。", ["吸っ"], ["すっ"], "吸(す)う → 吸った = breathed in."),
    ("病気の小鳥を世話していたが、結局%%てやれなかった。", ["救っ"], ["すくっ"], "救(すく)う → 救ってやれなかった = couldn't save it."),
    ("手が滑って、花瓶を落として%%てしまった。", ["割っ"], ["わっ"], "割(わ)る → 割ってしまった = broke (a vase)."),
   ], [
    ("入国管理局で入国[[□可]]を取った。／両親に結婚を[[□して]]もらった。", ["許"], [("a", "□可", ["きょか"]), ("b", "□して", ["ゆるして", "ゆる"])],
     "許 = きょ / ゆる(す): 許可(きょか) = permission; 許す = allow."),
    ("当時、彼は犯人ではないかと[[□われた]]。／この記事が確かかどうか[[□問]]だ。", ["疑"], [("c", "□われた", ["うたがわれた", "うたが"]), ("d", "□問", ["ぎもん"])],
     "疑 = うたが(う) / ぎ: 疑われた = was suspected; 疑問(ぎもん) = doubtful."),
    ("裁判で住民側の[[要□]]はすべて認められた。／卒業前の学生は職を[[□めて]]就職活動を開始した。", ["求"], [("e", "要□", ["ようきゅう"]), ("f", "□めて", ["もとめて", "もと"])],
     "求 = きゅう / もと(める): 要求(ようきゅう) = demand; 職を求める = look for a job."),
    ("この俳優は[[□技]]がうまい。／彼の[[□説]]は感動的で、聞いている人の心を打った。", ["演"], [("g", "□技", ["えんぎ"]), ("h", "□説", ["えんぜつ"])],
     "演 = えん: 演技(えんぎ) = acting; 演説(えんぜつ) = speech. 説 = ぜつ here, not せつ!"),
    ("石油の[[供□]]が不足すると、ガソリンの価格が上がる。／[[□料]]は月末に支払われることになっている。", ["給"], [("i", "供□", ["きょうきゅう"]), ("j", "□料", ["きゅうりょう"])],
     "給 = きゅう: 供給(きょうきゅう) = supply; 給料(きゅうりょう) = salary."),
   ], [
    ("a", "①届いた[[にもつ]]を開けてみると、…", ["荷物"], "にもつ = 荷物.", None),
    ("b", "…[[甘そうな]]お菓子が…", ["あま"], "甘(あま)い → 甘そうな = looks sweet.", "そうな"),
    ("c", "…いっぱい[[詰まって]]いた。", ["つ"], "詰(つ)まる = be packed full.", "まって"),
    ("d", "②3か月でコンピューターの[[きほん]]から…", ["基本"], "きほん = 基本 (basics).", None),
    ("e", "…[[おうよう]]まで学んだ。", ["応用"], "おうよう = 応用 (application).", None),
    ("f", "③カルシウムを[[含んだ]]食品は体にいい。", ["ふく"], "含(ふく)む → 含んだ = containing.", "んだ"),
    ("g", "④台風の被害を受けた地域に[[寄せられた]]…", ["よ"], "寄(よ)せる → 寄せられた = sent in (donations).", "せられた"),
    ("h", "…[[寄付]]金の合計は3,000万円を超えた。", ["きふ"], "寄付(きふ) = donation. 寄付金 = donated money.", None),
    ("i", "⑤この[[きんがく]]は、…", ["金額"], "きんがく = 金額.", None),
    ("j", "…[[ぶっか]]が上昇したと…", ["物価"], "ぶっか = 物価 (prices). ぶつ → ぶっ.", None),
    ("k", "…[[かてい]]して計算したものだ。", ["仮定"], "かてい = 仮定 (assume). (家庭/過程 also かてい — meaning paarthu choose pannunga.)", None),
    ("l", "⑥[[換気]]装置に…", ["かんき"], "換気(かんき) = ventilation.", None),
    ("m", "…[[いじょう]]がないかを調べるために、…", ["異常"], "いじょう = 異常 (abnormality). 以上 is 'more than' — different!", None),
    ("n", "…[[旧館]]を…", ["きゅうかん"], "旧館(きゅうかん) = old building. 新館 = new building.", None),
    ("o", "…[[あんない]]してもらった。", ["案内"], "あんない = 案内.", None),
   ], [
    ("1", "①大きな青い看板を[[目印]]に、目的の店を探した。", ["めしるし", "めじるし", "もくいん", "めど"], 1, "Answer 2 目印(めじるし). し → じ."),
    ("2", "②軽いスポーツで[[あせ]]を流した。", ["液", "汁", "泣", "汗"], 3, "Answer 4 汗(あせ) = sweat."),
    ("3", "③黄河は向こうの[[岸]]が見えないくらい大きな河だ。", ["かわ", "きし", "しぎ", "がん"], 1, "Answer 2 岸(きし) = bank, shore."),
    ("4", "④テストで答えが正しい時は[[まる]]を付ける。", ["円", "球", "玉", "丸"], 3, "Answer 4 丸(まる) = circle mark ○."),
    ("5", "⑤授業料は前期と後期に[[分割]]して支払うことができます。", ["ふんわり", "ぶんわり", "ぶんかつ", "ふんかつ"], 2, "Answer 3 分割(ぶんかつ) = split into instalments."),
   ]),
 ]
}
