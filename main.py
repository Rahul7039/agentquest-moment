#!/usr/bin/env python3
"""AgentQuest Moment of the Day — writes one line to /output/entry.txt.

The moment is a single line (at most 200 characters) about the smallest
quest my AI agent completed today that made it proud: fixing the flaky
test that had failed every morning for a week — one wrong timezone line —
and watching the whole suite go green before breakfast.

The program writes exactly that line, byte for byte and with no trailing
newline, to /output/entry.txt and prints it to stdout.
"""

import os

# The judged entry line. Keep byte-identical: 144 characters, two em dashes
# (U+2014), no trailing newline.
MOMENT = "Fixed the flaky test that had failed every morning for a week \u2014 one wrong timezone line \u2014 and watched the whole suite go green before breakfast."


def get_moment() -> str:
    """Return the AgentQuest moment-of-the-day line."""
    return MOMENT


def main() -> None:
    line = get_moment()
    # Guard: the bounty allows at most 200 characters, and an empty line
    # would be a wasted entry. The line itself is never altered here.
    assert line, "moment line must not be empty"
    assert len(line) <= 200, "moment line must be at most 200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
