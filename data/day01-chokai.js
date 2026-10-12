/* Day 1 · 聴解 (新完全マスター聴解 N2, 問題紹介 1 課題理解・2 ポイント理解, pp.2–5). Transcribed from the book scan.
   Scripts and answers are printed in the book on these pages. Audio is CD A (tracks A01, A02). */
window.N2_DAYS = window.N2_DAYS || {};
window.N2_DAYS[1] = window.N2_DAYS[1] || { sections: [] };
window.N2_DAYS[1].sections.push({
  book: "chokai",
  title: "{問題紹介|もんだいしょうかい}　1 {課題理解|かだいりかい}・2 ポイント{理解|りかい}",
  source: "新完全マスター聴解 N2 · 問題紹介 · pp.2–5 · CD A01–A02",
  blocks: [
    {
      type: "text",
      title: "🎧 {聴解|ちょうかい}の{勉強|べんきょう}のしかた · How to study each question",
      t: "① {質問|しつもん}と{選択肢|せんたくし}だけ{見|み}て、{音声|おんせい}を{聞|き}く。\n② {答|こた}えを{選|えら}ぶ。\n③ スクリプトを{開|ひら}いて、{聞|き}き{取|と}れなかった{所|ところ}を{確認|かくにん}する。\n④ スクリプトを{見|み}ながら、もう{一度|いちど}{聞|き}く。",
      explain: [
        "Listening-la important rule: mudhalla script paakkaadheenga! Audio mattum kettu answer pannunga. Apram dhaan script open panni, enga miss pannineenga nu check pannunga.",
        "Kadaisi-la script paathukitte innoru thadava kelunga. Idhu dhaan 'shadowing' ku first step. Inniki rendu question type kathukkalaam: 課題理解(かだいりかい) and ポイント理解(ポイントりかい)."
      ]
    },
    {
      type: "text",
      title: "1　{課題理解|かだいりかい}",
      t: "「{課題理解|かだいりかい}」は、まとまりのある{話|はなし}から、{指示|しじ}や{依頼|いらい}、{助言|じょげん}などを{聞|き}き{取|と}り、これから{何|なに}をすべきかを{判断|はんだん}する{問題|もんだい}です。{選択肢|せんたくし}は{問題用紙|もんだいようし}に{書|か}かれていて、イラストがあるものと、{文字|もじ}だけのものがあります。{実際|じっさい}の{試験|しけん}では、{問題|もんだい}の{前|まえ}に{練習|れんしゅう}があります。{例題|れいだい}をやってみましょう。",
      explain: [
        "課題理解(かだいりかい) = task-based comprehension. Oru conversation-la instructions (指示 しじ), requests (依頼 いらい), advice (助言 じょげん) varum. Question: 'ippo enna seiyyanum?'",
        "Trick: conversation-la neraya things varum. Sila already mudinjirukkum, sila innum seiyyanum. 'もう～た / ～てある / 大丈夫' kettaa → already done. 'まだ / ～なきゃいけない / ～てください' kettaa → still to do. Indha signal words-a pidinga!"
      ]
    },
    {
      type: "audio",
      title: "☆{例題|れいだい}1　CD A01",
      src: "audio/chokai/a01.mp3",
      label: "CD A · Track 01",
      t: "この{問題|もんだい}では、まず{質問|しつもん}を{聞|き}いてください。それから{話|はなし}を{聞|き}いて、{問題用紙|もんだいようし}の1から4の{中|なか}から、{最|もっと}もよいものを{一|ひと}つ{選|えら}んでください。\n（イラスト）ア {案内表示|あんないひょうじ}　イ マイク　ウ {机|つくえ}　エ いす　オ ごみ{箱|ばこ}"
    },
    {
      type: "mcq", id: "d1c-r1",
      q: "{例題|れいだい}1　２{人|ふたり}はこれから{何|なに}を{準備|じゅんび}しますか。",
      opts: ["ア　イ　ウ", "ア　ウ　オ", "ウ　オ", "ア　ウ"], keys: ["1", "2", "3", "4"], ans: 3,
      explain: "Answer 4 (ア 案内表示 + ウ 机). 案内表示 → '出さなきゃいけない' (innum podanum). 机 → 'まだ' (innum aagala). マイク → '大丈夫' (ready). ごみ箱 → 'さっき並べた' (already done). いす → 'ごみ箱を並べたときに、一緒にやっときました' (already done)."
    },
    {
      type: "reveal",
      label: "スクリプトと{答|こた}え（p.3）· open after you answer",
      children: [
        {
          type: "items",
          title: "◆スクリプト",
          lead: "Tap 💡 on each line: sensei explains it.",
          items: [
            { t: "{市民会館|しみんかいかん}で{男|おとこ}の{人|ひと}と{女|おんな}の{人|ひと}が{文化祭|ぶんかさい}の{準備|じゅんび}について{話|はな}しています。２{人|ふたり}はこれから{何|なに}を{準備|じゅんび}しますか。", explain: "市民会館(しみんかいかん) = city community hall. 文化祭(ぶんかさい) = cultural festival. 準備(じゅんび) = preparation. Question first varum: 'Rendu perum ippo enna prepare pannuvaanga?' Indha question-a manasula vechu kelunga." },
            { t: "{男|おとこ}：あしたの{文化祭|ぶんかさい}の{準備|じゅんび}、もう{済|す}みましたか。", explain: "済(す)む = be finished. 'Naalaikku festival preparation mudinjuducha?'" },
            { t: "{女|おんな}：もう{少|すこ}しです。あと、{案内表示|あんないひょうじ}を{出|だ}さなきゃいけないんですけど。", explain: "出さなきゃいけない = 出さなければいけない (casual: なきゃ). 'Innum konjam irukku. Direction board podanum.' → 案内表示 = TO DO ✔" },
            { t: "{男|おとこ}：{各部屋|かくへや}のマイクなんかの{用意|ようい}はできてるんですか。", explain: "各部屋(かくへや) = each room. ～なんか = things like ～. 用意(ようい)はできてる = is ready. 'Ovvoru room-layum mic ellam ready-aa?'" },
            { t: "{女|おんな}：{大丈夫|だいじょうぶ}です。あ、ただ、{受付|うけつけ}の{机|つくえ}がまだ……。", explain: "大丈夫 → マイク is done ✘. ただ = but. 受付(うけつけ)の机がまだ = reception desk innum podala → 机 = TO DO ✔" },
            { t: "{男|おとこ}：じゃ、それ、{手伝|てつだ}いましょう。", explain: "手伝(てつだ)う = help. 'Seri, adhukku naan help pannren.'" },
            { t: "{女|おんな}：すみません、{助|たす}かります。", explain: "助(たす)かります = that helps me a lot (thanks)." },
            { t: "{男|おとこ}：いすはもう{並|なら}べてあるんですか。", explain: "並(なら)べてある = has been lined up (～てある = state after someone did it). 'Chair ellam already arrange panniyaacha?'" },
            { t: "{女|おんな}：はい。さっき、ごみ{箱|ばこ}を{並|なら}べたときに、{一緒|いっしょ}にやっときました。", explain: "さっき = a while ago. やっときました = やっておきました (casual). 'Konja neram munnadi dustbin vechappo, chair-um senthu panniten.' → ごみ箱 ✘, いす ✘ (both done)." },
            { t: "{男|おとこ}：そうですか。じゃ、さっそく{残|のこ}りをやっちゃいましょうか。", explain: "さっそく = right away. 残(のこ)り = the rest. やっちゃいましょう = やってしまいましょう (casual). 'Appo meedhi irukkuradhai udane mudichiduvom.'" },
            { t: "{女|おんな}：はい。", explain: "" },
            { t: "２{人|ふたり}はこれから{何|なに}を{準備|じゅんび}しますか。", explain: "Question again at the end. So: 案内表示 + 机 → ア ウ → answer 4." }
          ]
        },
        {
          type: "text",
          title: "{答|こた}え　4",
          t: "{案内表示|あんないひょうじ}は「{出|だ}さなきゃいけない」、{机|つくえ}は「まだ」と{言|い}っているので、この２つがこれから{準備|じゅんび}するものです。\n{一方|いっぽう}、マイクについては「{大丈夫|だいじょうぶ}」、ごみ{箱|ばこ}は「さっき、ごみ{箱|ばこ}を{並|なら}べた」と{言|い}っています。また、いすは「ごみ{箱|ばこ}を{並|なら}べたときに、{一緒|いっしょ}にやっときました」と{言|い}っているので、これらは{準備|じゅんび}する{必要|ひつよう}がありません。\n「{課題理解|かだいりかい}」の{問題|もんだい}を{解|と}くためには、{話|はなし}の{中|なか}から{指示|しじ}や{助言|じょげん}の{部分|ぶぶん}を{聞|き}き{取|と}って、「するべきこと」を{理解|りかい}する{必要|ひつよう}があります。また、{質問|しつもん}で「これから[[まず]]{何|なに}をしなければなりませんか」のように、{最初|さいしょ}にすることを{聞|き}いている{場合|ばあい}は、いくつかのすることの{中|なか}でもどれが{優先|ゆうせん}されるのかを{判断|はんだん}しなければなりません。\nこの{部分|ぶぶん}については「Ⅲ 「{課題理解|かだいりかい}」のスキルを{学|まな}ぶ」で{練習|れんしゅう}します。",
          explain: [
            "Book solradhu: 課題理解-la 'seiyya vendiyadhu' (するべきこと) mattum pidikkanum. Already mudinjadhu ellam cut pannunga.",
            "Kavanam: question-la 'まず' (first) irundhaa, seiyya vendiya list-la edhu first nu paakkanum (優先 ゆうせん = priority). Idha Day 8–10-la innum practice pannuvom."
          ]
        }
      ]
    },
    {
      type: "text",
      title: "2　ポイント{理解|りかい}",
      t: "「ポイント{理解|りかい}」は、まとまりのある{話|はなし}から、{質問|しつもん}されたことにポイントを{絞|しぼ}って{聞|き}き{取|と}る{問題|もんだい}です。{出来事|できごと}の{理由|りゆう}や{目的|もくてき}、{話|はな}し{手|て}の{気持|きも}ちなどが{理解|りかい}できるかが{問|と}われます。{実際|じっさい}の{試験|しけん}では、{問題|もんだい}の{前|まえ}に{練習|れんしゅう}があります。{例題|れいだい}をやってみましょう。",
      explain: [
        "ポイント理解 = listening for one point. Question already theriyum (reason? purpose? feeling?). Andha point-ku mattum kaadhu kudunga (絞(しぼ)る = narrow down).",
        "Inga choices padikka time kudupaanga. Adhai use pannunga: 4 choices-a mun-kootiye padichu, 'edhu varum?' nu ready-aa irunga. Trap: audio-la choice-la irukkura words varum, aanaa adhu answer illa!"
      ]
    },
    {
      type: "audio",
      title: "☆{例題|れいだい}2　CD A02",
      src: "audio/chokai/a02.mp3",
      label: "CD A · Track 02",
      t: "この{問題|もんだい}では、まず{質問|しつもん}を{聞|き}いてください。そのあと、{問題用紙|もんだいようし}の{選択肢|せんたくし}を{読|よ}んでください。{読|よ}む{時間|じかん}があります。それから{話|はなし}を{聞|き}いて、{問題用紙|もんだいようし}の1から4の{中|なか}から、{最|もっと}もよいものを{一|ひと}つ{選|えら}んでください。"
    },
    {
      type: "mcq", id: "d1c-r2",
      q: "{例題|れいだい}2　{女|おんな}の{人|ひと}はどうして{送別会|そうべつかい}に{行|い}けないと{言|い}っていますか。",
      opts: ["{家|いえ}の{用事|ようじ}で{忙|いそが}しいから", "{子供|こども}の{具合|ぐあい}が{悪|わる}いから", "{体調|たいちょう}が{悪|わる}いから", "{健康診断|けんこうしんだん}を{受|う}けるから"], keys: ["1", "2", "3", "4"], ans: 3,
      explain: "Answer 4. 実は (actually) kku apram vara part dhaan real reason: '病院に行かなきゃいけなくて' + '健康診断をしてもらおうと思って'. 1: busy with kids — but that was why she missed the mail, not the party day. 2: child's illness 'もう治った'. 3: '悪いところがないか' check panna dhaan pogiraanga — she is not sick."
    },
    {
      type: "reveal",
      label: "スクリプトと{答|こた}え（p.5）· open after you answer",
      children: [
        {
          type: "items",
          title: "◆スクリプト",
          lead: "Tap 💡 on each line: sensei explains it.",
          items: [
            { t: "{男|おとこ}の{人|ひと}と{女|おんな}の{人|ひと}が{電話|でんわ}で{話|はな}しています。{女|おんな}の{人|ひと}はどうして{送別会|そうべつかい}に{行|い}けないと{言|い}っていますか。", explain: "送別会(そうべつかい) = farewell party. Question: 'Ava yen farewell party-ku vara mudiyaadhu nu solraa?' → REASON kekkaanga." },
            { t: "{男|おとこ}：もしもし、{松本|まつもと}さん？　{渡辺|わたなべ}です。メール{見|み}てくれましたか。{土曜日|どようび}の{古川|ふるかわ}さんの{送別会|そうべつかい}のこと。", explain: "'Hello Matsumoto-san? Watanabe pesuren. Saturday Furukawa-san farewell party pathi mail paatheengalaa?'" },
            { t: "{女|おんな}：え？　ごめん、このところ{子供|こども}のことですっごく{忙|いそが}しくてメール{見|み}られなかったのよ。{土曜日|どようび}ってあさってなの？　ずいぶん{急|きゅう}な{日|ひ}になったのね。", explain: "このところ = these days. すっごく = すごく (very, emphatic). Kids vishayathula busy → mail paakkala (choice 1 trap!). あさって = day after tomorrow. 急(きゅう)な = sudden." },
            { t: "{男|おとこ}：ええ。{月曜日|げつようび}にはもうマレーシアに{発|た}つんだそうですよ。お{子|こ}さん、ご{病気|びょうき}か{何|なに}かですか。", explain: "発(た)つ = depart. ～んだそうです = I heard that ～. 'Monday Malaysia kilambiraaraam. Ungal kozhandhaikku udambu sariyillaiyaa?'" },
            { t: "{女|おんな}：ええ、でも、それはもう{治|なお}ったからいいんですけどね。{実|じつ}は、その{日|ひ}わたしの{方|ほう}が{病院|びょういん}に{行|い}かなきゃいけなくて……。", explain: "もう治(なお)った = already recovered → choice 2 ✘. 実(じつ)は = actually (real point coming!). わたしの方が = I'm the one who… 病院に行かなきゃいけなくて = have to go to hospital." },
            { t: "{男|おとこ}：えー！　どこか{悪|わる}いんですか。", explain: "'Aiyyo! Edhaavadhu udambu sariyillaiyaa?'" },
            { t: "{女|おんな}：いえ、{悪|わる}いところがないか、{人間|にんげん}ドックでまとめて{健康診断|けんこうしんだん}をしてもらおうと{思|おも}ってね。その{日|ひ}やっと{予約|よやく}が{取|と}れたもんだから……。", explain: "人間(にんげん)ドック = full medical check-up. まとめて = all at once. 健康診断(けんこうしんだん) = health check-up. やっと予約(よやく)が取(と)れた = finally got a booking. 'Illai, edhaavadhu problem irukkaa nu full check-up panna poren' → choice 4 ✔, choice 3 ✘ (she isn't sick)." },
            { t: "{男|おとこ}：そうなんですか。でも、まあ、{健康|けんこう}が{何|なに}より{大切|たいせつ}ですから……。", explain: "何より大切 = more important than anything. 'Health dhaan ellaathaiyum vida mukkiyam.'" },
            { t: "{女|おんな}：ごめんなさい。{行|い}きたいんだけど。{彼女|かのじょ}にはわたしからおわびのメールしとくわ。", explain: "おわび = apology. しとく = しておく (do in advance). 'Varanum nu aasai dhaan. Avalukku naane sorry mail anuppiduren.'" },
            { t: "{女|おんな}の{人|ひと}はどうして{送別会|そうべつかい}に{行|い}けないと{言|い}っていますか。", explain: "Answer: 4 健康診断を受けるから." }
          ]
        },
        {
          type: "text",
          title: "{答|こた}え　4",
          t: "{女|おんな}の{人|ひと}は、「{実|じつ}は」に{続|つづ}けて、「{病院|びょういん}に{行|い}かなきゃいけなくて」「{健康診断|けんこうしんだん}をしてもらおうと{思|おも}って」と{言|い}っているので、4が{行|い}けない{理由|りゆう}です。1については、「{子供|こども}のことですっごく{忙|いそが}しくて」とは{言|い}っていますが、{送別会|そうべつかい}の{日|ひ}のことではありません。また、{子供|こども}の{病気|びょうき}は「もう{治|なお}ったからいい」と{言|い}っているので2ではありません。3は、「{悪|わる}いところがないか」「{健康診断|けんこうしんだん}をしてもらおうと{思|おも}って」と{言|い}っているので{違|ちが}います。\n「ポイント{理解|りかい}」の{問題|もんだい}を{解|と}くためには、{聞|き}き{取|と}るポイントに{関係|かんけい}のある{情報|じょうほう}を{選|えら}びながら{聞|き}くことが{必要|ひつよう}です。{話|はなし}の{中|なか}では{選択肢|せんたくし}とは{別|べつ}の{言|い}い{方|かた}が{使|つか}われていることが{多|おお}いので{注意|ちゅうい}します。\nこの{部分|ぶぶん}については「Ⅳ 「ポイント{理解|りかい}」のスキルを{学|まな}ぶ」で{練習|れんしゅう}します。",
          explain: [
            "Paarunga: choice-la '健康診断を受ける' nu irukku, aanaa audio-la '健康診断をしてもらおう' nu vandhuchu. Same meaning, vera words. Idhu dhaan 言い換え (いいかえ, paraphrase) — N2 listening-la romba common trap.",
            "'実は', 'でも', 'ただ' maadhiri words kku apram dhaan usually real answer varum. Indha words kettaa kaadhai innum koormaiyaa vechukkonga!"
          ]
        }
      ]
    }
  ]
});
