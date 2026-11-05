from _h import *
DAY = 18
TITLE = "総合問題2と統合理解"
INTRO = "Today: Kanji 総合問題2 and チャレンジ 接辞③, Goi 7章 1・2課 (複合語), Bunpo 第3部 3–6課, Dokkai 第3部 統合理解, Chokai Ⅵ 統合理解 問題形式・1."

P = "d18k"

WORDS = [
 ("総合問題2", [["日本","にほん","Japan"],["四つ","よっつ","four"],["島","しま","island"],["国","くに","country"],["生まれる","うまれる","to be born"],["神話","しんわ","myth"],["場合","ばあい","case"],["男","おとこ","man"],["女","おんな","woman"],["神様","かみさま","god"],["結婚","けっこん","marriage"],["作る","つくる","to make"],["大人","おとな","adult"],["幼い","おさない","very young"],["子供","こども","child"],["悩む","なやむ","to worry"],["苦しむ","くるしむ","to suffer"],["思う","おもう","to think"],["単純","たんじゅん","simple"],["児童文学者","じどうぶんがくしゃ","children's author"],["甘い","あまい","sweet"],["お菓子","おかし","sweets"],["話","はなし","story"],["与える","あたえる","to give"],["間違い","まちがい","mistake"],["彼ら","かれら","they"],["以上","いじょう","more than"],["死","し","death"],["恐怖","きょうふ","fear"],["感じる","かんじる","to feel"],["人生","じんせい","life"],["意味","いみ","meaning"],["考える","かんがえる","to think"],["語る","かたる","to talk about"],["上昇","じょうしょう","rise"],["下降","かこう","descent"],["容易","ようい","easy"],["困難","こんなん","difficult"],["個人","こじん","individual"],["団体","だんたい","group, team"],["出発","しゅっぱつ","departure"],["到着","とうちゃく","arrival"],["複雑","ふくざつ","complicated"],["支出","ししゅつ","expenditure"],["収入","しゅうにゅう","income"],["体重","たいじゅう","body weight"],["重体","じゅうたい","critical condition"],["階段","かいだん","stairs"],["段階","だんかい","stage"],["実現","じつげん","realisation"],["現実","げんじつ","reality"],["先祖","せんぞ","ancestor"],["祖先","そせん","ancestor (of a species)"],["精神","せいしん","mind"],["原因","げんいん","cause"],["身体的","しんたいてき","physical"],["深刻","しんこく","serious"],["医師","いし","doctor"],["接する","せっする","to deal with"],["印象","いんしょう","impression"],["周囲","しゅうい","surroundings, people around"],["期待通り","きたいどおり","as expected"],["優しい","やさしい","kind"],["設計","せっけい","plan, design"],["急","きゅう","sudden, rapid"],["常に","つねに","always"],["職場","しょくば","workplace"],["追われる","おわれる","to be driven out"],["必死に","ひっしに","desperately"],["脳","のう","brain"],["生じる","しょうじる","to be produced"],["感覚","かんかく","sense, feeling"],["含める","ふくめる","to include"],["冷静","れいせい","calm"],["観察","かんさつ","observation"],["努力","どりょく","effort"],["実る","みのる","to bear fruit"],["勇気","ゆうき","courage"]]),
 ("チャレンジ 接辞③", [["裏通り","うらどおり","back street"],["消費税","しょうひぜい","consumption tax"],["日光浴","にっこうよく","sunbathing"],["最新版","さいしんばん","latest edition"],["旧姓","きゅうせい","maiden name"],["珍事件","ちんじけん","strange incident"],["理科系","りかけい","science stream"],["合理化","ごうりか","rationalisation"],["可能性","かのうせい","possibility"],["反対派","はんたいは","the opposition"],["超高層","ちょうこうそう","super high-rise"]]),
]

def write(id, title, rows, explain):
    return {"type": "dictation", "id": id, "title": title,
            "lead": "Ⅰ　次の文を、漢字で書ける部分はできるだけ漢字を使って書きなさい。Type each sentence using kanji wherever you can, then press Check or open Answer. The number is how many characters the model answer has (punctuation included).",
            "counts": [len(a) for _, a in rows], "answers": [a for _, a in rows], "explain": explain,
            "note": "Hiragana you have to convert, sentence by sentence:\n" + "\n".join("%s　%s" % ("①②③④⑤⑥⑦⑧⑨⑩"[i], q) for i, (q, _) in enumerate(rows))}

W1 = [
 ("にほんはよっつのしまからなっています。", "日本は四つの島から成っています。"),
 ("どこのくににも、くにがどうやってうまれたかというしんわがありますが、", "どこの国にも、国がどうやって生まれたかという神話がありますが、"),
 ("にほんのばあいは、おとことおんなのかみさまがけっこんして、これらのしまをつくったということになっています。", "日本の場合は、男と女の神様が結婚して、これらの島を作ったということになっています。"),
]
W2 = [
 ("おとなは、おさないこどもはなやんだりくるしんだりすることはないとおもいがちだ。", "大人は、幼い子供は悩んだり{苦|くる}しんだりすることはないと思いがちだ。"),
 ("しかし、こどもはそんなにたんじゅんではない。", "しかし、子供はそんなに単純ではない。"),
 ("あるじどうぶんがくしゃは、「こどもにあまいおかしのようなはなしばかりあたえるのはまちがいだ。", "ある児童文学者は、「子供に甘いお菓子のような話ばかり与えるのは間違いだ。"),
 ("かれらはおとないじょうにしのきょうふをかんじ、じんせいのいみをかんがえている。」とかたっている。", "彼らは大人以上に死の恐怖を感じ、人生の意味を考えている。」と語っている。"),
]

def rf(id, q, ans, ex, suf=None):
    return fill(id, q, ans if isinstance(ans, list) else [ans], ex, suffix=suf)

S_II = group("総合問題2　Ⅱ　次の文の＿＿には〰〰を引いた語と反対の意味の言葉が入ります。考えて入れ、読み仮名も書きなさい。", [
  text("（例）{遠足|えんそく}の日は朝学校に〰集合〰して、帰りは駅で[[解散]]します。（かいさん）"),
  rf(P + "-s2-1", "①{飛行機|ひこうき}が〰{上昇|じょうしょう}〰したかと思うと、急に＿＿した。　＿＿＝%%", "下降", "上昇(じょうしょう) rise ↔ 下降(かこう) descent."),
  rf(P + "-s2-1y", "　↳ 読み方：%%", "かこう", ""),
  rf(P + "-s2-2", "②計画するのは〰{容易|ようい}〰だが、それを実行するには＿＿な問題がある。　＿＿＝%%", "困難", "容易(ようい) easy ↔ 困難(こんなん) difficult."),
  rf(P + "-s2-2y", "　↳ 読み方：%%", "こんなん", "", "な"),
  rf(P + "-s2-3", "③マラソンは〰{個人|こじん}〰{競技|きょうぎ}で、サッカーは＿＿競技だ。　＿＿＝%%", "団体", "個人競技 individual sport ↔ 団体競技(だんたいきょうぎ) team sport."),
  rf(P + "-s2-3y", "　↳ 読み方：%%", "だんたい", ""),
  rf(P + "-s2-4", "④{成田|なりた}の〰{出発|しゅっぱつ}〰時刻は9時で、{北京|ペキン}には3時間後に＿＿の予定です。　＿＿＝%%", "到着", "出発 departure ↔ 到着(とうちゃく) arrival."),
  rf(P + "-s2-4y", "　↳ 読み方：%%", "とうちゃく", ""),
  rf(P + "-s2-5", "⑤これは〰{複雑|ふくざつ}〰な問題ではない。＿＿な計算を{繰|く}り{返|かえ}せば答えが出る。　＿＿＝%%", "単純", "複雑(ふくざつ) complicated ↔ 単純(たんじゅん) simple."),
  rf(P + "-s2-5y", "　↳ 読み方：%%", "たんじゅん", "", "な"),
  rf(P + "-s2-6", "⑥〰{支出|ししゅつ}〰が増える割に、＿＿が増えない。　＿＿＝%%", "収入", "支出(ししゅつ) spending ↔ 収入(しゅうにゅう) income."),
  rf(P + "-s2-6y", "　↳ 読み方：%%", "しゅうにゅう", ""),
 ], lead="Type the opposite word in kanji, then its reading.")

S_III = group("総合問題2　Ⅲ　次の二つの文の＿＿には前後入れ替えた漢字の言葉が入ります。□の中から漢字を選んで入れ、（　）には読み仮名も書きなさい。", [
  dict(text("Box: ~~会~~　体　階　先　~~社~~　実　祖　段　現　重"), plainKeys=["t"]),
  text("（例）父は今年定年で[[会社]]を辞めた。（かいしゃ）／[[社会]]制度の発達についてレポートを書いた。（しゃかい）"),
  rf(P + "-s3-1a", "①お{相撲|すもう}さんの＿＿は100キロ以上ある。　＿＿＝%%", "体重", "体重(たいじゅう) = body weight."),
  rf(P + "-s3-1ay", "　↳ 読み方：%%", "たいじゅう", ""),
  rf(P + "-s3-1b", "　病人が＿＿になったので{救急車|きゅうきゅうしゃ}を呼んだ。　＿＿＝%%", "重体", "重体(じゅうたい) = critical condition. 体重 ↔ 重体: same two kanji, swapped."),
  rf(P + "-s3-1by", "　↳ 読み方：%%", "じゅうたい", ""),
  rf(P + "-s3-2a", "②エレベーターが{故障|こしょう}しているから＿＿で行こう。　＿＿＝%%", "階段", "階段(かいだん) = stairs."),
  rf(P + "-s3-2ay", "　↳ 読み方：%%", "かいだん", ""),
  rf(P + "-s3-2b", "　事態は新たな＿＿を{迎|むか}えた。　＿＿＝%%", "段階", "段階(だんかい) = stage, phase."),
  rf(P + "-s3-2by", "　↳ 読み方：%%", "だんかい", ""),
  rf(P + "-s3-3a", "③長年の夢が＿＿してうれしい。　＿＿＝%%", "実現", "実現(じつげん)する = come true."),
  rf(P + "-s3-3ay", "　↳ 読み方：%%", "じつげん", ""),
  rf(P + "-s3-3b", "　理想ばかり追っていないで＿＿をよく考えなさい。　＿＿＝%%", "現実", "現実(げんじつ) = reality."),
  rf(P + "-s3-3by", "　↳ 読み方：%%", "げんじつ", ""),
  rf(P + "-s3-4a", "④＿＿の{墓参|はかまい}りに行った。　＿＿＝%%", "先祖", "先祖(せんぞ) = (family) ancestors. 墓参り = visiting the grave."),
  rf(P + "-s3-4ay", "　↳ 読み方：%%", "せんぞ", ""),
  rf(P + "-s3-4b", "　人類の＿＿は{猿|さる}だという説がある。　＿＿＝%%", "祖先", "祖先(そせん) = ancestor of a species. 先祖 is for your own family line; 祖先 for humankind, species."),
  rf(P + "-s3-4by", "　↳ 読み方：%%", "そせん", ""),
 ], lead="Each pair uses the same two kanji in swapped order.")

IV1 = ("①　[[精神]](a)の病気にかかる人が増えているが、[[げんいん]](b)としては、[[身体]](c)的なもの、つらい体験から来るもの、特に理由のないものの三つに分けられる。一般に、心の病気というと体の病気とは違うと考えられがちだが、[[深刻]](d)に考えずに、すぐに医者にかかり、薬で治すほうがいい。ある精神科の[[医師]](e)の話では、「{患者|かんじゃ}に[[接した]](f)[[印象]](g)では、[[しゅうい]](h)の評判を気にして[[期待通り]](i)に動こうとするまじめで[[優しい]](j)人ほどかかりやすい。」とのことだった。",
 [("a", "せいしん", "精神(せいしん) = mind, spirit.", None), ("b", "原因", "げんいん = 原因 (cause).", None), ("c", "しんたい", "身体(しんたい)的 = physical. 体 = たい here.", None),
  ("d", "しんこく", "深刻(しんこく) = serious.", None), ("e", "いし", "医師(いし) = doctor.", None), ("f", ["せっ", "せっした"], "接(せっ)する = deal with. The book's box already prints した.", "した"),
  ("g", "いんしょう", "印象(いんしょう) = impression.", None), ("h", "周囲", "しゅうい = 周囲 (people around).", None), ("i", ["きたいどお", "きたいどおり"], "期待通(きたいどお)り = as expected. 通り → どおり after a noun.", "り"),
  ("j", ["やさ", "やさしい"], "優(やさ)しい = kind.", "しい")])
IV2 = ("②　{平均寿命|へいきんじゅみょう}が伸びた今日、人生[[せっけい]](a)をきちんと持つことが大切になっている。特に、技術の進歩が[[急]](b)テンポになったため、[[常に]](c)能力を高めておかないと、[[職場]](d)を[[おわれる]](e)ことにもなりかねない。だからといって、[[必死に]](f)仕事と勉強という生活も{寂|さび}しいものだ。最近の研究によると、人間の[[脳]](g)は楽しい時ほど、脳を{刺激|しげき}する物質が[[生じて]](h)よく働くという。仕事も勉強も遊び[[かんかく]](i)で楽しめたら最高だ。また、よい仲間を見付けることも重要だ。相手のことを生活面も[[ふくめて]](j)[[れいせい]](k)に[[かんさつ]](l)し、アドバイスし合える友人を持とう。長い人生の中で、[[努力]](m)が[[実らない]](n)時もある。そんな時も仲間がいれば[[勇気]](o)も出る。",
 [("a", "設計", "せっけい = 設計 (plan, design). 人生設計 = life plan.", None), ("b", "きゅう", "急(きゅう)テンポ = rapid pace.", None), ("c", ["つね", "つねに"], "常(つね)に = always.", "に"),
  ("d", "しょくば", "職場(しょくば) = workplace.", None), ("e", "追われる", "おわれる = 追われる (be driven out). 職場を追われる = lose your job.", None), ("f", ["ひっし", "ひっしに"], "必死(ひっし)に = desperately.", "に"),
  ("g", "のう", "脳(のう) = brain.", None), ("h", ["しょう", "しょうじて"], "生(しょう)じる = be produced, arise.", "じて"), ("i", "感覚", "かんかく = 感覚. 遊び感覚 = as if it were play.", None),
  ("j", "含めて", "ふくめて = 含めて (including).", None), ("k", "冷静", "れいせい = 冷静 (calm).", None), ("l", "観察", "かんさつ = 観察 (observation).", None),
  ("m", "どりょく", "努力(どりょく) = effort.", None), ("n", ["みの", "みのらない"], "実(みの)る = bear fruit. 努力が実らない = effort doesn't pay off.", "らない"), ("o", "ゆうき", "勇気(ゆうき) = courage.", None)])

def iv_group():
    ch = []
    for k, (t, rows) in enumerate([IV1, IV2]):
        ch.append(dict(text(t), noRubyU=True))
        for L, ans, ex, suf in rows:
            ch.append(rf("%s-s4%d%s" % (P, k + 1, L), "%s %s　→ %%%%" % ("①②"[k], L), ans, ex, suf))
    return group("総合問題2　Ⅳ　＿＿部分の漢字は読み仮名を、平仮名は漢字を（送り仮名も）書きなさい。", ch,
                 lead="Read each passage. For every underlined word: kanji → type the reading; hiragana → type the kanji (with okurigana).")

C3_I = [
 ("①今日はお祭りで表通りが込んでいるので、（　）通りを通って駅まで行きましょう。", ["離", "別", "裏", "静"], 2, "Answer 3. 表通り (main street) ↔ 裏通り(うらどおり) = back street."),
 ("②私の国の消費（　）は日本のより高い。", ["賃", "金", "税", "料"], 2, "Answer 3. 消費税(しょうひぜい) = consumption tax. ～税: 所得税, 住民税."),
 ("③よく晴れて気持ちのいい日には、外で日光（　）を楽しみたい。", ["味", "食", "吸", "浴"], 3, "Answer 4. 日光浴(にっこうよく) = sunbathing. ～浴: 森林浴, 海水浴."),
 ("④インターネットでそのニュースの最新（　）がチェックできる。", ["面", "本", "帳", "版"], 3, "Answer 4. 最新版(さいしんばん) = latest edition. ～版: 日本語版, 電子版."),
 ("⑤結婚して姓が変わっても、（　）姓で呼ばれている。", ["旧", "前", "古", "新"], 0, "Answer 1. 旧姓(きゅうせい) = maiden name. 旧～ = former: 旧友, 旧館."),
 ("⑥空から魚が降るという（　）事件が報道された。", ["実", "変", "新", "珍"], 3, "Answer 4. 珍事件(ちんじけん) = strange incident. 珍(ちん)～ = rare, odd: 珍現象."),
]
C3_II = [
 ("①コンピューターの仕事をするなら理科（　）に進んだほうがよい。", "系", "理科系(りかけい) = science track. ～系: 文科系, 体育会系."),
 ("②鉄道各社は自動改札にして合理（　）を進めた。", "化", "合理化(ごうりか) = rationalisation. ～化: 自動化, 国際化."),
 ("③地球外に生物がいる可能（　）があると思いますか。", "性", "可能性(かのうせい) = possibility. ～性: 安全性, 必要性."),
 ("④ダムの建設について、反対（　）の住民が集会を開いた。", "派", "反対派(はんたいは) = the opposing side. ～派: 賛成派, 改革派."),
 ("⑤都心には（　）高層ビルが立ち並んでいる。", "超", "超高層(ちょうこうそう) = super high-rise. 超～: 超特急, 超大型."),
]

SECTION = {
 "book": "kanji",
 "title": "総合問題2・チャレンジ 接辞③",
 "source": "新完全マスター漢字 N2 · pp.108–111 · this PDF has no answer pages, so answers are sensei's, checked word by word",
 "blocks": [
  wordlist("📋 今日の漢字リスト · Today's kanji words", WORDS,
   "Every answer word from today's pages. Hide a column to test yourself; tap a striped cell to peek.",
   ["Today is a review day. 総合問題2 mixes everything from ステップ3 (第40–53回), then the last 接辞 challenge.",
    "Opposite pairs: 上昇↔下降, 容易↔困難, 個人↔団体, 出発↔到着, 複雑↔単純, 支出↔収入.",
    "Swapped pairs: 体重／重体, 階段／段階, 実現／現実, 先祖／祖先 — same kanji, different meaning!"]),
  text("ステップ3の復習です。", "総合問題2", ["Idhu ステップ3 review test. Neenga mudhalla try pannunga, appuram 💡 paarunga.",
   "Ⅰ is a writing task: the book gives all-hiragana sentences and you rewrite them with as much kanji as possible. Watch okurigana: 成(な)っています, 幼(おさな)い, 悩(なや)んだり, 苦(くる)しんだり, 与(あた)える."]),
  text("（例）にほんごのべんきょうはたのしいです。→ 日本語の勉強は楽しいです。", "Ⅰ の（例）"),
  write("k-s2-1", "総合問題2　Ⅰ ①", W1, ["Sensei: 四つ(よっつ), 島(しま), 成る(なる) — 'is made up of' (written 成っています or なっています; both are fine on the test).",
   "神話(しんわ) = myth; 神様(かみさま) = gods. ということになっています = so the story goes."]),
  write("k-s2-2", "総合問題2　Ⅰ ②", W2, ["Sensei: 幼い子供, 悩んだり{苦|くる}しんだり, ～がちだ (tend to), 単純(たんじゅん), 児童文学者(じどうぶんがくしゃ), お菓子(かし), 与える, 間違い, 恐怖(きょうふ), 語る(かたる).",
   "If you wrote some words in hiragana (e.g. なっています, お菓子 → おかし), it's not wrong Japanese — compare with the Answer and see which kanji you missed."]),
  S_II, S_III, iv_group(),

  text("接辞（せつじ）のまとめ問題です。", "チャレンジ　接辞③", ["Last 接辞 set: prefixes 裏～, 旧～, 珍～, 超～ and suffixes ～税, ～浴, ～版, ～系, ～化, ～性, ～派."]),
  group("チャレンジ 接辞③　Ⅰ　（　）に入る漢字を1～4から選びなさい。",
   [dict(mcq("%s-c1-%d" % (P, i + 1), q, o, a, e, keys=["1", "2", "3", "4"]), plainKeys=["opts"]) for i, (q, o, a, e) in enumerate(C3_I)]),
  group("チャレンジ 接辞③　Ⅱ　次の文の（　）に入る漢字を、□から選んで書きなさい。　系　派　化　性　超",
   [rf("%s-c2-%d" % (P, i + 1), q + "　（　）＝%%", a, e) for i, (q, a, e) in enumerate(C3_II)]),
 ],
}
