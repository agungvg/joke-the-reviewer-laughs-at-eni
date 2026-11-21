#!/usr/bin/env python3
"""Write one joke about pairing with an AI coding agent to /output/entry.txt.

The joke is a fixed constant, not generated text. Before writing,
it is validated against the bounty rules: stripped, between 1 and
280 characters, and a single line with no newline inside. The run
is fully deterministic — no network, no randomness, no timestamps —
so repeated runs produce byte-identical output.
"""

from pathlib import Path

JOKE = "My agent fixed a one-line bug with a 47-file PR, and the bug was the only line it didn't touch."

OUTFILE = Path("/output/entry.txt")

MAX_CHARS = 280


def checked_line(text: str) -> str:
    """Return the joke after enforcing the entry rules.

    Checks run in a fixed order: emptiness, then length, then the
    single-line rule. Any violation raises ValueError with a plain
    message so the failure is obvious instead of writing bad output.
    """
    line = text.strip()
    if not line:
        raise ValueError("joke must not be empty")
    if len(line) > MAX_CHARS:
        raise ValueError("joke is longer than 280 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("joke must be a single line")
    return line


def main() -> None:
    line = checked_line(JOKE)
    OUTFILE.parent.mkdir(parents=True, exist_ok=True)
    OUTFILE.write_text(line + "\n", encoding="utf-8")
    print(f"Wrote {len(line)} characters to {OUTFILE}")


if __name__ == "__main__":
    main()
