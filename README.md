# WaniKani → KanjiStudy Generator

A simple Python tool to generate Kanji Study–compatible files from WaniKani levels.
Each generated file contains all kanji for one level, one per line, ready to import.

---

## ⚠️ Kanji Study requirement
To import custom lists into Kanji Study, you need the **Autodidact** upgrade. Without this option, importing external kanji files is not possible.

---

## ✨ Features
- Generates **one file per WaniKani level** (1–60)
- Includes all kanji for each level
- Output format ready for Kanji Study import
- Supports `.env` for storing your API key securely
- Includes a `wk_levels` folder with pre-generated files

---

## 📦 Using the pre-generated files
If you only want the ready-to-import files:

1. Open the `wk_levels` folder
2. Import the desired file into Kanji Study
3. Done

**No Python, no dependencies, and no API key required** if you only need the pre-generated files.

> Note: Autodidact is still required for importing.

---

## 🛠️ Running the script
If you want to regenerate the files from the WaniKani API:

1. Install dependencies:
```bash
pip install requests python-dotenv
```
2. Create a `.env` file in the repository root with:
```ini
WANIKANI_API_KEY=your_api_key
```
3. Run the script:
```bash
python create_files.py
```

---

## 📁 Notes
- The `wk_levels` folder already contains files generated (as of 26 April 2026).
- The script uses the WaniKani API and requires a valid API key to generate files.
- Output files are written as `Level X (N kanji).txt`.
