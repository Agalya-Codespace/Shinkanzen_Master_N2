/* Day 1 · 文法 (新完全マスター文法 N2, 第1部 Ⅰ 1課, pp.8–11). Transcribed from the book scan.
   Answers are from the book's 別冊 解答. */
window.N2_DAYS = window.N2_DAYS || {};
window.N2_DAYS[1] = window.N2_DAYS[1] || { sections: [] };

(function () {
  var A = ["a", "b", "c"];
  function q(id, text, opts, ans, explain) { return { type: "mcq", id: id, q: text, opts: opts, keys: A, ans: ans, explain: explain }; }

  window.N2_DAYS[1].sections.push({
    book: "bunpo",
    title: "Ⅰ ことがらを{説明|せつめい}する☆　1{課|か}　～とき・～{直後|ちょくご}に",
    source: "新完全マスター文法 N2 · 第1部 文の文法1 · pp.8–11",
    blocks: [
      {
        type: "items",
        title: "〔{復習|ふくしゅう}〕",
        items: [
          { t: "・{母|はは}は{新聞|しんぶん}を{読|よ}む[[とき]]、{眼鏡|めがね}をかけます。", explain: "Review: ～とき = when ～. 'Amma newspaper padikkum podhu kannaadi podurvaanga.' Inniki padikkira 際(さい) idhoda formal version." },
          { t: "・{窓|まど}を{開|あ}ける[[と]]すぐに、{涼|すず}しい{風|かぜ}が{入|はい}ってき[[た]]。", explain: "Review: ～とすぐに = as soon as ～. 'Window thirandha udane cool kaathu vandhuchu.' Inniki padikkira たとたん, かと思うと, か～ないかのうちに ellam 'right after' type expressions." }
        ],
        explain: "Indha lesson title: ～とき (when) and ～直後(ちょくご)に (right after). Mudhal 2 grammar 'when' type (formal), adutha 3 'immediately after' type. Seri, start pannalaam!"
      },
      {
        type: "grammar",
        no: "1",
        title: "～{際|さい}(に)",
        meaning: "～とき",
        tag: "硬い言い方",
        explain: [
          "際(さい)(に) = とき, but 硬(かた)い言い方 = formal/stiff way of saying. Notices, announcements, office, hotel — idhula dhaan adhigam varum.",
          "Shape: Noun + の + 際 (商品受け取りの際), Verb dictionary/た form + 際 (ご利用になる際, 来日した際に).",
          "Kavanam: daily life casual vishayathukku use panna maattom. '朝ご飯を食べる際' — weird! Action or event verbs/nouns (使う, 完成する, 搭乗, 外出) kooda dhaan."
        ],
        examples: [
          { t: "①この{整理券|せいりけん}は、{商品受|しょうひんう}け{取|と}りの[[{際|さい}]]、{必要|ひつよう}です。", explain: "整理券(せいりけん) = numbered ticket / token. 商品受(しょうひんう)け取(と)り = receiving goods. 'Product vaangum podhu indha token venum.' Noun + の + 際." },
          { t: "②こちらの{会議室|かいぎしつ}をご{利用|りよう}になる[[{際|さい}]]は、{受付|うけつけ}で{必要事項|ひつようじこう}をご{記入|きにゅう}ください。", explain: "会議室(かいぎしつ) = meeting room. ご利用(りよう)になる = (honorific) use. 受付(うけつけ) = reception. 必要事項(ひつようじこう) = required details. ご記入(きにゅう)ください = please fill in. Typical formal notice." },
          { t: "③アメリカの{大統領|だいとうりょう}は{来日|らいにち}した[[{際|さい}に]]、わたしたちの{大学|だいがく}でスピーチを{行|おこな}った。", explain: "大統領(だいとうりょう) = president (of a country). 来日(らいにち)する = come to Japan. 行(おこな)う = conduct. た-form + 際に = when (he) came." }
        ],
        form: "［名］－の・［動］{辞書形|じしょけい}／た{形|けい}　＋{際|さい}(に)",
        caution: "{主|おも}に{行為|こうい}や{出来事|できごと}を{表|あらわ}す{動詞|どうし}（{使|つか}う・{完成|かんせい}するなど）・{名詞|めいし}（{搭乗|とうじょう}・{外出|がいしゅつ}など）につく。{公的|こうてき}な{場面|ばめん}などで{多|おお}く{使|つか}い、{日常|にちじょう}の{普通|ふつう}のことにはあまり{使|つか}わない。"
      },
      {
        type: "grammar",
        no: "2",
        title: "～に{際|さい}して・～にあたって",
        meaning: "～するとき",
        tag: "硬い言い方",
        explain: [
          "に際(さい)して / にあたって = when doing ～ (on the occasion of). Formal.",
          "Important difference from 際: idhu 'その場1回だけの、意志的で特別な時' — one-time, intentional, special occasion (kalyaanam, new shop thirappu, business start). Appuram varra sentence-la oru action irukkanum (greet pannrom, prepare pannrom, help vaangrom).",
          "～にあたって is more positive & active. Negative events (別れ separation, 入院 hospitalisation, 倒産 bankruptcy) kooda にあたって use panna maattom.",
          "Polite forms: にあたりまして (speech), にあたり (written)."
        ],
        examples: [
          { t: "①{工事関係者|こうじかんけいしゃ}は{工事|こうじ}を{始|はじ}める[[に{際|さい}して]]、{近所|きんじょ}の{住民|じゅうみん}にあいさつをして{回|まわ}った。", explain: "工事関係者(こうじかんけいしゃ) = construction staff. 住民(じゅうみん) = residents. あいさつをして回(まわ)る = go around greeting. 'Construction start pannum podhu, pakkathu veetu kaarangalukku greet panni ponaanga.'" },
          { t: "②{当|とう}ショッピングサイトのご{利用|りよう}[[に{際|さい}して]]、{以下|いか}のご{利用条件|りようじょうけん}をよくお{読|よ}みください。", explain: "当(とう)～ = this ～ (our). 利用条件(りようじょうけん) = terms of use. Website terms-la typical sentence." },
          { t: "③{新|あたら}しく{事業|じぎょう}を{始|はじ}める[[にあたって]]、しっかりと{準備|じゅんび}をしようと{思|おも}っております。", explain: "事業(じぎょう) = business/enterprise. 準備(じゅんび) = preparation. Positive, active start → にあたって." },
          { t: "④お{二人|ふたり}の{門出|かどで}[[にあたりまして]]、お{祝|いわ}いの{言葉|ことば}を{申|もう}し{上|あ}げます。", explain: "門出(かどで) = a new start (here: wedding). お祝(いわ)いの言葉 = congratulatory words. 申(もう)し上(あ)げる = humble 'say'. Wedding speech-la kekkalaam." },
          { t: "⑤{日本|にほん}で{国際会議|こくさいかいぎ}を{開催|かいさい}する[[にあたり]]、{関係各方面|かんけいかくほうめん}からの{協力|きょうりょく}を{得|え}た。", explain: "国際会議(こくさいかいぎ) = international conference. 開催(かいさい)する = hold (an event). 関係各方面(かんけいかくほうめん) = all related parties. 協力(きょうりょく)を得(え)る = get cooperation." }
        ],
        form: "［名］・［動］{辞書形|じしょけい}　＋に{際|さい}して・にあたって",
        caution: "その{場|ば}1{回|かい}だけの、{意志的|いしてき}で{特別|とくべつ}な{時|とき}を{表|あらわ}す{言葉|ことば}（{結婚|けっこん}・{店|みせ}を{開|ひら}くなど）につく。{後|あと}には、{主|おも}に{行為|こうい}を{表|あらわ}す{文|ぶん}が{来|く}る。「～にあたって」は、より{積極的|せっきょくてき}な{行動|こうどう}を{表|あらわ}す{言葉|ことば}につき、マイナスイメージの{言葉|ことば}（{別|わか}れ・{入院|にゅういん}・{倒産|とうさん}など）にはつかない。"
      },
      {
        type: "grammar",
        no: "3",
        title: "～たとたん(に)",
        meaning: "～したら、{直後|ちょくご}に{意外|いがい}なことが{起|お}こる。",
        explain: [
          "たとたん(に) = the moment ～, (something unexpected) happened. Key point: 意外(いがい) = unexpected / surprising result.",
          "Verb た-form + とたん(に). Verb should be instant action/change (立ち上がる, 変わる, 着く).",
          "After-part: speaker's wish/intention (～よう, ～たい) or request (～ませんか, ～なさい) varakoodaadhu. Already nadandha surprising event mattum.",
          "Tamil feel: 'appadi pannina udane, enna aachu theriyumaa…!'"
        ],
        examples: [
          { t: "①{山|やま}の{頂上|ちょうじょう}でワインを{一口|ひとくち}{飲|の}ん[[だとたんに]]、めまいがした。", explain: "頂上(ちょうじょう) = summit. 一口(ひとくち) = one sip. めまいがする = feel dizzy. 'Malai uchiyila wine oru sip kudichadhum, thalai suthuchu.'" },
          { t: "②{夫|おっと}は{結婚前|けっこんまえ}は{優|やさ}しかったが、{結婚|けっこん}し[[たとたんに]]、{態度|たいど}が{変|か}わった。", explain: "夫(おっと) = (my) husband. 態度(たいど) = attitude. 'Kalyaanathukku munnadi nalla irundhaar, kalyaanam aanadhum attitude maariduchu!' Unexpected → たとたん." },
          { t: "③{国|くに}の{母|はは}に{電話|でんわ}をかけた。{母|はは}の{声|こえ}を{聞|き}い[[たとたん]]、{涙|なみだ}があふれてきた。", explain: "涙(なみだ)があふれる = tears overflow. 'Amma voice kettadhum kanneer vandhuduchu.'" },
          { t: "④{僕|ぼく}が「さよなら」と{言|い}っ[[たとたん]]、{彼女|かのじょ}は{走|はし}っていってしまった。", explain: "'Naan bye sonnadhum, aval odi poyitta.' ～てしまった shows regret/surprise." }
        ],
        form: "［動］た{形|けい}　＋とたん(に)",
        caution: "{瞬間的|しゅんかんてき}な{動|うご}きや{変化|へんか}を{表|あらわ}す{動詞|どうし}（{立|た}ち{上|あ}がる・{変|か}わるなど）につく。{後|あと}の{文|ぶん}は{意外性|いがいせい}のある{内容|ないよう}。{話者|わしゃ}の{希望|きぼう}・{意向|いこう}を{表|あらわ}す{文|ぶん}（～ようなど）や{働|はたら}きかけの{文|ぶん}（～ませんか・～なさいなど）は{来|こ}ない。"
      },
      {
        type: "grammar",
        no: "4",
        title: "～(か)と{思|おも}うと・～(か)と{思|おも}ったら",
        meaning: "～の{後|あと}、すぐに{続|つづ}いて{次|つぎ}の{出来事|できごと}や{大|おお}きな{変化|へんか}が{起|お}こる。",
        explain: [
          "(か)と思うと / (か)と思ったら = no sooner had ～ than ～. Oru vishayam nadandha udane, adutha event or big change.",
          "Very important rule: 話者(わしゃ)の行為については使わない — speaker's own action-ku use panna maattom. 'わたしは…かと思うと' wrong! Others (林さん, 赤ちゃん, 子供たち, weather) mattum.",
          "Result is slightly surprising. Wish/intention/request sentences varakoodaadhu.",
          "Tip: 'Ippo dhaan ～ nu nenachen, adhukkulla ～!' — Tamil-la apdiye feel pannunga."
        ],
        examples: [
          { t: "①{林|はやし}さんは{部屋|へや}に{入|はい}ってきた[[かと{思|おも}うと]]、いきなり{窓|まど}を{全部|ぜんぶ}{開|あ}けた。", explain: "いきなり = suddenly. 'Hayashi-san room-ku vandhaar, udane ella window-um thirandhuttaar.'" },
          { t: "②{赤|あか}ちゃんは{今泣|いまな}いた[[と{思|おも}うと]]、もう{笑|わら}っている。", explain: "'Baby ippo dhaan azhudhuchu, adhukkulla sirikkudhu!' Big change quickly." },
          { t: "③やっと{部屋|へや}が{片付|かたづ}いた[[かと{思|おも}ったら]]、{子供|こども}たちがすぐまた{散|ち}らかした。", explain: "片付(かたづ)く = get tidied. 散(ち)らかす = make a mess. 'Room-a oru vazhiyaa clean panninen nu nenachen, pasanga udane thirumba kalachittaanga.' Subject is 部屋/子供たち, not speaker's action directly." },
          { t: "④このごろは{気温|きおん}の{差|さ}が{大|おお}きい。{昨日|きのう}は{暑|あつ}くなった[[かと{思|おも}ったら]]、{今日|きょう}は{涼|すず}しい。", explain: "気温(きおん)の差(さ) = temperature difference. 'Nethu veyil nu nenachaa, inniki cool-aa irukku.'" }
        ],
        form: "［動］た{形|けい}　＋(か)と{思|おも}うと・(か)と{思|おも}ったら",
        caution: "{話者|わしゃ}の{行為|こうい}については{使|つか}わない。{後|あと}の{文|ぶん}は{少|すこ}し{意外性|いがいせい}のある{内容|ないよう}。{話者|わしゃ}の{希望|きぼう}・{意向|いこう}を{表|あらわ}す{文|ぶん}や{働|はたら}きかけの{文|ぶん}は{来|こ}ない。"
      },
      {
        type: "grammar",
        no: "5",
        title: "～か～ないかのうちに",
        meaning: "～が{終|お}わると{同時|どうじ}に、{次|つぎ}のことが{起|お}こる。",
        explain: [
          "Vか Vないかのうちに = almost at the same time as ～ (before ～ is even finished). Literally 'within (the time of) whether it did or didn't'.",
          "Form: dictionary/た form + か + same verb ない form + かのうちに. 横になるかならないかのうちに, 明けたか明けないかのうちに.",
          "Compared with (か)と思うと, idhu 'ほとんど同時に' (almost simultaneous) feeling stronger.",
          "Again: instant verbs (着く, 終わる). After-part: no volition/requests."
        ],
        examples: [
          { t: "①{一郎|いちろう}はベッドに{横|よこ}になる[[か]]なら[[ないかのうちに]]、ぐっすり{眠|ねむ}ってしまった。", explain: "横(よこ)になる = lie down. ぐっすり眠(ねむ)る = sleep soundly. 'Ichiro bed-la padukkaradhukkulla gaadamaa thoongiduttaan.'" },
          { t: "②わたしは{夜|よる}が{明|あ}けた[[か]]{明|あ}け[[ないかのうちに]]{家|いえ}を{出|で}て、{空港|くうこう}へ{向|む}かった。", explain: "夜が明(あ)ける = dawn breaks. 'Vidiyaradhukkulla veetai vittu kilambi airport ponen.' (Here speaker's action is OK — the rule of no-speaker-action is only for (か)と思うと.)" },
          { t: "③あの{作家|さっか}は{今売|いまう}れっ{子|こ}だ。{話題作|わだいさく}を{発表|はっぴょう}した[[か]]し[[ないかのうちに]]、もう{次|つぎ}の{作品|さくひん}に{取|と}りかかっているそうだ。", explain: "売(う)れっ子(こ) = popular person (in demand). 話題作(わだいさく) = much-talked-about work. 発表(はっぴょう)する = publish/release. 取(と)りかかる = start on. 'Hit book release aanadhum udane next book start pannittaaraam.'" }
        ],
        form: "［動］{辞書形|じしょけい}／た{形|けい}　＋か＋［動］ない{形|けい}　＋かのうちに",
        caution: "{瞬間的|しゅんかんてき}な{動|うご}きや{変化|へんか}を{表|あらわ}す{動詞|どうし}（{着|つ}く・{終|お}わるなど）につく。{後|あと}には、{話者|わしゃ}の{意向|いこう}を{表|あらわ}す{文|ぶん}や{働|はたら}きかけの{文|ぶん}は{来|こ}ない。「～(か)と{思|おも}うと・～(か)と{思|おも}ったら」より、「ほとんど{同時|どうじ}に」という{気持|きも}ちが{強|つよ}い。"
      },
      {
        type: "group",
        title: "【1】",
        lead: "a～cの{中|なか}から{最|もっと}も{良|よ}いものを{選|えら}ぶ（本書の使い方より）。（～際(に)）",
        scored: true,
        children: [
          q("d1b-1-1", "1　（　　）{際|さい}に、{家|いえ}の{中|なか}で{修理|しゅうり}をするところがあるかどうか{調|しら}べておく{必要|ひつよう}がある。", ["いい{天気|てんき}の", "{大掃除|おおそうじ}の", "{時間|じかん}がある"], 1, "大掃除(おおそうじ)の際に = at the time of the big cleaning. 際 needs an event/action. いい天気 and 時間がある are just states, so no." ),
          q("d1b-1-2", "2　（　　）{際|さい}、{音|おと}が{出|で}る{電子辞書|でんしじしょ}は{大変便利|たいへんべんり}です。", ["{発音|はつおん}が{難|むずか}しい", "{発音|はつおん}がわからない", "{発音|はつおん}を{調|しら}べる"], 2, "発音を調べる際 = when checking pronunciation (an action). 難しい / わからない are states → 際 doesn't fit."),
          q("d1b-1-3", "3　（　　）{際|さい}は、こちらのテーブルをお{使|つか}いいただけます。", ["お{食事|しょくじ}の", "ご{飯|はん}を{食|た}べる", "お{一人様|ひとりさま}の"], 0, "お食事の際は = when dining (formal, restaurant notice). ご飯を食べる is everyday casual — 際 is for formal/public scenes. お一人様 is a person, not an event."),
          q("d1b-1-4", "4　（　　）{際|さい}は、{以下|いか}のことに{注意|ちゅうい}してください。", ["{毎日学校|まいにちがっこう}へ{行|い}く", "{寮|りょう}での{生活|せいかつ}の", "{健康診断|けんこうしんだん}を{受|う}ける"], 2, "健康診断(けんこうしんだん)を受ける際 = when taking a health check-up — a specific event. 毎日 = daily routine; 寮(りょう)での生活 = ongoing life, not one occasion."),
          q("d1b-1-5", "5　{地震|じしん}の{際|さい}は、（　　）。", ["{慌|あわ}てずに{行動|こうどう}しなければならない", "{慌|あわ}てちゃだめ", "{慌|あわ}てていない"], 0, "地震(じしん)の際は、慌(あわ)てずに行動(こうどう)しなければならない = in an earthquake, you must act without panicking. 慌てちゃだめ is casual speech — doesn't match the formal 際. 慌てていない (is not panicking) doesn't make sense as advice.")
        ]
      },
      {
        type: "group",
        title: "【2】",
        lead: "a～cの{中|なか}から{最|もっと}も{良|よ}いものを{選|えら}ぶ（本書の使い方より）。（～に際して・～にあたって）",
        scored: true,
        children: [
          q("d1b-2-1", "1　{父|ちち}は（　　）に{際|さい}して、{医者|いしゃ}にいろいろ{質問|しつもん}した。", ["{病気|びょうき}が{回復|かいふく}する", "{手術|しゅじゅつ}を{受|う}ける", "{毎日病院|まいにちびょういん}へ{行|い}く"], 1, "手術(しゅじゅつ)を受けるに際して = on the occasion of having surgery — one-time, special, intentional. 回復(かいふく)する is not intentional; 毎日 is routine."),
          q("d1b-2-2", "2　{研修旅行|けんしゅうりょこう}に{際|さい}して、（　　）。", ["{体調|たいちょう}が{良|よ}くなかった", "{天候|てんこう}が{気|き}がかりだった", "{説明会|せつめいかい}が{開|ひら}かれた"], 2, "After に際して comes an action: 説明会(せつめいかい)が開かれた (a briefing was held). 体調 (health condition) and 天候が気がかり (worried about weather) are states/feelings."),
          q("d1b-2-3", "3　（　　）にあたって、{必要|ひつよう}な{書類|しょるい}を{準備|じゅんび}した。", ["{出勤|しゅっきん}する", "{留学|りゅうがく}する", "{図書館|としょかん}へ{行|い}く"], 1, "留学(りゅうがく)するにあたって = when going to study abroad — a special one-time event. 出勤 (going to work) and going to the library are ordinary."),
          q("d1b-2-4", "4　{新|あたら}しいオフィスへの{移転|いてん}にあたりまして、（　　）。", ["{気持|きも}ちも{新|あたら}しくなりました", "{非常|ひじょう}にうれしいです", "{一言|ひとこと}ごあいさつ{申|もう}し{上|あ}げます"], 2, "移転(いてん) = relocation. After にあたりまして we need an action: 一言(ひとこと)ごあいさつ申し上げます (let me say a few words). Feelings (a, b) don't fit.")
        ]
      },
      {
        type: "group",
        title: "【3】",
        lead: "a～cの{中|なか}から{最|もっと}も{良|よ}いものを{選|えら}ぶ（本書の使い方より）。（～たとたん(に)）",
        scored: true,
        children: [
          q("d1b-3-1", "1　（　　）とたん、{眠|ねむ}くなった。", ["{勉強|べんきょう}が{終|お}わった", "{勉強|べんきょう}をした", "{勉強|べんきょう}をしていた"], 0, "とたん needs an instant change: 勉強が終わったとたん (the moment studying ended) → got sleepy. 勉強をした (studied — a long activity) and していた (was studying) are not instant."),
          q("d1b-3-2", "2　（　　）とたんに、{気分|きぶん}が{悪|わる}くなってしまった。", ["ゴールに{向|む}かっていた", "ゴールに{近|ちか}くなった", "ゴールインした"], 2, "ゴールインした = crossed the finish line (one instant) → とたんに felt sick. 向かっていた (ongoing) and 近くなった (gradual) are not instant moments."),
          q("d1b-3-3", "3　{彼女|かのじょ}はわたしの{顔|かお}を{見|み}たとたんに、（　　）。", ["{泣|な}き{出|だ}した", "あいさつした", "うれしそうだった"], 0, "After とたん comes something unexpected: 泣(な)き出(だ)した (burst into tears). あいさつ is normal/expected; うれしそうだった is just a state."),
          q("d1b-3-4", "4　{電車|でんしゃ}が{駅|えき}に{着|つ}いたとたん、（　　）。", ["{友達|ともだち}に{電話|でんわ}をしよう", "{乗客|じょうきゃく}が{大勢乗|おおぜいの}り{込|こ}んできた", "{乗|の}りかえのホームに{行|い}った"], 1, "乗客(じょうきゃく)が大勢(おおぜい)乗り込んできた = lots of passengers rushed in (unexpected event). a is speaker's intention (しよう) — not allowed. c is just the planned, expected action.")
        ]
      },
      {
        type: "group",
        title: "【4】",
        lead: "a～cの{中|なか}から{最|もっと}も{良|よ}いものを{選|えら}ぶ（本書の使い方より）。（～(か)と思うと・～(か)と思ったら）",
        scored: true,
        children: [
          q("d1b-4-1", "1　（　　）{車|くるま}から{降|お}りたかと{思|おも}うと、{海|うみ}に{向|む}かって{走|はし}り{出|だ}した。", ["わたしは", "わたしたちは", "あの{子|こ}は"], 2, "(か)と思うと is not used for the speaker's own actions. So わたし / わたしたち are wrong; あの子は is right."),
          q("d1b-4-2", "2　さっきまで{大雨|おおあめ}が{降|ふ}っていたかと{思|おも}うと、{今|いま}は（　　）。", ["{雨|あめ}は{弱|よわ}くなった", "{太陽|たいよう}が{出|で}ている", "{雨|あめ}はさらに{激|はげ}しくなった"], 1, "Big, surprising change: heavy rain → now the sun is out (太陽が出ている). 'Rain got weaker/stronger' is not a big change."),
          q("d1b-4-3", "3　7{時|じ}の{時報|じほう}が{鳴|な}ったかと{思|おも}うと、（　　）。", ["ニュースが{始|はじ}まる", "{時計|とけい}のベルも{鳴|な}っていた", "{彼|かれ}は{突然立|とつぜんた}ち{上|あ}がった"], 2, "時報(じほう) = time signal. 'As soon as the 7 o'clock signal sounded, he suddenly stood up' — a next event, a bit surprising. a is non-past and expected; b is a background state."),
          q("d1b-4-4", "4　サッカーの{試合|しあい}が{始|はじ}まったかと{思|おも}うと、テレビの{前|まえ}に（　　）。", ["{人|ひと}が{大勢集|おおぜいあつ}まってきた", "{集|あつ}まろうよ", "{座|すわ}っていいですか"], 0, "After (か)と思うと no invitation (集まろうよ) or request (座っていいですか). 人が大勢集まってきた is a past event.")
        ]
      },
      {
        type: "group",
        title: "【5】",
        lead: "a～cの{中|なか}から{最|もっと}も{良|よ}いものを{選|えら}ぶ（本書の使い方より）。（～か～ないかのうちに）",
        scored: true,
        children: [
          q("d1b-5-1", "1　{弟|おとうと}は、やっと{見|み}つけた{就職先|しゅうしょくさき}なのに、（　　）のうちに、もう{辞|や}めてしまった。", ["{仕事|しごと}を{覚|おぼ}えたか{覚|おぼ}えないか", "{働|はたら}いているかいないか", "{友達|ともだち}がいるかいないか"], 0, "就職先(しゅうしょくさき) = workplace he got a job at. 覚えたか覚えないかのうちに = before he'd barely learned the job, he quit. Needs a change verb; いる (state) doesn't fit."),
          q("d1b-5-2", "2　あの{学生|がくせい}は、{試験|しけん}が{始|はじ}まって（　　）のうちに、{教室|きょうしつ}を{出|で}ていった。", ["よく{考|かんが}えたか{考|かんが}えないか", "10{分|ぷん}たったかたたないか", "{頑張|がんば}ったか{頑張|がんば}らないか"], 1, "10分たったかたたないかのうちに = barely 10 minutes in, he left the room. Time passing (たつ) is a clear moment."),
          q("d1b-5-3", "3　{雨|あめ}がやんだかやまないかのうちに、（　　）。", ["せみが{鳴|な}き{出|だ}した", "{試合|しあい}を{再開|さいかい}しよう", "{出発|しゅっぱつ}したい"], 0, "After か～ないかのうちに: no intention (しよう) or wish (したい). せみが鳴き出した (cicadas started singing) is a fact."),
          q("d1b-5-4", "4　{森|もり}さんは{部長|ぶちょう}の{話|はなし}が{終|お}わるか{終|お}わらないかのうちに、{会議室|かいぎしつ}の{方|ほう}へ（　　）。", ["{走|はし}っていってください", "{走|はし}っていった", "{走|はし}っていったほうがいい"], 1, "部長(ぶちょう) = department manager. Request (ください) and advice (ほうがいい) can't come after. 走っていった (ran off) is right.")
        ]
      },
      {
        type: "group",
        title: "【1～5】",
        lead: "a～cの{中|なか}から{最|もっと}も{良|よ}いものを{選|えら}ぶ（本書の使い方より）。",
        scored: true,
        children: [
          q("d1b-m-1", "1　{一|ひと}つの{問題|もんだい}が（　　）、すぐ{次|つぎ}の{問題|もんだい}を{渡|わた}された。", ["{終|お}わった{際|さい}に", "{終|お}わるにあたって", "{終|お}わったかと{思|おも}うと"], 2, "'Right after one problem finished, the next was handed over' → 終わったかと思うと. 際 is just 'when' (formal), not 'immediately'; にあたって is for special intentional occasions."),
          q("d1b-m-2", "2　やっと{来|き}たバスに（　　）、{忘|わす}れ{物|もの}に{気|き}がついた。", ["{乗|の}った{際|さい}に", "{乗|の}るにあたって", "{乗|の}ったとたん"], 2, "'The moment I got on the bus, I realised I'd forgotten something' — unexpected → 乗ったとたん."),
          q("d1b-m-3", "3　テニスコートをお{使|つか}いになる（　　）、{事務所|じむしょ}でロッカーのかぎをお{受|う}け{取|と}りください。", ["{際|さい}は", "にあたって", "かならないかのうちに"], 0, "Formal notice: お使いになる際は = when you use (the court). にあたって is for special one-time events, not using a tennis court."),
          q("d1b-m-4", "4　{選挙|せんきょ}に（　　）、{大勢|おおぜい}の{方|かた}に{協力|きょうりょく}を{依頼|いらい}した。", ["{出|で}るにあたって", "{出|で}たとたんに", "{出|で}たかと{思|おも}うと"], 0, "選挙(せんきょ)に出る = run in an election — special, intentional, one-time. 出るにあたって, asked many people for help (依頼(いらい)した).")
        ]
      }
    ]
  });
})();
