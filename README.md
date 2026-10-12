# Shinkanzen Master N2 · 20 Days

A static study site that splits the four 新完全マスター N2 books (漢字, 語彙, 文法, 読解) into 20 days. Each day has one slice of every book, side by side.

- Open `index.html` in a browser. No build step, no server needed.
- Progress (done marks, quiz answers, furigana on/off) is saved in the browser's localStorage.
- Every word, example and question has an **Explain 💡** button with a teacher-style explanation in Thanglish plus ひらがな readings.
- Furigana can be switched off from the top bar for self-testing.
- Goi and Kanji lessons open with a word list (漢字 · ひらがな · English) you can hide column by column to quiz yourself.
- Each grammar point starts with a sensei lesson: pattern, several ひらがな + Thanglish examples, a ✕/○ pair and a quick check.
- Answer choices and 連語 matching are tap buttons with instant ○/× feedback.

## Audio

The CD audio is not in the repository. Copy the tracks in locally:

- `audio/kanji/cd01.mp3` … `cd54.mp3` (Kanji book CD, lower-case file names)
- `audio/chokai/` for the 聴解 Listening book (the Listening tab fills in once its book is transcribed)

Browsers block audio on `file://` pages in some setups; if a player stays silent, run `python3 -m http.server` in this folder and open `http://localhost:8000`.

## Content

| Day | Status |
| --- | --- |
| 1 | Complete: Kanji pp.2–6, Goi 1章1課, Bunpo 1課, Dokkai 対比 例題1–3 |
| 2–20 | Planned pages listed in `data/plan.js` |

Book text is transcribed from the scanned PDFs page by page. Answers for Goi, Bunpo and Dokkai come from the books' own answer keys. The Kanji PDF has no answer booklet, so Kanji answers are written by hand and the CD dictation parts are input boxes with the CD player above them.

## Files

- `data/plan.js` — the 20-day split (book page numbers)
- `data/day01-*.js` — Day 1 content, one file per book
- `js/app.js` — renderer, quizzes, progress
- `css/style.css` — styles (light and dark)
- `tools/build_preview.py` — bundles everything into one HTML file for sharing

Markup inside the data files: `{漢字|かんじ}` = furigana, `[[text]]` = the book's underline, `**text**` = bold.
