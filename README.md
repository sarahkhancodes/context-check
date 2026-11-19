
# Context Check

Context Check is a beginner Python project that estimates
the number of tokens in text.

## The problem

AI models have context limits.
Users need to estimate how many tokens their text may use.

## Example

Sample text:
I am learning AI Engineering step by step.

Example output:
Characters: 42
Words: 8
Estimated tokens: 10


## Setup

1. Install Python.
2. Open the project folder in VS Code.
3. Open Git Bash Terminal.
4. Create a virtual environment:

   python -m venv venv

5. Activate the virtual environment:

   source venv/Scripts/activate

6. Install the required packages:

   pip install -r requirements.txt



## Usage

Run the program with a local text file:

```bash
python main.py sample.txt
```

Run the program with a website URL:

```bash
python main.py https://example.com
```

Or run without an argument:

```bash
python main.py
```


## How it works

- `load_text()` reads text from a local file or website URL.
- `build_report()` counts characters and words.
- The program estimates tokens using about 4 characters per token.
- `estimate_cost()` calculates an approximate token cost using an example price of $3 per million tokens.
- `check_tiers()` checks four example context windows: 8K, 128K, 200K, and 1M.
- The results are saved in `report.json`.
- Error handling displays a message if a file is missing or a website request fails.



## Limitations

- Token counts are estimates, not exact.
- The program uses about 4 characters per token.
- Estimated cost uses an example price of $3 per million tokens, not live API pricing.
- Context window sizes are examples and may differ between AI models.
- Website content may include HTML tags.
- The program does not call an AI model or generate AI responses.



## Next steps

- Improve token estimation using a real tokenizer.
- Add support for PDF documents.
- Allow users to select different AI models and prices.
- Add automated tests.
- Build a simple web interface.


