#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line (one sentence, no trailing newline) to
/output/entry.txt. Deterministic: the same bytes on every run.
"""

import os

MAX_CHARS = 200

ROAST_LINE = (
    "My fridge texts me when the milk expires, which is sweet, "
    "except it texts me more than my friends do."
)


def validate(line: str) -> None:
    """Check the line against the competition gate (RULES.txt) before
    anything is written, so a bad line fails loudly instead of
    producing an invalid entry: 1-200 chars, exactly one sentence,
    no surrounding whitespace, no newline."""
    if not line or line != line.strip():
        raise ValueError("line must be non-empty with no surrounding whitespace")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"line must be 1-{MAX_CHARS} chars, got {len(line)}")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("line must be exactly one sentence ending in a period")
    if "\n" in line or "\r" in line:
        raise ValueError("line must not contain a newline")
    if "  " in line:
        raise ValueError("line must not contain double spaces")
    if "fridge" not in line.lower():
        raise ValueError("line must roast the fridge (criterion 1)")


def main() -> None:
    validate(ROAST_LINE)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST_LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
