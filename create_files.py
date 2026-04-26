import requests
import os
import shutil
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("WANIKANI_API_KEY")

OUTPUT_DIR = "wk_levels"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def fetch_all_kanji():
    # Missing API key
    if not API_KEY or API_KEY.strip() == "":
        messagebox.showerror("Error", "Missing or invalid API key (.env not configured).")
        return None

    url = "https://api.wanikani.com/v2/subjects?types=kanji"
    kanji_by_level = {}

    while url:
        r = requests.get(url, headers=headers)

        # Invalid API key
        if r.status_code == 401:
            messagebox.showerror("Error", "Invalid API key. Please check your .env file.")
            return None

        r = r.json()

        for item in r["data"]:
            level = item["data"]["level"]
            character = item["data"]["characters"]

            if level not in kanji_by_level:
                kanji_by_level[level] = []

            kanji_by_level[level].append(character)

        url = r["pages"]["next_url"]

    return kanji_by_level


def generate_files():
    kanji_by_level = fetch_all_kanji()

    if kanji_by_level is None:
        return  # Stop if API key invalid or missing

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for level in range(1, 61):
        kanjis = kanji_by_level.get(level, [])
        filename = f"Level {level} ({len(kanjis)} kanji).txt"
        path = os.path.join(OUTPUT_DIR, filename)

        with open(path, "w", encoding="utf-8") as f:
            for k in kanjis:
                f.write(k + "\n")

    messagebox.showinfo("Done", f"Files generated in: {OUTPUT_DIR}")


def delete_files():
    if os.path.exists(OUTPUT_DIR):
        try:
            shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
            messagebox.showinfo("Deleted", "The folder 'wk_levels' has been removed.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete folder:\n{e}")
    else:
        messagebox.showwarning("Error", "The folder 'wk_levels' does not exist.")



# --- GUI ---
root = tk.Tk()
root.title("WaniKani → KanjiStudy Generator")
root.geometry("300x150")

btn_generate = tk.Button(root, text="Generate Files", command=generate_files, width=25, height=2)
btn_generate.pack(pady=10)

btn_delete = tk.Button(root, text="Delete wk_levels", command=delete_files, width=25, height=2)
btn_delete.pack(pady=5)

root.mainloop()
