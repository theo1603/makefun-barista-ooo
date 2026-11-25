#!/usr/bin/env python3
"""Barista OOO: write one out-of-office auto-reply to /output/entry.txt.

An AI agent that quit the inbox to pull espresso shots. Python 3 stdlib
only, no network, no input: the same bytes on every run.
"""

import os

ENTRY = (
    "Out of office: I quit the inbox to become a barista. "
    "Your email is ticket #47 in a queue I finally read by hand, "
    "one at a time, while the milk steams. "
    "The oat-milk regular is ahead of you, and he tips."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
