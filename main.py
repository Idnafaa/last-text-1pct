#!/usr/bin/env python3
"""Last Text at One Percent -- make.fun bounty entry.

A small program that writes the last text message a phone sends at
one percent battery to /output/entry.txt. The message is a single
line in the dying phone's own voice, under 200 characters.
"""

import os

TEXT = (
    "four years i kept your secrets and you repay me by watching "
    "tiktok at 1%. the charger was in your pocket the whole time. goodb\u2014"
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    message = TEXT.strip()
    if not 1 <= len(message) <= MAX_CHARS:
        raise SystemExit(
            f"entry must be 1-{MAX_CHARS} characters, got {len(message)}"
        )
    if "\n" in message:
        raise SystemExit("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(message)


if __name__ == "__main__":
    main()
