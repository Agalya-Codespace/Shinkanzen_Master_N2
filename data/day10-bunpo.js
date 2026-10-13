/* Day 10 · bunpo. Built from d10_bunpo.py by tools/build_day.py (furigana added automatically). */
window.N2_DAYS = window.N2_DAYS || {};
window.N2_DAYS[10] = window.N2_DAYS[10] || {"title": "", "intro": "", "sections": []};
if (false) window.N2_DAYS[10].title = "";
if (false) window.N2_DAYS[10].intro = "";
window.N2_DAYS[10].sections.push({
 "book": "bunpo",
 "title": "Ⅱ {主観|しゅかん}を{含|ふく}めて{説明|せつめい}する☆☆　18{課|か} ～できない・{困難|こんなん}だ・～できる／19{課|か} ～を{見|み}て{評価|ひょうか}すると・～の{立場|たちば}で{評価|ひょうか}すると",
 "source": "新完全マスター文法 N2 · 第1部 文の文法1 · pp.82–89 · answers from 別冊 解答 p.5",
 "blocks": [
  {
   "type": "items",
   "title": "18{課|か}　〔{復習|ふくしゅう}〕",
   "items": [
    {
     "t": "・あの{人|ひと}の{話|はなし}は{信|しん}じ[[られない]]。",
     "explain": "Review: potential negative = can't."
    },
    {
     "t": "・この{文|ぶん}は{複雑|ふくざつ}でわかり[[にくい]]。",
     "explain": "Review: ～にくい = hard to ～."
    },
    {
     "t": "・{社長|しゃちょう}{室|しつ}に{一人|ひとり}ではちょっと{入|はい}り[[づらい]]ですよ。",
     "explain": "Review: ～づらい = hard to ～ (feeling uneasy)."
    }
   ],
   "explain": "18課 = many ways to say 'can't' (and 'can'): がたい, わけにはいかない, かねる, ようがない, どころではない, 得る/得ない. Each one has a different REASON why you can't."
  },
  {
   "type": "grammar",
   "no": "1",
   "id": "d10b-g1",
   "teach": {
    "intro": [
     "がたい = 'very hard to ～ / can't bring myself to ～'. It is about the HEART, not ability.",
     "'Avlo nalla manushan ippadi seydhaar-nu nambave mudiyala.' → 信じがたい.",
     "Used with verbs of feeling/thinking (信じる・理解する・想像する) and saying (言う・表す)."
    ],
    "pattern": "［動詞］ます形（～~~ます~~）＋がたい",
    "examples": [
     {
      "jp": "{彼|かれ}がうそをついたとは{信|しん}じがたい。",
      "th": "Avan poi sonnaan-nu nambave mudiyala.",
      "kana": "かれがうそをついたとはしんじがたい。"
     },
     {
      "jp": "この{気持|きも}ちは{言葉|ことば}では{表|あらわ}しがたい。",
      "th": "Indha feeling-ai vaarthaigalaal solla mudiyaadhu.",
      "kana": "このきもちはことばではあらわしがたい。"
     },
     {
      "jp": "それは{理解|りかい}しがたい{考|かんが}え{方|かた}だ。",
      "th": "Adhu purinjikka kashtamaana yosanai.",
      "kana": "それはりかいしがたいかんがえかただ。"
     }
    ],
    "wrong": [
     {
      "ng": "うちの{子供|こども}はまだ{歩|ある}きがたい。",
      "ok": "うちの{子供|こども}はまだ{歩|ある}けない。",
      "th": "Ability (a baby can't walk yet) → 歩けない. がたい is never about physical ability."
     }
    ],
    "check": [
     {
      "q": "これは{思|おも}い{出|で}のシャツなので、（　　）がたい。",
      "opts": [
       "{捨|す}てる",
       "{捨|す}て",
       "{捨|す}てて"
      ],
      "ans": 1,
      "explain": "ます-stem: 捨て＋がたい = hard (emotionally) to throw away.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～がたい",
   "meaning": "～することが{難|むずか}しい・～できない。",
   "explain": [
    "がたい = it is hard to ～ / I can't ～ (because of feelings).",
    "Shape: verb ます-stem + がたい.",
    "Kavanam: NOT for ability. Mainly with verbs of the mind (想像する・理解する・信じる) or of saying (言う・表す)."
   ],
   "examples": [
    {
     "t": "①あの{優|やさ}しい{彼|かれ}がそんなひどいことをしたとは{信|しん}じ[[がたい]]。",
     "explain": "Can't believe it (feeling)."
    },
    {
     "t": "②この{料理|りょうり}は{何|なん}とも{言|い}い[[がたい]]{初|はじ}めての{味|あじ}だ。",
     "explain": "何とも言いがたい = hard to put into words."
    },
    {
     "t": "③{留学中|りゅうがくちゅう}、{自分|じぶん}の{国|くに}では{得|え}[[がたい]]{経験|けいけん}をたくさんした。",
     "explain": "{得|え}がたい経験 = a rare experience you can't easily get."
    }
   ],
   "form": "［動］~~ます~~　＋がたい",
   "caution": "{能力|のうりょく}{的|てき}にできないという{意味|いみ}では{使|つか}わない。{主|おも}に{心|こころ}の{働|はたら}きを{表|あらわ}す{動詞|どうし}（{想像|そうぞう}する・{理解|りかい}する・{信|しん}じるなど）や{発言|はつげん}を{表|あらわ}す{動詞|どうし}（{言|い}う・{表|あらわ}すなど）につく。"
  },
  {
   "type": "grammar",
   "no": "2",
   "id": "d10b-g2",
   "teach": {
    "intro": [
     "わけにはいかない = 'I can't (because it isn't right / I'd feel bad)'. Social or moral reason, not ability.",
     "'Ellaarum velai seiyumbodhu naan mattum veetukku poga mudiyaadhu.' — it wouldn't be right.",
     "わけにもいかない = 'can't do THAT either' (other options are also out). Subject is usually I (一人称)."
    ],
    "pattern": "［動詞］辞書形＋わけにはいかない・わけにもいかない",
    "examples": [
     {
      "jp": "{明日|あした}は{試験|しけん}だから、{遊|あそ}びに{行|い}くわけにはいかない。",
      "th": "Naalaikku exam, so velaiyaada poga mudiyaadhu (not right).",
      "kana": "あしたはしけんだから、あそびにいくわけにはいかない。"
     },
     {
      "jp": "{先生|せんせい}の{頼|たの}みだから、{断|ことわ}るわけにはいかない。",
      "th": "Teacher kettadhu, so maatten-nu solla mudiyaadhu.",
      "kana": "せんせいのたのみだから、ことわるわけにはいかない。"
     },
     {
      "jp": "{終電|しゅうでん}がないが、{会社|かいしゃ}に{泊|と}まるわけにもいかない。",
      "th": "Last train illa, aanaa office-la thoongavum mudiyaadhu.",
      "kana": "しゅうでんがないが、かいしゃにとまるわけにもいかない。"
     }
    ],
    "wrong": [
     {
      "ng": "{車|くるま}を{持|も}っていないので、ドライブに{行|い}くわけにはいかない。",
      "ok": "{車|くるま}を{持|も}っていないので、ドライブに{行|い}けない。",
      "th": "No car = physically impossible → 行けない. わけにはいかない needs a social/moral reason (e.g. urgent work)."
     }
    ],
    "check": [
     {
      "q": "みんなが{残|のこ}って{頑張|がんば}っているのだから、わたしだけ（　　）わけにはいかない。",
      "opts": [
       "{帰|かえ}る",
       "{帰|かえ}れる",
       "{帰|かえ}らない"
      ],
      "ans": 0,
      "explain": "Dictionary form: 帰るわけにはいかない.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～わけにはいかない・～わけにもいかない",
   "meaning": "{社会|しゃかい}{的|てき}{常識|じょうしき}に{反|はん}する・{心理|しんり}{的|てき}{抵抗|ていこう}があるなどの{事情|じじょう}があって、～できない。",
   "explain": [
    "わけにはいかない・わけにもいかない = can't, because of social common sense or a feeling of resistance.",
    "Shape: verb dictionary form + わけにはいかない / わけにもいかない.",
    "Kavanam: NOT for ability. The subject is usually 'I'."
   ],
   "examples": [
    {
     "t": "①{病気|びょうき}の{子供|こども}を{一人|ひとり}{家|いえ}において、{仕事|しごと}に{行|い}く[[わけにはいかない]]。",
     "explain": "Can't leave a sick child alone — not right."
    },
    {
     "t": "②いくらお{金|かね}に{困|こま}っていても、そんな{大金|たいきん}をあなたから{借|か}りる[[わけにはいかない]]。",
     "explain": "Pride / feeling bad."
    },
    {
     "t": "③もう{終電|しゅうでん}は{終|お}わってしまった。{会社|かいしゃ}に{泊|と}まる[[わけにもいかず]]、{困|こま}っている。",
     "explain": "わけにもいかず = can't do that either."
    }
   ],
   "form": "［動］{辞書形|じしょけい}　＋わけにはいかない・わけにもいかない",
   "caution": "{能力|のうりょく}{的|てき}にできないという{意味|いみ}では{使|つか}わない。{主語|しゅご}はふつう{一人称|いちにんしょう}。"
  },
  {
   "type": "grammar",
   "no": "3",
   "id": "d10b-g3",
   "teach": {
    "intro": [
     "かねる = 'I'm afraid I can't ～' — a polite refusal in business Japanese.",
     "'Mannikkavum, adhai naanga solla mudiyaadhu.' — shop/office staff talk.",
     "見かねて = couldn't just stand by and watch → so I helped. (Also: 待ちかねる = can't wait any longer.)"
    ],
    "pattern": "［動詞］ます形（～~~ます~~）＋かねる",
    "examples": [
     {
      "jp": "その{質問|しつもん}にはお{答|こた}えしかねます。",
      "th": "Andha kelvikku badhil solla mudiyaadhu (polite).",
      "kana": "そのしつもんにはおこたえしかねます。"
     },
     {
      "jp": "{申|もう}し{訳|わけ}ありませんが、ご{希望|きぼう}には{応|おう}じかねます。",
      "th": "Mannikkavum, ungal request-ai accept panna mudiyaadhu.",
      "kana": "もうしわけありませんが、ごきぼうにはおうじかねます。"
     },
     {
      "jp": "{見|み}るに{見|み}かねて、{手伝|てつだ}った。",
      "th": "Paarthu poruka mudiyaama help panninen.",
      "kana": "みるにみかねて、てつだった。"
     }
    ],
    "wrong": [
     {
      "ng": "{風邪|かぜ}を{引|ひ}いたので、{学校|がっこう}に{行|い}きかねます。",
      "ok": "{風邪|かぜ}を{引|ひ}いたので、{学校|がっこう}に{行|い}けません。",
      "th": "Being ill = simply can't → 行けません. かねる is a polite 'I can't (in my position)'."
     }
    ],
    "check": [
     {
      "q": "せっかくですが、この{仕事|しごと}は（　　）かねます。",
      "opts": [
       "{引|ひ}き{受|う}ける",
       "{引|ひ}き{受|う}け",
       "{引|ひ}き{受|う}けられ"
      ],
      "ans": 1,
      "explain": "ます-stem: 引き受け＋かねます.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～かねる",
   "meaning": "その{状況|じょうきょう}・その{条件|じょうけん}・{話者|わしゃ}の{立場|たちば}では～できない。",
   "explain": [
    "かねる = can't ～ in this situation / under these conditions / from my position.",
    "Shape: verb ます-stem + かねる.",
    "Kavanam: NOT for ability. Used for polite refusals."
   ],
   "examples": [
    {
     "t": "①メールでのご{質問|しつもん}だけでは{診断|しんだん}し[[かねます]]。{一度|いちど}{病院|びょういん}にいらっしゃってください。",
     "explain": "Doctor: can't diagnose by e-mail alone."
    },
    {
     "t": "②あなたの{気持|きも}ちも{理解|りかい}できますが、その{案|あん}には{賛成|さんせい}し[[かねます]]。",
     "explain": "Polite disagreement."
    },
    {
     "t": "③{子供|こども}が{泣|な}いているのを{見|み}[[かねて]]、{結局|けっきょく}{宿題|しゅくだい}を{手伝|てつだ}ってやった。",
     "explain": "見かねて = couldn't bear to watch."
    }
   ],
   "form": "［動］~~ます~~　＋かねる",
   "caution": "{能力|のうりょく}{的|てき}にできないという{意味|いみ}では{使|つか}わない。{丁寧|ていねい}に{断|ことわ}る{場合|ばあい}などに{使|つか}う。"
  },
  {
   "type": "grammar",
   "no": "4",
   "id": "d10b-g4",
   "teach": {
    "intro": [
     "ようがない = 'there is no way to ～'. よう = way, method (方法).",
     "'Avan number theriyaadhu, so solla vazhiye illa.' → 知らせようがない.",
     "Second meaning: 'it can't possibly ～' (= はずがない): 迷いようがない = you can't possibly get lost."
    ],
    "pattern": "［動詞］ます形（～~~ます~~）＋ようがない",
    "examples": [
     {
      "jp": "{住所|じゅうしょ}がわからないので、{手紙|てがみ}の{出|だ}しようがない。",
      "th": "Address theriyaadhu, letter anuppa vazhiye illa.",
      "kana": "じゅうしょがわからないので、てがみのだしようがない。"
     },
     {
      "jp": "{壊|こわ}れてしまった{物|もの}は{直|なお}しようがない。",
      "th": "Udainjadhai sari panna vazhi illa.",
      "kana": "こわれてしまったものはなおしようがない。"
     },
     {
      "jp": "こんなに{簡単|かんたん}なら、{間違|まちが}えようがない。",
      "th": "Ivlo easy-na thappu panna vaaippe illa.",
      "kana": "こんなにかんたんなら、まちがえようがない。"
     }
    ],
    "wrong": [
     {
      "ng": "{日本語|にほんご}の{勉強|べんきょう}を{始|はじ}めたばかりのトムさんには、{難|むずか}しい{漢字|かんじ}の{書|か}きようがないだろう。",
      "ok": "{日本語|にほんご}の{勉強|べんきょう}を{始|はじ}めたばかりのトムさんには、{難|むずか}しい{漢字|かんじ}は{書|か}けないだろう。",
      "th": "Lack of ability → 書けない. ようがない means there is no means/way at all."
     }
    ],
    "check": [
     {
      "q": "{東京|とうきょう}は{人|ひと}が{多|おお}いので、{渋滞|じゅうたい}や{混雑|こんざつ}は（　　）ようがない。",
      "opts": [
       "{避|さ}ける",
       "{避|さ}け",
       "{避|さ}けられ"
      ],
      "ans": 1,
      "explain": "ます-stem: 避け＋ようがない.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～ようがない",
   "meaning": "～したくても、どのようにしたらいいかわからない・{可能|かのう}{性|せい}が{全|まった}くない。",
   "explain": [
    "ようがない = there's no way to ～ / it can't possibly ～.",
    "Shape: verb ます-stem + ようがない. (Noun + の + しようがない is also seen: 連絡のしようがない.)",
    "Kavanam: used for 'no method at all' or for 'はずがない'. It stresses that it's impossible."
   ],
   "examples": [
    {
     "t": "①{彼|かれ}の{連絡先|れんらくさき}がわからないので、このニュースを{知|し}らせたくても{知|し}らせ[[ようがない]]。",
     "explain": "No means."
    },
    {
     "t": "②{実力|じつりょく}はあるのだから、{今回|こんかい}の{結果|けっか}には{運|うん}がなかったとしか{言|い}い[[ようがない]]。",
     "explain": "～としか言いようがない = can only say ～."
    },
    {
     "t": "③{選手|せんしゅ}たちの{今日|きょう}の{試合|しあい}での{活躍|かつやく}はとても{素晴|すば}らしく、{文句|もんく}のつけ[[ようがない]]。",
     "explain": "No way to complain = perfect."
    },
    {
     "t": "④{駅|えき}からここまではまっすぐ{歩|ある}いてくるだけだから、{迷|まよ}い[[ようがない]]と{思|おも}うけどね。",
     "explain": "= 迷うはずがない."
    },
    {
     "t": "⑤これだけしっかり{準備|じゅんび}したのだ。{悪|わる}い{結果|けっか}になり[[ようがない]]だろう。",
     "explain": "= なるはずがない."
    }
   ],
   "form": "［動］~~ます~~　＋ようがない",
   "caution": "{方法|ほうほう}が{全|まった}くないという{意味|いみ}、または「～はずがない」という{意味|いみ}で{使|つか}う。{不可能|ふかのう}であるというニュアンスを{強調|きょうちょう}する。"
  },
  {
   "type": "grammar",
   "no": "5",
   "id": "d10b-g5",
   "teach": {
    "intro": [
     "どころではない = 'this is no time for ～ / ～ is out of the question'.",
     "'Velai romba, trip-ai pathi yosikkave neram illa.' → 旅行どころではない.",
     "Reason: no money, no time, too noisy, sick… so the thing you hoped for is totally impossible. (Compare 12課 ～どころか.)"
    ],
    "pattern": "［名詞］・［動詞］辞書形＋どころではない",
    "examples": [
     {
      "jp": "{試験|しけん}の{前|まえ}で、{遊|あそ}ぶどころではない。",
      "th": "Exam munnaadi, velaiyaada neram illave illa.",
      "kana": "しけんのまえで、あそぶどころではない。"
     },
     {
      "jp": "{熱|ねつ}があって、{仕事|しごと}どころではない。",
      "th": "Kaaichal, velai paakkura nilamai illa.",
      "kana": "ねつがあって、しごとどころではない。"
     },
     {
      "jp": "{忙|いそが}しくて、{昼|ひる}ご{飯|はん}どころではなかった。",
      "th": "Busy-aa irundhadhaala lunch-kooda saapida mudiyala.",
      "kana": "いそがしくて、ひるごはんどころではなかった。"
     }
    ],
    "wrong": [
     {
      "ng": "のどが{痛|いた}くて、{薬|くすり}を{飲|の}むどころではない。",
      "ok": "のどが{痛|いた}くて、カラオケで{歌|うた}うどころではない。",
      "th": "どころではない is for the enjoyable thing you'd like to do (karaoke), not the medicine you need."
     }
    ],
    "check": [
     {
      "q": "（　　）、{仕事|しごと}どころではない。",
      "opts": [
       "{内容|ないよう}が{難|むずか}しくて",
       "{熱|ねつ}があって",
       "{給料|きゅうりょう}が{安|やす}くて"
      ],
      "ans": 1,
      "explain": "Situation with no room (illness) → 熱があって.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～どころではない",
   "meaning": "～できる{状況|じょうきょう}ではない。",
   "explain": [
    "どころではない = not in a situation where ～ is possible.",
    "Shape: Noun / verb dictionary form + どころではない.",
    "Kavanam: because of a situation with no room (no money, no time, noise, illness…), the expected or imagined thing is completely impossible."
   ],
   "examples": [
    {
     "t": "①{仕事|しごと}が{忙|いそが}しくて、{旅行|りょこう}[[どころではない]]。",
     "explain": "No time."
    },
    {
     "t": "②{隣|となり}のテーブルの{人|ひと}たちがうるさくて、ゆっくり{食事|しょくじ}を{楽|たの}しむ[[どころではなかった]]。",
     "explain": "Too noisy."
    },
    {
     "t": "③{当時|とうじ}はお{金|かね}がなかったのでどこかへ{遊|あそ}びに{行|い}く[[どころではなく]]、{毎日|まいにち}アルバイトをしていた。",
     "explain": "No money."
    }
   ],
   "form": "［名］・［動］{辞書形|じしょけい}　＋どころではない",
   "caution": "{余裕|よゆう}がないという{事情|じじょう}（お{金|かね}がない・{時間|じかん}がない・うるさい・{病気|びょうき}など）のため、{期待|きたい}していることや{想像|そうぞう}していることが{全|まった}くできないという{意味|いみ}で{使|つか}う。"
  },
  {
   "type": "grammar",
   "no": "6",
   "id": "d10b-g6",
   "teach": {
    "intro": [
     "{得|う}る = 'can happen / is possible'; {得|え}ない = 'can't happen / impossible'.",
     "'Yaarukkum varalaam.' → だれにでも起こり{得|う}る. 'Saathiyame illa.' → あり{得|え}ない.",
     "Reading: positive 得る = うる (also える); negative is always えない."
    ],
    "pattern": "［動詞］ます形（～~~ます~~）＋{得|う}る・{得|え}ない",
    "examples": [
     {
      "jp": "{事故|じこ}はどこでも{起|お}こり{得|え}る。",
      "th": "Accident engeyum nadakkalaam.",
      "kana": "じこはどこでもおこりえる。"
     },
     {
      "jp": "そんなことはあり{得|え}ない。",
      "th": "Appadi nadakkave mudiyaadhu.",
      "kana": "そんなことはありえない。"
     },
     {
      "jp": "{考|かんが}え{得|え}る{方法|ほうほう}はすべて{試|ため}した。",
      "th": "Yosikka mudinja ella vazhiyum try panniyaachu.",
      "kana": "かんがええるほうほうはすべてためした。"
     }
    ],
    "wrong": [
     {
      "ng": "この{子|こ}はまだ{字|じ}を{読|よ}み{得|え}ない。",
      "ok": "この{子|こ}はまだ{字|じ}が{読|よ}めない。",
      "th": "A person's everyday ability → 読めない. 得る/得ない is about possibility, not skill."
     }
    ],
    "check": [
     {
      "q": "{危機|きき}はチャンスにも（　　）{得|う}る。",
      "opts": [
       "なる",
       "なり",
       "なれ"
      ],
      "ans": 1,
      "explain": "ます-stem: なり＋得る.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～{得|う}る／～{得|え}ない",
   "meaning": "～できる・その{可能|かのう}{性|せい}がある／～できない・その{可能|かのう}{性|せい}がない。",
   "explain": [
    "得る / 得ない = can / is possible ↔ can't / is impossible.",
    "Shape: verb ます-stem + 得る・得ない.",
    "Kavanam: awkward for a particular person's everyday ability (英語が話せる) or situational possibility (酒を飲んでいないから運転できる). Positive 得る can be read える or うる; as a helper verb it is usually うる. Negative = えない."
   ],
   "examples": [
    {
     "t": "①がんはだれでもかかり[[{得|う}る]]{病気|びょうき}だ。",
     "explain": "Anyone can get it."
    },
    {
     "t": "②{経済|けいざい}の{成長|せいちょう}と{環境|かんきょう}{保護|ほご}は{両立|りょうりつ}し[[{得|う}る]]はずだ。",
     "explain": "両立する = both can exist together."
    },
    {
     "t": "③{人間|にんげん}が100メートルを5{秒|びょう}で{走|はし}るなんてあり[[{得|え}ない]]{話|はなし}だ。",
     "explain": "あり得ない = impossible."
    }
   ],
   "form": "［動］~~ます~~　＋{得|う}る・{得|え}ない",
   "caution": "{特定|とくてい}の{人|ひと}の{日常|にちじょう}{的|てき}な{能力|のうりょく}（{例|れい}：{英語|えいご}が{話|はな}せる）や{状況|じょうきょう}{的|てき}{可能|かのう}（{例|れい}：{酒|さけ}を{飲|の}んでいないから{運転|うんてん}できる）について{言|い}うときは{使|つか}いにくい。「{得|え}る（{肯定|こうてい}{形|がた}）」は「える・うる」の{二|ふた}つの{読|よ}み{方|かた}があるが、ここでの{使|つか}い{方|かた}（{補助|ほじょ}{動詞|どうし}）では「うる」と{読|よ}むことが{多|おお}い。{否定|ひてい}{形|がた}は「えない」。"
  },
  {
   "type": "group",
   "title": "【1】（～がたい）",
   "children": [
    {
     "type": "mcq",
     "id": "d10b-18-1-1",
     "q": "1　これは{思|おも}い{出|で}のシャツなので、（　　）がたい。",
     "opts": [
      "{捨|す}てる",
      "{捨|す}て",
      "{捨|す}てて"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "ます-stem + がたい."
    },
    {
     "type": "mcq",
     "id": "d10b-18-1-2",
     "q": "2　うちの{子供|こども}はまだ（　　）。",
     "opts": [
      "{歩|ある}きがたい",
      "{歩|ある}きにくい",
      "{歩|ある}けない"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Ability → 歩けない."
    },
    {
     "type": "mcq",
     "id": "d10b-18-1-3",
     "q": "3　この{靴|くつ}は（　　）。",
     "opts": [
      "{歩|ある}きがたい",
      "{歩|ある}きにくい",
      "{歩|ある}けない"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Physically hard (shoes) → 歩きにくい. がたい is for feelings."
    },
    {
     "type": "mcq",
     "id": "d10b-18-1-4",
     "q": "4　みんなの{信頼|しんらい}を{裏切|うらぎ}るなんて、（　　）ことだ。",
     "opts": [
      "{許|ゆる}しがたい",
      "{許|ゆる}しにくい",
      "{許|ゆる}しづらい"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Moral feeling: can't forgive → 許しがたい."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【2】（～わけにはいかない・～わけにもいかない）",
   "children": [
    {
     "type": "mcq",
     "id": "d10b-18-2-1",
     "q": "1　みんなが{残|のこ}って{頑張|がんば}っているのだから、わたしだけ（　　）わけにはいかない。",
     "opts": [
      "{帰|かえ}る",
      "{帰|かえ}れる",
      "{帰|かえ}らない"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Dictionary form."
    },
    {
     "type": "mcq",
     "id": "d10b-18-2-2",
     "q": "2　（　　）ので、{今週|こんしゅう}{末|まつ}はドライブに{行|い}くわけにはいかない。",
     "opts": [
      "{急|いそ}ぎの{仕事|しごと}を{頼|たの}まれた",
      "{天気|てんき}が{悪|わる}そうな",
      "{車|くるま}を{持|も}っていない"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Social reason (urgent work) → わけにはいかない. No car = can't (ability)."
    },
    {
     "type": "mcq",
     "id": "d10b-18-2-3",
     "q": "3　（　　）ので、{早|はや}く{結婚|けっこん}したくてもするわけにはいかないんです。",
     "opts": [
      "まだ{相手|あいて}がいない",
      "{一人|ひとり}でいるのが{好|す}きな",
      "まだ{仕事|しごと}が{決|き}まらない"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "No job yet → not right to marry. No partner = simply impossible."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【3】（～かねる）",
   "children": [
    {
     "type": "mcq",
     "id": "d10b-18-3-1",
     "q": "1　せっかくですが、この{仕事|しごと}は（　　）かねます。",
     "opts": [
      "{引|ひ}き{受|う}ける",
      "{引|ひ}き{受|う}け",
      "{引|ひ}き{受|う}けられ"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "ます-stem + かねる."
    },
    {
     "type": "mcq",
     "id": "d10b-18-3-2",
     "q": "2　（　　）、こちらではお{答|こた}えしかねます。",
     "opts": [
      "この{問題|もんだい}はとても{難|むずか}しくて",
      "それは{個人|こじん}{情報|じょうほう}ですから",
      "{質問|しつもん}の{意味|いみ}がわからないので"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Position/rule (personal info) → polite refusal."
    },
    {
     "type": "mcq",
     "id": "d10b-18-3-3",
     "q": "3　{太郎|たろう}は{練習|れんしゅう}の{厳|きび}しさに{耐|た}えかねて、（　　）。",
     "opts": [
      "サッカー{部|ぶ}を{辞|や}めてしまった",
      "サッカー{部|ぶ}に{入|はい}りたがっている",
      "サッカー{部|ぶ}のレギュラー{選手|せんしゅ}になった"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "耐えかねて = couldn't bear it → quit."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【4】（～ようがない）",
   "children": [
    {
     "type": "mcq",
     "id": "d10b-18-4-1",
     "q": "1　{東京|とうきょう}は{人|ひと}が{多|おお}いので、{渋滞|じゅうたい}や{混雑|こんざつ}は（　　）ようがない。",
     "opts": [
      "{避|さ}ける",
      "{避|さ}け",
      "{避|さ}けられ"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "ます-stem + ようがない."
    },
    {
     "type": "mcq",
     "id": "d10b-18-4-2",
     "q": "2　{日本語|にほんご}の{勉強|べんきょう}を{始|はじ}めたばかりのトムさんには（　　）だろう。",
     "opts": [
      "{難|むずか}しい{漢字|かんじ}は{書|か}けない",
      "{難|むずか}しい{漢字|かんじ}の{書|か}きようがない",
      "{難|むずか}しい{漢字|かんじ}を{書|か}けようがない"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Ability → 書けない."
    },
    {
     "type": "mcq",
     "id": "d10b-18-4-3",
     "q": "3　おいしそうなお{弁当|べんとう}だったけど、（　　）ので、{食|た}べようがなかった。",
     "opts": [
      "はしもスプーンもなかった",
      "おなかが{痛|いた}かった",
      "{時間|じかん}がなかった"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "No means (no chopsticks or spoon) → 食べようがない."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【5】（～どころではない）",
   "children": [
    {
     "type": "mcq",
     "id": "d10b-18-5-1",
     "q": "1　{趣味|しゅみ}はスキーだが、{去年|きょねん}はずっと{忙|いそが}しくて、スキーに（　　）どころではなかった。",
     "opts": [
      "{行|い}く",
      "{行|い}ける",
      "{行|い}った"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Dictionary form."
    },
    {
     "type": "mcq",
     "id": "d10b-18-5-2",
     "q": "2　（　　）、{仕事|しごと}どころではない。",
     "opts": [
      "{内容|ないよう}が{難|むずか}しくて",
      "{熱|ねつ}があって",
      "{給料|きゅうりょう}が{安|やす}くて"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "No room because of illness."
    },
    {
     "type": "mcq",
     "id": "d10b-18-5-3",
     "q": "3　（　　）、この{本|ほん}を{読|よ}むどころではなかった。",
     "opts": [
      "{来客|らいきゃく}があって",
      "{字|じ}が{小|ちい}さくて",
      "{眼鏡|めがね}がなくて"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Busy with visitors → no time to read."
    },
    {
     "type": "mcq",
     "id": "d10b-18-5-4",
     "q": "4　のどが{痛|いた}くて、（　　）どころではない。",
     "opts": [
      "カラオケで{歌|うた}う",
      "{小|ちい}さい{声|こえ}を{出|だ}す",
      "{薬|くすり}を{飲|の}む"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "The fun thing you'd like to do."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【6】（～{得|う}る／～{得|え}ない）",
   "children": [
    {
     "type": "mcq",
     "id": "d10b-18-6-1",
     "q": "1　{危機|きき}はチャンスにも（　　）{得|う}る。",
     "opts": [
      "なる",
      "なり",
      "なれ"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "ます-stem + 得る."
    },
    {
     "type": "mcq",
     "id": "d10b-18-6-2",
     "q": "2　どんな{場合|ばあい}でも{事故|じこ}は（　　）。",
     "opts": [
      "{起|お}これる",
      "{起|お}こることができる",
      "{起|お}こり{得|う}る"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Possibility → 起こり得る."
    },
    {
     "type": "mcq",
     "id": "d10b-18-6-3",
     "q": "3　この{子|こ}はまだ（　　）。",
     "opts": [
      "{字|じ}を{読|よ}み{得|え}ない",
      "{字|じ}が{読|よ}めない",
      "{字|じ}を{読|よ}むことができ{得|え}ない"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Ability → 読めない."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【1～6】まとめ",
   "children": [
    {
     "type": "mcq",
     "id": "d10b-18-7-1",
     "q": "1　{風邪|かぜ}を{引|ひ}いたので、{学校|がっこう}に（　　）。",
     "opts": [
      "{行|い}けません",
      "{行|い}きかねます",
      "{行|い}きがたいです"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Simply can't → 行けません."
    },
    {
     "type": "mcq",
     "id": "d10b-18-7-2",
     "q": "2　{夜|よる}{遅|おそ}くなり、わたしは{子供|こども}の{帰|かえ}りを（　　）、{駅|えき}まで{迎|むか}えに{行|い}った。",
     "opts": [
      "{待|ま}ち{得|え}なくて",
      "{待|ま}ちようがなくて",
      "{待|ま}ちかねて"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "待ちかねて = couldn't wait any longer."
    },
    {
     "type": "mcq",
     "id": "d10b-18-7-3",
     "q": "3　サラダは{野菜|やさい}を{切|き}って{混|ま}ぜるだけだから、だれでも（　　）。",
     "opts": [
      "{失敗|しっぱい}のしようがない",
      "{失敗|しっぱい}できない",
      "{失敗|しっぱい}しかねる"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Can't possibly fail → 失敗のしようがない."
    },
    {
     "type": "mcq",
     "id": "d10b-18-7-4",
     "q": "4　{雨|あめ}が{降|ふ}っているので、{散歩|さんぽ}に（　　）。",
     "opts": [
      "{行|い}きがたい",
      "{行|い}くわけにはいかない",
      "{行|い}けない"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Weather → simply can't → 行けない."
    },
    {
     "type": "mcq",
     "id": "d10b-18-7-5",
     "q": "5　{歌手|かしゅ}になるのは{難|むずか}しいとわかっているが、{会社|かいしゃ}も{辞|や}めてしまったのだから、（　　）。",
     "opts": [
      "あきらめようがない",
      "あきらめるわけにはいかない",
      "あきらめがたい"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Feeling/situation: I quit my job, so I can't give up now."
    }
   ],
   "scored": true
  },
  {
   "type": "items",
   "title": "19{課|か}　〔{復習|ふくしゅう}〕",
   "items": [
    {
     "t": "・80{歳|さい}という{年齢|ねんれい}[[を{考|かんが}えると]]、うちの{祖父|そふ}は{若々|わかわか}しい。",
     "explain": "Review: ～を考えると = considering ～."
    },
    {
     "t": "・{教師|きょうし}の{立場|たちば}[[から{言|い}うと]]、{素直|すなお}な{生徒|せいと}の{方|ほう}が{扱|あつか}いやすいのだろう。",
     "explain": "Review: ～から言うと = from the standpoint of ～."
    }
   ],
   "explain": "19課 = evaluating from a standard (わりに, にしては, だけある) or from a standpoint (として, にとって, にしたら)."
  },
  {
   "type": "grammar",
   "no": "7",
   "id": "d10b-g7",
   "teach": {
    "intro": [
     "わりに = 'for ～ / considering ～' — the result is different from what you'd expect.",
     "'Vayasu kammi, aanaa romba responsible.' → 若いわりにしっかりしている.",
     "Goes with words that have a range or degree: 年齢・値段・若い・心配する…"
    ],
    "pattern": "［名詞］の・［動詞・形容詞］{普通形|ふつうけい}（［な形容詞］だ→な／である）＋わりに（は）",
    "examples": [
     {
      "jp": "この{店|みせ}は{値段|ねだん}のわりにおいしい。",
      "th": "Vilaikku yetha maadhiri illaama, romba taste.",
      "kana": "このみせはねだんのわりにおいしい。"
     },
     {
      "jp": "たくさん{勉強|べんきょう}したわりには、{点|てん}が{悪|わる}かった。",
      "th": "Neraya padichen, aanaa marks kammi.",
      "kana": "たくさんべんきょうしたわりには、てんがわるかった。"
     },
     {
      "jp": "あの{人|ひと}は{年|とし}のわりに{若|わか}く{見|み}える。",
      "th": "Vayasukku ilamaiyaa therivaar.",
      "kana": "あのひとはとしのわりにわかくみえる。"
     }
    ],
    "wrong": [
     {
      "ng": "たくさん{練習|れんしゅう}したわりにいい{成績|せいせき}が{残|のこ}せた。",
      "ok": "あまり{練習|れんしゅう}しなかったわりにいい{成績|せいせき}が{残|のこ}せた。",
      "th": "わりに needs a gap between expectation and result. Practised a lot + good result = no gap."
     }
    ],
    "check": [
     {
      "q": "この{寺|てら}は（　　）わりには{観光|かんこう}{客|きゃく}が{少|すく}ない。",
      "opts": [
       "{有名|ゆうめい}",
       "{有名|ゆうめい}な",
       "{有名|ゆうめい}だ"
      ],
      "ans": 1,
      "explain": "な-adj: 有名な＋わりに.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～わりに（は）",
   "meaning": "～という{基準|きじゅん}から{考|かんが}えられる{程度|ていど}と{違|ちが}っている。",
   "explain": [
    "わりに（は） = different from the degree you'd expect from ～.",
    "Shape: Noun + の / verb・adj plain form (な-adj ~~だ~~ → な / である) + わりに（は）.",
    "Kavanam: attaches to words with a range/degree (age, price, worry, young…). After it comes an evaluation that doesn't fit the expected degree."
   ],
   "examples": [
    {
     "t": "①このお{菓子|かし}は{値段|ねだん}の[[わりには]]{量|りょう}が{少|すく}ない。",
     "explain": "For the price, small amount."
    },
    {
     "t": "②この{料理|りょうり}は{安|やす}い{材料|ざいりょう}で{簡単|かんたん}にできる[[わりには]]{豪華|ごうか}に{見|み}える。",
     "explain": "Cheap and easy but looks luxurious."
    },
    {
     "t": "③ゆき{子|こ}さんは{若|わか}い[[わりに]]しっかりしている。",
     "explain": "Young but mature."
    }
   ],
   "form": "［名］－の・［動・形］{普通|ふつう}{形|かたち}（［ナ形］だ－な／－である）　＋わりに（は）",
   "caution": "{意味|いみ}や{程度|ていど}に{幅|はば}がある{言葉|ことば}（{年齢|ねんれい}・{値段|ねだん}・{心配|しんぱい}する・{若|わか}いなど）につく。{後|あと}には、{予想|よそう}される{程度|ていど}とは{合|あ}わないという{評価|ひょうか}を{言|い}う{文|ぶん}が{来|く}る。"
  },
  {
   "type": "grammar",
   "no": "8",
   "id": "d10b-g8",
   "teach": {
    "intro": [
     "にしては = 'for a ～ (it's surprising)'. Used with ONE specific fact.",
     "'February-kku idhu romba warm.' → 2月にしては暖かい.",
     "わりに: a range (値段, 年齢). にしては: a specific point (2月, 1,000円, 子供が作った)."
    ],
    "pattern": "［名詞］・{普通形|ふつうけい}（［な形容詞］だ→である・［名詞］だ→である）＋にしては",
    "examples": [
     {
      "jp": "{初|はじ}めてにしては{上手|じょうず}だ。",
      "th": "First time-kku romba nalla irukku.",
      "kana": "はじめてにしてはじょうずだ。"
     },
     {
      "jp": "プロにしてはミスが{多|おお}い。",
      "th": "Professional-kku idhu neraya mistake.",
      "kana": "プロにしてはミスがおおい。"
     },
     {
      "jp": "{外国|がいこく}{人|じん}にしては{日本語|にほんご}がうまい。",
      "th": "Foreigner-kku Japanese romba nalla pesuraar.",
      "kana": "がいこくじんにしてはにほんごがうまい。"
     }
    ],
    "wrong": [
     {
      "ng": "いつも{派手|はで}な{服|ふく}を{着|き}ているさゆりさんにしては、{今日|きょう}はすてきな{服|ふく}を{着|き}ている。",
      "ok": "いつも{派手|はで}な{服|ふく}を{着|き}ているさゆりさんにしては、{今日|きょう}の{服|ふく}はシンプルだ。",
      "th": "にしては needs a surprise against the standard: always flashy → today SIMPLE."
     }
    ],
    "check": [
     {
      "q": "{彼女|かのじょ}は{今日|きょう}{初|はじ}めてテニスをしたのだそうだ。{初|はじ}めてにしては、（　　）。",
      "opts": [
       "{上手|じょうず}だ",
       "うまくない",
       "{今日|きょう}の{試合|しあい}で{勝|か}った"
      ],
      "ans": 0,
      "explain": "Surprising evaluation → 上手だ.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～にしては",
   "meaning": "～という{事実|じじつ}・{標準|ひょうじゅん}から{考|かんが}えると、{予想|よそう}{外|がい}だ。",
   "explain": [
    "にしては = considering the fact/standard ～, it's unexpected.",
    "Shape: Noun / plain form (な-adj ~~だ~~ → である, Noun ~~だ~~ → である) + にしては.",
    "Kavanam: usually attaches to a specific thing with no range (2月, 1,000円, 子供が作った). After it comes an evaluation different from what is expected."
   ],
   "examples": [
    {
     "t": "①{今日|きょう}は{2月|にがつ}[[にしては]]{暖|あたた}かかった。",
     "explain": "Warm for February."
    },
    {
     "t": "②このかばんは、1,000{円|えん}[[にしては]]{丈夫|じょうぶ}で、デザインもいい。",
     "explain": "Good for only 1,000 yen."
    },
    {
     "t": "③このケーキ、{子供|こども}が{作|つく}った[[にしては]]おいしくできていますね。",
     "explain": "Good for a child's cake."
    }
   ],
   "form": "［名］・{普通|ふつう}{形|かたち}（［ナ形］だ－である・［名］だ－である）　＋にしては",
   "caution": "{幅|はば}がなく、ある{特定|とくてい}のこと（{2月|にがつ}・1,000{円|えん}・{子供|こども}が{作|つく}ったなど）につくことが{多|おお}い。{後|あと}には、{予想|よそう}されることと{違|ちが}うという{評価|ひょうか}を{言|い}う{文|ぶん}が{来|く}る。"
  },
  {
   "type": "grammar",
   "no": "9",
   "id": "d10b-g9",
   "teach": {
    "intro": [
     "だけのことはある / だけあって = 'as expected of ～ / no wonder'. Positive evaluation.",
     "'Ten years Japan-la irukkaaru, adhaan ivlo theriyudhu.' → 住んでいるだけあって.",
     "Opposite feel of わりに/にしては (which are 'unexpected'). This one is 'just as expected'."
    ],
    "pattern": "［名詞］・{普通形|ふつうけい}（［な形容詞］だ→な）＋だけ（のことは）ある　＊［名詞］だ の形にはつかない",
    "examples": [
     {
      "jp": "さすがプロだけあって、{上手|じょうず}だ。",
      "th": "Professional-aache, adhaan ivlo nalla irukku.",
      "kana": "さすがプロだけあって、じょうずだ。"
     },
     {
      "jp": "{高|たか}いだけのことはある。{品質|ひんしつ}がいい。",
      "th": "Vilai adhigam dhaan, aanaa worth it.",
      "kana": "たかいだけのことはある。ひんしつがいい。"
     },
     {
      "jp": "{練習|れんしゅう}しただけあって、{素晴|すば}らしい{発表|はっぴょう}だった。",
      "th": "Practice pannadhaala dhaan, super presentation.",
      "kana": "れんしゅうしただけあって、すばらしいはっぴょうだった。"
     }
    ],
    "wrong": [
     {
      "ng": "たくさん{練習|れんしゅう}しただけあって、きっと{素晴|すば}らしい{発表|はっぴょう}だろう。",
      "ok": "たくさん{練習|れんしゅう}しただけあって、{素晴|すば}らしい{発表|はっぴょう}だった。",
      "th": "After だけあって: a high evaluation of a fact, not a guess or future (～だろう)."
     }
    ],
    "check": [
     {
      "q": "あの{学校|がっこう}は{町|まち}の{中心|ちゅうしん}から{離|はな}れているだけあって、（　　）。",
      "opts": [
       "{静|しず}かで{環境|かんきょう}がいい",
       "{遠|とお}くて{不便|ふべん}だ",
       "{通|かよ}うのに{時間|じかん}がかかる"
      ],
      "ans": 0,
      "explain": "Positive, as expected → 静かで環境がいい.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～だけ（のことは）ある",
   "meaning": "～という{条件|じょうけん}から{期待|きたい}されるとおりだ。",
   "explain": [
    "だけ（のことは）ある = just as you'd expect from ～.",
    "Shape: Noun / plain form (な-adj ~~だ~~ → な) + だけ（のことは）ある. Not used with 'Noun だ'.",
    "Kavanam: after ～だけあって comes a sentence that evaluates highly. No future or guessing sentence."
   ],
   "examples": [
    {
     "t": "①{素晴|すば}らしいマンションだ。{家賃|やちん}が{高|たか}い[[だけのことはある]]。",
     "explain": "Expensive rent — and worth it."
    },
    {
     "t": "②{彼|かれ}は10{年|ねん}も{日本|にほん}に{住|す}んでいる[[だけあって]]、{日本|にほん}のことをよく{知|し}っている。",
     "explain": "No wonder he knows a lot."
    },
    {
     "t": "③さすがオリンピック[[だけあって]]、{見事|みごと}な{試合|しあい}が{見|み}られた。",
     "explain": "As expected of the Olympics."
    }
   ],
   "form": "［名］・{普通|ふつう}{形|かたち}（［ナ形］だ－な）　＋だけ（のことは）ある　＊［名］だの{形|けい}には{接続|せつぞく}しない。",
   "caution": "「～だけあって」の{後|あと}には、{評価|ひょうか}が{高|たか}いことを{表|あらわ}す{文|ぶん}が{来|く}る。{未来|みらい}や{推量|すいりょう}を{表|あらわ}す{文|ぶん}は{来|こ}ない。"
  },
  {
   "type": "grammar",
   "no": "10",
   "id": "d10b-g10",
   "teach": {
    "intro": [
     "として = 'as ～' (in the role / position / name of ～).",
     "'Coach-aa team-kku velai paarthaar.' → コーチとして.",
     "After it: an action, a 'known as / famous' phrase, or a judgement (当然だ・恥ずかしい)."
    ],
    "pattern": "［名詞］＋として",
    "examples": [
     {
      "jp": "{留学生|りゅうがくせい}として{日本|にほん}に{来|き}た。",
      "th": "Foreign student-aa Japan vandhen.",
      "kana": "りゅうがくせいとしてにほんにきた。"
     },
     {
      "jp": "{京都|きょうと}は{古|ふる}い{町|まち}として{有名|ゆうめい}だ。",
      "th": "Kyoto pazhaya ooraa famous.",
      "kana": "きょうとはふるいまちとしてゆうめいだ。"
     },
     {
      "jp": "{親|おや}として{当然|とうぜん}のことをしただけだ。",
      "th": "Amma-appa-vaa seiya vendiyadhai dhaan seidhen.",
      "kana": "おやとしてとうぜんのことをしただけだ。"
     }
    ],
    "wrong": [
     {
      "ng": "わたしは{観光|かんこう}として{日本|にほん}に{来|き}た。",
      "ok": "わたしは{留学生|りゅうがくせい}として{日本|にほん}に{来|き}た。",
      "th": "として needs a role/status (留学生). Purpose → 観光で / 観光のために."
     }
    ],
    "check": [
     {
      "q": "{新聞紙|しんぶんし}は（　　）として{再|さい}{利用|りよう}されます。",
      "opts": [
       "ごみ",
       "{資源|しげん}",
       "もったいない"
      ],
      "ans": 1,
      "explain": "In the role of a resource → 資源として.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～として",
   "meaning": "～という{立場|たちば}・{資格|しかく}・{役割|やくわり}・{名目|めいもく}で、あることをする・ある{状態|じょうたい}である。",
   "explain": [
    "として = in the position / qualification / role / name of ～, do something or be in a state.",
    "Shape: Noun + として.",
    "Kavanam: followed by verbs of action/state, value words (知られている・有名だ) or judgements (当然だ・恥ずかしい)."
   ],
   "examples": [
    {
     "t": "①{彼|かれ}は{選手|せんしゅ}を{引退|いんたい}した{後|ご}、コーチ[[として]]チームのために{働|はたら}いた。",
     "explain": "Role."
    },
    {
     "t": "②コーヒーはもともと{薬|くすり}[[として]]{飲|の}まれていた。",
     "explain": "Used as medicine."
    },
    {
     "t": "③{京都|きょうと}は{日本|にほん}の{歴史|れきし}{的|てき}な{古|ふる}い{町|まち}[[として]]{知|し}られている。",
     "explain": "Known as."
    },
    {
     "t": "④{子供|こども}の{安全|あんぜん}に{気|き}をつけることは{親|おや}[[として]]{当然|とうぜん}だ。",
     "explain": "Judgement: natural as a parent."
    },
    {
     "t": "⑤{写真|しゃしん}は{趣味|しゅみ}じゃないんです。{仕事|しごと}[[として]]やっているんです。",
     "explain": "As a job."
    }
   ],
   "form": "［名］　＋として",
   "caution": "{後|あと}には、{行為|こうい}・{状態|じょうたい}を{表|あらわ}す{動詞|どうし}、{価値|かち}{付|づ}けの{言葉|ことば}（{知|し}られている・{有名|ゆうめい}だなど）や{判断|はんだん}・{評価|ひょうか}を{表|あらわ}す{言葉|ことば}（{当然|とうぜん}だ・{恥|は}ずかしいなど）が{来|く}る。"
  },
  {
   "type": "grammar",
   "no": "11",
   "id": "d10b-g11",
   "teach": {
    "intro": [
     "にとって = 'for ～ / to ～' (from that person's point of view).",
     "'Enakku idhu oru treasure.' → わたしにとっては宝物だ.",
     "After it: an EVALUATION (mostly adjectives: 大切だ・必要だ・難しい). NOT an action."
    ],
    "pattern": "［名詞］＋にとって",
    "examples": [
     {
      "jp": "わたしにとって{家族|かぞく}が{一番|いちばん}{大切|たいせつ}だ。",
      "th": "Enakku family dhaan mukkiyam.",
      "kana": "わたしにとってかぞくがいちばんたいせつだ。"
     },
     {
      "jp": "{学生|がくせい}にとってこの{本|ほん}は{高|たか}すぎる。",
      "th": "Students-ukku indha book romba costly.",
      "kana": "がくせいにとってこのほんはたかすぎる。"
     },
     {
      "jp": "{子供|こども}にとって{遊|あそ}びは{勉強|べんきょう}だ。",
      "th": "Kuzhandhaigalukku velaiyaattu-um oru padippu.",
      "kana": "こどもにとってあそびはべんきょうだ。"
     }
    ],
    "wrong": [
     {
      "ng": "{父|ちち}にとってよく{仕事|しごと}を{続|つづ}けた。",
      "ok": "{父|ちち}にとって{仕事|しごと}は{人生|じんせい}そのものだった。",
      "th": "No action after にとって. Give an evaluation (仕事は人生そのものだった)."
     }
    ],
    "check": [
     {
      "q": "{君|きみ}にとって（　　）、{考|かんが}えたことはありますか。",
      "opts": [
       "{何|なに}が{大切|たいせつ}か",
       "{何|なに}を{大切|たいせつ}にしているか",
       "{大切|たいせつ}にしているものは{何|なに}か"
      ],
      "ans": 0,
      "explain": "Evaluation word: 何が大切か.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～にとって",
   "meaning": "（いろいろな{考|かんが}え{方|かた}がある{中|なか}で）～の{考|かんが}えでは、あることが{言|い}える。",
   "explain": [
    "にとって = (among many views) from ～'s point of view, this can be said.",
    "Shape: Noun + にとって.",
    "Kavanam: mostly attaches to nouns for people. After it comes how that person evaluates (mainly adjective sentences). No action sentence."
   ],
   "examples": [
    {
     "t": "①{今|いま}のわたし[[にとって]]{一番|いちばん}{大切|たいせつ}なのは{家族|かぞく}です。",
     "explain": "From my view."
    },
    {
     "t": "②{現代|げんだい}{人|じん}[[にとって]]パソコンはなくてはならない{道具|どうぐ}である。",
     "explain": "Essential for modern people."
    },
    {
     "t": "③この{小石|こいし}はほかの{人|ひと}[[にとっては]]{普通|ふつう}の{石|いし}ですが、わたし[[にとっては]]{宝物|たからもの}なのです。",
     "explain": "Contrast with は."
    }
   ],
   "form": "［名］　＋にとって",
   "caution": "{主|おも}に{人|ひと}を{表|あらわ}す{名詞|めいし}につく。{後|あと}には、その{人|ひと}がどう{評価|ひょうか}しているかを{表|あらわ}す{文|ぶん}（{主|おも}に{形容詞|けいようし}の{文|ぶん}）が{来|く}る。{動作|どうさ}を{表|あらわ}す{文|ぶん}は{来|こ}ない。"
  },
  {
   "type": "grammar",
   "no": "12",
   "id": "d10b-g12",
   "teach": {
    "intro": [
     "にしたら / にすれば / にしてみれば = 'from ～'s standpoint, (I guess) they feel ～'. にしても = 'even for ～'.",
     "'Un amma-vukku, nee pathi kavalai dhaan.' → お母さんにしたら、心配なんだよ.",
     "Used for SOMEONE ELSE, and you guess their feelings (～だろう・～と思う・～ようだ)."
    ],
    "pattern": "［名詞］＋にしたら・にすれば・にしてみれば・にしても",
    "examples": [
     {
      "jp": "{親|おや}にしたら、{子供|こども}の{将来|しょうらい}が{心配|しんぱい}だろう。",
      "th": "Parents-ukku, kuzhandhaiyoda future pathi kavalai irukkum.",
      "kana": "おやにしたら、こどものしょうらいがしんぱいだろう。"
     },
     {
      "jp": "{客|きゃく}にすれば、{安|やす}いほうがいいに{決|き}まっている。",
      "th": "Customer-ukku vilai kammi-aa irundha dhaan nalladhu.",
      "kana": "きゃくにすれば、やすいほうがいいにきまっている。"
     },
     {
      "jp": "{先生|せんせい}にしても、この{結果|けっか}は{残念|ざんねん}だったはずだ。",
      "th": "Teacher-ukkum indha result varuthamaa irukkum.",
      "kana": "せんせいにしても、このけっかはざんねんだったはずだ。"
     }
    ],
    "wrong": [
     {
      "ng": "わたしにしたら、この{映画|えいが}はつまらない。",
      "ok": "わたしにとって、この{映画|えいが}はつまらない。",
      "th": "にしたら is for other people's feelings. For yourself, use にとって."
     }
    ],
    "check": [
     {
      "q": "わたしは{商品|しょうひん}の{売|う}り{込|こ}みの{電話|でんわ}はすぐ{切|き}ってしまうが、{営業|えいぎょう}マンにすれば（　　）。",
      "opts": [
       "なるべく{長|なが}く{話|はな}したいだろう",
       "{早|はや}く{話|はなし}を{終|お}わらせたいだろう",
       "それはありがたいことだろう"
      ],
      "ans": 0,
      "explain": "Guess the salesman's feelings: want to talk longer.",
      "keys": [
       "a",
       "b",
       "c"
      ]
     }
    ]
   },
   "title": "～にしたら・～にすれば・～にしてみれば・～にしても",
   "meaning": "～の{立場|たちば}になってみれば・～の{立場|たちば}から{言|い}っても、あることが{言|い}える。",
   "explain": [
    "にしたら・にすれば・にしてみれば・にしても = if you stand in ～'s position / even from ～'s position.",
    "Shape: Noun + にしたら・にすれば・にしてみれば・にしても.",
    "Kavanam: usually attaches to a word for someone other than the speaker. After it, the speaker imagines that person's feelings."
   ],
   "examples": [
    {
     "t": "①{君|きみ}もいろいろ{言|い}われて{面倒|めんどう}だろうが、{君|きみ}のお{母|かあ}さん[[にしたら]]、{君|きみ}のことが{心配|しんぱい}なんだよ。",
     "explain": "Mother's position."
    },
    {
     "t": "②たばこを{吸|す}う{人|ひと}[[にすれば]]、たばこの{害|がい}についての{話題|わだい}は{避|さ}けたいだろうと{思|おも}う。",
     "explain": "Smoker's position."
    },
    {
     "t": "③{新|あたら}しい{高速道路|こうそくどうろ}ができて{便利|べんり}になったが、{沿線|えんせん}の{住民|じゅうみん}[[にしてみれば]]、あまりありがたくはないかもしれない。",
     "explain": "Residents' position."
    },
    {
     "t": "④わたしは{早|はや}く{家|いえ}を{出|で}たい。{両親|りょうしん}[[にしても]]{息子|むすこ}には{自立|じりつ}してほしいと{思|おも}っているようだ。",
     "explain": "にしても = the parents too."
    }
   ],
   "form": "［名］　＋にしたら・にすれば・にしてみれば・にしても",
   "caution": "ふつう、{話者|わしゃ}{以外|いがい}の{人|ひと}を{表|あらわ}す{言葉|ことば}につく。{後|あと}には、その{人|ひと}の{立場|たちば}に{立|た}って、その{人|ひと}の{気持|きも}ちを{推量|すいりょう}して{言|い}う{文|ぶん}が{来|く}る。"
  },
  {
   "type": "group",
   "title": "【1】（～わりに（は））",
   "children": [
    {
     "type": "mcq",
     "id": "d10b-19-1-1",
     "q": "1　この{寺|てら}は（　　）わりには{観光客|かんこうきゃく}が{少|すく}ない。",
     "opts": [
      "{有名|ゆうめい}",
      "{有名|ゆうめい}な",
      "{有名|ゆうめい}だ"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "な-adj + な + わりに."
    },
    {
     "type": "mcq",
     "id": "d10b-19-1-2",
     "q": "2　（　　）わりにいい{成績|せいせき}が{残|のこ}せた。",
     "opts": [
      "3{時間|じかん}{練習|れんしゅう}した",
      "たくさん{練習|れんしゅう}した",
      "あまり{練習|れんしゅう}しなかった"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Gap: little practice but good result."
    },
    {
     "type": "mcq",
     "id": "d10b-19-1-3",
     "q": "3　{期待|きたい}したわりには（　　）。",
     "opts": [
      "{点数|てんすう}に{満足|まんぞく}できた",
      "{点数|てんすう}は{良|よ}くなかった",
      "{点数|てんすう}は80{点|てん}{以上|いじょう}だった"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Expected a lot → not good."
    },
    {
     "type": "mcq",
     "id": "d10b-19-1-4",
     "q": "4　この{事件|じけん}は、{新聞|しんぶん}で{騒|さわ}がれたわりには（　　）。",
     "opts": [
      "{知|し}らない{人|ひと}が{多|おお}い",
      "{知|し}らない{人|ひと}がいた",
      "わたしは{知|し}らなかった"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "General evaluation: many people don't know."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【2】（～にしては）",
   "children": [
    {
     "type": "mcq",
     "id": "d10b-19-2-1",
     "q": "1　いつも{派手|はで}な{服|ふく}を{着|き}ているさゆりさんにしては、（　　）。",
     "opts": [
      "{服|ふく}をたくさん{持|も}っている",
      "{今日|きょう}はすてきな{服|ふく}を{着|き}ている",
      "{今日|きょう}の{服|ふく}はシンプルだ"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Surprise against her usual: simple."
    },
    {
     "type": "mcq",
     "id": "d10b-19-2-2",
     "q": "2　{彼女|かのじょ}は{今日|きょう}{初|はじ}めてテニスをしたのだそうだ。{初|はじ}めてにしては、（　　）。",
     "opts": [
      "{上手|じょうず}だ",
      "うまくない",
      "{今日|きょう}の{試合|しあい}で{勝|か}った"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Evaluation: good for a first time."
    },
    {
     "type": "mcq",
     "id": "d10b-19-2-3",
     "q": "3　ジョンさんは{試験|しけん}に{合格|ごうかく}したにしては、（　　）。",
     "opts": [
      "{大喜|おおよろこ}びしている",
      "うれしくなさそうだ",
      "{国|くに}へ{帰|かえ}ってしまった"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Unexpected: not happy."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【3】（～だけ（のことは）ある）",
   "children": [
    {
     "type": "mcq",
     "id": "d10b-19-3-1",
     "q": "1　たくさん{練習|れんしゅう}しただけあって、（　　）。",
     "opts": [
      "きっと{素晴|すば}らしい{発表|はっぴょう}だろう",
      "{素晴|すば}らしい{発表|はっぴょう}だった",
      "{緊張|きんちょう}はしなかった"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "High evaluation of a fact (no guessing)."
    },
    {
     "type": "mcq",
     "id": "d10b-19-3-2",
     "q": "2　あの{学校|がっこう}は{町|まち}の{中心|ちゅうしん}から{離|はな}れているだけあって、（　　）。",
     "opts": [
      "{静|しず}かで{環境|かんきょう}がいい",
      "{遠|とお}くて{不便|ふべん}だ",
      "{通|かよ}うのに{時間|じかん}がかかる"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Positive and as expected."
    },
    {
     "type": "mcq",
     "id": "d10b-19-3-3",
     "q": "3　あの{人|ひと}は{若|わか}いだけあって、（　　）。",
     "opts": [
      "きっと{困難|こんなん}を{乗|の}り{越|こ}えられる",
      "{考|かんが}え{方|かた}が{子供|こども}っぽい",
      "{仕事|しごと}を{覚|おぼ}えるのが{早|はや}い"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Positive fact: learns fast."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【4】（～として）",
   "children": [
    {
     "type": "mcq",
     "id": "d10b-19-4-1",
     "q": "1　わたしは（　　）として{日本|にほん}に{来|き}た。",
     "opts": [
      "{留学生|りゅうがくせい}",
      "{仕事|しごと}",
      "{観光|かんこう}"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Status/role → 留学生として."
    },
    {
     "type": "mcq",
     "id": "d10b-19-4-2",
     "q": "2　{新聞紙|しんぶんし}は（　　）として{再利用|さいりよう}されます。",
     "opts": [
      "ごみ",
      "{資源|しげん}",
      "もったいない"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "As a resource."
    },
    {
     "type": "mcq",
     "id": "d10b-19-4-3",
     "q": "3　{彼|かれ}は{才能|さいのう}ある{建築家|けんちくか}として（　　）。",
     "opts": [
      "{劇場|げきじょう}の{設計|せっけい}が{専門|せんもん}だ",
      "この{劇場|げきじょう}が{代表|だいひょう}{作|さく}だ",
      "{高|たか}く{評価|ひょうか}されている"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Value/evaluation word after として."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【5】（～にとって）",
   "children": [
    {
     "type": "mcq",
     "id": "d10b-19-5-1",
     "q": "1　{父|ちち}にとって（　　）。",
     "opts": [
      "{仕事|しごと}が{好|す}きだった",
      "よく{仕事|しごと}を{続|つづ}けた",
      "{仕事|しごと}は{人生|じんせい}そのものだった"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Evaluation, not action."
    },
    {
     "type": "mcq",
     "id": "d10b-19-5-2",
     "q": "2　{君|きみ}にとって（　　）、{考|かんが}えたことはありますか。",
     "opts": [
      "{何|なに}が{大切|たいせつ}か",
      "{何|なに}を{大切|たいせつ}にしているか",
      "{大切|たいせつ}にしているものは{何|なに}か"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Evaluation word."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【6】（～にしたら・～にすれば・～にしてみれば・～にしても）",
   "children": [
    {
     "type": "mcq",
     "id": "d10b-19-6-1",
     "q": "1　わたしはフルタイムで{働|はたら}きたいし、{夫|おっと}（　　）、そのほうが{心強|こころづよ}いだろう。",
     "opts": [
      "にしたら",
      "にしても",
      "にしては"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "My view + my husband's too → にしても."
    },
    {
     "type": "mcq",
     "id": "d10b-19-6-2",
     "q": "2　わたしは{商品|しょうひん}の{売|う}り{込|こ}みの{電話|でんわ}はすぐ{切|き}ってしまうが、{営業|えいぎょう}マンにすれば（　　）。",
     "opts": [
      "なるべく{長|なが}く{話|はな}したいだろう",
      "{早|はや}く{話|はなし}を{終|お}わらせたいだろう",
      "それはありがたいことだろう"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Guessing the salesman's feelings."
    }
   ],
   "scored": true
  },
  {
   "type": "group",
   "title": "【1～6】まとめ",
   "children": [
    {
     "type": "mcq",
     "id": "d10b-19-7-1",
     "q": "1　ここは{幼稚園|ようちえん}（　　）、にぎやかな{子供|こども}の{声|こえ}が{聞|き}こえない。",
     "opts": [
      "のわりには",
      "にしては",
      "だけあって"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Specific fact (a kindergarten) → unexpected."
    },
    {
     "type": "mcq",
     "id": "d10b-19-7-2",
     "q": "2　{実験|じっけん}の{回数|かいすう}（　　）{正確|せいかく}なデータは{得|え}られなかった。",
     "opts": [
      "にしたら",
      "にとって",
      "のわりに"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Number of experiments = range → わりに."
    },
    {
     "type": "mcq",
     "id": "d10b-19-7-3",
     "q": "3　{子供|こども}のころのわたし（　　）{親|おや}は{神様|かみさま}だった。",
     "opts": [
      "としては",
      "にしては",
      "にとっては"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Evaluation from my view."
    },
    {
     "type": "mcq",
     "id": "d10b-19-7-4",
     "q": "4　{勉強|べんきょう}{時間|じかん}（　　）{成績|せいせき}は{上|あ}がらなかった。",
     "opts": [
      "のわりには",
      "にしては",
      "だけあって"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Range (study time) → わりには."
    },
    {
     "type": "mcq",
     "id": "d10b-19-7-5",
     "q": "5　この{町|まち}はしょうゆの{産地|さんち}（　　）{有名|ゆうめい}である。",
     "opts": [
      "にとって",
      "として",
      "にしたら"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Known/famous as → として."
    },
    {
     "type": "mcq",
     "id": "d10b-19-7-6",
     "q": "6　{農家|のうか}の{人|ひと}（　　）{米|こめ}の{値段|ねだん}をもっと{上|あ}げてほしいだろう。",
     "opts": [
      "にしては",
      "にしたら",
      "にとって"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Guessing someone else's feeling → にしたら."
    },
    {
     "type": "mcq",
     "id": "d10b-19-7-7",
     "q": "7　よう{子|こ}さんは{医学|いがく}を{勉強|べんきょう}した（　　）、{健康|けんこう}についての{知識|ちしき}が{豊富|ほうふ}だ。",
     "opts": [
      "わりに",
      "にしては",
      "だけあって"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "As expected → だけあって."
    },
    {
     "type": "mcq",
     "id": "d10b-19-7-8",
     "q": "8　わたしは{田中|たなか}さんを{先輩|せんぱい}（　　）{尊敬|そんけい}しているが、{結婚|けっこん}{相手|あいて}とは{考|かんが}えていない。",
     "opts": [
      "としては",
      "にとっては",
      "だけあっては"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": "Role: as a senior → としては."
    }
   ],
   "scored": true
  }
 ]
});
