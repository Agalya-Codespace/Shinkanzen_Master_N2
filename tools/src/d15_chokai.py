from _h import *
DAY = 15

NOTE = "Real CD track. The book prints no script or answer for 練習 and ステップアップ, so the script below was transcribed from the CD and checked by sensei; the answers are sensei's."
ABC = ["a", "b", "c"]
N3 = ["1", "2", "3"]

def pick(id, q, opts, ans, explain, keys=None):
    return mcq(id, q, opts, ans, explain, keys=keys or [""] * len(opts))

def struct(id, label, ans, explain, opts_text):
    return pick(id, label + "　どのような構造ですか。\n" + opts_text, ABC, ans, explain, keys=ABC)

SECTION = {
 "book": "chokai",
 "title": "実力養成編　Ⅴ「概要理解」　2 キーワードを関連づけて、話の構造をつかむ",
 "source": "新完全マスター聴解 N2 · 実力養成編 Ⅴ-2 · pp.70–75 · CD A82–A83 (read-aloud of the book's script), CD B01–B09 (real CD)",
 "blocks": [
  items("2　キーワードを関連づけて、話の構造をつかむ", [
   ("ここでは、キーワード（話の中で大切だと思われる言葉）を関連づけて、話の構造をつかむ練習をします。",
    "Sensei: Yesterday we sorted 'example' words from 'summing-up' words. Today we go one step further: draw a little map of how the keywords connect. Is it A → B → C (a change)? One topic split in two? A list under one heading? Once the map is clear, the 'what is it about?' answer is obvious."),
  ]),

  text("①話を聞いてください。この話はどのような構造になっていますか。キーワードを関連づけて考えてください。", "☆例題2"),
  audio("例題2 ①　CD A82", "a82", "", label="A82 · computer read-aloud of the book's script"),
  group("例題2 ①", [
   struct("d15c-e2-1", "", 2, ["Book's answer: c.", "最初に「教える人」「習う人」という対立する2つの言葉を紹介してから、「勉強する立場の人たちを何と言いますか」と聞いているので、「勉強する立場の人＝習う人」が重要なキーワードです。その後に続く「学生」「児童」「生徒」が「習う人」の「呼び方」の例です。したがって、この「習う人の呼び方」が話の中心だと整理できます。このようなキーワードの関係を表しているのはcです。"],
     "a　教師 ― 学生 ― 児童 ― 生徒\nb　学校 ┬ 教える人 ― 教師\n　　　　└ 習う人 ― 学生\nc　習う人 ┬ 児童\n　　　　　├ 生徒\n　　　　　└ 学生"),
  ]),
  audio("例題2 ②　CD A82 → A83", "a83", "②もう一度話を聞いてください。その後で質問に答えてください。", label="A83 · computer read-aloud of the book's question"),
  group("例題2 ②", [
   pick("d15c-e2-2", "Choose 1–3 (the question and choices are in the audio).", N3, 1,
    ["Book's answer: 2 (習う人たちの呼び方).", "Thanglish: 教師 is only mentioned once. The rest — 児童, 生徒, 学生 — are all names for the LEARNERS, changing with age. So the talk is about what learners are called."]),
  ]),
  script("例題2　スクリプトと答え（本）", [
   ("テレビで女の人が話しています。", "Situation."),
   ("女：学校っていうと、[[教える人]]がいて、[[習う人]]たちがいる場を考えますね。教える立場の人は「{教師|きょうし}」です。その教師の下で勉強する立場の人たちを[[何と言いますか]]。", "Two contrasting words, then the question → 習う人 is the key."),
   ("「学生」でしょうか。実はこれは、通っている学校によって違います。{通常|つうじょう}は{年齢|ねんれい}で[[呼び方]]が変わると言えるでしょう。", "呼び方 = the summing-up word."),
   ("{小学生|しょうがくせい}なら「[[{児童|じどう}]]」、中学生、高校生なら「[[{生徒|せいと}]]」、{専門|せんもん}学校や大学に通う人は「[[学生]]」で、「7歳の学生」というのは普通はありません。また、「生徒たちの{運動会|うんどうかい}」といえば、中学校か高校の運動会を意味します。", "Examples of 呼び方."),
   ("女の人は何について話していますか。\n1　教える人と習う人との関係\n2　習う人たちの呼び方\n3　習う人の学校での立場", "Question and choices."),
  ], extra=[text("答え　①c　②2", "答え（本）")]),

  text("Now the same two steps with real CD tracks. Step ① choose the structure a–c; step ② listen again and choose 1–3.", "練習2", ["Thanglish: Mudhalla map, appuram answer. Map correct-aa irundhaa answer easy."]),

  audio("練習2 (1)　CD B01", "b01", "①話を聞いてください。この話はどのような構造になっていますか。キーワードを関連づけて考えてください。", tts=False, note=NOTE),
  group("練習2 (1)", [
   struct("d15c-r2-1a", "①", 1, ["Answer b.", "関東では若い時がイナダ、そしてワラサ、それからブリ — 関西ではハマチ、メジロ、そしてブリ. Two regions, each with a growth sequence (→). That's b.", "a forgets the regions and the order; c puts さんま (a different fish) in the list."],
     "a　ぶり ┬ いなだ／はまち／わらさ／めじろ\nb　ぶり ┬ 関東 …… いなだ → わらさ → ぶり\n　　　　└ 関西 …… はまち → めじろ → ぶり\nc　名前が変わる魚 ┬ 関東 ┬ さんま／ぶり／いなだ\n　　　　　　　　　└ 関西 ── はまち"),
   pick("d15c-r2-1b", "②　CD B01 → B02　女の人は何について話していますか。\n1　ぶりという魚の種類\n2　ぶりの呼び方の変化\n3　ぶりの成長の地域性", N3, 1,
    ["Answer 2.", "Key sentence: ブリは成長段階によって呼び方が変わるのです. The whole talk is about the names changing as the fish grows.", "1: いなだ・はまち are not other kinds — 実はこのイナダもハマチもブリと同じ魚です. 3: the regions differ in the NAMES, not in how it grows."]),
  ]),
  audio("練習2 (1) 質問　CD B02", "b02", "", tts=False),
  script("練習2 (1)　スクリプト（CDから） · open after you answer", [
   ("テレビで女の人が話しています。", ""),
   ("女：秋においしい魚といえば、ぶりがサンマやサケと並んで有名です。ほかにもイナダやハマチが秋においしい魚としてよくあげられますが、[[実はこのイナダもハマチもブリと同じ魚です]]。", "実は → surprise fact: same fish."),
   ("ブリは[[成長段階によって呼び方が変わる]]のです。", "★ Main point."),
   ("[[関東]]では若い時がイナダ、そしてワラサ、それからブリになり、[[関西]]ではハマチ、メジロ、そしてブリの順に大きくなります。", "Two regions × growth order → structure b."),
   ("最近では関西の呼び方であるハマチが広く知られるようになりましたが、ブリとは別の魚だと思っている人もいるようです。", ""),
   ("女の人は何について話していますか。\n1　ぶりという魚の種類\n2　ぶりの呼び方の変化\n3　ぶりの成長の地域性", ""),
  ], extra=[text("答え　①b　②2", "答え")]),

  audio("練習2 (2)　CD B03", "b03", "①話を聞いてください。この話はどのような構造になっていますか。キーワードを関連づけて考えてください。", tts=False, note=NOTE),
  group("練習2 (2)", [
   struct("d15c-r2-2a", "①", 2, ["Answer c.", "The two places that look after pets are ペットホテル (you take the pet to the 店) and ペットシッター (they come to your 自宅). {保育所|ほいくしょ} and ベビーシッター are only comparisons (のようなもの, ～のように).", "a, b treat the comparisons as real kinds of 世話をする所."],
     "a　世話をする所 ┬ ペットホテル／{保育所|ほいくしょ}／ペットシッター／ベビーシッター\nb　世話をする所 ┬ ペットホテル ― ペットシッター\n　　　　　　　　└ {保育所|ほいくしょ} ― ベビーシッター\nc　世話をする所 ┬ ペットホテル …… 店\n　　　　　　　　└ ペットシッター …… 自宅"),
   pick("d15c-r2-2b", "②　CD B03 → B04　男の人は何について話していますか。\n1　ペットと赤ちゃんを世話するところの共通点\n2　子供とペットの世話をするところの種類\n3　ペットホテルとペットシッターの違い", N3, 2,
    ["Answer 3.", "He contrasts the two: ペットホテル = take the pet to the shop (but some pets get stressed by the change); ペットシッター = comes to your home, less stress. しかし marks the contrast.", "1, 2: the baby/child things are only comparisons to help you imagine."]),
  ]),
  audio("練習2 (2) 質問　CD B04", "b04", "", tts=False),
  script("練習2 (2)　スクリプト（CDから） · open after you answer", [
   ("テレビで男の人が話しています。", ""),
   ("男：出張や旅行などで家を{留守|るす}にするとき、かわいいペットの世話をどうしますか。そんなとき気軽に利用できるのが[[ペットホテル]]です。", "Topic 1."),
   ("ペットホテルは飼い主がペットを[[店まで連れて行って]]そこで面倒を見てもらうので、子供を預ける{保育所|ほいくしょ}のようなものです。散歩や{餌|えさ}の心配もなく安心して預けられます。", "保育所のようなもの = comparison only."),
   ("[[しかし]]ペットによっては環境が変わってストレスを感じ、元気がなくなってしまうこともあります。そのようなペットには[[ペットシッター]]が便利です。", "しかし → contrast, topic 2."),
   ("ペットシッターはベビーシッターが赤ちゃんの家に来て面倒を見てくれるように、[[自宅まで来て]]散歩に連れて行ってくれたり餌をやってくれたりするので、ペットにとってはストレスが少なくて済みます。", "店 vs 自宅 → structure c."),
   ("男の人は何について話していますか。\n1　ペットと赤ちゃんを世話するところの共通点\n2　子供とペットの世話をするところの種類\n3　ペットホテルとペットシッターの違い", ""),
  ], extra=[text("答え　①c　②3", "答え")]),

  audio("練習2 (3)　CD B05", "b05", "①話を聞いてください。この話はどのような構造になっていますか。キーワードを関連づけて考えてください。", tts=False, note=NOTE),
  group("練習2 (3)", [
   struct("d15c-r2-3a", "①", 2, ["Answer c.", "携帯電話も固定電話も後払い … しかし、電話をかける前にお金を払う（先払い）… 公衆電話. The talk splits phones by WHEN you pay.", "a lists phone types; b is a history line. Both miss the 後払い／先払い key."],
     "a　電話 ┬ 携帯電話／固定電話／公衆電話 ┬ 10円玉／テレフォンカード\nb　公衆電話(10円玉) → 公衆電話(テレフォンカード) → 固定電話 → 携帯電話\nc　電話 ┬ 後払い ┬ 携帯電話／固定電話\n　　　　└ 先払い ── 公衆電話"),
   pick("d15c-r2-3b", "②　CD B05 → B06　女の人は何について話していますか。\n1　電話の種類\n2　電話の歴史\n3　電話の料金の払い方", N3, 2,
    ["Answer 3.", "Keywords 後払い, 先払い, お金を払う keep coming back. The phone types and the history are only there to explain the two ways of paying."]),
  ]),
  audio("練習2 (3) 質問　CD B06", "b06", "", tts=False),
  script("練習2 (3)　スクリプト（CDから） · open after you answer", [
   ("テレビで女の人が話しています。", ""),
   ("女：携帯電話が{登場|とうじょう}する前は、電話といえば主に家や会社などの決まった場所からかける{固定電話|こていでんわ}のことでした。", ""),
   ("携帯電話も固定電話も[[後払い]]、つまり利用した人が後から使った分だけお金を払いますよね。今ではこの方法が当たり前のように思われています。", "Key 1."),
   ("[[しかし、電話をかける前にお金を払う]]のが当たり前の時代もありました。電話が使われ始めたころは電話機はとても高くて、普通の人には買うことができないものでした。", "Key 2: 先払い."),
   ("そこで駅やホテル、{公共施設|こうきょうしせつ}など多くの人が出入りする場所に[[公衆電話|こうしゅうでんわ]]を置き、お金を払って利用できるようにしたのです。", ""),
   ("今でも公衆電話のほとんどは[[先払い]]で、10円玉を入れてかけるタイプのものや、テレホンカードが使えるものなどがあります。", "→ structure c."),
   ("女の人は何について話していますか。\n1　電話の種類\n2　電話の歴史\n3　電話の料金の払い方", ""),
  ], extra=[text("答え　①c　②3", "答え")]),

  audio("練習2 (4)　CD B07", "b07", "①話を聞いて、話に出てくるキーワードを書き取ってください。", tts=False, note=NOTE),
  group("練習2 (4)", [
   fill("d15c-r2-4k", "①　キーワード（いくつでも）：%%", ["紅茶", "緑茶", "ウーロン茶", "お茶", "作り方", "同じ木", "{木|き}の{葉|は}", "葉"], "Model keywords: 紅茶・ウーロン茶・緑茶, 作り方, (お茶の)木, 同じ種類, 葉. Any of them counts — compare with the script."),
   pick("d15c-r2-4s", "②　この話はどのような構造になっていますか。a～cの型からよいものを選んでください。\na　［　］┬［　］／［　］／［　］　(one box splitting into three)\nb　［　］┬［　］―［　］\n　　　　└［　］　(two branches, one goes further)\nc　［　］―［　］\n　　［　］―［　］\n　　［　］―［　］　(three separate pairs)", ABC, 0,
    ["Answer a: 同じお茶の{木|き}の{葉|は} ┬ 紅茶／ウーロン茶／緑茶 (they differ only in 作り方).",
     "c would be the wrong picture: 紅茶の木、緑茶の木… — the man says some people think that, but 実は すべて同じ種類のお茶の{木|き}の{葉|は}から作られる."], keys=ABC),
   pick("d15c-r2-4q", "③　CD B07 → B08　男の人はお茶についてどう言っていますか。\n1　紅茶、緑茶、ウーロン茶は同じ{木|き}の{葉|は}から作られる\n2　紅茶とウーロン茶は同じ{木|き}の{葉|は}を使うが緑茶は違う\n3　木の種類によってお茶の種類が違う", N3, 0,
    ["Answer 1.", "Key sentence after 実は: すべて同じ種類のお茶の{木|き}の{葉|は}から作られるのです. The difference is only the 作り方.", "2: ウーロン茶 is only 'closer to' 紅茶 in how it's made. 3 is the mistaken idea he corrects."]),
  ]),
  audio("練習2 (4) 質問　CD B08", "b08", "", tts=False),
  script("練習2 (4)　スクリプト（CDから） · open after you answer", [
   ("男の人がお茶について話しています。", ""),
   ("男：[[紅茶|こうちゃ]]、[[ウーロン茶]]、[[緑茶|りょくちゃ]]。この3種類のお茶は、色も味も香りもそれぞれ違います。なぜこんな違いがあるかというと、それは[[作り方が違う]]からなんです。", "Keywords."),
   ("紅茶と緑茶とでは作り方が全く違います。ウーロン茶はどちらかというと紅茶に近いですが、やはり紅茶とは違う作り方をします。", ""),
   ("色も味も香りも違うから、紅茶は紅茶の木、緑茶は緑茶の木というように木の種類が違うと思う人もいるかもしれませんが、[[実はすべて同じ種類のお茶の{木|き}の{葉|は}から作られる]]のです。", "★ Main point → structure a, answer 1."),
   ("作り方の違いによって同じ葉っぱからいろんなお茶が楽しめるなんて、不思議ですね。", ""),
   ("男の人はお茶についてどう言っていますか。\n1　紅茶、緑茶、ウーロン茶は同じ{木|き}の{葉|は}から作られる\n2　紅茶とウーロン茶は同じ{木|き}の{葉|は}を使うが緑茶は違う\n3　木の種類によってお茶の種類が違う", ""),
  ], extra=[text("答え　①キーワード：紅茶・ウーロン茶・緑茶・作り方・同じ{木|き}の{葉|は}　②a　③1", "答え")]),

  audio("ステップアップ問題2　CD B09", "b09", "この問題は話の前に質問はありません。まず話を聞いてください。それから、質問と選択肢を聞いて、1から4の中から、最もよいものを一つ選んでください。", tts=False, note=NOTE),
  group("ステップアップ問題2", [
   pick("d15c-s2", "Listen, then choose 1–4.", ["1", "2", "3", "4"], 2,
    ["Answer 3 (植物が移動する方法).",
     "Map: 植物の移動方法 ┬ 自分の力（種が割れて飛ぶ）├ 風の力（タンポポ）└ 動物を利用（くっつく・実を食べてもらう）. The talk lists the ways plants move.",
     "1: the animal/plant difference is only the opening. 2: 範囲を広げる is the purpose, not the topic. 4 is only one of the three ways."]),
  ]),
  script("ステップアップ問題2　スクリプト（CDから） · open after you answer", [
   ("テレビで女の人が話しています。", ""),
   ("女：動物は自分で動いて生活の場所を変えることができますが、植物はそれができません。でも、自分で動けない植物も、親から離れて生活範囲を広げるために[[様々な移動方法]]を身につけています。", "★ Topic: 移動方法."),
   ("種が割れて遠くへ飛ぶなど[[自分の力だけで動く]]ものもあれば、タンポポのように[[風の力を利用して]]遠くに飛ばされて、親の植物から数百メートルも離れたところで成長するものもあります。", "Ways 1 and 2."),
   ("また、そばを通った動物にくっついて遠くに運んでもらうとか、甘い実をつけて食べられ、{糞|ふん}としてまき散らしてもらうなど、[[動物を利用して移動する]]ものもあります。", "Way 3."),
   ("女の人は何について話していますか。\n1　植物が動物と違う点\n2　植物が育つ範囲\n3　植物が移動する方法\n4　植物が動物を利用する方法", ""),
  ], extra=[text("答え　3", "答え")]),
 ],
}
