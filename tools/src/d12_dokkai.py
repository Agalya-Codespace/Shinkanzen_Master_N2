from _h import *
DAY = 12

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

def goi(imp, rel, ren=None):
    rows = [("重要{語|ご}い：" + imp, "Key words for solving the question."), ("関連{語|ご}い：" + rel, "Related words.")]
    if ren: rows.append(("練習の{語|ご}い：" + ren, "Words used in 練習45–46."))
    return items("{語|ご}いリスト", rows)

SECTION = {
 "book": "dokkai",
 "title": "第2部　2. 情報を探し出す―1) 広告",
 "source": "新完全マスター読解 N2 · 第2部 広告・お知らせ・説明書きなど · pp.86–93 · 例題 answers in the book; 練習 answers from 別冊 解答 pp.15–16",
 "blocks": [
  text("Inniki 広告 (ads): coupons, 'students wanted' posters, sale flyers. Indha type question-la full-aa padikka vendaam — question kekkura information mattum thedi edukkanum (情報を探し出す).",
   "今日のポイント　情報を探し出す　1) 広告",
   "3 steps every time: ① read the question AND the choices (what are they asking — date? time? how many? where?) ② find where that info is: big/bold letters = what they want everyone to see; small letters (＊ notes) = important conditions! ③ check each choice against the ad."),

  passage("☆例題20　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "{有効期限|ゆうこうきげん}　3/5（金）10:30～4/1（木）",
   "春の{割引|わりびき}クーポン",
   "クーポン価格　¥490　（{通常|つうじょう}価格 ¥540）",
   "ハンバーガー＋フライドポテトS＋ドリンクM",
   "＊1回{限|かぎ}り、1{枚|まい}で2セットまでご利用いただけます。＊ドリンクは、セットドリンクからお選びいただけます。＊モーニングタイム（10:30まで）以外でご利用ください。＊{表記|ひょうき}しているサイズのみ有効です。＊クーポンは切り取ってご利用ください。",
   "ご注文はこちらのクーポン番号で　35",
  ], [
   "有効期限(ゆうこうきげん) = valid until (expiry). 割引(わりびき) = discount. 通常価格(つうじょうかかく) = normal price. 1回限り(いっかいかぎり) = one time only. 表記(ひょうき) = written, shown. 切り取る(きりとる) = cut out.",
   "Coupon-la always check: dates & times, how many you can use, and the small ＊ notes.",
  ]),
  toi("d12d-e20", "このクーポンを1枚持っている。使い方として正しいものはどれか。", [
   "3月31日午前9時にこのセットを2つ注文する。",
   "4月{10日|とおか}午後6時にこのセットを2つ注文する。",
   "3月27日午後3時にこのセットを2つ注文する。",
   "3月5日午前10時半にこのセットを3つ注文する。"], 2,
   ["Answer 3. 3/27 is inside 3/5–4/1, 3 p.m. is after morning time, 2 sets is the limit → OK.",
    "1: 9 a.m. is モーニングタイム (until 10:30) → can't use. 2: only valid until 4/1. 4: max 2 sets per coupon."]),
  {"type": "reveal", "label": "本の解説：例題20", "children": [
   items("ステップ1　問いと選択肢を読もう", [T("問い：クーポンの使い方は？"), T("選択肢：何日？　何時？　いくつ？")]),
   items("ステップ2　どこに情報があるか探そう", [
    ("◇一般的な知識を使う。　→　クーポンには、通常価格、割引価格、使える期間（有効期限）、商品などが書いてある。", "Use general knowledge of what a coupon contains."),
    ("◇大きい字・太い字に注目する。　→　皆に知らせたいことは目立つ字で書かれている。\n　[[3/5～4/1]]、割引クーポン、¥490、ハンバーガー＋フライドポテトS＋ドリンクM", "Big letters = what they want everyone to notice."),
    ("◇小さい字に注目する。　→　小さい字は大事な注意が書かれていることがある。\n　＊1回限り、[[1枚で2セットまで]]ご利用いただけます。\n　＊[[モーニングタイム（10:30まで）以外]]でご利用ください。", "Small letters = important conditions."),
   ]),
   items("ステップ3　正しい答えを選ぼう", [
    T("1：9時はモーニングタイムなので使えない。"),
    T("2：4月1日までしか使えない。"),
    T("3：正解"),
    T("4：2セットまでしか使えない。"),
   ]),
  ]},
  goi("{有効期限|ゆうこうきげん}　{割引|わりびき}　クーポン", "{値引|ねび}き　サービスする　〔コーヒー〕{付|つ}き　セール　バーゲン　{以降|いこう}　{金額|きんがく}"),

  passage("☆例題21　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "キッズスクール\n生徒{募集|ぼしゅう}！",
   "サッカーで、\n楽しく全身運動ができる！\n{集団|しゅうだん}生活に慣れる！\n友達をたくさんつくろう！",
   "{曜日|ようび}…毎週水曜日　　時間…15:00～16:00\n{対象|たいしょう}…3歳～5歳の男女　　場所…{森山|もりやま}公園内グラウンド\n{定員|ていいん}…40名　　{月謝|げっしゃ}…4,000円\n{持参|じさん}するもの…運動靴",
   "・いつからでもご{入会|にゅうかい}いただけます。（月{途中|とちゅう}からのご入会につきましては、参加回数に{応|おう}じて月謝をお支払いいただきます。）\n・入会希望の方は、{前日|ぜんじつ}までに{以下|いか}お申し込み{先|さき}にご連絡ください。",
   "{尚|なお}、無料体験会もございます。ご興味のある方は、{是非|ぜひ}お気軽にご参加ください。\n{開催|かいさい}日時：5月15日（土）・{16日|じゅうろくにち}（日）　10:00～11:00\n＊ご都合の良い日をお選びください。\n対象：3歳～5歳の男女\n場所：{森山|もりやま}公園内グラウンド\n定員：10名\n申し込み締め切り：5月12日",
   "申し込み・お問い合わせ\nミヤモリサッカークラブ　Tel: 000-0000-0000",
  ], [
   "募集(ぼしゅう) = recruiting. 集団生活(しゅうだんせいかつ) = group life. 対象(たいしょう) = who it's for. 定員(ていいん) = capacity. 月謝(げっしゃ) = monthly fee (for lessons). 持参(じさん) = bring. 入会(にゅうかい) = join (a club). ～に応じて(おうじて) = according to. 無料体験会(むりょうたいけんかい) = free trial session. 開催(かいさい) = holding (an event).",
   "Two different things are in this ad: the school itself, and (after 尚) a free trial. Don't mix their dates!",
  ]),
  toi("d12d-e21", "サッカースクールに子供を入会させたい。どうすればいいか。", [
   "水曜日、15時に森山公園のグラウンドに行って申し込む。",
   "入会希望日の前日までにミヤモリサッカークラブに電話して申し込む。",
   "5月12日までにミヤモリサッカークラブに電話して申し込む。",
   "入会希望日の前日までに森山公園のグラウンドに行って申し込む。"], 1,
   ["Answer 2. 入会希望の方は、前日までに…お申し込み先にご連絡ください → phone ミヤモリサッカークラブ by the day before.",
    "1 & 4: you don't apply at the ground. 3: 5月12日 is the deadline for the free trial, not for joining."]),
  {"type": "reveal", "label": "本の解説：例題21", "children": [
   items("ステップ1　問いと選択肢を読もう", [T("問い：サッカースクールに参加する方法は？"), T("選択肢：いつ申し込む？　どこに申し込む？")]),
   items("ステップ2　どこに情報があるか探そう", [
    ("◇問いと選択肢のキーワードを見つける。　→　「入会」「申し込む」\n　いつからでもご[[入会]]いただけます。\n　[[入会]]希望の方は、[[前日までに]]以下お申し込み先にご連絡ください。\n　[[申し込み]]・お問い合わせ\n　[[ミヤモリサッカークラブ]]　Tel: 000-0000-0000", "Find the keywords from the question in the ad."),
   ]),
   items("ステップ3　正しい答えを選ぼう", [
    T("1：水曜日、グラウンドで申し込むのではない。"),
    T("2：正解"),
    T("3：5月12日は、無料体験会の締め切り日である。"),
    T("4：グラウンドで申し込むのではない。"),
   ]),
  ]},
  items("募集広告の一般的な形式", [
   ("〇〇〇募集！　←タイトル（何の募集か）", "Title: what they're recruiting."),
   ("日時：××××××", "Date and time."),
   ("対象：××××××　←どんな人を募集しているか", "Who can join."),
   ("場所：××××××", "Place."),
   ("定員：××××××　←何人まで参加できるか", "How many people."),
   ("参加費／月謝：××××××　←費用はいるか／いくらか", "Cost."),
   ("申し込み締め切り日：××××　←いつまでに申し込むか", "Deadline."),
   ("（その他：××××××）　←持ってくるもの／注意することなど", "Things to bring, notes."),
   ("連絡先：××××××　←会社名・名前・電話番号", "Contact."),
   ("※順番は決まっていない。強調したい情報は、上の方に太字で書いてあることが多い。", "Order varies; key info is often at the top in bold."),
  ]),
  goi("{募集|ぼしゅう}　{月謝|げっしゃ}　{開催|かいさい}", "お{試|ため}し　{見学|けんがく}　{資格|しかく}　{条件|じょうけん}　{応募|おうぼ}", "{半額|はんがく}　～{周年|しゅうねん}　トライアル　{随時|ずいじ}"),

  passage("練習45　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "1{周年|しゅうねん}{感謝|かんしゃ}セール",
   "3/15（月）\n{半額|はんがく}{金券|きんけん}セール",
   "＊お買い上げいただいた{金額|きんがく}の半分の{額|がく}の金券を差し上げます。次回{以降|いこう}お使いになれます。",
   "いつもご{来店|らいてん}いただき{誠|まこと}にありがとうございます。\n皆様のおかげで、無事1周年を{迎|むか}えることができました。\nこれからもおいしいパンを食べていただけるよう、\nスタッフ{一同|いちどう}全力をあげてがんばりますのでこれからもご来店くださいませ。",
   "{尚|なお}、金券の{有効期限|ゆうこうきげん}は4月30日です。",
   "ブーランジュリ　イトウ\nTel. 03-329-6521",
  ], [
   "1周年(いっしゅうねん) = first anniversary. 半額(はんがく) = half price. 金券(きんけん) = voucher. お買い上げ(おかいあげ) = purchase (polite). 次回以降(じかいいこう) = from next time on. 来店(らいてん) = visiting the shop. 一同(いちどう) = everyone (all the staff). 全力をあげる = give it everything.",
   "Big letters say 半額金券セール — but read the small ＊ note: it's NOT half price. You get a voucher worth half of what you paid.",
  ]),
  toi("d12d-r45", "「半額金券セール」の広告を見た。「半額金券セール」とはどのようなものか。", [
   "3月15日に、パンの値段が半額になる。",
   "3月15日から4月30日まで、パンの値段が半額になる。",
   "3月15日にパンを買うと、半額分の金券がもらえる。その金券はいつでも使える。",
   "3月15日にパンを買うと、半額分の金券がもらえる。その金券は4月30日まで使える。"], 3,
   ["Answer 4. Buy on 3/15 → get a voucher for half the amount → use it next time or later, until 4/30 (尚、金券の有効期限は4月30日).",
    "1 & 2: bread isn't half price. 3: the voucher expires on 4/30, so not 'any time'."]),
  kaisetsu(45, ["太い字・大きい字に注目する。",
   "「[[3／15]]」", "「[[半額金券セール]]」",
   "「＊お買い上げいただいた[[金額の半分の額の金券]]を差し上げます。[[次回以降]]お使いになれます。」",
   "小さい字には大事な注意が書いてある。",
   "「尚、金券の[[有効期限は4月30日]]です。」",
   "1：パンの値段が半分になるのではない。", "2：パンの値段が半分になるのではない。4月30日は金券の有効期限。",
   "3：金券の有効期限は4月30日である。", "4：正解"]),

  passage("練習46　問いに対する答えとして最もよいものを一つ選びなさい。", [
   "スマート・フィットネスクラブ",
   "スポーツの秋　トライアル7日間\n初めての方でも安心！　{是非|ぜひ}お{試|ため}しください！",
   "{施設|しせつ}{見学|けんがく}　{随時|ずいじ}受け付け中！",
   "たっぷり7日間　お{試|ため}し体験\n{事前|じぜん}のご予約が必要です。\n＊ご体験初日はクラブ{指定|してい}の運動メニューでの体験となります。",
   "期間：　10月{11日|じゅういちにち}～{20日|はつか}\n＊期間中ご{都合|つごう}の良い7日間をお選びください。\n参加料金：　2000円",
   "お持ちいただくもの：\n運動に{適|てき}した服・靴\nタオル（バスタオルはお{貸|か}しします）\n{身分証明書|みぶんしょうめいしょ}（お申込み時、または初日にお持ちください）",
   "ステップ1　まずはご予約\n　前日までにお電話かご{来館|らいかん}で。\nステップ2　ご体験初日\n　担当のスタッフがおすすめのレッスン、運動メニューを{提案|ていあん}いたします。\nステップ3　2日目～7日目\n　ご{自身|じしん}のお好きなメニューで{全|ぜん}施設をご利用いただけます。\nステップ4\n　ご体験{最終日|さいしゅうび}に担当のスタッフがご{満足度|まんぞくど}についてお話を{伺|うかが}わせていただきます。",
   "＊お一人様1回限りとさせていただきます。\n＊施設{休館日|きゅうかんび}（毎月第4水曜日）は、ご利用いただけません。",
   "スマート・フィットネスクラブ　tel: 111-000-0000",
  ], [
   "施設見学(しせつけんがく) = facility tour. 随時(ずいじ) = at any time. 受け付け中 = now accepting. 事前(じぜん) = in advance. 指定(してい) = designated. 適した(てきした) = suitable. 身分証明書(みぶんしょうめいしょ) = ID card. 来館(らいかん) = come to the building. 提案(ていあん) = suggest. 満足度(まんぞくど) = level of satisfaction. 休館日(きゅうかんび) = closed day.",
   "Key words from the choices: 予約 (when? how?) and the 期間 (which days?).",
  ]),
  toi("d12d-r46", "体験コースに7日間参加したい。適切な方法はどれか。", [
   "7日に電話で予約し、12日から始める。",
   "9日にフィットネスクラブに行って予約し、{翌日|よくじつ}から始める。",
   "11日にフィットネスクラブに行って予約し、その日から始める。",
   "13日に電話で予約し、15日から始める。"], 0,
   ["Answer 1. Booked the day before or earlier (7th), and 12th–18th fits inside 11th–20th.",
    "2: the trial starts on the 11th, so you can't start on the 10th. 3: you must book by the day before. 4: from the 15th you can't get 7 days by the 20th."]),
  kaisetsu(46, ["選択肢にあるキーワード「予約」を本文中から探す。",
   "「[[事前のご予約が必要]]です。」",
   "「ステップ1　まずはご予約　[[前日までにお電話かご来館で]]。」",
   "「期間」を見る。太い字、大きい字に注目する。",
   "「期間：10月[[11日～20日]]」",
   "1：正解", "2：お試し体験期間は11日からである。{10日|とおか}からは始められない。",
   "3：予約は前日までにしなければならない。", "4：15日から始めると、20日までに7日間体験できない。"]),
 ],
}
