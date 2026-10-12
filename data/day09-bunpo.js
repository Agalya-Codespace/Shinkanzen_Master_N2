/* Day 9 · bunpo. Built from d09_bunpo.py by tools/build_day.py (furigana added automatically). */
window.N2_DAYS = window.N2_DAYS || {};
window.N2_DAYS[9] = window.N2_DAYS[9] || {"title": "", "intro": "", "sections": []};
if (false) window.N2_DAYS[9].title = "";
if (false) window.N2_DAYS[9].intro = "";
window.N2_DAYS[9].sections.push({
 "book": "bunpo",
 "title": "Ⅱ {主観|しゅかん}を{含|ふく}めて{説明|せつめい}する☆☆　16{課|か} ～だから（{理由|りゆう}）-1／17{課|か} ～だから（{理由|りゆう}）-2",
 "source": "新完全マスター文法 N2 · 第1部 文の文法1 · pp.74–81 · answers from 別冊 解答 p.5",
 "blocks": [
  {
   "type": "items",
   "title": "16{課|か}　〔{復習|ふくしゅう}〕",
   "items": [
    {
     "t": "・{時間|じかん}がなかった[[ので]]、{十分|じゅうぶん}な{準備|じゅんび}ができなかった。",
     "explain": "Review: ので = because."
    },
    {
     "t": "・{試験|しけん}のことが{気|き}になっ[[て]]、なかなか{眠|ねむ}れなかった。",
     "explain": "Review: て = because (cause)."
    },
    {
     "t": "・{事故|じこ}があった[[ために]]、{道路|どうろ}が{渋滞|じゅうたい}した。",
     "explain": "Review: ために = because of (formal)."
    }
   ],
   "explain": "16・17課 = many ways to say 'because': によって, ものだから, おかげ/せい, あまり, につき, ことだし, のことだから, だけに, ばかりに, からには."
  },
  {
   "type": "grammar",
   "no": "1",
   "id": "d9b-g1",
   "teach": {
    "intro": [
     "によって = 'because of ～' (cause) or 'by means of ～' (method). Hard, formal style (硬い言い方).",
     "'Accident naala train timetable full-aa kozhambiduchu.' — cause.",
     "Before a noun it becomes による: 台風による被害 = damage caused by the typhoon."
    ],
    "pattern": "［名詞］＋によって　／　［名詞］＋による＋［名詞］",
    "examples": [
     {
      "jp": "{事故|じこ}によって、{電車|でんしゃ}が{止|と}まった。",
      "th": "Accident naala train nindruchu.",
      "kana": "じこによって、でんしゃがとまった。"
     },
     {
      "jp": "{台風|たいふう}による{被害|ひがい}が{大|おお}きかった。",
      "th": "Puyal-aala vandha sedham romba adhigam.",
      "kana": "たいふうによるひがいがおおきかった。"
     },
     {
      "jp": "{結果|けっか}はメールによってお{知|し}らせします。",
      "th": "Result-ai email moolama solvom.",
      "kana": "けっかはメールによっておしらせします。"
     }
    ],
    "wrong": [
     {
      "ng": "{結果|けっか}については{電話|でんわ}によりお{知|し}らせします。",
      "ok": "{結果|けっか}については{文書|ぶんしょ}によりお{知|し}らせします。",
      "th": "Method meaning: not used with everyday personal tools like 電話・ペン・電車 (except before a noun: 電話による問い合わせ)."
     }
    ],
    "check": [
     {
      "q": "この{地震|じしん}（　　）{津波|つなみ}の{心配|しんぱい}はありません。",
      "opts": [
       "によって",
       "による",
       "によっての"
      ],
      "ans": 1,
      "explain": "Before the noun 津波 → による.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～によって",
   "meaning": "～が{原因|げんいん}で、ある{結果|けっか}になる・～という{手段|しゅだん}や{方法|ほうほう}であることをする。",
   "explain": [
    "によって = because of ～ a result happens; or doing something by the means/method ～.",
    "Shape: Noun + によって; Noun + による + Noun.",
    "Kavanam: in the method meaning, it is awkward with everyday tools used personally (電話・ペン・電車), but OK in the noun-describing form like ⑤ (電話による問い合わせ)."
   ],
   "examples": [
    {
     "t": "①{今朝|けさ}、{中央線|ちゅうおうせん}は{踏切内|ふみきりない}で{起|お}きた{事故|じこ}[[によって]]、ダイヤが{大|おお}きく{乱|みだ}れた。",
     "explain": "Cause. ダイヤ = train timetable. 乱(みだ)れる = be disrupted."
    },
    {
     "t": "②{会長|かいちょう}が{交替|こうたい}したこと[[によって]]、{会|かい}の{雰囲気|ふんいき}が{大|おお}きく{変|か}わった。",
     "explain": "Cause. 交替 = change of person."
    },
    {
     "t": "③この{地方|ちほう}は{毎年|まいとし}{台風|たいふう}[[による]]{被害|ひがい}が{出|で}ている。",
     "explain": "Noun form: 台風による被害."
    },
    {
     "t": "④{仕事|しごと}をコンピューター{化|か}すること[[により]]、{労働|ろうどう}{力|りょく}{不足|ふそく}は{解決|かいけつ}できるのではないか。",
     "explain": "Method. により = written form of によって."
    },
    {
     "t": "⑤{合否|ごうひ}の{結果|けっか}は{後日|ごじつ}{書面|しょめん}で{連絡|れんらく}します。{電話|でんわ}[[による]]{問|と}い{合|あ}わせは{受|う}け{付|つ}けません。",
     "explain": "電話 is OK here because it describes a noun."
    }
   ],
   "form": "［名］　＋によって　／　［名］　＋による＋［名］",
   "caution": "{手段|しゅだん}の{意味|いみ}では、{日常|にちじょう}{的|てき}な{道具|どうぐ}など（{電話|でんわ}・ペン・{電車|でんしゃ}など）を{個人|こじん}{的|てき}に{使|つか}う{場合|ばあい}は{使|つか}いにくいが、⑤のように{名詞|めいし}を{説明|せつめい}する{形|けい}では{使|つか}える。"
  },
  {
   "type": "grammar",
   "no": "2",
   "id": "d9b-g2",
   "teach": {
    "intro": [
     "ものだから / もので = 'because ～ (you see)' — giving an EXCUSE. Spoken (話し言葉).",
     "'Sorry sir, fever irundhadhaala leave eduthen.' — personal excuse.",
     "もの at the end = 'because…!' (a bit childish/feminine). もんだから・もんで・もん = even more casual."
    ],
    "pattern": "{普通形|ふつうけい}（［な形容詞］だ→な・［名詞］だ→な）＋ものだから・もので　／　{普通形|ふつうけい}＋もの",
    "examples": [
     {
      "jp": "{道|みち}が{込|こ}んでいたものですから、{遅|おく}れてしまいました。",
      "th": "Traffic irundhadhaala late aayiduchu, sorry.",
      "kana": "みちがこんでいたものですから、おくれてしまいました。"
     },
     {
      "jp": "{急|いそ}いでいたもので、メールを{見|み}ていませんでした。",
      "th": "Avasaram-aa irundhadhaala mail paakkala.",
      "kana": "いそいでいたもので、メールをみていませんでした。"
     },
     {
      "jp": "だって、{知|し}らなかったんだもの。",
      "th": "Enakku theriyaadhae! (childish excuse)",
      "kana": "だって、しらなかったんだもの。"
     }
    ],
    "wrong": [
     {
      "ng": "{朝|あさ}ご{飯|はん}を{食|た}べなかったものだから、{早|はや}く{昼|ひる}ご{飯|はん}にしよう。",
      "ok": "{朝|あさ}ご{飯|はん}を{食|た}べなかったものだから、おなかがすいてきた。",
      "th": "No command or intention after ものだから. It's an excuse for something that already happened."
     }
    ],
    "check": [
     {
      "q": "A「どうしてこれ、{食|た}べないの？」B「だって、（　　）。」",
      "opts": [
       "{大嫌|だいきら}いなもの",
       "{大嫌|だいきら}いなんだもの",
       "{大嫌|だいきら}いであるもの"
      ],
      "ans": 1,
      "explain": "Sentence-end もの with an excuse: 大嫌いなんだもの.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～ものだから・～もので・～もの",
   "meaning": "「～ので…」と{言|い}い{訳|わけ}をする。",
   "explain": [
    "ものだから・もので・もの = make an excuse: 'because ～, you see'.",
    "Shape: plain form (な-adj ~~だ~~ → な, Noun ~~だ~~ → な) + ものだから・もので; plain form + もの.",
    "Kavanam: a personal excuse. No command or intention sentence after it. もの is mostly sentence-final, used a lot by women and children. After ものですから・もので the rest is sometimes left out. もんだから・もんで・もん are even more casual."
   ],
   "examples": [
    {
     "t": "①すみません。{昨日|きのう}はちょっと{熱|ねつ}があった[[ものですから]]、お{休|やす}みしました。",
     "explain": "Polite excuse to a teacher/boss."
    },
    {
     "t": "②このところ{忙|いそが}しかった[[もので]]、お{返事|へんじ}が{遅|おく}れてしまいました。ごめんなさい。",
     "explain": "Excuse for a late reply."
    },
    {
     "t": "③わたし、{近眼|きんがん}な[[もんで]]、お{顔|かお}がよく{見|み}えなかったんです。{失礼|しつれい}しました。",
     "explain": "近眼 = short-sighted. もんで = casual."
    },
    {
     "t": "④あの{人|ひと}の{言|い}うことはよくわからないよ。{言葉|ことば}が{難|むずか}しいんだ[[もの]]。",
     "explain": "Sentence-end もの."
    }
   ],
   "form": "{普通形|ふつうけい}（［ナ形］だ－な・［名］だ－な）　＋ものだから・もので　／　{普通形|ふつうけい}　＋もの",
   "caution": "{個人|こじん}{的|てき}な{言|い}い{訳|わけ}を{言|い}う。{後|あと}に{命令|めいれい}や{意向|いこう}を{表|あらわ}す{文|ぶん}は{来|こ}ない。「もの」は{主|おも}に{文末|ぶんまつ}に{使|つか}い、{特|とく}に{女性|じょせい}や{子供|こども}が{多|おお}く{使|つか}う。「ものですから・もので」の{後|あと}の{文|ぶん}も、{省略|しょうりゃく}されることがある。「もんだから・もんで・もん」は、さらにくだけた{言|い}い{方|かた}。"
  },
  {
   "type": "grammar",
   "no": "3",
   "id": "d9b-g3",
   "teach": {
    "intro": [
     "おかげ = thanks to ～ (GOOD result). せい = because of ～ / ～'s fault (BAD result).",
     "'Sir-oda help-aala pass panninen' → おかげ. 'Kulir naala sakura late' → せい.",
     "せいか = 'maybe because of ～'. After them: NO intention or request."
    ],
    "pattern": "［名詞］の・［動詞・形容詞］{普通形|ふつうけい}（［な形容詞］だ→な）＋おかげだ／せいだ",
    "examples": [
     {
      "jp": "{先生|せんせい}のおかげで、{合格|ごうかく}できました。",
      "th": "Teacher-naala dhaan pass aanen. Nandri!",
      "kana": "せんせいのおかげで、ごうかくできました。"
     },
     {
      "jp": "{雨|あめ}のせいで、{試合|しあい}が{中止|ちゅうし}になった。",
      "th": "Mazhai naala match cancel aachu.",
      "kana": "あめのせいで、しあいがちゅうしになった。"
     },
     {
      "jp": "{年|とし}のせいか、{最近|さいきん}{疲|つか}れやすい。",
      "th": "Vayasu-naalo enno, ippo seekiram tired aagudhu.",
      "kana": "としのせいか、さいきんつかれやすい。"
     }
    ],
    "wrong": [
     {
      "ng": "{体力|たいりょく}がついてきたおかげで、これからは{頑張|がんば}ろう。",
      "ok": "{体力|たいりょく}がついてきたおかげで、これからは{頑張|がんば}れる。",
      "th": "No intention (～よう) after おかげで. State a result: 頑張れる."
     }
    ],
    "check": [
     {
      "q": "この{夏|なつ}、{気温|きおん}が{上|あ}がらなかった（　　）、ぶどうが{甘|あま}くない。",
      "opts": [
       "せいで",
       "おかげで",
       "おかげか"
      ],
      "ans": 0,
      "explain": "Bad result (not sweet) → せいで.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～おかげだ／～せいだ",
   "meaning": "～の{影響|えいきょう}で、いい{結果|けっか}／{悪|わる}い{結果|けっか}になった。",
   "explain": [
    "おかげだ／せいだ = because of the influence of ～, a good result / a bad result happened.",
    "Shape: Noun + の, verb/adjective plain form (な-adj ~~だ~~ → な) + おかげだ／せいだ.",
    "Kavanam: after 〜おかげで comes a good result; after 〜せいで a bad result. No speaker's intention or request sentence after them."
   ],
   "examples": [
    {
     "t": "①わたしが{東西|とうざい}{大学|だいがく}に{合格|ごうかく}できたのは、{山川|やまかわ}{先生|せんせい}の[[おかげです]]。ありがとうございました。",
     "explain": "Thanks to the teacher."
    },
    {
     "t": "②{佐藤|さとう}さんが{丁寧|ていねい}にチェックしてくださった[[おかげで]]、いいレポートができました。",
     "explain": "Good result."
    },
    {
     "t": "③いい{天気|てんき}が{続|つづ}いている[[おかげで]]、{工事|こうじ}が{思|おも}ったより{早|はや}く{進|すす}んでいます。",
     "explain": "Good result (not only people)."
    },
    {
     "t": "④{父|ちち}は{最近|さいきん}{口数|くちかず}が{少|すく}ない。{疲|つか}れている[[せい]]かもしれない。",
     "explain": "口数が少ない = talks little."
    },
    {
     "t": "⑤{今年|ことし}の{春|はる}は{気温|きおん}が{低|ひく}い{日|ひ}が{多|おお}かった[[せいで]]、{桜|さくら}の{開花|かいか}が{遅|おそ}い。",
     "explain": "Bad result."
    },
    {
     "t": "⑥{値段|ねだん}の[[せいか]]、この{商品|しょうひん}は{売|う}れ{行|ゆ}きが{悪|わる}い。",
     "explain": "せいか = maybe because of."
    }
   ],
   "form": "［名］－の・［動・形］{普通形|ふつうけい}（［ナ形］だ－な）　＋おかげだ／せいだ",
   "caution": "「～おかげで」の{後|あと}にはいい{結果|けっか}を{表|あらわ}す{文|ぶん}、「～せいで」の{後|あと}には{良|よ}くない{結果|けっか}を{表|あらわ}す{文|ぶん}が{来|く}る。{話者|わしゃ}の{意向|いこう}を{表|あらわ}す{文|ぶん}や{働|はたら}きかけの{文|ぶん}は{来|こ}ない。"
  },
  {
   "type": "grammar",
   "no": "4",
   "id": "d9b-g4",
   "teach": {
    "intro": [
     "あまり = 'so ～ that (something unusual happened)'. 'Tension adhigam-aagi, mind blank aayiduchu.'",
     "Usually with feeling nouns: 緊張のあまり, 悔しさのあまり, うれしさのあまり.",
     "あまりの + Noun + に: あまりの寒さに = because it was SO cold. Result is unusual (often bad); no wish or request after."
    ],
    "pattern": "［名詞］の・［動詞・形容詞］{普通形|ふつうけい}肯定（［な形容詞］だ→な）＋あまり　／　あまりの＋［名詞］＋に",
    "examples": [
     {
      "jp": "{緊張|きんちょう}のあまり、{声|こえ}が{出|で}なかった。",
      "th": "Tension adhigam-aagi, kural varala.",
      "kana": "きんちょうのあまり、こえがでなかった。"
     },
     {
      "jp": "うれしさのあまり、{泣|な}いてしまった。",
      "th": "Romba sandhosham-aagi azhuthutten.",
      "kana": "うれしさのあまり、ないてしまった。"
     },
     {
      "jp": "あまりの{暑|あつ}さに、{倒|たお}れそうになった。",
      "th": "Veyil romba adhigam, kizha vizha poitten.",
      "kana": "あまりのあつさに、たおれそうになった。"
     }
    ],
    "wrong": [
     {
      "ng": "{結論|けつろん}を{急|いそ}いでのあまり、{相手|あいて}を{怒|おこ}らせてしまった。",
      "ok": "{結論|けつろん}を{急|いそ}いだあまり、{相手|あいて}を{怒|おこ}らせてしまった。",
      "th": "Verb plain form + あまり: 急いだあまり. (Noun + の + あまり.)"
     }
    ],
    "check": [
     {
      "q": "{沖縄|おきなわ}の{海|うみ}は{本当|ほんとう}にきれいだった。あまりの{美|うつく}しさに（　　）。",
      "opts": [
       "ぼーっとしてしまった",
       "よく{見|み}た",
       "とてもうれしかった"
      ],
      "ans": 0,
      "explain": "Unusual result: was dazed.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～あまり・あまりの～に",
   "meaning": "とても～ので、{普通|ふつう}ではない{結果|けっか}になってしまった。",
   "explain": [
    "あまり・あまりの～に = because it was very ～, it ended in an unusual result.",
    "Shape: Noun + の, verb/adj plain affirmative (な-adj ~~だ~~ → な) + あまり; あまりの + Noun + に.",
    "Kavanam: after it comes an unusual result (often a bad one). No speaker's wish/intention or request sentence."
   ],
   "examples": [
    {
     "t": "①{自分|じぶん}の{番|ばん}が{近|ちか}づいてきたとき、わたしは{緊張|きんちょう}の[[あまり]]{頭|あたま}の{中|なか}が{真|ま}っ{白|しろ}になってしまった。",
     "explain": "頭の中が真っ白 = mind went blank."
    },
    {
     "t": "②{当然|とうぜん}{勝|か}つと{思|おも}っていた{試合|しあい}で{最後|さいご}に{逆転|ぎゃくてん}{負|ま}けし、{悔|くや}しさの[[あまり]]ぼろぼろ{泣|な}いた。",
     "explain": "悔しさ = frustration."
    },
    {
     "t": "③{仕事|しごと}を{早|はや}く{片付|かたづ}けようと{急|いそ}いだ[[あまり]]、いくつかミスをしてしまった。",
     "explain": "Verb + あまり."
    },
    {
     "t": "④10{年|ねん}ぶりで{兄|あに}に{会|あ}った。{兄|あに}の[[あまりの]]{変化|へんか}[[に]]{言葉|ことば}が{出|で}なかった。",
     "explain": "あまりの変化に = at how much he had changed."
    }
   ],
   "form": "［名］－の・［動・形］{普通形|ふつうけい}{肯定|こうてい}（［ナ形］だ－な）　＋あまり　／　あまりの＋［名］　＋に",
   "caution": "{後|あと}には、{普通|ふつう}でない{結果|けっか}（{悪|わる}い{結果|けっか}が{多|おお}い）を{表|あらわ}す{文|ぶん}が{来|く}る。{話者|わしゃ}の{希望|きぼう}・{意向|いこう}を{表|あらわ}す{文|ぶん}や{働|はたら}きかけの{文|ぶん}は{来|こ}ない。"
  },
  {
   "type": "grammar",
   "no": "5",
   "id": "d9b-g5",
   "teach": {
    "intro": [
     "につき = 'due to ～' on public NOTICES and signs. Hard, written style.",
     "'Cleaning nadakkudhu, so toilet use panna mudiyaadhu' — the sign on the door.",
     "Noun + につき. After it: the current situation (closed, not available)."
    ],
    "pattern": "［名詞］＋につき",
    "examples": [
     {
      "jp": "{工事|こうじ}{中|ちゅう}につき、{通行止|つうこうど}め。",
      "th": "Work nadakkudhu, so road closed.",
      "kana": "こうじちゅうにつき、つうこうどめ。"
     },
     {
      "jp": "{本日|ほんじつ}は{祝日|しゅくじつ}につき、{休業|きゅうぎょう}します。",
      "th": "Inniki holiday, so leave.",
      "kana": "ほんじつはしゅくじつにつき、きゅうぎょうします。"
     },
     {
      "jp": "{故障|こしょう}につき、{使用|しよう}できません。",
      "th": "Repair, so use panna mudiyaadhu.",
      "kana": "こしょうにつき、しようできません。"
     }
    ],
    "wrong": [
     {
      "ng": "{雨天|うてん}につき、{今日|きょう}は{出|で}かけたくない。",
      "ok": "{雨天|うてん}につき、{本日|ほんじつ}の{野球|やきゅう}の{試合|しあい}は{中止|ちゅうし}とする。",
      "th": "につき is for public announcements, not personal feelings."
     }
    ],
    "check": [
     {
      "q": "このプリンターは{故障|こしょう}につき、（　　）。",
      "opts": [
       "わたしが{直|なお}しましょうか",
       "{直|なお}してくださいよ",
       "{使用|しよう}できません"
      ],
      "ans": 2,
      "explain": "Notice style: 使用できません.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～につき",
   "meaning": "「～の{理由|りゆう}で、ある{状態|じょうたい}になる」と{公|おおやけ}に{知|し}らせる。",
   "explain": [
    "につき = officially announce 'because of ～, the situation is …'.",
    "Shape: Noun + につき.",
    "Kavanam: attaches to words that show the current situation. Used on posted notices (張り紙) and official documents."
   ],
   "examples": [
    {
     "t": "①トイレはただ{今|いま}{清掃中|せいそうちゅう}[[につき]]、ご{利用|りよう}になれません。",
     "explain": "清掃中 = being cleaned."
    },
    {
     "t": "②{強風|きょうふう}[[につき]]、この{門|もん}は{閉鎖中|へいさちゅう}です。",
     "explain": "閉鎖 = closed."
    },
    {
     "t": "③{本日|ほんじつ}は{祝日|しゅくじつ}[[につき]]、{閉館|へいかん}しております。",
     "explain": "閉館 = building closed."
    }
   ],
   "form": "［名］　＋につき",
   "caution": "{現時点|げんじてん}での{状況|じょうきょう}を{表|あらわ}す{言葉|ことば}につく。{張|は}り{紙|がみ}や{公式|こうしき}{文書|ぶんしょ}などに{使|つか}う。"
  },
  {
   "type": "group",
   "title": "【1】（～によって）",
   "children": [
    {
     "type": "mcq",
     "id": "d9b-16-1-1",
     "q": "1　{結果|けっか}については（　　）によりお{知|し}らせします。",
     "opts": [
      "{手紙|てがみ}",
      "{文書|ぶんしょ}",
      "{電話|でんわ}"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Method + により: formal means → 文書. Not everyday tools like 電話・手紙."
    },
    {
     "type": "mcq",
     "id": "d9b-16-1-2",
     "q": "2　この{薬|くすり}は、20{回|かい}{以上|いじょう}の{実験|じっけん}（　　）{効果|こうか}が{証明|しょうめい}された。",
     "opts": [
      "によって",
      "による",
      "によっての"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Before a verb phrase → によって."
    },
    {
     "type": "mcq",
     "id": "d9b-16-1-3",
     "q": "3　この{地震|じしん}（　　）{津波|つなみ}の{心配|しんぱい}はありません。",
     "opts": [
      "によって",
      "による",
      "によっての"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Before the noun 津波 → による."
    },
    {
     "type": "mcq",
     "id": "d9b-16-1-4",
     "q": "4　{事故|じこ}の{原因|げんいん}は{運転|うんてん}{手|しゅ}の{不注意|ふちゅうい}（　　）{信号|しんごう}{無視|むし}だった。",
     "opts": [
      "から",
      "による",
      "によって"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "不注意による信号無視 = ignoring the light caused by carelessness (noun form)."
    },
    {
     "type": "mcq",
     "id": "d9b-16-1-5",
     "q": "5　{中川|なかがわ}{先生|せんせい}と{出会|であ}ったことによって、わたしは（　　）。",
     "opts": [
      "うれしかった",
      "たいへん{良|よ}かった",
      "{大|おお}きく{変|か}わった"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Cause → result change: 大きく変わった."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【2】（～ものだから・～もので・～もの）",
   "children": [
    {
     "type": "mcq",
     "id": "d9b-16-2-1",
     "q": "1　A「どうしてこれ、{食|た}べないの？」B「だって、（　　）。ぜんぜん{食|た}べられないよ。」",
     "opts": [
      "{大嫌|だいきら}いなもの",
      "{大嫌|だいきら}いなんだもの",
      "{大嫌|だいきら}いであるもの"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Excuse: ～んだもの."
    },
    {
     "type": "mcq",
     "id": "d9b-16-2-2",
     "q": "2　{朝|あさ}ご{飯|はん}を{食|た}べなかったものだから、（　　）。",
     "opts": [
      "おなかがすいてきた",
      "{早|はや}く{昼|ひる}ご{飯|はん}にしよう",
      "ここで{食|た}べてもいいですか"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "No intention/request after ものだから → a fact."
    },
    {
     "type": "mcq",
     "id": "d9b-16-2-3",
     "q": "3　ちょっと{寒|さむ}いんです。（　　）もので。",
     "opts": [
      "{冬|ふゆ}になった",
      "{気温|きおん}が8{度|ど}な",
      "シャツ1{枚|まい}しか{着|き}ていない"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Personal excuse: I'm only wearing one shirt."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【3】（～おかげだ／～せいだ）",
   "children": [
    {
     "type": "mcq",
     "id": "d9b-16-3-1",
     "q": "1　{田中|たなか}さんの（　　）、{楽|たの}しい{旅行|りょこう}ができました。ありがとうございました。",
     "opts": [
      "おかげで",
      "おかげさまで",
      "おかげか"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Noun の + おかげで. (おかげさまで is a set greeting.)"
    },
    {
     "type": "mcq",
     "id": "d9b-16-3-2",
     "q": "2　{体力|たいりょく}がついてきたおかげで、これからは（　　）。",
     "opts": [
      "{頑張|がんば}ろう",
      "{頑張|がんば}れる",
      "{頑張|がんば}ることにした"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "No intention after おかげで → 頑張れる."
    },
    {
     "type": "mcq",
     "id": "d9b-16-3-3",
     "q": "3　{来客|らいきゃく}が{多|おお}かったせいで、とても（　　）。",
     "opts": [
      "{良|よ}かった",
      "{楽|たの}しかった",
      "{疲|つか}れた"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "せいで → bad result."
    },
    {
     "type": "mcq",
     "id": "d9b-16-3-4",
     "q": "4　この{夏|なつ}、{気温|きおん}が{上|あ}がらなかった（　　）、ぶどうが{甘|あま}くない。",
     "opts": [
      "せいで",
      "おかげで",
      "おかげか"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Bad result → せいで."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【4】（～あまり・あまりの～に）",
   "children": [
    {
     "type": "mcq",
     "id": "d9b-16-4-1",
     "q": "1　{結論|けつろん}を（　　）あまり、{相手|あいて}を{怒|おこ}らせてしまった。",
     "opts": [
      "{急|いそ}いだ",
      "{急|いそ}いだの",
      "{急|いそ}いで"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Verb plain form + あまり."
    },
    {
     "type": "mcq",
     "id": "d9b-16-4-2",
     "q": "2　わたしが{書|か}いた{小説|しょうせつ}が{入選|にゅうせん}した。その{晩|ばん}はうれしさのあまり（　　）。",
     "opts": [
      "よく{眠|ねむ}った",
      "よく{眠|ねむ}れなかった",
      "{少|すこ}し{眠|ねむ}った"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Unusual result: couldn't sleep."
    },
    {
     "type": "mcq",
     "id": "d9b-16-4-3",
     "q": "3　お{祭|まつ}りの{後|あと}はごみがいっぱいだった。あまりの{汚|きたな}さに（　　）。",
     "opts": [
      "{良|よ}くないと{思|おも}う",
      "{気分|きぶん}が{悪|わる}くなった",
      "すぐ{掃除|そうじ}をしてください"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Unusual result, no request."
    },
    {
     "type": "mcq",
     "id": "d9b-16-4-4",
     "q": "4　{沖縄|おきなわ}の{海|うみ}は{本当|ほんとう}にきれいだった。あまりの{美|うつく}しさに（　　）。",
     "opts": [
      "ぼーっとしてしまった",
      "よく{見|み}た",
      "とてもうれしかった"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Unusual state: dazed."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【5】（～につき）",
   "children": [
    {
     "type": "mcq",
     "id": "d9b-16-5-1",
     "q": "1　ただ{今|いま}（　　）につき、{入室|にゅうしつ}はご{遠慮|えんりょ}ください。",
     "opts": [
      "{忙|いそが}しい",
      "{仕事|しごと}",
      "{録音|ろくおん}{中|ちゅう}"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Noun of the current situation: 録音中 (recording now)."
    },
    {
     "type": "mcq",
     "id": "d9b-16-5-2",
     "q": "2　{雨天|うてん}につき、（　　）。",
     "opts": [
      "{今日|きょう}は{出|で}かけたくない",
      "{本日|ほんじつ}の{野球|やきゅう}の{試合|しあい}は{中止|ちゅうし}とする",
      "{今日|きょう}は{外出|がいしゅつ}はやめよう"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Official announcement."
    },
    {
     "type": "mcq",
     "id": "d9b-16-5-3",
     "q": "3　このプリンターは{故障|こしょう}につき、（　　）。",
     "opts": [
      "わたしが{直|なお}しましょうか",
      "{直|なお}してくださいよ",
      "{使用|しよう}できません"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Notice: 使用できません."
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
     "id": "d9b-16-6-1",
     "q": "1　あの{議員|ぎいん}は{不注意|ふちゅうい}な{発言|はつげん}（　　）{人気|にんき}がなくなってしまった。",
     "opts": [
      "によって",
      "のあまり",
      "につき"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Cause → によって."
    },
    {
     "type": "mcq",
     "id": "d9b-16-6-2",
     "q": "2　わたしたちのチームがとうとう{優勝|ゆうしょう}した。{感激|かんげき}の（　　）、{涙|なみだ}が{出|で}た。",
     "opts": [
      "せいで",
      "おかげで",
      "あまり"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "感激のあまり = so moved that…"
    },
    {
     "type": "mcq",
     "id": "d9b-16-6-3",
     "q": "3　{工事|こうじ}{中|ちゅう}（　　）、この{道|みち}は{通行止|つうこうど}めです。",
     "opts": [
      "なものだから",
      "のあまり",
      "につき"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Notice → につき."
    },
    {
     "type": "mcq",
     "id": "d9b-16-6-4",
     "q": "4　ミスをしないようにと{気|き}にする（　　）、つい{消極|しょうきょく}{的|てき}になってしまう。",
     "opts": [
      "おかげで",
      "あまり",
      "もの"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Worry too much → あまり."
    },
    {
     "type": "mcq",
     "id": "d9b-16-6-5",
     "q": "5　（　　）、{本日|ほんじつ}の{野外|やがい}{写生|しゃせい}{会|かい}は{延期|えんき}させていただきます。",
     "opts": [
      "{悪天候|あくてんこう}のため",
      "{悪天候|あくてんこう}なものだから",
      "{悪天候|あくてんこう}のせいで"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Formal announcement → ため. ものだから = personal excuse; せいで = blaming."
    }
   ],
   "scored": true
  },
  {
   "type": "grammar",
   "no": "6",
   "id": "d9b-g6",
   "teach": {
    "intro": [
     "ことだし = 'since ～ (among other reasons), let's / I'll …'. Spoken.",
     "'Mazhai ninnuduchu, so konjam jogging poittu varalaam.'",
     "After it: judgement, wish, intention, invitation (～よう, ～ませんか, ～たい)."
    ],
    "pattern": "{普通形|ふつうけい}（［な形容詞］だ→な／である・［名詞］だ→の／である）＋ことだし",
    "examples": [
     {
      "jp": "{雨|あめ}もやんだことだし、{散歩|さんぽ}に{行|い}こう。",
      "th": "Mazhai ninnuduchu, walk polaam.",
      "kana": "あめもやんだことだし、さんぽにいこう。"
     },
     {
      "jp": "みんな{集|あつ}まったことだし、{始|はじ}めましょう。",
      "th": "Ellaarum vandhaachu, start pannalaam.",
      "kana": "みんなあつまったことだし、はじめましょう。"
     },
     {
      "jp": "{今日|きょう}は{休|やす}みのことだし、ゆっくりしよう。",
      "th": "Inniki leave dhaan, relax pannalaam.",
      "kana": "きょうはやすみのことだし、ゆっくりしよう。"
     }
    ],
    "wrong": [
     {
      "ng": "{今週|こんしゅう}は{忙|いそが}しかったことだし、とても{疲|つか}れた。",
      "ok": "{今週|こんしゅう}は{忙|いそが}しかったことだし、{週末|しゅうまつ}はゆっくり{休|やす}みたい。",
      "th": "ことだし leads to a judgement/wish/intention, not just a result."
     }
    ],
    "check": [
     {
      "q": "{出発|しゅっぱつ}まで{時間|じかん}も{十分|じゅうぶん}（　　）ことだし、ロビーでちょっとお{茶|ちゃ}でも{飲|の}みませんか。",
      "opts": [
       "ある",
       "あります",
       "あるの"
      ],
      "ans": 0,
      "explain": "Plain form + ことだし: あることだし.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～ことだし",
   "meaning": "ほかにも{理由|りゆう}はあるが、とにかく～だからあることをする。",
   "explain": [
    "ことだし = there are other reasons too, but anyway because ～, do something.",
    "Shape: plain form (な-adj ~~だ~~ → な / である, Noun ~~だ~~ → の / である) + ことだし.",
    "Kavanam: after it comes a sentence of the speaker's judgement, wish, intention, or a request/invitation."
   ],
   "examples": [
    {
     "t": "①{来週|らいしゅう}はお{客様|きゃくさま}が{来|く}る[[ことだし]]、{家|いえ}の{中|なか}の{大掃除|おおそうじ}をしなくちゃ。",
     "explain": "Intention."
    },
    {
     "t": "②{雨|あめ}もやんだ[[ことだし]]、ちょっとジョギングしてこようかな。",
     "explain": "Intention."
    },
    {
     "t": "③こちらのおなべは{値段|ねだん}も{安|やす}い[[ことですし]]、お{一|ひと}ついかがでしょうか。",
     "explain": "Polite: ことですし. Sales talk."
    },
    {
     "t": "④あしたはお{父|とう}さんも{休|やす}みの[[ことだし]]、みんなで{買|か}い{物|もの}でも{行|い}かない？",
     "explain": "Noun + の + ことだし. Invitation."
    }
   ],
   "form": "{普通形|ふつうけい}（［ナ形］だ－な／－である・［名］だ－の／－である）　＋ことだし",
   "caution": "{後|あと}には、{話者|わしゃ}の{判断|はんだん}・{希望|きぼう}・{意向|いこう}を{表|あらわ}す{文|ぶん}や{働|はたら}きかけの{文|ぶん}などが{来|く}る。"
  },
  {
   "type": "grammar",
   "no": "7",
   "id": "d9b-g7",
   "teach": {
    "intro": [
     "のことだから = 'knowing ～ (his/her character), surely …'. Mostly after PEOPLE.",
     "'Michiko-vaa? Avalukku hard work pazhakkam, so kandippa nalla mark vaanguvaa.'",
     "After it: guess or judgement (きっと～だろう, ～はずだ). Can also end a sentence: あの子のことだ。"
    ],
    "pattern": "［名詞］＋のことだから",
    "examples": [
     {
      "jp": "まじめな{彼|かれ}のことだから、{遅|おく}れずに{来|く}るだろう。",
      "th": "Sincere-aana aal, late-aa vara maattaan.",
      "kana": "まじめなかれのことだから、おくれずにくるだろう。"
     },
     {
      "jp": "{母|はは}のことだから、きっと{心配|しんぱい}している。",
      "th": "Amma-vaa? Kandippa worry pannuvaanga.",
      "kana": "ははのことだから、きっとしんぱいしている。"
     },
     {
      "jp": "あの{子|こ}のことだ。また{忘|わす}れたんだろう。",
      "th": "Andha paiyan dhaan. Marubadiyum marandhirupaan.",
      "kana": "あのこのことだ。またわすれたんだろう。"
     }
    ],
    "wrong": [
     {
      "ng": "{海|うみ}が{好|す}きな{母|はは}のことだから、{海|うみ}で{遊|あそ}ぶのをとても{楽|たの}しみにしている。",
      "ok": "{海|うみ}が{好|す}きな{母|はは}のことだから、{今|いま}ごろはハワイで{楽|たの}しんでいるだろう。",
      "th": "After のことだから: the speaker's GUESS (だろう), not a plain report."
     }
    ],
    "check": [
     {
      "q": "{栄養士|えいようし}の{彼女|かのじょ}のことだから、{食|た}べ{物|もの}には{十分|じゅうぶん}（　　）。",
      "opts": [
       "{気|き}をつけている",
       "{気|き}をつけてほしい",
       "{気|き}をつけているはずだ"
      ],
      "ans": 2,
      "explain": "Guess → はずだ.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～のことだから",
   "meaning": "～の{性格|せいかく}や{普段|ふだん}の{態度|たいど}から{考|かんが}えると、あることが{推量|すいりょう}される。",
   "explain": [
    "のことだから = thinking from ～'s character or usual behaviour, something can be guessed.",
    "Shape: Noun + のことだから.",
    "Kavanam: mostly after words for people. After it comes the speaker's guess or judgement. Can be used at the end of a sentence as in ③."
   ],
   "examples": [
    {
     "t": "①{頑張|がんば}り{屋|や}のみち{子|こ}[[のことだから]]、きっと{今度|こんど}のテストでもいい{点|てん}をとりますよ。",
     "explain": "頑張り屋 = hard worker."
    },
    {
     "t": "②いつもみんなを{笑|わら}わせていたカンさん[[のことだから]]、{国|くに}に{帰|かえ}ってもまた{人気者|にんきもの}になると{思|おも}いますよ。",
     "explain": "人気者 = popular person."
    },
    {
     "t": "③{太郎|たろう}の{帰|かえ}りが{遅|おそ}いね。でも、あの{子|こ}[[のことだ]]。どこかの{本屋|ほんや}で{立|た}ち{読|よ}みでもして{時間|じかん}が{経|た}つのを{忘|わす}れているんだろう。",
     "explain": "Sentence-final のことだ."
    }
   ],
   "form": "［名］　＋のことだから",
   "caution": "{主|おも}に{人|ひと}を{表|あらわ}す{言葉|ことば}につく。{後|あと}には、{話者|わしゃ}の{推量|すいりょう}・{判断|はんだん}などを{表|あらわ}す{文|ぶん}が{来|く}る。③のように{文末|ぶんまつ}に{使|つか}うこともある。"
  },
  {
   "type": "grammar",
   "no": "8",
   "id": "d9b-g8",
   "teach": {
    "intro": [
     "だけに = 'precisely because ～, (naturally / even more) …'.",
     "'Famous restaurant-aa irukkradhaala dhaan, food problem periya news aachu.'",
     "年が年だけに = 'because of his age (it's not normal)'. No requests after it."
    ],
    "pattern": "［名詞］・{普通形|ふつうけい}（［な形容詞］だ→な／である・［名詞］→である）＋だけに　＊［名詞］だ の形には接続しない",
    "examples": [
     {
      "jp": "{期待|きたい}していただけに、がっかりした。",
      "th": "Romba expect pannadhaala dhaan, romba disappointment.",
      "kana": "きたいしていただけに、がっかりした。"
     },
     {
      "jp": "ベテランだけに、{仕事|しごと}が{速|はや}い。",
      "th": "Experienced aal dhaan, so velai fast.",
      "kana": "ベテランだけに、しごとがはやい。"
     },
     {
      "jp": "{高|たか}かっただけに、{大切|たいせつ}に{使|つか}っている。",
      "th": "Vilai adhigam dhaan, so careful-aa use panren.",
      "kana": "たかかっただけに、たいせつにつかっている。"
     }
    ],
    "wrong": [
     {
      "ng": "{彼|かれ}はクラスのリーダーだけに、{頑張|がんば}ってもらおう。",
      "ok": "{彼|かれ}はクラスのリーダーだけに、{責任|せきにん}が{重|おも}い。",
      "th": "No request after だけに. State the natural degree/state."
     }
    ],
    "check": [
     {
      "q": "{田中|たなか}{君|くん}は{海|うみ}に{近|ちか}い{村|むら}で{育|そだ}っただけに、（　　）。",
      "opts": [
       "{魚|さかな}の{名前|なまえ}をよく{知|し}っている",
       "{魚|さかな}の{名前|なまえ}はあまり{知|し}らない",
       "{海|うみ}のお{土産|みやげ}を{持|も}ってきてくれた"
      ],
      "ans": 0,
      "explain": "Natural result of growing up by the sea.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～だけに",
   "meaning": "～だから、ある{状態|じょうたい}なのは{当然|とうぜん}だ・{普通|ふつう}の{場合|ばあい}よりもっとある{状態|じょうたい}になる。",
   "explain": [
    "だけに = because of ～, being in a certain state is natural; or it is even more so than usual.",
    "Shape: Noun / plain form (な-adj ~~だ~~ → な / である, Noun → である) + だけに. (No 'Noun だ' form.)",
    "Kavanam: after it comes a sentence of the degree/state that fits the reason ～. No request sentence. ④「～が～だけに」 = because the degree of ～ is not ordinary."
   ],
   "examples": [
    {
     "t": "①あそこは{有名|ゆうめい}レストラン[[だけに]]、{客|きゃく}に{出|だ}した{料理|りょうり}に{問題|もんだい}があったとわかったときは{大|だい}ニュースになった。",
     "explain": "Famous → big news."
    },
    {
     "t": "②{母|はは}は{花|はな}が{好|す}きな[[だけに]]、{花|はな}をもらうと{大喜|おおよろこ}びする。",
     "explain": "Even more happy."
    },
    {
     "t": "③{父|ちち}はよく{話|はな}す{人|ひと}だった[[だけに]]、いなくなった{後|あと}、いっそう{寂|さび}しさを{感|かん}じる。",
     "explain": "いっそう = all the more."
    },
    {
     "t": "④{祖父|そふ}はよく{山登|やまのぼ}りをするが、{年|とし}が{年|とし}[[だけに]]、{無事|ぶじ}に{帰|かえ}ってくるまで{心配|しんぱい}だ。",
     "explain": "年が年だけに = given his age."
    }
   ],
   "form": "［名］・{普通形|ふつうけい}（［ナ形］だ－な／－である・［名］－である）　＋だけに　＊［名］だ　の{形|けい}には{接続|せつぞく}しない。",
   "caution": "{後|あと}には、「～」という{理由|りゆう}にふさわしい{程度|ていど}や{状態|じょうたい}を{表|あらわ}す{文|ぶん}が{来|く}る。{働|はたら}きかけの{文|ぶん}は{来|こ}ない。④の「～が～だけに」は、「～の{程度|ていど}が{普通|ふつう}ではないから」という{意味|いみ}の{言|い}い{方|かた}。"
  },
  {
   "type": "grammar",
   "no": "9",
   "id": "d9b-g9",
   "teach": {
    "intro": [
     "ばかりに = 'just because of ～ (one small thing), something bad happened'. Regret feeling.",
     "'Saavi marandhu poitten — adhunaala dhaan family vara varaikkum veliya nikka vendiyadhaa pochu.'",
     "～たいばかりに = 'wanting ～ so badly that (did something extreme)'."
    ],
    "pattern": "{普通形|ふつうけい}（［な形容詞］だ→な／である・［名詞］だ→である）＋ばかりに",
    "examples": [
     {
      "jp": "うそをついたばかりに、{信用|しんよう}をなくした。",
      "th": "Oru poi sonnadhaala, nambikkai poyiduchu.",
      "kana": "うそをついたばかりに、しんようをなくした。"
     },
     {
      "jp": "{英語|えいご}ができないばかりに、いい{仕事|しごと}に{就|つ}けない。",
      "th": "English theriyaadhadhaala nalla velai kidaikkala.",
      "kana": "えいごができないばかりに、いいしごとにつけない。"
     },
     {
      "jp": "{彼女|かのじょ}に{会|あ}いたいばかりに、{毎日|まいにち}その{店|みせ}に{通|とお}った。",
      "th": "Ava-va paakkanum-nu dhaan daily andha kadaikku ponen.",
      "kana": "かのじょにあいたいばかりに、まいにちそのみせにとおった。"
     }
    ],
    "wrong": [
     {
      "ng": "{外国|がいこく}で、その{国|くに}の{言葉|ことば}が{話|はな}せないばかりに、{外国|がいこく}{語|ご}をしっかり{勉強|べんきょう}しようと{思|おも}った。",
      "ok": "{外国|がいこく}で、その{国|くに}の{言葉|ことば}が{話|はな}せないばかりに、{高|たか}い{買|か}い{物|もの}をしてしまった。",
      "th": "No intention after ばかりに; it shows an unexpected bad result."
     }
    ],
    "check": [
     {
      "q": "バスに（　　）ばかりに、{予定|よてい}の{新幹線|しんかんせん}に{乗|の}れなかった。",
      "opts": [
       "{乗|の}り{遅|おく}れの",
       "{乗|の}り{遅|おく}れて",
       "{乗|の}り{遅|おく}れた"
      ],
      "ans": 2,
      "explain": "Plain past form + ばかりに.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～ばかりに",
   "meaning": "～が{原因|げんいん}で、{予期|よき}しない{悪|わる}い{結果|けっか}になった・どうしても～ということを{実現|じつげん}したいので、{普通|ふつう}ではないことをした。",
   "explain": [
    "ばかりに = because of ～, an unexpected bad result happened; or wanting to make ～ happen so much, did something unusual.",
    "Shape: plain form (な-adj ~~だ~~ → な / である, Noun ~~だ~~ → である) + ばかりに.",
    "Kavanam: ①②③ show that just that one thing caused an unexpected minus result; no wish/intention or request after. ④⑤ with ～たい: after it comes a sentence showing an unusual degree of effort; it need not be a minus thing."
   ],
   "examples": [
    {
     "t": "①ちょっと{大工|だいく}の{経験|けいけん}がある[[ばかりに]]、いろいろな{仕事|しごと}を{頼|たの}まれてしまう。",
     "explain": "Just a little experience → lots of work."
    },
    {
     "t": "②{家|いえ}のかぎを{忘|わす}れて{出|で}かけた[[ばかりに]]、{家族|かぞく}が{帰|かえ}ってくるまで{家|いえ}に{入|い}れなかった。",
     "explain": "Bad result."
    },
    {
     "t": "③{遅刻|ちこく}の{回数|かいすう}がちょっと{多|おお}かった[[ばかりに]]、{推薦状|すいせんじょう}を{書|か}いてもらえなかった。",
     "explain": "推薦状 = recommendation letter."
    },
    {
     "t": "④{山頂|さんちょう}から{一目|ひとめ}{日|ひ}の{出|で}を{見|み}たい[[ばかりに]]、{暗|くら}いうちに{山小屋|やまごや}を{出|で}て2{時間|じかん}も{歩|ある}いたのだ。",
     "explain": "～たいばかりに = desperate wish."
    },
    {
     "t": "⑤テレビで{見|み}たこの{村|むら}の{人|ひと}たちに{会|あ}いたい[[ばかりに]]、はるばる{日本|にほん}からやって{来|き}た。",
     "explain": "はるばる = all the way."
    }
   ],
   "form": "{普通形|ふつうけい}（［ナ形］だ－な／－である・［名］だ－である）　＋ばかりに",
   "caution": "①②③はそれだけのことが{原因|げんいん}で、{予期|よき}しないマイナスの{結果|けっか}になったということを{表|あらわ}す。{後|あと}には、{話者|わしゃ}の{希望|きぼう}・{意向|いこう}を{表|あらわ}す{文|ぶん}や{働|はたら}きかけの{文|ぶん}は{来|こ}ない。④⑤のように{希望|きぼう}を{表|あらわ}す「～たい」につくときは、{後|あと}には、{普通|ふつう}の{程度|ていど}ではないことを{表|あらわ}す{文|ぶん}が{来|く}る。{特|とく}にマイナスのことでなくても{良|よ}い。"
  },
  {
   "type": "grammar",
   "no": "10",
   "id": "d9b-g10",
   "teach": {
    "intro": [
     "からには / 以上(は) / 上は = 'now that ～ / since ～, (of course) must / will …'.",
     "'Japan-ku padikka vandhaachu-naa, oru clear goal irukkanum.'",
     "After it: judgement, wish, intention, request (～なければならない, ～べきだ, ～つもりだ, ～てください)."
    ],
    "pattern": "{普通形|ふつうけい}（［な形容詞］だ→である・［名詞］だ→である）＋からには・以上（は）　／　［動詞］辞書形／た形＋上は",
    "examples": [
     {
      "jp": "やると{言|い}ったからには、{最後|さいご}までやる。",
      "th": "Seiyren-nu sonnaachu, kadaisi varaikkum seivEn.",
      "kana": "やるといったからには、さいごまでやる。"
     },
     {
      "jp": "{学生|がくせい}である{以上|いじょう}、{勉強|べんきょう}するべきだ。",
      "th": "Student-aa irukkra varaikkum, padikkanum.",
      "kana": "がくせいであるいじょう、べんきょうするべきだ。"
     },
     {
      "jp": "{決|き}めた{上|うえ}は、{後悔|こうかい}しない。",
      "th": "Mudivu panniyaachu, regret illa.",
      "kana": "きめたうえは、こうかいしない。"
     }
    ],
    "wrong": [
     {
      "ng": "A{社|しゃ}の{社長|しゃちょう}が{来|く}るからには、うちの{社長|しゃちょう}は{緊張|きんちょう}している。",
      "ok": "A{社|しゃ}の{社長|しゃちょう}が{来|く}るからには、{我々|われわれ}もしっかり{準備|じゅんび}をしよう。",
      "th": "After からには: judgement/intention/request, not a description."
     }
    ],
    "check": [
     {
      "q": "{子供|こども}を{預|あず}かる{上|うえ}は、（　　）。",
      "opts": [
       "{責任|せきにん}を{持|も}たなければならない",
       "{楽|たの}しくなると{思|おも}う",
       "いろいろ{準備|じゅんび}をした"
      ],
      "ans": 0,
      "explain": "Natural duty → なければならない.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～からには・～{以上|いじょう}（は）・～{上|うえ}は",
   "meaning": "～のだから、あることをするのは{当然|とうぜん}だ・あることをしてほしい・あることをするつもりだ。",
   "explain": [
    "からには・以上(は)・上は = since ～, it's natural to do something / I want something done / I intend to do something.",
    "Shape: plain form (な-adj ~~だ~~ → である, Noun ~~だ~~ → である) + からには・以上(は); Verb dictionary / た-form + 上は.",
    "Kavanam: the whole sentence expresses what is generally thought natural. After it comes the speaker's judgement, wish, intention, or a request."
   ],
   "examples": [
    {
     "t": "①{留学|りゅうがく}する[[からには]]、ちゃんと{目的|もくてき}があるのでしょうね。",
     "explain": "Judgement."
    },
    {
     "t": "②{高|たか}いお{金|かね}を{払|はら}って{外国|がいこく}{旅行|りょこう}をする[[からには]]、{大|おお}いに{楽|たの}しまなければ{損|そん}だ。",
     "explain": "損 = loss."
    },
    {
     "t": "③{自分|じぶん}{一人|ひとり}でやると{言|い}った[[{以上|いじょう}]]、みんなに{助|たす}けてもらうことはできない。",
     "explain": "以上 = since."
    },
    {
     "t": "④{専門職|せんもんしょく}である[[{以上|いじょう}は]]、{常|つね}に{新|あたら}しい{知識|ちしき}を{身|み}につけなければならないと{思|おも}う。",
     "explain": "専門職 = professional job."
    },
    {
     "t": "⑤オリンピック{出場|しゅつじょう}を{目指|めざ}す[[{上|うえ}は]]、{中途半端|ちゅうとはんぱ}な{気持|きも}ちではだめだ。",
     "explain": "中途半端 = half-hearted."
    },
    {
     "t": "⑥{会社|かいしゃ}を{辞|や}めると{決|き}めた[[{上|うえ}は]]、{覚悟|かくご}して{今後|こんご}のことを{考|かんが}える{必要|ひつよう}がある。",
     "explain": "覚悟 = be prepared."
    }
   ],
   "form": "{普通形|ふつうけい}（［ナ形］だ－である・［名］だ－である）　＋からには・{以上|いじょう}（は）　／　［動］{辞書形|じしょけい}／た{形|けい}　＋{上|うえ}は",
   "caution": "{文|ぶん}{全体|ぜんたい}で、{一般|いっぱん}{的|てき}に{当然|とうぜん}と{思|おも}われることを{表|あらわ}す。{後|あと}には、{話者|わしゃ}の{判断|はんだん}・{希望|きぼう}・{意向|いこう}などを{表|あらわ}す{文|ぶん}や{働|はたら}きかけの{文|ぶん}が{来|く}る。"
  },
  {
   "type": "group",
   "title": "【1】（～ことだし）",
   "children": [
    {
     "type": "mcq",
     "id": "d9b-17-1-1",
     "q": "1　{出発|しゅっぱつ}まで{時間|じかん}も{十分|じゅうぶん}（　　）ことだし、ロビーでちょっとお{茶|ちゃ}でも{飲|の}みませんか。",
     "opts": [
      "ある",
      "あります",
      "あるの"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Plain form + ことだし."
    },
    {
     "type": "mcq",
     "id": "d9b-17-1-2",
     "q": "2　{今週|こんしゅう}は{忙|いそが}しかったことだし、（　　）。",
     "opts": [
      "とても{疲|つか}れた",
      "メールもできなかった",
      "{週末|しゅうまつ}はゆっくり{休|やす}みたい"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Wish after ことだし."
    },
    {
     "type": "mcq",
     "id": "d9b-17-1-3",
     "q": "3　このベッドは{品質|ひんしつ}もいいことだし、（　　）。",
     "opts": [
      "{値段|ねだん}が{高|たか}い",
      "これを{買|か}うことにしよう",
      "よく{売|う}れた"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Decision after ことだし."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【2】（～のことだから）",
   "children": [
    {
     "type": "mcq",
     "id": "d9b-17-2-1",
     "q": "1　{海|うみ}が{好|す}きな{母|はは}のことだから、（　　）。",
     "opts": [
      "{今|いま}ごろはハワイで{楽|たの}しんでいるだろう",
      "{海|うみ}で{遊|あそ}ぶのをとても{楽|たの}しみにしている",
      "{海|うみ}に{行|い}けて{良|よ}かったと{言|い}っている"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Guess → だろう."
    },
    {
     "type": "mcq",
     "id": "d9b-17-2-2",
     "q": "2　{厳|きび}しい{原田|はらだ}コーチのことだから、（　　）。",
     "opts": [
      "{僕|ぼく}たちはとても{緊張|きんちょう}した",
      "{試合|しあい}に{負|ま}けたらきっとすごく{怒|おこ}るよ",
      "{僕|ぼく}は{試合|しあい}には{負|ま}けたくないよ"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Guess about the coach → きっと怒るよ."
    },
    {
     "type": "mcq",
     "id": "d9b-17-2-3",
     "q": "3　{栄養士|えいようし}の{彼女|かのじょ}のことだから、{食|た}べ{物|もの}には{十分|じゅうぶん}（　　）。",
     "opts": [
      "{気|き}をつけている",
      "{気|き}をつけてほしい",
      "{気|き}をつけているはずだ"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Guess → はずだ."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【3】（～だけに）",
   "children": [
    {
     "type": "mcq",
     "id": "d9b-17-3-1",
     "q": "1　みんなに{期待|きたい}されているだけに、（　　）。",
     "opts": [
      "いい{作品|さくひん}ができるように{頑張|がんば}れ",
      "いい{作品|さくひん}ができるかどうか{心配|しんぱい}だ",
      "いい{作品|さくひん}ができなかった"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Natural state: worried, because of expectations. No command."
    },
    {
     "type": "mcq",
     "id": "d9b-17-3-2",
     "q": "2　{彼|かれ}はクラスのリーダーだけに、（　　）。",
     "opts": [
      "わたしは{彼|かれ}が{好|す}きだ",
      "{頑張|がんば}ってもらおう",
      "{責任|せきにん}が{重|おも}い"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Natural state for a leader."
    },
    {
     "type": "mcq",
     "id": "d9b-17-3-3",
     "q": "3　{彼|かれ}は{営業|えいぎょう}の{仕事|しごと}をしているだけに、（　　）。",
     "opts": [
      "ほかの{人|ひと}より{話|はな}すのが{上手|じょうず}だ",
      "{営業|えいぎょう}マンと{呼|よ}ばれている",
      "{外回|そとまわ}りの{仕事|しごと}をする"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "More than usual: better at talking."
    },
    {
     "type": "mcq",
     "id": "d9b-17-3-4",
     "q": "4　{田中|たなか}{君|くん}は{海|うみ}に{近|ちか}い{村|むら}で{育|そだ}っただけに、（　　）。",
     "opts": [
      "{魚|さかな}の{名前|なまえ}をよく{知|し}っている",
      "{魚|さかな}の{名前|なまえ}はあまり{知|し}らない",
      "{海|うみ}のお{土産|みやげ}を{持|も}ってきてくれた"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Natural result."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【4】（～ばかりに）",
   "children": [
    {
     "type": "mcq",
     "id": "d9b-17-4-1",
     "q": "1　バスに（　　）ばかりに、{予定|よてい}の{新幹線|しんかんせん}に{乗|の}れなかった。",
     "opts": [
      "{乗|の}り{遅|おく}れの",
      "{乗|の}り{遅|おく}れて",
      "{乗|の}り{遅|おく}れた"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Plain form + ばかりに."
    },
    {
     "type": "mcq",
     "id": "d9b-17-4-2",
     "q": "2　{木村|きむら}{氏|し}は{記者|きしゃ}{会見|かいけん}の{時|とき}、{一言|ひとこと}{多|おお}かったばかりに、（　　）。",
     "opts": [
      "{信用|しんよう}をなくしてしまった",
      "すっかり{人気者|にんきもの}になった",
      "すぐに{言|い}い{直|なお}した"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Unexpected bad result."
    },
    {
     "type": "mcq",
     "id": "d9b-17-4-3",
     "q": "3　{外国|がいこく}で、その{国|くに}の{言葉|ことば}が{話|はな}せないばかりに、（　　）。",
     "opts": [
      "ガイドを{頼|たの}んで{通訳|つうやく}してもらった",
      "{外国|がいこく}{語|ご}をしっかり{勉強|べんきょう}しようと{思|おも}った",
      "{高|たか}い{買|か}い{物|もの}をしてしまった"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Unexpected bad result."
    },
    {
     "type": "mcq",
     "id": "d9b-17-4-4",
     "q": "4　{弟|おとうと}はジェットコースターに{乗|の}りたいばかりに、（　　）そうだ。",
     "opts": [
      "{遊園|ゆうえん}{地|ち}が{好|す}きなのだ",
      "どの{遊園|ゆうえん}{地|ち}がいいか{考|かんが}えている",
      "2{時間|じかん}も{並|なら}んで{待|ま}った"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "～たいばかりに → unusual effort."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【5】（～からには・～{以上|いじょう}（は）・～{上|うえ}は）",
   "children": [
    {
     "type": "mcq",
     "id": "d9b-17-5-1",
     "q": "1　A{社|しゃ}の{社長|しゃちょう}が{来|く}るからには、（　　）。",
     "opts": [
      "{一緒|いっしょ}にゴルフをしよう",
      "{我々|われわれ}もしっかり{準備|じゅんび}をしよう",
      "うちの{社長|しゃちょう}は{緊張|きんちょう}している"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Natural intention: we must prepare properly."
    },
    {
     "type": "mcq",
     "id": "d9b-17-5-2",
     "q": "2　{君|きみ}がそこまで{言|い}うからには、（　　）。",
     "opts": [
      "{何|なに}か{理由|りゆう}があるんだろうね",
      "{僕|ぼく}はわかったよ",
      "みんなが{理解|りかい}できたよ"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Judgement: there must be a reason."
    },
    {
     "type": "mcq",
     "id": "d9b-17-5-3",
     "q": "3　{入館|にゅうかん}{料|りょう}を1,000{円|えん}{払|はら}った{以上|いじょう}、（　　）。",
     "opts": [
      "おつりをもらえませんか",
      "しっかり{見学|けんがく}しよう",
      "さあ、{入館|にゅうかん}できる"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Intention: see everything properly."
    },
    {
     "type": "mcq",
     "id": "d9b-17-5-4",
     "q": "4　{子供|こども}を{預|あず}かる{上|うえ}は、（　　）。",
     "opts": [
      "{責任|せきにん}を{持|も}たなければならない",
      "{楽|たの}しくなると{思|おも}う",
      "いろいろ{準備|じゅんび}をした"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Duty → なければならない."
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
     "id": "d9b-17-6-1",
     "q": "1　この{町|まち}は{人口|じんこう}が{少|すく}ない（　　）、{個人|こじん}{的|てき}なことがみんなに{知|し}られてしまう。",
     "opts": [
      "ことだから",
      "{以上|いじょう}は",
      "だけに"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Natural result of a small town → だけに."
    },
    {
     "type": "mcq",
     "id": "d9b-17-6-2",
     "q": "2　{外|そと}は{寒|さむ}い（　　）、{建物|たてもの}の{中|なか}でタクシーが{来|く}るのを{待|ま}ちましょう。",
     "opts": [
      "だけに",
      "ことだし",
      "からには"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Invitation → ことだし."
    },
    {
     "type": "mcq",
     "id": "d9b-17-6-3",
     "q": "3　{大|おお}きな{仕事|しごと}を{引|ひ}き{受|う}けた（　　）、{最後|さいご}まで{頑張|がんば}らなければいけない。",
     "opts": [
      "だけに",
      "ばかりに",
      "からには"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Duty → からには."
    },
    {
     "type": "mcq",
     "id": "d9b-17-6-4",
     "q": "4　{彼女|かのじょ}はモデルになりたい（　　）、{無理|むり}なダイエットをしているそうだ。",
     "opts": [
      "ばかりに",
      "からには",
      "ことだし"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "～たいばかりに → extreme diet."
    },
    {
     "type": "mcq",
     "id": "d9b-17-6-5",
     "q": "5　ここは{禁煙|きんえん}{席|せき}（　　）、ここでのおたばこはご{遠慮|えんりょ}{願|ねが}います。",
     "opts": [
      "のことだから",
      "ですので",
      "だけに"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Polite reason: ですので. のことだから is for people."
    }
   ],
   "scored": true
  }
 ]
});
