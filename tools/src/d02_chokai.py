from _h import *
DAY = 2

NUM4, NUM3 = ["1", "2", "3", "4"], ["1", "2", "3"]
def listen_q(id, q, n, ans, explain):
    """Choices are only heard, as in the real test: buttons show just the numbers."""
    return mcq(id, q, NUM4[:n], ans, explain, keys=[""] * n)

def answer(title, t, explain):
    return {"type": "text", "title": title, "t": t, "explain": explain}

SECTION = {
 "book": "chokai",
 "title": "問題紹介　3 概要理解・4 即時応答・5 統合理解",
 "source": "新完全マスター聴解 N2 · 問題紹介 · pp.6–12 · CD A03–A06",
 "blocks": [
  text("Inniki listening-la meedhi moonu question type: 概要理解 (overall gist), 即時応答 (quick response), 統合理解 (integrated). Ovvoru 例題-um: (1) audio kelunga, (2) answer select pannunga, (3) appram script open panni check pannunga.",
   "🎧 今日の聴解",
   ["CD A innum varala, adhanaala A03–A06 computer read-aloud. Book script-a appadiye padikkudhu; voice konjam robot maadhiri irukkum, aanaa words ellam correct."]),

  text("「概要理解」は、まとまりのある話を聞いて、その話全体の主題、話し手の意図、主張などを判断する問題です。実際の試験では、問題の前に練習があります。例題をやってみましょう。",
   "3　概要理解",
   ["概要理解(がいようりかい) = understanding the gist. Oru neenda pechu kettu, adhoda main topic (主題 しゅだい), speaker-oda intention (意図 いと), opinion (主張 しゅちょう) enna-nu decide pannanum.",
    "Trap: question munnaadi varaadhu! Pechu mudinja appram dhaan question + options kekkum. So full-aa kettu summary manasula vechukkonga."]),
  audio("☆例題3　CD A03", "a03",
   "この問題は、全体としてどんな内容かを聞く問題です。話の前に質問はありません。まず話を聞いてください。それから、質問と選択肢を聞いて、1から4の中から、最もよいものを一つ選んでください。"),
  listen_q("d2c-r3", "例題3　（選択肢は音声だけ）", 4, 2,
   "Answer 3 (スライド式本棚の長所). Pechu muzhukka 'slide type bookshelf' pathi — 簡単に取り出せる, 空間を有効に使える, 使いやすさが特徴 = ellam nalla points (長所 ちょうしょ). Vilai konjam adhigam-nu sonnaalum, adhu main point illa."),
  script("スクリプトと答え（p.7）· open after you answer", [
   ("テレビで男の人が話しています。", "TV-la oru aal pesuraaru. (Shopping programme maadhiri.)"),
   ("男：一般的な本棚は棚の位置が動かせない固定式で、棚の奥までがかなりあります。", "一般的(いっぱんてき) = ordinary. 本棚(ほんだな) = bookshelf. 棚(たな) = shelf. 位置(いち) = position. 固定式(こていしき) = fixed type. 奥(おく)までがかなりある = it's quite deep. Normal bookshelf = fixed, romba deep."),
   ("それで、つい本が並べてある手前にもまた本を並べてしまって、必要なときに奥の本が取り出せないということがありました。", "つい = without meaning to. 手前(てまえ) = front side. 取(と)り出(だ)せない = can't take out. Problem: munnaadi-yum books vechiduvom, pinnaadi irukkira book edukka mudiyaadhu (fixed type-oda 短所)."),
   ("しかし、今日ご紹介するこちらのスライド式は、奥にある本を簡単に取り出すことができます。", "しかし = but → key point varudhu! ご紹介(しょうかい)する = introduce. Slide type-la pinnaadi book easy-aa edukkalaam. ← 長所 ①"),
   ("棚が手前と奥とに2つあって、手前の方の棚を横にスライドさせれば、奥の棚が見えるようになっています。", "横(よこ)に = sideways. Rendu shelf: front shelf-a side-la slide pannaa, back shelf theriyum."),
   ("よく使う本は手前、大切なファイルなどは奥にしまうといった使い方もできますし、とにかく空間を有効に使えます。", "しまう = put away. とにかく = anyway. 空間(くうかん)を有効(ゆうこう)に使える = use space efficiently. ← 長所 ②"),
   ("値段は固定式のものに比べて少々高いですが、この使いやすさが特徴です。", "少々(しょうしょう) = a little. 特徴(とくちょう) = feature. Konjam vilai adhigam, aanaa easy-to-use dhaan special. ← 長所 ③"),
   ("男の人は、何について話していますか。", "Question: 'Avar edha pathi pesuraaru?'"),
   ("1　固定式本棚の長所", "長所(ちょうしょ) = good point."), ("2　固定式本棚の短所", "短所(たんしょ) = bad point. Fixed type problem konjam sonnaaru, aanaa adhu intro mattum."),
   ("3　スライド式本棚の長所", "✔ Correct."), ("4　スライド式本棚の短所", "少々高い only one small point; main topic illa."),
  ], extra=[answer("答え　3",
   "話全体から話の主題を理解する問題です。「こちらのスライド式」の「本棚」について、「簡単に取り出すことができます」「空間を有効に使えます」「使いやすさが特徴」と、主によい点を説明しています。これらをまとめたのが3です。\nこのように、多くの場合、話全体の主題や話し手の主張は一言で表されていないので、いくつかのキーワードや大切な内容を聞き取り、それらを整理してまとめる必要があります。\nこの部分については「Ⅴ 「概要理解」のスキルを学ぶ」で練習します。",
   ["Book solradhu: main topic oru word-la sollamaattaanga. Keywords (取り出せる, 有効, 使いやすさ) collect panni summary pannunga.", "Day 14–17-la (Ⅴ) idha innum practice pannuvom."])]),

  text("「即時応答」は、質問、報告、依頼などの短い文を聞いた後、すぐにそれに合う答え方を判断する問題です。実際の試験では、問題の前に練習があります。例題をやってみましょう。",
   "4　即時応答",
   ["即時応答(そくじおうとう) = quick response. Oru short sentence (question, report, request) kettu, adhukku correct reply edhu-nu udane decide pannanum.",
    "Paper-la onnum print aagirukkaadhu — 1 2 3 mattum. Speed mukkiyam: first sentence kettappave 'yaaru, enna pannraanga' purinjikkanum."]),
  audio("☆例題4　CD A04", "a04",
   "まず文を聞いてください。それから、それに対する返事を聞いて、1から3の中から、最もよいものを一つ選んでください。"),
  group("例題4", [
   listen_q("d2c-r4-1", "(1)", 3, 2, "Answer 3. 'じゃない' ↗ = confirming: 'Inniki late-aa irundhu work mudippen-nu sonna-la?' → Tanaka kilambraar pola. Reply: でも、風邪気味だから、もう帰るよ."),
   listen_q("d2c-r4-2", "(2)", 3, 1, "Answer 2. 'Ennoda pechu kettadhukku romba thanks.' → Reply: 'また何かあったら相談に乗りますよ' (innoru thadava edhavadhu irundhaa sollunga, naan kekkiren)."),
  ]),
  script("スクリプトと答え（p.9）· open after you answer", [
   ("(1)　女：あれ？　田中くん、今日は残って仕事片づけちゃうって言ってたじゃない。", "あれ？ = huh? (surprise). 残(のこ)る = stay back. 片(かた)づけちゃう = 片づけてしまう (finish off). 言ってたじゃない = 'you said, didn't you?' Tanaka bag eduthu kilambraar pola — adhaan 'あれ？'."),
   ("男：1　うん、今日は言ってなかったね。", "✘ Avan sonnaan; adhu pathi illa."),
   ("2　ああ、仕事がたくさん残ってるんだ。", "✘ Work irukku-nu sonnaa, adhu 'stay pannren' maadhiri — situation-ku match aagala."),
   ("3　でも、風邪気味だから、もう帰るよ。", "✔ 風邪気味(かぜぎみ) = a bit of a cold. 'Aanaa konjam jalathosham, so veetukku poren.'"),
   ("(2)　男：今日は話を聞いていただけて、よかったです。", "～ていただけて = (humble) that you listened to me. 'Inniki en pechu kettadhukku nandri, nalla irundhuchu.'"),
   ("女：1　いえ、つまらない話ばかりですみません。", "✘ Avanga dhaan kettaanga; 'en pechu boring' nu solla avasiyam illa."),
   ("2　また何かあったら相談に乗りますよ。", "✔ 相談(そうだん)に乗(の)る = give advice / listen to someone's problem."),
   ("3　時間がとれなくて、申し訳ありません。", "✘ Time edukka mudiyala-nu solradhu situation-ku opposite."),
  ], extra=[answer("答え　(1) 3　(2) 2",
   "(1)は、「～じゃない」が確認の意味であることに気をつけます。相手に確認をしていることから、相手の行動が、話し手が考えていたことと違うと推測できます。この場合、相手（田中くん）が残るのではなく帰ろうとしていると考えられるので、3が答えです。「あれ？」と言っていることからも、今の状況を不思議に思っていることがわかります。\n(2)は、自分の話を相手が聞いてくれたことに感謝する言い方です。それに対する返答ですから、「またいつでも聞きますよ」という意味の2が答えです。\n聞く文は短いので、まず最初の文を聞いたとき、だれが何をするのかをすぐに理解しなければなりません。同時に、返事の文についても聞いてすぐに理解する必要があります。また、音の変化や、イントネーション、音の高低などは意味に影響を与えるので、特に注意が必要です。\nこの部分については「Ⅱ 「即時応答」のスキルを学ぶ」で練習します。",
   ["Key: 'じゃない' with rising tone = checking (確認 かくにん), not negative. 'Neenga sonneenga illa?' feel.", "Intonation and sound changes (片づけちゃう, 言ってた) N2-la romba varum. Day 5–7-la (Ⅱ) practice."])]),

  text("「統合理解」は、いくつかの情報を整理・統合しながら内容を理解する問題です。主に\n・2人以上の話し手の意見を整理しながら聞き取るタイプ\n・ある話を聞いた後で、それについての意見や評価などを聞いて、判断するタイプ\nがあります。また、この問題だけ、実際の試験のときに練習がありません。例題をやってみましょう。",
   "5　統合理解",
   ["統合理解(とうごうりかい) = integrated comprehension. Pala information-a sethu yosikkanum.",
    "Type 1: 2-3 per discussion — yaar enna opinion sollraanga-nu note pannunga. Type 2: first oru explanation (options list), appram rendu per pesuvaanga — avanga condition-ku match aagura option select pannunga.",
    "Memo edunga! Indha type-ku note-taking dhaan weapon."]),
  audio("☆例題5　CD A05", "a05",
   "まず話を聞いてください。それから、質問と選択肢を聞いて、1から4の中から、最もよいものを一つ選んでください。"),
  listen_q("d2c-r5", "例題5　（選択肢は音声だけ）", 4, 1,
   "Answer 2 (サッカーをする). Pool → swimsuit fit aagaadhu (not keen). Jogging → son 'boring' sonnaan, appa drop pannitaaru. Catch ball → 'not much exercise'. Soccer → 'injury aagura alavukku vilaiyaada maatten' — no problem → 'じゃ、行こうか'."),
  script("スクリプトと答え（p.11）· open after you answer", [
   ("家族3人が休日の過ごし方について話しています。", "休日(きゅうじつ) = holiday. 過(す)ごし方(かた) = how to spend. Family 3 per: amma (女), appa (男1), son Takashi (男2)."),
   ("女：お父さん、またテレビの前でごろごろ？　外に出て体を動かしたほうがいいんじゃないの？　ちょっと太ってきたみたいだし。プールにでも行ってくれば？", "ごろごろ = lazing around. 体(からだ)を動(うご)かす = exercise. 太(ふと)ってきた = getting fat. Option 1: プール."),
   ("男1：たしかに少し運動不足だよな。水泳ねえ。太っちゃったから水着が入らないかもな。", "運動不足(うんどうぶそく) = lack of exercise. 水着(みずぎ)が入(はい)らない = swimsuit won't fit. → Pool ✘ (not keen)."),
   ("男2：ねえ、公園でサッカーしようよ。", "Son: Option 2 サッカー."),
   ("男1：サッカーは久しぶりだな。でも最近、運動してないから、体が動くかな。健康のためなら、本当はジョギングなんかの方が続けやすいんだけど。たかし、一緒に走るか。", "久(ひさ)しぶり = after a long time. 続(つづ)けやすい = easy to keep up. Appa suggests Option 3 ジョギング."),
   ("男2：えー、ただ走るだけなんてつまんないよ。", "つまんない = つまらない (boring). Son rejects jogging → appa adhukku appram jogging pathi pesala. → ✘"),
   ("女：だけど、サッカーやってけがなんかしたら、仕事に差し支えるんじゃない？", "けが = injury. 差(さ)し支(つか)える = interfere. Amma worried about soccer."),
   ("男1：プロじゃないんだから、けがするほどやんないよ。", "やんない = やらない. 'Pro illa, injury aagura alavukku vilaiyaada maatten.' → soccer problem illa ✔"),
   ("男2：キャッチボールでもいいよ。", "Option 4 キャッチボール."),
   ("男1：それじゃ、あんまり運動にならないなあ。うーん、最近たかしともゆっくり遊んでないし……。よし。じゃ、行こうか。", "運動にならない = won't be (real) exercise → ✘. よし。じゃ、行こうか = 'OK, let's go (play soccer)'."),
   ("お父さんは今日、何をすることにしましたか。", "～ことにしました = decided to."),
   ("1　プールで泳ぐ　2　サッカーをする　3　ジョギングをする　4　キャッチボールをする", "Answer 2."),
  ], extra=[answer("答え　2",
   "水泳については「水着が入らないかも」と、積極的に賛成していません。また、ジョギングは「続けやすい」と言って子供を誘ったところ、子供が「つまんない（つまらない）」と反対したので、その後話を続けるのをあきらめています。子供の提案のうちサッカーは「けがするほどやんない（やらない）」と問題ないことを伝え、キャッチボールは「あんまり運動にならない」と反対していることから、サッカーをすることがわかります。\nこのように例題5のタイプの問題では、2人以上の話し手による話から意見を聞き取ります。「概要理解」の問題と似ていますが、人数が多いので、複雑になります。それぞれの話し手の意見の対立点を早い段階で聞き分け、それを整理しながら聞く練習が必要です。",
   ["Memo style: プール ✘ / サッカー ○ / ジョギング ✘ / キャッチボール ✘. Ovvoru option-kkum yaar enna sonnaanga-nu tick pannunga.", "対立点(たいりつてん) = points of disagreement."])]),

  audio("☆例題6　CD A06", "a06",
   "まず話を聞いてください。それから、二つの質問を聞いて、それぞれ問題用紙の1から4の中から、最もよいものを一つ選んでください。\n質問1　1 1番　2 2番　3 3番　4 4番\n質問2　1 1番　2 2番　3 3番　4 4番"),
  group("例題6", [
   mcq("d2c-r6-1", "質問1　女の人はどのバスに乗りますか。", ["1番", "2番", "3番", "4番"], 1,
    "Answer 2 (2番). Woman: '商店街に寄ってから帰る' → 商店街を通る bus = 2番."),
   mcq("d2c-r6-2", "質問2　男の人はどのバスに乗りますか。", ["1番", "2番", "3番", "4番"], 2,
    "Answer 3 (3番). Man: seekiram veetukku poganum, mazhai-la 20 min wait panna maatten. 3番 'もうすぐ来る' and reaches about the same time as 1番 → 'あっちに乗るよ' → 'バスが来た'."),
  ]),
  script("スクリプトと答え（p.12）· open after you answer", [
   ("男の人と女の人がバスについての案内を聞いています。", "案内(あんない) = information/announcement. Bus stop-la oru staff (男1) explain pannraaru; appram rendu per (男2, 女) pesuvaanga."),
   ("男1：ここから山下駅に行くバスは4系統出ています。", "山下駅(やましたえき). 4系統(けいとう) = 4 routes. Memo ready!"),
   ("一番早く着くのは、1番のバスなんですが、次のバスまではあと20分ぐらいですね。", "1番: fastest, aanaa next bus 20 min wait."),
   ("2番のバスは商店街を通ります。マツダデパート前にも止まりますが、これもあと20分ほど待ちますね。", "2番: 商店街(しょうてんがい, shopping street) vazhiya, department store-la nikkum; 20 min wait."),
   ("3番は安田大学前を通って行くので遠回りになりますが、もうすぐ来るので1番のバスに乗るのと着く時間はほとんど変わらないでしょうね。", "3番: 遠回(とおまわ)り = roundabout route, aanaa もうすぐ来る (coming soon) → arrival time 1番 maadhiri dhaan."),
   ("あと、4番は今そこに止まっていますが、住宅地の中を通るバスで、この時間だと駅まで一番時間がかかるかもしれませんね。", "4番: ippo nikkudhu, aanaa 住宅地(じゅうたくち, residential area) vazhiya — slowest."),
   ("男2：僕、この後用事があるから、できるだけ早く帰りたいんだけど。", "用事(ようじ) = errand. Condition ①: early-aa poganum."),
   ("女：そう。わたしはちょっと買い物もしたいし、商店街の方に寄っていこうかな。", "寄(よ)る = drop by. Woman condition: shopping street → 2番."),
   ("男2：そっか。じゃ、悪いけど、違うバスで先に帰るよ。一番早いって言ってたのは、これだけ。うーん、あと20分か。雨が降ってるし、寒いから、外で待ちたくないな。どうせ着く時間が同じくらいなら、あっちに乗るよ。", "1番 = 20 min wait ✘ (rain, cold). どうせ = anyway. 'Same time-la reach aanaa, adhula (3番) yeruren.'"),
   ("ね、一緒に乗って、駅で買い物したらどう？", "'Ennoda vandhu station-la shopping pannalaame?'"),
   ("女：うーん、町の中も見てみたいし、やっぱり商店街に寄ってから帰るわ。", "やっぱり = after all → 2番 confirmed."),
   ("男2：そっか。あ、バスが来た。じゃ、またね。", "'Bus vandhuduchu' → もうすぐ来る bus = 3番."),
   ("質問1　女の人はどのバスに乗りますか。", "→ 2番"), ("質問2　男の人はどのバスに乗りますか。", "→ 3番"),
  ], extra=[answer("答え　質問1　2　質問2　3",
   "まず、最初の話を聞き取ってから、2人の話を聞き、条件に合うものを選びます。男の人は「早く帰りたい」「外で待ちたくない」「バスが来た」と言っているので、「もうすぐ来る」「1番のバスに乗るのと着く時間はほとんど変わらない」という3番に、女の人は「商店街に寄ってから帰る」と言っているので、「商店街を通」る2番に乗るとわかります。\n例題6のタイプの問題では、2種類の話を聞き、その両方の情報を比較したり関連づけたりして答えます。最初の話を聞いて情報を整理し、次の話（会話）で述べられている条件に合うものはどれかを判断します。ですから、必要な情報を聞き取ってメモをとる練習、それをもとに情報を統合しながら聞く練習が必要です。\nこれらについては「Ⅵ 統合問題のスキルを学ぶ」で練習します。",
   ["Memo table podunga: 1番 fast/20分待ち, 2番 商店街/20分, 3番 遠回り/もうすぐ, 4番 now/slowest. Appram ovvoruthar condition match pannunga.", "Day 18–19-la (Ⅵ) idha practice pannuvom."])]),
 ],
}
