/* Day 4 · bunpo. Built from d04_bunpo.py by tools/build_day.py (furigana added automatically). */
window.N2_DAYS = window.N2_DAYS || {};
window.N2_DAYS[4] = window.N2_DAYS[4] || {"title": "", "intro": "", "sections": []};
if (false) window.N2_DAYS[4].title = "";
if (false) window.N2_DAYS[4].intro = "";
window.N2_DAYS[4].sections.push({
 "book": "bunpo",
 "title": "Ⅰ ことがらを{説明|せつめい}する☆　6{課|か} ～だけではなく・それに{加|くわ}えて／7{課|か} ～について・～を{相手|あいて}にして",
 "source": "新完全マスター文法 N2 · 第1部 文の文法1 · pp.30–37 · answers from 別冊 解答 p.3",
 "blocks": [
  {
   "type": "items",
   "title": "6{課|か}　〔{復習|ふくしゅう}〕",
   "items": [
    {
     "t": "・この{公園|こうえん}では、{子供|こども}[[だけでなく]]{大人|おとな}も{楽|たの}しむことができる。",
     "explain": "Review: だけでなく = not only. Kids mattum illa, periyavangalum."
    },
    {
     "t": "・わたしは{音楽|おんがく}を{聞|き}くのが{好|す}きな[[ばかりでなく]]、{自分|じぶん}でも{作曲|さっきょく}します。",
     "explain": "Review: ばかりでなく = not only. 作曲(さっきょく) = compose."
    },
    {
     "t": "・わたしは{犬|いぬ}や{猫|ねこ}[[はもちろん]]{虫|むし}や{魚|さかな}も{好|す}きです。{動物|どうぶつ}は{何|なに}でも{好|す}きです。",
     "explain": "Review: はもちろん = of course ～, and also."
    }
   ],
   "explain": "6課 = 'not only ～ but also'. Five look-alikes: に限らず (wider range), のみならず (formal), ばかりか (surprise), はもとより (obvious first), 上に (same evaluation piles up)."
  },
  {
   "type": "grammar",
   "no": "1",
   "id": "d4b-g1",
   "teach": {
    "intro": [
     "に限らず = 'not only ～ (but a wider group too)'. 限(かぎ)る = limit → 限らず = without limiting to ～.",
     "Pinnaadi wide-range words varum: も, みんな, さまざまな, いつも. Tamil feel: 'Holiday mattum illa, varusham muzhuvadhum koottam.'",
     "Day 3-la 'に限り' (only ～) paathom — idhu adhoda opposite feel!"
    ],
    "pattern": "［名詞］＋に限らず、～も／みんな／さまざまな…",
    "examples": [
     {
      "jp": "この{店|みせ}は{週末|しゅうまつ}に{限|かぎ}らず、{平日|へいじつ}も{込|こ}んでいる。",
      "th": "Indha kadai weekend mattum illa, weekdays-um koottam.",
      "kana": "このみせはしゅうまつにかぎらず、へいじつもこんでいる。"
     },
     {
      "jp": "{子供|こども}に{限|かぎ}らず、{大人|おとな}もこのゲームに{夢中|むちゅう}だ。",
      "th": "Kids mattum illa, periyavangalum indha game-la moozhgi irukkaanga.",
      "kana": "こどもにかぎらず、おとなもこのゲームにむちゅうだ。"
     },
     {
      "jp": "{日本|にほん}{料理|りょうり}に{限|かぎ}らず、アジアの{料理|りょうり}はみんな{好|す}きです。",
      "th": "Japanese food mattum illa, Asian food ellaame pidikkum.",
      "kana": "にほんりょうりにかぎらず、アジアのりょうりはみんなすきです。"
     },
     {
      "jp": "{東京|とうきょう}に{限|かぎ}らず、{大|おお}きな{町|まち}は{家賃|やちん}が{高|たか}い。",
      "th": "Tokyo mattum illa, periya town ellaathilum rent adhigam.",
      "kana": "とうきょうにかぎらず、おおきなまちはやちんがたかい。"
     }
    ],
    "wrong": [
     {
      "ng": "この{店|みせ}は{日曜日|にちようび}に{限|かぎ}らず、{休|やす}みだ。",
      "ok": "この{店|みせ}は{日曜日|にちようび}に{限|かぎ}らず、{祝日|しゅくじつ}も{休|やす}みだ。",
      "th": "に限らず-ku pinnaadi 'also others' (祝日も) venum. Just 休みだ podhaadhu."
     }
    ],
    "check": [
     {
      "q": "（　　）に{限|かぎ}らず、どの{季節|きせつ}もこの{山|やま}は{美|うつく}しい。",
      "opts": [
       "{秋|あき}",
       "{四季|しき}",
       "どこ"
      ],
      "ans": 0,
      "explain": "One example (秋) + に限らず → wider (どの季節も).",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～に{限|かぎ}らず",
   "meaning": "{範囲|はんい}は～だけでなく、さらに{広|ひろ}い{範囲|はんい}のものも{含|ふく}む。",
   "explain": [
    "に限らず = the range is not only ～, it includes a wider range too.",
    "Shape: Noun + に限らず.",
    "Kavanam: after it, a sentence with も (= also others) or wide-range words (みんな・さまざまな・いつも)."
   ],
   "examples": [
    {
     "t": "①この{記念|きねん}{館|かん}は、{休日|きゅうじつ}[[に{限|かぎ}らず]]{一年中|いちねんじゅう}{入館|にゅうかん}{者|しゃ}が{多|おお}い。",
     "explain": "記念館(きねんかん) = memorial hall. 入館者(にゅうかんしゃ) = visitors. Holiday mattum illa, year muzhuvadhum koottam."
    },
    {
     "t": "②うち[[に{限|かぎ}らず]]{近所|きんじょ}の{住民|じゅうみん}はみんな{夜中|よなか}のバイクの{音|おと}に{悩|なや}まされている。",
     "explain": "住民(じゅうみん) = residents. 夜中(よなか) = midnight. 悩(なや)まされる = be troubled. Enga veedu mattum illa, ellaarum."
    },
    {
     "t": "③{近年|きんねん}、{地方|ちほう}の{町|まち}[[に{限|かぎ}らず]]{大|だい}{都会|とかい}でも{書店|しょてん}の{閉店|へいてん}が{相次|あいつ}いでいる。",
     "explain": "地方(ちほう) = provinces. 閉店(へいてん) = shop closing. 相次(あいつ)ぐ = happen one after another."
    }
   ],
   "form": "［名］　＋に{限|かぎ}らず",
   "caution": "{後|あと}には、「ほかにも」という{意味|いみ}を{表|あらわ}す「も」や、さらに{広|ひろ}い{範囲|はんい}を{表|あらわ}す{言葉|ことば}（みんな・さまざまな・いつもなど）を{使|つか}った{文|ぶん}が{来|く}る。"
  },
  {
   "type": "grammar",
   "no": "2",
   "id": "d4b-g2",
   "teach": {
    "intro": [
     "のみならず = formal 'だけでなく'. のみ = だけ (written style).",
     "Unlike に限らず, it can add something at the **same level**, not only a wider range. Sentences, verbs, adjectives kooda munnaadi varalaam.",
     "Pinnaadi often も: 'electricity bill mattum illa, gas bill-um water bill-um koodudhu.'"
    ],
    "pattern": "［名詞］・［普通形］（な形-である・名-である）＋のみならず、～も",
    "examples": [
     {
      "jp": "{彼|かれ}は{英語|えいご}のみならず、{中国|ちゅうごく}{語|ご}も{話|はな}せる。",
      "th": "Avar English mattum illa, Chinese-um pesuvaar.",
      "kana": "かれはえいごのみならず、ちゅうごくごもはなせる。"
     },
     {
      "jp": "この{問題|もんだい}は{日本|にほん}のみならず、{世界|せかい}{全体|ぜんたい}の{問題|もんだい}だ。",
      "th": "Idhu Japan problem mattum illa, ulaga problem.",
      "kana": "このもんだいはにほんのみならず、せかいぜんたいのもんだいだ。"
     },
     {
      "jp": "{彼女|かのじょ}は{歌|うた}が{上手|じょうず}であるのみならず、{作曲|さっきょく}もする。",
      "th": "Ava nalla paaduvaa, adhu mattum illa song-um compose pannuvaa. (な形 + である)",
      "kana": "かのじょはうたがじょうずであるのみならず、さっきょくもする。"
     },
     {
      "jp": "{値段|ねだん}が{高|たか}いのみならず、{品質|ひんしつ}も{悪|わる}い。",
      "th": "Vilai adhigam mattum illa, quality-um mosam.",
      "kana": "ねだんがたかいのみならず、ひんしつもわるい。"
     }
    ],
    "wrong": [
     {
      "ng": "このカメラは{便利|べんり}なのみならず、{軽|かる}い。",
      "ok": "このカメラは{便利|べんり}であるのみならず、{軽|かる}くもある。",
      "th": "な形 + である + のみならず. 'な' direct-aa podaadheenga. Pinnaadi も better."
     }
    ],
    "check": [
     {
      "q": "あの{選手|せんしゅ}は{足|あし}が（　　）のみならず、{頭|あたま}もいい。",
      "opts": [
       "{速|はや}い",
       "{速|はや}いだ",
       "{速|はや}くて"
      ],
      "ans": 0,
      "explain": "い形 plain form + のみならず → 速いのみならず.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～のみならず",
   "meaning": "～だけでなく、ほかにもある。",
   "explain": [
    "のみならず = not only ～, there is more. 硬い言い方.",
    "Shape: Noun / plain form (な形-である・名-である) + のみならず.",
    "Kavanam: unlike に限らず, also used when other things are at the same level. After it, usually a sentence with も."
   ],
   "examples": [
    {
     "t": "①{電気|でんき}{代|だい}[[のみならず]]、ガス{代|だい}や{水道|すいどう}{代|だい}も{値上|ねあ}がりするようだ。",
     "explain": "電気代(でんきだい) = electricity bill. 水道代(すいどうだい) = water bill. 値上(ねあ)がり = price rise."
    },
    {
     "t": "②{与党|よとう}[[のみならず]]、{野党|やとう}も{党首|とうしゅ}の{選出|せんしゅつ}には{慎重|しんちょう}だ。",
     "explain": "与党(よとう) = ruling party. 野党(やとう) = opposition. 党首(とうしゅ) = party leader. 選出(せんしゅつ) = election. 慎重(しんちょう) = careful."
    },
    {
     "t": "③{石井|いしい}さんは、{差別|さべつ}{的|てき}な{発言|はつげん}をした[[のみならず]]、それについて{謝|あやま}ることもなかった。",
     "explain": "差別的(さべつてき) = discriminatory. 発言(はつげん) = remark. 謝(あやま)る = apologise. Verb plain past + のみならず."
    }
   ],
   "form": "［名］・{普通|ふつう}{形|かたち}（［な形］だ－である・［名］だ－である）　＋のみならず",
   "caution": "「～に{限|かぎ}らず」と{違|ちが}って、{同|おな}じレベルのほかのものも{同様|どうよう}だという{場合|ばあい}にも{使|つか}える。{後|あと}には、「ほかにも」という{意味|いみ}を{表|あらわ}す「も」を{使|つか}った{文|ぶん}が{来|く}ることが{多|おお}い。",
   "tag": "硬い言い方"
  },
  {
   "type": "grammar",
   "no": "3",
   "id": "d4b-g3",
   "teach": {
    "intro": [
     "ばかりか = 'not only ～ but even ～' — surprise feel! First part already 'adhu podhum', second part innum unexpected.",
     "Pinnaadi も/まで/さえ varum. Example: 'Friends mattum illa, sondha appa-amma kooda avan engey irukkaan-nu theriyaadhu!'",
     "Pinnaadi request/invitation (しよう, してください) varaadhu."
    ],
    "pattern": "［名詞］・［普通形］（な形-な/-である・名-である）＋ばかりか、～も",
    "examples": [
     {
      "jp": "{彼|かれ}は{宿題|しゅくだい}を{忘|わす}れたばかりか、{教科書|きょうかしょ}も{持|も}ってこなかった。",
      "th": "Homework maranthaan, adhu mattum illa, textbook kooda kondu varala.",
      "kana": "かれはしゅくだいをわすれたばかりか、きょうかしょももってこなかった。"
     },
     {
      "jp": "この{薬|くすり}は{効|き}かないばかりか、{副作用|ふくさよう}もある。",
      "th": "Indha marundhu velai seyyala, adhu mattum illa, side effect vera.",
      "kana": "このくすりはきかないばかりか、ふくさようもある。"
     },
     {
      "jp": "{子供|こども}ばかりか、{大人|おとな}までこの{番組|ばんぐみ}を{見|み}ている。",
      "th": "Kids mattum illa, periyavanga kooda indha show paakkuraanga.",
      "kana": "こどもばかりか、おとなまでこのばんぐみをみている。"
     },
     {
      "jp": "あの{店|みせ}は{安|やす}いばかりか、{味|あじ}もいい。",
      "th": "Andha kadai cheap mattum illa, taste-um super. (plus + plus)",
      "kana": "あのみせはやすいばかりか、あじもいい。"
     }
    ],
    "wrong": [
     {
      "ng": "{雨|あめ}が{降|ふ}っているばかりか、{傘|かさ}を{持|も}っていこう。",
      "ok": "{雨|あめ}が{降|ふ}っているばかりか、{風|かぜ}も{強|つよ}くなってきた。",
      "th": "ばかりか-ku pinnaadi volition/request (持っていこう) varaadhu. Another fact (風も強い) venum."
     }
    ],
    "check": [
     {
      "q": "この{道|みち}は{狭|せま}い（　　）、{車|くるま}も{多|おお}くて{危|あぶ}ない。",
      "opts": [
       "ばかりか",
       "ばかりで",
       "ばかりに"
      ],
      "ans": 0,
      "explain": "Narrow + also many cars → ばかりか.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～ばかりか",
   "meaning": "～だけでも{十分|じゅうぶん}なのに、さらにほかのことも{加|くわ}わる。",
   "explain": [
    "ばかりか = ～ alone would be enough, but something more is added.",
    "Shape: Noun / plain form (な形-な/-である・名-である) + ばかりか.",
    "Kavanam: the first part says something unusual; the second part adds something even more surprising, often with も. No requests or invitations after it."
   ],
   "examples": [
    {
     "t": "①{発見|はっけん}が{遅|おく}れた[[ばかりか]]{対策|たいさく}にも{手間取|てまど}ったので、{牛|うし}の{病気|びょうき}が{広|ひろ}がってしまった。",
     "explain": "発見(はっけん) = discovery. 対策(たいさく) = countermeasure. 手間取(てまど)る = take time. Late-aa kandupudichaanga, plus action-um late."
    },
    {
     "t": "②{田島|たじま}{先生|せんせい}の{説明|せつめい}は、{子供|こども}にもわかりやすい[[ばかりか]]、{非常|ひじょう}におもしろくてためになる。",
     "explain": "ためになる = useful. Plus + plus example."
    },
    {
     "t": "③Aコースの{山道|やまみち}は、{初心者|しょしんしゃ}には{危険|きけん}な[[ばかりか]]、{途中|とちゅう}の{景色|けしき}もあまり{良|よ}くない。",
     "explain": "初心者(しょしんしゃ) = beginner. 途中(とちゅう) = on the way. 景色(けしき) = scenery. Minus + minus."
    },
    {
     "t": "④{友達|ともだち}[[ばかりか]]{親|おや}{兄弟|きょうだい}も{彼|かれ}の{居場所|いばしょ}を{知|し}らない。",
     "explain": "親兄弟(おやきょうだい) = parents and siblings. 居場所(いばしょ) = whereabouts."
    }
   ],
   "form": "［名］・{普通|ふつう}{形|かたち}（［な形］だ－な／－である・［名］だ－である）　＋ばかりか",
   "caution": "{前|まえ}の{文|ぶん}で{普通|ふつう}ではないことを{言|い}い、さらに{後|あと}の{文|ぶん}でも{意外|いがい}{性|せい}を{感|かん}じさせるほかのことを{加|くわ}える。{後|あと}の{文|ぶん}では「ほかにも」という{意味|いみ}を{表|あらわ}す「も」を{使|つか}うことが{多|おお}い。また、{働|はたら}きかけの{文|ぶん}は{来|こ}ない。"
  },
  {
   "type": "grammar",
   "no": "4",
   "id": "d4b-g4",
   "teach": {
    "intro": [
     "はもとより = formal 'はもちろん' (of course ～, and also ～).",
     "First item = obvious one (当然). Second item = additional one, usually with も.",
     "Tamil feel: 'Smoker-ku dhaan kedudhal — adhu sollave venaam — pakkathula irukkiravangalukkum kedudhal.'"
    ],
    "pattern": "［名詞］（＋助詞）＋はもとより、～も",
    "examples": [
     {
      "jp": "この{歌|うた}は{子供|こども}はもとより、{大人|おとな}にも{人気|にんき}がある。",
      "th": "Kids-ku popular — adhu sollave venaam — periyavangalukkum.",
      "kana": "このうたはこどもはもとより、おとなにもにんきがある。"
     },
     {
      "jp": "{彼|かれ}は{英語|えいご}はもとより、フランス{語|ご}もできる。",
      "th": "English obviously, French-um theriyum.",
      "kana": "かれはえいごはもとより、フランスごもできる。"
     },
     {
      "jp": "{平日|へいじつ}はもとより、{週末|しゅうまつ}も{働|はたら}いている。",
      "th": "Weekdays obviously, weekend-um velai.",
      "kana": "へいじつはもとより、しゅうまつもはたらいている。"
     },
     {
      "jp": "{東京|とうきょう}ではもとより、{地方|ちほう}でもこの{商品|しょうひん}は{売|う}れている。",
      "th": "Noun + 助詞 (で) + はもとより → Tokyo-la obviously, provinces-layum.",
      "kana": "とうきょうではもとより、ちほうでもこのしょうひんはうれている。"
     }
    ],
    "wrong": [
     {
      "ng": "この{料理|りょうり}は{大人|おとな}はもとより、おいしい。",
      "ok": "この{料理|りょうり}は{大人|おとな}はもとより、{子供|こども}にも{人気|にんき}がある。",
      "th": "Pinnaadi 'another example + も' venum."
     }
    ],
    "check": [
     {
      "q": "{彼女|かのじょ}は（　　）はもとより、ダンスも{上手|じょうず}だ。",
      "opts": [
       "{歌|うた}",
       "ダンス",
       "{全部|ぜんぶ}"
      ],
      "ans": 0,
      "explain": "Obvious example = 歌 (she is a singer) → 歌はもとより、ダンスも.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～はもとより",
   "meaning": "～はもちろん、ほかもそうだ。",
   "explain": [
    "はもとより = ～ of course, and others too. 硬い言い方.",
    "Shape: Noun (+ particle) + はもとより.",
    "Kavanam: attached to an example the speaker thinks is obvious; then another example is added, usually with も."
   ],
   "examples": [
    {
     "t": "①たばこは{本人|ほんにん}[[はもとより]]、{周|まわ}りの{人|ひと}にも{害|がい}を{及|およ}ぼす。",
     "explain": "害(がい)を及(およ)ぼす = cause harm."
    },
    {
     "t": "②{家族|かぞく}で{外国|がいこく}に{滞在|たいざい}している{人|ひと}は、{自分|じぶん}の{健康|けんこう}{管理|かんり}[[はもとより]]{家族|かぞく}の{心身|しんしん}の{健康|けんこう}にも{気|き}を{配|くば}ったほうがいい。",
     "explain": "滞在(たいざい) = stay. 心身(しんしん) = mind and body. 気を配(くば)る = pay attention."
    },
    {
     "t": "③{地元|じもと}の{住民|じゅうみん}[[はもとより]]、{周辺|しゅうへん}の{地域|ちいき}に{住|す}む{人|ひと}たちも{原子力|げんしりょく}{発電|はつでん}{所|しょ}に{不安|ふあん}を{感|かん}じている。",
     "explain": "地元(じもと) = local. 周辺(しゅうへん) = surrounding. 原子力発電所(げんしりょくはつでんしょ) = nuclear power plant."
    },
    {
     "t": "④この{学校|がっこう}では、{教室|きょうしつ}{内|ない}で[[はもとより]]{教室|きょうしつ}の{外|そと}でも{禁煙|きんえん}を{守|まも}ってください。",
     "explain": "教室内(きょうしつない)で + はもとより (with particle で). 禁煙(きんえん) = no smoking."
    }
   ],
   "form": "［名］（＋{助詞|じょし}）　＋はもとより",
   "caution": "{話者|わしゃ}が{当然|とうぜん}だと{思|おも}っている{例|れい}を{示|しめ}す{言葉|ことば}につく。{後|あと}には、そのほかの{例|れい}を{加|くわ}える。「ほかにも」という{意味|いみ}を{表|あらわ}す「も」を{使|つか}った{文|ぶん}が{来|く}ることが{多|おお}い。",
   "tag": "硬い言い方"
  },
  {
   "type": "grammar",
   "no": "5",
   "id": "d4b-g5",
   "teach": {
    "intro": [
     "上(うえ)に = 'on top of ～, also ～'. Same direction: good + good, or bad + bad.",
     "3課-la 上で (after ～) paathom — idhu vera meaning!",
     "Pinnaadi request/command varaadhu. Tamil feel: 'Help pannaanga, adhukku mela dinner-um vaangi koduthaanga.'"
    ],
    "pattern": "［普通形］（な形-な/-である・名-の/-である）＋上(に)",
    "examples": [
     {
      "jp": "この{部屋|へや}は{広|ひろ}い{上|うえ}に、{駅|えき}にも{近|ちか}い。",
      "th": "Room periya-dhu, adhukku mela station pakkam. (good + good)",
      "kana": "このへやはひろいうえに、えきにもちかい。"
     },
     {
      "jp": "{昨日|きのう}は{雨|あめ}が{降|ふ}った{上|うえ}に、{風|かぜ}も{強|つよ}かった。",
      "th": "Mazhai, adhukku mela kaathu-um adhigam. (bad + bad)",
      "kana": "きのうはあめがふったうえに、かぜもつよかった。"
     },
     {
      "jp": "{彼女|かのじょ}は{美人|びじん}な{上|うえ}に、{性格|せいかく}もいい。",
      "th": "Ava azhagu, adhukku mela nalla gunam. (な形 + な + 上に)",
      "kana": "かのじょはびじんなうえに、せいかくもいい。"
     },
     {
      "jp": "{今日|きょう}は{休日|きゅうじつ}の{上|うえ}、{天気|てんき}もいい。",
      "th": "Inniki leave, plus weather-um super. (名 + の + 上)",
      "kana": "きょうはきゅうじつのうえ、てんきもいい。"
     }
    ],
    "wrong": [
     {
      "ng": "この{店|みせ}は{安|やす}い{上|うえ}に、まずい。",
      "ok": "この{店|みせ}は{安|やす}い{上|うえ}に、おいしい。",
      "th": "上に connects same evaluation: cheap (good) + tasty (good). Good + bad mix pannaadheenga."
     }
    ],
    "check": [
     {
      "q": "このかばんは{丈夫|じょうぶ}な{上|うえ}に、（　　）。",
      "opts": [
       "{軽|かる}い",
       "{重|おも}い",
       "{高|たか}すぎる"
      ],
      "ans": 0,
      "explain": "Plus + plus → 丈夫な上に軽い.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～{上|うえ}(に)",
   "meaning": "～だけでなく、さらにいいこと・{悪|わる}いことが{重|かさ}なる。",
   "explain": [
    "上(に) = not only ～, and in addition more good (or bad) things pile up.",
    "Shape: plain form (な形-な/-である・名-の/-である) + 上(に).",
    "Kavanam: words of the same evaluation come before and after (plus & plus / minus & minus). Opposite or unrelated things don't come. No requests after it."
   ],
   "examples": [
    {
     "t": "①{田中|たなか}さんには{仕事|しごと}を{手伝|てつだ}ってもらった[[{上|うえ}に]]、{仕事|しごと}の{後|あと}、ごちそうになった。",
     "explain": "ごちそうになる = be treated to a meal."
    },
    {
     "t": "②{森田|もりた}{先生|せんせい}は、{毎日|まいにち}{医師|いし}として{忙|いそが}しく{仕事|しごと}をしている[[{上|うえ}]]、{週末|しゅうまつ}も{学会|がっかい}や{講演|こうえん}で{飛|と}び{回|まわ}っている。",
     "explain": "医師(いし) = doctor. 学会(がっかい) = academic conference. 講演(こうえん) = lecture. 飛(と)び回(まわ)る = rush around."
    },
    {
     "t": "③このテキストは{用語|ようご}が{難|むずか}しい[[{上|うえ}に]]、{内容|ないよう}も{良|よ}くない。",
     "explain": "用語(ようご) = terminology. Minus + minus."
    },
    {
     "t": "④ここは{空気|くうき}がきれいな[[{上|うえ}]]、{近|ちか}くに{明|あか}るいところがないので{星|ほし}がよく{見|み}える。",
     "explain": "な形 + な + 上. Plus + plus."
    },
    {
     "t": "⑤{今日|きょう}は{寝不足|ねぶそく}の[[{上|うえ}]]、{少|すこ}し{熱|ねつ}がある。{早|はや}く{帰|かえ}りたい。",
     "explain": "寝不足(ねぶそく) = lack of sleep. 名 + の + 上."
    }
   ],
   "form": "{普通|ふつう}{形|かたち}（［な形］だ－な／－である・［名］だ－の／－である）　＋{上|うえ}（に）",
   "caution": "{前後|ぜんご}には{同|おな}じ{評価|ひょうか}の{言葉|ことば}（プラスのこととプラスのこと・マイナスのこととマイナスのこと）が{来|く}る。{反対|はんたい}のことや{関係|かんけい}ないことは{来|こ}ない。{後|あと}には、{働|はたら}きかけの{文|ぶん}は{来|こ}ない。"
  },
  {
   "type": "group",
   "title": "【1】（～に{限|かぎ}らず）",
   "children": [
    {
     "type": "mcq",
     "id": "d4b-6-1-1",
     "q": "1　（　　）に{限|かぎ}らずこの{県|けん}{全体|ぜんたい}に{高層|こうそう}ビルが{増|ふ}えている。",
     "opts": [
      "わたしの{町|まち}",
      "{東京|とうきょう}",
      "{全国|ぜんこく}"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Small range (my town) → wider range (the whole prefecture). 東京 isn't in 'this prefecture' necessarily; 全国 is bigger than the prefecture."
    },
    {
     "type": "mcq",
     "id": "d4b-6-1-2",
     "q": "2　{日本|にほん}のアニメは、（　　）に{限|かぎ}らず{今|いま}や{世界中|せかいじゅう}で{評価|ひょうか}されている。",
     "opts": [
      "{人気|にんき}{作家|さっか}の{作品|さくひん}",
      "アニメ{好|す}きな{若者|わかもの}",
      "{日本|にほん}{国内|こくない}"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "日本国内 → 世界中 (wider place)."
    },
    {
     "type": "mcq",
     "id": "d4b-6-1-3",
     "q": "3　りんごに{限|かぎ}らず（　　）{新鮮|しんせん}さが{大切|たいせつ}だ。",
     "opts": [
      "みかんも",
      "{魚|さかな}も",
      "{果物|くだもの}はみんな"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Apple → all fruit (みんな = wider group including apples)."
    },
    {
     "type": "mcq",
     "id": "d4b-6-1-4",
     "q": "4　{田中|たなか}さんに{限|かぎ}らず（　　）{昼休|ひるやす}みに{勉強|べんきょう}している。",
     "opts": [
      "わたしは",
      "ほかの{人|ひと}たちも",
      "{山中|やまなか}さんが"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Not only Tanaka → others too (も)."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【2】（～のみならず）",
   "children": [
    {
     "type": "mcq",
     "id": "d4b-6-2-1",
     "q": "1　{今年|ことし}の{6月|ろくがつ}は、{気温|きおん}が（　　）のみならず、{大雨|おおあめ}の{日|ひ}も{多|おお}いようだ。",
     "opts": [
      "{不安定|ふあんてい}",
      "{不安定|ふあんてい}だ",
      "{不安定|ふあんてい}である"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "な形 + である + のみならず."
    },
    {
     "type": "mcq",
     "id": "d4b-6-2-2",
     "q": "2　{環境|かんきょう}{問題|もんだい}は、（　　）のみならず、{地球|ちきゅう}{全体|ぜんたい}の{問題|もんだい}である。",
     "opts": [
      "わが{国|くに}",
      "わたし",
      "{人間|にんげん}"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "One country → the whole earth."
    },
    {
     "type": "mcq",
     "id": "d4b-6-2-3",
     "q": "3　この{小説|しょうせつ}は、{賞|しょう}を{受賞|じゅしょう}したのみならず、（　　）。",
     "opts": [
      "{大変|たいへん}{評価|ひょうか}された",
      "{映画|えいが}{化|か}もされた",
      "よく{売|う}れるだろう"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Additional fact with も → 映画化もされた."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【3】（～ばかりか）",
   "children": [
    {
     "type": "mcq",
     "id": "d4b-6-3-1",
     "q": "1　この{道具|どうぐ}は、{使|つか}い{方|かた}が（　　）ばかりか、{壊|こわ}れやすい。",
     "opts": [
      "{複雑|ふくざつ}",
      "{複雑|ふくざつ}な",
      "{複雑|ふくざつ}で"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "な形 + な + ばかりか."
    },
    {
     "type": "mcq",
     "id": "d4b-6-3-2",
     "q": "2　{今年|ことし}の{夏|なつ}の{暑|あつ}さはひどかった。（　　）、{暑|あつ}さが{原因|げんいん}で{病気|びょうき}になる{人|ひと}が{続出|ぞくしゅつ}した。",
     "opts": [
      "わたしばかりか{友人|ゆうじん}も",
      "{男性|だんせい}ばかりか{女性|じょせい}でも",
      "{高齢|こうれい}{者|しゃ}ばかりか{若者|わかもの}でも"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Elderly getting sick is expected; even young people → surprise. ばかりか needs that 'even' feel."
    },
    {
     "type": "mcq",
     "id": "d4b-6-3-3",
     "q": "3　{昨日|きのう}{就職|しゅうしょく}{説明|せつめい}{会|かい}があったが、{遅刻|ちこく}{者|しゃ}が{多|おお}かったばかりか、（　　）。",
     "opts": [
      "{私語|しご}も{多|おお}かった",
      "{真剣|しんけん}な{質問|しつもん}も{多|おお}かった",
      "{欠席|けっせき}{者|しゃ}は{少|すく}なかった"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Minus + minus → 私語(しご, chatting)も多かった."
    },
    {
     "type": "mcq",
     "id": "d4b-6-3-4",
     "q": "4　この{薬|くすり}を{飲|の}むようになってから、よく{眠|ねむ}れるようになったばかりか、（　　）。",
     "opts": [
      "{食欲|しょくよく}も{出|で}てきた",
      "のどが{渇|かわ}くようになった",
      "{集中|しゅうちゅう}{力|りょく}もなくなった"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Plus + plus → 食欲も出てきた."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【4】（～はもとより）",
   "children": [
    {
     "type": "mcq",
     "id": "d4b-6-4-1",
     "q": "1　（　　）{病気|びょうき}を{治|なお}すために{努力|どりょく}をしていかなければならない。",
     "opts": [
      "{医者|いしゃ}はもとより{患者|かんじゃ}も",
      "{病院|びょういん}はもとより{医者|いしゃ}も",
      "{家族|かぞく}はもとより{患者|かんじゃ}も"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Obvious one first: doctors (of course) → patients too."
    },
    {
     "type": "mcq",
     "id": "d4b-6-4-2",
     "q": "2　{息子|むすこ}がやっと{大学|だいがく}に{合格|ごうかく}しました。（　　）{喜|よろこ}んでいます。",
     "opts": [
      "{家族|かぞく}はもとより{本人|ほんにん}も",
      "{本人|ほんにん}はもとより{家族|かぞく}も",
      "わたしはもとより{本人|ほんにん}も"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "The son himself is obviously happy → the family too."
    },
    {
     "type": "mcq",
     "id": "d4b-6-4-3",
     "q": "3　{敬語|けいご}の{使|つか}い{方|かた}は、（　　）{難|むずか}しいようだ。",
     "opts": [
      "{社会|しゃかい}{人|じん}はもとより{学生|がくせい}にも",
      "{外国|がいこく}{人|じん}はもとより{日本人|にほんじん}にも",
      "{大人|おとな}はもとより10{代|だい}の{人|ひと}たちにも"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Obviously hard for foreigners → even for Japanese."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【5】（～{上|うえ}(に)）",
   "children": [
    {
     "type": "mcq",
     "id": "d4b-6-5-1",
     "q": "1　{彼|かれ}は{明|あか}るい{上|うえ}に、（　　）。",
     "opts": [
      "まじめな{性格|せいかく}だ",
      "{漫画|まんが}が{好|す}きだ",
      "{趣味|しゅみ}がない"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Plus + plus → まじめな性格."
    },
    {
     "type": "mcq",
     "id": "d4b-6-5-2",
     "q": "2　{彼|かれ}には30{分|ふん}も{待|ま}たされた{上|うえ}、{夕食|ゆうしょく}を（　　）。",
     "opts": [
      "ごちそうした",
      "ごちそうしてもらった",
      "ごちそうさせられた"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Minus + minus: made to wait, AND made to pay for dinner (させられた)."
    },
    {
     "type": "mcq",
     "id": "d4b-6-5-3",
     "q": "3　{山中|やまなか}さんにはプレゼントをいただいた{上|うえ}に、（　　）。",
     "opts": [
      "{家|いえ}まで{送|おく}っていただいた",
      "プレゼントは{高価|こうか}なものだった",
      "いつも{優|やさ}しくしてくれる"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Two kind acts at that time → 家まで送っていただいた."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【1～5】まとめ",
   "children": [
    {
     "type": "mcq",
     "id": "d4b-6-6-1",
     "q": "1　ビタミンB（　　）、ビタミンEも{体|からだ}に{必要|ひつよう}な{栄養素|えいようそ}である。",
     "opts": [
      "の{上|うえ}に",
      "ばかりでなく",
      "ばかりか"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Neutral fact, same level → ばかりでなく. ばかりか needs surprise; の上に needs plain form (ビタミンBの上に = on top of)."
    },
    {
     "type": "mcq",
     "id": "d4b-6-6-2",
     "q": "2　{元気|げんき}なとき（　　）、つらいときもわたしは{散歩|さんぽ}に{出|で}かける。",
     "opts": [
      "はもちろん",
      "ばかりか",
      "に{限|かぎ}らず"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Obvious (when well) → はもちろん."
    },
    {
     "type": "mcq",
     "id": "d4b-6-6-3",
     "q": "3　{残業|ざんぎょう}（　　）{休日|きゅうじつ}{出勤|しゅっきん}もしたので、{今週|こんしゅう}はとても{疲|つか}れた。",
     "opts": [
      "はもとより",
      "に{限|かぎ}らず",
      "の{上|うえ}に"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Minus + minus piling up → 残業の上に."
    },
    {
     "type": "mcq",
     "id": "d4b-6-6-4",
     "q": "4　{彼|かれ}はかっこいい（　　）、ギターも{歌|うた}も{上手|じょうず}だ。",
     "opts": [
      "に{限|かぎ}らず",
      "はもとより",
      "ばかりか"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "い形 plain + ばかりか. (はもとより/に限らず take nouns.)"
    },
    {
     "type": "mcq",
     "id": "d4b-6-6-5",
     "q": "5　{留学|りゅうがく}{中|ちゅう}は{日本|にほん}の{言語|げんご}や{文化|ぶんか}を{学|まな}ぶ（　　）、{自分|じぶん}の{国|くに}のことも{伝|つた}えていこうと{考|かんが}えている。",
     "opts": [
      "{上|うえ}",
      "のみならず",
      "ばかりか"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Volition (伝えていこう) after → のみならず. ばかりか/上 can't take volition."
    },
    {
     "type": "mcq",
     "id": "d4b-6-6-6",
     "q": "6　{禁煙|きんえん}するには、{本人|ほんにん}の{意志|いし}（　　）、{一緒|いっしょ}に{暮|く}らす{家族|かぞく}の{協力|きょうりょく}が{欠|か}かせない。",
     "opts": [
      "はもとより",
      "に{限|かぎ}らず",
      "の{上|うえ}"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Of course one's own will → はもとより."
    }
   ],
   "scored": true
  },
  {
   "type": "items",
   "title": "7{課|か}　〔{復習|ふくしゅう}〕",
   "items": [
    {
     "t": "・{母|はは}に{佐藤|さとう}さん[[のことを]]{話|はな}した。",
     "explain": "Review: ～のことを = about ～."
    },
    {
     "t": "・わたしは{今|いま}、{紅茶|こうちゃ}の{歴史|れきし}[[について]]{調|しら}べています。",
     "explain": "Review: について = about. 紅茶(こうちゃ) = black tea."
    },
    {
     "t": "・{犬|いぬ}[[に]]{文句|もんく}を{言|い}ってもしょうがない。",
     "explain": "Review: に = to (the target). 文句(もんく) = complaint."
    }
   ],
   "explain": "7課 = 'about ～ / toward ～'. に関して (formal about), をめぐって (argument over), にかけては (best at), に対して (toward / in contrast), にこたえて (in response to hopes)."
  },
  {
   "type": "grammar",
   "no": "1",
   "id": "d4b-g6",
   "teach": {
    "intro": [
     "に関して = formal 'について' (about ～). Investigation, explanation, survey-la romba varum.",
     "Pinnaadi: 調べる, 説明する, 質問する, アンケート — information verbs.",
     "Big theme words munnaadi (事件, 問題, 生活). 'How old are you' maadhiri quick-answer vishayam illa."
    ],
    "pattern": "［名詞］＋に関して　／　＋に関する＋［名詞］",
    "examples": [
     {
      "jp": "この{件|けん}に{関|かん}して、{何|なに}か{質問|しつもん}はありますか。",
      "th": "Indha vishayam pathi edhavadhu kelvi irukka?",
      "kana": "このけんにかんして、なにかしつもんはありますか。"
     },
     {
      "jp": "{日本|にほん}の{歴史|れきし}に{関|かん}して、レポートを{書|か}いた。",
      "th": "Japan history pathi report ezhudhinen.",
      "kana": "にほんのれきしにかんして、レポートをかいた。"
     },
     {
      "jp": "{事故|じこ}の{原因|げんいん}に{関|かん}しては、{現在|げんざい}{調査|ちょうさ}{中|ちゅう}です。",
      "th": "Accident-oda kaaranam pathi ippo investigate panrom.",
      "kana": "じこのげんいんにかんしては、げんざいちょうさちゅうです。"
     },
     {
      "jp": "{環境|かんきょう}に{関|かん}する{本|ほん}をたくさん{読|よ}んだ。",
      "th": "Environment pathina books neraya padichen. (に関する + Noun)",
      "kana": "かんきょうにかんするほんをたくさんよんだ。"
     }
    ],
    "wrong": [
     {
      "ng": "{彼|かれ}の{年齢|ねんれい}に{関|かん}して{教|おし}えてください。",
      "ok": "{彼|かれ}の{年齢|ねんれい}を{教|おし}えてください。",
      "th": "に関して is for wide themes, not a one-word answer like age."
     }
    ],
    "check": [
     {
      "q": "（　　）に{関|かん}して{詳|くわ}しく{調|しら}べた。",
      "opts": [
       "{日本|にほん}の{食|しょく}{文化|ぶんか}",
       "{昨日|きのう}の{天気|てんき}",
       "{彼|かれ}の{名前|なまえ}"
      ],
      "ans": 0,
      "explain": "A big theme → 日本の食文化に関して.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～に{関|かん}して",
   "meaning": "～の{内容|ないよう}について、{詳|くわ}しい{情報|じょうほう}を{得|え}たり{発|はっ}したりする。",
   "explain": [
    "に関して = about the content of ～: get or give detailed information. 硬い言い方.",
    "Shape: Noun + に関して / Noun + に関する + Noun.",
    "Kavanam: after it, verbs for getting information (調べる・説明する). Unlike について, not for things with an instant clear answer (年齢・国籍); it takes words for a big theme."
   ],
   "examples": [
    {
     "t": "①{今回|こんかい}の{事件|じけん}[[に{関|かん}して]]{何|なに}か{詳|くわ}しいことがわかりましたか。",
     "explain": "事件(じけん) = incident."
    },
    {
     "t": "②ごみ{処理|しょり}の{問題|もんだい}[[に{関|かん}しましては]]、{環境|かんきょう}{課|か}の{課長|かちょう}がご{説明|せつめい}いたします。",
     "explain": "処理(しょり) = disposal. 環境課(かんきょうか) = environment section. に関しましては = super polite."
    },
    {
     "t": "③{警察|けいさつ}では、{犯行|はんこう}の{動機|どうき}[[に{関|かん}し]]、{詳|くわ}しい{調査|ちょうさ}を{開始|かいし}した。",
     "explain": "犯行(はんこう) = crime. 動機(どうき) = motive. 調査(ちょうさ) = investigation."
    },
    {
     "t": "④{高齢|こうれい}{者|しゃ}の{生活|せいかつ}[[に{関|かん}する]]アンケートにご{協力|きょうりょく}ください。",
     "explain": "高齢者(こうれいしゃ) = elderly. 協力(きょうりょく) = cooperation."
    }
   ],
   "form": "［名］　＋に{関|かん}して　／　［名］　＋に{関|かん}する＋［名］",
   "caution": "{後|あと}には{情報|じょうほう}を{得|え}ることを{表|あらわ}す{動詞|どうし}（{調|しら}べる・{説明|せつめい}するなど）の{文|ぶん}が{来|く}ることが{多|おお}い。「～について」と{違|ちが}って、{答|こた}えがはっきりすぐ{出|で}ること（{年齢|ねんれい}・{国籍|こくせき}など）ではなく、{周辺|しゅうへん}を{含|ふく}む{大|おお}きなテーマを{表|あらわ}す{言葉|ことば}につく。",
   "tag": "硬い言い方"
  },
  {
   "type": "grammar",
   "no": "2",
   "id": "d4b-g7",
   "teach": {
    "intro": [
     "をめぐって = 'over / surrounding ～' — argument, fight, rumour around a topic.",
     "Usually **many people** involved: 親族が争う, 国会が揺れる, うわさが広がる.",
     "Tamil feel: 'Appa vitta land-ukkaaga sondhakkaaranga sanda podraanga.'"
    ],
    "pattern": "［名詞］＋をめぐって　／　＋をめぐる＋［名詞］",
    "examples": [
     {
      "jp": "{遺産|いさん}をめぐって{兄弟|きょうだい}が{争|あらそ}っている。",
      "th": "Property-kaaga brothers sanda podraanga.",
      "kana": "いさんをめぐってきょうだいがあらそっている。"
     },
     {
      "jp": "{新|あたら}しい{空港|くうこう}の{建設|けんせつ}をめぐって、{住民|じゅうみん}の{意見|いけん}が{分|わ}かれた。",
      "th": "Pudhu airport kattradhu pathi residents opinion pirinjudhu.",
      "kana": "あたらしいくうこうのけんせつをめぐって、じゅうみんのいけんがわかれた。"
     },
     {
      "jp": "その{問題|もんだい}をめぐり、{会議|かいぎ}は3{時間|じかん}{続|つづ}いた。",
      "th": "Andha problem pathi meeting 3 mani neram nadandhudhu.",
      "kana": "そのもんだいをめぐり、かいぎは3じかんつづいた。"
     },
     {
      "jp": "{彼|かれ}をめぐるうわさが{広|ひろ}がっている。",
      "th": "Avana pathina rumour paraviduchu. (をめぐる + Noun)",
      "kana": "かれをめぐるうわさがひろがっている。"
     }
    ],
    "wrong": [
     {
      "ng": "わたしは{日本|にほん}の{歴史|れきし}をめぐって{本|ほん}を{読|よ}んだ。",
      "ok": "わたしは{日本|にほん}の{歴史|れきし}について{本|ほん}を{読|よ}んだ。",
      "th": "One person reading — no debate or conflict → について. をめぐって needs argument/conflict among people."
     }
    ],
    "check": [
     {
      "q": "ダムの{建設|けんせつ}をめぐって、（　　）。",
      "opts": [
       "{住民|じゅうみん}が{対立|たいりつ}している",
       "わたしは{賛成|さんせい}だ",
       "{雨|あめ}が{降|ふ}った"
      ],
      "ans": 0,
      "explain": "Conflict among many people → 住民が対立している.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～をめぐって",
   "meaning": "～について{議論|ぎろん}・{対立|たいりつ}{的|てき}{行為|こうい}・うわさなどをする。",
   "explain": [
    "をめぐって = discussion, conflict, rumours about ～. 硬い言い方.",
    "Shape: Noun + をめぐって / Noun + をめぐる + Noun.",
    "Kavanam: the actors are usually plural. After it, a verb showing several people involved."
   ],
   "examples": [
    {
     "t": "①{親|おや}が{残|のこ}した{土地|とち}[[をめぐって]]{親族|しんぞく}が{争|あらそ}っている。",
     "explain": "土地(とち) = land. 親族(しんぞく) = relatives. 争(あらそ)う = fight."
    },
    {
     "t": "②{消費|しょうひ}{税|ぜい}の{問題|もんだい}[[をめぐり]]、{国会|こっかい}は{大|おお}きく{揺|ゆ}れた。",
     "explain": "消費税(しょうひぜい) = consumption tax. 国会(こっかい) = the Diet. 揺(ゆ)れる = be shaken."
    },
    {
     "t": "③{彼女|かのじょ}の{行動|こうどう}[[をめぐる]]うわさはたちまち{社内|しゃない}に{広|ひろ}がった。",
     "explain": "行動(こうどう) = behaviour. 社内(しゃない) = within the company."
    }
   ],
   "form": "［名］　＋をめぐって　／　［名］　＋をめぐる＋［名］",
   "caution": "{動作主|どうさしゅ}は{複数|ふくすう}であることが{多|おお}い。{後|あと}には、{複数|ふくすう}の{人|ひと}がかかわることを{表|あらわ}す{動詞|どうし}の{文|ぶん}が{来|く}る。",
   "tag": "硬い言い方"
  },
  {
   "type": "grammar",
   "no": "3",
   "id": "d4b-g8",
   "teach": {
    "intro": [
     "にかけては = 'when it comes to ～ (skill), no one beats him'.",
     "Munnaadi: skill/ability words (演説, 料理, 足の速さ). Pinnaadi: 'number one' meaning (最高, だれにも負けない).",
     "Day 3 にかけて (time range) — idhu vera! にかけて**は** = skill."
    ],
    "pattern": "［名詞］＋にかけては、（だれよりも）～",
    "examples": [
     {
      "jp": "{計算|けいさん}の{速|はや}さにかけては、{彼|かれ}にかなう{人|ひと}はいない。",
      "th": "Calculation speed-la avana yaarum jeikka mudiyaadhu.",
      "kana": "けいさんのはやさにかけては、かれにかなうひとはいない。"
     },
     {
      "jp": "{料理|りょうり}にかけては、{母|はは}が{一番|いちばん}だ。",
      "th": "Samayal-na amma dhaan number one.",
      "kana": "りょうりにかけては、ははがいちばんだ。"
     },
     {
      "jp": "サッカーにかけては、クラスのだれにも{負|ま}けない。",
      "th": "Football-na class-la yaarukkum thoarkka maatten.",
      "kana": "サッカーにかけては、クラスのだれにもまけない。"
     },
     {
      "jp": "{歌|うた}のうまさにかけては、{彼女|かのじょ}はプロ{並|な}みだ。",
      "th": "Paadura thiramai-la ava professional level.",
      "kana": "うたのうまさにかけては、かのじょはプロなみだ。"
     }
    ],
    "wrong": [
     {
      "ng": "{料理|りょうり}にかけては、わたしは{下手|へた}だ。",
      "ok": "{料理|りょうり}にかけては、わたしはだれにも{負|ま}けない。",
      "th": "にかけては must lead to 'best / strong ability', not weakness."
     }
    ],
    "check": [
     {
      "q": "（　　）にかけては、{兄|あに}が{一番|いちばん}だ。",
      "opts": [
       "{泳|およ}ぎ",
       "{背|せ}の{高|たか}さ",
       "{年|とし}"
      ],
      "ans": 0,
      "explain": "A skill → 泳ぎにかけては. Height/age aren't skills.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～にかけては",
   "meaning": "～がだれよりも{上手|じょうず}だ。",
   "explain": [
    "にかけては = ～ is better than anyone.",
    "Shape: Noun + にかけては.",
    "Kavanam: attached to words for skill/ability. After it, a sentence meaning 'the most able'."
   ],
   "examples": [
    {
     "t": "①あの{政治|せいじ}{家|か}は{演説|えんぜつ}[[にかけては]]{最高|さいこう}のレベルだ。",
     "explain": "政治家(せいじか) = politician. 演説(えんぜつ) = speech."
    },
    {
     "t": "②わたしは{安|やす}い{材料|ざいりょう}でおいしい{料理|りょうり}を{作|つく}ること[[にかけては]]だれにも{負|ま}けませんよ。",
     "explain": "材料(ざいりょう) = ingredients."
    },
    {
     "t": "③ボール{運|はこ}びのうまさ[[にかけては]]{中井|なかい}{選手|せんしゅ}の{右|みぎ}に{出|で}るものはいない。",
     "explain": "右に出るものはいない = no one is better (idiom)."
    }
   ],
   "form": "［名］　＋にかけては",
   "caution": "{技術|ぎじゅつ}・{能力|のうりょく}などを{表|あらわ}す{言葉|ことば}につく。{後|あと}には、「{一番|いちばん}{能力|のうりょく}がある」という{意味|いみ}の{文|ぶん}が{来|く}る。"
  },
  {
   "type": "grammar",
   "no": "4",
   "id": "d4b-g9",
   "teach": {
    "intro": [
     "Two meanings! **A = towards / against ～**: action, attitude, feeling aimed at a person/group/plan (目上の人に対して失礼).",
     "**B = in contrast to ～**: 父は感情が激しいのに対して、母は冷静. Clear difference between two things.",
     "B shape: plain form + の + に対して. A shape: Noun + に対して / に対する + Noun."
    ],
    "pattern": "A：［名詞］＋に対して／に対する＋［名詞］　　B：［名詞］・［普通形］＋の＋に対して",
    "examples": [
     {
      "jp": "{先生|せんせい}に{対|たい}して{失礼|しつれい}なことを{言|い}ってはいけない。",
      "th": "A: Teacher kitta rude-aa pesa koodaadhu.",
      "kana": "せんせいにたいしてしつれいなことをいってはいけない。"
     },
     {
      "jp": "その{意見|いけん}に{対|たい}して、{反対|はんたい}する{人|ひと}が{多|おお}かった。",
      "th": "A: Andha opinion-ku ethiraa neraya per.",
      "kana": "そのいけんにたいして、はんたいするひとがおおかった。"
     },
     {
      "jp": "{客|きゃく}に{対|たい}するサービスが{悪|わる}い。",
      "th": "A: Customers-ku service mosam. (に対する + Noun)",
      "kana": "きゃくにたいするサービスがわるい。"
     },
     {
      "jp": "{兄|あに}は{背|せ}が{高|たか}いのに{対|たい}して、{弟|おとうと}は{低|ひく}い。",
      "th": "B: Anna uyaram, aanaa thambi kuttai — contrast.",
      "kana": "あにはせがたかいのにたいして、おとうとはひくい。"
     }
    ],
    "wrong": [
     {
      "ng": "{田中|たなか}さんに{対|たい}してプレゼントをあげた。",
      "ok": "{田中|たなか}さんにプレゼントをあげた。",
      "th": "Simple giving uses に. A に対して is for attitudes/actions directed at someone (失礼, 反対, 親切)."
     }
    ],
    "check": [
     {
      "q": "{東京|とうきょう}は{人|ひと}が{多|おお}い（　　）、この{村|むら}は{少|すく}ない。",
      "opts": [
       "のに{対|たい}して",
       "に{対|たい}して",
       "に{対|たい}する"
      ],
      "ans": 0,
      "explain": "B meaning with a clause → 多いのに対して.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～に{対|たい}して",
   "meaning": "A：～を{相手|あいて}にあることをする・～についてある{感情|かんじょう}を{持|も}つ。　B：～とははっきり{違|ちが}って、あることが{言|い}える。",
   "explain": [
    "A = do something toward ～ / have some feeling about ～. B = clearly different from ～, something can be said.",
    "Shape: A: Noun + に対して / に対する + Noun. B: Noun / plain form (な形-な/-である・名-な/-である) + の + に対して.",
    "Kavanam A: attached to people, groups, themes, problems; after it, a direct action, attitude or feeling toward that target. B: a clear difference comes before and after."
   ],
   "examples": [
    {
     "t": "①{目上|めうえ}の{人|ひと}[[に{対|たい}して]]そんな{乱暴|らんぼう}な{言|い}い{方|かた}をしてはいけません。",
     "explain": "A. 目上(めうえ) = superiors. 乱暴(らんぼう)な = rough."
    },
    {
     "t": "②{桜井|さくらい}{氏|し}の{発言|はつげん}は{県民|けんみん}[[に{対|たい}して]]{失礼|しつれい}だと{思|おも}う。",
     "explain": "A. 氏(し) = Mr. 県民(けんみん) = prefecture residents. 失礼(しつれい) = rude."
    },
    {
     "t": "③{政府|せいふ}の{案|あん}[[に{対|たい}して]]{住民|じゅうみん}は{大|だい}{反対|はんたい}した。",
     "explain": "A. 政府(せいふ) = government. 案(あん) = plan."
    },
    {
     "t": "④このアンケートから{会社|かいしゃ}[[に{対|たい}する]]{不満|ふまん}が{読|よ}み{取|と}れる。",
     "explain": "A. 不満(ふまん) = dissatisfaction. 読み取る = read (between lines)."
    },
    {
     "t": "⑤やる{気|き}がなかった{前|まえ}の{会長|かいちょう}[[に{対|たい}して]]、{新|あたら}しい{会長|かいちょう}は{素晴|すば}らしい{行動|こうどう}{力|りょく}がある。",
     "explain": "B. 会長(かいちょう) = chairman. 行動力(こうどうりょく) = drive to act."
    },
    {
     "t": "⑥うちでは、{父|ちち}は{感情|かんじょう}が{激|はげ}しいの[[に{対|たい}して]]、{母|はは}は{冷静|れいせい}で{穏|おだ}やかな{性格|せいかく}です。",
     "explain": "B. 激(はげ)しい = intense. 冷静(れいせい) = calm. 穏(おだ)やか = gentle."
    },
    {
     "t": "⑦{朝|あさ}はパンを{食|た}べると{答|こた}えた{人|ひと}が30%だったの[[に{対|たい}して]]、ご{飯|はん}を{食|た}べると{答|こた}えた{人|ひと}は65%だった。",
     "explain": "B. Survey numbers contrast."
    }
   ],
   "form": "A：［名］　＋に{対|たい}して　／　［名］　＋に{対|たい}する＋［名］　　B：［名］・{普通|ふつう}{形|かたち}（［な形］だ－な／－である・［名］だ－な／－である）＋の　＋に{対|たい}して",
   "caution": "A：{人|ひと}や{団体|だんたい}・テーマや{問題|もんだい}{点|てん}などを{表|あらわ}す{語|ご}につく。{後|あと}には、その{対象|たいしょう}への{直接的|ちょくせつてき}な{行為|こうい}・{態度|たいど}・{気持|きも}ちなどを{表|あらわ}す{文|ぶん}が{来|く}る。　B：{前後|ぜんご}には、はっきり{違|ちが}いがあることが{来|く}る。"
  },
  {
   "type": "grammar",
   "no": "5",
   "id": "d4b-g10",
   "teach": {
    "intro": [
     "にこたえて = 'in response to (someone's hopes/requests)'. 応(こた)える.",
     "Only limited words before it: 期待, 要望, 希望, アンコール, 声援, 要求.",
     "Tamil feel: 'Rasigargal-oda encore-ku response-aa thirumba stage-ku vandhaar.'"
    ],
    "pattern": "［名詞（期待・要望・希望・アンコール）］＋にこたえて　／　＋にこたえる＋［名詞］",
    "examples": [
     {
      "jp": "ファンの{声援|せいえん}にこたえて、{選手|せんしゅ}は{手|て}を{振|ふ}った。",
      "th": "Fans cheer-ku response-aa player kai aattinaar.",
      "kana": "ファンのせいえんにこたえて、せんしゅはてをふった。"
     },
     {
      "jp": "{社員|しゃいん}の{要望|ようぼう}にこたえて、{食堂|しょくどう}のメニューを{増|ふ}やした。",
      "th": "Staff request-ku response-aa canteen menu increase pannaanga.",
      "kana": "しゃいんのようぼうにこたえて、しょくどうのメニューをふやした。"
     },
     {
      "jp": "{両親|りょうしん}の{期待|きたい}にこたえて、{医者|いしゃ}になった。",
      "th": "Parents expectation-ku eththa maadhiri doctor aanen.",
      "kana": "りょうしんのきたいにこたえて、いしゃになった。"
     },
     {
      "jp": "{客|きゃく}のニーズにこたえる{商品|しょうひん}を{作|つく}りたい。",
      "th": "Customer needs-ku match aagura product pannanum. (にこたえる + Noun)",
      "kana": "きゃくのニーズにこたえるしょうひんをつくりたい。"
     }
    ],
    "wrong": [
     {
      "ng": "{先生|せんせい}の{質問|しつもん}にこたえて、{手|て}を{挙|あ}げた。",
      "ok": "{先生|せんせい}の{質問|しつもん}に{答|こた}えて、{手|て}を{挙|あ}げた。",
      "th": "Answering a question is plain 答える. にこたえて is for hopes/requests/expectations."
     }
    ],
    "check": [
     {
      "q": "{市民|しみん}の（　　）にこたえて、{図書館|としょかん}の{開館|かいかん}{時間|じかん}を{延|の}ばした。",
      "opts": [
       "{要望|ようぼう}",
       "{不満|ふまん}",
       "{生活|せいかつ}"
      ],
      "ans": 0,
      "explain": "要望 (request) → にこたえて.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～にこたえて",
   "meaning": "～の{期待|きたい}・{要望|ようぼう}がかなうように、あることをする。",
   "explain": [
    "にこたえて = do something so that ～'s expectations or requests are met.",
    "Shape: Noun + にこたえて / Noun + にこたえる + Noun.",
    "Kavanam: only with limited words such as 期待・要望・希望・アンコール. After it, a sentence with a verb."
   ],
   "examples": [
    {
     "t": "①{応援|おうえん}してくれる{人|ひと}の{気持|きも}ち[[にこたえて]]{立派|りっぱ}な{試合|しあい}をしよう。",
     "explain": "応援(おうえん) = support. 立派(りっぱ) = splendid."
    },
    {
     "t": "②その{歌手|かしゅ}は、{会場|かいじょう}の{人々|ひとびと}のアンコール[[にこたえて]]{再|ふたた}び{舞台|ぶたい}に{出|で}てきた。",
     "explain": "会場(かいじょう) = venue. 再(ふたた)び = again. 舞台(ぶたい) = stage."
    },
    {
     "t": "③{国民|こくみん}の{皆様|みなさま}のご{要望|ようぼう}[[にこたえる]]{政治|せいじ}を{行|おこな}いたいと{思|おも}います。",
     "explain": "国民(こくみん) = citizens. 要望(ようぼう) = request. 政治(せいじ) = politics."
    }
   ],
   "form": "［名］　＋にこたえて　／　［名］　＋にこたえる＋［名］",
   "caution": "「{期待|きたい}・{要望|ようぼう}・{希望|きぼう}・アンコール」など{限|かぎ}られた{言葉|ことば}につく。{後|あと}には、{動詞|どうし}の{文|ぶん}が{来|く}る。"
  },
  {
   "type": "group",
   "title": "【1】（～に{関|かん}して）",
   "children": [
    {
     "type": "mcq",
     "id": "d4b-7-1-1",
     "q": "1　{本人|ほんにん}の{了解|りょうかい}がなければ、（　　）に{関|かん}してはお{答|こた}えできません。",
     "opts": [
      "{今年|ことし}{何|なん}{歳|さい}か",
      "{個人|こじん}{情報|じょうほう}",
      "メールアドレス"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Big theme → 個人情報 (personal information). Age/email = one quick answer."
    },
    {
     "type": "mcq",
     "id": "d4b-7-1-2",
     "q": "2　ここには{日本語|にほんご}{能力|のうりょく}{試験|しけん}（　　）ことが{詳|くわ}しく{書|か}いてある。",
     "opts": [
      "に{関|かん}して",
      "に{関|かん}する",
      "に{関|かん}している"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Before a noun (こと) → に関する."
    },
    {
     "type": "mcq",
     "id": "d4b-7-1-3",
     "q": "3　わたしはこの{地域|ちいき}の{植物|しょくぶつ}に{関|かん}して（　　）。",
     "opts": [
      "{本|ほん}で{調|しら}べてみた",
      "{世話|せわ}をしている",
      "{写真|しゃしん}に{撮|と}っている"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Information verb → 調べてみた."
    },
    {
     "type": "mcq",
     "id": "d4b-7-1-4",
     "q": "4　{選挙|せんきょ}{結果|けっか}に{関|かん}する（　　）。",
     "opts": [
      "データを{見|み}たい",
      "{何|なに}か{意見|いけん}はありませんか",
      "インターネットで{調|しら}べた"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "に関する + Noun → データ."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【2】（～をめぐって）",
   "children": [
    {
     "type": "mcq",
     "id": "d4b-7-2-1",
     "q": "1　（　　）{子供|こども}の{教育|きょういく}{問題|もんだい}をめぐっていろいろと{議論|ぎろん}した。",
     "opts": [
      "わたしは",
      "わたしたちは",
      "{父|ちち}は"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Discussion needs many people → わたしたちは."
    },
    {
     "type": "mcq",
     "id": "d4b-7-2-2",
     "q": "2　{旅行|りょこう}のスケジュールをめぐって（　　）。",
     "opts": [
      "ご{説明|せつめい}いたします",
      "このプリントに{書|か}いてある",
      "メンバーの{意見|いけん}が{割|わ}れた"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Conflict/discussion → 意見が割れた."
    },
    {
     "type": "mcq",
     "id": "d4b-7-2-3",
     "q": "3　{新|しん}{年度|ねんど}の{予算|よさん}{案|あん}をめぐって（　　）。",
     "opts": [
      "{国民|こくみん}はあまり{関心|かんしん}がない",
      "{首相|しゅしょう}は{多|おお}くの{質問|しつもん}を{受|う}けた",
      "{対立|たいりつ}はまだ{続|つづ}いている"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Conflict among several → 対立はまだ続いている."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【3】（～にかけては）",
   "children": [
    {
     "type": "mcq",
     "id": "d4b-7-3-1",
     "q": "1　{父|ちち}は（　　）にかけては{親戚|しんせき}の{中|なか}で{一番|いちばん}だ。",
     "opts": [
      "{背|せ}の{高|たか}さ",
      "{話|はなし}のうまさ",
      "{年齢|ねんれい}"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Skill → 話のうまさ."
    },
    {
     "type": "mcq",
     "id": "d4b-7-3-2",
     "q": "2　{花子|はなこ}は（　　）にかけてはすごい{腕|うで}を{持|も}っている。",
     "opts": [
      "{料理|りょうり}",
      "{読書|どくしょ}",
      "おいしいもの"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "腕(うで) = skill → 料理."
    },
    {
     "type": "mcq",
     "id": "d4b-7-3-3",
     "q": "3　わたしは{足|あし}の{速|はや}さにかけては（　　）。",
     "opts": [
      "{全|まった}くだめだ",
      "{速|はや}いほうだ",
      "だれにも{負|ま}けない"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Number one meaning → だれにも負けない."
    },
    {
     "type": "mcq",
     "id": "d4b-7-3-4",
     "q": "4　うちの{子|こ}は{魚|さかな}のことにかけては（　　）。",
     "opts": [
      "{博士|はかせ}と{言|い}ってもいいくらいだ",
      "あまり{関心|かんしん}がないようだ",
      "かなり{好|す}きらしい"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Top level → 博士(はかせ, doctor/expert)と言ってもいいくらい."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【4】（～に{対|たい}して）",
   "children": [
    {
     "type": "mcq",
     "id": "d4b-7-4-1",
     "q": "1　{外国|がいこく}{人|じん}に{対|たい}してこの{国|くに}は（　　）。",
     "opts": [
      "{暮|く}らしやすいか",
      "どんなサポートをするのか",
      "{憧|あこが}れの{国|くに}なのか"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "A: direct action toward foreigners → サポートをする."
    },
    {
     "type": "mcq",
     "id": "d4b-7-4-2",
     "q": "2　{田中|たなか}さんはわたしに{対|たい}して（　　）。",
     "opts": [
      "お{姉|ねえ}さんのような{人|ひと}だ",
      "{最|もっと}も{信頼|しんらい}できる",
      "{特別|とくべつ}に{親切|しんせつ}にしてくれる"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "A: attitude toward me → 親切にしてくれる."
    },
    {
     "type": "mcq",
     "id": "d4b-7-4-3",
     "q": "3　A{校|こう}は（　　）に{対|たい}して、B{校|こう}は{文化|ぶんか}{施設|しせつ}をたくさん{持|も}っている。",
     "opts": [
      "スポーツ{施設|しせつ}がいい",
      "スポーツ{施設|しせつ}がいいの",
      "スポーツ{施設|しせつ}の{良|よ}さ"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "B: plain form + の + に対して."
    },
    {
     "type": "mcq",
     "id": "d4b-7-4-4",
     "q": "4　{昨年|さくねん}、{6月|ろくがつ}は{雨量|うりょう}が{多|おお}かったのに{対|たい}して、（　　）。",
     "opts": [
      "{5月|ごがつ}は{少|すく}なかった",
      "{3月|さんがつ}も{多|おお}かった",
      "{9月|くがつ}は{少|すこ}し{多|おお}かった"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "B: clear contrast → 少なかった."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【5】（～にこたえて）",
   "children": [
    {
     "type": "mcq",
     "id": "d4b-7-5-1",
     "q": "1　{皆様|みなさま}の（　　）にこたえて{精|せい}いっぱい{頑張|がんば}ります。",
     "opts": [
      "ご{期待|きたい}",
      "ご{満足|まんぞく}",
      "ご{不満|ふまん}"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "期待にこたえる = live up to expectations."
    },
    {
     "type": "mcq",
     "id": "d4b-7-5-2",
     "q": "2　{市|し}では{市民|しみん}の{要求|ようきゅう}にこたえて（　　）。",
     "opts": [
      "{商店|しょうてん}{街|がい}が{明|あか}るい",
      "{公園|こうえん}ができた",
      "{保育所|ほいくじょ}を{増|ふ}やした"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "A verb sentence of what the city did → 保育所を増やした."
    },
    {
     "type": "mcq",
     "id": "d4b-7-5-3",
     "q": "3　{歴史|れきし}{的|てき}な{大|だい}{記録|きろく}を{作|つく}った{斉藤|さいとう}{選手|せんしゅ}は、{祝福|しゅくふく}の{拍手|はくしゅ}にこたえて（　　）。",
     "opts": [
      "{帽子|ぼうし}をとって{軽|かる}くおじぎをした",
      "{大|おお}きな{声|こえ}で{返事|へんじ}をした",
      "とても{満足|まんぞく}した{様子|ようす}だった"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Responding to applause with an action → bowed."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【1～5】まとめ",
   "children": [
    {
     "type": "mcq",
     "id": "d4b-7-6-1",
     "q": "1　この{問題|もんだい}はわたし（　　）{難|むずか}しい。",
     "opts": [
      "に{対|たい}して",
      "に{関|かん}して",
      "にとって"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "From my viewpoint → にとって (review)."
    },
    {
     "type": "mcq",
     "id": "d4b-7-6-2",
     "q": "2　{所長|しょちょう}は{今回|こんかい}の{事件|じけん}（　　）どう{責任|せきにん}をとるつもりなのか。",
     "opts": [
      "をめぐって",
      "に{対|たい}して",
      "にこたえて"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Taking responsibility toward the incident → に対して (A)."
    },
    {
     "type": "mcq",
     "id": "d4b-7-6-3",
     "q": "3　エンジンの{開発|かいはつ}（　　）、{日本|にほん}ではN{社|しゃ}が{一番|いちばん}{進|すす}んでいると{思|おも}う。",
     "opts": [
      "に{対|たい}しては",
      "にこたえては",
      "にかけては"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Best at → にかけては."
    },
    {
     "type": "mcq",
     "id": "d4b-7-6-4",
     "q": "4　{今回|こんかい}の{選挙|せんきょ}では、{環境|かんきょう}{税|ぜい}（　　）{候補|こうほ}{者|しゃ}たちの{意見|いけん}が{対立|たいりつ}している。",
     "opts": [
      "に{対|たい}して",
      "をめぐって",
      "にこたえて"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Opinions clash over it → をめぐって."
    },
    {
     "type": "mcq",
     "id": "d4b-7-6-5",
     "q": "5　{政治|せいじ}{問題|もんだい}（　　）{若|わか}い{人|ひと}たちはあまり{興味|きょうみ}がないようだ。",
     "opts": [
      "に{関|かん}して",
      "にかけて",
      "をめぐって"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "About a theme → に関して."
    }
   ],
   "scored": true
  }
 ]
});
