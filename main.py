"""Entry program for the make.fun bounty "Have You Tried Turning It Off?".

The entry is one line from a hopeless support agent. This program
checks the line against the house gate and writes it, as plain UTF-8
with no trailing newline, to /output/entry.txt.
"""

from pathlib import Path

AGENT_LINE = (
    "Sir, I have escalated this to the highest level available: "
    "I am now also worried."
)

DESTINATION = Path("/output/entry.txt")
CHAR_LIMIT = 199


def gate(line: str) -> None:
    """Raise ValueError unless the line passes the entry gate."""
    if not line.strip():
        raise ValueError("entry line is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line spans more than one line")
    if len(line) > CHAR_LIMIT:
        raise ValueError("entry line is longer than 199 characters")
    line.encode("utf-8")


def emit(line: str, path: Path) -> int:
    """Write the line to path and return how many characters went out."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(line, encoding="utf-8", newline="")
    return len(line)


def main() -> None:
    gate(AGENT_LINE)
    written = emit(AGENT_LINE, DESTINATION)
    print("wrote %d characters to %s" % (written, DESTINATION))


if __name__ == "__main__":
    main()
