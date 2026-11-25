#!/usr/bin/env python3
"""Write the one-line dad joke to /output/entry.txt.

Competition: The One-Liner Groan-Off (u-alfasurya91-the-one-liner-groan-off-5a1febd5)
Task: one original one-line dad joke, at most 140 characters.
"""

import os

ENTRY = "My goldfish got a job at the bank — turns out he's great at saving, but his memory keeps losing the interest."
# The joke turns on two bank words at once: a goldfish "saving" (hoarding
# food/money) while "losing the interest" (forgetting, and earning none).


def main():
    # Enforce the competition's caps so a bad edit fails loudly instead of
    # submitting an entry the gate would refuse: 1-140 chars, one line.
    # The trailing newline in the file is the writer's, not part of the joke.
    body = ENTRY.strip()
    if not (1 <= len(body) <= 140):
        raise ValueError(f"entry is {len(body)} chars, must be 1-140")
    if "\n" in body:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(body + "\n")


if __name__ == "__main__":
    main()
