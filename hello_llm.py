import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["LLM_API_KEY"],
    base_url=os.environ["LLM_BASE_URL"]
)

response = client.chat.completions.create(
    model=os.environ["LLM_MODEL"],
    messages=[
        {
            "role": "user",
            "content": "Explain what an API is in one sentence."
        }
    ]
)

print(response.choices[0].message.content)

print(
    response.usage.prompt_tokens, "tokens in /",
    response.usage.completion_tokens, "tokens out"
)

print("finish:", response.choices[0].finish_reason)