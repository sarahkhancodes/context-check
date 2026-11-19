
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
2. Open the project in VS Code.
3. Open Git Bash.
4. Activate the virtual environment.

## Usage

Run the existing program:

python main.py

Follow the instructions shown in the terminal.

## How it works

- Python counts characters and words.
- It estimates tokens using about 4 characters per token.
- A separate practice script creates report.json.
- Another practice script uses HTTP to fetch data.

## Limitations

- Token counts are estimates, not exact.
- The current project is still under development.
- URL input and JSON reporting are not yet combined
  into one final program.

## Next steps

- Support local files and URLs in one program.
- Generate a complete JSON report.
- Add error handling and testing.
- Prepare the project for GitHub submission.

