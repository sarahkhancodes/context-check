import requests

url = "https://api.github.com/users/octocat"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

except requests.exceptions.RequestException as error:
    print(f"Could not download: {error}")

else:
    print(response.status_code)
    text = response.text
    print(f"{len(text):,} characters")