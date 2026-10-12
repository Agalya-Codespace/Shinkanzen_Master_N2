/* Day 9 · chokai. Built from d09_chokai.py by tools/build_day.py (furigana added automatically). */
window.N2_DAYS = window.N2_DAYS || {};
window.N2_DAYS[9] = window.N2_DAYS[9] || {"title": "", "intro": "", "sections": []};
if (false) window.N2_DAYS[9].title = "";
if (false) window.N2_DAYS[9].intro = "";
window.N2_DAYS[9].sections.push({
 "book": "chokai",
 "title": "{実力|じつりょく}{養成|ようせい}{編|へん}　Ⅲ「{課題|かだい}{理解|りかい}」のスキルを{学|まな}ぶ　2 {最初|さいしょ}にすることを{考|かんが}える",
 "source": "新完全マスター聴解 N2 · 実力養成編 Ⅲ-2 · pp.37–39 · CD A32–A35 (read-aloud)",
 "blocks": [
  {
   "type": "text",
   "t": "{質問|しつもん}で「{最初|さいしょ}にすることは{何|なに}か」と{聞|き}いている{場合|ばあい}は、「{最初|さいしょ}にすること」や「する{順序|じゅんじょ}」を{示|しめ}す{表現|ひょうげん}などに{注意|ちゅうい}します。",
   "title": "2 {最初|さいしょ}にすることを{考|かんが}える",
   "explain": [
    "N2 問題1-la 'まず何をしますか' romba common. Ellaa task-um kekkum, aanaa FIRST edhu-nu dhaan kelvi.",
    "Trap: conversation-la mudhalla sonna task first illa! '先に', '～前に', 'その前に' kettaa order maarum."
   ]
  },
  {
   "type": "items",
   "title": "{順序|じゅんじょ}の{表現|ひょうげん}",
   "items": [
    {
     "t": "・{最初|さいしょ}にすることを{示|しめ}す{表現|ひょうげん}：まず／{最初|さいしょ}に／はじめに",
     "explain": "First: まず, 最初に, はじめに."
    },
    {
     "t": "・する{順序|じゅんじょ}を{示|しめ}す{表現|ひょうげん}：それから／～{前|まえ}に／～{後|あと}で／～てから／～たら／～ないうちに",
     "explain": "Order words. ～ないうちに = before ～ happens."
    },
    {
     "t": "・いつするかを{示|しめ}す{表現|ひょうげん}：{先|さき}に／{今|いま}すぐ／{急|いそ}いで／{後|あと}で／{後回|あとまわ}し",
     "explain": "先に・今すぐ = do it first. 後で・後回し = later."
    },
    {
     "t": "・ほかの{案|あん}を{示|しめ}す{表現|ひょうげん}：それより／やっぱり",
     "explain": "Change of plan: それより = rather than that, やっぱり = on second thought."
    }
   ]
  },
  {
   "type": "audio",
   "title": "{例題|れいだい}2　CD A32",
   "src": "audio/chokai/a32.mp3",
   "label": "A32 · computer read-aloud of the book's script",
   "t": "{話|はなし}を{聞|き}いて、{質問|しつもん}の{答|こた}えに○をつけてください。"
  },
  {
   "type": "group",
   "title": "{例題|れいだい}2　{男|おとこ}の{人|ひと}はこの{後|あと}まず、{何|なに}をしますか。",
   "children": [
    {
     "type": "mcq",
     "id": "d9c-e2",
     "q": "Tap the FIRST thing the man does.",
     "opts": [
      "{朝|あさ}ご{飯|はん}を{食|た}べる",
      "{洗濯物|せんたくもの}を{干|ほ}す",
      "{新聞|しんぶん}を{取|と}ってくる",
      "ごみを{出|だ}す"
     ],
     "ans": 3,
     "keys": [
      "",
      "",
      "",
      ""
     ],
     "explain": "Book answer: ごみを出す. He said 干したら行ってくる, but she said 缶の回収がそろそろ来ちゃうから、先にお願い → garbage first."
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
       "t": "{朝|あさ}、{家|いえ}で{女|おんな}の{人|ひと}と{男|おとこ}の{人|ひと}が{話|はな}しています。{男|おとこ}の{人|ひと}はこの{後|あと}まず、{何|なに}をしますか。",
       "explain": "Question: 男の人 + まず."
      },
      {
       "t": "{女|おんな}：えーと、こっちが{朝|あさ}ご{飯|はん}で、こっちがお{弁当用|べんとうよう}で……。そろそろ{朝|あさ}ご{飯|はん}できるから、{食|た}べて。",
       "explain": "朝ご飯 — later."
      },
      {
       "t": "{男|おとこ}：{洗濯|せんたく}、{終|お}わったみたいだけど、おれ、{干|ほ}そうか。",
       "explain": "He offers to hang the washing."
      },
      {
       "t": "{女|おんな}：お{願|ねが}いできる？　{後|あと}で{新聞|しんぶん}も{取|と}ってきてね。わたし、お{弁当|べんとう}{作|つく}っちゃうから。",
       "explain": "後で新聞 → later."
      },
      {
       "t": "{男|おとこ}：うん、いいよ。",
       "explain": ""
      },
      {
       "t": "{女|おんな}：あ、いけない！　{資源|しげん}ごみの{日|ひ}、{今日|きょう}だった！　ちょっと{行|い}ってきてくれる？",
       "explain": "資源ごみ = recyclable garbage."
      },
      {
       "t": "{男|おとこ}：うん。ここにあるびんと{缶|かん}だけでいい？　これ、{干|ほ}したら{行|い}ってくるよ。",
       "explain": "His plan: washing first, then garbage."
      },
      {
       "t": "{女|おんな}：あ、でも、{缶|かん}の{回収|かいしゅう}がそろそろ{来|き}ちゃうから、{先|さき}にお{願|ねが}い。あと、このびんも。",
       "explain": "でも + 先にお願い → garbage FIRST."
      },
      {
       "t": "{男|おとこ}：わかった。",
       "explain": ""
      }
     ]
    },
    {
     "type": "text",
     "t": "{答|こた}え　ごみを{出|だ}す　{男|おとこ}の{人|ひと}がすることは「{朝|あさ}ご{飯|はん}を{食|た}べる」「{洗濯物|せんたくもの}を{干|ほ}す」「{新聞|しんぶん}を{取|と}ってくる」「ごみを{出|だ}す」ことです。{男|おとこ}の{人|ひと}が「{干|ほ}したら（ごみを{出|だ}しに）{行|い}ってくる」と{言|い}ったのに{対|たい}して、「でも、…{先|さき}にお{願|ねが}い。」と{言|い}っているので、まず{最初|さいしょ}にごみを{出|だ}すことがわかります。",
     "title": "{答|こた}え（{本|ほん}）"
    }
   ]
  },
  {
   "type": "audio",
   "title": "{練習|れんしゅう}2 (1)　CD A33",
   "src": "audio/chokai/a33.mp3",
   "label": "A33 · computer read-aloud of the book script",
   "t": "{話|はなし}を{聞|き}いて、{質問|しつもん}の{答|こた}えに○をつけてください。",
   "note": "⚠ The book prints no script or answer for this CD track, so sensei made this practice set in the same format. The audio is a computer read-aloud, not the real CD."
  },
  {
   "type": "group",
   "title": "{練習|れんしゅう}2 (1)　{男|おとこ}の{人|ひと}はまず{何|なに}をしますか。",
   "children": [
    {
     "type": "mcq",
     "id": "d9c-r2-1",
     "q": "Tap the FIRST thing.",
     "opts": [
      "{割|わ}れたガラスを{片|かた}づける",
      "{指|ゆび}にばんそうこうをはる",
      "ティッシュで{血|ち}をふき{取|と}る",
      "ゴムの{手袋|てぶくろ}をする"
     ],
     "ans": 2,
     "keys": [
      "",
      "",
      "",
      ""
     ],
     "explain": "Answer: ティッシュで血をふき取る. 片づけるのは後でいい → まず、ティッシュで血をふいて. Then ばんそうこう, then gloves, then glass."
    }
   ],
   "scored": true
  },
  {
   "type": "audio",
   "title": "{練習|れんしゅう}2 (2)　CD A34",
   "src": "audio/chokai/a34.mp3",
   "label": "A34 · computer read-aloud of the book script",
   "t": "{話|はなし}を{聞|き}いて、{質問|しつもん}の{答|こた}えに○をつけてください。",
   "note": "⚠ The book prints no script or answer for this CD track, so sensei made this practice set in the same format. The audio is a computer read-aloud, not the real CD."
  },
  {
   "type": "group",
   "title": "{練習|れんしゅう}2 (2)　{女|おんな}の{子|こ}はまず{何|なに}をしますか。",
   "children": [
    {
     "type": "mcq",
     "id": "d9c-r2-2",
     "q": "Tap the FIRST thing.",
     "opts": [
      "{玄関|げんかん}の{掃除|そうじ}",
      "{昼|ひる}ご{飯|はん}の{後片|あとかた}づけ",
      "{服|ふく}を{着替|きが}える",
      "お{菓子|かし}を{買|か}いに{行|い}く",
      "テレビの{周|まわ}りの{片|かた}づけ"
     ],
     "ans": 4,
     "keys": [
      "",
      "",
      "",
      "",
      ""
     ],
     "explain": "Answer: テレビの周りの片づけ. 玄関の掃除をお願い。でも、その前に… → TV area first. 先にやって confirms it. Snacks: grandma brings them. Clothes: after all the tidying."
    }
   ],
   "scored": true
  },
  {
   "type": "audio",
   "title": "{練習|れんしゅう}2 (3)　CD A35",
   "src": "audio/chokai/a35.mp3",
   "label": "A35 · computer read-aloud of the book script",
   "t": "{話|はなし}を{聞|き}いて、{質問|しつもん}の{答|こた}えに○をつけてください。",
   "note": "⚠ The book prints no script or answer for this CD track, so sensei made this practice set in the same format. The audio is a computer read-aloud, not the real CD."
  },
  {
   "type": "group",
   "title": "{練習|れんしゅう}2 (3)　{男|おとこ}の{人|ひと}はまず{何|なに}をしますか。",
   "children": [
    {
     "type": "mcq",
     "id": "d9c-r2-3",
     "q": "Tap the FIRST thing.",
     "opts": [
      "{知|し}り{合|あ}いに{頼|たの}む",
      "{講義|こうぎ}を{受|う}ける",
      "{社員|しゃいん}に{声|こえ}をかける",
      "お{知|し}らせを{作|つく}る",
      "{課長|かちょう}に{話|はな}す",
      "{正式|せいしき}に{依頼|いらい}する"
     ],
     "ans": 4,
     "keys": [
      "",
      "",
      "",
      "",
      "",
      ""
     ],
     "explain": "Answer: 課長に話す. 正式に依頼する前に、一応課長に話して → 今すぐ課長に話してきます. The friend: その後で. Notices: after the teacher is decided."
    }
   ],
   "scored": true
  },
  {
   "type": "reveal",
   "label": "{練習|れんしゅう}2　スクリプトと{答|こた}え · open after you answer",
   "children": [
    {
     "type": "items",
     "title": "◆スクリプト",
     "lead": "Tap 💡 on each line: sensei explains it.",
     "items": [
      {
       "t": "(1)　{台所|だいどころ}で、{女|おんな}の{人|ひと}と{男|おとこ}の{人|ひと}が{話|はな}しています。{男|おとこ}の{人|ひと}はまず{何|なに}をしますか。",
       "explain": ""
      },
      {
       "t": "{男|おとこ}：あっ、{痛|いた}っ。コップ、{割|わ}っちゃった。{指|ゆび}も{切|き}っちゃったよ。",
       "explain": ""
      },
      {
       "t": "{女|おんな}：{大丈夫|だいじょうぶ}？　{血|ち}が{出|で}てるじゃない。あ、ガラス、{手|て}で{触|さわ}らないで。",
       "explain": "Don't touch the glass."
      },
      {
       "t": "{男|おとこ}：でも、{早|はや}く{片|かた}づけないと{危|あぶ}ないよ。　{女|おんな}：{片|かた}づけるのは{後|あと}でいいから。まず、ティッシュで{血|ち}をふいて。ばんそうこう、{持|も}ってくるから。",
       "explain": "後でいい + まず → ティッシュ first."
      },
      {
       "t": "{男|おとこ}：わかった。　{女|おんな}：それから、ガラスを{片|かた}づけるときは、ゴムの{手袋|てぶくろ}をしてね。",
       "explain": "Gloves: later, with the glass."
      },
      {
       "t": "(2)　{家|いえ}で、お{母|かあ}さんと{女|おんな}の{子|こ}が{話|はな}しています。{女|おんな}の{子|こ}はまず{何|なに}をしますか。",
       "explain": ""
      },
      {
       "t": "{母|はは}：もうすぐおばあちゃんたちが{来|く}るから、ちょっと{手伝|てつだ}ってくれる？　{子|こ}：いいよ。{何|なに}すればいい？",
       "explain": ""
      },
      {
       "t": "{母|はは}：お{昼|ひる}ご{飯|はん}の{後片|あとかた}づけはお{母|かあ}さんがやるから、{玄関|げんかん}の{掃除|そうじ}をお{願|ねが}い。あ、でも、その{前|まえ}に、テレビの{周|まわ}りに{散|ち}らかってるおもちゃ、{片|かた}づけてくれる？　お{客|きゃく}さんがすぐ{目|め}にするところだから。",
       "explain": "その前に → TV area first."
      },
      {
       "t": "{子|こ}：えー、{玄関|げんかん}の{掃除|そうじ}の{後|あと}じゃだめ？　{母|はは}：だめ。{先|さき}にやって。",
       "explain": "先に confirms."
      },
      {
       "t": "{子|こ}：はーい。あ、お{菓子|かし}は？　{買|か}いに{行|い}こうか？　{母|はは}：お{菓子|かし}は、おばあちゃんが{持|も}ってきてくれるって。それより、その{服|ふく}、{着替|きが}えなさいね。{片|かた}づけが{全部|ぜんぶ}{終|お}わってからでいいから。",
       "explain": "Snacks: no. Clothes: last."
      },
      {
       "t": "(3)　{会社|かいしゃ}で、{女|おんな}の{人|ひと}と{男|おとこ}の{人|ひと}が{話|はな}しています。{男|おとこ}の{人|ひと}はまず{何|なに}をしますか。",
       "explain": ""
      },
      {
       "t": "{女|おんな}：{来月|らいげつ}の{社内研修|しゃないけんしゅう}で、パソコンの{講義|こうぎ}をしてくれる{先生|せんせい}を{探|さが}してるんだけど、だれか{知|し}らない？",
       "explain": "社内研修 = in-company training."
      },
      {
       "t": "{男|おとこ}：{大学|だいがく}のときの{知|し}り{合|あ}いに、そういうのが{得意|とくい}な{人|ひと}がいますよ。{頼|たの}んでみましょうか。",
       "explain": ""
      },
      {
       "t": "{女|おんな}：ほんと？　{助|たす}かる。じゃ、{正式|せいしき}に{依頼|いらい}する{前|まえ}に、{一応|いちおう}{課長|かちょう}に{話|はな}しておいてくれる？",
       "explain": "～前に → 課長 first."
      },
      {
       "t": "{男|おとこ}：はい。じゃ、{今|いま}すぐ{課長|かちょう}に{話|はな}してきます。{知|し}り{合|あ}いには、その{後|あと}で{連絡|れんらく}しますね。",
       "explain": "今すぐ = first."
      },
      {
       "t": "{女|おんな}：お{願|ねが}い。{社員|しゃいん}への{声|こえ}かけとお{知|し}らせは、{先生|せんせい}が{決|き}まってからでいいから。",
       "explain": "Later."
      }
     ]
    },
    {
     "type": "text",
     "t": "{答|こた}え　(1) ティッシュで{血|ち}をふき{取|と}る　(2) テレビの{周|まわ}りの{片|かた}づけ　(3) {課長|かちょう}に{話|はな}す",
     "title": "{答|こた}え"
    }
   ]
  }
 ]
});
