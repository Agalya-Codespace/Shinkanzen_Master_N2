from _h import *
DAY = 6

def passage(title, paras, explain, notes=None, src=None):
    b = {"type": "passage", "title": title, "paras": paras, "explain": explain}
    if notes: b["paras"] = paras + notes
    if src: b["cite"] = "（" + src + "）"
    return b

def toi(id, q, opts, ans, explain):
    return mcq(id, "【問い】" + q, opts, ans, explain)

def kaisetsu(n, lines):
    return {"type": "reveal", "label": "本の解説（別冊）：練習%d" % n,
            "children": [{"type": "items", "title": "解答・解説", "items": [{"t": x} for x in lines]}]}

def T(s): return {"t": s}

SECTION = {
 "book": "dokkai",
 "title": "2. 問いを解く技術を身につける　1）指示語を問う",
 "source": "新完全マスター読解 N2 · 第1部 評論・解説・エッセイなど · pp.38–45 · 例題 answers in the book; 練習 answers from 別冊 解答 pp.8–9",
 "blocks": [
  items("◆指示語を問う", [
   ("「これ・それ・あれ」「このこと・そのこと・あのこと」などの「指示語」が何を指しているかを問う問題である。",
    "指示語(しじご) = pointing words: これ・それ・あれ・こんな・そういう. Question: 'indha それ edha point pannudhu?'"),
   ("次の順番で考えよう。",
    "Order-aa yosinga:"),
   ("・「指示語」を含む文をよく見て、内容をつかもう。",
    "Step 1: 指示語 irukkira sentence-a nalla padichu, meaning purinjikonga."),
   ("・その文の前後を見て、「指示語」が指す言葉を探そう。",
    "Step 2: Andha sentence-oda munnaadi, pinnaadi paathu, adhu point pannra words-a thedunga."),
   ("※特に直前の文は必ずよく見よう。",
    "直前(ちょくぜん) = right before. 90% answer munnaadi irukkira sentence-la dhaan irukkum!"),
  ], explain="Inniki technique: 指示語. それ/そんなこと/そういう～ vandhaa, adhu munnaadi sonna edhaiyo point pannudhu. Answer-a 指示語-oda edathula pottu, meaning sariyaa varudhaa-nu check pannunga."),

  passage("☆例題9　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "多くの人が使う、「またにしてください」「今はちょっと」という、その場しのぎ（注1）的な{遠回|とおまわ}しの断り方があります。でもそんな言い方が通用しないことは、一度、何かの{勧誘|かんゆう}電話でも経験してみれば、わかると思います。すぐに、「では、いつ連絡さしあげましょうか」「明日の{今頃|いまごろ}ならばよろしいですか」と時間の空いているところを探してきます。真面目でウソをつけない人は、{暇|ひま}のある時間をつい答えてしまうかもしれません。",
   "相手が正当な要求をしてきているとしたら、それに対して真面目な対応をするのが{筋|すじ}（注2）でしょう。当たり前のように思えます。{一見|いっけん}、これは正しい{対処|たいしょ}だと思われますが、それは相手がまともな場合に限ります。{近頃|ちかごろ}では、①[[そんなこと]]をすると、うっかりだまされてしまうことがあるのです。",
  ], [
   "（注1）その場しのぎ：後のことは考えずに、そのときの状況だけで何とかしようとすること　（注2）{筋|すじ}：当然そうするべきこと",
   "Para 1: 遠回(とおまわ)し = indirect. 断(ことわ)り方 = way of refusing. 通用(つうよう)しない = doesn't work. 勧誘(かんゆう)電話 = sales call. 'Appuram paakkalaam' sonna, 'Seri, naalai indha time OK-vaa?'-nu kekkaanga.",
   "Para 2: 正当(せいとう)な要求(ようきゅう) = fair request. 対応(たいおう) = respond. 一見(いっけん) = at first glance. 対処(たいしょ) = deal with. まとも = decent. Chain: それ → 正当な要求, これ → 真面目な対応をする, そんなこと → これ (= same thing).",
  ], src="西田公昭『だましの手口　知らないと損する心の法則』PHP研究所"),
  toi("d6d-e9", "①そんなこととは何を指しているか。", [
   "正当な要求をすること",
   "真面目に対応すること",
   "相手がまともな場合に対処すること",
   "真面目でウソをつけない人に答えてしまうこと"], 1,
   ["Answer 2. そんなこと = これ = 相手の要求に対して、真面目な対応をすること.",
    "Check: '近頃では、真面目に対応すると、うっかりだまされてしまう' ✓ meaning sariyaa varudhu."]),
  {"type": "reveal", "label": "本の解説：例題9", "children": [
   items("ステップ1　本文を読んで全体をつかもう", [
    ("キーワード：断り方、勧誘電話、だまされる、書名『だましの手口』＊　→　テーマは、だますこと？", "Keywords → theme guess."),
    ("＊書名がいつもキーワードになるとは限らないが、ヒントになることもある。", "Book title sometimes gives a hint."),
   ]),
   items("ステップ2　問いを見て本文から答えを探そう　「指示語」に注目する", [
    ("相手が[[正当な要求]]をしてきているとしたら、", "↑ それ points here."),
    ("[[それ]]に対して[[真面目な対応をする]]のが筋でしょう。", "↓ これ points to 真面目な対応をする."),
    ("一見、[[これ]]は正しい対処だと思われますが、…", "これ = 真面目な対応をする."),
    ("近頃では、①[[そんなこと]]をすると、うっかりだまされてしまうことがあるのです。", "そんなこと = これ."),
    ("そんなこと＝相手の要求に対して、真面目な対応をすること", "Answer."),
   ]),
   items("ステップ3　選択肢と比べよう", [T("2：正解"), T("・下線部に「答え」を入れ、意味が通るかどうか確かめよう。")]),
  ]},

  items("◆下線部の「指示語＋N（名詞）」が何を指すかを問う問題", [
   ("「N（名詞）」が指す言葉を探そう。",
    "そういう感覚, そんな損得勘定 maadhiri 指示語 + Noun vandhaa, andha Noun (感覚 = feeling, 勘定 = calculation) enna-nu munnaadi thedunga."),
  ]),

  passage("☆例題10　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "私は新入社員によくこう言うんです。",
   "「君たちはお金をもらって会社で仕事を教えてもらい、{鍛|きた}えられている。給料をもらうなんて話が逆だろう。会社がもらいたいくらいだ。{授業料|じゅぎょうりょう}、持ってこい」",
   "これで本当に持ってきたらすごいことですが、今のところいません。しかし実際、新入社員を受け入れる会社としては、①[[そういう感覚]]でいるわけです。",
  ], [
   "新入社員(しんにゅうしゃいん) = new employees. 鍛(きた)えられる = be trained. 話が逆(ぎゃく) = it's the other way round. 授業料(じゅぎょうりょう) = tuition fee. 'Neenga company-la kathukkuren, so neenga dhaan fees kattanum!' (joke, but company really feels that way).",
  ], src="丹羽宇一郎『負けてたまるか！　若者のための仕事論』朝日新聞出版"),
  toi("d6d-e10", "①そういう感覚とは何を指しているか。", [
   "新入社員に給料を払って、仕事を学ばせるのは、授業料だからしかたがない。",
   "一人前の社員に育てるために、新入社員からお金をもらうのは話が逆だ。",
   "仕事を教えてもらっている新入社員が授業料を払わないのはすごいことだ。",
   "新入社員は、給料をもらうどころか、会社に授業料を払ってもいいくらいだ。"], 3,
   ["Answer 4. そういう感覚 = the feeling in the quote: 給料をもらうなんて話が逆, 授業料、持ってこい.",
    "2: reversed — the writer says getting salary is 逆, not getting money from them. 3: すごい is about actually bringing it."]),
  {"type": "reveal", "label": "本の解説：例題10", "children": [
   items("ステップ1　本文を読んで全体をつかもう", [("キーワード：新入社員、お金、会社、仕事、感覚　→　テーマは、新入社員の仕事？", "Keywords → theme.")]),
   items("ステップ2　問いを見て本文から答えを探そう", [
    ("1）「指示語」に注目する：「会社としては、①そういう感覚でいるわけです。」①そういう感覚は、「指示語＋N（名詞）」の形。", "指示語 + Noun."),
    ("2）何を指すか見る：そういう感覚でいる　＝　「そう感じている」　→　「そう言っている」？", "感覚 = feeling → what the writer says."),
    ("私は新入社員によく[[こう]]言うんです。→「君たちはお金をもらって…授業料、持ってこい」←①そういう感覚", "こう points forward to the quote; そういう points back to it."),
    ("①そういう感覚＝新入社員は会社で仕事を教えてもらっているのに給料をもらうなんて話が逆だ。新入社員は会社に授業料を払えと感じている感覚", "Answer."),
   ]),
   items("ステップ3　選択肢と比べよう", [T("4：正解")]),
  ]},

  text("Ippo 指示語 practice. Ovvoru passage-layum: (1) underlined 指示語 irukkira sentence-a padinga, (2) munnaadi sentence-la adhu point pannra words thedunga, (3) answer-a 指示語 edathula pottu meaning sariyaa-nu check pannunga.", "🎓 練習21～24"),

  passage("練習21　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "物理学者でもあり、科学者の社会的責任などについて{活発|かっぱつ}に{発言|はつげん}している{池内了|いけうちさとる}さんは、「便利さとは、自分自身の中にある能力を失うこと」と述べています。（中略）",
   "道具やエネルギーに多くを{依存|いそん}していると、これらが使えない状況になったときにとても困ることは、経験した人はもちろん、そうでない人も容易に想像できるでしょう。",
   "自動はたしかに便利です。ただし、どの部分を「自動化」し、どの部分を、わたしたちの{内的|ないてき}能力を高めることで処理していくか、わたしたち自身が考えて決めていく必要があります。便利さをどんどん取り入れていくことは、最初は「よい面」がよく見え、あたかも「よい面」しかないように思えます。しかし、①[[それ]]はほんの一面に過ぎません。わたしたちは、「便利」や「自動」を受け入れるときには、それによって現れるかもしれない「悪い面」も予測できなければならないと思います。便利を受け入れる「実力」を身につける必要があるのです。",
  ], [
   "Para 1: 物理学者(ぶつりがくしゃ) = physicist. 責任(せきにん) = responsibility. 発言(はつげん) = speak out. 'Convenience = losing the ability inside yourself.'",
   "Para 2: 依存(いそん) = depend on. 容易(ようい)に = easily.",
   "Para 3: 内的(ないてき)能力 = inner ability. 処理(しょり) = handle. あたかも～ように = as if. ほんの一面に過ぎない = only one side. 予測(よそく) = predict. それ comes right after 'あたかも「よい面」しかないように思えます' → それ = よい面.",
  ], src="佐倉統、古田ゆかり『おはようからおやすみまでの科学』筑摩書房"),
  toi("d6d-r21", "①それは何を指しているか。", [
   "自動化すること",
   "便利さをどんどん取り入れること",
   "よい面",
   "悪い面"], 2,
   ["Answer 3. しかし、それはほんの一面に過ぎません — the sentence before: 'あたかも「よい面」しかないように思えます'. 'よい面 is only one side' ✓.",
    "2: 便利さを取り入れること is not '一面'. 4: 悪い面 comes after."]),
  kaisetsu(21, ["便利さを取り入れることについて書かれた文章である。",
   "指示語を含む文の「しかし」とその前の「あたかも「よい面」しかないように思えます」に注目する。",
   "①それ＝よい面", "3：正解"]),

  passage("練習22　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "音楽にしろ、美術にしろ、演劇にしろ、それを好んで{鑑賞|かんしょう}する人々の{内面|ないめん}には、それぞれの表現手法に{憧|あこが}れる気持ちがあるんだろうと思います。できることなら、自分も同じようにやってみたい。けれどもふつうの人は、自分で表現できるほどの技術はないし、そのための訓練も積んでいませんから、プロのように歌ったり{描|か}いたりすることはできません。試しにやってみても、自分で{思|おも}い{描|えが}いていたような歌や絵にはならないでしょう。",
   "そこで、人々の芸術{欲|よく}を満たす代理人の役割を果たしてくれるのが、プロのアーティストたちです。",
   "彼らの作品を鑑賞することで、私たちは、あたかも自分が何かを表現したような気分になれる。スポーツ（これも広い意味の{芸術|アート}に含めていいでしょう）を見ているときの気持ちを思い出してみれば、①[[そういう面]]があるのは明らかです。",
  ], [
   "Para 1: 美術(びじゅつ) = fine art. 演劇(えんげき) = theatre. 鑑賞(かんしょう) = appreciate. 内面(ないめん) = inner self. 憧(あこが)れる = long for. 訓練(くんれん)を積む = train. 思い描(えが)く = imagine. Theme: we wish we could do it too, but can't.",
   "Para 2: 芸術欲(げいじゅつよく) = desire for art. 満(み)たす = satisfy. 代理人(だいりにん) = substitute, agent. 役割を果たす = play a role.",
   "Para 3: あたかも～ような気分 = feel as if. Sports paakkumbodhu naamae vilaiyaadina maadhiri feel. そういう面 = the sentence right before.",
  ], src="林望『「芸術力」の磨きかた　鑑賞、そして自己表現へ』PHP研究所"),
  toi("d6d-r22", "①そういう面とは何を指しているか。", [
   "自分の好きな音楽や美術や演劇など、それぞれの表現手法に憧れること",
   "プロと同じようにやってみるが、自分が思い描いていたようなものにならないこと",
   "プロの作品を鑑賞することで自分が何かを表現したような満足感を得ること",
   "スポーツを見て、自分もまるで選手と同じように興奮した気持ちになること"], 2,
   ["Answer 3. そういう面 = あたかも自分が何かを表現したような気分になれる面 (the sentence just before).",
    "4: sports is only the example used to show it; the 面 itself is 'feel as if you expressed something'."]),
  kaisetsu(22, ["芸術作品を鑑賞することについて書かれた文章である。",
   "①そういう面＝あたかも自分が何かを表現したような気分になれる面。", "3：正解"]),

  passage("練習23　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "{文句|もんく}を言うことはとても大切です。{文句|もんく}を言う力をつけることも必要です。",
   "ただ、いまは、言う「力」そのものが若い人から{奪|うば}われている。なぜか。{文句|もんく}を言うことで、言った人自身が{損|そん}をしてしまうと思わざるを得なくなっているからです。言ったらもっと状況が悪くなる。職場で{疎|うと}んじられて、クビを切られるかもしれない。{藪蛇|やぶへび}（注1）だろう、ってことなんです。",
   "さらには①[[そんな{損得勘定|そんとくかんじょう}]]以前に、「なにか言ったって、どうせどうにもならないよ」という空気が社会全体を{覆|おお}っている。",
  ], [
   "（注1）{藪蛇|やぶへび}：よけいなことをして、かえって自分にとって悪い結果になること",
   "Para 1: 文句(もんく)を言う = complain.",
   "Para 2: 奪(うば)われる = be taken away. 損(そん)をする = lose out. ～ざるを得(え)ない = can't help ～. 疎(うと)んじられる = be shunned. クビを切られる = be fired. 'Complain panna, naama dhaan loss aaguvom' — so young people stay quiet.",
   "Para 3: 損得勘定(そんとくかんじょう) = calculating profit and loss. 覆(おお)う = cover. そんな損得勘定 = 'will complaining make me lose or gain?' from Para 2.",
  ], src="湯浅誠『どんとこい、貧困！』イースト・プレス"),
  toi("d6d-r23", "①そんな損得勘定とは、何を指しているか。", [
   "文句を言うことが、自分にとって得になるかどうか考えること",
   "文句を言う力をつけることが、自分にとって得になるかどうか考えること",
   "クビを切られることが、自分にとって得になるように変えようとすること",
   "自分が損をしていると思われる状況を、得になるように変えようとすること"], 0,
   ["Answer 1. 損得勘定 = thinking whether 文句を言うこと will make you lose (損) — 言ったらもっと状況が悪くなる, クビを切られるかもしれない.",
    "2: the calculation is about saying it, not about building the power. 3, 4: not about changing anything."]),
  kaisetsu(23, ["文句を言うことについて書かれた文章である。",
   "①そんな損得勘定＝文句を言うことで、言った人自身が損をしてしまうかどうか考えること（言ったらもっと状況が悪くなる。職場で疎んじられて、クビを切られるかもしれない）",
   "1：正解"]),

  passage("練習24　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "日本では、経済のことを「知っている」人が経済の専門家である。医学の知識のある人が医師。法律の知識のある人が法律の専門家。つまり学問をその対象によって分類している。これが変だということは、少し考えたら、わかるはずである。",
   "料理には{包丁|ほうちょう}を使う。{包丁|ほうちょう}の使い方、{研|と}ぎ方、選び方には、共通の{原則|げんそく}があるはずである。学問ではそれを方法論という。{包丁|ほうちょう}をどう{扱|あつか}うか。学ばなくてはならないのは、それである。経済学を学ぶのではない。経済の取り扱い方を学ぶ。それは{女房|にょうぼう}の扱い方を学ぶのと、同じか違うか。同じかもしれないし、違うかもしれない。",
   "大学では①[[そういうこと]]を教えなくてはいけない。私はそう思うが、そうではなくて、医学を教えたり、経済学を教えたり、{法学|ほうがく}を教えたりする。これでは役に立たなくて当然である。",
  ], [
   "Para 1: 専門家(せんもんか) = expert. 医師(いし) = doctor. 学問(がくもん) = academic study. 対象(たいしょう) = subject, object. 分類(ぶんるい) = classify. Japan-la subject-a vechu dhaan study-a pirikkiraanga — writer: 'idhu weird.'",
   "Para 2: 包丁(ほうちょう) = kitchen knife. 研(と)ぎ方 = way of sharpening. 原則(げんそく) = principle. 方法論(ほうほうろん) = methodology. 扱(あつか)う = handle. 女房(にょうぼう) = wife (humour). Knife = comparison (比喩) for 'how to handle things'.",
   "Para 3: そういうこと = 方法論 = 対象の取り扱い方 (how to handle the subject), not the expert knowledge itself.",
  ], src="養老孟司『まともな人』中央公論新社"),
  toi("d6d-r24", "①そういうことは何を指しているか。", [
   "包丁の研ぎ方、選び方",
   "対象の取り扱い方",
   "女房の取り扱い方",
   "専門の知識"], 1,
   ["Answer 2. そういうこと = 方法論 = 対象の取り扱い方. Universities should teach how to handle the subject, not just the subject knowledge.",
    "1: the knife is a comparison. 3: 女房 = a humorous example of an 対象. 4: the opposite of the writer's point."]),
  kaisetsu(24, ["大学で学ぶことについて書かれた文章である。",
   "①そういうこと＝方法論（＝対象の取り扱い方）",
   "大学で教えるべきなのは専門の知識ではなく対象の取り扱い方だというのが筆者の主張。",
   "1：包丁の研ぎ方、選び方は方法論を説明するための比喩。", "2：正解",
   "3：女房はユーモアを込めて出した、対象の例。", "4：専門の知識ではなく、対象の取り扱い方を教えるべき。"]),
 ],
}
