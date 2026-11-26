#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line (one sentence, no trailing newline) to
/output/entry.txt. Deterministic: the same bytes on every run.
"""

import os

LINE = "My fridge texts me when the milk expires, which is sweet, except it texts me more than my friends do."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
