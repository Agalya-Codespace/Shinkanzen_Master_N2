from _h import *
DAY = 18

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

def goi(imp, rel=None):
    rows = [("重要{語|ご}い：" + imp, "Key words for solving the question.")]
    if rel: rows.append(("関連{語|ご}い：" + rel, "Related words."))
    return items("{語|ご}いリスト", rows)

BLOCKS = [
  text("◆統合理解は、あるテーマについて書かれた二つ以上の文章を読んで、それらを比較・統合しながら理解できるかを問う問題である。第1部の「評論・解説・エッセイなど」、第2部の「広告・お知らせ・説明書きなど」のどちらのタイプの文章も出題される可能性がある。\n統合理解の問題は、問題文の中に大事な情報がある。必ずチェックしよう。\n例　問題12　次の文章は、相談者Aからの相談と、それに対するBとCからの回答である。三つの文章を読んで、後の問いに対する答えとして…（←問題文）\n　相談者：A　私の彼のことで相談したいことがあります。…（←本文A）\n　回答者：B　あなたの悩みは…（←本文B）\n　回答者：C　一人で考えていると…（←本文C）\n　26　相談者Aの相談に対するB、Cの回答について、正しいものはどれか。（←問い）\nこれは、相談者Aの文章から相談内容をつかみ、回答者B、Cの考えを読み取る問題である。\n◆問いに答えるために、次の手順で考えよう\n・問題文から、複数の本文（本文A、本文B、…）がそれぞれどのような文章かを知る。\n・問いを読み、読み取るべきことを知る。\n・本文を読む。\n　＊必要な情報がどの本文にあるか\n　＊複数の本文の関係はどうなっているか　共通している点は何か　違いはどこにあるか　などに注目する。",
   "3. 統合理解",
   ["Sensei: 統合理解 = JLPT 読解 問題11. You get two (or three) short texts on ONE theme — two opinions, a question and answers, or a chain of emails — and you must compare (比較) or combine (統合) them.",
    "Two kinds of question: ① 統合 = put A's info and B's info together to get the full picture (e.g. 'what kind of concert was it?'). ② 比較 = how are A and B the same / different (e.g. 'A says keep it, B says change it').",
    "Thanglish: Rendu text-um oru topic dhaan. First 問題文 paarunga — A yaaru, B yaaru. Then question padinga — 'rendu perum enna solraanga?' Apram dhaan text. A-kku + / −, B-kku + / − nu side-la note podunga."]),

  # ---------------- 例題30 ----------------
  passage("☆例題30　次のAとBは、同じコンサートについて書かれた文章である。AとBの両方を読んで、後の問いに対する答えとして最もよいものを一つ選びなさい。", [
   "【A】このコンサートはとてもありがたいです。小さい子供と一緒に行ってもいいコンサートは、なかなかありません。子供が小さいうちはコンサートに行くのは無理だと、今まであきらめていました。今回、久しぶりに生の音楽が聞けて、とても幸せな時間が過ごせました。親だけでなく子供にとっても{貴重|きちょう}な機会でした。無料なのもありがたいです。是非これからも続けてくださいますように。演奏の途中で子供が泣いて、隣の席の人ににらまれてしまいましたが、赤ちゃんが泣くのはしかたがありません。泣き声が気になる方は、有料のコンサートへ行けばいいのではないでしょうか。周囲の人々が子供のことをもっと理解してくだされればと思います。",
   "【B】このような平日昼間のコンサートは非常にうれしい。ただ、そのやりかたを考え直してはどうだろう。せっかく一流の演奏者が演奏しているのに、会場が子供の声でうるさくては、音楽に集中できない。たとえ無料のコンサートであっても、会場の客はもちろん、演奏者に対しても失礼だ。「子供連れ可」というのは、子供が泣いても騒いでもいいということなのか。それなら「子供とその親に限る」コンサートにするべきだ。そうではなく今の形を続けるなら、騒がしくならない対策が必要である。例えば、子供連れの人々の席を出入り口の近くに作り、子供が騒いだときなどに会場を出やすくしてはどうだろう。演奏する人も聞いている人も音楽に集中できる環境を作っていただきたい。",
  ], ["A = a parent: 'Thank you! A free concert I can bring my little child to. Please keep it going. If crying bothers you, go to a paid concert.' → プラス評価.",
      "B = another listener: 'Weekday daytime concerts are great, BUT rethink the way it's run. Kids' noise makes it hard to focus. Either make it kids-and-parents only, or put families near the exits.' → 批判と提案.",
      "Thanglish: A = 'super, continue pannunga!'; B = 'nalla idea, aana konjam maathunga'. Rendu perum concert-a pidikkum, aana opinion vera."]),
  toi("d18d-e30-1", "問1　このコンサートは、どのようなコンサートだったか。", ["小さい子供に音楽教育をするコンサート","小さい子供が生の音楽を演奏するコンサート","小さい子供を連れて入場できるコンサート","小さい子供とその親しか入場できないコンサート"], 2,
   ["Answer 3 (book). 統合 question: put A and B's facts together. A: 小さい子供と一緒に行ってもいい・無料. B: 平日昼間・一流の演奏者が演奏・子供連れ可.",
    "1: music education isn't mentioned. 2: children don't perform. 4: 'kids and parents only' is B's PROPOSAL, not what the concert was."]),
  toi("d18d-e30-2", "問2　コンサートに対するAとBの意見について、正しいものはどれか。", ["AもBも、コンサートを今の方法で続けてほしいと言っている。","AもBも、コンサートの方法を変えればもっと良くなると言っている。","Aは今の方法で続けてほしいと言い、Bは方法を変えてほしいと言っている。","Bは今の方法で続けてほしいと言い、Aは方法を変えてほしいと言っている。"], 2,
   ["Answer 3 (book). 比較 question. A: 「…ありがたいです」「幸せな時間が過ごせました」「貴重な機会でした」 → プラス評価. B: 「やりかたを考え直してはどうだろう」「会場が子供の声でうるさくては…できない」「…対策が必要である」「…てはどうだろう」 → 批判と提案.",
    "1: B criticises the concert. 2: A says the current concert is fine. 4: A and B are reversed."]),
  {"type": "reveal", "label": "本の解説：例題30", "children": [
   items("どのような文章か", [T("AとBは同じコンサートについて書かれた文章である。")]),
   items("問1に答える　ABの情報を統合する問題（AとBの情報を合わせる）", [
    T("ABから、このコンサートの情報を読み取る。\nA：「小さい子供と一緒に行ってもいい」「無料」\nB：「平日昼間」「一流の演奏者が演奏」「子供連れ可」"),
    T("1：音楽教育をするとは書かれていない。\n2：子供が演奏するとは書かれていない。\n3：正解\n4：子供とその親に限るというのはBの提案で、このコンサートのことではない。"),
   ]),
   items("問2に答える　ABの情報を比較する問題（AとBの筆者の考えを読み取る）", [
    T("コンサートに対する意見を探す。\nA：「…ありがたいです」「幸せな時間が過ごせました」「貴重な機会でした」←プラス評価\nB：「やりかたを考え直してはどうだろう」「会場が子供の声でうるさくては…できない」「…対策が必要である」「…てはどうだろう」←批判と提案"),
    T("1：Bはコンサートを批判している。\n2：Aは今のコンサートがいいと言っている。\n3：正解\n4：AとBが反対になっている。"),
   ]),
  ]},
  goi("{貴重|きちょう}（な） valuable・にらむ glare at・{周囲|しゅうい} surroundings・平日 weekday・昼間 daytime・一流 first-class・集中 concentrate・失礼 rude・騒ぐ make noise・～に限る limited to・対策 measure・出入り口 entrance/exit・環境 environment"),

  # ---------------- 例題31 ----------------
  passage("☆例題31　次のAとBは、第一営業部坂田さんが第一営業部全員に宛てて出したメールである。AとBの両方を読んで、後の問いに対する答えとして最もよいものを一つ選びなさい。", [
   "【A】件名：第一営業部定例会議について\n第一営業部各位\n第一営業部定例会議について\n以下のように第一営業部定例会議を行いますので、ご出席くださいますようお願いいたします。資料配布の必要がある方は、6月1日までに、坂田まで原稿をお送りください。当日お持ちになる場合は30部コピーしてお持ちください。やむを得ず欠席される方は、部長に許可を得た後、6月6日までにご連絡ください。\n尚、開催場所は9階、第3会議室となっておりますので、お間違いのないようによろしくお願いいたします。\n日時　平成24年6月8日（{金|きん}）10:00～11:30\n場所　9階　第3会議室\n第一営業部　坂田歩（asakata@eigyo_1.xxx.co.jp）",
   "【B】件名：第一営業部定例会議について【変更】\n第一営業部各位\n第一営業部定例会議について【変更】\n昨日、第一営業部定例会議についてお知らせしましたが、ICプロジェクトについての報告会も兼ねて、第二営業部と合同で行うことになりました。\nつきましては、時間と場所が変更になりましたので、ご連絡いたします。\n配布資料の原稿送付、及び欠席連絡の期限については変更ありません。当日配布資料をお持ちになる方は50部準備してください。\nよろしくお願いいたします。\n第一営業部・第二営業部合同会議\n日時　平成24年6月8日（{金|きん}）15:00～16:30\n場所　10階　第1会議室\n第一営業部　坂田歩（asakata@eigyo_1.xxx.co.jp）",
  ], ["A = the first notice of the regular meeting. B = the CHANGE notice. 件名 tells you: 【変更】!",
      "各位(かくい) = to all. 定例会議(ていれいかいぎ) = regular meeting. 資料配布(しりょうはいふ) = handing out materials. 原稿(げんこう) = draft. やむを得ず(やむをえず) = unavoidably. 欠席(けっせき) = absence. 尚(なお) = also. 兼ねて(かねて) = combined with. 合同(ごうどう) = joint. つきましては = accordingly. 及び(および) = and. 期限(きげん) = deadline.",
      "Thanglish: Office email rendu. Second one 'change' nu solludhu — time and room maaridhu, aana deadline maaraadhu. Exam-la idhu dhaan trick."]),
  toi("d18d-e31-1", "問1　6月8日に行われる会議は次のうちどれか。", ["10時から第3会議室で行われる第一営業部の定例会議","15時から第1会議室で行われるICプロジェクトの報告会","10時から第3会議室で行われる第一営業部・第二営業部合同会議","15時から第1会議室で行われる第一営業部・第二営業部合同会議"], 3,
   ["Answer 4 (book). 比較 question: find what changed. B: 第一営業部・第二営業部合同会議, 15:00～16:30, 10階 第1会議室.",
    "1: the regular meeting became a joint meeting and the time and place changed. 2: it's not ONLY the IC project report (報告会も兼ねて). 3: not 10:00 / room 3."]),
  toi("d18d-e31-2", "問2　配布資料の原稿を坂田さんに送る期限はいつか。", ["6月1日","6月6日","6月7日","6月8日"], 0,
   ["Answer 1 (book). A: 資料配布の必要がある方は、6月1日までに、坂田まで原稿をお送りください。 B: 配布資料の原稿送付、及び欠席連絡の期限については変更ありません。 → still 6月1日.",
    "Trap: 6月6日 is the deadline for absence notices, not for the draft."]),
  {"type": "reveal", "label": "本の解説：例題31", "children": [
   items("どのような文章か", [T("AとBは会議についての社内メール")]),
   items("問1に答える　ABを比較する問題（AとBの情報の違いを読み取る）", [
    T("件名に注目する。\nA「第一営業部定例会議について」＝会議についてのお知らせ\nB「第一営業部定例会議について【変更】」＝会議変更のお知らせ\n会議がどのように変更されたかを探す。"),
    T("A：「第一営業部定例会議」「平成24年6月8日（{金|きん}）10:00～11:30」「9階　第3会議室」\nB：「第一営業部・第二営業部合同会議」「平成24年6月8日（{金|きん}）15:00～16:30」「10階　第1会議室」"),
    T("1：第一営業部の定例会議は合同会議となり、時間と場所が変更された。\n2：ICプロジェクトの報告会だけではない。\n3：10時から、第3会議室で行われるのではない。\n4：正解"),
   ]),
   items("問2に答える　ABを比較する問題（AとBの情報の違いを読み取る）", [
    T("配布資料の原稿提出期限がどのように変更されたかを探す。\nA：「資料配布の必要がある方は、6月1日までに、坂田まで原稿をお送りください。」\nB：「配布資料の原稿送付、及び欠席連絡の期限については変更ありません。」"),
    T("1：正解"),
   ]),
  ]},
  goi("定例会議 regular meeting・各位 to all・資料 materials・配布 distribution・原稿 draft・やむを得ず unavoidably・欠席 absence・許可 permission・尚 also・開催 holding・兼ねる combine・合同 joint・つきましては accordingly・送付 sending・及び and・期限 deadline"),

  # ---------------- 練習62 ----------------
  passage("練習62　次のAとBは、ともに朝の読書（{朝読|あさどく}）について書かれた文章である。AとBの両方を読んで、後の問いに対する答えとして最もよいものを一つ選びなさい。", [
   "【A】27日から秋の読書週間が始まったが、朝の読書（{朝読|あさどく}）を学校の活動に取り入れている小・中・高校が全国で2万6732校にのぼり、全体の72％を占めていることが、朝の読書推進協議会（大塚笑子理事長）の調査で分かった。朝に本を読むと落ち着いた気持ちで一日のスタートが切れるなど、効果を実感する声も広がっているという。",
   "　{朝読|あさどく}は「毎日やる」「みんなでやる」「好きな本でよい」「ただ読むだけ」が4原則。1988年に千葉県の2人の教師が始めたのがきっかけだった。同協議会は本の取次会社トーハンの協力で97年から実施率などを調べており、10月25日現在で小学校と中学校はそれぞれ76％、高校は42％で{朝読|あさどく}をしていた。（朝日新聞2010年10月28日）",
   "【B】本校では、2002年から{朝読|あさどく}を始めました。毎朝授業の前に、生徒は、床に座るなどいろいろな姿勢で読書をしていますが、どんな姿勢でも静かに好きな本が読めれば、それでいいと考えています。",
   "　「基礎学力となる“読む力”をつけよう」という目標で始めた活動ですが、始めてみると、教室が落ち着いたことに驚きました。遅刻も少なくなり、毎朝いい雰囲気で一日を始められるようになりました。",
   "　今では生徒の中から「図書室の本をもっと増やそう」という声も上がっています。一番の効果は、学校全体の雰囲気が良くなったことだと言えるかもしれません。",
  ], ["A = a newspaper article: survey numbers (2万6732校, 72%, 76%, 42%), the 4 rules, the history (1988, two teachers in Chiba).",
      "B = a report from one school that does {朝読|あさどく}: started 2002, any posture is OK, the class calmed down, fewer late arrivals, the best effect = the whole school's atmosphere improved.",
      "推進協議会(すいしんきょうぎかい) = promotion council. 占める(しめる) = account for. 原則(げんそく) = principle. 取次会社(とりつぎがいしゃ) = book distributor. 実施率(じっしりつ) = rate of implementation. 姿勢(しせい) = posture. 基礎学力(きそがくりょく) = basic academic ability. 遅刻(ちこく) = being late."]),
  toi("d18d-p62-1", "問1　「{朝読|あさどく}」についての説明で、最も適切なものはどれか。", ["授業が始まる前の時間に本を読むという活動で、二人の教師が始めた。","「基礎学力となる“読む力”をつけよう」という活動で、2002年に始まった。","秋の読書週間に毎年行われる活動で、年々取り入れる学校が増えている。","毎朝本を読むという活動で、いろいろな姿勢で読むことをすすめている。"], 0,
   ["Answer 1. 統合: A says two teachers in Chiba started it (1988); B says it's done before class every morning (毎朝授業の前に).",
    "2: 2002 is when ONE school (B) started. 3: it isn't only during reading week. 4: B says any posture is fine, but doesn't recommend it."]),
  toi("d18d-p62-2", "問2　「{朝読|あさどく}」について、AとBにはどのような内容が書かれているか。", ["AもBも、{朝読|あさどく}に関する調査結果を報告している。","AもBも、{朝読|あさどく}の効果を紹介して感想を述べている。","Aは{朝読|あさどく}に関する調査結果を報告し、Bは{朝読|あさどく}の効果と感想を述べている。","Aは{朝読|あさどく}の効果と感想を述べ、Bは{朝読|あさどく}に関する調査結果を報告している。"], 2,
   ["Answer 3. A uses numbers and percentages → a survey report. B describes effects in para 2 and says 「考えています」 → effects and impressions."]),
  kaisetsu(62, [
   "A　{朝読|あさどく}についての新聞記事　　B　{朝読|あさどく}を実施している学校からの報告",
   "問1　AとBの情報を統合する問題。{朝読|あさどく}の説明に注目して本文を読む。{朝読|あさどく}とは何かについての説明とそれ以外の説明を区別する。\n1：正解\n2：2002年に始まったのは、ある学校での{朝読|あさどく}である。\n3：読書週間だけの活動ではない。\n4：Bはどのような姿勢で読んでも構わないと言っているが、すすめているわけではない。",
   "問2　AとBの情報を比較する問題。調査結果を報告しているか、{朝読|あさどく}を実施した効果と感想を述べているかを見る。Aは数字や割合を出していることから調査結果を報告した文章であるとわかる。Bは第2段落で効果を述べている。「考えています」などと書かれていることから、感想を述べた文章であることがわかる。\n3：正解",
  ]),
  goi("{朝読|あさどく} morning reading・推進 promotion・協議会 council・調査 survey・占める account for・実感 real feeling・原則 principle・実施率 rate of implementation・姿勢 posture・基礎学力 basic ability・遅刻 lateness・雰囲気 atmosphere"),

  # ---------------- 練習63 ----------------
  passage("練習63　次のAとBは、それぞれ「ほめる」ことをテーマにした本の一部である。AとBの両方を読んで、後の問いに対する答えとして最もよいものを一つ選びなさい。", [
   "【A】「ホメ言葉って、本当に効果的なのかな？」\nと{懐疑的|かいぎてき}な読者がいらっしゃるかもしれません。（中略）",
   "　たしかに人によっては、せっかくホメてあげても、「いやぁ、ホメすぎですよ」「そんなことないですよ」「うぬぼれちゃいますから、もう{勘弁|かんべん}してくださいよ」と軽く流してしまう人がいないわけではありません。",
   "　このように流されてしまうと、私たちは、「あれっ、ホメないほうがよかったのかな？」と心配になってしまいますが、そんなことはないのです。相手は、もう間違いなく喜んでおりますから、やめることなく、これからもどんどんホメてあげてください。",
   "　ホメ言葉というのは、ジワジワと効いてくる{麻酔|ますい}のような性質を持っていて、「私は、ほかの人のお世辞などに影響されないぞ」という人でも、自分でも気づかないうちに影響を受けてしまうもの。**ホメ言葉は、まさに無意識的に働いて、相手の行動を変えさせてしまうほどの力を持っているのです。**\n（{内藤誼人|ないとうよしひと}『すごい！ホメ方　職場で、家庭で、恋愛で…相手を思うままに操る悪魔の心理術』廣済堂あかつき）",
   "【B】古代ローマの英雄カエサルは「人は見たいと欲するものしか見ようとしない」と言ったというが、通常、人は自分が興味関心のあることについてしか目を向けようとしない。けれども**「ほめる」という意識を持って人を観察しているうちに視野が広がっていき、これまで気がついていなかったその人の魅力や長所が見えるようになってくる。**ほかの人は見えていないその人の魅力に、自分だけが気づくといったことも可能になるのだ。",
   "　ほめることが上手な人は、それだけ人や世界の美しいところ、素敵なところを見つけ出すのがうまいということだ。つまり自分を「ほめる体質」に変えることは、人を幸せにするだけではなく、自分自身の人生を豊かで彩りあるものにすることにもつながるのだ。\n（伊東明『ほめる技術、しかる作法』PHP研究所）",
  ], ["A: praise works like a slow anaesthetic — even people who brush it off are changed by it without noticing. Keep praising! → effect on the person who IS praised (ほめられる人).",
      "B: when you look at people meaning to praise them, your view widens and you notice their charms; becoming a 'praising person' makes YOUR life richer → effect on the person who praises (ほめる人).",
      "懐疑的(かいぎてき) = sceptical. うぬぼれる = get conceited. 勘弁(かんべん)する = spare. お世辞(おせじ) = flattery. 麻酔(ますい) = anaesthetic. 欲する(ほっする) = desire. 視野(しや) = field of view. 魅力(みりょく) = charm. 長所(ちょうしょ) = strong point. 体質(たいしつ) = constitution, nature. 彩り(いろどり) = colour."]),
  toi("d18d-p63-1", "問1　AとBは「ほめること」についてどのように考えているか。", ["AもBも、ほめることは良いことだと考え、ほめることをすすめている。","Aは、ほめることを無条件にすすめているのに対し、Bは、ほめることで相手を変えなければならないと述べている。","Aは、ほめることで相手を変えなければならないと述べているのに対し、Bはほめることを無条件にすすめている。","AもBも、ほめることは良いことだが、ほめることで相手を変えなければならないと述べている。"], 0,
   ["Answer 1. Both A and B think praising is good and recommend it.",
    "2, 3, 4: Neither says you MUST change the other person by praising. A only says praise is powerful enough to change someone's behaviour."]),
  toi("d18d-p63-2", "問2　AとBは「ほめること」について、どのようなことを主張しているか。", ["Aは「ほめる人」に及ぼす効果について、Bは「ほめられる人」に及ぼす効果について述べている。","Aは「ほめられる人」に及ぼす効果について、Bは「ほめる人」に及ぼす効果について述べている。","AもBも「ほめる人」に及ぼす効果について述べている。","AもBも「ほめられる人」に及ぼす効果について述べている。"], 1,
   ["Answer 2. A: praise changes the PRAISED person's behaviour. B: praising enriches the PRAISER's own life.",
    "Thanglish: A = paaraattu vaangravanga maaruvaanga; B = paaraatturavanga life colourful aagum."]),
  kaisetsu(63, [
   "AとBはほめることについて書かれた文章。",
   "問1　AとBの情報を比較する問題。選択肢を読む。AとBが「ほめる」ことをすすめているか、ほめることで相手を変えなければならないと考えているかに注目する。\n1：正解\n2：Bには、ほめることで相手を変えなければならないとは書かれていない。\n3：Aには、ほめることで相手を変えなければならないとは書かれていない。ほめることは相手を変えるほどの力を持っていると書かれている。\n4：AにもBにもほめることで相手を変えなければならないとは書かれていない。",
   "問2　AとBの情報を比較する問題。「ほめること」が「ほめる人」への効果か、「ほめられる人」への効果かを見る。\nA　ほめ言葉は相手（ほめられる人）の行動を変えるほど効果的であると述べている。つまり、ほめられる人への効果について述べられている。\nB　ほめ言葉はほめる人自身の人生を豊かにすると述べている。つまり、ほめる人への効果について述べられている。\n1：Aは「ほめる人」への効果が書かれていない。Bは「ほめられる人」への効果が書かれていない。\n2：正解\n3：Aは「ほめる人」への効果が書かれていない。\n4：Bは「ほめられる人」への効果が書かれていない。",
  ]),
  goi("懐疑的 sceptical・うぬぼれる be conceited・勘弁 pardon・お世辞 flattery・麻酔 anaesthetic・無意識的 unconscious・欲する desire・視野 field of view・魅力 charm・長所 strong point・体質 nature・彩り colour・及ぼす exert (an effect)"),

  # ---------------- 練習64 ----------------
  passage("練習64　次の文章はマリアさんが友人の山田さんから受け取ったメールである。3通のメールを読んで、後の問いに対する答えとして、最もよいものを一つ選びなさい。", [
   "【A】件名：山田です\nマリアさん\nお久しぶりです。元気ですか。\n新しい会社に入って3か月ですね。仕事にはもう慣れましたか。\n僕もこの4月から、新しい部署に配属されました。前の仕事はデスクワークばかりで、一時は辞めようかと思ったほどでしたが、今はお客さんと話す機会も多く、とてもやりがいがあります。お客さんとのやり取りは緊張しますが、こちらの仕事のほうが僕には合っているような気がします。\n\nさて、来週なのですが、そちらに1週間出張することになりました。\n木曜日か金曜日の夜、時間が取れませんか。どちらでも構いません。\nもしよければ、食事でもどうですか。久しぶりにいろいろ話しましょう。\nでは、都合を知らせてください。\n山田",
   "【B】件名：Re: Re: 山田です\nマリアさん\n早速のお返事ありがとうございます。\nでは、木曜日にしましょう。\n以前マリアさんと一緒に行ったレストラン「アローロ」でいいですか。おいしかったので、また是非行きたいと思っていました。\n17時45分ごろ、レストランで会いましょう。予約しておきます。\n山田",
   "【C】件名：Re: Re: Re: Re: 山田です\nマリアさん\nレストランに電話をしましたが、予約がいっぱいで取れませんでした。最近の東京のことはよく知らないので、どこかいいレストランを予約してもらってもいいですか。\nよろしくお願いします。\n山田",
  ], ["Three emails from Yamada to Maria. A: news + 'shall we eat Thursday or Friday?' B: 'Thursday, at Arōro, 17:45, I'll book.' C: 'Arōro is full — could you book a good restaurant?'",
      "部署(ぶしょ) = department. 配属(はいぞく)される = be assigned. やりがい = worth doing. やり取り = exchange. 出張(しゅっちょう) = business trip. 構(かま)わない = doesn't matter. 都合(つごう) = convenience.",
      "Thanglish: Last email dhaan final plan — Thursday fix, aana restaurant Maria dhaan book pannanum."]),
  toi("d18d-p64-1", "問1　山田さんの最近の様子は次のうちどれか。", ["新しい会社に移った。","今までと同じ仕事をしている。","同じ会社の新しい部署に移った。","新しい部署に移ったが、辞めようと思っている。"], 2,
   ["Answer 3. A: 「僕もこの4月から、新しい部署に配属されました。」",
    "1: It's Maria who joined a new company. 2: his job changed. 4: he wanted to quit the OLD job; now he finds it rewarding."]),
  toi("d18d-p64-2", "問2　マリアさんがすることは何か。", ["木曜日の17時45分頃アローロに行く。","金曜日に空いているレストランを探して予約し、山田さんに知らせる。","山田さんが金曜日のレストランの予約をしてくれるので、連絡を待つ。","いいレストランを探して、木曜日の予約をし、山田さんに知らせる。"], 3,
   ["Answer 4. 統合 A+B+C: B fixes Thursday; C says Arōro is full and asks Maria to book somewhere good.",
    "1: not Arōro. 2: not Friday. 3: not Friday, and Yamada isn't booking."]),
  kaisetsu(64, [
   "AとBとCはすべて、山田さんからマリアさんへのメールの文章である。",
   "問1　AとBとCから山田さんの最近の様子が書かれている部分を探す。\nA「僕もこの4月から、新しい部署に配属されました。」\n1：新しい会社に移ったのではない。\n2：今までと同じ仕事ではない。\n3：正解\n4：今の仕事を辞めようとは思っていない。",
   "問2　AとBとCの内容を統合して、最終的に曜日、場所、だれがレストランを予約するかを読み取る。\nB「では、木曜日にしましょう。以前…行ったレストラン「アローロ」でいいですか。…予約しておきます。」\nC「予約がいっぱいで取れませんでした。…どこかいいレストランを予約してもらってもいいですか。」\n1：アローロに行くのではない。\n2：金曜日ではない。\n3：金曜日ではない。予約するのは山田さんではない。\n4：正解",
  ]),
  goi("部署 department・配属 assignment・一時 for a while・やりがい sense of worth・やり取り exchange・緊張 nervousness・出張 business trip・構わない don't mind・都合 convenience・早速 promptly・予約 booking"),

  # ---------------- 練習65 ----------------
  passage("練習65　次のAはイダ機械工業のクォン・ヒョンスさんからトーホー部品工業の田村さんへのメールで、Bはトーホー部品工業の山田部長（田村さんの上司）からクォン・ヒョンスさんへのメールである。AとBの両方を読んで、後の問いに対する答えとして最もよいものを一つ選びなさい。", [
   "【A】日時：2012年11月10日 19:20:54\nトーホー部品工業株式会社\n田村明様\n\nいつもお世話になっております。\n早速ですが、本日（10日）17時までに納めていただく予定のEW2000-B、3000個ですが、現在19時を過ぎた時点でまだ届いておりません。\n至急ご確認いただけますでしょうか。\n当方では、取り付け作業の日程が厳しいため、遅くとも明日（11日）17時までには納品していただきたく思っています。\n\n先ほど第3営業部と田村様の携帯に何度かお電話差し上げましたが、どちらも留守番電話になっておりました。\nお忙しいところ申し訳ありませんが、至急ご確認の上、ご連絡いただきますようお願い申し上げます。\n\n株式会社イダ機械工業\n生産管理課　クォン・ヒョンス\nkwonh@idamachinex.co.jp\nTel/Fax: 111-2222-3333",
   "【B】日時：2012年11月11日 10:56:53\n株式会社イダ機械工業　生産管理課\nクォン・ヒョンス様\n\nいつもお世話になっております。\nこの度は、納期の件で大変ご迷惑をおかけしております。\n先ほど田村がお電話でお伝えしましたが、EW2000-B、3000個は本日（11日）15時までに必ずお届けいたします。すでに田村が現物を持って御社に向かいましたので、お受け取りくださいますようお願いいたします。\nその後、原因を確認いたしましたところ、運送会社への納期の連絡が不十分だったということがわかりました。私どもの不手際で、このような事態となりましたことを心からお詫び申し上げます。今後このようなことが起こらないよう万全を期す所存でございます。\n後日改めまして、お詫びに伺わせていただきます。何とぞよろしくお願い申し上げます。\n\nトーホー部品工業株式会社\n第3営業部　山田　弘\nyamadahiroshi@tohobuhinx.ne.jp\nTel/Fax: 555-6666-7777",
  ], ["A (customer → supplier): the 3000 parts due by 17:00 today haven't arrived. Please check urgently and contact me; deliver by 17:00 tomorrow at the latest.",
      "B (supplier's manager → customer): we're sorry; Tamura is bringing them, they'll arrive by 15:00 today. Cause: our notice of the delivery date to the shipping company was insufficient. Our mistake. I'll come in person to apologise.",
      "納める(おさめる)／納品(のうひん) = deliver goods. 至急(しきゅう) = urgently. 当方(とうほう) = our side. 取り付け = installation. 納期(のうき) = delivery date. 御社(おんしゃ) = your company. 運送会社(うんそうがいしゃ) = shipping company. 不手際(ふてぎわ) = mishandling. 万全を期す(ばんぜんをきす) = make every effort. 所存(しょぞん) = intention. 伺(うかが)う = visit (humble)."]),
  toi("d18d-p65-1", "問1　AとBのメールの内容として正しいのはどれか。", ["AはEW2000-Bの{納期|のうき}が遅れているので、電話するように伝えている。Bは納期が遅れたことを改めて手紙でお{詫|わ}びすると言っている。","AはEW2000-Bが届かないが、その理由を聞いている。Bはその理由がわからないことを謝っている。","AはEW2000-Bが届かないが、確認して連絡してほしいと言っている。Bは届かなかった理由を知らせ、謝っている。","AはEW2000-Bの納期について連絡がないと怒っている。Bは納期が遅れた原因を説明し、お詫びに伺うと言っている。"], 2,
   ["Answer 3. A: 至急ご確認の上、ご連絡いただきますよう… B: gives the cause (運送会社への納期の連絡が不十分) and apologises.",
    "1: A is right, but B says he'll visit (伺う), not write a letter. 2: A doesn't ask the reason; B does give the reason. 4: A's complaint is that the goods haven't arrived after the deadline, not 'no contact about the deadline'; B is correct."]),
  toi("d18d-p65-2", "問2　EW2000-Bの納期が遅れた理由は何か。", ["イダ機械工業が運送会社にEW2000-Bの納期を間違って伝えていた。","トーホー部品工業と{運送|うんそう}会社との間で納期について誤解があった。","運送会社がトーホー部品工業が指定した日にEW2000-Bを届け忘れた。","トーホー部品工業からイダ機械工業への連絡が間違っていた。"], 1,
   ["Answer 2. B: 原因を確認いたしましたところ、運送会社への納期の連絡が不十分だった… 私どもの不手際で… → a miscommunication between Tōhō and the shipping company.",
    "1: Ida didn't tell the shipper anything. 3: not 'forgot'. 4: not about Tōhō → Ida contact."]),
  kaisetsu(65, [
   "Aはクォンさんから田村さんへのメール。Bは田村さんの上司からクォンさんへのメール。",
   "問1　AとBの情報を読み取る問題\n1：A　正しい。　B　手紙ではなく、お詫びに伺うと言っている。\n2：A　理由は聞いていない。　B　理由を知らせている。\n3：正解\n4：A　納期の連絡がないのではなく、納期を過ぎても届いていないと言っている。　B　正しい。",
   "問2　AとBから納期が遅れた理由を読み取る。\nB「原因を確認いたしましたところ、運送会社への納期の連絡が不十分だったということがわかりました。私どもの不手際で、…」\n1：イダ機械工業が運送会社に納期を伝えたのではない。\n2：正解\n3：運送会社がEW2000-Bを届け忘れたとは書かれていない。\n4：トーホー部品工業とイダ機械工業の間の連絡が間違ったとは書かれていない。",
  ]),
  goi("納める deliver・至急 urgently・当方 our side・取り付け installation・日程 schedule・納品 delivery・留守番電話 answering machine・納期 delivery date・迷惑 trouble・現物 actual goods・御社 your company・運送会社 shipping company・不手際 mishandling・事態 situation・詫びる apologise・万全を期す do everything possible・所存 intention"),
]

SECTION = {
 "book": "dokkai",
 "title": "第3部　実戦問題　3. 統合理解",
 "source": "新完全マスター読解 N2 · 第3部 3. 統合理解 · pp.147–160 · 例題 answers in the book; 練習 answers from 別冊 解答 pp.26–29",
 "blocks": BLOCKS,
}
