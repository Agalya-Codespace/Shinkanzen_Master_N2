from _h import *
DAY = 2

def passage(title, paras, explain, notes=None, src=None):
    b = {"type": "passage", "title": title, "paras": paras, "explain": explain}
    if notes: b["paras"] = paras + notes
    if src: b["cite"] = "（" + src + "）"
    return b

def toi(id, q, opts, ans, explain):
    return mcq(id, "【問い】" + q, opts, ans, explain)

def kaisetsu(n, theme, taihi, choices, extra=None):
    its = [{"t": theme}, {"t": taihi}] + ([{"t": x} for x in extra] if extra else []) + [{"t": c} for c in choices]
    return {"type": "reveal", "label": "本の解説（別冊）：練習%d" % n,
            "children": [{"type": "items", "title": "解答・解説", "items": its}]}

SECTION = {
 "book": "dokkai",
 "title": "1. 文章のしくみを理解する　1）［対比］ほかのものと比べる　練習1～5",
 "source": "新完全マスター読解 N2 · 第1部 評論・解説・エッセイなど · pp.10–13 · answers from 別冊 解答 pp.2–3",
 "blocks": [
  text("Day 1-la 例題 moonu paathom. Inniki 対比 (contrast) technique-a 5 practice passage-la use pannunga. Ovvoru passage-layum: (1) A edhu, B edhu-nu kandupudinga, (2) 'しかし・それに対して・つまり' maadhiri signal words-a mark pannunga, (3) appram dhaan options paarunga.",
   "🎓 Inniki plan",
   ["Answer option-la 'passage-la sollaadha vishayam' (書かれていない) dhaan most common trap. Book-oda 解説 kooda adhaye dhaan check pannudhu."]),

  passage("練習1　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "この前、教師の人と話していて、子供がTVゲームばかりして、友達{同士|どうし}遊ばないから困っているとぼやいていました。",
   "TVゲームに対するもっとも一般的な批判です。{僕|ぼく}はいつも、この批判を聞くと、それは正しいのだけれど、だけど、先生、あなた{方|がた}だって、カラオケで盛り上がるでしょう、つまり、ゆっくり酒でも飲みはじめたら、{誰|だれ}のどんな批判が飛び出すか分からないから、その{空間|くうかん}を避けるでしょう、もちろん、{僕|ぼく}もそうですよ、スタッフや役者{同士|どうし}が{酔|よ}っぱらって{何|なに}を言いだすか分からない時は、カラオケに走るのがもっとも安全な方法ですから、と心の{中|なか}で思ってしまうのです。",
   "そして、子供は、そういう大人の生活の知恵を敏感に知っていて、友達の家に遊びに行って、{何|なに}を話そうかと緊張する瞬間、ある{者|もの}はTVゲームのスイッチを入れ、ある{者|もの}は『スラムダンク』のコミックを手に取るのですよ、と思ってしまうのです。",
  ], [
   "Para 1: 教師(きょうし) = teacher. 友達同士(ともだちどうし) = among friends. ぼやく = grumble. Teacher complain pannaanga: 'Pasanga TV game mattum vilaiyaadraanga, friends kooda serndhu vilaiyaadala.'",
   "Para 2: 批判(ひはん) = criticism. Writer manasukulla: 'Aanaa sir, neenga kooda (大人) kudikka aarambichaa yaar enna criticise pannuvaanga-nu theriyaadhu, adhanaala karaoke-ku odureenga — andha awkward 空間(くうかん, space)-a avoid panna.' 盛(も)り上(あ)がる = get lively. 酔(よ)っぱらう = get drunk.",
   "Para 3: 知恵(ちえ) = wisdom. 敏感(びんかん)に = sensitively. 緊張(きんちょう) = tension. 瞬間(しゅんかん) = moment. Kids-um adhe maadhiri: friend veetla 'enna pesradhu?'-nu tension aagum podhu, game switch on pannuvaanga or comic eduppaanga.",
   "対比: 大人 (karaoke) ↔ 子供 (TV game). Rendum oru reason-ku dhaan: tension/awkwardness-a avoid panna.",
  ], src="鴻上尚史『真実の言葉はいつも短い』光文社"),
  toi("d2d-r1", "この文章の内容として最も適切なものはどれか。", [
   "子供がTVゲームをするのは、まだ子供たちだけでカラオケに行けないからだ。",
   "子供がTVゲームをするのは緊張を避けるためで、大人がカラオケに行くのと同じだ。",
   "子供がTVゲームをすることを批判するなら、大人もカラオケに行くべきではない。",
   "子供がTVゲームをするのは、カラオケほど他人から批判されず、安全だからだ。"], 1,
   ["Answer 2. Kids game pannradhu tension avoid panna — periyavanga karaoke pogra maadhiri dhaan.",
    "1: kids karaoke poga mudiyaadhu-nu passage sollala. 3: 'periyavanga karaoke poga koodaadhu'-nu ezhudhala. 4: kids karaoke pogradhu pathi ezhudhave illa."]),
  kaisetsu(1, "子供がテレビゲームをする理由について書かれた文章である。",
   "対比（子供と大人）に注目する。緊張を避けるために、大人はカラオケに行き、子供はテレビゲームをする。",
   ["1：子供の友達同士でカラオケに行けないからではない。", "2：正解", "3：大人もカラオケに行くべきではないとは書かれていない。", "4：子供がカラオケに行くとは書かれていない。"]),

  passage("練習2　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "現在、学校の部活動や地域の少年スポーツチーム、クラブには、参加の意志さえあれば{誰|だれ}でも参加できるようになっています。それでいて、{万が一|まんがいち}事故が起こった場合は、{現場|げんば}にいる指導者や、施設管理者だけに責任があるかのように思われています。一般に、一つの部やクラブ、チームの{部員数|ぶいんすう}が30～40人くらいになることは、それほど珍しいことではありません。しかし、それだけの{大人数|おおにんずう}の安全や健康状態を完璧に（注1）観察し、適切な判断をたったひとり、もしくは{数人|すうにん}の指導者でおこなうことは不可能に近いことです。",
  ], [
   "部活動(ぶかつどう) = school club activities. 意志(いし) = will. 万が一(まんがいち) = in the unlikely case. 指導者(しどうしゃ) = coach. 施設管理者(しせつかんりしゃ) = facility manager. 責任(せきにん) = responsibility.",
   "対比: 一般的な考え 'accident aanaa coach/manager mattum dhaan responsible' ↔ writer: '30–40 per safety-a oru-rendu coach perfect-aa paakkaradhu 不可能に近い (almost impossible).'",
   "完璧(かんぺき)に = perfectly. 観察(かんさつ) = observe. 適切(てきせつ)な判断(はんだん) = proper judgement.",
  ], notes=["（注1）完璧に：欠点が全くなく、完全に"], src="佐保豊『日本のスポーツはあぶない』小学館"),
  toi("d2d-r2", "この文章で筆者が最も言いたいことは何か。", [
   "指導者は、指導中の事故にもっと責任を持つ必要がある。",
   "部員は、指導者に自分の健康状態を報告する義務がある。",
   "自分の意志で参加しているので、事故の責任は部員本人にある。",
   "少人数の指導者や管理者で数十人の部員の安全を守ることはできない。"], 3,
   ["Answer 4. Writer-oda main point: konjam coaches-aala 30–40 members safety-a paathukka mudiyaadhu.",
    "1, 2: passage-la illa. 3: 'responsibility member-kku dhaan'-nu sollala; people think it's the coach's, that's all."]),
  kaisetsu(2, "部活動などスポーツ活動の管理について書かれた文章である。",
   "対比（一般的な考え「部活動の事故は管理者だけに責任がある」と、筆者の考え「完璧に観察し、適切な判断を…おこなうことは不可能に近い」）に注目する。筆者は、今の状況では安全管理が十分にできないと書いている。",
   ["1：指導者が事故にもっと責任を持つべきだとは書かれていない。", "2：部員に報告する義務があるとは書かれていない。",
    "3：事故の責任が部員本人にあるとは書かれていない。現場の指導者や、施設管理者に責任があるかのように思われていると書かれている。", "4：正解"]),

  passage("練習3　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "人の嫌がる仕事を進んで引き受けたり、お年寄りやハンディキャップをもつ人を的確にお世話するボランティアの姿を見ていると、「すごい。自分にはできない」と感じてしまう人は多いかもしれません。",
   "でも、こうした行動や態度は活動をしていくなかで徐々に{身|み}についていくものです。ボランティアをしているのは特別、正義感が強いやさしい人ばかりというわけではありません。",
   "ボランティアを始めた動機に「おもしろそうだから、興味があったから」と、好奇心や探求心をあげる人はたくさんいます。責任をもって活動できるなら、きっかけは{何|なん}でもいいのです。むしろ、「よいことをする！」という{気負|きお}いがない{分|ぶん}、自然体でボランティアに{関|かか}われる人も多いのです。",
  ], [
   "Para 1: 嫌(いや)がる = dislike. 引(ひ)き受(う)ける = take on. お年寄(としよ)り = elderly. 的確(てきかく)に = precisely. 'Volunteers-a paathaa, enakku mudiyaadhu-nu thonum.'",
   "Para 2: 徐々(じょじょ)に身(み)につく = gradually acquire. 正義感(せいぎかん) = sense of justice. Volunteers ellarum special nalla manushanga illa — work panna panna dhaan varum.",
   "Para 3: 動機(どうき) = motive. 好奇心(こうきしん) = curiosity. 探求心(たんきゅうしん) = spirit of inquiry. 気負(きお)い = eagerness/over-enthusiasm. 自然体(しぜんたい) = naturally. 'Responsibility irundhaa, start panna reason edhuvaanalum OK.'",
   "対比: 一般的なイメージ (special, kind people) ↔ 筆者 (anyone with responsibility).",
  ], src="大勝文仁、山田由佳『自分スタイルのボランティアを見つける本』山と溪谷社"),
  toi("d2d-r3", "この文章で筆者が最も言いたいことは何か。", [
   "特別な人でなくても、責任感さえあれば、誰でもボランティア活動はできる。",
   "お年寄りやハンディキャップをもつ人を的確に世話できる人は、ボランティア活動に向いている。",
   "正義感や責任感はなくても、もっと気軽にボランティア活動に参加してほしい。",
   "「よいことをする！」という気持ちが強くなければ、ボランティアはできない。"], 0,
   ["Answer 1. Special aal-aa irukka vendaam; 責任 irundhaa podhum.",
    "3 trap: 正義感 vendaam OK, aanaa 責任感 vendaam-nu sollala — 責任感 必要. 4: opposite."]),
  kaisetsu(3, "ボランティア活動に向いている人について書かれた文章である。",
   "対比（一般的なイメージのボランティアと筆者の考えるボランティア）に注目する。一般的なボランティアのイメージは、人の嫌がる仕事を引き受けたり、お年寄りやハンディキャップをもつ人を的確に世話したりする、正義感が強いやさしい人。筆者の考えるボランティアは、責任を持って活動できる人。",
   ["1：正解", "2：お年寄りやハンディキャップを持つ人を的確に世話する能力は、徐々に{身|み}についていくものである。", "3：責任感は必要である。",
    "4：「よいことをする！」という気持ちが強くない人のほうが、自然体でボランティアができる。"]),

  passage("練習4　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "近代以前の社会では、職業はおのずと{定|さだ}められていることが多く、選択の幅はきわめて小さかった。さらに、生まれて死ぬまで同じコミュニティ（注1）のなかで暮らす人が多かった。",
   "それに対して近代社会では、人びとは自由に職業を選択できる。また国内ならば自由に移動することもできるし、自由に起業したり、趣味やボランティアのサークルをつくって活動することもできる。",
   "つまり、近代社会では{一人|ひと}ひとりの「自由」という理念が大切にされ、さまざまな自由な活動が保証されている。そしてそれに対応して、社会の{側|がわ}も、不特定多数の人びとやモノや情報がさまざまに{行|ゆ}き{交|か}う（注2）空間となっているのである。",
  ], [
   "Para 1: 近代(きんだい)以前 = before the modern era. おのずと = naturally (automatically). 定(さだ)められる = be decided. 選択(せんたく)の幅(はば) = range of choice. Munnaadi job already fix, choice kammi, same ooru-la life.",
   "Para 2: それに対して = contrast signal! 近代社会 = free job choice, free movement, 起業(きぎょう) = start a business, 趣味(しゅみ) = hobby.",
   "Para 3: つまり = summary signal. 理念(りねん) = ideal. 保証(ほしょう) = guarantee. 不特定多数(ふとくていたすう) = many unspecified. 行(ゆ)き交(か)う = come and go.",
  ], notes=["（注1）コミュニティ：地域社会", "（注2）{行|ゆ}き{交|か}う：行ったり来たりする"], src="苅谷剛彦、西研『考えあう技術――教育と社会を哲学する』筑摩書房"),
  toi("d2d-r4", "この文章で筆者が最も言いたいことは何か。", [
   "近代以前、人はずっと移動せずに暮らしてきたが、近代以降は移動の自由を得た。",
   "近代社会では個人の自由が重視され、職業選択や移動等の活動も自由になった。",
   "近代以前は自由がなかったため、近代社会の人びとはそれを非常に大切に考えている。",
   "近代社会になって自由が保証されたが、人も情報も多すぎて社会が不安定になった。"], 1,
   ["Answer 2. 'つまり' sentence dhaan main point: individual freedom is valued, job & movement free.",
    "1: movement mattum illa — too narrow. 3: 'munnaadi freedom illaadhadhaala' reason ezhudhala. 4: 不安定 (unstable) ezhudhave illa."]),
  kaisetsu(4, "近代社会における自由について書かれた文章である。",
   "対比（近代以前の社会と近代社会）に注目する。近代以前では、職業の選択肢がほとんどなく、一生同じ地域で暮らすことが多かった。それに対し、近代では自由が大切にされ、職業選択も移動も自由になり、人やモノや情報が{行|ゆ}き{交|か}うようになったことが書かれている。",
   ["1：筆者は、移動の自由だけについて言いたいのではない。", "2：正解", "3：近代社会が自由という理念を大切にする理由は、それ以前に自由がなかったためだ、とは書かれていない。",
    "4：人も情報も多すぎて社会が不安定になるとは書かれていない。"]),

  passage("練習5　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "知名度の高い執筆者ばかり適当に揃えて{一冊|いっさつ}の雑誌をつくる編集は、たとえて言えば、インスタント食品（注1）をうまく使って食卓を賑わす料理人みたいなものだ。失敗の危険は少ないかもしれないが、{創|つく}る喜びは少ない。",
   "そこへゆくと、まだ{固|かた}いつぼみ（注2）を見つけ出して、これにあたたかい春の風を送り、花に育てる編集の仕事はそれ自体がひとつの芸術である。そういうことの可能なエディターはそれほど多くいるとは考えられないが、すぐれた才能の開花のかげにはきわめてしばしばこういう創造的編集が存在するのではあるまいか。",
  ], [
   "Para 1: 知名度(ちめいど) = fame. 執筆者(しっぴつしゃ) = writer. 揃(そろ)える = gather. 編集(へんしゅう) = editing. 食卓(しょくたく)を賑(にぎ)わす = fill the dining table. Famous writers-a mattum sethu magazine pannradhu = instant food-la samaikkira cook maadhiri — safe, aanaa create panra sandhosham illa.",
   "Para 2: そこへゆくと = in contrast. つぼみ = flower bud. Innum theriyaadha talent (固いつぼみ)-a kandupudichu, valarthu poo-vaa aakkaradhu = 芸術(げいじゅつ, art). 開花(かいか) = blooming. 創造的(そうぞうてき) = creative. ～ではあるまいか = isn't it ～? (writer's opinion).",
   "対比: famous-writer editing (safe, no joy) ↔ 創造的編集 (finding unknown talent). Kavanam: 'つぼみ→花' = 比喩 (metaphor) for new writers.",
  ], notes=["（注1）インスタント食品：ほとんど手間をかけずに簡単に食べられる食品", "（注2）つぼみ：花がまだ咲かないで閉じている状態"], src="外山滋比古『新エディターシップ』みすず書房"),
  toi("d2d-r5", "この文章で筆者が最も言いたいことは何か。", [
   "まだ有名でない執筆者の才能が花開くかげには、優秀な編集者がいる。",
   "雑誌をつくるということは、花を育てるように創造的で芸術的な仕事である。",
   "簡単につくられた雑誌より、時間をかけて編集された雑誌のほうが内容が良い。",
   "優秀な才能を持つ編集者がいれば、より良い雑誌がつくれるようになる。"], 0,
   ["Answer 1. Last sentence: talent bloom aagura pinnaadi creative editor irukkaanga.",
    "2 trap: magazine panradhu ellame art illa — 'つぼみ-a valarkkura' editing dhaan art. 3: time pathi sollala. 4: editor's own talent pathi illa."]),
  kaisetsu(5, "創造的な編集について書かれた文章である。",
   "対比（知名度の高い執筆者ばかり適当にそろえて一冊の雑誌をつくる編集と、創造的編集）に注目する。前者は、失敗は少ないが、創る喜びが少ない。",
   ["1：正解", "2：雑誌をつくること自体が創造的で芸術的な仕事だとは書かれていない。", "3：時間をかけることではなく、まだ知られていない才能を見つけ育てることが創造的編集である。", "4：雑誌をつくる編集者の才能については書かれていない。"],
   extra=["創造的編集とは、「{固|かた}いつぼみを見つけ出して、これにあたたかい春の風を送り、花に育てる編集」のこと（創造的編集＝まだ発見されていない才能を見つけ出し、励ましたりして、りっぱな書き手に育てることの比喩）。"]),
 ],
}
