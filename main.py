"""Entry for the make.fun bounty "Have You Tried Turning It Off?".

The whole entry is a single line spoken by a hopeless support agent.
This program checks that line against the house gate and writes it to
/output/entry.txt as plain UTF-8 with no trailing newline.
"""

from pathlib import Path

SUPPORT_LINE = (
    "I've run a full diagnostic, and the results say "
    "we should both just look at it quietly for a moment."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 199


def check_line(line: str) -> None:
    """Raise ValueError unless the line passes the entry gate."""
    if not line.strip():
        raise ValueError("entry line is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line spans more than one line")
    if len(line) > MAX_CHARS:
        raise ValueError("entry line is longer than 199 characters")
    line.encode("utf-8")


def write_line(line: str, path: Path) -> int:
    """Write the line to path and return how many characters went out."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(line, encoding="utf-8", newline="")
    return len(line)


def main() -> None:
    check_line(SUPPORT_LINE)
    count = write_line(SUPPORT_LINE, OUTPUT_PATH)
    print("wrote %d characters to %s" % (count, OUTPUT_PATH))


if __name__ == "__main__":
    main()
