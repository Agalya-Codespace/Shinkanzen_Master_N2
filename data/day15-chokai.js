/* Day 15 · chokai. Built from d15_chokai.py by tools/build_day.py (furigana added automatically). */
window.N2_DAYS = window.N2_DAYS || {};
window.N2_DAYS[15] = window.N2_DAYS[15] || {"title": "", "intro": "", "sections": []};
if (false) window.N2_DAYS[15].title = "";
if (false) window.N2_DAYS[15].intro = "";
window.N2_DAYS[15].sections.push({
 "book": "chokai",
 "title": "{実力|じつりょく}{養成|ようせい}{編|へん}　Ⅴ「{概要|がいよう}{理解|りかい}」　2 キーワードを{関連|かんれん}づけて、{話|はなし}の{構造|こうぞう}をつかむ",
 "source": "新完全マスター聴解 N2 · 実力養成編 Ⅴ-2 · pp.70–75 · CD A82–A83 (read-aloud of the book's script), CD B01–B09 (real CD)",
 "blocks": [
  {
   "type": "items",
   "title": "2　キーワードを{関連|かんれん}づけて、{話|はなし}の{構造|こうぞう}をつかむ",
   "items": [
    {
     "t": "ここでは、キーワード（{話|はなし}の{中|なか}で{大切|たいせつ}だと{思|おも}われる{言葉|ことば}）を{関連|かんれん}づけて、{話|はなし}の{構造|こうぞう}をつかむ{練習|れんしゅう}をします。",
     "explain": "Sensei: Yesterday we sorted 'example' words from 'summing-up' words. Today we go one step further: draw a little map of how the keywords connect. Is it A → B → C (a change)? One topic split in two? A list under one heading? Once the map is clear, the 'what is it about?' answer is obvious."
    }
   ]
  },
  {
   "type": "text",
   "t": "①{話|はなし}を{聞|き}いてください。この{話|はなし}はどのような{構造|こうぞう}になっていますか。キーワードを{関連|かんれん}づけて{考|かんが}えてください。",
   "title": "☆{例題|れいだい}2"
  },
  {
   "type": "audio",
   "title": "{例題|れいだい}2 ①　CD A82",
   "src": "audio/chokai/a82.mp3",
   "label": "A82 · computer read-aloud of the book's script"
  },
  {
   "type": "group",
   "title": "{例題|れいだい}2 ①",
   "children": [
    {
     "type": "mcq",
     "id": "d15c-e2-1",
     "q": "　どのような{構造|こうぞう}ですか。\na　{教師|きょうし} ― {学生|がくせい} ― {児童|じどう} ― {生徒|せいと}\nb　{学校|がっこう} ┬ {教|おし}える{人|ひと} ― {教師|きょうし}\n　　　　└ {習|なら}う{人|ひと} ― {学生|がくせい}\nc　{習|なら}う{人|ひと} ┬ {児童|じどう}\n　　　　　├ {生徒|せいと}\n　　　　　└ {学生|がくせい}",
     "opts": [
      "a",
      "b",
      "c"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": [
      "Book's answer: c.",
      "最初に「教える人」「習う人」という対立する2つの言葉を紹介してから、「勉強する立場の人たちを何と言いますか」と聞いているので、「勉強する立場の人＝習う人」が重要なキーワードです。その後に続く「学生」「児童」「生徒」が「習う人」の「呼び方」の例です。したがって、この「習う人の呼び方」が話の中心だと整理できます。このようなキーワードの関係を表しているのはcです。"
     ]
    }
   ],
   "scored": true
  },
  {
   "type": "audio",
   "title": "{例題|れいだい}2 ②　CD A82 → A83",
   "src": "audio/chokai/a83.mp3",
   "label": "A83 · computer read-aloud of the book's question",
   "t": "②もう{一度|いちど}{話|はなし}を{聞|き}いてください。その{後|ご}で{質問|しつもん}に{答|こた}えてください。"
  },
  {
   "type": "group",
   "title": "{例題|れいだい}2 ②",
   "children": [
    {
     "type": "mcq",
     "id": "d15c-e2-2",
     "q": "Choose 1–3 (the question and choices are in the audio).",
     "opts": [
      "1",
      "2",
      "3"
     ],
     "ans": 1,
     "keys": [
      "",
      "",
      ""
     ],
     "explain": [
      "Book's answer: 2 (習う人たちの呼び方).",
      "Thanglish: 教師 is only mentioned once. The rest — 児童, 生徒, 学生 — are all names for the LEARNERS, changing with age. So the talk is about what learners are called."
     ]
    }
   ],
   "scored": true
  },
  {
   "type": "reveal",
   "label": "{例題|れいだい}2　スクリプトと{答|こた}え（{本|ほん}）",
   "children": [
    {
     "type": "items",
     "title": "◆スクリプト",
     "lead": "Tap 💡 on each line: sensei explains it.",
     "items": [
      {
       "t": "テレビで{女|おんな}の{人|ひと}が{話|はな}しています。",
       "explain": "Situation."
      },
      {
       "t": "{女|おんな}：{学校|がっこう}っていうと、[[{教|おし}える{人|ひと}]]がいて、[[{習|なら}う{人|ひと}]]たちがいる{場|ば}を{考|かんが}えますね。{教|おし}える{立場|たちば}の{人|ひと}は「{教師|きょうし}」です。その{教師|きょうし}の{下|した}で{勉強|べんきょう}する{立場|たちば}の{人|ひと}たちを[[{何|なん}と{言|い}いますか]]。",
       "explain": "Two contrasting words, then the question → 習う人 is the key."
      },
      {
       "t": "「{学生|がくせい}」でしょうか。{実|じつ}はこれは、{通|かよ}っている{学校|がっこう}によって{違|ちが}います。{通常|つうじょう}は{年齢|ねんれい}で[[{呼|よ}び{方|かた}]]が{変|か}わると{言|い}えるでしょう。",
       "explain": "呼び方 = the summing-up word."
      },
      {
       "t": "{小学生|しょうがくせい}なら「[[{児童|じどう}]]」、{中学生|ちゅうがくせい}、{高校生|こうこうせい}なら「[[{生徒|せいと}]]」、{専門|せんもん}{学校|がっこう}や{大学|だいがく}に{通|かよ}う{人|ひと}は「[[{学生|がくせい}]]」で、「7{歳|さい}の{学生|がくせい}」というのは{普通|ふつう}はありません。また、「{生徒|せいと}たちの{運動会|うんどうかい}」といえば、{中学校|ちゅうがっこう}か{高校|こうこう}の{運動会|うんどうかい}を{意味|いみ}します。",
       "explain": "Examples of 呼び方."
      },
      {
       "t": "{女|おんな}の{人|ひと}は{何|なに}について{話|はな}していますか。\n1　{教|おし}える{人|ひと}と{習|なら}う{人|ひと}との{関係|かんけい}\n2　{習|なら}う{人|ひと}たちの{呼|よ}び{方|かた}\n3　{習|なら}う{人|ひと}の{学校|がっこう}での{立場|たちば}",
       "explain": "Question and choices."
      }
     ]
    },
    {
     "type": "text",
     "t": "{答|こた}え　①c　②2",
     "title": "{答|こた}え（{本|ほん}）"
    }
   ]
  },
  {
   "type": "text",
   "t": "Now the same two steps with real CD tracks. Step ① choose the structure a–c; step ② listen again and choose 1–3.",
   "title": "{練習|れんしゅう}2",
   "explain": [
    "Thanglish: Mudhalla map, appuram answer. Map correct-aa irundhaa answer easy."
   ]
  },
  {
   "type": "audio",
   "title": "{練習|れんしゅう}2 (1)　CD B01",
   "src": "audio/chokai/b01.mp3",
   "label": "CD B01",
   "t": "①{話|はなし}を{聞|き}いてください。この{話|はなし}はどのような{構造|こうぞう}になっていますか。キーワードを{関連|かんれん}づけて{考|かんが}えてください。",
   "note": "Real CD track. The book prints no script or answer for 練習 and ステップアップ, so the script below was transcribed from the CD and checked by sensei; the answers are sensei's."
  },
  {
   "type": "group",
   "title": "{練習|れんしゅう}2 (1)",
   "children": [
    {
     "type": "mcq",
     "id": "d15c-r2-1a",
     "q": "①　どのような{構造|こうぞう}ですか。\na　ぶり ┬ いなだ／はまち／わらさ／めじろ\nb　ぶり ┬ {関東|かんとう} …… いなだ → わらさ → ぶり\n　　　　└ {関西|かんさい} …… はまち → めじろ → ぶり\nc　{名前|なまえ}が{変|か}わる{魚|さかな} ┬ {関東|かんとう} ┬ さんま／ぶり／いなだ\n　　　　　　　　　└ {関西|かんさい} ── はまち",
     "opts": [
      "a",
      "b",
      "c"
     ],
     "ans": 1,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": [
      "Answer b.",
      "関東では若い時がイナダ、そしてワラサ、それからブリ — 関西ではハマチ、メジロ、そしてブリ. Two regions, each with a growth sequence (→). That's b.",
      "a forgets the regions and the order; c puts さんま (a different fish) in the list."
     ]
    },
    {
     "type": "mcq",
     "id": "d15c-r2-1b",
     "q": "②　CD B01 → B02　{女|おんな}の{人|ひと}は{何|なに}について{話|はな}していますか。\n1　ぶりという{魚|さかな}の{種類|しゅるい}\n2　ぶりの{呼|よ}び{方|かた}の{変化|へんか}\n3　ぶりの{成長|せいちょう}の{地域|ちいき}{性|せい}",
     "opts": [
      "1",
      "2",
      "3"
     ],
     "ans": 1,
     "keys": [
      "",
      "",
      ""
     ],
     "explain": [
      "Answer 2.",
      "Key sentence: ブリは成長段階によって呼び方が変わるのです. The whole talk is about the names changing as the fish grows.",
      "1: いなだ・はまち are not other kinds — 実はこのイナダもハマチもブリと同じ魚です. 3: the regions differ in the NAMES, not in how it grows."
     ]
    }
   ],
   "scored": true
  },
  {
   "type": "audio",
   "title": "{練習|れんしゅう}2 (1) {質問|しつもん}　CD B02",
   "src": "audio/chokai/b02.mp3",
   "label": "CD B02"
  },
  {
   "type": "reveal",
   "label": "{練習|れんしゅう}2 (1)　スクリプト（CDから） · open after you answer",
   "children": [
    {
     "type": "items",
     "title": "◆スクリプト",
     "lead": "Tap 💡 on each line: sensei explains it.",
     "items": [
      {
       "t": "テレビで{女|おんな}の{人|ひと}が{話|はな}しています。",
       "explain": ""
      },
      {
       "t": "{女|おんな}：{秋|あき}においしい{魚|さかな}といえば、ぶりがサンマやサケと{並|なら}んで{有名|ゆうめい}です。ほかにもイナダやハマチが{秋|あき}においしい{魚|さかな}としてよくあげられますが、[[{実|じつ}はこのイナダもハマチもブリと{同|おな}じ{魚|さかな}です]]。",
       "explain": "実は → surprise fact: same fish."
      },
      {
       "t": "ブリは[[{成長|せいちょう}{段階|だんかい}によって{呼|よ}び{方|かた}が{変|か}わる]]のです。",
       "explain": "★ Main point."
      },
      {
       "t": "[[{関東|かんとう}]]では{若|わか}い{時|とき}がイナダ、そしてワラサ、それからブリになり、[[{関西|かんさい}]]ではハマチ、メジロ、そしてブリの{順|じゅん}に{大|おお}きくなります。",
       "explain": "Two regions × growth order → structure b."
      },
      {
       "t": "{最近|さいきん}では{関西|かんさい}の{呼|よ}び{方|かた}であるハマチが{広|ひろ}く{知|し}られるようになりましたが、ブリとは{別|べつ}の{魚|さかな}だと{思|おも}っている{人|ひと}もいるようです。",
       "explain": ""
      },
      {
       "t": "{女|おんな}の{人|ひと}は{何|なに}について{話|はな}していますか。\n1　ぶりという{魚|さかな}の{種類|しゅるい}\n2　ぶりの{呼|よ}び{方|かた}の{変化|へんか}\n3　ぶりの{成長|せいちょう}の{地域|ちいき}{性|せい}",
       "explain": ""
      }
     ]
    },
    {
     "type": "text",
     "t": "{答|こた}え　①b　②2",
     "title": "{答|こた}え"
    }
   ]
  },
  {
   "type": "audio",
   "title": "{練習|れんしゅう}2 (2)　CD B03",
   "src": "audio/chokai/b03.mp3",
   "label": "CD B03",
   "t": "①{話|はなし}を{聞|き}いてください。この{話|はなし}はどのような{構造|こうぞう}になっていますか。キーワードを{関連|かんれん}づけて{考|かんが}えてください。",
   "note": "Real CD track. The book prints no script or answer for 練習 and ステップアップ, so the script below was transcribed from the CD and checked by sensei; the answers are sensei's."
  },
  {
   "type": "group",
   "title": "{練習|れんしゅう}2 (2)",
   "children": [
    {
     "type": "mcq",
     "id": "d15c-r2-2a",
     "q": "①　どのような{構造|こうぞう}ですか。\na　{世話|せわ}をする{所|ところ} ┬ ペットホテル／{保育所|ほいくしょ}／ペットシッター／ベビーシッター\nb　{世話|せわ}をする{所|ところ} ┬ ペットホテル ― ペットシッター\n　　　　　　　　└ {保育所|ほいくしょ} ― ベビーシッター\nc　{世話|せわ}をする{所|ところ} ┬ ペットホテル …… {店|みせ}\n　　　　　　　　└ ペットシッター …… {自宅|じたく}",
     "opts": [
      "a",
      "b",
      "c"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": [
      "Answer c.",
      "The two places that look after pets are ペットホテル (you take the pet to the 店) and ペットシッター (they come to your 自宅). {保育所|ほいくしょ} and ベビーシッター are only comparisons (のようなもの, ～のように).",
      "a, b treat the comparisons as real kinds of 世話をする所."
     ]
    },
    {
     "type": "mcq",
     "id": "d15c-r2-2b",
     "q": "②　CD B03 → B04　{男|おとこ}の{人|ひと}は{何|なに}について{話|はな}していますか。\n1　ペットと{赤|あか}ちゃんを{世話|せわ}するところの{共通|きょうつう}{点|てん}\n2　{子供|こども}とペットの{世話|せわ}をするところの{種類|しゅるい}\n3　ペットホテルとペットシッターの{違|ちが}い",
     "opts": [
      "1",
      "2",
      "3"
     ],
     "ans": 2,
     "keys": [
      "",
      "",
      ""
     ],
     "explain": [
      "Answer 3.",
      "He contrasts the two: ペットホテル = take the pet to the shop (but some pets get stressed by the change); ペットシッター = comes to your home, less stress. しかし marks the contrast.",
      "1, 2: the baby/child things are only comparisons to help you imagine."
     ]
    }
   ],
   "scored": true
  },
  {
   "type": "audio",
   "title": "{練習|れんしゅう}2 (2) {質問|しつもん}　CD B04",
   "src": "audio/chokai/b04.mp3",
   "label": "CD B04"
  },
  {
   "type": "reveal",
   "label": "{練習|れんしゅう}2 (2)　スクリプト（CDから） · open after you answer",
   "children": [
    {
     "type": "items",
     "title": "◆スクリプト",
     "lead": "Tap 💡 on each line: sensei explains it.",
     "items": [
      {
       "t": "テレビで{男|おとこ}の{人|ひと}が{話|はな}しています。",
       "explain": ""
      },
      {
       "t": "{男|おとこ}：{出張|しゅっちょう}や{旅行|りょこう}などで{家|いえ}を{留守|るす}にするとき、かわいいペットの{世話|せわ}をどうしますか。そんなとき{気軽|きがる}に{利用|りよう}できるのが[[ペットホテル]]です。",
       "explain": "Topic 1."
      },
      {
       "t": "ペットホテルは{飼|か}い{主|ぬし}がペットを[[{店|みせ}まで{連|つ}れて{行|い}って]]そこで{面倒|めんどう}を{見|み}てもらうので、{子供|こども}を{預|あづ}ける{保育所|ほいくしょ}のようなものです。{散歩|さんぽ}や{餌|えさ}の{心配|しんぱい}もなく{安心|あんしん}して{預|あづ}けられます。",
       "explain": "保育所のようなもの = comparison only."
      },
      {
       "t": "[[しかし]]ペットによっては{環境|かんきょう}が{変|か}わってストレスを{感|かん}じ、{元気|げんき}がなくなってしまうこともあります。そのようなペットには[[ペットシッター]]が{便利|べんり}です。",
       "explain": "しかし → contrast, topic 2."
      },
      {
       "t": "ペットシッターはベビーシッターが{赤|あか}ちゃんの{家|いえ}に{来|き}て{面倒|めんどう}を{見|み}てくれるように、[[{自宅|じたく}まで{来|き}て]]{散歩|さんぽ}に{連|つ}れて{行|い}ってくれたり{餌|えさ}をやってくれたりするので、ペットにとってはストレスが{少|すく}なくて{済|す}みます。",
       "explain": "店 vs 自宅 → structure c."
      },
      {
       "t": "{男|おとこ}の{人|ひと}は{何|なに}について{話|はな}していますか。\n1　ペットと{赤|あか}ちゃんを{世話|せわ}するところの{共通|きょうつう}{点|てん}\n2　{子供|こども}とペットの{世話|せわ}をするところの{種類|しゅるい}\n3　ペットホテルとペットシッターの{違|ちが}い",
       "explain": ""
      }
     ]
    },
    {
     "type": "text",
     "t": "{答|こた}え　①c　②3",
     "title": "{答|こた}え"
    }
   ]
  },
  {
   "type": "audio",
   "title": "{練習|れんしゅう}2 (3)　CD B05",
   "src": "audio/chokai/b05.mp3",
   "label": "CD B05",
   "t": "①{話|はなし}を{聞|き}いてください。この{話|はなし}はどのような{構造|こうぞう}になっていますか。キーワードを{関連|かんれん}づけて{考|かんが}えてください。",
   "note": "Real CD track. The book prints no script or answer for 練習 and ステップアップ, so the script below was transcribed from the CD and checked by sensei; the answers are sensei's."
  },
  {
   "type": "group",
   "title": "{練習|れんしゅう}2 (3)",
   "children": [
    {
     "type": "mcq",
     "id": "d15c-r2-3a",
     "q": "①　どのような{構造|こうぞう}ですか。\na　{電話|でんわ} ┬ {携帯|けいたい}{電話|でんわ}／{固定|こてい}{電話|でんわ}／{公衆|こうしゅう}{電話|でんわ} ┬ 10{円|えん}{玉|だま}／テレフォンカード\nb　{公衆|こうしゅう}{電話|でんわ}(10{円|えん}{玉|だま}) → {公衆|こうしゅう}{電話|でんわ}(テレフォンカード) → {固定|こてい}{電話|でんわ} → {携帯|けいたい}{電話|でんわ}\nc　{電話|でんわ} ┬ {後払|あとばら}い ┬ {携帯|けいたい}{電話|でんわ}／{固定|こてい}{電話|でんわ}\n　　　　└ {先払|さきばら}い ── {公衆|こうしゅう}{電話|でんわ}",
     "opts": [
      "a",
      "b",
      "c"
     ],
     "ans": 2,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": [
      "Answer c.",
      "携帯電話も固定電話も後払い … しかし、電話をかける前にお金を払う（先払い）… 公衆電話. The talk splits phones by WHEN you pay.",
      "a lists phone types; b is a history line. Both miss the 後払い／先払い key."
     ]
    },
    {
     "type": "mcq",
     "id": "d15c-r2-3b",
     "q": "②　CD B05 → B06　{女|おんな}の{人|ひと}は{何|なに}について{話|はな}していますか。\n1　{電話|でんわ}の{種類|しゅるい}\n2　{電話|でんわ}の{歴史|れきし}\n3　{電話|でんわ}の{料金|りょうきん}の{払|はら}い{方|かた}",
     "opts": [
      "1",
      "2",
      "3"
     ],
     "ans": 2,
     "keys": [
      "",
      "",
      ""
     ],
     "explain": [
      "Answer 3.",
      "Keywords 後払い, 先払い, お金を払う keep coming back. The phone types and the history are only there to explain the two ways of paying."
     ]
    }
   ],
   "scored": true
  },
  {
   "type": "audio",
   "title": "{練習|れんしゅう}2 (3) {質問|しつもん}　CD B06",
   "src": "audio/chokai/b06.mp3",
   "label": "CD B06"
  },
  {
   "type": "reveal",
   "label": "{練習|れんしゅう}2 (3)　スクリプト（CDから） · open after you answer",
   "children": [
    {
     "type": "items",
     "title": "◆スクリプト",
     "lead": "Tap 💡 on each line: sensei explains it.",
     "items": [
      {
       "t": "テレビで{女|おんな}の{人|ひと}が{話|はな}しています。",
       "explain": ""
      },
      {
       "t": "{女|おんな}：{携帯|けいたい}{電話|でんわ}が{登場|とうじょう}する{前|まえ}は、{電話|でんわ}といえば{主|おも}に{家|いえ}や{会社|かいしゃ}などの{決|き}まった{場所|ばしょ}からかける{固定電話|こていでんわ}のことでした。",
       "explain": ""
      },
      {
       "t": "{携帯|けいたい}{電話|でんわ}も{固定|こてい}{電話|でんわ}も[[{後払|あとばら}い]]、つまり{利用|りよう}した{人|ひと}が{後|あと}から{使|つか}った{分|ぶん}だけお{金|かね}を{払|はら}いますよね。{今|いま}ではこの{方法|ほうほう}が{当|あ}たり{前|まえ}のように{思|おも}われています。",
       "explain": "Key 1."
      },
      {
       "t": "[[しかし、{電話|でんわ}をかける{前|まえ}にお{金|かね}を{払|はら}う]]のが{当|あ}たり{前|まえ}の{時代|じだい}もありました。{電話|でんわ}が{使|つか}われ{始|はじ}めたころは{電話機|でんわき}はとても{高|たか}くて、{普通|ふつう}の{人|ひと}には{買|か}うことができないものでした。",
       "explain": "Key 2: 先払い."
      },
      {
       "t": "そこで{駅|えき}やホテル、{公共施設|こうきょうしせつ}など{多|おお}くの{人|ひと}が{出入|でい}りする{場所|ばしょ}に[[{公衆|こうしゅう}{電話|でんわ}|こうしゅうでんわ]]を{置|お}き、お{金|かね}を{払|はら}って{利用|りよう}できるようにしたのです。",
       "explain": ""
      },
      {
       "t": "{今|いま}でも{公衆|こうしゅう}{電話|でんわ}のほとんどは[[{先払|さきばら}い]]で、10{円|えん}{玉|だま}を{入|い}れてかけるタイプのものや、テレホンカードが{使|つか}えるものなどがあります。",
       "explain": "→ structure c."
      },
      {
       "t": "{女|おんな}の{人|ひと}は{何|なに}について{話|はな}していますか。\n1　{電話|でんわ}の{種類|しゅるい}\n2　{電話|でんわ}の{歴史|れきし}\n3　{電話|でんわ}の{料金|りょうきん}の{払|はら}い{方|かた}",
       "explain": ""
      }
     ]
    },
    {
     "type": "text",
     "t": "{答|こた}え　①c　②3",
     "title": "{答|こた}え"
    }
   ]
  },
  {
   "type": "audio",
   "title": "{練習|れんしゅう}2 (4)　CD B07",
   "src": "audio/chokai/b07.mp3",
   "label": "CD B07",
   "t": "①{話|はなし}を{聞|き}いて、{話|はなし}に{出|で}てくるキーワードを{書|か}き{取|と}ってください。",
   "note": "Real CD track. The book prints no script or answer for 練習 and ステップアップ, so the script below was transcribed from the CD and checked by sensei; the answers are sensei's."
  },
  {
   "type": "group",
   "title": "{練習|れんしゅう}2 (4)",
   "children": [
    {
     "type": "fill",
     "id": "d15c-r2-4k",
     "q": "①　キーワード（いくつでも）：%%",
     "ans": [
      "紅茶",
      "緑茶",
      "ウーロン茶",
      "お茶",
      "作り方",
      "同じ木",
      "{木|き}の{葉|は}",
      "葉"
     ],
     "explain": "Model keywords: 紅茶・ウーロン茶・緑茶, 作り方, (お茶の)木, 同じ種類, 葉. Any of them counts — compare with the script."
    },
    {
     "type": "mcq",
     "id": "d15c-r2-4s",
     "q": "②　この{話|はなし}はどのような{構造|こうぞう}になっていますか。a～cの{型|かた}からよいものを{選|えら}んでください。\na　［　］┬［　］／［　］／［　］　(one box splitting into three)\nb　［　］┬［　］―［　］\n　　　　└［　］　(two branches, one goes further)\nc　［　］―［　］\n　　［　］―［　］\n　　［　］―［　］　(three separate pairs)",
     "opts": [
      "a",
      "b",
      "c"
     ],
     "ans": 0,
     "keys": [
      "a",
      "b",
      "c"
     ],
     "explain": [
      "Answer a: 同じお茶の{木|き}の{葉|は} ┬ 紅茶／ウーロン茶／緑茶 (they differ only in 作り方).",
      "c would be the wrong picture: 紅茶の木、緑茶の木… — the man says some people think that, but 実は すべて同じ種類のお茶の{木|き}の{葉|は}から作られる."
     ]
    },
    {
     "type": "mcq",
     "id": "d15c-r2-4q",
     "q": "③　CD B07 → B08　{男|おとこ}の{人|ひと}はお{茶|ちゃ}についてどう{言|い}っていますか。\n1　{紅茶|こうちゃ}、{緑茶|りょくちゃ}、ウーロン{茶|ちゃ}は{同|おな}じ{木|き}の{葉|は}から{作|つく}られる\n2　{紅茶|こうちゃ}とウーロン{茶|ちゃ}は{同|おな}じ{木|き}の{葉|は}を{使|つか}うが{緑茶|りょくちゃ}は{違|ちが}う\n3　{木|き}の{種類|しゅるい}によってお{茶|ちゃ}の{種類|しゅるい}が{違|ちが}う",
     "opts": [
      "1",
      "2",
      "3"
     ],
     "ans": 0,
     "keys": [
      "",
      "",
      ""
     ],
     "explain": [
      "Answer 1.",
      "Key sentence after 実は: すべて同じ種類のお茶の{木|き}の{葉|は}から作られるのです. The difference is only the 作り方.",
      "2: ウーロン茶 is only 'closer to' 紅茶 in how it's made. 3 is the mistaken idea he corrects."
     ]
    }
   ],
   "scored": true
  },
  {
   "type": "audio",
   "title": "{練習|れんしゅう}2 (4) {質問|しつもん}　CD B08",
   "src": "audio/chokai/b08.mp3",
   "label": "CD B08"
  },
  {
   "type": "reveal",
   "label": "{練習|れんしゅう}2 (4)　スクリプト（CDから） · open after you answer",
   "children": [
    {
     "type": "items",
     "title": "◆スクリプト",
     "lead": "Tap 💡 on each line: sensei explains it.",
     "items": [
      {
       "t": "{男|おとこ}の{人|ひと}がお{茶|ちゃ}について{話|はな}しています。",
       "explain": ""
      },
      {
       "t": "{男|おとこ}：[[{紅茶|こうちゃ}|こうちゃ]]、[[ウーロン{茶|ちゃ}]]、[[{緑茶|りょくちゃ}|りょくちゃ]]。この3{種類|しゅるい}のお{茶|ちゃ}は、{色|いろ}も{味|あじ}も{香|かお}りもそれぞれ{違|ちが}います。なぜこんな{違|ちが}いがあるかというと、それは[[{作|つく}り{方|かた}が{違|ちが}う]]からなんです。",
       "explain": "Keywords."
      },
      {
       "t": "{紅茶|こうちゃ}と{緑茶|りょくちゃ}とでは{作|つく}り{方|かた}が{全|まった}く{違|ちが}います。ウーロン{茶|ちゃ}はどちらかというと{紅茶|こうちゃ}に{近|ちか}いですが、やはり{紅茶|こうちゃ}とは{違|ちが}う{作|つく}り{方|かた}をします。",
       "explain": ""
      },
      {
       "t": "{色|いろ}も{味|あじ}も{香|かお}りも{違|ちが}うから、{紅茶|こうちゃ}は{紅茶|こうちゃ}の{木|き}、{緑茶|りょくちゃ}は{緑茶|りょくちゃ}の{木|き}というように{木|き}の{種類|しゅるい}が{違|ちが}うと{思|おも}う{人|ひと}もいるかもしれませんが、[[{実|じつ}はすべて{同|おな}じ{種類|しゅるい}のお{茶|ちゃ}の{木|き}の{葉|は}から{作|つく}られる]]のです。",
       "explain": "★ Main point → structure a, answer 1."
      },
      {
       "t": "{作|つく}り{方|かた}の{違|ちが}いによって{同|おな}じ{葉|は}っぱからいろんなお{茶|ちゃ}が{楽|たの}しめるなんて、{不思議|ふしぎ}ですね。",
       "explain": ""
      },
      {
       "t": "{男|おとこ}の{人|ひと}はお{茶|ちゃ}についてどう{言|い}っていますか。\n1　{紅茶|こうちゃ}、{緑茶|りょくちゃ}、ウーロン{茶|ちゃ}は{同|おな}じ{木|き}の{葉|は}から{作|つく}られる\n2　{紅茶|こうちゃ}とウーロン{茶|ちゃ}は{同|おな}じ{木|き}の{葉|は}を{使|つか}うが{緑茶|りょくちゃ}は{違|ちが}う\n3　{木|き}の{種類|しゅるい}によってお{茶|ちゃ}の{種類|しゅるい}が{違|ちが}う",
       "explain": ""
      }
     ]
    },
    {
     "type": "text",
     "t": "{答|こた}え　①キーワード：{紅茶|こうちゃ}・ウーロン{茶|ちゃ}・{緑茶|りょくちゃ}・{作|つく}り{方|かた}・{同|おな}じ{木|き}の{葉|は}　②a　③1",
     "title": "{答|こた}え"
    }
   ]
  },
  {
   "type": "audio",
   "title": "ステップアップ{問題|もんだい}2　CD B09",
   "src": "audio/chokai/b09.mp3",
   "label": "CD B09",
   "t": "この{問題|もんだい}は{話|はなし}の{前|まえ}に{質問|しつもん}はありません。まず{話|はなし}を{聞|き}いてください。それから、{質問|しつもん}と{選択肢|せんたくし}を{聞|き}いて、1から4の{中|なか}から、{最|もっと}もよいものを{一|ひと}つ{選|えら}んでください。",
   "note": "Real CD track. The book prints no script or answer for 練習 and ステップアップ, so the script below was transcribed from the CD and checked by sensei; the answers are sensei's."
  },
  {
   "type": "group",
   "title": "ステップアップ{問題|もんだい}2",
   "children": [
    {
     "type": "mcq",
     "id": "d15c-s2",
     "q": "Listen, then choose 1–4.",
     "opts": [
      "1",
      "2",
      "3",
      "4"
     ],
     "ans": 2,
     "keys": [
      "",
      "",
      "",
      ""
     ],
     "explain": [
      "Answer 3 (植物が移動する方法).",
      "Map: 植物の移動方法 ┬ 自分の力（種が割れて飛ぶ）├ 風の力（タンポポ）└ 動物を利用（くっつく・実を食べてもらう）. The talk lists the ways plants move.",
      "1: the animal/plant difference is only the opening. 2: 範囲を広げる is the purpose, not the topic. 4 is only one of the three ways."
     ]
    }
   ],
   "scored": true
  },
  {
   "type": "reveal",
   "label": "ステップアップ{問題|もんだい}2　スクリプト（CDから） · open after you answer",
   "children": [
    {
     "type": "items",
     "title": "◆スクリプト",
     "lead": "Tap 💡 on each line: sensei explains it.",
     "items": [
      {
       "t": "テレビで{女|おんな}の{人|ひと}が{話|はな}しています。",
       "explain": ""
      },
      {
       "t": "{女|おんな}：{動物|どうぶつ}は{自分|じぶん}で{動|うご}いて{生活|せいかつ}の{場所|ばしょ}を{変|か}えることができますが、{植物|しょくぶつ}はそれができません。でも、{自分|じぶん}で{動|うご}けない{植物|しょくぶつ}も、{親|おや}から{離|はな}れて{生活|せいかつ}{範囲|はんい}を{広|ひろ}げるために[[{様々|さまざま}な{移動|いどう}{方法|ほうほう}]]を{身|み}につけています。",
       "explain": "★ Topic: 移動方法."
      },
      {
       "t": "{種|たね}が{割|わ}れて{遠|とお}くへ{飛|と}ぶなど[[{自分|じぶん}の{力|ちから}だけで{動|うご}く]]ものもあれば、タンポポのように[[{風|かぜ}の{力|ちから}を{利用|りよう}して]]{遠|とお}くに{飛|と}ばされて、{親|おや}の{植物|しょくぶつ}から{数|すう}{百|ひゃく}メートルも{離|はな}れたところで{成長|せいちょう}するものもあります。",
       "explain": "Ways 1 and 2."
      },
      {
       "t": "また、そばを{通|とお}った{動物|どうぶつ}にくっついて{遠|とお}くに{運|はこ}んでもらうとか、{甘|あま}い{実|み}をつけて{食|た}べられ、{糞|ふん}としてまき{散|ち}らしてもらうなど、[[{動物|どうぶつ}を{利用|りよう}して{移動|いどう}する]]ものもあります。",
       "explain": "Way 3."
      },
      {
       "t": "{女|おんな}の{人|ひと}は{何|なに}について{話|はな}していますか。\n1　{植物|しょくぶつ}が{動物|どうぶつ}と{違|ちが}う{点|てん}\n2　{植物|しょくぶつ}が{育|そだ}つ{範囲|はんい}\n3　{植物|しょくぶつ}が{移動|いどう}する{方法|ほうほう}\n4　{植物|しょくぶつ}が{動物|どうぶつ}を{利用|りよう}する{方法|ほうほう}",
       "explain": ""
      }
     ]
    },
    {
     "type": "text",
     "t": "{答|こた}え　3",
     "title": "{答|こた}え"
    }
   ]
  }
 ]
});
