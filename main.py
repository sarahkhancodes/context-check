import sys
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

def estimate_cost(tokens):
    price_per_million = 3
    cost = (tokens / 1000000) * price_per_million
    return cost


def check_tiers(tokens):
    return {
        "Small (8K)": tokens <= 8000,
        "Standard (128K)": tokens <= 128000,
        "Large (200K)": tokens <= 200000,
        "Extra-large (1M)": tokens <= 1000000
    }

def build_report(source, text):
    chars = len(text)
    words = len(text.split())
    tokens = round(chars / 4)

    return {
        "source": source,
        "characters": chars,
        "words": words,
        "estimated_tokens": tokens,
        "estimated_cost_usd": round(estimate_cost(tokens), 6),
        "fits": check_tiers(tokens)
    }

if len(sys.argv) > 1:
    source = sys.argv[1]
else:
    source = input("File or web address to check: ").strip()

try:
    text = load_text(source)



    report = build_report(source, text)


    with open("report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)

    print("Report saved successfully!")

except FileNotFoundError:
    print("Error: File nahi mili. Please filename check karein.")

except requests.exceptions.RequestException:
    print("Error: Website se data nahi mil saka. URL check karein.")


