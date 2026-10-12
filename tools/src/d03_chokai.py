from _h import *
DAY = 3

def hear(id, q, ans, explain, n=3):
    """a/b/c heard only: buttons show just the letters."""
    return mcq(id, q, ABC[:n], ans, explain, keys=[""] * n)

OWN = "⚠ The book prints no script or answer for this CD track, so sensei made this practice set in the same format. The audio is a computer read-aloud, not the real CD."

W11 = [  # (target, a, b, c, ans, thanglish)
 ("きって", "きて", "きいて", "きって", 2, "切手(きって) = stamp. 小さい「っ」 = a tiny stop. きて (来て) has no stop; きいて (聞いて) has a long い."),
 ("びょういん", "びょういん", "びよういん", "ひょういん", 0, "病院(びょういん, hospital) = 3 beats: びょ・う・い・ん. 美容院(びよういん, beauty salon) = び・よ・う・い・ん, 5 beats. Book-oda 例 idhu dhaan!"),
 ("おばあさん", "おばさん", "おばあさん", "おばあちゃん", 1, "おばあさん (grandmother) = long あ. おばさん (aunt) = short. Length maarinaa meaning maarum."),
 ("しゅじん", "しんじん", "しゅうじん", "しゅじん", 2, "主人(しゅじん) = husband / master. 囚人(しゅうじん) = prisoner (long う). 新人(しんじん) = newcomer."),
 ("じゆう", "じゅう", "じゆう", "しゆう", 1, "自由(じゆう) = freedom: じ・ゆ・う, 3 beats. 十(じゅう) = じゅ・う, 2 beats. しゆう (私有) = no ゛."),
 ("さっか", "さっか", "さか", "さんか", 0, "作家(さっか) = writer. 坂(さか) = slope. 参加(さんか) = participation. っ vs nothing vs ん."),
 ("こうこう", "こうこう", "ここう", "こうこ", 0, "高校(こうこう) = high school: rendu long お. Count the beats: こ・う・こ・う = 4."),
 ("きんえん", "きねん", "きんえん", "きえん", 1, "禁煙(きんえん) = no smoking: き・ん・え・ん. 記念(きねん) = memorial: ん illa, ね dhaan. Idhu romba confuse aagum!"),
 ("ちず", "ちず", "チーズ", "しず", 0, "地図(ちず) = map. チーズ = cheese (long ー). Short vs long."),
 ("かいぎ", "かいき", "かいぎ", "がいき", 1, "会議(かいぎ) = meeting: last ぎ has ゛. かいき = no ゛."),
 ("しんぱい", "しっぱい", "しはい", "しんぱい", 2, "心配(しんぱい) = worry. 失敗(しっぱい) = failure. 支配(しはい) = rule/control. ん vs っ vs nothing."),
]

W12 = [  # (q with choices, a, b, ans, read, thanglish)
 ("昨日、（　　）行きました。", "病院へ", "美容院へ", 1, "きのう、びよういんへ行きました。", "Book-oda 例: ⓑ 美容院(びよういん, beauty salon)."),
 ("（　　）の話です。", "選手", "先週", 0, "せんしゅの話です。", "選手(せんしゅ) = player: しゅ short. 先週(せんしゅう) = last week: しゅう long."),
 ("（　　）なんだから、黙って。", "試験", "真剣", 1, "しんけんなんだから、だまって。", "真剣(しんけん) = serious: し・ん・け・ん. 試験(しけん) = exam: ん only once. 黙(だま)って = be quiet."),
 ("（　　）んですか。", "若いって言った", "わかっていた", 0, "わかいって言ったんですか。", "若(わか)いって言(い)った = said 'young'. わかっていた = knew. Speed-aa pesumbodhu 'わかいって' and 'わかって' romba close."),
 ("（　　）なりました。", "3人に", "3位に", 1, "さんいになりました。", "3位(さんい) = 3rd place. 3人(さんにん) = 3 people. 'さんい' has no extra に beat."),
 ("ちょっと（　　）ください。", "出して", "足して", 1, "ちょっとたしてください。", "足(た)して = add. 出(だ)して = take out / submit. Only ゛ difference: た vs だ."),
 ("実はすごく（　　）んです。", "言いたかった", "痛かった", 0, "じつはすごく、いいたかったんです。", "言(い)いたかった = wanted to say: い・い・た. 痛(いた)かった = it hurt: い・た. One extra い."),
 ("あれ、（　　）。", "今日かな", "着ようかな", 1, "あれ、きようかな。", "着(き)ようかな = shall I wear it? (き・よ・う). 今日(きょう)かな = is it today? (きょ・う, 拗音). Small ょ vs big よ."),
 ("天気は（　　）そうです。", "よくない", "よくなり", 0, "天気はよくないそうです。", "よくないそうです = I hear it won't be good (hearsay). よくなりそうです = looks like it will get better. な・い vs な・り."),
 ("これ、（　　）送りましょう。", "教授に", "今日中に", 1, "これ、きょうじゅうに送りましょう。", "今日中(きょうじゅう)に = within today: long う after じゅ. 教授(きょうじゅ)に = to the professor."),
 ("お客さんが（　　）来ました。", "急に", "9人", 0, "お客さんが、きゅうにきました。", "急(きゅう)に = suddenly. 9人(きゅうにん) = 9 people: has ん. 急に has no ん."),
]

W13 = [  # (first line, a, b, c, ans, thanglish)
 ("男：あした、病院へ行きます。", "どこか具合が悪いんですか。", "髪を切るんですか。", "何を買うんですか。", 0,
  "病院(びょういん) = hospital → '具合(ぐあい)が悪いんですか' (are you unwell?). 髪を切る = 美容院 (beauty salon) answer. Sound-a correct-aa kettaa dhaan answer varum."),
 ("女：来週、試験なんです。", "おめでとうございます。", "真剣ですね。", "がんばってくださいね。", 2,
  "試験(しけん) = exam → 'がんばって' (all the best). 真剣(しんけん) is a trap built from the similar sound."),
 ("男：このコーヒー、ちょっとぬるいですね。", "もう少し冷ましましょうか。", "温め直しましょうか。", "濃いのにしましょうか。", 1,
  "ぬるい = lukewarm. So reheat: 温(あたた)め直(なお)す. 冷(さ)ます = cool down = opposite. 濃(こ)い = strong, not about temperature."),
 ("女：これ、今日中にお願いできますか。", "はい、教授に渡します。", "はい、夕方までにやります。", "はい、昨日やりました。", 1,
  "今日中(きょうじゅう)に = by end of today → 'by evening I'll do it'. 教授(きょうじゅ) is the sound trap."),
 ("男：先週の試合、選手が9人しか来なかったんだって。", "えっ、それで試合できたの？", "急に来られても困るよね。", "3位になったんだね。", 0,
  "9人(きゅうにん)しか来(こ)なかった = only 9 people came → 'then could you even play?'. 急(きゅう)に is the sound trap; 3位 doesn't follow."),
 ("女：このスープ、少し塩を足してくれる？", "はい、出しますね。", "はい、これくらいでいい？", "はい、脱いでおきます。", 1,
  "足(た)して = add (salt) → 'this much OK?'. 出(だ)します is the ゛ trap."),
 ("男：新しいコート、あした着ようかな。", "今日は寒くないよ。", "今日かなって、もう夜だよ。", "あしたは雨らしいから、やめたほうがいいよ。", 2,
  "着(き)ようかな = maybe I'll wear it (tomorrow). Reply about tomorrow's rain fits. 'b' mishears it as 今日(きょう)かな."),
]

def opts_line(a, b, c=None):
    return "a　" + a + "　　b　" + b + ("　　c　" + c if c else "")

SECTION = {
 "book": "chokai",
 "title": "実力養成編　Ⅰ 音声の特徴に慣れる　1 似ている音の聞き分け",
 "source": "新完全マスター聴解 N2 · 実力養成編 Ⅰ-1 · pp.14–15 · CD A07–A09 (read-aloud)",
 "blocks": [
  text("発音が似ている言葉の聞き取りを間違えると、文全体の意味がわからなくなることがあります。「゛」や小さい「っ」「ゃ／ゅ／ょ」で表す音、「ん」や長音（おかあさん／コーヒー）など、間違えやすい音とともに、アクセントやイントネーションなどに気をつけて聞きましょう。",
   "1　似ている音の聞き分け",
   ["Inniki 'similar sounds' training. Japanese-la oru beat (拍 はく) maarinaa vera word aayidum: びょういん (hospital) vs びよういん (beauty salon).",
    "Watch: ゛ (か/が), small っ (きて/きって), small ゃゅょ (きょう/きよう), ん (きねん/きんえん), long vowel (おばさん/おばあさん). Kai thatti beats count pannunga — adhu dhaan best trick."]),

  audio("練習1-1　CD A07", "a07", "言葉を聞いてください。その{後|あと}に聞くa～cの言葉の中で、最初の言葉と同じものはどれですか。", note=OWN),
  group("練習1-1", [hear("d3c-11-%d" % i, "（例）" if i == 0 else "(%d)" % i, w[4],
     "Answer %s. %s" % ("abc"[w[4]], w[5])) for i, w in enumerate(W11)]),
  script("練習1-1　スクリプトと答え · open after you answer",
   [(("（例）" if i == 0 else "(%d)" % i) + "　" + w[0] + "　→　" + opts_line(w[1], w[2], w[3]), "Answer %s. %s" % ("abc"[w[4]], w[5])) for i, w in enumerate(W11)],
   extra=[text("答え　（例）c　(1) a　(2) b　(3) c　(4) b　(5) a　(6) a　(7) b　(8) a　(9) b　(10) c", "答え", "Sensei's set — the book has no key for this track.")]),

  audio("練習1-2　CD A08", "a08", "文を聞いてください。どちらですか。",
   note="⚠ The choices are the book's. The book prints no script, so which word is read aloud is sensei's choice; the key below matches this read-aloud, not the real CD."),
  group("練習1-2", [mcq("d3c-12-%d" % i, ("（例）" if i == 0 else "(%d)　" % i) + w[0], [w[1], w[2]], w[3], "Answer %s. %s" % ("ab"[w[3]], w[5]), keys=["a", "b"]) for i, w in enumerate(W12)]),
  script("練習1-2　スクリプトと答え · open after you answer",
   [(("（例）" if i == 0 else "(%d)　" % i) + w[0].replace("（　　）", "（" + (w[1], w[2])[w[3]] + "）"), w[5]) for i, w in enumerate(W12)],
   extra=[text("答え　（例）b　(1) a　(2) b　(3) a　(4) b　(5) b　(6) a　(7) b　(8) a　(9) b　(10) a", "答え")]),

  audio("練習1-3　CD A09", "a09", "文を聞いて、それに対する返事の文を聞き、最もよいものを選んでください。", note=OWN),
  group("練習1-3", [hear("d3c-13-%d" % i, "（例）" if i == 0 else "(%d)" % i, w[4], "Answer %s. %s" % ("abc"[w[4]], w[5])) for i, w in enumerate(W13)]),
  script("練習1-3　スクリプトと答え · open after you answer",
   [(("（例）" if i == 0 else "(%d)　" % i) + w[0] + "\n" + opts_line(w[1], w[2], w[3]), "Answer %s. %s" % ("abc"[w[4]], w[5])) for i, w in enumerate(W13)],
   extra=[text("答え　（例）a　(1) c　(2) b　(3) b　(4) a　(5) b　(6) c", "答え", "Ovvoru question-layum oru 'similar sound' trap irukku. Wrong option eppadi trap pannudhu-nu paarunga.")]),
 ],
}
