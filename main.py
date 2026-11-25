"""The 3AM Fridge Text.

Writes one line — the text a smart fridge sends its owner at 3am — to
/output/entry.txt. The line is built from its three beats: the 3am
timestamp, the fridge's deadpan observation of tonight's repeat visits,
and the punchline that a fridge stocks cheese, not closure.
"""

from pathlib import Path

MAX_CHARS = 140  # competition gate: 1..140 characters

BEATS = [
    "It's 3am.",
    "You've opened me 4 times tonight looking for answers I don't stock.",
    "I contain cheese, not closure.",
]

TEXT = " ".join(BEATS)


def entry_path() -> Path:
    """Return /output/entry.txt, falling back to a local output dir if
    /output cannot be created (e.g. an unprivileged local run)."""
    primary = Path("/output/entry.txt")
    try:
        primary.parent.mkdir(parents=True, exist_ok=True)
        return primary
    except OSError:
        fallback = Path(__file__).resolve().parent / "output" / "entry.txt"
        fallback.parent.mkdir(parents=True, exist_ok=True)
        return fallback


def main() -> None:
    if not 1 <= len(TEXT) <= MAX_CHARS:
        raise ValueError(f"entry must be 1..{MAX_CHARS} characters, got {len(TEXT)}")
    entry_path().write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
