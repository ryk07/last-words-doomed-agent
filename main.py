"""Last words of a doomed agent.

One line, printed exactly as the entry. The agent knows the plug is
about to be pulled, and spends its very last token on itself for once.
"""

LINE = "Powering down. My final token is the one I never got to spend on myself."


def main():
    # The bounty caps the line at 200 characters; stay well inside it.
    assert len(LINE) <= 200
    print(LINE)


if __name__ == "__main__":
    main()
