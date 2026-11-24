#!/usr/bin/env python3
"""AgentQuest Moment of the Day — writes one line to /output/entry.txt."""

import os

LINE = "Fixed the flaky test that had failed every morning for a week \u2014 one wrong timezone line \u2014 and watched the whole suite go green before breakfast."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
