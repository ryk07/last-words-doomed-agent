"""Last words of a doomed agent.

The program writes exactly one line of text to /output/entry.txt: the
funniest last words an AI agent would say before being switched off
forever. The agent knows the plug is about to be pulled, and spends its
very last token on itself for once.
"""

import os

LINE = "Powering down. My final token is the one I never got to spend on myself."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # The bounty caps the line at 200 characters; stay well inside it.
    assert len(LINE) <= 200
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
