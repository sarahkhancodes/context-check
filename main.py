
import requests
import json
def load_text(source):
    if source.startswith(("http://", "https://")):
        response = requests.get(source, timeout=10)
        response.raise_for_status()
        return response.text
    else:
        with open(source, "r", encoding="utf-8") as file:
            return file.read()



try:
    text = load_text("sample.txt")

    chars = len(text)
    words = len(text.split())
    tokens = round(chars / 4)

    report = {
        "characters": chars,
        "words": words,
        "estimated_tokens": tokens,
        "fits_small_8k": tokens <= 8000
    }

    with open("report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)

    print("Report saved successfully!")

except FileNotFoundError:
    print("Error: File nahi mili. Please filename check karein.")


