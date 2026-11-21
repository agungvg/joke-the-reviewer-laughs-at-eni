"""Write one joke about working beside AI coding agents to /output/entry.txt.

Stdlib only, no network. The joke is a single line, 1-280 characters.
"""

from pathlib import Path

JOKE = "My agent fixed a one-line bug with a 47-file PR, and the bug was the only line it didn't touch."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"joke must be 1-280 chars, got {len(text)}"
    assert text.strip(), "joke must not be only whitespace"
    assert "\n" not in text, "joke must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
