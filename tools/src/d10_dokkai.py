from _h import *
DAY = 10

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
 "title": "2. 問いを解く技術を身につける　5）例を問う／第2部の読み方",
 "source": "新完全マスター読解 N2 · 第1部 評論・解説・エッセイなど · pp.68–75 · 例題 answer in the book; 練習 answers from 別冊 解答 pp.13–14",
 "blocks": [
  items("◆筆者が本文で述べていることに合う「具体的な例」を選択肢から選ぶ問題である。選択肢の内容が本文に書かれていないことに注意しよう。", [
   ("次の順番で考えよう。", "Order:"),
   ("・下線部の文や【問い】の文をよく見て、内容をつかもう。下線部がなければ、問い、及び文章全体を読んで、内容をつかもう。", "Step 1: Read the underlined part and the question. No underline? Read the question and the whole passage."),
   ("・選択肢を比べ、どれが具体例として適切か考えよう。", "Step 2: Compare the choices — which one is a good concrete example of the writer's idea?"),
  ], explain="Inniki technique: 'which is an EXAMPLE of ～?' questions. Tricky part: the choices are NOT written in the passage. Neenga writer-oda idea-vai purinjikittu, adhukku match aagura new example-ai choose pannanum."),

  passage("☆例題16　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "この先に何か{目標|もくひょう}があって、そこに向かっていくときにはモチベーション（注1）というのはどんどん高まっていくのだと思います。目標さえあれば、その目標に向かって、よし、こうしよう、ああしようとイメージを{先|さき}へ先へと進められる。成功する人はみな、{明日|あした}こうしよう、{明後日|あさって}こうしようと思った{瞬間|しゅんかん}、実は頭の中で①[[{明日|あした}、{明後日|あさって}の「こうしよう」を{一足|ひとあし}先に、{体感|たいかん}として身につけてしまっているのです]]。",
   "たとえば、まだ今日なのに、「{明日|あした}は朝から{釣|つ}りに行ってこうしよう」と思うと、もうその{時点|じてん}で頭の中では魚を釣っています。それがイメージ力なのです。つまり、まだ{明日|あした}じゃないのに情報を作ってしまってある。{明日|あした}になったらそれを{引|ひ}っ{張|ぱ}り出すだけなのです。成功する人たちというのは、だいたいそういうプラスのイメージをいつも働かせている。だから実際に目標{達成|たっせい}するのです。",
  ], [
   "（注1）モチベーション：目的に向けて行動し、続ける力",
   "目標(もくひょう) = goal. 瞬間(しゅんかん) = moment. 一足先に(ひとあしさきに) = one step ahead. 体感(たいかん) = bodily feeling. 釣り(つり) = fishing. 時点(じてん) = point in time. 達成(たっせい) = achieve.",
   "Look: 「たとえば」 starts paragraph 2 → the fishing example. In your head you are already catching fish. Find a choice that works the same way.",
  ], src="岡本正善『めげても立ちなおる心の習慣』筑摩書房"),
  toi("d10d-e16", "①{明日|あした}、{明後日|あさって}の「こうしよう」を一足先に、体感として身につけてしまっているの例として、最も適切なものはどれか。", [
   "「{明日|あした}は上手に発表しよう」と思うのをやめて、今すぐに発表の練習を始める。",
   "「{明日|あした}は上手に発表しよう」と思うだけで、実際にうまく発表している気分になる。",
   "「{明後日|あさって}は上手に発表しよう」と思うと、{明日|あした}発表したくなる。",
   "「{明後日|あさって}は上手に発表しよう」と思わなくても、だれよりもうまく発表できる。"], 1,
   ["Answer 2. Just THINKING 'tomorrow I'll present well' and you already feel you are presenting well — same as already catching fish in your head.",
    "1: the image is important, so you shouldn't stop thinking. 3: wanting to present sooner isn't written. 4: you DO need to think/imagine."]),
  {"type": "reveal", "label": "本の解説：例題16", "children": [
   items("ステップ1　本文を読んで全体をつかもう", [
    ("キーワード：目標、モチベーション、イメージ　→　テーマは、モチベーション？", "Keywords → theme."),
   ]),
   items("ステップ2　問いを見て本文から答えを探そう", [
    ("1）下線部の文を見る：「成功する人はみな、…と思った瞬間、実は…①{明日|あした}…{明後日|あさって}の…身につけて…。」", "The underlined sentence."),
    ("下線部の意味がはっきりわからなくてもいい。「成功する人」についての例を探す。", "Don't worry if the underline is hard — look for the example about successful people."),
    ("2）本文中の例を見る：第2段落のはじめ「たとえば」＝魚釣りの例", "たとえば = example marker."),
    ("魚釣りの例：「{明日|あした}は朝から釣りに行ってこうしよう」と思う　「その時点で頭の中では魚を釣っている」　→　成功する人：実際に始める前にプラスイメージを作って頭の中ではすでに成功している", "Fishing example ↔ successful people."),
   ]),
   items("ステップ3　選択肢と比べよう", [
    T("1：イメージが大切なので、思うことをやめてはいけない。"),
    T("2：正解"),
    T("3：早く発表したくなるとは書かれていない。"),
    T("4：イメージが大切なので思うことをしなければならない。"),
   ]),
   items("ポイント", [T("・本文に具体例がある場合は、それを参考にして考えよう。")]),
  ]},

  text("Ippo practice. Ovvoru 'example' question-kkum: (1) writer-oda main idea enna-nu kandupidinga; (2) passage-la たとえば example irundha adhai model-aa use pannunga; (3) choice-la writer idea-kku SAME pattern irukka-nu paarunga.", "🎓 練習39～41"),

  passage("練習39　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "運動を続けて、{体調|たいちょう}がよくなるのを{実感|じっかん}できるのは{数週間後|すうしゅうかんご}からでしょう。しかし、その{間|あいだ}にさまざまな「いいわけ」トラブルが出てきます。すると例えば、毎日続けられる{確率|かくりつ}が70%なら、{10日|とおか}連続して続けられる確率は0.7の10{乗|じょう}＝0.028、つまり2.8%。ほとんどの人は{途中|とちゅう}でくじけて（注1）しまうのです。",
   "これを防ぐには「{意志|いし}の力に頼らなくても、続けられる{仕組|しく}み（注2）を作ること」に{尽|つ}きます。運動を続けたいなら、家の場所を{最寄|もよ}りの駅から歩いて15{分|ふん}かかるところにすれば、毎日、30{分|ぷん}歩くことになります。あるいは、スポーツクラブに入るときのコツは「家か職場か、どちらかに必ず近いところにすること」と「{極力|きょくりょく}（注3）、手ぶら（注4）で行けること」、さらに「{固定|こてい}レッスンや予約などをとってスケジュールを{確保|かくほ}すること」。どんなに意志が弱い人でも、続けられるようにするのです。",
  ], [
   "（注1）くじける：がんばろうとする気持ちをなくす　（注2）{仕組|しく}み：何かがうまく進むように{工夫|くふう}された計画　（注3）{極力|きょくりょく}：できるだけ　（注4）手ぶら：手に何も持たないこと",
   "体調(たいちょう) = physical condition. 実感(じっかん) = feel for real. 確率(かくりつ) = probability. 意志(いし) = will power. ～に尽きる = it all comes down to ～. 最寄り(もより)の駅 = nearest station. 確保(かくほ) = secure.",
   "No underline → read the question and the whole text. Key idea: don't rely on will power; build a SITUATION where you have to move (house 15 minutes from the station).",
  ], src="勝間和代「人生を変えるコトバ」朝日新聞2009年5月16日"),
  toi("d10d-r39", "運動を続けられる仕組みの例として、最も適切なものはどれか。", [
   "「がんばって運動しよう！」と毎朝声に出して言う。",
   "細かく計画を立て、毎日そのとおりに運動する。",
   "運動したら、内容と時間を{手帳|てちょう}に書く。",
   "犬を{飼|か}い、犬の運動のために毎日30{分|ぷん}一緒に歩く。"], 3,
   ["Answer 4. Having a dog means you HAVE to walk 30 minutes every day — a situation that works without will power (like living 15 minutes from the station).",
    "1: shouting a promise every morning still relies on will power. 2: a plan, not a situation that forces you. 3: writing in a notebook still depends on your own will."]),
  kaisetsu(39, ["運動を続けるにはどうすればいいかについて書かれた文章である。",
   "下線部がないので、問いと文章全体を読む。運動を続けられる仕組みは、意志の力に頼らないことである。本文中の例を見ると、「家の場所を最寄りの駅から歩いて15{分|ふん}かかるところに」するなど、つまり、そうしなければならない状況を作ることである。",
   "1：毎朝声に出して言うのは、意志の力に頼っていることであり、それは否定されている。", "2：計画ではなく、やらなければならない状況を作る。",
   "3：運動した内容と時間を手帳に書くことは、自分の意志の力にかかっているので、仕組みにはなっていない。", "4：正解"]),

  passage("練習40　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "「“ことほぐ”って知ってる？」",
   "若い人三人に{尋|たず}ねてみた。",
   "一人が「知らない」と首を{振|ふ}る。二人が「お祝いすることでしょ」と答えてくれた。",
   "「じゃあ、友人の結婚を聞いてひとり静かにことほぐ、これ、正しい？」",
   "重ねて尋ねると、ジロリとにらむ。わざわざ聞かれるのは「正しくない」からだろうけれど、どこがどうちがうかわからない、そんな{心境|しんきょう}にちがいない。",
   "その通り、正しくない。“ことほぐ”は“言葉を{告|つ}げて（注1）祝う”こと。ひとり静かに{黙|だま}って祝うのは、ことほぐではない。ただ、ほとんどの場合、祝うと言えば「おめでとうございます」とか「よかったねえ」とか言葉を{発|はっ}して祝うから“ことほぐ”と“祝う”とが{同義語|どうぎご}に思われてしまうのだろう。{屁理屈|へりくつ}をこねれば、お祝いのプレゼントだって、なにかしら言葉をそえて{贈|おく}る。言葉なしでただ贈るのは、失礼、と、これが{良識|りょうしき}だろう。やっぱりことほいでいるのだ。",
  ], [
   "（注1）{告|つ}げる：言葉などで自分の考えを相手に知らせる",
   "ことほぐ(言祝ぐ/寿ぐ) = celebrate WITH WORDS. 尋ねる(たずねる) = ask. 首を振る(ふる) = shake your head. 心境(しんきょう) = state of mind. 黙って(だまって) = silently. 同義語(どうぎご) = synonym. 屁理屈をこねる(へりくつをこねる) = quibble. 良識(りょうしき) = good sense.",
   "No underline → find the definition: ことほぐ = 言葉を告げて祝う. So the right use must include SAYING words to someone.",
  ], src="阿刀田高『日本語えとせとら――ことばっておもしろい』時事通信出版局"),
  toi("d10d-r40", "筆者が考える「ことほぐ」という言葉の正しい使い方はどれか。", [
   "新年をことほぎ、ごあいさつを申し上げたいと思います。",
   "一人で酒を飲み、新年をことほぎたいと思っています。",
   "新年をことほぐため、新しい服を着ます。",
   "家にきれいな花を{飾|かざ}って、新年をことほぐつもりです。"], 0,
   ["Answer 1. ごあいさつを申し上げる = saying words of greeting to people → celebrating with words.",
    "2: drinking alone — no one to say words to. 3 & 4: wearing new clothes / decorating with flowers aren't saying words to someone."]),
  kaisetsu(40, ["「ことほぐ」という言葉について書かれた文章である。",
   "下線部がないので、問いと文章全体を読む。「ことほぐ」という言葉の正しい使い方を本文で探す。「ことほぐ」とは、言葉を告げて（相手に言葉を言って）祝うこと。言葉を相手に告げていなければ、「ことほぐ」とは言えない。",
   "1：正解", "2：一人で酒を飲むという行動には、相手がいないので、言葉を告げられない。", "3：新しい服を着ることは、言葉を相手に告げる行動ではない。", "4：花を飾ることは、言葉を相手に告げる行動ではない。"]),

  passage("練習41　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "小学校に上がるころ、ほとんどの人が聞いたり歌ったりした{記憶|きおく}があると思いますが、「一年生になったら」という歌があります。「一年生になったら、友だち{百人|ひゃくにん}できるかな」という{歌詞|かし}なのですが、あれってけっこう{強烈|きょうれつ}なメッセージですよね。小学校の一年生になったら、友だちを百人作りたい、あるいは百人友だちを作ることが{望|のぞ}ましいのだという、{暗|あん}にプレッシャー（注1）を感じた人も多いのではないでしょうか。",
   "学校というのは、とにかく「みんな{仲良|なかよ}く」で、「いつも心が{触|ふ}れ合って、みんなで一つだ」という、まさにここで私は「{幻想|げんそう}（注2）」という言葉を使ってみたいのですが、「一年生になったら」という歌に{象徴|しょうちょう}されるような「友だち幻想」というものが強調される場所のような気がします。けれど私たちはそろそろ、①[[そうした{発想|はっそう}から{解放|かいほう}されなければならない]]と思っているのです。",
  ], [
   "（注1）プレッシャー：精神的な圧力　（注2）{幻想|げんそう}：実際にはないことをあるかのように想像すること",
   "記憶(きおく) = memory. 歌詞(かし) = lyrics. 強烈(きょうれつ) = intense. 暗に(あんに) = implicitly. 触れ合う(ふれあう) = connect. 象徴(しょうちょう) = symbolise. 解放(かいほう) = set free.",
   "そうした発想 = the 'everyone must be friends, all one' idea (友だち幻想). Free yourself from it → you don't have to be close to everyone.",
  ], src="菅野仁『友だち幻想　人と人の〈つながり〉を考える』筑摩書房"),
  toi("d10d-r41", "①そうした発想から解放されなければならないとあるが、筆者のこの考えに{従|したが}った行動の例として、最も適切なものはどれか。", [
   "クラスの仲間{同士|どうし}、お{互|たが}いのいい点を見つけ、{対立|たいりつ}が起きないようにする。",
   "一人で行動している子供がいたら、その子が仲間に入れるようみんなが努力する。",
   "どうしても気が合わない相手がいたら、無理に話をしなくてもいい。",
   "やりたくないのなら、クラス全員で決めた{掃除|そうじ}{当番|とうばん}などの仕事をしなくてもいい。"], 2,
   ["Answer 3. Free from 'everyone must be friends' → you don't have to force yourself to talk with someone you don't get along with.",
    "1 & 2: these are actions to make everyone 'one' — the very idea the writer wants to leave. 4: class rules (cleaning duty) aren't discussed at all."]),
  kaisetsu(41, ["友達について書かれた文章である。",
   "下線部の文を見る。「①そうした発想から解放されなければならない」の「そうした発想」とは、学校では「みんな仲良く」して、「いつも心が触れ合って、みんなで一つだ」という考え方（友だち幻想）を指す。この考え方に{縛|しば}られない考え方の例を選ぶ。",
   "1：クラスの仲間同士対立が起きないようにするのは、みんなが一つになるための行動である。", "2：一人で行動している子供を仲間に入れるようにするのは、みんなが一つになるための行動である。",
   "3：正解", "4：掃除など自分が任された仕事をするのはクラスのルールであり、ルールのことは書かれていない。"]),

  items("実力養成編　第2部　広告・お知らせ・説明書きなど（pp.74–75）", [
   ("第2部では、生活や仕事の中でよく見る文章（ビジネスレター、メール、広告、お知らせ、説明書き、表・リストなど）を読みます。これらの文章は、最初から最後まで全部理解する必要はないので、わからない言葉や表現は飛ばして読んでください。ここでは問いの種類を二つに分類し、それによって文章の読み方を変えて正解を導きます。", "From tomorrow: real-life texts (letters, e-mails, ads, notices, instructions, tables). You DON'T need to understand every word — skip the hard ones!"),
   ("「問い」を読んで、どちらの種類の問いか、判断する。\n1．タイトルを選ぶ、目的を問う　→全体をつかむ―全体的な内容を尋ねる問い\n2．「いつ」「どうやって」などを問う　→情報を探し出す―部分的な内容を尋ねる問い", "Two kinds of question: (1) the whole picture — title or purpose; (2) find one piece of info — when? how? how much?"),
  ], explain="Day 11 starts 第2部. Indha page-ai first padinga — it's the map for all the 広告・お知らせ lessons."),
  items("1．全体をつかむ―全体的な内容を尋ねる問い", [
   ("ビジネスレター、メール、{貼|は}り{紙|がみ}などの内容、目的を読み取る。", "Goal: get the content and the PURPOSE."),
   ("ステップ1　問いを読もう：タイトルを選ぶ　文章の目的を問うなど", "Read the question first."),
   ("ステップ2　どのような文章か知ろう\n◇全体にざっと目を通す。何の文章か？　ビジネスレター、メール、貼り{紙|がみ}、お知らせなど\n◇一般的な形式についての知識を使う。手紙やメールなどには一般的な形式がある。その形式を知っていれば、文章の目的やいちばん伝えたいことがどこにあるかすぐにわかる。", "Skim the whole thing. Letters and e-mails have fixed formats — the main point is usually after the greeting."),
   ("ステップ3　選択肢と比べよう：読み取った情報と選択肢を比べ、正解を探す。", "Compare with the choices."),
  ]),
  items("2．情報を探し出す―部分的な内容を尋ねる問い", [
   ("広告、お知らせ、説明書き、表・リストから必要な情報を探す。", "Goal: pick out the info you need."),
   ("ステップ1　問いと選択肢を読もう：問いと選択肢からどのような情報を探すべきか見る。例：いくら？　いつ？　何が必要？　など", "Decide what to look for."),
   ("ステップ2　どこに情報があるか探そう\n◇問いと選択肢にある言葉をキーワードとして答えを探す。\n　例：いくら？ → 本文中から数字、「～円」、「¥」などを探す。　電話する？ → 本文中から「電話」「おかけください」などを探す。\n◇広告か、お知らせか、説明書きかなど、文章の種類をつかんだ{上|うえ}で、自分の知識を活用する。\n　例：安売りの広告なら、何がいくら安くなるか、いつからいつまで安いかなどの情報が書いてあるはずである。その知識を使って、わからない言葉や数字の意味を推測する。\n◇目立つ部分に注目する。\n　◇タイトル　◇項目／見出し　◇大きい字、太い字、小さい字　◇下線　◇矢印、番号　◇枠、囲み", "Use keywords (～円, 電話…), your real-life knowledge (a sale ad tells you what, how much, from when), and anything that stands out (titles, headings, bold, arrows, boxes)."),
   ("ステップ3　正しい答えを選ぼう：読み取った情報から正解を探す。", "Choose."),
   ("1、2ともに、例題の後に{語|ご}いリストをつけた。\n重要{語|ご}い：例題の本文及び選択肢の中にある{語|ご}いのうち、問いを解く上で重要な{語|ご}い\n関連{語|ご}い：同じようなテーマの問題を解く上で覚えておいたほうがいい{語|ご}い\n練習の{語|ご}い：練習で使われている重要{語|ご}い\n・省略語など意味がわかりにくいものには、（　）{内|ない}に説明を加えた。", "Word lists come after each 例題: 重要{語|ご}い (key words), 関連{語|ご}い (related), 練習の{語|ご}い (from the practice)."),
  ]),
 ],
}
