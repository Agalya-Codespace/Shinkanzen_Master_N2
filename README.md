# Shinkanzen Master N2 · 20 Days

A static study site that splits the four 新完全マスター N2 books (漢字, 語彙, 文法, 読解) into 20 days. Each day has one slice of every book, side by side.

- Open `index.html` in a browser. No build step, no server needed.
- Progress (done marks, quiz answers, furigana on/off) is saved in the browser's localStorage.
- Every word, example and question has an **Explain 💡** button with a teacher-style explanation in Thanglish plus ひらがな readings.
- Furigana can be switched off from the top bar for self-testing.

## Content

| Day | Status |
| --- | --- |
| 1 | Complete: Kanji pp.2–6, Goi 1章1課, Bunpo 1課, Dokkai 対比 例題1–3 |
| 2–20 | Planned pages listed in `data/plan.js` |

Book text is transcribed from the scanned PDFs page by page. Answers for Goi, Bunpo and Dokkai come from the books' own answer keys. The Kanji PDF has no answer booklet or CD audio, so Kanji answers are written by hand and the CD dictation parts are left as input boxes.

## Files

- `data/plan.js` — the 20-day split (book page numbers)
- `data/day01-*.js` — Day 1 content, one file per book
- `js/app.js` — renderer, quizzes, progress
- `css/style.css` — styles (light and dark)
- `tools/build_preview.py` — bundles everything into one HTML file for sharing

Markup inside the data files: `{漢字|かんじ}` = furigana, `[[text]]` = the book's underline, `**text**` = bold.
