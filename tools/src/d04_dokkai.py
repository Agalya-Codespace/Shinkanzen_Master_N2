from _h import *
DAY = 4

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
 "title": "1. 文章のしくみを理解する　3）［比喩］ほかのものにたとえる　4）［疑問提示文］疑問文を使って話題を提示する",
 "source": "新完全マスター読解 N2 · 第1部 評論・解説・エッセイなど · pp.22–31 · 例題 answers in the book; 練習 answers from 別冊 解答 pp.4–7",
 "blocks": [
  items("◆比喩とは", [
   ("比喩とは、難しいことを私たちがよく知っている日常的なことに置き換えて（＝たとえて）、わかりやすく説明することである。",
    "比喩(ひゆ) = metaphor / comparison. Kashtamaana vishayatha, namakku therinja daily vishayama maathi (たとえて) explain pannuvaanga."),
   ("本文に、それまでの内容と全く関係のない言葉が突然出てきたら、比喩を使っているかもしれない。何を何にたとえているかしっかりつかもう。",
    "Topic-ku sambandhame illaadha word thideernu vandhaa (sports pathi pesumbodhu 'mountain path'), adhu metaphor! 'Edha edhukku compare panraanga?'-nu pidinga."),
  ], explain="Inniki rendu techniques: 比喩 (metaphor) and 疑問提示文 (question that introduces the topic). Exam trap: metaphor-oda subject (mountain, umbrella, car) option-la vandhaa, adhu passage-oda theme illa!"),

  passage("☆例題6　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "スポーツをやる目的やかかわり方は{種々多様|しゅじゅたよう}である。オリンピックで金メダルを{争|あらそ}うような{熾烈|しれつ}なスポーツもあれば、勝敗はともかくみんなで楽しく遊べばよいというスポーツもある。健康のために、あるいはレクリエーションのためにというスポーツのある一方で、スポーツが仕事というプロスポーツも存在している。しかしやり方や目的は違え、どれもスポーツであることには変わりはない。（中略）",
   "レベルは違ってもスポーツはスポーツなのであり、そのレベルから少しでもうまくなり、強くなろうとするやり方は基本的には違いのないものである。{頂点|ちょうてん}に通じる長い{山道|やまみち}のどこを歩いているかの違いであり、けわしさや空気の{薄|うす}さは上にいくほどつらくはなるが、歩いて進むことや歩き方には変わりはない。そしてどこで立ち止まっても山の空気は新鮮で、景色は美しい。その人その人によって、どの高さで楽しんでもいいものだし、そうして{誰|だれ}にでももう少し高く登ってみたいと思わせるのがスポーツというものなのである。",
  ], [
   "Para 1: 種々多様(しゅじゅたよう) = all kinds. 金(きん)メダルを争(あらそ)う = compete for gold. 熾烈(しれつ)な = fierce. 勝敗(しょうはい)はともかく = win or lose doesn't matter. 存在(そんざい) = exist. Olympic sport, jolly sport, health sport, pro sport — ellaam sports dhaan.",
   "Para 2: 頂点(ちょうてん) = summit. けわしさ = steepness. 空気の薄(うす)さ = thin air. 立(た)ち止(ど)まる = stop. 新鮮(しんせん) = fresh. 景色(けしき) = scenery. Suddenly mountain path pathi pesuraar — adhu 比喩!",
   "Mountain = sports. Mela poga poga kashtam (higher level, harder practice), aanaa enga ninnaalum view azhagu (any level is fun), innum konjam mela poganum-nu thonum (want to improve).",
  ], src="浅見俊雄『スポーツの科学』東京大学出版会"),
  toi("d4d-e6", "この文章で筆者が最も言いたいことは何か。", [
   "登山は、どんな人でも楽しむことができ、誰もがより高いところを目指そうとする。",
   "登山というスポーツは、上にいくほど苦しくなるが、どこにも楽しさはある。",
   "スポーツとは、どのレベルでも楽しさがあり、少しでも上達したいと思うものである。",
   "スポーツにはさまざまなレベルがあるが、楽しくないものはスポーツではない。"], 2,
   ["Answer 3. Mountain story-a sports-ku maathunga: every level fun + want to improve.",
    "1, 2: 登山(とざん) is the metaphor, not the theme — classic trap! 4: 'fun illaadhadhu sports illa'-nu ezhudhala."]),
  {"type": "reveal", "label": "本の解説：全体をつかもう（例題6）", "children": [
   items("1）キーワードからテーマを推測する", [("スポーツ、{山道|やまみち}、けわしさ、高さ　→　テーマは、スポーツの話？　山登りの話？", "Rendu topic theriyudhu — edhu real theme, edhu metaphor?")]),
   items("2）「比喩」に注目する", [
     ("第1段落：オリンピックを目指すスポーツも、健康や楽しみのためのスポーツも同じスポーツである。", "Para 1 = all sports are the same 'sports'."),
     ("第2段落：スポーツ全般の話から、{山道|やまみち}の話になる。山登りはスポーツの比喩。山登りの話を通じて、スポーツについて何を言いたいか考える。山登りについて書かれている文章をスポーツに置き換えてみる。", "Para 2 = sports → mountain path. Mountain = metaphor for sports. Replace mountain words with sports words."),
   ]),
   {"type": "table", "title": "〔山登り〕→〔スポーツ〕", "rows": [
     ["頂点に通じる長い{山道|やまみち}", "→", "上達の過程"],
     ["けわしさ　空気の薄さ", "→", "練習の厳しさ、つらさ"],
     ["山の空気は新鮮　景色は美しい", "→", "楽しさ"],
     ["高さ", "→", "レベル"],
     ["高く登ってみたい", "→", "上手になりたい"],
   ], "explain": "Idhu dhaan metaphor decode: 過程(かてい) = process. 厳(きび)しさ = strictness. Left side (mountain) = right side (sports)."},
   items("3）全体をまとめる", [("上達のための練習の厳しさ、つらさ（＝けわしさ、空気の薄さ）はそれぞれ違う。しかし、どのレベルでも楽しめるし（＝山の空気は新鮮）、上達しよう（＝高く登ろう）と思わせるのがスポーツである。", "Summary: each level is hard in its own way, but every level is fun and makes you want to improve.")]),
   items("選択肢と比べよう", [T("1：登山は比喩で、この文章のテーマではない。"), T("2：登山は比喩で、この文章のテーマではない。"), T("3：正解"), T("4：楽しくないものはスポーツではないとは書かれていない。")]),
  ]},

  text("Ippo 比喩 practice. Ovvoru passage-layum: (1) topic-ku sambandhame illaadha word (umbrella, car, birds) kandupudinga, (2) 'X = Y' table podunga, (3) options-la metaphor word mattum irundhaa — trap!", "🎓 練習10～12"),

  passage("練習10　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "雨が降れば{傘|かさ}をさす。{傘|かさ}がなければ{風呂敷|ふろしき}でもかぶる。それもなければぬれるしか仕方がない。",
   "雨の日に{傘|かさ}がないのは、天気のときに{油断|ゆだん}して、その用意をしなかったからだ。雨にぬれて、はじめて{傘|かさ}の必要を知る。そして次の雨にはぬれないように考える。雨があがれば、何をおいても{傘|かさ}の用意をしようと決意する。これもやはり、人生の一つの教えである。",
   "わかりきったことながら、世の中にはそして人生には、晴れの日もあれば雨の日もある。{好調|こうちょう}の時もあれば、{不調|ふちょう}の時もある。にもかかわらず、晴れの日が少しつづくと、つい雨の日を忘れがちになる。{好調|こうちょう}の波がつづくと、ついゆきすぎる。{油断|ゆだん}する。これも、人間の一つの{姿|すがた}であろうか。",
  ], [
   "Para 1: 傘(かさ)をさす = hold up an umbrella. 風呂敷(ふろしき) = wrapping cloth. かぶる = put over one's head. ～しか仕方(しかた)がない = no choice but ～.",
   "Para 2: 油断(ゆだん) = carelessness. 用意(ようい) = preparation. 何(なに)をおいても = above all else. 決意(けつい) = resolve. 教(おし)え = lesson.",
   "Para 3: わかりきった = obvious. 好調(こうちょう) = going well. 不調(ふちょう) = going badly. ～がち = tend to. ゆきすぎる = go too far. 姿(すがた) = nature, figure.",
   "比喩: 晴れの日 = 好調の時, 雨の日 = 不調の時, 傘 = preparation for bad times. Nalla neram continue aanaa, ketta neram varum-nu marandhuduvom.",
  ], src="松下幸之助『道をひらく』PHP研究所"),
  toi("d4d-r10", "この文章の内容として最も適切なものはどれか。", [
   "雨の日に傘を持っていないのは、つい油断してしまうからである。",
   "人生がうまく行っている時は、悪い時に備える心を忘れがちだ。",
   "人は、雨があがると、いつもつい傘をどこかに忘れて来てしまう。",
   "人生が好調な時は晴れの日が続くので、傘を準備しておく必要はない。"], 1,
   ["Answer 2. 晴れ = good times, 雨 = bad times, 傘 = preparation. Good times-la bad times-ku prepare panna marandhuduvom.",
    "1, 3: real umbrella story = metaphor, not theme. 4: opposite — good times-laye prepare pannanum."]),
  kaisetsu(10, ["人生の好調、不調について書かれた文章である。", "比喩に注目する。",
   "晴れの日＝好調の時、雨の日＝不調の時、傘＝不調の時のための用意", "好調の時が続くと、不調の時のことを忘れがちである。",
   "1：傘の話は比喩であり、この文章のテーマではない。", "2：正解", "3：傘の話は比喩であり、この文章のテーマではない。", "4：好調なときも油断せず、用意をする必要がある。"]),

  passage("練習11　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "足が速い人は、生まれつき速い。遅い人は、生まれながらにして遅い。特に{短距離走|たんきょりそう}はポテンシャルの勝負――。",
   "そう思っている方が多いでしょうし、私もつい数年前まではそう思っていました。そして、ある面ではやはりその通りなのです。生まれ持った{骨格|こっかく}や{腱|けん}、{筋肉|きんにく}などの質によって、足の速さはかなりの部分まで決まってしまいます。",
   "車と同じで、エンジンの性能を超えた走りはできません。",
   "ただし、多くの人は、性能を限界まで引き出していないのです。また、エンジンの性能がアップしなくても、タイヤを{履|は}き{替|か}えたり、運転テクニックを上達させたりと、スピードをアップさせる方法はほかにいくらでもあるのです。",
  ], [
   "Para 1: 生(う)まれつき = by birth. 生まれながらにして = from birth. 短距離走(たんきょりそう) = sprint. ポテンシャル = potential.",
   "Para 2: 骨格(こっかく) = skeleton. 腱(けん) = tendon. 筋肉(きんにく) = muscle. 質(しつ) = quality. Udambu structure-aala speed konjam decide aagudhu — true.",
   "Para 3–4: 性能(せいのう) = performance. 限界(げんかい) = limit. 引(ひ)き出(だ)す = draw out. タイヤを履(は)き替(か)える = change tyres. Car metaphor: engine limit-a thaanda mudiyaadhu, aanaa tyres maathi, driving technique improve panni speed koottalaam.",
   "比喩: 車 = runner, エンジン = born-with body (体質), tyres/technique = various efforts (工夫).",
  ], src="為末大『日本人の足を速くする』新潮社"),
  toi("d4d-r11", "この文章で筆者が最も言いたいことは何か。", [
   "車の速さは、エンジンの性能によって決まる。",
   "足が速いか遅いかは、生まれながらにして決まっている。",
   "車のスピードをアップさせる方法は、いろいろある。",
   "足が遅いと思っている人も、工夫すればもっと速くなれる。"], 3,
   ["Answer 4. Car (metaphor) → runner: even slow runners can get faster with effort (工夫 くふう).",
    "1, 3: car = metaphor. 2: partly true but writer's main point is 'there are ways to speed up'."]),
  kaisetsu(11, ["走るスピードを上げることについて書かれた文章である。", "比喩に注目する。",
   "車＝走る人、エンジン＝生まれ持った質（体質）", "タイヤを履き替えたり、運転テクニックを上達させたりすること＝さまざまな工夫", "工夫をすることで、走るスピードを上げることができる。",
   "1：車の性能は比喩で、この文章のテーマではない。", "2：足の速さは生まれながらにしてかなりの部分まで決まっているが、スピードアップさせる方法があることを主張している。",
   "3：車のスピードは比喩で、この文章のテーマではない。", "4：正解"]),

  passage("練習12　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "なんかの本で読んだ話。ある山の{麓|ふもと}（注1）で、おじいさんと孫が、{山鳩|やまばと}（注2）の{雛|ひな}（注3）を育てていた。その山の反対側に、別のおじいさんと孫がいて、こっちは{鷹|たか}（注4）の{雛|ひな}を育てていた。それぞれの{雛|ひな}が成長して、飛べるようになったんで、ある日、空に放してやった。そしたら、{鷹|たか}が{山鳩|やまばと}を食べてしまった。山のこっち側では、{山鳩|やまばと}が{喰|く}われたって泣いた。向こう側では、{鷹|たか}がはじめて{餌|えさ}を{獲|と}ったって喜んだ。ひとつの現象なのに、山のこっちと向こうでは、まるっきり正反対のことが起きたってことになる。",
   "{妙|みょう}な話だけど、人生の喜びや悲しみは、{根本的|こんぽんてき}にそういうものだ。この世で起きることには、本来、何の色も{着|つ}いていない。",
   "そこに、喜びだの悲しみだのの色を{着|つ}けるのは人間だ。",
  ], [
   "Para 1: 麓(ふもと) = foot of a mountain. 孫(まご) = grandchild. 山鳩(やまばと) = wild dove. 雛(ひな) = chick. 鷹(たか) = hawk. 放(はな)す = release. 喰(く)われる = be eaten. 餌(えさ)を獲(と)る = catch prey. 現象(げんしょう) = phenomenon. まるっきり = completely.",
   "Story: Malai oru pakkam dove valarththaanga, innoru pakkam hawk. Hawk dove-a saapittudhu. Oru side azhudhaanga, innoru side 'first hunt!'-nu sandhosham. Same event, opposite feelings.",
   "Para 2–3: 妙(みょう)な = strange. 根本的(こんぽんてき)に = fundamentally. 本来(ほんらい) = originally. Life events-ku colour illa; sandhosham/dukkam colour podradhu manushan dhaan.",
   "比喩: birds story = one fact; each side sees it differently (立場によって見方が違う).",
  ], notes=["（注1）{麓|ふもと}：山の下の部分", "（注2）{山鳩|やまばと}：山に住む鳥", "（注3）{雛|ひな}：鳥の子供", "（注4）{鷹|たか}：肉食の鳥で、{山鳩|やまばと}より大きい"], src="北野武『全思考』幻冬舎"),
  toi("d4d-r12", "この文章の内容として最も適切なものはどれか。", [
   "住んでいるところが変われば、同じ現象でも違って見えるものだ。",
   "人生にうれしいことも悲しいこともあるのは、しかたがないことだ。",
   "いくら人が喜んだり悲しんだりしても、起きたことはどうすることもできない。",
   "世の中で起きる物事は、立場によって見え方や意味が変わってくる。"], 3,
   ["Answer 4. One event, two sides, opposite meanings → 立場(たちば, standpoint)によって見え方が変わる.",
    "1 trap: 'where you live' = the mountain sides = metaphor. 2: 'can't be helped' ezhudhala. 3: 'can't do anything' illa — how you SEE it is the point."]),
  kaisetsu(12, ["人生の喜びや悲しみについて書かれた文章である。", "比喩に注目する。",
   "鷹が山鳩を食べたという一つのことに対して、ある人は喜び、ある人は泣く＝ある一つの事実について、立場により見方が違う。",
   "1：「住んでいるところ」は比喩で、この文章のテーマではない。", "2：しかたがないとは書かれていない。この世で起きることをどう見るかが人により違うと書かれている。",
   "3：起きたことをどうするかではなく、どう見るかについて書かれている。", "4：正解"]),

  items("◆疑問提示文とは", [
   ("疑問提示文とは、これから何について述べるかを、疑問文を使って示している文である。疑問の答えを探そう。",
    "疑問提示文(ぎもんていじぶん) = a question the writer asks to introduce the topic. Writer-e question kettu, appram answer solluvaar. Andha answer dhaan main point!"),
   ("種類：疑問詞疑問文（「なぜ・どうして・いつ・どこで・どのようにして…」がつく。）\nYes-No疑問文（疑問詞はない。文末が「～だろうか。」「～(の)か。」）",
    "Rendu type: question-word type (なぜ, どうして, いつ, どこで, どのように) and Yes-No type (ending ～だろうか / ～のか, no question word)."),
  ]),

  passage("☆例題7　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "リーダーたるもの、必要であればメンバーを{怒|おこ}ることからも逃げてはならない。{締|し}めるところを{締|し}めてこそチームの結束も強まるものだ。",
   "ではリーダーは、メンバーの何を{怒|おこ}ればいいのか。",
   "いちばん最悪なのは、相手の人格を否定する{怒|おこ}り方だ。「だからお前はダメなんだ！」などと{怒鳴|どな}っても、ことは何ひとつ進展しない。{怒|おこ}るのはあくまでも、仕事への取り組みについてであるべきだ。",
   "とはいえ仕事のミス自体を「何をしているんだ！」とただ{叱咤|しった}（注1）するのもいただけない。リーダーならばメンバーのミスについては、なぜミスが起きたのかをまず分析したい（この点は後述する）。",
   "リーダーが本気で{怒|おこ}るべきは、メンバーの仕事に対する「意識」や「姿勢」に甘さが見えたときだ。",
   "たとえば、ある人が同じミスを何度も繰り返したときや、周りに協力を{仰|あお}がねばならないのに本人が消極的なとき。口だけで行動がともなっていないときや下を育てる立場にいながら、後輩の力不足を{嘆|なげ}いているだけのとき（そこを伸ばすのが自分の使命だとわかっていない）。（中略）",
   "もちろん{怒|おこ}れば自分自身も気分はよくないし、相手もいったんは完全にしょげてしまう。だが、あなたが手を抜かずに本気で{怒|おこ}れば、相手もあなたの想いを{汲|く}み{取|と}って必ず{奮起|ふんき}して（注2）くれる。",
  ], [
   "Para 1: ～たるもの = as a (leader), one should. 怒(おこ)る = scold. 締(し)める = tighten. 結束(けっそく) = unity. Leader-na thevai-na scold pannanum.",
   "Para 2 = 疑問提示文! 'Leader member-oda ENNA-va scold pannanum?' Answer-a thedunga.",
   "Para 3: 最悪(さいあく) = worst. 人格(じんかく) = personality. 否定(ひてい) = deny. 怒鳴(どな)る = yell. 進展(しんてん) = progress. 取(と)り組(く)み = approach to work.",
   "Para 4: 叱咤(しった) = loud scolding. いただけない = not good. 分析(ぶんせき) = analyse. 後述(こうじゅつ) = described later.",
   "Para 5 = answer: 意識(いしき) (awareness) and 姿勢(しせい) (attitude) to work-la 甘(あま)さ (laxness) theriyumbodhu.",
   "Para 6–7: 仰(あお)ぐ = ask for. 消極的(しょうきょくてき) = passive. 後輩(こうはい) = juniors. 嘆(なげ)く = lament. 使命(しめい) = mission. しょげる = be dejected. 手を抜(ぬ)く = cut corners. 汲(く)み取(と)る = understand. 奮起(ふんき) = be roused.",
  ], notes=["（注1）{叱咤|しった}：大声で{叱|しか}る", "（注2）{奮起|ふんき}する：やる気を出す"], src="藤巻幸夫『フジマキ流　アツイチームをつくる　チームリーダーの教科書』インデックス・コミュニケーションズ"),
  toi("d4d-e7", "この文章で筆者が最も言いたいことは何か。", [
   "リーダーはメンバーの取り組んでいる仕事におけるミスだけを取り上げて怒るべきだ。",
   "リーダーはメンバーの仕事に対する取り組みに真剣さが足りないことを怒るべきだ。",
   "リーダーはメンバーの、消極的とか、そそっかしい等の性格について怒るべきだ。",
   "リーダーは、メンバーが怒られた後がっかりして立ち直れなくなることを怒るべきだ。"], 1,
   ["Answer 2. 疑問: 'what to scold?' → answer: 意識・姿勢に甘さ = 真剣さが足りない (paraphrase!).",
    "1: mistakes → first analyse, don't just scold. 3: personality → 最悪. 4: not written."]),
  {"type": "reveal", "label": "本の解説：全体をつかもう（例題7）", "children": [
   items("1）キーワードからテーマを推測する", [("リーダー、メンバー、怒る、「意識」、「姿勢」　→　テーマは、リーダーがメンバーを怒ること？", "Topic = leader scolding members.")]),
   items("2）「疑問提示文」に注目する", [
     ("「疑問提示文」とその答えを探す。", "Find the question and its answer."),
     ("疑問提示文：第2段落「リーダーは、メンバーの何を怒ればいいのか。」", "The question is in paragraph 2."),
   ]),
   {"type": "table", "title": "答え", "rows": [
     ["第3段落：相手の人格", "→", "最悪"],
     ["第4段落：仕事のミス自体", "→", "いただけない（＝よくない）"],
     ["第5段落：仕事に対する意識・姿勢に甘さ", "→", "本気で怒るべき"],
   ], "explain": "Moonu options writer check panraar: personality = worst, mistake itself = not good, laxness in attitude = scold seriously. Last one dhaan answer."},
   items("3）全体をまとめる", [("リーダーは、メンバーの仕事に対する意識・姿勢に甘さが見えたとき、本気で怒るべきだ。", "Summary.")]),
   items("選択肢と比べよう", [T("1：リーダーなら「なぜミスが起きたのかをまず分析したい」と書かれている。"), T("2：正解（仕事に対する取り組みに真剣さが足りない＝意識や姿勢が甘い）"),
     T("3：「人格を否定する怒り方」は「最悪」だと書かれている。"), T("4：立ち直れなくなることを怒るべきとは書かれていない。本気で怒れば「必ず奮起」すると書かれている。")]),
  ]},

  text("Ippo 疑問提示文 practice. Ovvoru passage-layum: (1) writer kekkura question (～だろうか／～のでしょうか／なぜ) kandupudinga, (2) adhoda answer thedunga — adhu dhaan correct option.", "🎓 練習13～16"),

  passage("練習13　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "今の日本人の欲望は{留|とど}まるところを知りません。常に新しい物を欲しがる。{美味|おい}しい{物|もの}ばかりに{目移|めうつ}りする。{身|み}の{丈|たけ}（注1）以上の生活を求め続けている。そして子供には過度の期待をかけ、能力以上の成果を望む。果たしてそこに本当の幸福があるのでしょうか。",
   "ほんのつい最近まで、日本人は{身|み}の{丈|たけ}に合った{慎|つつ}ましい（注2）生活を送っていました。少なくとも私が{幼少|ようしょう}の{頃|ころ}はそうでした。{背伸|せの}びをすることなく、不満を口にすることなく、{慎|つつ}ましい暮らしの幸せを感じていました。",
   "かつてのような貧しい暮らしが良いというのではありません。ただ、{身|み}の{丈|たけ}に合わない生活には、きっと大きな{落|お}とし{穴|あな}がある。そんな気がするのです。",
  ], [
   "Para 1: 欲望(よくぼう) = desire. 留(とど)まるところを知らない = knows no limit. 目移(めうつ)り = eyes wandering. 身(み)の丈(たけ) = one's height → one's means. 過度(かど) = excessive. 成果(せいか) = results. 果(は)たして…でしょうか = 疑問提示文!",
   "Para 2: 慎(つつ)ましい = modest. 幼少(ようしょう)の頃(ころ) = childhood. 背伸(せの)び = stretching (living beyond means).",
   "Para 3 = answer: 落(お)とし穴(あな) = pitfall. Means-ku meeriya life-la periya pitfall irukkum.",
  ], notes=["（注1）{身|み}の{丈|たけ}：身長", "（注2）{慎|つつ}ましい：ぜいたくでない"], src="山田洋次「わたしの幸福論」『PHP No.679』PHP研究所"),
  toi("d4d-r13", "この文章で筆者が最も言いたいことは何か。", [
   "昔は貧しかったが、今は欲しい物が何でも手に入り、現代の日本人は幸福である。",
   "少し前まで日本人は貧しい暮らしをしていて、あまり幸福とは言えなかった。",
   "今の日本人は背伸びして良い生活を求めているが、それでは幸福になれないだろう。",
   "筆者が子供の頃は、自分の生活に満足しながら生活していて、幸福だった。"], 2,
   ["Answer 3. Question: 'Is there real happiness there?' → Answer: 身の丈に合わない生活には落とし穴 = can't be happy.",
    "1: writer doubts it. 2: opposite — they were happy. 4: true detail, but only used as contrast."]),
  kaisetsu(13, ["身の丈以上の生活を求めることに本当の幸福があるのかについて書かれた文章である。",
   "疑問提示文に注目する。疑問提示文は「果たしてそこに本当の幸福があるのでしょうか。」である。", "「そこ」＝今の日本人が身の丈（自分の財力・能力）以上の生活を求めていること",
   "疑問提示文の答えは、「身の丈に合わない生活には、きっと大きな落とし穴がある。」である。",
   "1：現代の日本人は幸福であるとは書かれていない。疑問に思っている。", "2：少し前の日本人があまり幸福ではなかったとは書かれていない。幸せだったとある。",
   "3：正解", "4：筆者の子供の頃の話は、今の日本人との違いを対比するためだけに書かれている。"]),

  passage("練習14　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "みなさんは、そもそも何のために文章を書くのでしょうか。",
   "もし、私自身が同じ質問を受けたら、「自分を表現し、{他者|たしゃ}と{関|かか}わりながら生きていくため」と答えます。学校の教科書や参考書をいくら読んでも、それだけでは{他者|たしゃ}との{関|かか}わりは生まれてきません。知識として知ることと{他者|たしゃ}と{関|かか}わるということは、{質的|しつてき}に全く別{次元|じげん}のことだからです。知識をいくら{積|つ}み{重|かさ}ねても、{他者|たしゃ}と{関|かか}わることは永遠にできないでしょう。",
   "理解し感動したことや{一生懸命|いっしょうけんめい}に考えたことを、{拙|つたな}くても（注1）いいから、{試行錯誤|しこうさくご}（注2）しながらでもいいから、{誰|だれ}かにきちんと「伝える」練習をしてみましょう。それは、きっと社会に働きかけ、他の人々と共に生きていく練習にもなるでしょう。「書く」という{行為|こうい}は、静かに自分の{内面|ないめん}を見つめることでありながら、同時に社会に向けて行動する第一歩にもなり得るのです。",
  ], [
   "Para 1 = 疑問提示文: そもそも = in the first place. 'Edhukkaaga ezhudhurom?'",
   "Para 2 = answer: 表現(ひょうげん) = express. 他者(たしゃ) = others. 関(かか)わる = relate to. 参考書(さんこうしょ) = reference book. 質的(しつてき) = qualitatively. 別次元(べつじげん) = different dimension. 積(つ)み重(かさ)ねる = pile up. 永遠(えいえん) = forever.",
   "Para 3: 拙(つたな)い = clumsy. 試行錯誤(しこうさくご) = trial and error. 働(はたら)きかける = act on. 行為(こうい) = act. 内面(ないめん) = inner self. ～得(う)る = can.",
  ], notes=["（注1）{拙|つたな}い：下手だ", "（注2）{試行錯誤|しこうさくご}：いろいろやってみて失敗しながら目的に近づいていくこと"], src="原和久『創作力トレーニング』岩波書店"),
  toi("d4d-r14", "この文章で筆者が最も言いたいことは何か。", [
   "書くときには「何のために文章を書くのか」をよく考えることが大切だ。",
   "書くことは、誰かにきちんと「伝え」、社会に向けて行動することにつながる。",
   "教科書や参考書で勉強しても、知識が増えるだけで、書くことは上手にならない。",
   "書くことによって人は成長し、自分の内面を見つめられるようになる。"], 1,
   ["Answer 2. Question 'why write?' → answer: to express yourself and connect with others = 伝える + 社会に向けて行動する.",
    "1: the question itself, not the answer. 3: not about getting good at writing. 4: 'grow' not written; and not ONLY the inner self."]),
  kaisetsu(14, ["文章を書くことについて書かれた文章である。",
   "疑問提示文に注目する。疑問提示文は「みなさんは、そもそも何のために文章を書くのでしょうか。」である。その答えは、「自分を表現し、他者と関わりながら生きていくため」、つまり、だれかにきちんと伝え、社会に働きかけて、ほかの人々と共に生きていくためである。",
   "1：よく考えることが大切だとは書かれていない。", "2：正解", "3：教科書や参考書の知識と書くことが上手になることとどう関係するかは書かれていない。",
   "4：書くことで成長するとは書かれていない。また、内面を見つめることだけでなく、社会に向けて行動することにもなると書かれている。"]),

  passage("練習15　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "日本で生活している留学生の多くが、「日本人は家族の関係が{薄|うす}い」という感想を{抱|いだ}くようだ。{一人暮|ひとりぐ}らしをしている大学生があまり家族と連絡をとらないことや、老人ホームなどの施設で暮らすお年寄りが多いことなどから、そう感じるらしい。「経済が発展した結果、昔は強かった家族の人間関係が、だんだん{薄|うす}く、冷たくなったのだ」という意見もよく聞く。本当にそうなのだろうか。",
   "ある全国調査によると、「あなたにとって何がいちばん大切ですか」という質問に対して「家族」と答えた人の割合は、1978年が23%、1988年が33%、1998年が40%、2008年が46%だった。家族がいちばん大切だと言う考えの人が30年で倍になったことがわかる。",
   "一方、「職場の{同僚|どうりょう}とのつきあい」「{隣近所|となりきんじょ}の人とのつきあい」「親せき」について、「相談したり助けあったりできる関係」にあることが望ましいかどうかを聞いたところ、すべての項目において、「望ましい」と答える人の割合は減少傾向にあった。",
  ], [
   "Para 1: 感想(かんそう)を抱(いだ)く = have an impression. 施設(しせつ) = facility. 経済(けいざい) = economy. 発展(はってん) = development. 本当にそうなのだろうか = 疑問提示文 (Yes-No type).",
   "Para 2 = answer part 1: 割合(わりあい) = proportion. 倍(ばい) = double. 'Family most important' 23% → 46% — family ties weaker aagala!",
   "Para 3 = part 2: 同僚(どうりょう) = colleagues. 隣近所(となりきんじょ) = neighbours. 望(のぞ)ましい = desirable. 項目(こうもく) = item. 減少傾向(げんしょうけいこう) = decreasing trend. Office, neighbours, relatives kooda close relation venum-nu solravanga kammi.",
  ]),
  toi("d4d-r15", "この文章の内容として最も適切なものはどれか。", [
   "職場や地域、親せきとのつきあいは薄れているが、家族関係を重視する人の割合が高まっている。",
   "経済発展をしても、家族関係や、職場や地域、親せきとの関係の強さはあまり変わっていない。",
   "年とともに、職場や地域、親せきとの関係は強まりつつあるが、家族を大切に思う人の割合は増えていない。",
   "家族関係だけでなく、職場や地域、親せき関係を重視する人の割合もすべて低下してきている。"], 0,
   ["Answer 1. Family value ↑ (23% → 46%), other relationships ↓.",
    "2: other relationships did change (weaker). 3: opposite of both. 4: family value went UP, not down."]),
  kaisetsu(15, ["日本人の家族関係について書かれた文章である。",
   "疑問提示文に注目する。疑問提示文は、「昔は強かった家族の人間関係が、だんだん薄く、冷たくなったのだ」「本当にそうなのだろうか。」である。その答えとして、「家族がいちばん大切だ」という考えの人が30年で倍になった、つまり、家族関係が冷たくなったのではないということが読み取れる。一方で、「職場の同僚、隣近所の人、親せきとのつきあいについて、相談したり助けあったりできる関係が望ましい」と答える人の割合は減少した。",
   "1：正解", "2：職場や地域、親せきとの関係は薄くなっている。", "3：職場や地域、親せきとの関係は強まっていない。家族を大切に思う人の割合は増えていないとは書かれていない。",
   "4：家族関係を重視する人の割合は低下しているのではなく、高まっている。"]),

  passage("練習16　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "目の前の相手が悲しんでいるとき、その自分の感情を思い出していただきたい。{同情|どうじょう}とか、{共感|きょうかん}とか、力になってやりたいといった気持ちが起こるだろう。また、人に親切にしたときや贈り物をしたときなど、相手がうれしそうな表情やしぐさをして、喜んでいるとわかれば、自分もうれしくなるだろう。このようにして相手の感情がわかり、それに対して{共感|きょうかん}する気持ちが生まれれば、それは相手に対する{好感情|こうかんじょう}につながる。",
   "だが、喜んでいるのか悲しんでいるのか、さっぱりわからない人の場合はどうだろうか。その人にどう{接|せっ}していいかわからず、{共感|きょうかん}する気持ちもわかない。なんとなく{敬遠|けいえん}（注1）したくなるのではないだろうか。（中略）",
   "とくに若い世代は、感情を{表|おもて}にあらわさない人に対して、「わからない人」という評価を下し{敬遠|けいえん}しがちだ。そのため、人と話すときに自分の感情をうまくあらわせない少年少女は、クラスメートたちから{仲間|なかま}はずれにされやすく、ときにはいじめられっ子になったりもする。感情をうまく{表|おもて}にあらわせない人は、対人関係が悪くなりやすいのである。",
  ], [
   "Para 1: 同情(どうじょう) = sympathy. 共感(きょうかん) = empathy. 贈(おく)り物(もの) = gift. 表情(ひょうじょう) = facial expression. しぐさ = gesture. 好感情(こうかんじょう) = good feeling. Feelings theriyumbodhu empathy varum → like pannuvom.",
   "Para 2 = 疑問提示文: 'Sandhoshama dukkama-nu theriyaadha aal-na eppadi?' 接(せっ)する = deal with. 敬遠(けいえん) = keep at a distance.",
   "Para 3 = answer: 表(おもて)にあらわす = show outwardly. 評価(ひょうか)を下(くだ)す = judge. 仲間(なかま)はずれ = left out. 対人関係(たいじんかんけい) = relationships with people. Feelings kaattaadhavanga relationships kettu pogum.",
  ], notes=["（注1）{敬遠|けいえん}：{嫌|いや}がって避けること"], src="本明寛『なぜ電車の席は両端が人気なのか――行動の心理学』双葉社"),
  toi("d4d-r16", "この文章で筆者が最も言いたいことは何か。", [
   "相手の感情がわからない人は、仲間はずれにされたりいじめられたりする。",
   "自分の感情を相手に対して上手に出していけば、良い人間関係を作りやすい。",
   "目の前にいる人が自分の気持ちに共感してくれないと、その人との関係が悪くなる。",
   "感情を{表|おもて}に出さない人より、{表|おもて}に出す人のほうが人間関係で問題が起きやすい。"], 1,
   ["Answer 2. Answer to the question: people who can't show feelings → bad relationships. Flip side: show feelings well → good relationships.",
    "1: it's people who can't SHOW feelings, not who can't READ them. 3: reversed. 4: opposite."]),
  kaisetsu(16, ["自分の感情を{表|おもて}に出すということについて書かれた文章である。",
   "疑問提示文に注目する。疑問提示文は、「喜んでいるのか悲しんでいるのか、さっぱりわからない人の場合はどうだろうか。」で、その答えは、「感情をうまく{表|おもて}にあらわせない人は、対人関係が悪くなりやすい」である。",
   "1：仲間はずれにされたりいじめられたりするのは、自分の感情をうまくあらわせない人であって、相手の感情がわからない人ではない。", "2：正解",
   "3：目の前にいる人が自分の気持ちに共感してくれないのではなく、目の前にいる人に自分の気持ちを出さないと、相手は共感できない。", "4：感情を{表|おもて}に出さない人のほうが人間関係で問題が起きやすい。"]),
 ],
}
