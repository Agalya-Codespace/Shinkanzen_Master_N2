/* Day 19 · chokai. Built from d19_chokai.py by tools/build_day.py (furigana added automatically). */
window.N2_DAYS = window.N2_DAYS || {};
window.N2_DAYS[19] = window.N2_DAYS[19] || {"title": "", "intro": "", "sections": []};
if (false) window.N2_DAYS[19].title = "";
if (false) window.N2_DAYS[19].intro = "";
window.N2_DAYS[19].sections.push({
 "book": "chokai",
 "title": "{実力|じつりょく}{養成|ようせい}{編|へん}　Ⅵ「{統合|とうごう}{理解|りかい}」のスキルを{学|まな}ぶ　2 2{種類|しゅるい}の{話|はなし}を{整理|せいり}する・{確認|かくにん}{問題|もんだい}",
 "source": "新完全マスター聴解 N2 · 実力養成編 Ⅵ-2・確認問題 · pp.90–95 · CD B37–B44",
 "blocks": [
  {
   "type": "items",
   "title": "2　2{種類|しゅるい}の{話|はなし}を{整理|せいり}する",
   "items": [
    {
     "t": "この{問題|もんだい}{形式|けいしき}では、2{種類|しゅるい}の{話|はなし}（{例|れい}：あることについての{説明|せつめい}＋それについての{会話|かいわ}）を{整理|せいり}して{聞|き}きます。{最初|さいしょ}の{話|はなし}では、{選択肢|せんたくし}を{見|み}ながら{大切|たいせつ}な{点|てん}を{聞|き}き{取|と}ってメモします。その{後|ご}の{会話|かいわ}では、{最初|さいしょ}にメモした{情報|じょうほう}について、{2人|ふたり}の{意見|いけん}の{違|ちが}いなどを{聞|き}き{取|と}ります。",
     "explain": [
      "Sensei: This is JLPT 聴解 問題5 番号3 type. Part 1: a shop clerk / announcer explains 4 things (A, B, C, D). Part 2: two people talk about which one each will choose. Two questions: 'which does the man choose?' and 'which does the woman choose?'",
      "Method: while part 1 plays, write 2–3 keywords next to each printed option (1 Aセット: パスタ・飲み物…). In part 2 listen for the reason each person gives, then match it to your notes.",
      "Thanglish: Mudhal part-la 4 options-kku side-la notes podunga. Rendaavadhu part-la man enna solraar, woman enna solraanga — separate-a track pannunga. Last-la 'これにしよう' enga varudhu nu paarunga."
     ]
    }
   ]
  },
  {
   "type": "audio",
   "title": "☆{例題|れいだい}2　①　CD B37",
   "src": "audio/chokai/b37.mp3",
   "label": "CD B37",
   "t": "{最初|さいしょ}の{話|はなし}を{聞|き}いて、{選択肢|せんたくし}の{横|よこ}に{下|した}から{当|あ}てはまるものを{選|えら}んで{書|か}いてください。",
   "note": "Real CD track. Script and answer are printed in the book."
  },
  {
   "type": "group",
   "title": "{例題|れいだい}2　①　メモ（{下|した}から{選|えら}ぶ：パスタ・ピザ・{飲|の}み{物|もの}・サラダ・デザート・{肉|にく}か{魚|さかな}の{料理|りょうり}・パンかライス）",
   "children": [
    {
     "type": "text",
     "t": "1　Aセット：パスタ、{飲|の}み{物|もの}\n2　Bセット：ピザ、{飲|の}み{物|もの}\n3　Cセット：パスタかピザ、{飲|の}み{物|もの}、サラダ、デザート\n4　Dセット：{肉|にく}か{魚|さかな}の{料理|りょうり}、パンかライス、サラダ、デザート、{飲|の}み{物|もの}",
     "title": "{答|こた}え（{本|ほん}）"
    }
   ],
   "scored": false
  },
  {
   "type": "audio",
   "title": "{例題|れいだい}2　②　CD B38",
   "src": "audio/chokai/b38.mp3",
   "label": "CD B38",
   "t": "{次|つぎ}に{2人|ふたり}の{会話|かいわ}と{質問|しつもん}を{聞|き}いて、{上|うえ}の1から4の{中|なか}から、{最|もっと}もよいものを{選|えら}んでください。",
   "note": "Real CD track. Script and answer are printed in the book."
  },
  {
   "type": "group",
   "title": "{例題|れいだい}2　②",
   "children": [
    {
     "type": "mcq",
     "id": "d19c-e2-1",
     "q": "{質問|しつもん}1　{男|おとこ}の{人|ひと}はどのセットにしますか。",
     "opts": [
      "Aセット",
      "Bセット",
      "Cセット",
      "Dセット"
     ],
     "ans": 3,
     "keys": [
      "1",
      "2",
      "3",
      "4"
     ],
     "explain": [
      "Book's answer: 4.",
      "男の人は「ライス」「肉」と言っているので、「Dセット」です。Only Dセット has 肉か魚 and パンかライス."
     ]
    },
    {
     "type": "mcq",
     "id": "d19c-e2-2",
     "q": "{質問|しつもん}2　{女|おんな}の{人|ひと}はどのセットにしますか。",
     "opts": [
      "Aセット",
      "Bセット",
      "Cセット",
      "Dセット"
     ],
     "ans": 2,
     "keys": [
      "1",
      "2",
      "3",
      "4"
     ],
     "explain": [
      "Book's answer: 3.",
      "女の人は「パスタがいい」と言っているので「Aセット」か「Cセット」で、「デザート」の話の後、「サラダも付いている」ことを確認してから「これにしてみよう」と言っているので、「Cセット」です。",
      "Thanglish: Pasta venum → A or C. Dessert + salad irukku nu confirm panni 'idhu try pannuren' → C."
     ]
    }
   ],
   "scored": true
  },
  {
   "type": "reveal",
   "label": "{例題|れいだい}2　スクリプト（{本|ほん}）",
   "children": [
    {
     "type": "items",
     "title": "◆スクリプト",
     "lead": "Tap 💡 on each line: sensei explains it.",
     "items": [
      {
       "t": "レストランで{店員|てんいん}がメニューを{説明|せつめい}しています。",
       "explain": ""
      },
      {
       "t": "{男|おとこ}1：{本日|ほんじつ}のランチは{次|つぎ}の4{種類|しゅるい}になっております。Aセットはパスタ、Bセットはピザで、それぞれお{飲|の}み{物|もの}が{付|つ}いております。Cセットは、AセットかBセットのどちらかに、{食前|しょくぜん}のサラダと{食後|しょくご}のデザートが{付|つ}いたものです。パスタかピザをお{選|えら}びください。Dセットは、{肉|にく}か{魚|さかな}のお{料理|りょうり}と、それからパンかライスを{選|えら}んでいただいて、こちらもサラダとデザート、お{飲|の}み{物|もの}が{付|つ}いております。",
       "explain": [
        "The 4 sets. Note them as you listen: A = pasta + drink; B = pizza + drink; C = A or B + salad + dessert; D = meat or fish + bread or rice + salad + dessert + drink.",
        "食前(しょくぜん) = before the meal. 食後(しょくご) = after the meal."
       ]
      },
      {
       "t": "{女|おんな}　：どれにしようかな。{決|き}まった？",
       "explain": ""
      },
      {
       "t": "{男|おとこ}2：{今日|きょう}はたくさん{食|た}べたい{気分|きぶん}なんだよね。ちょっと{高|たか}いけど、{今日|きょう}はこれ。[[ライスにしよう]]。",
       "explain": "Rice → only D has rice."
      },
      {
       "t": "{女|おんな}　：お{肉|にく}とお{魚|さかな}が{選|えら}べるけど、どっちにする？",
       "explain": ""
      },
      {
       "t": "{男|おとこ}2：やっぱり[[{肉|にく}]]だな。",
       "explain": "Meat → D confirmed."
      },
      {
       "t": "{女|おんな}　：わたしは[[パスタがいいな]]。Aセットは850{円|えん}なのね。",
       "explain": "Pasta → A or C."
      },
      {
       "t": "{男|おとこ}2：あれ？　デザートはいいの？",
       "explain": ""
      },
      {
       "t": "{女|おんな}　：うーん。デザートが{付|つ}くと、1,200{円|えん}か。アイスクリームかケーキが{選|えら}べるんだ。",
       "explain": "With dessert = C (1,200 yen)."
      },
      {
       "t": "{男|おとこ}2：ここのケーキ、おいしいよ。それで{僕|ぼく}はいつもデザート{付|つ}きのにしてるんだ。",
       "explain": ""
      },
      {
       "t": "{女|おんな}　：ふーん。サラダも{付|つ}いてるんだっけ。じゃ、[[これにしてみよう]]。",
       "explain": "Salad and dessert → C."
      },
      {
       "t": "{質問|しつもん}1　{男|おとこ}の{人|ひと}はどのセットにしますか。\n{質問|しつもん}2　{女|おんな}の{人|ひと}はどのセットにしますか。",
       "explain": ""
      }
     ]
    },
    {
     "type": "text",
     "t": "{答|こた}え　①（{上|うえ}のメモ）　②{質問|しつもん}1　4　{質問|しつもん}2　3",
     "title": "{答|こた}え（{本|ほん}）"
    }
   ]
  },
  {
   "type": "audio",
   "title": "{練習|れんしゅう}2 (1)　①　CD B39",
   "src": "audio/chokai/b39.mp3",
   "label": "CD B39",
   "t": "{最初|さいしょ}の{話|はなし}を{聞|き}いて、{選択肢|せんたくし}の{横|よこ}に{下|した}から{当|あ}てはまるものを{選|えら}んで{書|か}いてください。",
   "note": "Real CD track. The book prints no script or answer for this one, so the script below was transcribed from the CD and checked by sensei; the answer is sensei's."
  },
  {
   "type": "group",
   "title": "{練習|れんしゅう}2 (1)　①　メモ（{下|した}から{選|えら}ぶ：バッグ・{布|ぬの}ぞうり・かご・なべ{敷|し}き／{広告|こうこく}・{古|ふる}い{布|ぬの}・{新聞紙|しんぶんし}・{葉書|はがき}）",
   "children": [
    {
     "type": "mcq",
     "id": "d19c-r21-a",
     "q": "1　Aグループ",
     "opts": [
      "バッグ／新聞紙",
      "かご／広告",
      "布ぞうり／古い布",
      "なべ{敷|し}き／葉書"
     ],
     "ans": 0,
     "keys": [
      "",
      "",
      "",
      ""
     ],
     "explain": "Aグループは新聞紙で買い物用のバッグを作ります."
    },
    {
     "type": "mcq",
     "id": "d19c-r21-b",
     "q": "2　Bグループ",
     "opts": [
      "バッグ／新聞紙",
      "かご／広告",
      "布ぞうり／古い布",
      "なべ{敷|し}き／葉書"
     ],
     "ans": 1,
     "keys": [
      "",
      "",
      "",
      ""
     ],
     "explain": "Bグループはカゴなんですが、これ、広告の紙から作るんですよ."
    },
    {
     "type": "mcq",
     "id": "d19c-r21-c",
     "q": "3　Cグループ",
     "opts": [
      "バッグ／新聞紙",
      "かご／広告",
      "布ぞうり／古い布",
      "なべ{敷|し}き／葉書"
     ],
     "ans": 2,
     "keys": [
      "",
      "",
      "",
      ""
     ],
     "explain": "Cグループはこの布ぞうりです。古い布を裂いて、ひもにして編んでいきます."
    },
    {
     "type": "mcq",
     "id": "d19c-r21-d",
     "q": "4　Dグループ",
     "opts": [
      "バッグ／新聞紙",
      "かご／広告",
      "布ぞうり／古い布",
      "なべ{敷|し}き／葉書"
     ],
     "ans": 3,
     "keys": [
      "",
      "",
      "",
      ""
     ],
     "explain": "Dグループは葉書でなべ{敷|し}きを作ります。はがきを40枚使って…"
    }
   ],
   "scored": false
  },
  {
   "type": "audio",
   "title": "{練習|れんしゅう}2 (1)　②　CD B40",
   "src": "audio/chokai/b40.mp3",
   "label": "CD B40",
   "t": "{次|つぎ}に{2人|ふたり}の{会話|かいわ}と{質問|しつもん}を{聞|き}いて、{上|うえ}の1から4の{中|なか}から、{最|もっと}もよいものを{選|えら}んでください。",
   "note": "Real CD track. The book prints no script or answer for this one, so the script below was transcribed from the CD and checked by sensei; the answer is sensei's."
  },
  {
   "type": "group",
   "title": "{練習|れんしゅう}2 (1)　②",
   "children": [
    {
     "type": "mcq",
     "id": "d19c-r21-1",
     "q": "{質問|しつもん}1　{男|おとこ}の{人|ひと}はどのグループに{入|はい}りますか。",
     "opts": [
      "Aグループ",
      "Bグループ",
      "Cグループ",
      "Dグループ"
     ],
     "ans": 0,
     "keys": [
      "1",
      "2",
      "3",
      "4"
     ],
     "explain": [
      "Sensei's answer: 1.",
      "He wants to make one for his grandma, who refuses plastic shopping bags (レジ袋を{断|ことわ}っている) → a shopping bag. At the end: 僕はやっぱりこれ。はがきは集めるのが大変そうだけど新聞紙ならいくらでもあるからね → 新聞紙 = A."
     ]
    },
    {
     "type": "mcq",
     "id": "d19c-r21-2",
     "q": "{質問|しつもん}2　{女|おんな}の{人|ひと}はどのグループに{入|はい}りますか。",
     "opts": [
      "Aグループ",
      "Bグループ",
      "Cグループ",
      "Dグループ"
     ],
     "ans": 1,
     "keys": [
      "1",
      "2",
      "3",
      "4"
     ],
     "explain": [
      "Sensei's answer: 2.",
      "She first likes the 布ぞうり (C), but it looks hard (左右2つ作らないといけない, 力がいりそう). Then: お菓子やみかんを入れておくのに喜ばれそうだから、これにしようかな → a basket = B.",
      "Thanglish: First choice change aagudhu — adhu dhaan trap. Final 'これにしようかな' paarunga."
     ]
    }
   ],
   "scored": true
  },
  {
   "type": "reveal",
   "label": "{練習|れんしゅう}2 (1)　スクリプト（CDから）",
   "children": [
    {
     "type": "items",
     "title": "◆スクリプト",
     "lead": "Tap 💡 on each line: sensei explains it.",
     "items": [
      {
       "t": "ボランティア{講習|こうしゅう}{会|かい}で{女|おんな}の{人|ひと}が{説明|せつめい}しています。",
       "explain": "講習会(こうしゅうかい) = training session."
      },
      {
       "t": "{女|おんな}1：さて、{皆|みな}さんには{来週|らいしゅう}、お{年寄|としよ}りの{施設|しせつ}に{行|い}って{小物|こもの}の{作|つく}り{方|かた}を{指導|しどう}していただきます。{今日|きょう}はその{実習|じっしゅう}なんですが、4つのグループに{分|わ}かれて{作業|さぎょう}を{行|おこな}います。",
       "explain": "小物(こもの) = small articles. 指導(しどう) = teach. 実習(じっしゅう) = practice."
      },
      {
       "t": "まず、Aグループは[[{新聞紙|しんぶんし}で{買|か}い{物|もの}{用|よう}のバッグ]]を{作|つく}ります。{丈夫|じょうぶ}でしっかりしているでしょ。",
       "explain": "A = bag from newspaper."
      },
      {
       "t": "Bグループは[[かご]]なんですが、これ、[[{広告|こうこく}の{紙|かみ}]]から{作|つく}るんですよ。このかごにはテレビのリモコンや{果物|くだもの}が{入|い}れられて{便利|べんり}です。",
       "explain": "B = basket from advertising flyers."
      },
      {
       "t": "Cグループはこの[[{布|ぬの}ぞうり]]です。[[{古|ふる}い{布|ぬの}]]を{裂|さ}いて、ひもにして{編|あ}んでいきます。このぞうり、{履|は}いたとき{気持|きも}ちいいですよ。",
       "explain": "C = cloth sandals from old cloth. 裂く(さく) = tear. 編む(あむ) = weave."
      },
      {
       "t": "{最後|さいご}にDグループは[[{葉書|はがき}でなべ{敷|し}き]]を{作|つく}ります。はがきを40{枚|まい}{使|つか}って{作|つく}るんですが、{作|つく}り{方|かた}は{簡単|かんたん}です。{熱|あつ}いお{鍋|なべ}を{置|お}いても{大丈夫|だいじょうぶ}ですよ。",
       "explain": "D = pot stand from postcards."
      },
      {
       "t": "{皆|みな}さんは{好|す}きなグループに{入|はい}って、{講師|こうし}の{先生|せんせい}から{作|つく}り{方|かた}を{教|おそ}わってください。{来週|らいしゅう}はお{年寄|としよ}りに{指導|しどう}していただきますから、{頑張|がんば}って{作|つく}ってくださいね。",
       "explain": "講師(こうし) = instructor."
      },
      {
       "t": "{男|おとこ}：{僕|ぼく}、これにしよう。うちのおばあちゃんにも{作|つく}ってあげよう。スーパーに{行|い}っても[[レジ{袋|ぶくろ}を{断|ことわ}っている]]みたいだから。",
       "explain": "Bag for grandma → A."
      },
      {
       "t": "{女|おんな}2：わたしはこれ。{部屋|へや}で{履|は}けるし、お{年寄|としよ}りは{古|ふる}い{服|ふく}、{捨|す}てられない{人|ひと}、{多|おお}いでしょ？　きっと{喜|よろこ}ばれると{思|おも}う。",
       "explain": "She likes C (sandals)…"
      },
      {
       "t": "{男|おとこ}：でも{作|つく}り{方|かた}が{難|むずか}しそうだよ。{左右|さゆう}2つ{作|つく}らないといけないし。",
       "explain": "…but they're hard: you must make two."
      },
      {
       "t": "{女|おんな}2：あ、そっか。{結構|けっこう}{力|ちから}がいりそうだしね。じゃあ、[[お{菓子|かし}やみかんを{入|い}れておくのに{喜|よろこ}ばれそうだから、これにしようかな]]。",
       "explain": "Changes to B (basket)."
      },
      {
       "t": "{男|おとこ}：{僕|ぼく}はやっぱりこれ。はがきは{集|あつ}めるのが{大変|たいへん}そうだけど、[[{新聞紙|しんぶんし}ならいくらでもある]]からね。",
       "explain": "Stays with A."
      },
      {
       "t": "{質問|しつもん}1　{男|おとこ}の{人|ひと}はどのグループに{入|はい}りますか。\n{質問|しつもん}2　{女|おんな}の{人|ひと}はどのグループに{入|はい}りますか。",
       "explain": ""
      }
     ]
    },
    {
     "type": "text",
     "t": "{答|こた}え　①1 バッグ・{新聞紙|しんぶんし}　2 かご・{広告|こうこく}　3 {布|ぬの}ぞうり・{古|ふる}い{布|ぬの}　4 なべ{敷|し}き・{葉書|はがき}　②{質問|しつもん}1　1　{質問|しつもん}2　2",
     "title": "{答|こた}え（sensei）"
    }
   ]
  },
  {
   "type": "audio",
   "title": "{練習|れんしゅう}2 (2)　①　CD B41",
   "src": "audio/chokai/b41.mp3",
   "label": "CD B41",
   "t": "{最初|さいしょ}の{話|はなし}を{聞|き}いて、{選択肢|せんたくし}の{横|よこ}にメモを{書|か}いてください。",
   "note": "Real CD track. The book prints no script or answer for this one, so the script below was transcribed from the CD and checked by sensei; the answer is sensei's."
  },
  {
   "type": "group",
   "title": "{練習|れんしゅう}2 (2)　①　メモ",
   "children": [
    {
     "type": "mcq",
     "id": "d19c-r22-a",
     "q": "1　A{会場|かいじょう}",
     "opts": [
      "野菜・果物・花の販売",
      "もちつき",
      "伝統的な遊びの体験・ゲーム大会",
      "人形づくり（見学・指導）"
     ],
     "ans": 0,
     "keys": [
      "",
      "",
      "",
      ""
     ],
     "explain": "A会場では、今朝採れたばかりの野菜や果物、そして花などを販売しております."
    },
    {
     "type": "mcq",
     "id": "d19c-r22-b",
     "q": "2　B{会場|かいじょう}",
     "opts": [
      "野菜・果物・花の販売",
      "もちつき",
      "伝統的な遊びの体験・ゲーム大会",
      "人形づくり（見学・指導）"
     ],
     "ans": 1,
     "keys": [
      "",
      "",
      "",
      ""
     ],
     "explain": "B会場ではもちつきを行います。出来上がったお餅はその場で召し上がっていただけます."
    },
    {
     "type": "mcq",
     "id": "d19c-r22-c",
     "q": "3　C{会場|かいじょう}",
     "opts": [
      "野菜・果物・花の販売",
      "もちつき",
      "伝統的な遊びの体験・ゲーム大会",
      "人形づくり（見学・指導）"
     ],
     "ans": 2,
     "keys": [
      "",
      "",
      "",
      ""
     ],
     "explain": "C会場はこの地方の伝統的な遊びの体験とゲーム大会を行います。親子でご一緒にご参加ください."
    },
    {
     "type": "mcq",
     "id": "d19c-r22-d",
     "q": "4　D{会場|かいじょう}",
     "opts": [
      "野菜・果物・花の販売",
      "もちつき",
      "伝統的な遊びの体験・ゲーム大会",
      "人形づくり（見学・指導）"
     ],
     "ans": 3,
     "keys": [
      "",
      "",
      "",
      ""
     ],
     "explain": "D会場では人形づくりを見ていただけます。また作り方の指導もいたします."
    }
   ],
   "scored": false
  },
  {
   "type": "audio",
   "title": "{練習|れんしゅう}2 (2)　②　CD B42",
   "src": "audio/chokai/b42.mp3",
   "label": "CD B42",
   "t": "{次|つぎ}に{2人|ふたり}の{会話|かいわ}と{質問|しつもん}を{聞|き}いて、{上|うえ}の1から4の{中|なか}から、{最|もっと}もよいものを{選|えら}んでください。",
   "note": "Real CD track. On this CD copy the 質問1 announcement is silent (only 質問2 is heard). 質問1 below is sensei's version of the question, built from the conversation; both answers are sensei's."
  },
  {
   "type": "group",
   "title": "{練習|れんしゅう}2 (2)　②",
   "children": [
    {
     "type": "mcq",
     "id": "d19c-r22-1",
     "q": "{質問|しつもん}1（sensei）　{女|おんな}の{人|ひと}は{最初|さいしょ}にどの{会場|かいじょう}へ{行|い}きますか。",
     "opts": [
      "A{会場|かいじょう}",
      "B{会場|かいじょう}",
      "C{会場|かいじょう}",
      "D{会場|かいじょう}"
     ],
     "ans": 3,
     "keys": [
      "1",
      "2",
      "3",
      "4"
     ],
     "explain": [
      "Sensei's answer: 4.",
      "わたしは先に人形を作るところを見てから、花とか野菜を見てきたい → first D (dolls), then A (vegetables). 先に = first."
     ]
    },
    {
     "type": "mcq",
     "id": "d19c-r22-2",
     "q": "{質問|しつもん}2　{男|おとこ}の{人|ひと}は{最初|さいしょ}にどの{会場|かいじょう}へ{行|い}きますか。",
     "opts": [
      "A{会場|かいじょう}",
      "B{会場|かいじょう}",
      "C{会場|かいじょう}",
      "D{会場|かいじょう}"
     ],
     "ans": 2,
     "keys": [
      "1",
      "2",
      "3",
      "4"
     ],
     "explain": [
      "Sensei's answer: 3.",
      "He rejects もちつき (学校でもする機会がある) and wants 子供と一緒に参加できるもの; 昔の遊びなんか懐かしい → C会場 (traditional games, 親子でご一緒に).",
      "Thanglish: Amma 'saapadu idam (B)' nu solraanga, appa 'school-la mochi panniyiruppaan, kid kooda serndhu vilayaadra idam' nu C choose pannuraar."
     ]
    }
   ],
   "scored": true
  },
  {
   "type": "reveal",
   "label": "{練習|れんしゅう}2 (2)　スクリプト（CDから）",
   "children": [
    {
     "type": "items",
     "title": "◆スクリプト",
     "lead": "Tap 💡 on each line: sensei explains it.",
     "items": [
      {
       "t": "ふるさと{祭|まつ}りの{会場|かいじょう}でアナウンスをしています。",
       "explain": ""
      },
      {
       "t": "{女|おんな}1：{本日|ほんじつ}は、ふるさと{祭|まつ}りにようこそおいでくださいました。{広場|ひろば}の{周|まわ}りの4つの{会場|かいじょう}で、それぞれ{楽|たの}しいイベントを{行|い}っております。",
       "explain": ""
      },
      {
       "t": "[[A{会場|かいじょう}]]では、{今朝|けさ}{採|と}れたばかりの[[{野菜|やさい}や{果物|くだもの}、そして{花|はな}]]などを{販売|はんばい}しております。",
       "explain": "A = selling vegetables, fruit, flowers."
      },
      {
       "t": "[[B{会場|かいじょう}]]では[[もちつき]]を{行|おこな}います。{出来上|できあ}がったお{餅|もち}はその{場|ば}で{召|め}し{上|あ}がっていただけます。",
       "explain": "B = pounding rice cakes; you can eat them there."
      },
      {
       "t": "[[C{会場|かいじょう}]]はこの{地方|ちほう}の[[{伝統|でんとう}{的|てき}な{遊|あそ}びの{体験|たいけん}とゲーム{大会|たいかい}]]を{行|おこな}います。{親子|おやこ}でご{一緒|いっしょ}にご{参加|さんか}ください。",
       "explain": "C = traditional games, parents and children together."
      },
      {
       "t": "そして[[D{会場|かいじょう}]]では[[{人形|にんぎょう}づくり]]を{見|み}ていただけます。また、{作|つく}り{方|かた}の{指導|しどう}もいたしますので、{皆様|みなさま}どうぞおいでください。",
       "explain": "D = watching / learning doll-making."
      },
      {
       "t": "{女|おんな}2：どの{会場|かいじょう}もみんな{面白|おもしろ}そうね。でも、この{子|こ}が{楽|たの}しめるところというと、やっぱり{食|た}べるところかしらね。おもちつきなんかどう？",
       "explain": "She suggests B for the child."
      },
      {
       "t": "{男|おとこ}：もちつきは{学校|がっこう}でもする{機会|きかい}があるんじゃない？　せっかくの{機会|きかい}だから[[{子供|こども}と{一緒|いっしょ}に{参加|さんか}できるもの]]にしたいな。[[{昔|むかし}の{遊|あそ}び]]なんか{懐|なつ}かしいし。",
       "explain": "He chooses C."
      },
      {
       "t": "{女|おんな}2：そう。わたしは[[{先|さき}に{人形|にんぎょう}を{作|つく}るところを{見|み}て]]から、{花|はな}とか{野菜|やさい}を{見|み}てきたいんだけど、いい？　{今晩|こんばん}のおかずも{探|さが}せそうだし。",
       "explain": "She goes to D first, then A."
      },
      {
       "t": "{男|おとこ}：わかった。じゃあ、ここで{一旦|いったん}{別|わか}れて、{後|あと}で{広場|ひろば}で{会|あ}おう。",
       "explain": "一旦(いったん) = for a while."
      },
      {
       "t": "{質問|しつもん}2　{男|おとこ}の{人|ひと}は{最初|さいしょ}にどの{会場|かいじょう}へ{行|い}きますか。",
       "explain": ""
      }
     ]
    },
    {
     "type": "text",
     "t": "{答|こた}え　①1 {野菜|やさい}・{果物|くだもの}・{花|はな}の{販売|はんばい}　2 もちつき　3 {伝統|でんとう}{的|てき}な{遊|あそ}びの{体験|たいけん}・ゲーム{大会|たいかい}　4 {人形|にんぎょう}づくり　②{質問|しつもん}1（sensei）4　{質問|しつもん}2　3",
     "title": "{答|こた}え（sensei）"
    }
   ]
  },
  {
   "type": "audio",
   "title": "{確認|かくにん}{問題|もんだい} (1)　CD B43",
   "src": "audio/chokai/b43.mp3",
   "label": "CD B43",
   "t": "まず{話|はなし}を{聞|き}いてください。それから、{質問|しつもん}と{選択肢|せんたくし}を{聞|き}いて、1から4の{中|なか}から、{最|もっと}もよいものを{一|ひと}つ{選|えら}んでください。",
   "note": "Real CD track. The book prints no script or answer for this one, so the script below was transcribed from the CD and checked by sensei; the answer is sensei's."
  },
  {
   "type": "group",
   "title": "{確認|かくにん}{問題|もんだい} (1)",
   "children": [
    {
     "type": "mcq",
     "id": "d19c-k1",
     "q": "（{質問|しつもん}と{選択肢|せんたくし}はCDで{聞|き}きます）",
     "opts": [
      "1",
      "2",
      "3",
      "4"
     ],
     "ans": 3,
     "keys": [
      "1",
      "2",
      "3",
      "4"
     ],
     "explain": [
      "Sensei's answer: 4.",
      "Question: 女の人が夜行バスで行きたいと思った理由は何ですか。 1 乗り換えがないから　2 4時に起きられないから　3 リラックスできるから　4 テントに泊まりたくないから",
      "She worried she couldn't sleep on the bus. The other option was staying near the mountain the night before — but rooms are full, so it would be a tent. 「えっ、テントに泊まるの？　それだけは勘弁してよ」 → then she agrees: わかった、バスにしよう. So the deciding reason is 4.",
      "Trap: 1 (乗り換えもないし楽) and the low price were said, but they didn't decide it for her."
     ]
    }
   ],
   "scored": true
  },
  {
   "type": "reveal",
   "label": "{確認|かくにん}{問題|もんだい} (1)　スクリプト（CDから）",
   "children": [
    {
     "type": "items",
     "title": "◆スクリプト",
     "lead": "Tap 💡 on each line: sensei explains it.",
     "items": [
      {
       "t": "{友達|ともだち}3{人|にん}が{山|やま}へ{行|い}く{相談|そうだん}をしています。",
       "explain": ""
      },
      {
       "t": "{男|おとこ}1：{大空山|おおぞらやま}までは、やっぱり{電車|でんしゃ}とバスを{乗|の}り{継|つ}いでいくしかないのかなあ。",
       "explain": "乗り継ぐ(のりつぐ) = change trains/buses."
      },
      {
       "t": "{女|おんな}：5{時|じ}の{電車|でんしゃ}で{行|い}けば、{上|うえ}まで{登|のぼ}って、{暗|くら}くなる{前|まえ}に{山|やま}を{降|お}りて{来|こ}られるかしら。",
       "explain": ""
      },
      {
       "t": "{男|おとこ}2：じゃあ、4{時|じ}{起|お}きか。{大変|たいへん}だね。{夜行|やこう}バスはどう？　{夜行|やこう}バスなら{半分|はんぶん}ぐらいの{値段|ねだん}で{行|い}けるし。",
       "explain": "夜行(やこう)バス = overnight bus."
      },
      {
       "t": "{男|おとこ}1：{夜行|やこう}バスかあ。{乗|の}り{換|か}えもないし、{楽|らく}かもね。",
       "explain": ""
      },
      {
       "t": "{女|おんな}：{確|たし}かに{安|やす}いのは{魅力|みりょく}だけど、バスの{中|なか}で{眠|ねむ}れるかしら。",
       "explain": "She is worried about sleeping."
      },
      {
       "t": "{男|おとこ}2：{大丈夫|だいじょうぶ}だよ。{最近|さいきん}のバスはシートも{広|ひろ}くて、ベッドみたいに{倒|たお}せるんだって。",
       "explain": ""
      },
      {
       "t": "{男|おとこ}1：{前|まえ}の{日|ひ}にぐっすり{寝|ね}たかったら、{前日|ぜんじつ}どこかに{宿|やど}を{取|と}るか。でも、もう{予約|よやく}はいっぱいだろうから、テントかなあ。",
       "explain": "The alternative: a tent."
      },
      {
       "t": "{女|おんな}：えっ、[[テントに{泊|と}まるの？　それだけは{勘弁|かんべん}してよ]]。",
       "explain": "勘弁(かんべん)して = please spare me. → the reason."
      },
      {
       "t": "{男|おとこ}1：そうだよな。{荷物|にもつ}{増|ふ}えちゃうしな。",
       "explain": ""
      },
      {
       "t": "{男|おとこ}2：じゃあ、やっぱり{夜行|やこう}しかないでしょう。",
       "explain": ""
      },
      {
       "t": "{女|おんな}：わかった。バスにしよう。",
       "explain": ""
      },
      {
       "t": "{女|おんな}の{人|ひと}が{夜行|やこう}バスで{行|い}きたいと{思|おも}った{理由|りゆう}は{何|なに}ですか。\n1　{乗|の}り{換|か}えがないから\n2　4{時|じ}に{起|お}きられないから\n3　リラックスできるから\n4　テントに{泊|と}まりたくないから",
       "explain": ""
      }
     ]
    },
    {
     "type": "text",
     "t": "{答|こた}え　4（sensei）\nSpeaker labels are sensei's best reading of the voices; the answer doesn't depend on them.",
     "title": "{答|こた}え"
    }
   ]
  },
  {
   "type": "audio",
   "title": "{確認|かくにん}{問題|もんだい} (2)　CD B44",
   "src": "audio/chokai/b44.mp3",
   "label": "CD B44",
   "t": "まず{話|はなし}を{聞|き}いてください。それから、{二|ふた}つの{質問|しつもん}を{聞|き}いて、それぞれ1から4の{中|なか}から、{最|もっと}もよいものを{一|ひと}つ{選|えら}んでください。",
   "note": "Real CD track. The book prints no script or answer for this one, so the script below was transcribed from the CD and checked by sensei; the answer is sensei's."
  },
  {
   "type": "group",
   "title": "{確認|かくにん}{問題|もんだい} (2)",
   "children": [
    {
     "type": "mcq",
     "id": "d19c-k2-1",
     "q": "{質問|しつもん}1　{女|おんな}の{人|ひと}はどのセットを{選|えら}びますか。",
     "opts": [
      "ありがとうセット",
      "しあわせセット",
      "ふんわりセット",
      "うきうきセット"
     ],
     "ans": 1,
     "keys": [
      "1",
      "2",
      "3",
      "4"
     ],
     "explain": [
      "Sensei's answer: 2.",
      "うちのお母さん、甘いもの好きだから、これにしようかな → しあわせセット (two kinds of sweets + tea). She rejects flowers: 水やったりするの面倒くさがるんだ."
     ]
    },
    {
     "type": "mcq",
     "id": "d19c-k2-2",
     "q": "{質問|しつもん}2　{男|おとこ}の{人|ひと}はどのセットを{選|えら}びますか。",
     "opts": [
      "ありがとうセット",
      "しあわせセット",
      "ふんわりセット",
      "うきうきセット"
     ],
     "ans": 3,
     "keys": [
      "1",
      "2",
      "3",
      "4"
     ],
     "explain": [
      "Sensei's answer: 4.",
      "He first thinks of ふんわり (料理のときに使ってもらえるもの), but she says his mum is stylish (おしゃれ), and he remembers 最近は絵を習い始めて外に出ることも増えた → じゃあ、これにしよう = うきうきセット (scarf + parasol, for stylish mothers who go out a lot)."
     ]
    }
   ],
   "scored": true
  },
  {
   "type": "reveal",
   "label": "{確認|かくにん}{問題|もんだい} (2)　スクリプト（CDから）",
   "children": [
    {
     "type": "items",
     "title": "◆スクリプト",
     "lead": "Tap 💡 on each line: sensei explains it.",
     "items": [
      {
       "t": "デパートで{店員|てんいん}が{話|はな}しています。",
       "explain": ""
      },
      {
       "t": "{女|おんな}1：{母|はは}の{日|ひ}のプレゼントですか。それなら……。この[[ありがとうセット]]は、{母|はは}の{日|ひ}の{花|はな}、[[{赤|あか}いカーネーションにクッキー]]を{添|そ}えたセットでございます。",
       "explain": "ありがとう = carnation + cookies. 添える(そえる) = add."
      },
      {
       "t": "{次|つぎ}にこちらの[[しあわせセット]]は、[[お{菓子|かし}2{種類|しゅるい}と{紅茶|こうちゃ}]]のセットで、お{好|す}きなお{菓子|かし}が{選|えら}べます。",
       "explain": "しあわせ = 2 sweets + tea."
      },
      {
       "t": "それからこちらの[[ふんわりセット]]は、[[{柔|やわ}らかいタオルとエプロン]]のセットです。{台所|だいどころ}の{仕事|しごと}が{多|おお}いお{母様|かあさま}に{喜|よろこ}ばれます。",
       "explain": "ふんわり = towel + apron, for mothers who cook a lot."
      },
      {
       "t": "{最後|さいご}は[[うきうきセット]]ですが、[[おしゃれなスカーフと{日傘|ひがさ}]]のセットです。スカーフと{日傘|ひがさ}の{柄|がら}が{合|あ}っていて、[[{外出|がいしゅつ}の{多|おお}いおしゃれなお{母様|かあさま}]]にぴったりのセットです。",
       "explain": "うきうき = scarf + parasol, for stylish mothers who go out a lot. 柄(がら) = pattern."
      },
      {
       "t": "{女|おんな}2：うちのお{母|かあ}さん、[[{甘|あま}いもの{好|す}きだから]]、これにしようかな。",
       "explain": "→ しあわせ."
      },
      {
       "t": "{男|おとこ}：え？　お{花|はな}はいいの？",
       "explain": ""
      },
      {
       "t": "{女|おんな}2：うん、{水|みず}やったりするの、{面倒|めんどう}くさがるんだ。",
       "explain": "No flowers."
      },
      {
       "t": "{男|おとこ}：ふーん。{僕|ぼく}は{料理|りょうり}のときに{使|つか}ってもらえるものにしようかな。",
       "explain": "He's thinking of ふんわり…"
      },
      {
       "t": "{女|おんな}2：でも、つよし{君|くん}のお{母|かあ}さん、おしゃれだから、これもいいんじゃない？",
       "explain": "…she suggests うきうき."
      },
      {
       "t": "{男|おとこ}：ああ、そういえば{最近|さいきん}は{絵|え}を{習|なら}い{始|はじ}めて、{外|そと}に{出|で}ることも{増|ふ}えたしね。[[じゃあ、これにしよう]]。",
       "explain": "→ うきうき."
      },
      {
       "t": "{質問|しつもん}1　{女|おんな}の{人|ひと}はどのセットを{選|えら}びますか。\n{質問|しつもん}2　{男|おとこ}の{人|ひと}はどのセットを{選|えら}びますか。",
       "explain": ""
      }
     ]
    },
    {
     "type": "text",
     "t": "{答|こた}え　{質問|しつもん}1　2　{質問|しつもん}2　4（sensei）",
     "title": "{答|こた}え"
    }
   ]
  }
 ]
});
