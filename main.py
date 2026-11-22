import sys
import requests
import json
import os
from dotenv import load_dotenv
from openai import OpenAI

def load_text(source):
    if source.startswith(("http://", "https://")):
        response = requests.get(source, timeout=10)
        response.raise_for_status()
        return response.text
    else:
        with open(source, "r", encoding="utf-8") as file:
            return file.read()


# Example prices from Edversity course PDF
# USD per 1 million tokens: (input, output)

PRICES = {
    "gemini-4-hydrogen": (1.50, 7.50),
    "gemini-3.5-flash-lite": (0.30, 2.50),
    "gpt-5-nano": (0.05, 0.40),
    "claude-haiku-5-5": (0.10, 0.50),
}


        
def summarise(client, model, text):
    prompt = (
        "Summarise this document in 5 short bullet points.\n\n"
        f"<document>\n{text}\n</document>"
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content, response.usage


def cost_of(model, usage):
    price_in, price_out = PRICES.get(model, (0.0, 0.0))

    return (
        usage.prompt_tokens * price_in
        + usage.completion_tokens * price_out
    ) / 1_000_000


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


    # Step 4: AI Summary and Real Token Cost

    load_dotenv()

    client = OpenAI(
        api_key=os.environ["LLM_API_KEY"],
        base_url=os.environ["LLM_BASE_URL"]
    )

    model = os.environ["LLM_MODEL"]

    summary, usage = summarise(client, model, text)

    print(f"\nSummary from {model}:")
    print(summary)

    print(
        f"Real tokens: {usage.prompt_tokens:,} in · "
        f"{usage.completion_tokens:,} out"
    )

    print(f"Real cost: ${cost_of(model, usage):.4f}")


except FileNotFoundError:
    print("Error: File nahi mili. Please filename check karein.")

except requests.exceptions.RequestException:
    print("Error: Website se data nahi mil saka. URL check karein.")


