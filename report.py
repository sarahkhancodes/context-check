
import json

with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

tokens = round(len(text) / 4)

report = {
    "source": "sample.txt",
    "characters": len(text),
    "words": len(text.split()),
    "estimated_tokens": tokens,
    "fits_small_8k": tokens <= 8_000,
}

with open("report.json", "w", encoding="utf-8") as file:
    json.dump(report, file, indent=2)

print("Saved report.json")
