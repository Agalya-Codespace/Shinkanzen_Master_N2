from _h import *
DAY = 13
TITLE = "形容詞とお知らせ"
INTRO = "Today: Kanji 第40–41回 and チャレンジ 接辞②, Goi 第2部 形容詞・名詞・副詞, Bunpo 提案する・強くそう感じる, Dokkai 第2部 お知らせ, Chokai ポイント理解 3 and 確認問題."

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
    for i, t in enumerate(ii):
        q, word, yomi, ex = t[:4]
        ch.append(fill("%s-2%d" % (p, i + 1), (t[4] if len(t) > 4 else NUMS[i]) + q, word, ex))
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
 ("第40回", [["面接","めんせつ","interview"],["第一印象","だいいちいんしょう","first impression"],["委員会","いいんかい","committee"],["住民","じゅうみん","residents"],["代表","だいひょう","representative"],["専門家","せんもんか","expert"],["構成","こうせい","composition, make-up"],["積む","つむ","to pile up, load"],["伸びる","のびる","to grow, stretch"],["吹く","ふく","to blow"],["焼く","やく","to grill, bake"],["触る","さわる","to touch"],["接近","せっきん","approach"],["紹介","しょうかい","introduction"],["清書","せいしょ","clean copy"],["処理","しょり","processing"],["承知","しょうち","understanding, consent"],["支配","しはい","rule, control"],["反省","はんせい","reflection"],["捜す","さがす","to search for (a missing person)"],["灰皿","はいざら","ashtray"],["窓","まど","window"],["掃く","はく","to sweep"],["掃除機","そうじき","vacuum cleaner"],["看護師","かんごし","nurse"],["精神的","せいしんてき","mental"],["対照的","たいしょうてき","contrasting"],["製品","せいひん","product"],["成績","せいせき","result, grade"],["賞状","しょうじょう","certificate of merit"],["温泉","おんせん","hot spring"],["占める","しめる","to occupy, account for"],["面積","めんせき","area"],["床","ゆか","floor"],["占う","うらなう","to tell fortunes"],["大勢","おおぜい","many people"],["万歳","ばんざい","hurrah"],["郊外","こうがい","suburbs"]]),
 ("第41回", [["機械","きかい","machine"],["構造","こうぞう","structure"],["意外","いがい","unexpected"],["簡単","かんたん","simple"],["約束","やくそく","promise"],["信用","しんよう","trust"],["失う","うしなう","to lose"],["お礼状","おれいじょう","thank-you letter"],["血液型","けつえきがた","blood type"],["ドイツ製","ドイツせい","made in Germany"],["死亡率","しぼうりつ","death rate"],["定期券","ていきけん","commuter pass"],["発言権","はつげんけん","right to speak"],["身体測定","しんたいそくてい","physical measurement"],["測る","はかる","to measure"],["尊重","そんちょう","respect"],["尊敬","そんけい","respect, esteem"],["存在","そんざい","existence"],["生存者","せいぞんしゃ","survivor"],["法則","ほうそく","law (of nature)"],["規則","きそく","rule"],["骨","ほね","bone"],["骨折","こっせつ","broken bone"],["息子","むすこ","son"],["息","いき","breath"],["整理","せいり","tidying up"],["高層","こうそう","high-rise"],["乾燥機","かんそうき","dryer"],["製作","せいさく","production"],["方針","ほうしん","policy"],["贈り物","おくりもの","present"],["花束","はなたば","bouquet"],["硬貨","こうか","coin"],["お札","おさつ","banknote"],["勢い","いきおい","momentum"],["昔話","むかしばなし","folk tale"],["孫","まご","grandchild"],["子孫","しそん","descendants"],["操作","そうさ","operation"],["除く","のぞく","to exclude"],["御中","おんちゅう","Messrs. (on letters to companies)"],["触れる","ふれる","to touch"],["軒下","のきした","under the eaves"]]),
 ("チャレンジ 接辞②", [["指定席","していせき","reserved seat"],["専門誌","せんもんし","specialist journal"],["免許証","めんきょしょう","licence"],["異文化","いぶんか","different culture"],["理想像","りそうぞう","ideal image"],["来客用","らいきゃくよう","for visitors"],["非常用","ひじょうよう","for emergencies"],["携帯用","けいたいよう","portable"],["再提出","さいていしゅつ","resubmission"],["再教育","さいきょういく","re-education"],["再出発","さいしゅっぱつ","fresh start"],["予想外","よそうがい","unexpected"],["時間外","じかんがい","outside hours"],["範囲外","はんいがい","out of range"],["人類愛","じんるいあい","love for humankind"],["家族愛","かぞくあい","family love"],["兄弟愛","きょうだいあい","brotherly love"],["死生観","しせいかん","view of life and death"],["人生観","じんせいかん","outlook on life"],["価値観","かちかん","sense of values"],["新聞紙","しんぶんし","newspaper (paper)"],["古新聞","ふるしんぶん","old newspapers"],["新聞社","しんぶんしゃ","newspaper company"],["禁煙中","きんえんちゅう","not smoking"],["禁煙席","きんえんせき","non-smoking seat"],["禁煙車","きんえんしゃ","non-smoking car"],["消防士","しょうぼうし","firefighter"],["消防署","しょうぼうしょ","fire station"],["消防車","しょうぼうしゃ","fire engine"],["下水道","げすいどう","sewer"],["水道管","すいどうかん","water pipe"],["水道水","すいどうすい","tap water"],["文化財","ぶんかざい","cultural asset"],["文化的","ぶんかてき","cultural"],["文化人","ぶんかじん","cultured person"]]),
]

def plain(b, k):
    b["plainKeys"] = b.get("plainKeys", []) + [k]
    return b

C2_I = [
 ("①映画を見る前に、指定（　　）を予約しておこう。", ["間", "室", "席", "区"], 2, "Answer 3. 指定席(していせき) = reserved seat. ～席: 自由席, 禁煙席."),
 ("②専門（　　）に大学の教授の論文が{載|の}っている。", ["誌", "語", "家", "職"], 0, "Answer 1. 専門誌(せんもんし) = specialist journal. 論文 appears in a magazine/journal → 誌. (専門家 = expert; 専門語 = jargon.)"),
 ("③車を運転する際は、{免許|めんきょ}（　　）を忘れないように。", ["紙", "章", "書", "証"], 3, "Answer 4. 免許証(めんきょしょう) = licence card. ～証: 学生証, 保険証."),
 ("④海外でボランティアをして、（　　）文化交流の楽しさを知った。", ["外", "異", "違", "比"], 1, "Answer 2. 異文化(いぶんか) = a different culture. 異 = different (prefix)."),
 ("⑤心の中に教師としての理想（　　）を持っている。", ["心", "型", "体", "像"], 3, "Answer 4. 理想像(りそうぞう) = ideal image. ～像: 人物像, 未来像."),
]
C2_II = [
 ("①（　）…来客□　非常□　{携帯|けいたい}□", "用", "～用(よう) = for ～: 来客用 (for guests), 非常用 (emergency), 携帯用 (portable)."),
 ("②（　）…□提出　□教育　□出発", "再", "再(さい)～ = again: 再提出, 再教育, 再出発."),
 ("③（　）…予想□　時間□　範囲□", "外", "～外(がい) = outside ～: 予想外, 時間外, 範囲外."),
 ("④（　）…人類□　家族□　兄弟□", "愛", "～愛(あい) = love of ～: 人類愛, 家族愛, 兄弟愛."),
 ("⑤（　）…死生□　人生□　価値□", "観", "～観(かん) = view of ～: 死生観, 人生観, 価値観."),
]
C2_III = [
 ("①（　）…［　］{紙|し}　{古|ふる}［　］　［　］{社|しゃ}", "新聞", "新聞紙, 古新聞(ふるしんぶん), 新聞社."),
 ("②（　）…［　］{中|ちゅう}　［　］{席|せき}　［　］{車|しゃ}", "禁煙", "禁煙中, 禁煙席, 禁煙車."),
 ("③（　）…［　］{士|し}　［　］{署|しょ}　［　］{車|しゃ}", "消防", "消防士(しょうぼうし), 消防署(しょうぼうしょ), 消防車."),
 ("④（　）…{下|げ}［　］　［　］{管|かん}　［　］{水|すい}", "水道", "下水道(げすいどう), 水道管(すいどうかん), 水道水(すいどうすい)."),
 ("⑤（　）…［　］{財|ざい}　［　］{的|てき}　［　］{人|じん}", "文化", "文化財(ぶんかざい), 文化的, 文化人(ぶんかじん)."),
]

SECTION = {
 "book": "kanji",
 "title": "ステップ3　第40回～第41回・チャレンジ 接辞②",
 "source": "新完全マスター漢字 N2 · pp.78–83 · 850まで · CD41–CD42 · this PDF has no answer pages, so answers are sensei's, checked word by word",
 "blocks": [
  wordlist("📋 今日の漢字リスト · Today's kanji words", WORDS,
   "Every answer word from today's Ⅱ–Ⅴ and the チャレンジ, plus key words from the CD sentences. Hide a column to test yourself; tap a striped cell to peek.",
   ["Today's suffixes (接辞): ～状 (letter), ～型 (type), ～製 (made in), ～率 (rate), ～券 (ticket), ～権 (right), ～席, ～誌, ～証, ～像, ～用, ～外, ～愛, ～観 and prefixes 再～, 異～.",
    "Special readings: 大勢(おおぜい), 万歳(ばんざい), 息子(むすこ), 御中(おんちゅう), 軒下(のきした), 床(ゆか — also とこ in 床屋), 生存者(せいぞんしゃ — 存 = ぞん here)."]),

  *step2(40, 41, [8, 12], [
    "面接は第一印象が大切である。",
    "この委員会は住民の代表と専門家で構成されている。"],
   ("□の中の漢字を使って、文を完成させなさい。＿＿部分の読み方も書きなさい。",
    "Box: 焼・積・触・吹・伸・植. One kanji is not used."), [
    ("これ以上荷物を%%だら危険だ。", ["積ん"], ["つん"], "積(つ)む → 積んだら = if you pile/load more."),
    ("日本人の平均身長は、この半世紀でかなり%%た。", ["伸び"], ["のび"], "身長が伸(の)びる = height increases."),
    ("海からの風に%%れながら散歩した。", ["吹か"], ["ふか"], "風に吹(ふ)かれる = be blown by the wind (passive)."),
    ("キャンプで肉や魚を%%て食べた。", ["焼い"], ["やい"], "焼(や)く → 焼いて = grill."),
    ("手で%%てみてください。柔らかくて軽い{布|ぬの}でしょう。", ["触っ"], ["さわっ"], "触(さわ)る → 触ってみて = try touching. 植 is the one not used."),
   ], [
    ("①大型の台風が東京に[[□近して]]いる。", ["接"], [("①", "□近して", ["せっきんして", "せっきん"])], "接近(せっきん)する = approach."),
    ("②私は日本の文化を世界の人に[[紹□しよう]]と思っている。", ["介"], [("②", "紹□しよう", ["しょうかいしよう", "しょうかい"])], "紹介(しょうかい)する = introduce."),
    ("③作文は間違いを直して、[[清□して]]から出してください。", ["書"], [("③", "清□して", ["せいしょして", "せいしょ"])], "清書(せいしょ)する = make a clean copy."),
    ("④新しいコンピューターは、今までの倍の速さで仕事を[[□理する]]ことができる。", ["処"], [("④", "□理する", ["しょりする", "しょり"])], "処理(しょり)する = process, handle."),
    ("⑤部長：この件は、すぐ{先方|せんぽう}に連絡してくれ。　社員：はい、[[□知しました]]。", ["承"], [("⑤", "□知しました", ["しょうちしました", "しょうち"])], "承知(しょうち)しました = certainly (polite 'understood')."),
    ("⑥この国は、ほかの国によって長い間[[□配されて]]いた。", ["支"], [("⑥", "□配されて", ["しはいされて", "しはい"])], "支配(しはい)される = be ruled."),
   ], [
    ("a", "①毎日、寝る前に日記を書いて1日の[[反省]]をしている。", ["はんせい"], "反省(はんせい) = reflecting on oneself.", None),
    ("b", "②古いビルに逃げ込んだ犯人を必死に[[捜した]]。", ["さが", "さがした"], "捜(さが)す = search for (a missing person, criminal).", "した"),
    ("c", "③たばこは[[灰皿]]のある所で吸うこと。", ["はいざら"], "灰皿(はいざら) = ashtray. さら → ざら.", None),
    ("d", "④[[窓]]ガラスを割ってしまったので、…", ["まど"], "窓(まど) = window.", None),
    ("e", "…ほうきで[[掃いた]]後、…", ["は", "はいた"], "掃(は)く = sweep.", "いた"),
    ("f", "…[[掃除機]]をかけた。", ["そうじき"], "掃除機(そうじき) = vacuum cleaner.", None),
    ("g", "⑤彼女は[[看護師]]を目指して頑張っている。", ["かんごし"], "看護師(かんごし) = nurse.", None),
    ("h", "⑥あの兄弟は、顔は似ているが[[精神]]的な面では…", ["せいしん"], "精神的(せいしんてき) = mental.", None),
    ("i", "…[[対照]]的だ。", ["たいしょう"], "対照的(たいしょうてき) = contrasting.", None),
    ("j", "⑦大型スーパーでは食料品のほか衣服や電気[[製品]]も売っている。", ["せいひん"], "製品(せいひん) = product.", None),
    ("k", "⑧競技大会でいい[[せいせき]]を取ったので、…", ["成績"], "せいせき = 成績 (result).", None),
    ("l", "…[[賞状]]と…", ["しょうじょう"], "賞状(しょうじょう) = certificate of merit.", None),
    ("m", "…[[温泉]]旅行の招待券をもらった。", ["おんせん"], "温泉(おんせん) = hot spring.", None),
    ("n", "⑨地球上で海が[[占める]]…", ["し", "しめる"], "占(し)める = occupy, account for.", "める"),
    ("o", "…[[めんせき]]の割合は、全体のおよそ10{分|ぶん}の7と言われている。", ["面積"], "めんせき = 面積 (area).", None),
   ], [
    ("1", "①[[床]]にカーテンと同じ色のカーペットを{敷|し}いた。", ["とこ", "ゆか", "いた", "かべ"], 1, "Answer 2 床(ゆか) = floor. (とこ in 床屋, 床の間.)"),
    ("2", "②結婚の相手をトランプで[[占って]]もらった。", ["うらなって", "さぐって", "しめって", "めぐって"], 0, "Answer 1 占(うらな)う = tell a fortune. (占める = しめる.)"),
    ("3", "③昨夜のクラス会は学生時代の友人が[[大勢]]集まった。", ["たいせい", "たいぜい", "おおせい", "おおぜい"], 3, "Answer 4 大勢(おおぜい) = many people."),
    ("4", "④試験に合格し、思わず「[[万歳]]。」と叫んだ。", ["まんざい", "まんさい", "ばんざい", "ばんさい"], 2, "Answer 3 万歳(ばんざい) = hurrah! (漫才 = まんざい comedy.)"),
    ("5", "⑤彼の家は東京の[[こうがい]]にある。", ["交外", "校外", "郊外", "効外"], 2, "Answer 3 郊外(こうがい) = suburbs. 校外 = outside school."),
   ], explain="第40回 Ⅲ is a different style: each line has a 2-kanji する-verb with one kanji missing. Think of the whole word from the meaning."),

  *step2(41, 42, [8, 6], [
    "その機械の構造は意外にも簡単だった。",
    "約束を守らなければ信用を失うだろう。"],
   ("□の中の漢字を使って、文を完成させなさい。＿＿部分の読み方も書きなさい。",
    "Box: 型・券・権・状・製・軒・率. All are suffixes; one is not used."), [
    ("お世話になった先生に[[お礼]]%%を書いた。", ["状"], ["おれいじょう"], "お礼状(おれいじょう) = thank-you letter. ～状 = letter."),
    ("医者は手術の前に、もう一度[[血液]]%%を確かめた。", ["型"], ["けつえきがた"], "血液型(けつえきがた) = blood type. ～型 = type (がた)."),
    ("このドイツ%%の車は、とても運転しやすくできている。", ["製"], ["せい", "ドイツせい", "どいつせい"], "ドイツ製(せい) = made in Germany."),
    ("日本では、{赤|あか}ん{坊|ぼう}や{幼児|ようじ}の[[死亡]]%%が大変低い。", ["率"], ["しぼうりつ"], "死亡率(しぼうりつ) = death rate. ～率 = rate."),
    ("彼は、いつも[[定期]]%%と一緒に子供の写真を持ち歩いている。", ["券"], ["ていきけん"], "定期券(ていきけん) = commuter pass."),
    ("今回の会議においては、会員以外の方に[[発言]]%%はありません。", ["権"], ["はつげんけん"], "発言権(はつげんけん) = right to speak. 軒 is not used."),
   ], [
    ("身体[[□定]]の日に、身長を[[□った]]。", ["測"], [("a", "□定", ["そくてい"]), ("b", "□った", ["はかった", "はか"])],
     "測 = そく / はか(る): 身体測定(しんたいそくてい) = physical check-up; 測(はか)る = measure."),
    ("ほかの人の意見も[[□重する]]ことが大切だ。／あの先生は学生から[[□敬されて]]いる。", ["尊"], [("c", "□重する", ["そんちょうする", "そんちょう"]), ("d", "□敬されて", ["そんけいされて", "そんけい"])],
     "尊 = そん: 尊重(そんちょう)する = respect (opinions); 尊敬(そんけい)する = look up to."),
    ("地球以外の星にも生物は[[□在する]]のだろうか。／飛行機事故の[[生□]]{者|しゃ}の名前が確認された。", ["存"], [("e", "□在する", ["そんざいする", "そんざい"]), ("f", "生□", ["せいぞん"])],
     "存 = そん / ぞん: 存在(そんざい) = exist; 生存者(せいぞんしゃ) = survivor."),
    ("自然を観察することから自然の[[法□]]が発見された。／学校の[[規□]]に{従|したが}って行動してください。", ["則"], [("g", "法□", ["ほうそく"]), ("h", "規□", ["きそく"])],
     "則 = そく: 法則(ほうそく) = law (of nature); 規則(きそく) = rule."),
    ("年を取ると[[□]]が弱くなり、転んだだけでも[[□折する]]ことがある。", ["骨"], [("i", "□", ["ほね"]), ("j", "□折する", ["こっせつする", "こっせつ"])],
     "骨 = ほね / こつ: 骨(ほね) = bone; 骨折(こっせつ)する = break a bone. こつ → こっ."),
   ], [
    ("a", "①熱を出した[[息子]]が、…", ["むすこ"], "息子(むすこ) = son (special reading).", None),
    ("b", "…苦しそうに[[息]]をしている。", ["いき"], "息(いき) = breath.", None),
    ("c", "②今日こそは、机の上を[[整理]]しよう。", ["せいり"], "整理(せいり) = tidy up.", None),
    ("d", "③{上海|シャンハイ}には[[高層]]ビルが建っている。", ["こうそう"], "高層(こうそう)ビル = high-rise.", None),
    ("e", "④雨なので洗濯物を[[乾燥機]]で乾かした。", ["かんそうき"], "乾燥機(かんそうき) = dryer.", None),
    ("f", "⑤新しいCDの[[製作]]について、…", ["せいさく"], "製作(せいさく) = production (of goods).", None),
    ("g", "…会社の[[方針]]はまだ決まっていない。", ["ほうしん"], "方針(ほうしん) = policy.", None),
    ("h", "⑥誕生日の[[贈り物]]に…", ["おく", "おくりもの"], "贈(おく)り物(もの) = present.", "り"),
    ("i", "…ばらの[[花束]]をもらった。", ["はなたば"], "花束(はなたば) = bouquet. たば ← 束.", None),
    ("j", "⑦銀行で[[硬貨]]を…", ["こうか"], "硬貨(こうか) = coin.", None),
    ("k", "…[[お札]]に替えた。", ["さつ", "おさつ"], "お札(さつ) = banknote.", None),
    ("l", "⑧Aチームは[[勢い]]に乗って勝ち進み、とうとう優勝した。", ["いきお", "いきおい"], "勢(いきお)い = momentum.", "い"),
    ("m", "⑨[[昔話]]は親から子へ、…", ["むかしばなし"], "昔話(むかしばなし) = folk tale. はなし → ばなし.", None),
    ("n", "…子から[[孫]]へ、…", ["まご"], "孫(まご) = grandchild.", None),
    ("o", "…そしてその[[子孫]]へと伝えられてきた。", ["しそん"], "子孫(しそん) = descendants.", None),
   ], [
    ("1", "①彼は、パソコンの[[操作]]には自信を持っている。", ["そうさ", "そうさく", "そさ", "そさく"], 0, "Answer 1 操作(そうさ) = operation."),
    ("2", "②住所変更後、1年{未満|みまん}の住民は、この調査の対象から[[のぞき]]ます。", ["余き", "除き", "省き", "削き"], 1, "Answer 2 除(のぞ)く = exclude. 省く = はぶく, 削る = けずる."),
    ("3", "③会社に手紙を出す場合は、会社名の下に「[[御中]]」と書く。", ["おんちゅう", "おちゅう", "ぎょちゅう", "ごちゅう"], 0, "Answer 1 御中(おんちゅう) = used after a company name on letters."),
    ("4", "④この装置は危ないですから、[[触れて]]はいけません。", ["ふうれて", "さわれて", "されて", "ふれて"], 3, "Answer 4 触(ふ)れる = touch. (触る = さわる.)"),
    ("5", "⑤夕立がやむのを[[軒下]]で待っていた。", ["けんした", "のきした", "のきしも", "けんしも"], 1, "Answer 2 軒下(のきした) = under the eaves. (軒 = けん when counting houses.)"),
   ]),

  group("チャレンジ　接辞②　Ⅰ　（　）に入る漢字を1～4から選びなさい。",
   [dict(mcq("d13k-c1%d" % (i + 1), q, o, a, e), plainKeys=["opts"]) for i, (q, o, a, e) in enumerate(C2_I)]),
  plain(group("チャレンジ　接辞②　Ⅱ　□に入る共通の漢字を、　愛　外　用　観　再　から選んで（　）に書きなさい。",
   [fill("d13k-c2%d" % (i + 1), q.replace("（　）", "（%%）"), [a], e) for i, (q, a, e) in enumerate(C2_II)],
   lead="Box: 愛・外・用・観・再"), "lead"),
  plain(group("チャレンジ　接辞②　Ⅲ　［　］に入る共通の言葉を、　水道　禁煙　消防　新聞　文化　から選んで（　）に書きなさい。",
   [fill("d13k-c3%d" % (i + 1), q.replace("（　）", "（%%）", 1), [a], e) for i, (q, a, e) in enumerate(C2_III)],
   lead="Box: 水道・禁煙・消防・新聞・文化"), "lead"),
 ],
}
