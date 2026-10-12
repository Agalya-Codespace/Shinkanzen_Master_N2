/* Day 1 · 漢字 (新完全マスター漢字 N2, Step 1, pp.2–6). Transcribed from the book scan. */
window.N2_DAYS = window.N2_DAYS || {};
window.N2_DAYS[1] = window.N2_DAYS[1] || { title: "はじめの一歩", intro: "Today: 送り仮名 rules + 第1–4回 (Kanji), 親類・友人・知人 (Goi), ～とき・～直後に (Bunpo), 対比 (Dokkai).", sections: [] };
window.N2_DAYS[1].sections.push({
  book: "kanji",
  title: "ステップ1　送り仮名のルール ＋ 第1回～第4回",
  source: "新完全マスター漢字 N2 · pp.2–6 · 300まで",
  blocks: [
    {
      type: "wordlist",
      title: "📋 {今日|きょう}の{漢字|かんじ}リスト · Today's kanji words",
      lead: "Every kanji word printed in today's pages: the 送り仮名 rule examples, the クイズ and 第4回 Ⅱ. (The 第1–4回 CD sentences are audio only.) Hide a column to test yourself; tap a striped cell to peek.",
      explain: [
        "Indha list-la inniki pages-la vara ella kanji words-um irukku. Kanji book-la important: correct reading (ひらがな) and correct okurigana.",
        "Practice: 'ひらがな' column hide pannunga, kanji paathu reading solla try pannunga. Apram '漢字' hide pannunga, hiragana paathu kanji-a notebook-la ezhudhi paarunga. Okurigana enga start aagudhu nu kavanikkanum!"
      ],
      groups: [
        { h: "◆{動詞|どうし}の{例|れい}", words: [
          ["書く", "かく", "to write"],
          ["話す", "はなす", "to speak"],
          ["帰る", "かえる", "to return home"],
          ["考える", "かんがえる", "to think"],
          ["起きる", "おきる", "to get up; to happen"],
          ["変える", "かえる", "to change (something)"],
          ["着る", "きる", "to wear"],
          ["見る", "みる", "to see"],
          ["出る", "でる", "to go out"],
          ["寝る", "ねる", "to sleep"],
          ["止まる", "とまる", "to stop (intransitive)"],
          ["止める", "とめる", "to stop (something)"],
          ["伝わる", "つたわる", "to be conveyed"],
          ["伝える", "つたえる", "to convey; to tell"],
          ["助かる", "たすかる", "to be saved; to be helped"],
          ["助ける", "たすける", "to save; to help"],
          ["冷える", "ひえる", "to get cold"],
          ["冷やす", "ひやす", "to cool (something)"]
        ] },
        { h: "◆{形容詞|けいようし}・{派生語|はせいご}の{例|れい}", words: [
          ["美しい", "うつくしい", "beautiful"],
          ["新しい", "あたらしい", "new"],
          ["高い", "たかい", "high; expensive"],
          ["重い", "おもい", "heavy"],
          ["近い", "ちかい", "near"],
          ["大きい", "おおきい", "big"],
          ["小さい", "ちいさい", "small"],
          ["少ない", "すくない", "few"],
          ["冷たい", "つめたい", "cold (to the touch)"],
          ["静かな", "しずかな", "quiet"],
          ["確かな", "たしかな", "certain; reliable"],
          ["柔らかな", "やわらかな", "soft"],
          ["悲しい", "かなしい", "sad"],
          ["悲しむ", "かなしむ", "to grieve"],
          ["楽しい", "たのしい", "fun"],
          ["楽しみ", "たのしみ", "something to look forward to"],
          ["強い", "つよい", "strong"],
          ["強まる", "つよまる", "to become stronger"],
          ["頼む", "たのむ", "to ask; to request"],
          ["頼もしい", "たのもしい", "reliable; dependable"],
          ["憎む", "にくむ", "to hate"],
          ["憎らしい", "にくらしい", "hateful; detestable"]
        ] },
        { h: "【クイズ】", words: [
          ["働く", "はたらく", "to work"],
          ["食べる", "たべる", "to eat"],
          ["来る", "くる", "to come"],
          ["集まる", "あつまる", "to gather (intransitive)"],
          ["集める", "あつめる", "to collect (something)"],
          ["寒い", "さむい", "cold (weather)"],
          ["難しい", "むずかしい", "difficult"],
          ["暖かな", "あたたかな", "warm"],
          ["広い", "ひろい", "wide; spacious"],
          ["広がる", "ひろがる", "to spread; to widen"],
          ["喜ぶ", "よろこぶ", "to be glad"],
          ["喜び", "よろこび", "joy"]
        ] },
        { h: "{第|だい}４{回|かい}　Ⅱ", words: [
          ["湖", "みずうみ", "lake"],
          ["丸い", "まるい", "round"],
          ["映る", "うつる", "to be reflected"],
          ["大学", "だいがく", "university"],
          ["屋上", "おくじょう", "rooftop"],
          ["大小", "だいしょう", "large and small"],
          ["二つ", "ふたつ", "two (things)"],
          ["下さる", "くださる", "to give (to me; honorific)"],
          ["心温まる", "こころあたたまる", "heartwarming"],
          ["外科医", "げかい", "surgeon"],
          ["医学", "いがく", "medicine (the science)"],
          ["学ぶ", "まなぶ", "to learn; to study"],
          ["結婚", "けっこん", "marriage"],
          ["見事に", "みごとに", "completely; splendidly"],
          ["外れる", "はずれる", "to miss; to be wrong (a guess)"],
          ["世間", "せけん", "the world; people in general"],
          ["悪口", "わるくち", "bad-mouthing; speaking ill of others"],
          ["会う", "あう", "to meet (a person)"],
          ["急ぐ", "いそぐ", "to hurry"],
          ["駅", "えき", "station"],
          ["向かう", "むかう", "to head for"]
        ] }
      ]
    },
    {
      type: "text",
      t: "この{本|ほん}には、ＣＤを{聞|き}いて{文|ぶん}を{書|か}く{問題|もんだい}があります。{各回|かくかい}を{始|はじ}める{前|まえ}に、{送|おく}り{仮名|がな}のルールを{覚|おぼ}えましょう。\n{問題|もんだい}の{解|と}き{方|かた}はⅷページを{見|み}てください。",
      explain: [
        "Vanakkam! Inniki namma Kanji book-oda first page. Sensei solradhu: indha book-la CD kettu sentence ezhudhura (書く) questions irukku. Adhukku munnadi 送り仮名(おくりがな) rules-a nyabagam vechukkonga.",
        "送り仮名(おくりがな) na enna? Kanji-ku appuram varra hiragana part. Example: 書く(かく) — 書 kanji, く okurigana. 考える(かんがえる) — 考 kanji, える okurigana. N2 exam-la 'correct okurigana edhu?' nu kekkalaam, so idhu romba mukkiyam."
      ]
    },
    {
      type: "audio",
      title: "ＣＤを{聞|き}いて{書|か}く{問題|もんだい}の{書|か}き{方|かた}　CD1（p.ⅷ）",
      src: "audio/kanji/cd01.mp3",
      label: "CD 1 · {例|れい}",
      t: "Ⅰ{番|ばん}の{問題|もんだい}は、ＣＤを{聞|き}いて{文|ぶん}を{書|か}く{練習|れんしゅう}です。{文|ぶん}は２{回|かい}{読|よ}みます。できるだけ{最初|さいしょ}から{漢字|かんじ}を{使|つか}って{書|か}きましょう。\n・（　）の{中|なか}の{数|かず}は、{漢字|かんじ}の{数|かず}です。{例|れい}のように５と{書|か}いてあったら、{五|いつ}つの{漢字|かんじ}を{使|つか}って{文|ぶん}を{書|か}いてください。\n・{同|おな}じ{字|じ}がもう{一度|いちど}{出|で}てきたら、２{回|かい}と{数|かぞ}えます。\n{例|れい}）ＣＤ「いちにちいっかいはてきすとをみてください。」→（５）[[一日一回はテキストを見てください。]]\n**{書|か}き{方|かた}の{注意|ちゅうい}**\n(1)「{漢字|かんじ}」「{平仮名|ひらがな}」「{片仮名|かたかな}」を{使|つか}って{文|ぶん}を{書|か}きます。{数字|すうじ}は{漢字|かんじ}で{書|か}きます。（{一二三|いちにさん}……）\n(2) {次|つぎ}のようなものは、{平仮名|ひらがな}で{書|か}きます。「～て―」～てください、～ていく、～てくる、～てみる、～てあげる　「こと」～ことがある、～ことにする　「いう」～という、～からといって　「ほう」～たほうがいい　など\n(3)「わたし」は「{私|わたし}」と{漢字|かんじ}で{書|か}きます。\n{間違|まちが}いは{消|け}しゴムで{消|け}さないで、{線|せん}で{消|け}して、{正|ただ}しい{字|じ}を{書|か}きましょう。",
      explain: [
        "Dictation eppadi pannanum nu book sollitharudhu. CD 1 play pannunga: 'いちにちいっかいはてきすとをみてください' nu varum. Neenga ezhudhanum: 一日一回はテキストを見てください。 Kanji count: 一・日・一・回・見 = 5. 一 rendu thadava vandhaalum 2 nu count pannanum.",
        "Mukkiyamaana rules: numbers kanji-la (一二三). ～てください, ～ことがある, ～という, ～たほうがいい maadhiri grammar parts hiragana-la. 'わたし' mattum 私 nu kanji-la ezhudhunga."
      ]
    },
    {
      type: "table",
      title: "◆{動詞|どうし}",
      head: ["ルール", "{例|れい}"],
      rows: [
        ["①グループ１の{動詞辞書形|どうしじしょけい}は　**１{字|じ}{送|おく}る。**", "{書|か}く　{話|はな}す　{帰|かえ}る"],
        ["②-1　グループ２の{動詞辞書形|どうしじしょけい}は　**２{字|じ}{送|おく}る。**", "{考|かんが}える　{起|お}きる　{変|か}える"],
        ["②-2　グループ２の２{音|おん}の{動詞辞書形|どうしじしょけい}は　**１{字|じ}{送|おく}る。**", "{着|き}る　{見|み}る　{出|で}る　{寝|ね}る"],
        ["③{自動詞|じどうし}と{他動詞|たどうし}のある{動詞|どうし}は　**{音|おと}が{変|か}わるところから{送|おく}る。**", "（{下|した}の{表|ひょう}）"]
      ],
      explain: [
        "Rule ① Group 1 verb (う-verb) dictionary form-la kadaisi 1 letter mattum hiragana: 書(か)＋く, 話(はな)＋す, 帰(かえ)＋る.",
        "Rule ②-1 Group 2 verb (る-verb, ～える／～いる) — 2 letters anuppuvom: 考(かんが)＋える, 起(お)＋きる, 変(か)＋える.",
        "Rule ②-2 Group 2-la motham 2 sound mattum irundha (き・る = 2 音), 1 letter dhaan: 着(き)＋る, 見(み)＋る, 出(で)＋る, 寝(ね)＋る.",
        "Rule ③ 自動詞(じどうし, intransitive, ～が) / 他動詞(たどうし, transitive, ～を) pair irundha, sound maarra edathula irundhu okurigana start aagum. 止(と)まる / 止(と)める — 'ま' vs 'め' maarudhu, adhanaala 止まる, 止める. Idhu romba logical, paarunga!"
      ]
    },
    {
      type: "table",
      title: "{自動詞|じどうし}・{他動詞|たどうし}",
      rows: [
        ["{自動詞|じどうし}　～が", "＊{止|と}まる", "＊{伝|つた}わる", "＊{助|たす}かる", "{冷|ひ}える"],
        ["{他動詞|たどうし}　～を", "{止|と}める", "{伝|つた}える", "{助|たす}ける", "＊{冷|ひ}やす"]
      ],
      rowHead: true,
      note: "＊は{送|おく}り{仮名|がな}２{字|じ}のグループ１の{動詞|どうし}",
      explain: [
        "Table-a kavanichu paarunga. ＊ mark irukkura verbs ellam Group 1 verbs, aanaa okurigana 2 letters (止まる = ま・る). Yen? Rule ③ — sound maarra point-la irundhu send pannrom, adhanaala 2 letters.",
        "止(と)まる (stop, intransitive) ↔ 止(と)める (stop something). 伝(つた)わる (be conveyed) ↔ 伝(つた)える (convey). 助(たす)かる (be saved) ↔ 助(たす)ける (help/save). 冷(ひ)える (become cold) ↔ 冷(ひ)やす (cool something).",
        "Exam trap: '止る' or '冷す' nu ezhudhinaa thappu. Correct: 止まる, 冷やす."
      ]
    },
    {
      type: "table",
      title: "◆い{形容詞|けいようし}",
      head: ["ルール", "{例|れい}"],
      rows: [
        ["①「～しい」で{終|お}わる{言葉|ことば}は　**「しい」を{送|おく}る。**", "{美|うつく}しい　{新|あたら}しい"],
        ["②「～い」で{終|お}わる{言葉|ことば}は　**「い」を{送|おく}る。**", "{高|たか}い　{重|おも}い　{近|ちか}い"],
        ["{例外|れいがい}", "{大|おお}きい　{小|ちい}さい　{少|すく}ない　{冷|つめ}たい"]
      ],
      explain: [
        "い-adjective: '～しい' la mudinjaa 'しい' motham anuppuvom — 美(うつく)しい, 新(あたら)しい. Ille-naa 'い' mattum — 高(たか)い, 重(おも)い, 近(ちか)い.",
        "例外(れいがい) = exceptions. 大(おお)きい, 小(ちい)さい, 少(すく)ない, 冷(つめ)たい — idhu rule-a follow pannala, manapaadam pannunga. '大い', '少い' nu ezhudha koodaadhu."
      ]
    },
    {
      type: "table",
      title: "◆な{形容詞|けいようし}",
      head: ["ルール", "{例|れい}"],
      rows: [
        ["①「～かな」で{終|お}わる{言葉|ことば}は　**「かな」を{送|おく}る。**", "{静|しず}かな　{確|たし}かな"],
        ["②「～らかな」で{終|お}わる{言葉|ことば}は　**「らかな」を{送|おく}る。**", "{柔|やわ}らかな"]
      ],
      explain: [
        "な-adjective '～かな' la mudinjaa 'かな' anuppu: 静(しず)かな, 確(たし)かな. '～らかな' la mudinjaa 'らかな': 柔(やわ)らかな. Simple!"
      ]
    },
    {
      type: "table",
      title: "◆{派生語|はせいご}",
      rows: [
        ["{基本語|きほんご}", "{悲|かな}しい", "{楽|たの}しい", "{強|つよ}い", "{頼|たの}む", "{憎|にく}む"],
        ["{派生語|はせいご}", "{悲|かな}しむ", "{楽|たの}しみ", "{強|つよ}まる", "{頼|たの}もしい", "{憎|にく}らしい"]
      ],
      rowHead: true,
      note: "①{基本|きほん}になっている{語|ご}の{送|おく}り{仮名|がな}に{基|もと}づく。",
      explain: [
        "派生語(はせいご) = derived word. Rule: base word-oda okurigana-va follow pannu.",
        "悲(かな)しい → 悲(かな)しむ (to grieve). 楽(たの)しい → 楽(たの)しみ (fun / looking forward). 強(つよ)い → 強(つよ)まる (become stronger). 頼(たの)む → 頼(たの)もしい (reliable). 憎(にく)む → 憎(にく)らしい (hateful).",
        "Kavanikkanum: 楽 and 頼 rendum 'たの' reading. 楽しい (fun) vs 頼む (request) — kanji vera vera, meaning vera vera."
      ]
    },
    {
      type: "group",
      title: "【クイズ】{次|つぎ}の{言葉|ことば}の{送|おく}り{仮名|がな}を{書|か}いてみましょう。",
      lead: "Type only the okurigana (or the whole word). p.3",
      scored: true,
      explain: "Ippo neenga try pannunga. Kanji already kuduthirukku, okurigana mattum type pannunga. Mudinjaa 'Why?' button-la rule paarunga.",
      children: [
        { type: "fill", id: "d1k-q1", q: "①はたらく　→（{働|はたら}%%）", ans: ["く", "働く"], ansNote: "働く", explain: "働(はたら)く — Group 1 verb, so 1 letter: く. Rule ①." },
        { type: "fill", id: "d1k-q2", q: "②たべる　→（{食|た}%%）", ans: ["べる", "食べる"], ansNote: "食べる", explain: "食(た)べる — Group 2 verb (た・べ・る, 3 sounds), so 2 letters: べる. Rule ②-1." },
        { type: "fill", id: "d1k-q3", q: "③くる　→（{来|く}%%）", ans: ["る", "来る"], ansNote: "来る", explain: "来(く)る — 1 letter る. (来る is irregular, but okurigana is just る.)" },
        { type: "fill", id: "d1k-q4", q: "④あつまる　→（{集|あつ}%%）", ans: ["まる", "集まる"], ansNote: "集まる", explain: "集(あつ)まる / 集(あつ)める pair — sound maarra edam ま/め. So 集まる. Rule ③." },
        { type: "fill", id: "d1k-q5", q: "⑤あつめる　→（{集|あつ}%%）", ans: ["める", "集める"], ansNote: "集める", explain: "集(あつ)める — transitive pair of 集まる, sound changes at め. So 集める. Rule ③." },
        { type: "fill", id: "d1k-q6", q: "⑥さむい　→（{寒|さむ}%%）", ans: ["い", "寒い"], ansNote: "寒い", explain: "寒(さむ)い — ～い adjective (not ～しい), so only い." },
        { type: "fill", id: "d1k-q7", q: "⑦むずかしい→（{難|むずか}%%）", ans: ["しい", "難しい"], ansNote: "難しい", explain: "難(むずか)しい — ends in ～しい, so send しい." },
        { type: "fill", id: "d1k-q8", q: "⑧あたたかな→（{暖|あたた}%%）", ans: ["かな", "暖かな"], ansNote: "暖かな", explain: "暖(あたた)かな — な-adjective ending ～かな, so send かな." },
        { type: "fill", id: "d1k-q9", q: "⑨ひろい　→（{広|ひろ}%%）", ans: ["い", "広い"], ansNote: "広い", explain: "広(ひろ)い — normal ～い adjective → い." },
        { type: "fill", id: "d1k-q10", q: "⑩ひろがる　→（{広|ひろ}%%）", ans: ["がる", "広がる"], ansNote: "広がる", explain: "広(ひろ)がる / 広(ひろ)げる pair — sound changes at が/げ → 広がる. Also a 派生語 of 広い, so 広 + がる." },
        { type: "fill", id: "d1k-q11", q: "⑪よろこぶ　→（{喜|よろこ}%%）", ans: ["ぶ", "喜ぶ"], ansNote: "喜ぶ", explain: "喜(よろこ)ぶ — Group 1 verb → 1 letter ぶ." },
        { type: "fill", id: "d1k-q12", q: "⑫よろこび→（{喜|よろこ}%%）", ans: ["び", "喜び"], ansNote: "喜び", explain: "喜(よろこ)び — noun from 喜ぶ. 派生語 rule: follow the base word, so 喜 + び." }
      ]
    },
    {
      type: "dictation",
      id: "r1",
      audio: "audio/kanji/cd02.mp3",
      audioLabel: "CD 2 · 漢字 N2",
      title: "{第|だい}１{回|かい}　300まで",
      lead: "Ⅰ　ＣＤを{聞|き}いて、{指示|しじ}された{数|かず}の{漢字|かんじ}を{使|つか}って{文|ぶん}を{書|か}きなさい。{数字|すうじ}も{漢字|かんじ}で{書|か}きます。CD2",
      counts: [5, 8, 5, 5, 7, 7, 12],
      note: "The number in （　） is how many kanji your sentence must use. Play CD track 2 above (pause after each sentence). The answer booklet is not in your PDF, so this site cannot check these; write them here and they stay saved.",
      explain: [
        "Idhu dictation. CD-la oru sentence varum, adha kettu ezhudhanum. (5) na 5 kanji use pannanum. Numbers kooda kanji-la: 三, 十 maadhiri.",
        "'300まで' na: book-oda first 300 kanji list-la irundhu dhaan varum. Mela irukkura player-la CD track play pannunga; oru sentence mudinjadhum pause panni ezhudhunga. Slow-aa kekkanum na 0.75× button use pannunga."
      ]
    },
    {
      type: "dictation",
      id: "r2",
      audio: "audio/kanji/cd03.mp3",
      audioLabel: "CD 3 · 漢字 N2",
      title: "{第|だい}２{回|かい}　300まで",
      lead: "Ⅰ　ＣＤを{聞|き}いて、{指示|しじ}された{数|かず}の{漢字|かんじ}を{使|つか}って{文|ぶん}を{書|か}きなさい。{数字|すうじ}も{漢字|かんじ}で{書|か}きます。CD3",
      counts: [9, 7, 6, 8, 6, 6, 7],
      note: "CD track 3. Same as 第1回."
    },
    {
      type: "dictation",
      id: "r3",
      audio: "audio/kanji/cd04.mp3",
      audioLabel: "CD 4 · 漢字 N2",
      title: "{第|だい}３{回|かい}　300まで",
      lead: "Ⅰ　ＣＤを{聞|き}いて、{指示|しじ}された{数|かず}の{漢字|かんじ}を{使|つか}って{文|ぶん}を{書|か}きなさい。{数字|すうじ}も{漢字|かんじ}で{書|か}きます。CD4",
      counts: [8, 6, 9, 7, 6, 10, 8, 8],
      note: "CD track 4. In the book, 第3回 has only this dictation part."
    },
    {
      type: "dictation",
      id: "r4",
      audio: "audio/kanji/cd05.mp3",
      audioLabel: "CD 5 · 漢字 N2",
      title: "{第|だい}４{回|かい}　300まで",
      lead: "Ⅰ　ＣＤを{聞|き}いて、{指示|しじ}された{数|かず}の{漢字|かんじ}を{使|つか}って{文|ぶん}を{書|か}きなさい。{数字|すうじ}も{漢字|かんじ}で{書|か}きます。CD5",
      counts: [15, 14, 6, 4, 10, 6, 6, 8],
      note: "CD track 5."
    },
    {
      type: "group",
      title: "{第|だい}４{回|かい}　Ⅱ　＿＿の{部分|ぶぶん}の{漢字|かんじ}には{読|よ}み{仮名|がな}を、{平仮名|ひらがな}には{漢字|かんじ}を（{送|おく}り{仮名|がな}も）{書|か}きなさい。",
      lead: "Underlined kanji → write the reading. Underlined hiragana → write kanji (with okurigana). The book's answer box already prints some okurigana (shown after the box).",
      scored: true,
      explain: "Kanji-ku hiragana reading ezhudhanum; hiragana-ku kanji ezhudhanum. Box-la sila okurigana already print panni irukku (って, つ, さる...), adhanaala avanga munnadi irukkura part mattum ezhudhinaa podhum. (Book-oda answer booklet unga PDF-la illa — indha answers naan check panni kuduthadhu.)",
      children: [
        { type: "fill", id: "d1k-2a", q: "①{夜|よる}の{湖|みずうみ}に、{丸|まる}い{月|つき}が[[映って]]いる。　a", suffix: "って", ans: ["うつ", "うつって"], ansNote: "うつ（って）", explain: "映(うつ)る = to be reflected. 映っている = is reflected. 'The round moon is reflected on the night lake.' 映(えい) on-reading (映画 えいが) kooda nyabagam vechukko." },
        { type: "fill", id: "d1k-2b", q: "②{新|あたら}しい[[大学]]の…　b", ans: ["だいがく"], explain: "大学(だいがく) = university." },
        { type: "fill", id: "d1k-2c", q: "…[[屋上]]には、…　c", ans: ["おくじょう"], explain: "屋上(おくじょう) = rooftop. 屋 = おく (on), 上 = じょう. 'やね' (屋根, roof) kooda irukku, confuse aagaadheenga." },
        { type: "fill", id: "d1k-2d", q: "…[[だいしょう]]…　d", ans: ["大小"], explain: "だいしょう = 大小 (big and small). 大小二つのプール = two pools, one big and one small." },
        { type: "fill", id: "d1k-2e", q: "…[[二つ]]のプールがある。　e", suffix: "つ", ans: ["ふた", "ふたつ"], ansNote: "ふた（つ）", explain: "二(ふた)つ = two (things). Box-la つ already irukku, so ふた mattum." },
        { type: "fill", id: "d1k-2f", q: "③{先生|せんせい}が[[下さる]]{手紙|てがみ}には、いつも{心温|こころあたた}まる{言葉|ことば}が{書|か}いてある。　f", suffix: "さる", ans: ["くだ", "くださる"], ansNote: "くだ（さる）", explain: "下(くだ)さる = (someone higher) gives me — 'くれる' oda respectful form. 'The letters my teacher gives me always have heart-warming words.' 心温(こころあたた)まる = heart-warming." },
        { type: "fill", id: "d1k-2g", q: "④{妹|いもうと}は、[[外科]]{医|い}になるために…　g", ans: ["げか"], explain: "外科(げか) = surgery (department). 外科医(げかい) = surgeon. 外 here is 'げ', not 'がい' — idhu exam favourite trap!" },
        { type: "fill", id: "d1k-2h", q: "…{大学|だいがく}で[[医学]]を…　h", ans: ["いがく"], explain: "医学(いがく) = medical science." },
        { type: "fill", id: "d1k-2i", q: "…[[学んで]]いる。　i", suffix: "んで", ans: ["まな", "まなんで"], ansNote: "まな（んで）", explain: "学(まな)ぶ = to learn/study. 学んでいる = is studying. 学 kun-reading まな(ぶ)." },
        { type: "fill", id: "d1k-2j", q: "⑤みんなあの{二人|ふたり}が{結婚|けっこん}するだろうと{思|おも}っていたが、[[見事に]]　j", suffix: "に", ans: ["みごと", "みごとに"], ansNote: "みごと（に）", explain: "見事(みごと)に = completely / splendidly. Inga 'completely (wrong)' nu artham: everyone thought they'd marry, but the guess was completely wrong." },
        { type: "fill", id: "d1k-2k", q: "…[[外れた]]。　k", suffix: "れた", ans: ["はず", "はずれた"], ansNote: "はず（れた）", explain: "外(はず)れる = to miss / be wrong (a guess). 予想が外れる = prediction misses. 外 has many readings: そと, がい, げ, はず(れる), はず(す)." },
        { type: "fill", id: "d1k-2l", q: "⑥あの{人|ひと}が{話|はな}すことは、[[世間]]のうわさと…　l", ans: ["せけん"], explain: "世間(せけん) = society / the world / people in general. 世 = せ, 間 = けん here (not かん!). 世間のうわさ = gossip going around." },
        { type: "fill", id: "d1k-2m", q: "…{人|ひと}の[[わるくち]]ばかりだ。　m", ans: ["悪口"], explain: "わるくち (also わるぐち) = 悪口 = speaking ill of others. 'All that person talks about is gossip and bad-mouthing people.'" },
        { type: "fill", id: "d1k-2n", q: "⑦{友達|ともだち}に[[あう]]ために、…　n", ans: ["会う"], explain: "あう (meet a person) = 会う. 合う (fit/match) is different! Friend-a meet panradhu → 会う." },
        { type: "fill", id: "d1k-2o", q: "…[[いそいで]]{駅|えき}に{向|む}かった。　o", ans: ["急いで"], explain: "いそいで = 急(いそ)いで, from 急ぐ (hurry). Group 1 verb → okurigana from ぐ: 急ぐ → 急いで." }
      ]
    }
  ]
});
