from _h import *
DAY = 16

def R(form, example, ka, explain):
    return {"t": "**%s**　%s　（%s）" % (form, example, ka), "explain": explain}

def FB(id, q, ans, explain):
    return fill(id, q, ans if isinstance(ans, list) else [ans], explain)

def PICK(id, q, opts, ans, explain, keys):
    return mcq(id, q, opts, ans, explain, keys=keys)

ABCD = ["a", "b", "c", "d"]
AB = ["a", "b"]
N4 = ["1", "2", "3", "4"]

# ================= E 「わけ・ところ」を使った言い方 (pp.132–133) =================
E = [
 text("N2の文法形式には「わけ」「ところ」を使ったものがあります。整理しておきましょう。（＊はここで初めて学習する文法形式）",
  title="Ⅳ 文法形式の整理　E 「わけ・ところ」を使った言い方",
  explain=["Sensei: わけ and ところ make lots of N2 forms that look alike. Today we line them up side by side so you stop mixing them.",
           "Thanglish: わけ = reason / logical conclusion. ところ = point, moment, situation. どころ = 'far from…'. Indha moonu-um exam-la confuse pannum — table-a nalla paarunga.",
           "Two new forms today (＊): ～わけだ／～というわけだ and ～ところから／～ことから."]),
 items("わけ", [
  R("～わけがない", "こんなに重い物を一人で運べるわけがない。", "12課", "わけがない = there's no way. There's no way one person can carry something this heavy."),
  R("～わけではない／～というわけではない", "いつでも電話に出られるわけではない。／ペンならどれでも同じというわけではない。", "12課", "わけではない = it's not that… (partial denial). I can't always answer the phone. / It's not true that any pen is the same."),
  R("～わけにはいかない", "今日は試験なので、休むわけにはいかない。", "18課", "わけにはいかない = can't (for social / moral reasons). There's an exam today, so I can't take the day off."),
  R("～ないわけに(は)いかない", "妹の結婚式に出席しないわけにはいかない。", "25課", "ないわけにはいかない = must, can't not. I can't not attend my sister's wedding."),
  R("＊～わけだ／～というわけだ", "そんなに残業しているんですか。それでは疲れるわけですよ。", "＊", "NEW: わけだ = no wonder / so naturally… (a logical result). See the teach panel below."),
 ]),
 items("ところ", [
  R("～どころではない／～どころか", "連休中も休むどころではなく、毎日残業だ。／部屋の中は涼しいどころか、35度もあった。", "12課", "どころではない = it's no time for…; どころか = far from…, actually the opposite. Far from cool, the room was 35 degrees!"),
  R("～どころではない", "眠くて仕事どころではない。", "18課", "noun + どころではない = can't possibly think about (work) because of something else. I'm so sleepy, work is out of the question."),
  R("～たところ", "メールを送ったところ、すぐに返事が来た。", "20課", "たところ = when I did…, (result). When I sent an email, a reply came at once."),
  R("～ところだった", "もう少しで車にぶつかるところだった。", "20課", "ところだった = almost… (but didn't). I nearly hit a car."),
  R("＊～ところから／～ことから", "この木は雪がかかったように花が咲くところから、「雪柳」という名前がついた。", "＊", "NEW: ところから／ことから = from the fact that… (the basis for a name or judgement). See the teach panel below."),
 ]),
 gram("＊1", "d16b-wakeda", "～わけだ・～というわけだ", "当然そういうことになる。",
  ["わけだ = so naturally…, no wonder… You hear a fact, and you say the result that logically follows.",
   "'Avan romba overtime panraan — adhaan tired-aa irukkaan!' → そんなに残業しているんですか。それでは疲れるわけですよ。",
   "Also used for maths-like conclusions: 1人1,500円 × 7人 = 1万500円になるわけですね.",
   "というわけだ is the same, often when you sum up: 'so that's why it's cheap' → それで安いというわけですね."],
  "普通形（ナ形 だ→な／である・名 だ→の／な／である）＋わけだ　普通形（ナ形(だ)・名(だ)）＋というわけだ",
  [ex("そんなに残業しているんですか。それでは疲れるわけですよ。", "Avlo overtime-aa? Appo tired-aa irukradhu sahajam dhaan."),
   ex("会費は1人1,500円です。ということは7人で1万500円になるわけですね。", "Oru aalukku 1,500 yen. Appo 7 per-ku 10,500 yen aagum, illaiyaa?"),
   ex("産地直送ですか。それで安いというわけですね。", "Farm-la irundhu direct-aa varudhaa? Adhaan vilai kammi-aa irukku!")],
  [("雨が降っているわけだから、傘を貸してください。", "雨が降っているから、傘を貸してください。",
    "わけだ is a conclusion you reach from facts. For a simple reason + request, use から.")],
  [("田中さんは10年もアメリカに住んでいたんですか。英語が上手な（　　）。", ["わけだ", "わけがない", "わけにはいかない"], 0, "Fact (lived in the US 10 years) → natural result → わけだ.")],
  ["～わけだ = naturally / no wonder (a result that follows from facts).",
   "Shape: plain form + わけだ (ナ形 → な, 名 → の／な／である); plain form + というわけだ.",
   "Kavanam: the speaker has just understood or calculated something."],
  [("①そんなに残業しているんですか。それでは疲れる[[わけです]]よ。", "You're doing that much overtime? No wonder you're tired."),
   ("②会費は1人1,500円です。ということは7人で1万500円になる[[わけです]]ね。", "The fee is ¥1,500 each. So for seven people that makes ¥10,500."),
   ("③産地直送ですか。それで安い[[というわけです]]ね。", "Straight from the farm? So that's why it's cheap.")],
  "普通形（ナ形 だ→な／である・名 だ→の／な／である）＋わけだ\n普通形（ナ形(だ)・名(だ)）＋というわけだ",
  "前の文や状況から、当然の結果として言う。"),
 gram("＊2", "d16b-tokorokara", "～ところから・～ことから", "ある出来事の直接の原因や、判断や決定の根拠を言う。",
  ["ところから／ことから = from the fact that…, because… — gives the basis for a name, a judgement or a decision.",
   "'Snow vizhundha maadhiri pookkal pookkradhaala, adhukku 雪柳 nu per vandhuchu' → 雪がかかったように花が咲くところから、「雪柳」という名前がついた.",
   "Very common in explanations of names and origins: ～ことから、～と呼ばれるようになった."],
  "普通形（ナ形 だ→な／である・名 だ→である）＋ところから・ことから",
  [ex("この木は雪がかかったように花が咲くところから、「雪柳」という名前がついた。", "Indha maraththula snow pottadhu maadhiri pookkal pookkudhu — adhanaala 'yuki-yanagi' nu per."),
   ex("同じ町の出身だとわかったことから、彼女と親しくなった。", "Rendu perum ore ooru-nu therinjadhaala, aval kooda close aayitten."),
   ex("顔がとてもよく似ていることから、二人は兄弟だとすぐにわかった。", "Mugam romba same-aa irundhadhaala, avanga brothers-nu udane purinjiduchu.")],
  [("おなかがすいたことから、ご飯を食べた。", "おなかがすいたから、ご飯を食べた。",
    "ことから is for a basis of a name / judgement / decision in a formal explanation. Everyday 'because I was hungry' → から.")],
  [("形が琵琶という楽器に似ている（　　）、琵琶湖という名前がつけられた。", ["ことから", "わけだから", "どころか"], 0, "Basis for a name → ことから／ところから.")],
  ["～ところから・～ことから = from the fact that (reason for a name / judgement / decision).",
   "Shape: plain form + ところから／ことから (ナ形 → な／である, 名 → である).",
   "Kavanam: explanatory, a little formal; not for everyday reasons."],
  [("①この木は雪がかかったように花が咲く[[ところから]]、「{雪柳|ゆきやなぎ}」という名前がついた。", "Because its flowers bloom as if covered in snow, this tree was named 'snow willow'."),
   ("②同じ町の出身だとわかった[[ことから]]、彼女と親しくなった。", "When we found we came from the same town, we became close."),
   ("③顔がとてもよく似ている[[ことから]]、二人は兄弟だとすぐにわかった。", "Their faces were so alike that I knew at once they were brothers.")],
  "普通形（ナ形 だ→な／である・名 だ→である）＋ところから・ことから",
  "名前の由来や、判断・決定の根拠を説明するときによく使う。"),
 group("練習1　適当なものを選びなさい。", [
  PICK("d16b-e1-1", "1　日本で{就職|しゅうしょく}活動をしなければならないので、今年の夏は国へ（　）。", ["帰るわけにはいかない","帰らないわけにはいかない","帰るわけではない","帰らないわけではない"], 0, "I have to job-hunt in Japan → I can't go home → 帰るわけにはいかない.", ABCD),
  PICK("d16b-e1-2", "2　{普段|ふだん}は外食が多いが、料理が（　）。忙しいのだ。", ["できるわけにはいかない","できないわけにはいかない","できるわけではない","できないわけではない"], 3, "It's not that I CAN'T cook — I'm just busy → できないわけではない.", ABCD),
  PICK("d16b-e1-3", "3　ダイエットを始めたが、やせる（　）{逆|ぎゃく}に太ってしまった。", ["ところが","どころか","ところで","どころで"], 1, "Far from losing weight, I gained → どころか.", ABCD),
  PICK("d16b-e1-4", "4　新聞の広告を見てさっそく商品を注文した（　）、すぐに商品が送られてきた。", ["ところで","ところを","ところ","ところが"], 2, "When I ordered, (result) it arrived at once → たところ.", ABCD),
  PICK("d16b-e1-5", "5　子供の時に1度会っただけの人の顔を（　）。", ["覚えているわけにはいかない","覚えているわけがない","覚えていないわけではない","覚えていないわけだ"], 1, "There's no way I'd remember a face I saw once as a child → わけがない.", ABCD),
  PICK("d16b-e1-6", "6　駅にあと1分遅く着いたら、電車に（　）。", ["乗れないところだった","乗れるどころではなかった","乗れないわけだった","乗れるわけではなかった"], 0, "One minute later and I'd have missed it (but didn't) → ところだった.", ABCD),
 ], lead="Key (別冊 p.6): 1a 2d 3b 4c 5b 6a."),
 group("練習2　「ところ」か「どころ」か「わけ」を＿＿の上に書きなさい。", [
  FB("d16b-e2-1", "1　前にその本を買ったことをすっかり忘れて、もう一冊買ってしまう%%だった。", "ところ", "ところだった = almost did (but didn't)."),
  FB("d16b-e2-2", "2　今は働いていないが、働きたくない%%ではない。", "わけ", "わけではない = it's not that I don't want to work."),
  FB("d16b-e2-3", "3　バスはすいている%%か、{超満員|ちょうまんいん}だった。", "どころ", "どころか = far from empty, it was packed."),
  FB("d16b-e2-4", "4　{琵琶湖|びわこ}の名は、形が{琵琶|びわ}という楽器に似ている%%からつけられた。", "ところ", "ところから = from the fact that (origin of a name)."),
  FB("d16b-e2-5", "5　飛行機は朝早いですが、眠ければ機内で寝てしまえばいい%%ですから、大丈夫です。", "わけ", "わけだ = so naturally (logically) you can just sleep."),
  FB("d16b-e2-6", "6　このココア、そんなに砂糖が入っているんですか。{道理|どうり}で甘い%%だ。", "わけ", "道理で～わけだ = no wonder it's sweet."),
 ], lead="Key (別冊 p.6): 1ところ 2わけ 3どころ 4ところ 5わけ 6わけ."),
]

# ================= F 二つの言葉を組にする言い方・助詞 (pp.134–135) =================
F = [
 text("N2の文法形式には、同じ言葉、対になる言葉を2回重ねて言う表現があります。同じ言葉を重ねるのは、主に例を挙げるものです。また、特別な使い方の助詞も整理しましょう。（＊はここで初めて学習する文法形式）",
  title="Ⅳ 文法形式の整理　F 二つの言葉を組にする言い方・助詞",
  explain=["Sensei: Some N2 forms come in pairs: ～やら～やら, ～だの～だの, ～か～ないかのうちに. Most of them list examples.",
           "Thanglish: rendu examples solli 'idhu, adhu ellaam…' nu solra style. Each pair has its own feeling — やら = and so on (busy, mixed), だの = complaining, というか = 'or should I say…'.",
           "Also a table of particles with special meanings: とは, ぐらい, なんか, まで, として～ない, さえ, and the new ＊ のみ."]),
 items("二つの言葉を組にする言い方", [
  R("～やら～やら", "四角いものやら丸いものやらいろいろな形の皿がある。", "10課", "やら～やら = things like A and B (a mixed bunch). There are plates of all shapes, square ones, round ones…"),
  R("～というか～というか", "このクラスはうるさいというかにぎやかというか……。", "10課", "というか～というか = I'd call it A, or maybe B… (hard to describe). This class is noisy, or lively, or…"),
  R("～にしても～にしても／～にしろ～にしろ／～にせよ～にせよ", "野菜にしても魚にしても、材料は新鮮なほうがいい。", "10課", "A にしても B にしても = whether A or B, either way. Whether vegetables or fish, fresh is better."),
  R("＊～だの～だの", "弟の部屋は、紙くずだの空きかんだのでいっぱいだ。", "＊", "NEW: だの～だの = A and B and such (fed-up tone). See the teach panel below."),
  R("～か～ないかのうちに", "夜が明けたか明けないかのうちに家を出た。", "1課", "か～ないかのうちに = the moment that…, almost at the same time. I left home just as dawn was breaking."),
  R("～(よ)うか～まいか", "旅行に行こうか行くまいか迷っている。", "24課", "(よ)うか～まいか = whether to do or not. I can't decide whether to go on the trip."),
 ]),
 items("助詞", [
  R("とは　～とは", "留学とは外国で勉強することだ。", "13課", "とは = (definition) ～ means… Studying abroad means studying in another country."),
  R("ぐらい・くらい　～ぐらい・～くらい", "わからない言葉ぐらい調べてきなさい。", "21課", "ぐらい = at least (this minimum). At least look up the words you don't know before class."),
  R("など・なんか・なんて", "医者になんかならなければよかった。", "21課", "なんか = (looking down on it) the likes of… I wish I'd never become a doctor."),
  R("まで　～まで・～までして", "この山小屋には電子レンジまである。／借金までして車を買うんですか。", "21課", "まで = even (surprising extreme). This mountain hut even has a microwave. / You'd even borrow money to buy a car?"),
  R("として　～として～ない", "この寒さには1日として我慢できない。", "21課", "1日として～ない = not even one day. I can't stand this cold for even a single day."),
  R("さえ　～さえ", "のどが痛くておかゆさえ食べられない。／お金さえあれば、この困難を乗り切れる。", "21課", "さえ = even; さえ～ば = if only. I can't even eat rice porridge. / If only I had money, I could get through this."),
  R("＊のみ　～のみ", "ここから先は、関係者のみ入場可とする。", "＊", "NEW: のみ = only (stiff, written). See the teach panel below."),
 ]),
 gram("＊3", "d16b-danodano", "～だの～だの", "うんざりというニュアンスで例を挙げる。【話し言葉】",
  ["だの～だの = A and B and so on — listing examples with a fed-up, complaining tone.",
   "'Thambi room-la paper kuppai, kaali can — ellaam niranju kidakku!' → 弟の部屋は、紙くずだの空きかんだのでいっぱいだ.",
   "Very often used for someone's endless complaints: ～が悪いだの、～はだめだの、文句ばかり言う.",
   "Spoken language. Compare ～やら～やら (just a messy mix, less complaining)."],
  "［名詞］・普通形（ナ形 だ・名 だ）＋だの",
  [ex("弟の部屋は、紙くずだの空きかんだのでいっぱいだ。", "Thambi room full-aa paper kuppai, kaali can — ugh."),
   ex("隣のうちの人は、ごみの出し方が悪いだの夜の洗濯はだめだの、文句ばかり言う。", "Pakkaththu veettukaarar 'kuppai podra murai thappu, raathiri thuni thuvaikka koodaadhu' nu complaint mattum dhaan."),
   ex("妹は、寒いだのおなかがすいただのと言って、全然歩こうとしない。", "Thangachi 'kulirudhu, pasikkudhu' nu solli nadakkave maataa.")],
  [("私の好きな食べ物は、すしだの天ぷらだのです。", "私の好きな食べ物は、すしや天ぷらなどです。",
    "だの～だの has a fed-up feeling. For neutral, happy examples use や～など.")],
  [("母は、早く寝ろ（　　）勉強しろ（　　）、毎日うるさい。", ["だの・だの", "とか・など", "にしても・にしても"], 0, "Complaining list of nagging → だの～だの.")],
  ["～だの～だの = A, B and so on, listed with an annoyed feeling.",
   "Shape: noun / plain form (ナ形・名 without だ) + だの.",
   "Kavanam: spoken; usually negative, complaining."],
  [("①弟の部屋は、紙くず[[だの]]空きかん[[だの]]でいっぱいだ。", "My brother's room is full of scrap paper, empty cans and stuff."),
   ("②{隣|となり}のうちの人は、ごみの出し方が悪い[[だの]]夜の洗濯はだめ[[だの]]、{文句|もんく}ばかり言う。", "The man next door keeps complaining — the way we put out rubbish is wrong, no laundry at night…")],
  "［名］・普通形（ナ形 だ・名 だ）＋だの",
  "話し言葉。うんざりした気持ちで例を挙げる。"),
 gram("＊4", "d16b-nomi", "～のみ", "限定を表す。【硬い言い方】",
  ["のみ = only — the stiff, written version of だけ.",
   "Signs, rules and notices love it: 関係者のみ入場可 = staff only.",
   "Also in job ads etc.: 土日のみのアルバイト = a weekends-only part-time job."],
  "［名詞］＋のみ",
  [ex("ここから先は、関係者のみ入場可とする。", "Inga irundhu munnaadi, sambandhapattavanga mattum dhaan ulle varalaam."),
   ex("土日のみのアルバイトを探している。", "Sani-Nyaayiru mattum work panra part-time thedikittu irukken."),
   ex("ご注文は、お一人様1点のみとさせていただきます。", "Order oru aalukku oru item mattum dhaan.")],
  [("きのうは、コーヒーのみ飲んだよ。", "きのうは、コーヒーだけ飲んだよ。",
    "のみ is stiff, for notices and writing. In daily talk use だけ.")],
  [("この{駐車場|ちゅうしゃじょう}は、{利用者|りようしゃ}（　　）{駐車|ちゅうしゃ}できます。", ["のみ", "さえ", "まで"], 0, "Rule on a sign: users only → のみ.")],
  ["～のみ = only (formal だけ).",
   "Shape: noun + のみ.",
   "Kavanam: written / official notices."],
  [("①ここから先は、関係者[[のみ]]入場可とする。", "Beyond this point, authorised persons only."),
   ("②土日[[のみ]]のアルバイトを探している。", "I'm looking for a weekends-only part-time job.")],
  "［名］＋のみ",
  "硬い言い方。"),
 group("練習1　［　］から最も適当な言い方を選び、（　）の中の言葉を適当な形にして、＿＿の上に書きなさい。", [
  text("［～か～ないかのうちに　・　～(よ)うか～まいか　・　～やら～やら　・　～というか～というか　・　～にしても～にしても　・　～だの～だの］"),
  FB("d16b-f1-1", "1　この作家の文章は%%、とにかく深刻であることは確かだ。（重い・暗い）", ["重いというか暗いというか"], "Hard to describe: heavy, or dark… → 重いというか暗いというか."),
  FB("d16b-f1-2", "2　弟は毎朝%%と言って、なかなか起きようとしない。（頭が痛い・おなかが痛い）", ["頭が痛いだのおなかが痛いだの"], "Complaining excuses → 頭が痛いだのおなかが痛いだの."),
  FB("d16b-f1-3", "3　引っ越したばかりで、%%買わなければならないものがいろいろある。（カーテン・机）", ["カーテンやら机やら"], "Mixed list of many things → カーテンやら机やら."),
  FB("d16b-f1-4", "4　%%、映画を見るのは楽しい。（映画館で見る・DVDで見る）", ["映画館で見るにしてもDVDで見るにしても","映画館で見るにしてもＤＶＤで見るにしても"], "Either way, it's fun → 映画館で見るにしてもDVDで見るにしても."),
  FB("d16b-f1-5", "5　%%、メールの返事が来た。（5分たつ・たたない）", ["5分たったかたたないかのうちに","5分たつかたたないかのうちに","５分たったかたたないかのうちに","５分たつかたたないかのうちに"], "Barely five minutes later → 5分たったかたたないかのうちに (or たつかたたないかのうちに)."),
  FB("d16b-f1-6", "6　少し高そうな店だったので、%%しばらく中の様子をのぞきながら考えていた。（入る・入らない）", ["入ろうか入るまいか"], "Whether to go in or not → 入ろうか入るまいか."),
 ], lead="Key (別冊 p.6): 1 重いというか暗いというか 2 頭が痛いだのおなかが痛いだの 3 カーテンやら机やら 4 映画館で見るにしてもDVDで見るにしても 5 5分たったかたたないかのうちに／5分たつかたたないかのうちに 6 入ろうか入るまいか."),
 group("練習2　［　］から適当なものを選び、＿＿の上に書きなさい。（一つの言葉を1回だけ使います。）", [
  text("［とは　・　ぐらい　・　など　・　のみ　・　まで　・　さえ　・　として］"),
  FB("d16b-f2-1", "1　交通の{便|べん}%%よければ、この町はもっと観光客が増えると思うのですが……。", "さえ", "さえ～ば = if only transport were good."),
  FB("d16b-f2-2", "2　【注意書き】こちらの商品のご注文は、お一人様1点%%とさせていただきます。", "のみ", "Notice → 1点のみ (only one)."),
  FB("d16b-f2-3", "3　大雨が降ると聞いて長靴%%{履|は}いていったが、午後は晴れた。", "まで", "長靴まで = I even wore rain boots."),
  FB("d16b-f2-4", "4　小学校に上がる前に、自分の名前%%は読み書きできたほうがいい。", "ぐらい", "名前ぐらい = at least your own name."),
  FB("d16b-f2-5", "5　わたしはうそ%%言っていない。全部本当のことだ。", "など", "うそなど言っていない = I'm not telling lies (or anything like that)."),
  FB("d16b-f2-6", "6　一生の仕事%%どういうことかをよく考えて、会社を辞めた。", "とは", "～とはどういうことか = what ～ really means."),
  FB("d16b-f2-7", "7　このボタンは手作りなので、全く同じものは一つ%%ない。", "として", "一つとして～ない = not even one."),
 ], lead="Key (別冊 pp.6–7): 1さえ 2のみ 3まで 4ぐらい 5など 6とは 7として."),
]

# ================= G 文法的性質の整理 (pp.136–137) =================
G = [
 text("N2の文法形式は、それぞれに文法的性質を持っていて、文を作るときの制約になります。以下のような文法的性質に気をつけながら学習しましょう。",
  title="Ⅳ 文法形式の整理　G 文法的性質の整理",
  explain=["Sensei: Each grammar form has rules about WHAT can come after it. The exam tests this a lot: 'which ending fits?'",
           "Thanglish: Three checks: (1) can a wish / command / 'let's' come after it? (2) is the subject me or someone else? (3) is the result good or bad? Indha list-a oru checklist maadhiri use pannunga."]),
 items("1　事実か気持ちが入っているか", [
  ("a) 後に話者の希望・意向を表す文や働きかけの文が来る\n～次第（3課）　～ものなら（15課）　～からには・～以上は・～{上|うえ}は（17課）　～ことだし（17課）　～てでも（21課）",
   "After these, you CAN put your wish / will / a request or order: 情報が入り次第、お知らせします ✓."),
  ("b) 後に話者の希望・意向を表す文や働きかけの文は来ない\n～たとたん(に)（1課）　～(か)と思うと・～(か)と思ったら（1課）　～か～ないかのうちに（1課）　～もかまわず（11課）　～にもかかわらず（14課）　～ものの・～とはいうものの（14課）　～とすると・～となると（15課）　～ものだから（16課）　～おかげだ／～せいだ（16課）　～あまり・あまりの～に（16課）　～だけに（17課）　～ばかりに（17課）　～たところ（20課）　～きり（20課）",
   "After these, only FACTS — no 'let's', no 'please', no 'I will'. ～たところ、珍しい景色に出会えた ✓ / ～ましょう ✗."),
  ("c) 後に推量の文が来る\n～(よ)うものなら（15課）　～のことだから（17課）",
   "After these, a guess (～だろう, きっと～): 彼のことだから、きっと遅れて来るだろう."),
 ]),
 items("2　自分か他者か", [
  ("a) 一人称が主語の文で使う\n～わけにはいかない（18課）　～てしかたがない（25課）　～てならない（25課）　～ないではいられない・～ずにはいられない（25課）　～ないわけに(は)いかない（25課）　～ざるを得ない（25課）　～たいものだ（26課）",
   "Subject = I (the speaker's own feelings). For someone else add らしい／ようだ."),
  ("b) 三人称が主語の文で使う\n～(か)と思うと・～(か)と思ったら（1課）　～とみえる（22課）",
   "Subject = someone / something else, seen from outside. Not for yourself."),
 ]),
 items("3　プラスイメージかマイナスイメージか", [
  ("a) 後に主にマイナスイメージの文が来る、または全体としてマイナスイメージの文になる\n～ばかりだ・～一方だ（2課）　～せいだ（16課）　～ばかりに（17課）　～どころではない（18課）　～あげく（20課）　～ずじまいだ（20課）　～かねない（22課）　～おそれがある（22課）　～てならない（25課）",
   "Bad result / negative feeling comes after these. 課長に文句を言われかねない ✓ / ほめられかねない ✗."),
  ("b) 後に主にプラスイメージの文が来る、または全体としてプラスイメージの文になる\n～にかけては（7課）　～おかげだ（16課）　～だけ(のことは)ある（19課）",
   "Good result / praise comes after these."),
 ]),
 group("練習1　どちらか適当な方を選びなさい。", [
  PICK("d16b-g1-1", "1　詳しい情報が入り次第、（　）", ["お知らせいたします。","関係者が知らせてくれた。"], 0, "次第 → the speaker's intention follows (1a). A past fact can't come after 次第.", AB),
  PICK("d16b-g1-2", "2　手術を避けられるものなら（　）", ["避けたいのだが、そうはいかないだろう。","ほかの治療方法があるのではないか。"], 0, "ものなら → a wish (～たい) follows (1a).", AB),
  PICK("d16b-g1-3", "3　山川先生が病気だと聞いたからには（　）", ["ぜひお見舞いに行かなくては。","あしたお見舞いに行くことにした。"], 0, "からには → strong will / duty (～なくては) follows (1a).", AB),
  PICK("d16b-g1-4", "4　夕立がやんだかと思ったら、（　）", ["すぐに工事を再開しよう。","もう太陽が出てきた。"], 1, "かと思ったら → no will after it; a fact that happened at once (1b).", AB),
  PICK("d16b-g1-5", "5　（　）", ["営業の仕事が忙しいので、人目もかまわずバスの中で昼ご飯を食べようと思う。","営業の仕事が忙しいらしく、彼は人目もかまわずバスの中で昼ご飯を食べている。"], 1, "もかまわず → describes what someone does, not 'I'll do' (1b).", AB),
  PICK("d16b-g1-6", "6　年末は道路が渋滞するものだから、（　）", ["ふるさとへは電車で行きなさい。","ふるさとへは電車で行くことにした。"], 1, "ものだから → no command after it (1b). 行くことにした is a fact ✓.", AB),
  PICK("d16b-g1-7", "7　いつもとは違うコースをドライブしてみたところ、（　）", ["珍しい景色を楽しみましょう。","珍しい景色に出会えた。"], 1, "たところ → a result (fact), not 'let's' (1b).", AB),
  PICK("d16b-g1-8", "8　泣いている子供を見て、（　）", ["母は声をかけずにはいられなかった。","わたしは声をかけずにはいられなかった。"], 1, "ずにはいられない → subject is 'I' (2a).", AB),
  PICK("d16b-g1-9", "9　（　）", ["わたしもこんなすばらしい花の庭を作ってみたいものだ。","花子さんもこんなすばらしい花の庭を作ってみたいものらしい。"], 0, "たいものだ → the speaker's own wish (2a).", AB),
  PICK("d16b-g1-10", "10　（　）", ["玄関のチャイムが鳴ったかと思うと、大勢のお客さんが入ってきた。","今日はとても眠かった。夕食を食べ終わったかと思うとすぐ寝てしまった。"], 0, "かと思うと → used about someone/something else, not yourself (2b).", AB),
  PICK("d16b-g1-11", "11　（　）", ["わたしはどうも風邪を引いたとみえる。熱がある。","あの人は風邪を引いているとみえる。さっきからせきばかりしている。"], 1, "とみえる → judging someone else from outside (2b).", AB),
  PICK("d16b-g1-12", "12　この報告書だと、また課長に（　）", ["文句を言われかねない。","ほめられかねない。"], 0, "かねない → bad result only (3a).", AB),
  PICK("d16b-g1-13", "13　右手の指にけがをしたばかりに、（　）", ["パソコンをいつもの速さで打てなかった。","まゆみさんが親切に包帯を巻いてくれた。"], 0, "ばかりに → bad result (3a).", AB),
  PICK("d16b-g1-14", "14　夜、コーヒーを1杯飲んだばかりに、（　）", ["明け方まで眠れなかった。","明け方まで試験勉強がよくできた。"], 0, "ばかりに → bad result: couldn't sleep (3a).", AB),
 ], lead="Key (別冊 p.7): 1a 2a 3a 4b 5b 6b 7b 8b 9a 10a 11b 12a 13a 14a."),
]

# ================= 第2部 1課 文の組み立て-1 決まった形 (pp.140–141) =================
def star(id, q, opts, ans, order, explain):
    return PICK(id, q, opts, ans, ["Answer %d. Correct order: %s" % (ans + 1, order), explain], N4)

P2 = [
 text("語と語を結びつけて意味の通る文を組み立てるためには、文法的な決まりを考えながら語を並べていかなければなりません。文法形式の意味や用法がわかることだけではなく、実際に文を組み立てられることが大切です。",
  title="実力養成編　第2部　文の文法2",
  explain=["Sensei: 第2部 trains the JLPT 文法 問題8 type: four pieces, put them in order, and choose the one in the ★ slot.",
           "Thanglish: Meaning theriyum-naa podhaadhu — words-a correct order-la vekkanum. Trick: find the fixed pairs first (からといって…わけではない, さえ…ば, 何一つとして…ない), then fit the rest around them."]),
 text("文を組み立てるときは、組み立てのルールに従わなければなりません。そのうち、ぜひ覚えておくべきルールは次のようなものです。", title="1課　文の組み立て-1　決まった形"),
 items("1　後に否定の言い方が来るもの", [
  ("・～てからでないと　　現地を見てからでないと、何とも申し上げられ**ません**。（第1部3課）", "てからでないと + negative: I can't say anything until I've seen the site."),
  ("・～に限って　　あの子に限ってうそをつく**はずがない**。（第1部5課）", "に限って + はずがない: Not that child — he'd never lie."),
  ("・～からといって　　正月だからといって、仕事を休める**わけではない**。／安いからといって、品質が悪い**とは限らない**。（第1部14課）", "からといって + わけではない／とは限らない: Just because it's New Year doesn't mean I can take time off."),
  ("・～ないことには　　体力がないことには、責任のある仕事は**できない**。（第1部15課）", "ないことには + negative: Without stamina you can't do a responsible job."),
  ("・～を抜きにしては　　山下さんを抜きにしては、この計画は実行**できない**。（第1部15課）", "を抜きにしては + negative: Without Mr Yamashita this plan can't go ahead."),
  ("・～として～ない　　1日として酒を飲まない日は**なかった**。（第1部21課）", "1日として + ない: There wasn't a single day he didn't drink."),
 ]),
 items("2　疑問詞につくもの", [
  ("・～にしても・にしろ・にせよ　　**どちら**にしてもやらなければならないことは同じだ。（第1部15課）", "Question word + にしても: whichever, it's the same."),
  ("・～として～ない　　**だれ**一人として会長の意見に賛成する者はいなかった。（第1部21課）", "だれ一人として～ない = not a single person."),
  ("・～ことだろう・ことか　　あの子にはもう**何度**注意したことか。（第1部26課）", "何度～ことか = how many times have I…!"),
 ]),
 items("3　数字につくもの", [
  ("・～として～ない　　古い本を**1冊**として残さず、捨ててしまった。（第1部21課）", "1冊として残さず = without keeping even one book."),
 ]),
 items("4　後に名詞が来るもの", [
  ("・～といった　　わたしはうどん、そばといった**めん類**が好きだ。（第1部10課）", "A、Bといった + noun (the group): noodles like udon and soba."),
 ]),
 items("5　だいたい決まった組み合わせで使うもの", [
  ("・～さえ～ば　　弟は暇さえあればインターネットで何か見ている。（第1部21課）", "さえ…ば: whenever he has a spare moment."),
  ("・～を～にして　　漢字をもとにして、ひらがなとカタカナが作られた。", "AをもとにしてB: hiragana and katakana were made from kanji."),
  ("・～を～として　　昨夜、関東地方を中心として、大雨が降った。", "Aを中心として: heavy rain, centred on Kanto."),
  ("・たとえ～としても・にしても・にしろ・にせよ　　たとえ正解でないにしても、大きく間違ってはいないはずだ。（第1部15課）", "たとえ～にしても: even if it isn't right, it can't be far off."),
  ("・なにも～ことはない　　なにもそんなに怒ることはないでしょう。（第1部24課）", "なにも～ことはない: there's no need to get THAT angry."),
  ("・なんと～ことだろう・ことか　　マリさんの分析力はなんと鋭いことだろう。（第1部26課）", "なんと～ことだろう: how sharp Mari's analysis is!"),
 ]),
 group("練習1　次の文の＿★＿に入る最もよいものを1・2・3・4の中から一つ選びなさい。", [
  star("d16b-p1-1", "1　一度ぐらい店長にしかられた＿＿ ＿＿ ★ ＿＿でしょう。", ["ことはない","なにも","からといって","店を辞める"], 3, "からといって → なにも → 店を辞める → ことはない", "なにも～ことはない and からといって are both fixed partners. 'Just because the manager scolded you once, there's no need to quit.'"),
  star("d16b-p1-2", "2　ぜひ買ってほしいと＿＿ ＿＿ ★ ＿＿気にはなりません。", ["買う","言われても","でないと","現物を見てから"], 2, "言われても → 現物を見てから → でないと → 買う", "てからでないと + negative (気にはなりません). 'Even if you ask me to buy it, I won't feel like buying until I've seen the real thing.'"),
  star("d16b-p1-3", "3　帰国の前日、家具が＿＿ ＿＿ ★ ＿＿部屋を掃除した。", ["として","一つ","残っていない","何"], 0, "何 → 一つ → として → 残っていない", "何一つとして～ない. 'The day before going home, I cleaned the room with not a single piece of furniture left.'"),
  star("d16b-p1-4", "4　わたしの主張が認められなくて＿＿ ＿＿ ★ ＿＿と思う。", ["悔しかった","どんなに","わかってもらえない","ことか"], 3, "どんなに → 悔しかった → ことか → わかってもらえない", "どんなに～ことか (how much…!). 'Nobody will understand how frustrated I was that my point wasn't accepted.'"),
  star("d16b-p1-5", "5　君が＿＿ ＿＿ ★ ＿＿から必ず来てくれ。", ["バンド演奏が","来ない","できない","ことには"], 0, "来ない → ことには → バンド演奏が → できない", "ないことには + negative. 'Unless you come, the band can't play, so be sure to come.'"),
  star("d16b-p1-6", "6　あいさつを＿＿ ＿＿ ★ ＿＿決めておかなければならない。", ["頼む","スケジュールは","にしても","だれに"], 2, "だれに → 頼む → にしても → スケジュールは", "Question word + にしても. 'Whoever we ask to give the speech, we have to fix the schedule.'"),
  star("d16b-p1-7", "7　このたび、この町の＿＿ ＿＿ ★ ＿＿会が活動を開始しました。", ["する","目的と","交流を","外国人と日本人の"], 1, "外国人と日本人の → 交流を → 目的と → する", "AをBとする: an association whose aim is exchange between foreign and Japanese residents."),
  star("d16b-p1-8", "8　彼はたとえ＿＿ ＿＿ ★ ＿＿だろう。", ["一度決めた","にしても","進路を変えない","困難である"], 0, "困難である → にしても → 一度決めた → 進路を変えない", "たとえ～にしても. 'Even if it's hard, he won't change the path he has chosen.'"),
  star("d16b-p1-9", "9　うちでは＿＿ ＿＿ ★ ＿＿専業主婦のわたしがやっているんです。", ["といった","面倒なことは","家事や育児","みんな"], 1, "家事や育児 → といった → 面倒なことは → みんな", "AといったB (noun). 'At home, troublesome things like housework and childcare are all done by me, the housewife.'"),
  star("d16b-p1-10", "10　この村は＿＿ ＿＿ ★ ＿＿としてもっと発展するのに。", ["さえ","観光の名所","よければ","交通の{便|べん}"], 2, "交通の{便|べん} → さえ → よければ → 観光の名所", "さえ～ば. 'If only the transport were good, this village would develop more as a tourist spot.'"),
  star("d16b-p1-11", "11　周囲の人たちの＿＿ ＿＿ ★ ＿＿と思う。", ["協力を","優勝は","無理だった","抜きにしては"], 1, "協力を → 抜きにしては → 優勝は → 無理だった", "を抜きにしては + negative. 'Without the help of the people around us, winning would have been impossible.'"),
  star("d16b-p1-12", "12　H氏に＿＿ ＿＿ ★ ＿＿と思っていたのに……。", ["発言をする","はずはない","限って","そんな"], 0, "限って → そんな → 発言をする → はずはない", "に限って + はずはない. 'I thought Mr H, of all people, would never make a remark like that…'"),
 ], lead="Key (別冊 p.7): 1-4 2-3 3-1 4-4 5-1 6-3 7-2 8-1 9-2 10-3 11-2 12-1. Tip: put the fixed pair together first, then the rest falls into place."),
]

SECTION = {
 "book": "bunpo",
 "title": "Ⅳ 文法形式の整理 E–G・第2部 1課 文の組み立て-1",
 "source": "新完全マスター文法 N2 · 第1部 Ⅳ E–G · 第2部 1課 · pp.132–141 · answers from 別冊 解答 pp.6–7",
 "blocks": [*E, *F, *G, *P2],
}
