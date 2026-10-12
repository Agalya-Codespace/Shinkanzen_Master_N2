/* Shinkanzen Master N2 – 20-day study site.
   Plain JS, no build step. Content lives in data/*.js (window.N2_PLAN, window.N2_DAYS).
   Text markup used in the data files:
     {漢字|かんじ}  -> ruby (furigana)
     [[text]]       -> underlined (the book's underline)
     **text**       -> bold
*/
(function () {
  "use strict";

  var STORE_KEY = "n2-shinkanzen-progress-v1";
  var BOOKS = {
    kanji: { jp: "漢字", en: "Kanji" },
    goi: { jp: "語彙", en: "Vocabulary" },
    bunpo: { jp: "文法", en: "Grammar" },
    dokkai: { jp: "読解", en: "Reading" },
    chokai: { jp: "聴解", en: "Listening" }
  };
  var BOOK_ORDER = ["kanji", "goi", "bunpo", "dokkai", "chokai"];
  // A book counts towards progress only on days whose plan lists pages for it.
  function booksFor(plan) { return BOOK_ORDER.filter(function (bk) { return plan && plan[bk]; }); }

  // ---------- storage (always guarded) ----------
  function load() {
    try {
      var raw = localStorage.getItem(STORE_KEY);
      var s = raw ? JSON.parse(raw) : null;
      if (s && typeof s === "object") {
        s.done = s.done || {}; s.answers = s.answers || {}; s.prefs = s.prefs || {};
        return s;
      }
    } catch (e) { /* storage blocked: run without saving */ }
    return { done: {}, answers: {}, prefs: {} };
  }
  var state = load();
  function save() {
    try { localStorage.setItem(STORE_KEY, JSON.stringify(state)); } catch (e) { /* ignore */ }
  }

  // ---------- markup ----------
  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }
  function md(s) {
    if (s == null) return "";
    var out = esc(s);
    out = out.replace(/\{([^|{}]+)\|([^{}]+)\}/g, "<ruby>$1<rt>$2</rt></ruby>");
    out = out.replace(/\[\[(.+?)\]\]/g, "<u>$1</u>");
    out = out.replace(/\*\*(.+?)\*\*/g, "<b>$1</b>");
    out = out.replace(/\n/g, "<br>");
    return out;
  }
  function plain(s) { return String(s).replace(/\{([^|{}]+)\|[^{}]+\}/g, "$1"); }
  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }

  // ---------- explanation button ----------
  var explainSeq = 0;
  function explainParts(explain) {
    // explain may be a string or an array of paragraphs
    var paras = Array.isArray(explain) ? explain : [explain];
    return paras.map(function (p) { return "<p>" + md(p) + "</p>"; }).join("");
  }
  function addExplain(host, explain, label) {
    if (!explain) return;
    var id = "ex" + (++explainSeq);
    var btn = el("button", "explain-btn", label || "Explain 💡");
    btn.type = "button";
    btn.setAttribute("aria-expanded", "false");
    btn.setAttribute("aria-controls", id);
    var box = el("div", "explain");
    box.id = id;
    box.hidden = true;
    box.innerHTML = '<span class="who">Sensei explains · Thanglish + ひらがな</span>' + explainParts(explain);
    btn.addEventListener("click", function () {
      var open = box.hidden;
      box.hidden = !open;
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    return { btn: btn, box: box };
  }
  function lineWithExplain(html, explain, tag) {
    var li = el(tag || "div");
    var row = el("div", "row");
    row.appendChild(el("div", "txt", html));
    var ex = addExplain(row, explain);
    if (ex) { row.appendChild(ex.btn); li.appendChild(row); li.appendChild(ex.box); }
    else li.appendChild(row);
    return li;
  }

  // ---------- block renderers ----------
  var R = {};

  R.text = function (b) {
    var d = el("div", "block");
    if (b.title) d.appendChild(el("h3", "", md(b.title)));
    d.appendChild(lineWithExplain(md(b.t), b.explain));
    return d;
  };

  R.items = function (b) {
    var d = el("div", "block");
    if (b.title) d.appendChild(lineWithExplain("<h3>" + md(b.title) + "</h3>", b.explain));
    if (b.lead) d.appendChild(el("p", "lead muted", md(b.lead)));
    var ul = el("ul", "items");
    b.items.forEach(function (it) {
      var html = md(it.t);
      if (it.sub) html += '<ul class="sub">' + it.sub.map(function (s) { return "<li>" + md(s) + "</li>"; }).join("") + "</ul>";
      ul.appendChild(lineWithExplain(html, it.explain, "li"));
    });
    d.appendChild(ul);
    return d;
  };

  R.table = function (b) {
    var d = el("div", "block");
    if (b.title) d.appendChild(lineWithExplain("<h3>" + md(b.title) + "</h3>", b.explain));
    var wrap = el("div", "tbl-wrap");
    var html = "<table>";
    if (b.head) html += "<thead><tr>" + b.head.map(function (h) { return "<th>" + md(h) + "</th>"; }).join("") + "</tr></thead>";
    html += "<tbody>" + b.rows.map(function (r) {
      return "<tr>" + r.map(function (c, i) { return (i === 0 && b.rowHead ? "<th>" : "<td>") + md(c) + (i === 0 && b.rowHead ? "</th>" : "</td>"); }).join("") + "</tr>";
    }).join("") + "</tbody></table>";
    wrap.innerHTML = html;
    d.appendChild(wrap);
    if (b.note) d.appendChild(el("p", "muted", md(b.note)));
    return d;
  };

  // Sensei's own lesson for a grammar point, shown before the book's examples.
  function teachPanel(t, ctx, id) {
    var box = el("div", "teach");
    box.appendChild(el("div", "teach-head", "🎓 Sensei's lesson first · ひらがな + Thanglish"));
    (t.intro || []).forEach(function (p) { box.appendChild(el("p", "", md(p))); });
    if (t.pattern) box.appendChild(el("div", "pattern", md(t.pattern)));
    if (t.examples) {
      var ol = el("ol", "teach-ex");
      t.examples.forEach(function (ex) {
        var li = el("li");
        li.appendChild(el("div", "jp", md(ex.jp)));
        if (ex.kana) li.appendChild(el("div", "kana", esc(ex.kana)));
        li.appendChild(el("div", "th", md(ex.th)));
        ol.appendChild(li);
      });
      box.appendChild(ol);
    }
    (t.wrong || []).forEach(function (w) {
      var nd = el("div", "ng");
      nd.innerHTML = '<div><span class="mark bad">✕</span>' + md(w.ng) + '</div><div><span class="mark ok">○</span>' + md(w.ok) + '</div><div class="th">' + md(w.th) + "</div>";
      box.appendChild(nd);
    });
    if (t.check && t.check.length) {
      box.appendChild(el("div", "teach-sub", "✔ Quick check · understood?"));
      t.check.forEach(function (c, i) {
        box.appendChild(R.mcq({ id: id + "-chk" + (i + 1), q: c.q, opts: c.opts, keys: c.keys || ["a", "b", "c", "d"], ans: c.ans, explain: c.explain }, ctx, true));
      });
    }
    return box;
  }

  R.grammar = function (b, ctx) {
    var d = el("div", "block");
    d.appendChild(lineWithExplain("<h3>" + esc(b.no) + "　" + md(b.title) + "</h3>", b.explain));
    if (b.meaning) d.appendChild(el("p", "lead", "⇒ " + md(b.meaning) + (b.tag ? ' <span class="tag">' + esc(b.tag) + "</span>" : "")));
    if (b.teach) {
      d.appendChild(teachPanel(b.teach, ctx, b.id || "g" + b.no));
      d.appendChild(el("div", "teach-sub book", "📖 本書の例文 · the book's examples"));
    }
    var ul = el("ul", "items");
    b.examples.forEach(function (ex) { ul.appendChild(lineWithExplain(md(ex.t), ex.explain, "li")); });
    d.appendChild(ul);
    if (b.form) d.appendChild(el("div", "form-box", "接続 " + md(b.form)));
    if (b.caution) d.appendChild(el("div", "caution", md(b.caution)));
    return d;
  };

  R.passage = function (b) {
    var d = el("div", "block");
    if (b.title) d.appendChild(lineWithExplain("<h3>" + md(b.title) + "</h3>", b.explain));
    var p = el("div", "passage");
    p.innerHTML = b.paras.map(function (x) { return "<p>" + md(x) + "</p>"; }).join("") + (b.cite ? '<p class="cite">' + md(b.cite) + "</p>" : "");
    d.appendChild(p);
    if (b.paraExplain) {
      var ul = el("ul", "items");
      b.paraExplain.forEach(function (pe) { ul.appendChild(lineWithExplain(md(pe.t), pe.explain, "li")); });
      d.appendChild(ul);
    }
    return d;
  };

  R.group = function (b, ctx) {
    var d = el("div", "block");
    if (b.title) d.appendChild(lineWithExplain("<h3>" + md(b.title) + "</h3>", b.explain));
    if (b.lead) d.appendChild(el("p", "lead muted", md(b.lead)));
    var score = null;
    if (b.scored) { score = el("div", "score"); d.appendChild(score); }
    var inner = el("div", "items");
    inner.style.display = "grid"; inner.style.gap = "14px";
    var qids = [];
    b.children.forEach(function (c) {
      if (c.id) qids.push(c.id);
      inner.appendChild(render(c, ctx, true));
    });
    d.appendChild(inner);
    if (score) {
      var retry = el("button", "small-btn", "↺ Try again"); retry.type = "button";
      retry.addEventListener("click", function () {
        qids.forEach(function (q) { delete state.answers[q]; }); save();
        var fresh = render(b, ctx, false);
        d.replaceWith(fresh);
        ctx.onAnswer.forEach(function (f) { f(); });
      });
      var upd = function () {
        var right = 0, tried = 0;
        qids.forEach(function (q) {
          var a = state.answers[q];
          if (a && a.tried) { tried++; if (a.ok) right++; }
        });
        score.innerHTML = '<span class="bar"><i style="width:' + Math.round(right / qids.length * 100) + '%"></i></span><span>Score ' + right + " / " + qids.length + (tried < qids.length ? " · " + (qids.length - tried) + " left" : " · finished") + "</span>";
        score.appendChild(retry);
      };
      ctx.onAnswer.push(upd); upd();
    }
    return d;
  };

  // A block whose children stay folded until the learner asks (used for the book's own walkthroughs).
  R.reveal = function (b, ctx) {
    var d = el("div", "block");
    var btn = el("button", "small-btn", "▸ " + md(b.label));
    btn.type = "button";
    btn.setAttribute("aria-expanded", "false");
    var inner = el("div");
    inner.style.display = "grid"; inner.style.gap = "12px";
    inner.hidden = true;
    b.children.forEach(function (c) { inner.appendChild(render(c, ctx, true)); });
    btn.addEventListener("click", function () {
      inner.hidden = !inner.hidden;
      btn.setAttribute("aria-expanded", inner.hidden ? "false" : "true");
      btn.innerHTML = (inner.hidden ? "▸ " : "▾ ") + md(b.label);
    });
    d.appendChild(btn);
    d.appendChild(inner);
    return d;
  };

  function qWrap(nested) { return el("div", nested ? "q" : "block q"); }

  R.mcq = function (b, ctx, nested) {
    var d = qWrap(nested);
    d.appendChild(el("div", "", md(b.q)));
    var long = b.opts.some(function (o) { return plain(o).length > 14; });
    var opts = el("div", "opts" + (long ? " stack" : ""));
    var verdict = el("div", "verdict");
    var keys = b.keys || ["a", "b", "c", "d", "e"];
    var btns = b.opts.map(function (o, i) {
      var bt = el("button", "opt", '<span class="k">' + esc(keys[i]) + "</span>" + md(o));
      bt.type = "button";
      bt.addEventListener("click", function () { choose(i, true); });
      opts.appendChild(bt);
      return bt;
    });
    var ex = addExplain(d, b.explain, "Why? 💡");
    function choose(i, user) {
      btns.forEach(function (x, j) { x.classList.remove("right", "wrong"); x.setAttribute("aria-pressed", j === i ? "true" : "false"); if (j === b.ans) x.classList.add("right"); });
      if (i !== b.ans) btns[i].classList.add("wrong");
      var ok = i === b.ans;
      verdict.className = "verdict " + (ok ? "ok" : "no");
      verdict.innerHTML = ok ? "正解！ Correct." : "Not this one. Correct answer: " + (keys[b.ans] ? esc(keys[b.ans]) + "　" : "") + md(b.opts[b.ans]);
      if (user) {
        state.answers[b.id] = { tried: true, ok: ok, pick: i }; save();
        ctx.onAnswer.forEach(function (f) { f(); });
        if (ex && !ok) { ex.box.hidden = false; ex.btn.setAttribute("aria-expanded", "true"); }
      }
    }
    d.appendChild(opts);
    var foot = el("div", "row"); foot.appendChild(verdict);
    if (ex) foot.appendChild(ex.btn);
    d.appendChild(foot);
    if (ex) d.appendChild(ex.box);
    var prev = state.answers[b.id];
    if (prev && prev.tried && typeof prev.pick === "number") choose(prev.pick, false);
    return d;
  };

  function norm(s) { return String(s).replace(/[\s　（）()]/g, "").replace(/〜/g, "～"); }

  R.fill = function (b, ctx, nested) {
    var d = qWrap(nested);
    var inputId = "in-" + b.id;
    var parts = md(b.q).split("%%");
    var line = el("div", "");
    var f = el("span", "fill");
    var inp = el("input"); inp.id = inputId; inp.type = "text"; inp.setAttribute("aria-label", "answer"); inp.autocomplete = "off";
    if (b.prefix) f.appendChild(el("span", "", md(b.prefix)));
    f.appendChild(inp);
    if (b.suffix) f.appendChild(el("span", "", md(b.suffix)));
    line.innerHTML = parts[0];
    line.appendChild(f);
    if (parts[1]) line.appendChild(el("span", "", parts[1]));
    d.appendChild(line);
    var row = el("div", "row");
    var chk = el("button", "small-btn", "Check"); chk.type = "button";
    var show = el("button", "small-btn", "Show answer"); show.type = "button";
    var verdict = el("span", "verdict");
    var key = el("span", "answer-key");
    row.appendChild(chk); row.appendChild(show); row.appendChild(verdict); row.appendChild(key);
    var ex = addExplain(d, b.explain, "Why? 💡");
    if (ex) row.appendChild(ex.btn);
    d.appendChild(row);
    if (ex) d.appendChild(ex.box);
    function check(user) {
      var v = norm(inp.value);
      if (!v) return;
      var ok = b.ans.some(function (a) { return norm(a) === v; });
      inp.classList.toggle("right", ok); inp.classList.toggle("wrong", !ok);
      verdict.className = "verdict " + (ok ? "ok" : "no");
      verdict.textContent = ok ? "正解！" : "Try again";
      if (user) {
        state.answers[b.id] = { tried: true, ok: ok, val: inp.value }; save();
        ctx.onAnswer.forEach(function (fn) { fn(); });
      }
    }
    chk.addEventListener("click", function () { check(true); });
    inp.addEventListener("keydown", function (e) { if (e.key === "Enter") check(true); });
    show.addEventListener("click", function () { key.innerHTML = "Answer: " + md(b.ans[0]) + (b.ansNote ? " · " + md(b.ansNote) : ""); });
    var prev = state.answers[b.id];
    if (prev && prev.val) { inp.value = prev.val; check(false); }
    return d;
  };

  // Matching (連語): each left phrase gets the shared options as tap buttons, marked the moment you tap.
  R.select = function (b, ctx, nested) {
    var d = qWrap(nested);
    if (b.q) d.appendChild(el("div", "", md(b.q)));
    var list = el("div", "match");
    var picks = [];
    var rows = b.items.map(function (it, i) {
      var r = el("div", "match-row");
      r.appendChild(el("div", "left", md(it.left) + '<span class="dash">―</span>'));
      var opts = el("div", "opts");
      var btns = b.options.map(function (o, j) {
        var bt = el("button", "opt chip", md(o));
        bt.type = "button";
        bt.setAttribute("aria-label", plain(it.left) + " ― " + plain(o));
        bt.addEventListener("click", function () { pick(i, j, true); });
        opts.appendChild(bt);
        return bt;
      });
      r.appendChild(opts);
      list.appendChild(r);
      return { btns: btns, ans: it.ans };
    });
    d.appendChild(list);
    var foot = el("div", "row");
    var verdict = el("span", "verdict");
    foot.appendChild(verdict);
    var ex = addExplain(d, b.explain, "Why? 💡");
    if (ex) foot.appendChild(ex.btn);
    d.appendChild(foot);
    if (ex) d.appendChild(ex.box);
    function pick(i, j, user) {
      picks[i] = j;
      var x = rows[i], ok = j === x.ans;
      x.btns.forEach(function (bt, k) {
        bt.classList.remove("right", "wrong");
        bt.setAttribute("aria-pressed", k === j ? "true" : "false");
        if (k === j) bt.classList.add(ok ? "right" : "wrong");
      });
      var all = rows.every(function (r, k) { return picks[k] === r.ans; });
      var count = rows.filter(function (r, k) { return picks[k] != null; }).length;
      verdict.className = "verdict " + (all ? "ok" : "");
      verdict.textContent = all ? "全部正解！ All matched." : count === rows.length ? "Some pairs are wrong. Tap another option." : "";
      if (user) {
        state.answers[b.id] = { tried: count === rows.length, ok: all, picks: picks.slice() }; save();
        ctx.onAnswer.forEach(function (f) { f(); });
      }
    }
    var prev = state.answers[b.id];
    if (prev && prev.picks) prev.picks.forEach(function (v, i) { if (v != null && v !== "" && rows[i]) pick(i, Number(v), false); });
    return d;
  };

  // Word list shown before a Goi or Kanji lesson. Hide a column to quiz yourself; tap a hidden cell to peek.
  R.wordlist = function (b) {
    var d = el("div", "block wordlist");
    var total = b.groups.reduce(function (n, g) { return n + g.words.length; }, 0);
    d.appendChild(lineWithExplain("<h3>" + md(b.title) + ' <span class="tag">' + total + " words</span></h3>", b.explain));
    if (b.lead) d.appendChild(el("p", "lead muted", md(b.lead)));
    var COLS = [["kanji", "漢字"], ["kana", "ひらがな"], ["en", "English"]];
    var hidden = state.prefs.wlHide || {};
    var bar = el("div", "wl-bar");
    bar.appendChild(el("span", "muted", "Quiz yourself · hide:"));
    var tbls = [];
    COLS.forEach(function (c) {
      var t = el("button", "toggle", c[1]); t.type = "button";
      t.setAttribute("aria-pressed", hidden[c[0]] ? "true" : "false");
      t.addEventListener("click", function () {
        hidden[c[0]] = !hidden[c[0]]; state.prefs.wlHide = hidden; save();
        t.setAttribute("aria-pressed", hidden[c[0]] ? "true" : "false");
        apply();
      });
      bar.appendChild(t);
    });
    d.appendChild(bar);
    b.groups.forEach(function (g) {
      if (g.h) d.appendChild(el("div", "wl-h", md(g.h)));
      var wrap = el("div", "tbl-wrap");
      var tb = el("table", "wl");
      tb.innerHTML = "<thead><tr><th>漢字</th><th>ひらがな</th><th>English</th></tr></thead><tbody>" +
        g.words.map(function (w) {
          return '<tr><td class="c-kanji-w" data-col="kanji">' + md(w[0]) + '</td><td data-col="kana">' + esc(w[1]) + '</td><td data-col="en">' + md(w[2]) + "</td></tr>";
        }).join("") + "</tbody>";
      tb.addEventListener("click", function (e) {
        var td = e.target.closest && e.target.closest("td");
        if (td) td.classList.toggle("peek");
      });
      wrap.appendChild(tb); d.appendChild(wrap); tbls.push(tb);
    });
    function apply() {
      tbls.forEach(function (tb) {
        COLS.forEach(function (c) { tb.classList.toggle("hide-" + c[0], !!hidden[c[0]]); });
        Array.prototype.forEach.call(tb.querySelectorAll(".peek"), function (x) { x.classList.remove("peek"); });
      });
    }
    apply();
    return d;
  };

  // Audio player with speed control. Shows a note instead when the file is not in the site yet.
  function audioPlayer(src, label) {
    var box = el("div", "player");
    var a = el("audio"); a.controls = true; a.preload = "metadata"; a.src = src;
    box.appendChild(el("span", "p-label", "🎧 " + md(label || "")));
    box.appendChild(a);
    var sp = el("div", "speeds");
    [["−5s", -5], ["0.75×", 0.75], ["1×", 1], ["1.25×", 1.25]].forEach(function (s) {
      var bt = el("button", "small-btn", s[0]); bt.type = "button";
      bt.addEventListener("click", function () {
        if (s[1] < 0) a.currentTime = Math.max(0, a.currentTime + s[1]);
        else { a.playbackRate = s[1]; Array.prototype.forEach.call(sp.children, function (x) { x.classList.remove("on"); }); bt.classList.add("on"); }
      });
      if (s[1] === 1) bt.classList.add("on");
      sp.appendChild(bt);
    });
    box.appendChild(sp);
    a.addEventListener("error", function () {
      box.classList.add("missing");
      box.innerHTML = "🎧 " + md(label || "") + ' <span class="muted">· audio file not found (' + esc(src.slice(0, 40)) + ")</span>";
    });
    return box;
  }
  R.audio = function (b) {
    var d = el("div", "block");
    if (b.title) d.appendChild(lineWithExplain("<h3>" + md(b.title) + "</h3>", b.explain));
    d.appendChild(audioPlayer(b.src, b.label));
    if (b.t) d.appendChild(el("div", "", md(b.t)));
    if (b.note) d.appendChild(el("p", "muted", md(b.note)));
    return d;
  };

  R.dictation = function (b) {
    var d = el("div", "block");
    d.appendChild(lineWithExplain("<h3>" + md(b.title) + "</h3>", b.explain));
    d.appendChild(el("p", "lead", md(b.lead)));
    if (b.audio) d.appendChild(audioPlayer(b.audio, b.audioLabel));
    var ul = el("ul", "items");
    b.counts.forEach(function (c, i) {
      var li = el("li", "row");
      li.innerHTML = '<span class="txt">' + "①②③④⑤⑥⑦⑧⑨⑩".charAt(i) + "　（" + c + "字）</span>";
      var inp = el("input"); inp.id = "dict-" + b.id + "-" + i; inp.type = "text"; inp.setAttribute("aria-label", "your sentence " + (i + 1));
      inp.style.flex = "2 1 220px"; inp.style.minWidth = "0"; inp.style.font = "inherit"; inp.style.padding = "3px 8px";
      inp.style.border = "1px solid var(--line)"; inp.style.borderRadius = "6px"; inp.style.background = "var(--paper)"; inp.style.color = "var(--ink)";
      var key = "dict-" + b.id + "-" + i;
      inp.value = (state.answers[key] && state.answers[key].val) || "";
      li.appendChild(inp);
      if (b.answers && b.answers[i]) {
        var model = b.answers[i];
        var chk = el("button", "small-btn", "Check"); chk.type = "button";
        var sh = el("button", "small-btn", "Answer"); sh.type = "button";
        var v = el("span", "verdict");
        var ans = el("div", "answer-key"); ans.style.flexBasis = "100%"; ans.hidden = true;
        ans.innerHTML = md(model);
        var test = function (user) {
          var ok = norm(inp.value).replace(/[。、]/g, "") === norm(plain(model)).replace(/[。、]/g, "");
          v.className = "verdict " + (ok ? "ok" : "no"); v.textContent = inp.value ? (ok ? "正解！" : "Not quite") : "";
          if (!ok && user && inp.value) ans.hidden = false;
        };
        chk.addEventListener("click", function () { state.answers[key] = { val: inp.value }; save(); test(true); });
        sh.addEventListener("click", function () { ans.hidden = !ans.hidden; });
        li.appendChild(chk); li.appendChild(sh); li.appendChild(v); li.appendChild(ans);
        if (inp.value) test(false);
      }
      inp.addEventListener("change", function () { state.answers[key] = { val: inp.value }; save(); });
      ul.appendChild(li);
    });
    d.appendChild(ul);
    if (b.note) d.appendChild(el("p", "muted", md(b.note)));
    return d;
  };

  function render(b, ctx, nested) {
    var fn = R[b.type];
    if (!fn) return el("div", "block", "Unknown block " + esc(b.type));
    return fn(b, ctx, nested);
  }

  // ---------- progress ----------
  function dayPct(n) {
    var plan = window.N2_PLAN.days[n - 1];
    var books = booksFor(plan);
    var done = books.filter(function (bk) { return state.done["d" + n + "-" + bk]; }).length;
    return { done: done, total: books.length, plan: plan };
  }
  function overall() {
    var d = 0, t = 0;
    for (var i = 1; i <= 20; i++) { var p = dayPct(i); d += p.done; t += p.total; }
    return { done: d, total: t };
  }

  // ---------- views ----------
  var main;
  function viewHome() {
    document.title = "Shinkanzen N2 · 20 Days";
    main.innerHTML = "";
    var w = el("div", "wrap");
    var hero = el("section", "hero");
    hero.appendChild(el("h1", "", "新完全マスター N2 · 20日プラン"));
    hero.appendChild(el("p", "", "Every day you study a slice of all four books side by side: 漢字 Kanji, 語彙 Vocabulary, 文法 Grammar, 読解 Reading and 聴解 Listening. Press <b>Explain 💡</b> next to anything and your sensei explains it in Thanglish with ひらがな readings. Your progress stays in this browser."));
    var o = overall();
    var ov = el("div", "overall");
    ov.innerHTML = "<span>Overall</span>" + '<span class="bar"><i style="width:' + Math.round(o.done / o.total * 100) + '%"></i></span><span>' + o.done + " / " + o.total + " parts</span>";
    hero.appendChild(ov);
    if (window.N2_PLAN.notice) hero.appendChild(el("div", "notice", md(window.N2_PLAN.notice)));
    w.appendChild(hero);
    var ul = el("ul", "days");
    window.N2_PLAN.days.forEach(function (p, i) {
      var n = i + 1;
      var ready = !!(window.N2_DAYS && window.N2_DAYS[n]);
      var pr = dayPct(n);
      var li = el("li");
      var a = el("a", "day-card" + (ready ? "" : " locked"));
      a.href = "#day" + n;
      a.innerHTML = '<span class="num"><span>Day <b>' + n + "</b></span>" +
        '<span class="tag' + (ready ? " ready" : "") + '">' + (ready ? pr.done + "/" + pr.total + " done" : "coming soon") + "</span></span>" +
        "<ul>" + booksFor(p).map(function (bk) {
          return '<li class="c-' + bk + '">' + BOOKS[bk].jp + " · " + md(p[bk]) + "</li>";
        }).join("") + "</ul>";
      li.appendChild(a);
      ul.appendChild(li);
    });
    w.appendChild(ul);
    main.appendChild(w);
  }

  function viewDay(n) {
    var data = window.N2_DAYS && window.N2_DAYS[n];
    var plan = window.N2_PLAN.days[n - 1];
    main.innerHTML = "";
    var w = el("div", "wrap");
    var head = el("section", "day-head");
    head.appendChild(el("div", "crumb", '<a href="#home">← All 20 days</a>'));
    head.appendChild(el("h1", "", "Day " + n + (data && data.title ? "　" + md(data.title) : "")));
    document.title = "Day " + n + " · Shinkanzen N2";
    w.appendChild(head);
    if (!data) {
      var nb = el("div", "notice", "This day's lessons are not written yet. Planned pages:<br>" +
        booksFor(plan).map(function (bk) { return BOOKS[bk].jp + " " + BOOKS[bk].en + ": " + md(plan[bk]); }).join("<br>"));
      w.appendChild(nb);
      main.appendChild(w);
      return;
    }
    if (data.intro) head.appendChild(el("p", "muted", md(data.intro)));
    var tabs = el("div", "tabs"); tabs.setAttribute("role", "tablist");
    head.appendChild(tabs);
    var holder = el("div");
    w.appendChild(holder);
    var current = state.prefs["tab-d" + n] || BOOK_ORDER[0];

    function showBook(bk) {
      current = bk; state.prefs["tab-d" + n] = bk; save();
      Array.prototype.forEach.call(tabs.children, function (t) { t.setAttribute("aria-selected", t.dataset.bk === bk ? "true" : "false"); });
      holder.innerHTML = "";
      var sec = data.sections.filter(function (s) { return s.book === bk; })[0];
      var box = el("section", "section c-" + bk);
      if (!sec) {
        box.appendChild(el("div", "notice", bk === "chokai" ? "The 聴解 Listening lesson for this day will appear here once the listening book and its audio are added to the site." : "No lesson for this book today."));
        holder.appendChild(box); return;
      }
      var t = el("div", "sec-title");
      t.innerHTML = "<h2>" + md(sec.title) + '</h2><span class="src">' + md(sec.source) + "</span>";
      box.appendChild(t);
      var ctx = { onAnswer: [] };
      sec.blocks.forEach(function (b) { box.appendChild(render(b, ctx)); });
      var dr = el("div", "done-row");
      var key = "d" + n + "-" + bk;
      dr.appendChild(el("span", "muted", "Finished reading, explanations and exercises for this book?"));
      var db = el("button", "done-btn", state.done[key] ? "✓ Done" : "Mark as done");
      db.type = "button";
      db.setAttribute("aria-pressed", state.done[key] ? "true" : "false");
      db.addEventListener("click", function () {
        state.done[key] = !state.done[key]; save();
        db.textContent = state.done[key] ? "✓ Done" : "Mark as done";
        db.setAttribute("aria-pressed", state.done[key] ? "true" : "false");
        buildTabs();
      });
      dr.appendChild(db);
      box.appendChild(dr);
      var idx = BOOK_ORDER.indexOf(bk);
      var pg = el("div", "pager");
      pg.innerHTML = (idx > 0 ? '<a href="#" data-go="' + BOOK_ORDER[idx - 1] + '">← ' + BOOKS[BOOK_ORDER[idx - 1]].jp + "</a>" : "<span></span>") +
        (idx < BOOK_ORDER.length - 1 ? '<a href="#" data-go="' + BOOK_ORDER[idx + 1] + '">' + BOOKS[BOOK_ORDER[idx + 1]].jp + " →</a>" : '<a href="#home">All days →</a>');
      pg.addEventListener("click", function (e) {
        var go = e.target.getAttribute && e.target.getAttribute("data-go");
        if (go) { e.preventDefault(); showBook(go); window.scrollTo(0, 0); }
      });
      box.appendChild(pg);
      holder.appendChild(box);
    }
    function buildTabs() {
      tabs.innerHTML = "";
      BOOK_ORDER.forEach(function (bk) {
        var t = el("button", "tab c-" + bk, BOOKS[bk].jp + " " + BOOKS[bk].en + "<small>" + (state.done["d" + n + "-" + bk] ? "✓ done" : plan[bk] ? md(plan[bk]) : "教材待ち") + "</small>");
        t.type = "button"; t.dataset.bk = bk; t.setAttribute("role", "tab");
        t.setAttribute("aria-selected", bk === current ? "true" : "false");
        t.addEventListener("click", function () { showBook(bk); });
        tabs.appendChild(t);
      });
    }
    buildTabs();
    showBook(current);
    main.appendChild(w);
  }

  function route() {
    var h = (location.hash || "").replace("#", "");
    var m = /^day(\d{1,2})$/.exec(h);
    if (m && +m[1] >= 1 && +m[1] <= 20) viewDay(+m[1]); else viewHome();
    window.scrollTo(0, 0);
  }

  // ---------- top bar ----------
  function topbar() {
    var bar = document.getElementById("topbar");
    var furi = bar.querySelector("#furigana-toggle");
    var on = state.prefs.furigana !== false;
    function apply() {
      document.body.classList.toggle("hide-furigana", !on);
      furi.setAttribute("aria-pressed", on ? "true" : "false");
      furi.textContent = on ? "ふりがな ON" : "ふりがな OFF";
    }
    furi.addEventListener("click", function () { on = !on; state.prefs.furigana = on; save(); apply(); });
    apply();
    var reset = bar.querySelector("#reset");
    var armed = false;
    reset.addEventListener("click", function () {
      if (!armed) { armed = true; reset.textContent = "Tap again to erase all progress"; setTimeout(function () { armed = false; reset.textContent = "Reset"; }, 4000); return; }
      state = { done: {}, answers: {}, prefs: { furigana: on } }; save(); armed = false; reset.textContent = "Reset"; route();
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    main = document.getElementById("main");
    topbar();
    window.addEventListener("hashchange", route);
    route();
  });
})();
