from _h import *
DAY = 15

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
    if ren: rows.append(("練習の{語|ご}い：" + ren, "Words used in 練習52."))
    return items("{語|ご}いリスト", rows)

SECTION = {
 "book": "dokkai",
 "title": "第2部　2. 情報を探し出す―4) 表・リスト／第3部へ",
 "source": "新完全マスター読解 N2 · 第2部 広告・お知らせ・説明書きなど · pp.116–123 · 例題 answers in the book; 練習 answers from 別冊 解答 p.18",
 "blocks": [
  text("Inniki 表・リスト (tables and lists): a price-comparison website for a TV, and an art-museum listings table. Tables look scary, but the question always gives you 2–4 conditions. Tick each condition off column by column and the answer drops out.",
   "今日のポイント　情報を探し出す　4) 表・リスト",
   "Same 3 steps: ① read the question and choices and list the CONDITIONS (date, price, payment, 'young Japanese painters') ② go to the column for each condition and cross out shops/places that fail ③ compare what's left. Watch for hidden extra costs (送料) and dates (～まで vs ～から～)."),

  passage("☆例題27　キムさんはSomyT32Aというテレビを買おうと思っている。以下は、インターネットの価格比較サイトで検索した結果である。問いに対する答えとして最もよいものを一つ選びなさい。", [
   "**順位　｜　価格　｜　送料　｜　在庫・発送の目安　｜　ショップ／支払い方法　｜　コメント**",
   "1位　｜　¥52,240　｜　¥600　｜　問い合わせ　｜　e-Shop　［代］［振］［ク］［コ］　｜　約2週間でお届けできます　延長保証有り",
   "2位　｜　¥52,500　｜　無料　｜　問い合わせ　｜　アキバnet　［代］［振］　｜　納期約2～3週間、ご注文お待ちしています",
   "2位　｜　¥52,500　｜　¥1,800　｜　有　当日発送可　｜　Powerでんき　［代］［振］［ク］［コ］　｜　即納です",
   "4位　｜　¥52,800　｜　無料　｜　有　すぐ送れます　｜　家電のKY　［代］［振］　｜　大型家電全国設置いたします",
   "4位　｜　¥52,800　｜　¥600　｜　有　当日発送可　｜　denkiyasan　［代］［振］［ク］［コ］　｜　テレビ等、設置いたします",
   "6位　｜　¥54,000　｜　¥1,500　｜　有　すぐ発送します　｜　サカイ　［代］［振］［ク］［コ］　｜　古いテレビを無料にて引き取ります",
   "（各行の右端に「詳細を見る▶」のボタンがある）",
   "［代］代引き　　［振］銀行振込　　［ク］クレジットカード支払い　　［コ］コンビニ支払い",
  ], [
   "順位(じゅんい) = ranking. 価格(かかく) = price. 送料(そうりょう) = shipping fee. 在庫(ざいこ) = stock. 発送(はっそう) = dispatch. 目安(めやす) = rough guide. 支払い方法 = payment method. 問い合わせ = ask us (stock unknown).",
   "延長保証(えんちょうほしょう)有り = extended warranty. 納期(のうき) = delivery time. 即納(そくのう) = immediate delivery. 当日発送可 = can ship the same day. 設置(せっち) = installation. 引き取る = take back.",
   "代引き(だいびき) = cash on delivery. 銀行振込(ぎんこうふりこみ) = bank transfer.",
   "Thanglish: 'Uyarndha rank' = cheapest PRICE only — but shipping (送料) separate-aa add aagum! Rank-a nambaadheenga, total-a calculate pannunga.",
  ]),
  toi("d15d-e27", "キムさんは買ったテレビをすぐに届けてほしいと思っている。クレジットカード支払いかコンビニ支払いで、いちばん安く買えるのはどこのショップか。", ["e-Shop","Powerでんき","家電のKY","denkiyasan"], 3,
   ["Answer 4 denkiyasan. Conditions: in stock now + card/convenience-store payment + cheapest total.",
    "In stock: Powerでんき, 家電のKY, denkiyasan (サカイ too, but it's not a choice). Card/コンビニ: Powerでんき, denkiyasan. Totals: Power ¥52,500 + ¥1,800 = ¥54,300; denkiyasan ¥52,800 + ¥600 = ¥53,400 → denkiyasan.",
    "e-Shop takes 2 weeks; 家電のKY has no card or コンビニ payment."]),
  {"type": "reveal", "label": "本の解説：例題27", "children": [
   items("ステップ1　問いと選択肢を読もう", [T("問い：すぐに届けてくれて、クレジットカード支払いかコンビニ支払いができるいちばん安いショップは？"), T("選択肢：「e-Shop」「Powerでんき」「家電のKY」「denkiyasan」の中から問いの条件に合うものを探す。")]),
   items("ステップ2　どこに情報があるか探そう", [
    ("◇項目「在庫（＝商品が店にあるかどうか）・発送の目安（＝いつごろ発送できるか）」を見る。\n　在庫有り　＝　Powerでんき　家電のKY　denkiyasan", "Stock column: three shops have it now."),
    ("◇項目「支払い方法」を見る。\n　［ク］［コ］　＝　Powerでんき　denkiyasan", "Payment column: two shops left."),
    ("◇項目「価格」と「送料」を見る。\n　Powerでんき　¥52,500＋¥1,800＝¥54,300\n　denkiyasan　¥52,800＋　¥600＝¥53,400", "Add the shipping: denkiyasan is cheaper overall."),
   ]),
   items("ステップ3　正しい答えを選ぼう", [
    T("1：届くまでに約2週間かかる。"),
    T("2：価格と送料が選択肢4より高い。"),
    T("3：クレジットカード支払い、コンビニ支払いができない。"),
    T("4：正解"),
   ]),
  ]},
  goi("{在庫|ざいこ}　{延長保証有|えんちょうほしょうあ}り　{納期|のうき}　{即納|そくのう}　{当日発送可|とうじつはっそうか}　{設置|せっち}　{銀行振込|ぎんこうふりこみ}", "{出荷|しゅっか}　{別途|べっと}", "{展示|てんじ}　{絵画|かいが}　～{世紀|せいき}　{公開|こうかい}　{彫刻|ちょうこく}"),

  passage("練習52　ミハイさんは、美術館へ行こうと思い、情報誌を見ている。以下はその一覧表である。問いに対する答えとして最もよいものを一つ選びなさい。", [
   "**美術館／博物館　｜　タイトル　｜　展示内容紹介　｜　展示期間**",
   "青田アート　｜　10人の冬　｜　今年、最も活躍した10人の若手による現代美術を紹介します。海外でも評価されている新進気鋭の日本人画家たちです。　｜　12月20日まで",
   "原田美術館　｜　アメリカ現代美術展　｜　アメリカ現代美術の一時代を創り上げた、ポップアーティストたちの作品を取り上げました。日本の現代絵画にも影響を与えたアメリカ現代美術のおもしろさを感じていただければ幸いです。　｜　12月31日まで",
   "森山美術館　｜　１２３絵画展　｜　出品作家は{小田|おだ}{高|たかし}、中瀬道夫、溝井聡子という、注目の現代作家です。それぞれの代表的な絵画作品を並べました。　｜　10月26日～12月10日",
   "三葉美術館　｜　美人画展　｜　江戸時代、その中でも特に17世紀後半から18世紀初めにかけての美人画を集めました。同時代の絵師による江戸の女性美を比べます。　｜　10月26日～12月31日",
   "都立博物館　｜　飛べ　もっと高く　｜　博物館所蔵の宇宙航空研究開発の資料など、航空・宇宙の技術開発の歴史をすべて公開。「はやぶさ」の実物大モデルもあります。　｜　10月26日～12月31日",
   "山の上美術館　｜　岸大助　山で考えたこと　｜　作品と自然が一つになった風景が広がります。庭に置かれた彫刻の数々。特に黒い石で作られた女性の像「座る女」「歩く女」「眠る女」は、是非見ていただきたい作品です。　｜　11月2日～1月31日",
  ], [
   "情報誌(じょうほうし) = listings magazine. 一覧表(いちらんひょう) = table, list. 展示(てんじ) = exhibition. 活躍(かつやく) = be active, do well. 若手(わかて) = young (artists). 現代美術(げんだいびじゅつ) = contemporary art. 新進気鋭(しんしんきえい) = up-and-coming.",
   "創り上げる = create. 絵画(かいが) = painting. 影響(えいきょう)を与える = influence. 出品作家 = exhibiting artists. 美人画(びじんが) = paintings of beautiful women. 絵師(えし) = (old) painter. 所蔵(しょぞう) = in the collection. 航空(こうくう) = aviation. 実物大(じつぶつだい) = life-size. 彫刻(ちょうこく) = sculpture.",
   "Thanglish: Moonu condition — ① young ② Japanese painters ③ contemporary art ④ open on 12月12日. Ovvoru column-um check pannunga.",
  ]),
  toi("d15d-r52", "ミハイさんは若い日本人画家による現代美術を見たいと思っている。12月12日に見られる美術館はどこか。", ["青田アート","森山美術館","三葉美術館","山の上美術館"], 0,
   ["Answer 1 青田アート: 若手 + 現代美術 + 日本人画家, open until 12月20日 → OK on 12月12日.",
    "2 森山: ends 12月10日. 3 三葉: Edo-period paintings, not contemporary. 4 山の上: sculpture, not painting."]),
  kaisetsu(52, ["問いにある「12月12日」「現代美術」「若い日本人画家」というキーワードで探す。",
   "「青田アート」\n「今年、最も活躍した10人の[[若手]]による[[現代美術]]を紹介します。海外でも評価されている新進気鋭の[[日本人画家]]たちです。」\n「[[12月20日まで]]」",
   "1：正解", "2：12月10日までなので、12日はやっていない。", "3：江戸時代の絵画で、現代美術ではない。", "4：彫刻であり、絵画ではない。"]),

  text("第3部では、第1部、第2部で学んだことを応用し、実際の試験と同じ形式の問いに答える練習をします。ただし、一つの文章に問いが一つの形式（短文の問題）はすでに練習しましたので、ここでは扱いません。一つの文章に複数の問いがある形式の問題を解いていきましょう。\n\n**1．内容理解（中文）**\n評論、解説、エッセイなど500字程度の文章について、第1部で解いたような問いが出題されます。中文では問いが三つ程度あります。\n\n**2．主張理解（長文）**\n論理展開が比較的明快な評論など、900字程度の文章について、第1部で解いたような問いが出題されます。問いが三つあり、その中の1問は筆者の主張を問うものです。\n\n**3．統合理解**\n統合理解は、比較的平易な二つ以上の文章（合計600字程度）を読んで問いに答える問題です。第1部、第2部で学んだことの応用ですが、問題の形式が上の1と2とは異なります。→問題形式の特徴、問題の解き方については、147ページを見てください。\n\n**4．情報検索**\n情報検索は、情報素材（700字程度）の中から必要な情報を探し出す問題です。第2部で学んだことの応用ですが、問いが情報素材の前にあります。→問題形式の特徴、問題の解き方については、161ページを見てください。",
   "第3部　実戦問題　（p.123）",
   ["Sensei: Part 3 = the real JLPT N2 reading formats, one passage with several questions.",
    "内容理解（中文） ≈ 500 characters, about 3 questions. 主張理解（長文） ≈ 900 characters, 3 questions, one asks the writer's main claim (主張). 統合理解 = compare 2+ short texts (≈600 total). 情報検索 = find info in a 700-character document; the question comes BEFORE the material.",
    "Thanglish: Naalaiyilirundhu (Day 16) real exam style aarambam. Part 1 skills (指示語, 理由, 下線部) + Part 2 skills (情報を探す) rendum serndhu use pannuvom."]),
 ],
}
