from _h import *
DAY = 19

NOTE = "Real CD track. The book prints no script or answer for this one, so the script below was transcribed from the CD and checked by sensei; the answer is sensei's."
BOOK = "Real CD track. Script and answer are printed in the book."
N4 = ["1", "2", "3", "4"]

def pick(id, q, opts, ans, explain, keys=None):
    return mcq(id, q, opts, ans, explain, keys=keys or N4)

def table(title, head, rows, note=None, explain=None):
    b = {"type": "table", "title": title, "head": head, "rows": rows}
    if note: b["note"] = note
    if explain: b["explain"] = explain
    return b

def memo(id, label, opts, ans, ex):
    return dict(choose(id, label, opts, ans, ex), plainKeys=["opts"])

SECTION = {
 "book": "chokai",
 "title": "実力養成編　Ⅵ「統合理解」のスキルを学ぶ　2 2種類の話を整理する・確認問題",
 "source": "新完全マスター聴解 N2 · 実力養成編 Ⅵ-2・確認問題 · pp.90–95 · CD B37–B44",
 "blocks": [
  items("2　2種類の話を整理する", [
   ("この問題形式では、2種類の話（例：あることについての説明＋それについての会話）を整理して聞きます。最初の話では、選択肢を見ながら大切な点を聞き取ってメモします。その後の会話では、最初にメモした情報について、2人の意見の違いなどを聞き取ります。",
    ["Sensei: This is JLPT 聴解 問題5 番号3 type. Part 1: a shop clerk / announcer explains 4 things (A, B, C, D). Part 2: two people talk about which one each will choose. Two questions: 'which does the man choose?' and 'which does the woman choose?'",
     "Method: while part 1 plays, write 2–3 keywords next to each printed option (1 Aセット: パスタ・飲み物…). In part 2 listen for the reason each person gives, then match it to your notes.",
     "Thanglish: Mudhal part-la 4 options-kku side-la notes podunga. Rendaavadhu part-la man enna solraar, woman enna solraanga — separate-a track pannunga. Last-la 'これにしよう' enga varudhu nu paarunga."]),
  ]),

  # ---------- 例題2 ----------
  audio("☆例題2　①　CD B37", "b37", "最初の話を聞いて、選択肢の横に下から当てはまるものを選んで書いてください。", tts=False, note=BOOK),
  group("例題2　①　メモ（下から選ぶ：パスタ・ピザ・飲み物・サラダ・デザート・肉か魚の料理・パンかライス）", [
   text("1　Aセット：パスタ、飲み物\n2　Bセット：ピザ、飲み物\n3　Cセット：パスタかピザ、飲み物、サラダ、デザート\n4　Dセット：肉か魚の料理、パンかライス、サラダ、デザート、飲み物", "答え（本）"),
  ], scored=False),
  audio("例題2　②　CD B38", "b38", "次に2人の会話と質問を聞いて、上の1から4の中から、最もよいものを選んでください。", tts=False, note=BOOK),
  group("例題2　②", [
   pick("d19c-e2-1", "質問1　男の人はどのセットにしますか。", ["Aセット","Bセット","Cセット","Dセット"], 3,
    ["Book's answer: 4.", "男の人は「ライス」「肉」と言っているので、「Dセット」です。Only Dセット has 肉か魚 and パンかライス."]),
   pick("d19c-e2-2", "質問2　女の人はどのセットにしますか。", ["Aセット","Bセット","Cセット","Dセット"], 2,
    ["Book's answer: 3.", "女の人は「パスタがいい」と言っているので「Aセット」か「Cセット」で、「デザート」の話の後、「サラダも付いている」ことを確認してから「これにしてみよう」と言っているので、「Cセット」です。",
     "Thanglish: Pasta venum → A or C. Dessert + salad irukku nu confirm panni 'idhu try pannuren' → C."]),
  ]),
  script("例題2　スクリプト（本）", [
   ("レストランで店員がメニューを説明しています。", ""),
   ("男1：本日のランチは次の4種類になっております。Aセットはパスタ、Bセットはピザで、それぞれお飲み物が付いております。Cセットは、AセットかBセットのどちらかに、{食前|しょくぜん}のサラダと{食後|しょくご}のデザートが付いたものです。パスタかピザをお選びください。Dセットは、肉か魚のお料理と、それからパンかライスを選んでいただいて、こちらもサラダとデザート、お飲み物が付いております。",
    ["The 4 sets. Note them as you listen: A = pasta + drink; B = pizza + drink; C = A or B + salad + dessert; D = meat or fish + bread or rice + salad + dessert + drink.", "食前(しょくぜん) = before the meal. 食後(しょくご) = after the meal."]),
   ("女　：どれにしようかな。決まった？", ""),
   ("男2：今日はたくさん食べたい気分なんだよね。ちょっと高いけど、今日はこれ。[[ライスにしよう]]。", "Rice → only D has rice."),
   ("女　：お肉とお魚が選べるけど、どっちにする？", ""),
   ("男2：やっぱり[[肉]]だな。", "Meat → D confirmed."),
   ("女　：わたしは[[パスタがいいな]]。Aセットは850円なのね。", "Pasta → A or C."),
   ("男2：あれ？　デザートはいいの？", ""),
   ("女　：うーん。デザートが付くと、1,200円か。アイスクリームかケーキが選べるんだ。", "With dessert = C (1,200 yen)."),
   ("男2：ここのケーキ、おいしいよ。それで僕はいつもデザート付きのにしてるんだ。", ""),
   ("女　：ふーん。サラダも付いてるんだっけ。じゃ、[[これにしてみよう]]。", "Salad and dessert → C."),
   ("質問1　男の人はどのセットにしますか。\n質問2　女の人はどのセットにしますか。", ""),
  ], extra=[text("答え　①（上のメモ）　②質問1　4　質問2　3", "答え（本）")]),

  # ---------- 練習2 (1) ----------
  audio("練習2 (1)　①　CD B39", "b39", "最初の話を聞いて、選択肢の横に下から当てはまるものを選んで書いてください。", tts=False, note=NOTE),
  group("練習2 (1)　①　メモ（下から選ぶ：バッグ・布ぞうり・かご・なべ{敷|し}き／広告・古い布・新聞紙・葉書）", [
   memo("d19c-r21-a", "1　Aグループ", ["バッグ／新聞紙","かご／広告","布ぞうり／古い布","なべ{敷|し}き／葉書"], 0, "Aグループは新聞紙で買い物用のバッグを作ります."),
   memo("d19c-r21-b", "2　Bグループ", ["バッグ／新聞紙","かご／広告","布ぞうり／古い布","なべ{敷|し}き／葉書"], 1, "Bグループはカゴなんですが、これ、広告の紙から作るんですよ."),
   memo("d19c-r21-c", "3　Cグループ", ["バッグ／新聞紙","かご／広告","布ぞうり／古い布","なべ{敷|し}き／葉書"], 2, "Cグループはこの布ぞうりです。古い布を裂いて、ひもにして編んでいきます."),
   memo("d19c-r21-d", "4　Dグループ", ["バッグ／新聞紙","かご／広告","布ぞうり／古い布","なべ{敷|し}き／葉書"], 3, "Dグループは葉書でなべ{敷|し}きを作ります。はがきを40枚使って…"),
  ], scored=False),
  audio("練習2 (1)　②　CD B40", "b40", "次に2人の会話と質問を聞いて、上の1から4の中から、最もよいものを選んでください。", tts=False, note=NOTE),
  group("練習2 (1)　②", [
   pick("d19c-r21-1", "質問1　男の人はどのグループに入りますか。", ["Aグループ","Bグループ","Cグループ","Dグループ"], 0,
    ["Sensei's answer: 1.", "He wants to make one for his grandma, who refuses plastic shopping bags (レジ袋を{断|ことわ}っている) → a shopping bag. At the end: 僕はやっぱりこれ。はがきは集めるのが大変そうだけど新聞紙ならいくらでもあるからね → 新聞紙 = A."]),
   pick("d19c-r21-2", "質問2　女の人はどのグループに入りますか。", ["Aグループ","Bグループ","Cグループ","Dグループ"], 1,
    ["Sensei's answer: 2.", "She first likes the 布ぞうり (C), but it looks hard (左右2つ作らないといけない, 力がいりそう). Then: お菓子やみかんを入れておくのに喜ばれそうだから、これにしようかな → a basket = B.",
     "Thanglish: First choice change aagudhu — adhu dhaan trap. Final 'これにしようかな' paarunga."]),
  ]),
  script("練習2 (1)　スクリプト（CDから）", [
   ("ボランティア講習会で女の人が説明しています。", "講習会(こうしゅうかい) = training session."),
   ("女1：さて、皆さんには来週、お年寄りの施設に行って{小物|こもの}の作り方を指導していただきます。今日はその実習なんですが、4つのグループに分かれて作業を行います。", "小物(こもの) = small articles. 指導(しどう) = teach. 実習(じっしゅう) = practice."),
   ("まず、Aグループは[[新聞紙で買い物用のバッグ]]を作ります。{丈夫|じょうぶ}でしっかりしているでしょ。", "A = bag from newspaper."),
   ("Bグループは[[かご]]なんですが、これ、[[広告の紙]]から作るんですよ。このかごにはテレビのリモコンや果物が入れられて便利です。", "B = basket from advertising flyers."),
   ("Cグループはこの[[布ぞうり]]です。[[古い布]]を{裂|さ}いて、ひもにして{編|あ}んでいきます。このぞうり、{履|は}いたとき気持ちいいですよ。", "C = cloth sandals from old cloth. 裂く(さく) = tear. 編む(あむ) = weave."),
   ("最後にDグループは[[葉書でなべ{敷|し}き]]を作ります。はがきを40枚使って作るんですが、作り方は簡単です。熱いお鍋を置いても大丈夫ですよ。", "D = pot stand from postcards."),
   ("皆さんは好きなグループに入って、講師の先生から作り方を教わってください。来週はお年寄りに指導していただきますから、頑張って作ってくださいね。", "講師(こうし) = instructor."),
   ("男：僕、これにしよう。うちのおばあちゃんにも作ってあげよう。スーパーに行っても[[レジ袋を{断|ことわ}っている]]みたいだから。", "Bag for grandma → A."),
   ("女2：わたしはこれ。部屋で履けるし、お年寄りは古い服、捨てられない人、多いでしょ？　きっと喜ばれると思う。", "She likes C (sandals)…"),
   ("男：でも作り方が難しそうだよ。左右2つ作らないといけないし。", "…but they're hard: you must make two."),
   ("女2：あ、そっか。結構力がいりそうだしね。じゃあ、[[お菓子やみかんを入れておくのに喜ばれそうだから、これにしようかな]]。", "Changes to B (basket)."),
   ("男：僕はやっぱりこれ。はがきは集めるのが大変そうだけど、[[新聞紙ならいくらでもある]]からね。", "Stays with A."),
   ("質問1　男の人はどのグループに入りますか。\n質問2　女の人はどのグループに入りますか。", ""),
  ], extra=[text("答え　①1 バッグ・新聞紙　2 かご・広告　3 布ぞうり・古い布　4 なべ{敷|し}き・葉書　②質問1　1　質問2　2", "答え（sensei）")]),

  # ---------- 練習2 (2) ----------
  audio("練習2 (2)　①　CD B41", "b41", "最初の話を聞いて、選択肢の横にメモを書いてください。", tts=False, note=NOTE),
  group("練習2 (2)　①　メモ", [
   memo("d19c-r22-a", "1　A会場", ["野菜・果物・花の販売","もちつき","伝統的な遊びの体験・ゲーム大会","人形づくり（見学・指導）"], 0, "A会場では、今朝採れたばかりの野菜や果物、そして花などを販売しております."),
   memo("d19c-r22-b", "2　B会場", ["野菜・果物・花の販売","もちつき","伝統的な遊びの体験・ゲーム大会","人形づくり（見学・指導）"], 1, "B会場ではもちつきを行います。出来上がったお餅はその場で召し上がっていただけます."),
   memo("d19c-r22-c", "3　C会場", ["野菜・果物・花の販売","もちつき","伝統的な遊びの体験・ゲーム大会","人形づくり（見学・指導）"], 2, "C会場はこの地方の伝統的な遊びの体験とゲーム大会を行います。親子でご一緒にご参加ください."),
   memo("d19c-r22-d", "4　D会場", ["野菜・果物・花の販売","もちつき","伝統的な遊びの体験・ゲーム大会","人形づくり（見学・指導）"], 3, "D会場では人形づくりを見ていただけます。また作り方の指導もいたします."),
  ], scored=False),
  audio("練習2 (2)　②　CD B42", "b42", "次に2人の会話と質問を聞いて、上の1から4の中から、最もよいものを選んでください。", tts=False, note="Real CD track. On this CD copy the 質問1 announcement is silent (only 質問2 is heard). 質問1 below is sensei's version of the question, built from the conversation; both answers are sensei's."),
  group("練習2 (2)　②", [
   pick("d19c-r22-1", "質問1（sensei）　女の人は最初にどの会場へ行きますか。", ["A会場","B会場","C会場","D会場"], 3,
    ["Sensei's answer: 4.", "わたしは先に人形を作るところを見てから、花とか野菜を見てきたい → first D (dolls), then A (vegetables). 先に = first."]),
   pick("d19c-r22-2", "質問2　男の人は最初にどの会場へ行きますか。", ["A会場","B会場","C会場","D会場"], 2,
    ["Sensei's answer: 3.", "He rejects もちつき (学校でもする機会がある) and wants 子供と一緒に参加できるもの; 昔の遊びなんか懐かしい → C会場 (traditional games, 親子でご一緒に).",
     "Thanglish: Amma 'saapadu idam (B)' nu solraanga, appa 'school-la mochi panniyiruppaan, kid kooda serndhu vilayaadra idam' nu C choose pannuraar."]),
  ]),
  script("練習2 (2)　スクリプト（CDから）", [
   ("ふるさと祭りの会場でアナウンスをしています。", ""),
   ("女1：本日は、ふるさと祭りにようこそおいでくださいました。広場の周りの4つの会場で、それぞれ楽しいイベントを行っております。", ""),
   ("[[A会場]]では、今朝採れたばかりの[[野菜や果物、そして花]]などを販売しております。", "A = selling vegetables, fruit, flowers."),
   ("[[B会場]]では[[もちつき]]を行います。出来上がったお{餅|もち}はその場で{召|め}し{上|あ}がっていただけます。", "B = pounding rice cakes; you can eat them there."),
   ("[[C会場]]はこの地方の[[伝統的な遊びの体験とゲーム大会]]を行います。親子でご一緒にご参加ください。", "C = traditional games, parents and children together."),
   ("そして[[D会場]]では[[人形づくり]]を見ていただけます。また、作り方の指導もいたしますので、皆様どうぞおいでください。", "D = watching / learning doll-making."),
   ("女2：どの会場もみんな面白そうね。でも、この子が楽しめるところというと、やっぱり食べるところかしらね。おもちつきなんかどう？", "She suggests B for the child."),
   ("男：もちつきは学校でもする機会があるんじゃない？　せっかくの機会だから[[子供と一緒に参加できるもの]]にしたいな。[[昔の遊び]]なんか懐かしいし。", "He chooses C."),
   ("女2：そう。わたしは[[先に人形を作るところを見て]]から、花とか野菜を見てきたいんだけど、いい？　今晩のおかずも探せそうだし。", "She goes to D first, then A."),
   ("男：わかった。じゃあ、ここで{一旦|いったん}別れて、後で広場で会おう。", "一旦(いったん) = for a while."),
   ("質問2　男の人は最初にどの会場へ行きますか。", ""),
  ], extra=[text("答え　①1 野菜・果物・花の販売　2 もちつき　3 伝統的な遊びの体験・ゲーム大会　4 人形づくり　②質問1（sensei）4　質問2　3", "答え（sensei）")]),

  # ---------- 確認問題 ----------
  audio("確認問題 (1)　CD B43", "b43", "まず話を聞いてください。それから、質問と選択肢を聞いて、1から4の中から、最もよいものを一つ選んでください。", tts=False, note=NOTE),
  group("確認問題 (1)", [
   pick("d19c-k1", "（質問と選択肢はCDで聞きます）", ["1","2","3","4"], 3,
    ["Sensei's answer: 4.", "Question: 女の人が夜行バスで行きたいと思った理由は何ですか。 1 乗り換えがないから　2 4時に起きられないから　3 リラックスできるから　4 テントに泊まりたくないから",
     "She worried she couldn't sleep on the bus. The other option was staying near the mountain the night before — but rooms are full, so it would be a tent. 「えっ、テントに泊まるの？　それだけは勘弁してよ」 → then she agrees: わかった、バスにしよう. So the deciding reason is 4.",
     "Trap: 1 (乗り換えもないし楽) and the low price were said, but they didn't decide it for her."]),
  ]),
  script("確認問題 (1)　スクリプト（CDから）", [
   ("友達3人が山へ行く相談をしています。", ""),
   ("男1：大空山までは、やっぱり電車とバスを乗り継いでいくしかないのかなあ。", "乗り継ぐ(のりつぐ) = change trains/buses."),
   ("女：5時の電車で行けば、上まで登って、暗くなる前に山を降りて来られるかしら。", ""),
   ("男2：じゃあ、4時起きか。大変だね。夜行バスはどう？　夜行バスなら半分ぐらいの値段で行けるし。", "夜行(やこう)バス = overnight bus."),
   ("男1：夜行バスかあ。乗り換えもないし、楽かもね。", ""),
   ("女：確かに安いのは魅力だけど、バスの中で眠れるかしら。", "She is worried about sleeping."),
   ("男2：大丈夫だよ。最近のバスはシートも広くて、ベッドみたいに倒せるんだって。", ""),
   ("男1：前の日にぐっすり寝たかったら、前日どこかに宿を取るか。でも、もう予約はいっぱいだろうから、テントかなあ。", "The alternative: a tent."),
   ("女：えっ、[[テントに泊まるの？　それだけは勘弁してよ]]。", "勘弁(かんべん)して = please spare me. → the reason."),
   ("男1：そうだよな。荷物増えちゃうしな。", ""),
   ("男2：じゃあ、やっぱり夜行しかないでしょう。", ""),
   ("女：わかった。バスにしよう。", ""),
   ("女の人が夜行バスで行きたいと思った理由は何ですか。\n1　乗り換えがないから\n2　4時に起きられないから\n3　リラックスできるから\n4　テントに泊まりたくないから", ""),
  ], extra=[text("答え　4（sensei）\nSpeaker labels are sensei's best reading of the voices; the answer doesn't depend on them.", "答え")]),

  audio("確認問題 (2)　CD B44", "b44", "まず話を聞いてください。それから、二つの質問を聞いて、それぞれ1から4の中から、最もよいものを一つ選んでください。", tts=False, note=NOTE),
  group("確認問題 (2)", [
   pick("d19c-k2-1", "質問1　女の人はどのセットを選びますか。", ["ありがとうセット","しあわせセット","ふんわりセット","うきうきセット"], 1,
    ["Sensei's answer: 2.", "うちのお母さん、甘いもの好きだから、これにしようかな → しあわせセット (two kinds of sweets + tea). She rejects flowers: 水やったりするの面倒くさがるんだ."]),
   pick("d19c-k2-2", "質問2　男の人はどのセットを選びますか。", ["ありがとうセット","しあわせセット","ふんわりセット","うきうきセット"], 3,
    ["Sensei's answer: 4.", "He first thinks of ふんわり (料理のときに使ってもらえるもの), but she says his mum is stylish (おしゃれ), and he remembers 最近は絵を習い始めて外に出ることも増えた → じゃあ、これにしよう = うきうきセット (scarf + parasol, for stylish mothers who go out a lot)."]),
  ]),
  script("確認問題 (2)　スクリプト（CDから）", [
   ("デパートで店員が話しています。", ""),
   ("女1：母の日のプレゼントですか。それなら……。この[[ありがとうセット]]は、母の日の花、[[赤いカーネーションにクッキー]]を添えたセットでございます。", "ありがとう = carnation + cookies. 添える(そえる) = add."),
   ("次にこちらの[[しあわせセット]]は、[[お菓子2種類と紅茶]]のセットで、お好きなお菓子が選べます。", "しあわせ = 2 sweets + tea."),
   ("それからこちらの[[ふんわりセット]]は、[[柔らかいタオルとエプロン]]のセットです。台所の仕事が多いお母様に喜ばれます。", "ふんわり = towel + apron, for mothers who cook a lot."),
   ("最後は[[うきうきセット]]ですが、[[おしゃれなスカーフと日傘]]のセットです。スカーフと日傘の{柄|がら}が合っていて、[[外出の多いおしゃれなお母様]]にぴったりのセットです。", "うきうき = scarf + parasol, for stylish mothers who go out a lot. 柄(がら) = pattern."),
   ("女2：うちのお母さん、[[甘いもの好きだから]]、これにしようかな。", "→ しあわせ."),
   ("男：え？　お花はいいの？", ""),
   ("女2：うん、水やったりするの、面倒くさがるんだ。", "No flowers."),
   ("男：ふーん。僕は料理のときに使ってもらえるものにしようかな。", "He's thinking of ふんわり…"),
   ("女2：でも、つよし君のお母さん、おしゃれだから、これもいいんじゃない？", "…she suggests うきうき."),
   ("男：ああ、そういえば最近は絵を習い始めて、外に出ることも増えたしね。[[じゃあ、これにしよう]]。", "→ うきうき."),
   ("質問1　女の人はどのセットを選びますか。\n質問2　男の人はどのセットを選びますか。", ""),
  ], extra=[text("答え　質問1　2　質問2　4（sensei）", "答え")]),
 ],
}
