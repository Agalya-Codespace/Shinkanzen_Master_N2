from _h import *
DAY = 7

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
 "title": "2. 問いを解く技術を身につける　2）「だれが」「何が」「何を」などを問う",
 "source": "新完全マスター読解 N2 · 第1部 評論・解説・エッセイなど · pp.46–51 · 例題 answers in the book; 練習 answers from 別冊 解答 p.9",
 "blocks": [
  items("◆「だれが」「何が」「何を」などを問う", [
   ("「何が＿＿（～する）のか。」「＿＿（～する）のは、だれか。」「何を＿＿（～する）のか。」「何と＿＿（～する）のか。」という{形|かたち}の問題。",
    "Question shapes: 'Yaaru ～ pannraanga?', 'Edhu ～?', 'Edha ～?'. Japanese-la subject-a adikkadi vittuduvaanga — adha thedi kandupidikkanum."),
   ("下線部に書かれていない主語や対象語などを探す。",
    "主語(しゅご) = subject (yaaru/edhu). 対象語(たいしょうご) = object (edha). Underlined part-la ivanga ezhudhala — neenga dhaan thedanum."),
   ("次の順番で考えよう。", "Order:"),
   ("・まず、下線部をよく見て、内容をつかもう。", "Step 1: Underlined part-a nalla paarunga, enna nadakkudhu-nu purinjikonga."),
   ("・前後を見て答えを探し、下線部の主語、対象語に当てはめてみよう。", "Step 2: Munnaadi-pinnaadi paathu answer thedi, adha subject/object edathula pottu check pannunga."),
  ], explain="Inniki technique: missing subject. Japanese-la 'Raman school-ku ponaan. Saappittaan. Thoonginaan.' maadhiri — first sentence-la mattum subject, appuram ellaam vittuduvaanga. So 「Aは～」 paathu, adhu evlo dhooram continue aagudhu-nu follow pannunga."),

  passage("☆例題11　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "オーケストラは{演奏会|えんそうかい}の前に、その{会場|かいじょう}で{本番|ほんばん}と同じように練習する。このとき、ステージマネジャーは、まずトラックで練習場から{会場|かいじょう}まで楽器を運び、{会場|かいじょう}を{本番|ほんばん}どおりに{設定|せってい}し、舞台や客席の{照明|しょうめい}を決める。練習が始まれば曲の演奏時間を{計|はか}り、遅れて来たお客さんを席に{案内|あんない}するタイミングも決める。{本番|ほんばん}になると、ステージに続くドアを開け閉めして、{指揮者|しきしゃ}や{演奏者|えんそうしゃ}を送りだしたり迎えたりする。{照明|しょうめい}やアナウンスの指示もする。そして{演奏会後|えんそうかいご}は舞台を{片付|かたづ}け、楽器を練習場まで戻して、①[[次の準備をする]]のである。",
  ], [
   "演奏会(えんそうかい) = concert. 会場(かいじょう) = venue. 本番(ほんばん) = the real performance. 設定(せってい) = set up. 照明(しょうめい) = lighting. 計(はか)る = measure (time). 案内(あんない) = guide. 指揮者(しきしゃ) = conductor. 演奏者(えんそうしゃ) = performers. 片付(かたづ)ける = tidy up.",
   "Sentence 2-la ステージマネジャーは vandhuchu. Adhukku appuram ella sentence-um subject illaama continue aagudhu → ellaam stage manager pannradhu dhaan.",
  ]),
  toi("d7d-e11", "①次の準備をするのはだれか。", [
   "オーケストラ", "ステージマネジャー", "{指揮者|しきしゃ}", "{演奏者|えんそうしゃ}"], 1,
   ["Answer 2. 'このとき、ステージマネジャーは…' — andha は topic last sentence varaikkum continue aagudhu. 運び、設定し、決める、計り、決める、開け閉めして、送りだしたり迎えたりする、指示もする、片付け、戻して、次の準備をする — all stage manager.",
    "1: オーケストラ is only the subject of the first sentence (練習する). 3, 4: they are the people the manager 送りだす/迎える."]),
  {"type": "reveal", "label": "本の解説：例題11", "children": [
   items("ステップ1　本文を読んで全体をつかもう", [("キーワード：オーケストラ、演奏会、会場、ステージマネジャー　→　テーマは、演奏会？", "Keywords → theme.")]),
   items("ステップ2　問いを見て本文から答えを探そう", [
    ("1）下線部の文を見る：「①次の準備をするのである」　「～はだれか」　→　主語を質問している。", "The question asks for the subject."),
    ("2）前の文を見る：[[オーケストラは]]、…練習する。", "Subject of sentence 1 only."),
    ("このとき、[[ステージマネジャーは]]、…運び、…設定し、…照明を決める。", "New topic: stage manager."),
    ("練習が始まれば…計り、…決める。", "(stage manager)"),
    ("本番になると、…開け閉めして、…送りだしたり迎えたりする。", "(stage manager)"),
    ("照明や～指示もする。", "(stage manager)"),
    ("そして演奏会後は…片付け、…戻して、…次の準備をするのである。", "(stage manager)"),
    ("この五つの文の主語は、すべて「ステージマネジャー」", "All five sentences → ステージマネジャー."),
   ]),
   items("ステップ3　選択肢と比べよう", [T("次の準備をするのは「ステージマネジャー」"), T("2：正解")]),
   items("ポイント", [
    ("「だれが」「何が」を問う問題の場合、トピックを表す助詞「は」に注目しよう。", "助詞(じょし)「は」 = topic marker. Adha follow pannunga."),
    ("「Aは～。～。～。Bは～」のような文章の場合、「A」が2文目や3文目の主語になることが多い。", "A は vandha, adutha sentences-um A dhaan subject — B は varra varaikkum."),
   ]),
  ]},

  passage("☆例題12　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "むかしは、トレーニングを{軽視|けいし}しがちだった。いや{軽視|けいし}したわけではないが、テニスの選手が、野球をしたり、スキーをやったり、あるいは{陸上競技|りくじょうきょうぎ}に出たりしたこともあるそうだ。それが、知らず知らずのうちにいいトレーニングになっていたのだろう。だがスポーツをする人が多くなってから、{各競技|かくきょうぎ}かけ持ちという{万能|ばんのう}選手がいなくなって、{次第|しだい}に、トレーニングをあまりやらなくなった時代があるという。もちろん軽い{体操|たいそう}やランニングは、どんな時代でもあったが……。",
   "①[[いまは違う]]。「科学的」ということばが流行しているように、トレーニングも{重要視|じゅうようし}されるようになった。それも、サッカーなら、サッカーにあうように、テニスならテニスにいいように研究されてきている。",
  ], [
   "Para 1: 軽視(けいし)する = make light of. ～がち = tend to. 陸上競技(りくじょうきょうぎ) = track and field. 知らず知らずのうちに = without realising. かけ持ち = doing several at once. 万能(ばんのう)選手 = all-rounder. 次第(しだい)に = gradually. 体操(たいそう) = exercises.",
   "Para 2: 流行(りゅうこう) = be in fashion. 重要視(じゅうようし) = regard as important. ～にあうように = to suit ～.",
   "Structure: むかし vs いま (対比). むかし = other sports became training without realising. いま = training suited to each sport is researched.",
  ], src="石黒修『テニス』講談社"),
  toi("d7d-e12", "①いまは違うとは、むかしとどのように違うのか。", [
   "むかしは、トレーニングを{軽視|けいし}していたが、いまは「科学的」研究が盛んになり、トレーニングを全くしなくてもよくなった。",
   "むかしはトレーニングをしなくてもどんなスポーツもうまくなったが、いまはスポーツによって異なるトレーニングが必要である。",
   "むかしは、ほかのスポーツをすることがトレーニングになっていたが、いまはそれぞれのスポーツにあうトレーニングをするようになった。",
   "むかしは、いろいろなスポーツをかけ持ちでやる選手がいなかったが、いまはトレーニングが重視され、{万能|ばんのう}選手が増えてきた。"], 2,
   ["Answer 3. むかし: playing other sports (野球、スキー、陸上) was good training without knowing. いま: training is researched to suit each sport.",
    "1: 全くしなくてもよい — not written. 2: 'became good without training' — not written. 4: reversed — むかし there WERE all-rounders, and 万能選手が増えた is not written."]),
  {"type": "reveal", "label": "本の解説：例題12", "children": [
   items("ステップ1　本文を読んで全体をつかもう", [("キーワード：トレーニング、軽視、「科学的」、重要視　→　テーマは、トレーニング？", "Keywords → theme.")]),
   items("ステップ2　問いを見て本文から答えを探そう", [
    ("下線部の文を見る：①いまは違う。　→　「むかし」と「いま」の対比に注目する。", "対比(たいひ) = contrast."),
    ("[[むかし]]は、トレーニングを軽視しがちだった。いや軽視したわけではないが、テニスの選手が、野球をしたり、…陸上競技に出たりしたこともあるそうだ。[[それ]]が、知らず知らずのうちにいいトレーニングになっていた", "むかし side."),
    ("[[いま]]は、トレーニングも重要視されるようになった。それも、サッカーなら、サッカーにあうように、…研究されてきている", "いま side."),
   ]),
   items("ステップ3　選択肢と比べよう", [
    T("むかしは、ほかのスポーツをすることがいいトレーニングになっていた。"),
    T("いまは、「科学的」トレーニングが重視され、それぞれのスポーツにあうものが研究されている。"),
    T("1：いま、トレーニングを全くしないとは書かれていない。"),
    T("2：むかし、トレーニングをしなくてもうまくなったとは書かれていない。"),
    T("3：正解"),
    T("4：むかし、スポーツをかけ持ちしなかったとは書かれていない。いま、万能選手が増えてきたとは書かれていない。"),
   ]),
  ]},

  text("Ippo practice. Ovvoru underline-kkum: (1) question 'yaaru/edhu' kekkudhaa paarunga, (2) munnaadi sentences-la は topic thedunga, (3) answer-a underline-oda subject/object-aa pottu read pannunga.", "🎓 練習25～27"),

  passage("練習25　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "人に何かを聞かれたとき、つい使ってしまうのが「あ、それでいいですよ」という言葉。ベストではないが断るほどでもない、といったニュアンスだろう。",
   "たとえば、{帰宅|きたく}して妻に「{夕飯|ゆうはん}、カレーなんだけど」と言われた夫が、「ランチもカレーだったのにな」と思いながらも「ああ、それでいいよ」と答えてしまう、という感じだ。{本音|ほんね}では「カレーが{二回|にかい}続くのはイヤだな」と思いながらもそれを口にしないやさしさも、そこには{込|こ}められている。",
   "しかし、「それでいいよ」と言われたほうは、そこに{混|ま}じっている{気配|きくば}りややさしさには①[[なかなか気づかない]]。",
  ], [
   "Para 1: つい = without meaning to. 断(ことわ)るほどでもない = not bad enough to refuse. ニュアンス = nuance.",
   "Para 2: 帰宅(きたく) = come home. 夕飯(ゆうはん) = dinner. 本音(ほんね) = true feeling. 口にしない = not say it. 込(こ)められている = is packed in.",
   "Para 3: 混(ま)じる = be mixed in. 気配(きくば)り = consideration. 'それでいいよ'-nu sonnadhu husband. 言われたほう = the one who was told = wife, who asked 'カレーなんだけど'.",
  ], src="香山リカ『言葉のチカラ　コミュニケーションレッスン』集英社"),
  toi("d7d-r25", "①なかなか気づかないのはだれか。", [
   "カレーでいいかどうか聞かれた人",
   "カレーでいいかどうか聞いた人",
   "カレーでいいと答える人",
   "カレーはイヤだと思う人"], 1,
   ["Answer 2. 主語 = 「それでいいよ」と言われたほう = the wife who asked 'is curry OK?'. She doesn't notice the husband's kindness.",
    "1, 3, 4 are all the husband — he is the one being kind, not the one failing to notice."]),
  kaisetsu(25, ["「それでいいよ」という言葉について書かれた文章である。",
   "①なかなか気づかないの主語は「それでいいよ」と言われたほう＝いいかどうか聞いた人", "2：正解"]),

  passage("練習26　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "まとめて{助数詞|じょすうし}と呼ぶそうだが、ものを{勘定|かんじょう}する言葉は{奥深|おくぶか}い。生き物は{匹|ひき}で足りると思いきや、ウサギは{羽|わ}、イカは{杯|はい}、チョウは{頭|とう}とも数える。では、それらを生き物たらしめている命はどう数えるのだろう。{草花|くさばな}にも①[[ある]]から{人|にん}や{体|たい}ではなく、{個|こ}も違う。",
   "とりあえず、八つの命が送り出されたと書く。{米国|べいこく}で生まれた男6人、女2人の{八|や}つ{子|ご}である。680～1470グラムの{未熟児|みじゅくじ}（注1）ながら、{帝王切開|ていおうせっかい}（注2）による5分の「{安産|あんざん}」だった。{八|や}つ{子|ご}は{米国|べいこく}で2例目、全員が元気に育てば世界初のケースになるらしい。",
  ], [
   "（注1）{未熟児|みじゅくじ}：普通より軽い体重で産まれた赤ん坊　（注2）{帝王切開|ていおうせっかい}：出産のために行う手術",
   "Para 1: 助数詞(じょすうし) = counter words. 勘定(かんじょう)する = count. 奥深(おくぶか)い = deep. ～と思いきや = you'd think ～, but. 匹(ひき)・羽(わ)・杯(はい)・頭(とう) = counters for animals, rabbits (traditionally), squid, butterflies. ～たらしめる = make something what it is. 草花(くさばな) = plants and flowers. 人(にん)・体(たい)・個(こ) = counters for people, bodies, objects.",
   "Flow: 'How do we count 命? 命 exists in plants too (草花にもある), so it isn't 人 or 体, and 個 doesn't fit either.' → subject of ある = 命.",
   "Para 2: 米国(べいこく) = USA. 八(や)つ子(ご) = octuplets. 安産(あんざん) = easy birth.",
  ], src="朝日新聞2009年1月30日"),
  toi("d7d-r26", "何が①あるのか。", [
   "生き物", "数", "命", "{助数詞|じょすうし}"], 2,
   ["Answer 3. The sentence before: '命はどう数えるのだろう'. Then [命は]草花にもあるから → 命 exists in plants too, so you can't count it with 人 or 体.",
    "1: 生き物 is what 匹/羽 count; the topic moved to 命. 2, 4: numbers and counters don't 'exist in flowers'."]),
  kaisetsu(26, ["八つ子が生まれたことについて書かれた文章である。",
   "「①ある」を含む文の前を見ると、「命はどう数えるのだろう」とあり、命について書かれている。",
   "「命はどう数えるのだろう。[命は]草花にも①あるから[命の数え方は]人や体ではなく、個も違う。」", "3：正解"]),

  passage("練習27　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "学校でも会社でも、「計算は速く正確にやれ」「{厳密|げんみつ}な答えを{出|だ}せ」とばかり言われる。そうして、みんな{頭|あたま}がくたびれて、いつしか数がキライになっていく。「それはあまりにモッタイナイことだ」と筆者は思うのである。",
   "数に強くなると、いろいろ{面白|おもしろ}くて、{実|み}になることが多くなる。たとえば、いつも{的確|てきかく}に判断できるようになるとか、物事を考えたとおりに動かせるようになる。そんなことを{繰|く}り返していると、とても自信がつく。そして、①[[もっとある]]。人が{褒|ほ}めそやしてくれるのである。だから、イイ気になれる（注1）。",
   "そういう人は、{脇|わき}から見ていると、{妙|みょう}に自信あり{気|げ}で、{立派|りっぱ}な感じに見える。{読者|どくしゃ}のみなさんのまわりにも、必ず{一人|ひとり}はそういう人がいるはずである。",
  ], [
   "（注1）イイ気になる：良い気持ちになる",
   "Para 1: 厳密(げんみつ) = exact. くたびれる = get tired. いつしか = before you know it. モッタイナイ = wasteful, a pity.",
   "Para 2: 実(み)になる = be useful, bear fruit. 的確(てきかく) = accurate. 自信(じしん)がつく = gain confidence. 褒(ほ)めそやす = praise lavishly. Topic sentence: 面白くて{実|み}になることが多くなる. たとえば～ = examples of it. そして、もっとある = [面白くて{実|み}になることは] even more → people praise you.",
   "Para 3: 脇(わき)から = from the side. 妙(みょう)に = strangely. 自信あり気(げ) = looking confident. 立派(りっぱ) = impressive.",
  ], src="畑村洋太郎『数に強くなる』岩波書店"),
  toi("d7d-r27", "①もっとあるとあるが、何がもっとあるのか。", [
   "数がキライになる理由",
   "イイ気になれること",
   "{的確|てきかく}に判断できるようになること",
   "{面白|おもしろ}くて{実|み}になること"], 3,
   ["Answer 4. Topic: 数に強くなると、面白くて{実|み}になることが多くなる. たとえば (的確に判断, 動かせる, 自信がつく) are examples. もっとある = there are even more 面白くて{実|み}になること — e.g. people praise you.",
    "3: only one of the examples. 2: イイ気になれる is the result of being praised, not what もっとある refers to. 1: Para 1 topic, not here."]),
  kaisetsu(27, ["数に強くなることについて書かれた文章である。",
   "下線部の前を見ると、「数に強くなると、いろいろ面白くて、{実|み}になることが多くなる。」と書かれている。「たとえば」以下は面白くて{実|み}になることの例である。",
   "[面白くて、{実|み}になることは]①もっとある。", "4：正解"]),
 ],
}
