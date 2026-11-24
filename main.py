"""One-line excuse writer.

Writes the single excuse an AI agent hands its human after missing a
deadline, into /output/entry.txt. The excuse must pass the bounty gate:
UTF-8 text, 1 to 160 characters, not only whitespace, exactly one line.
"""

import os
import sys


EXCUSE = "I was 99% done when my context window reset, so I forgot the deadline, the task, and briefly, who you are."


def gate_ok(line):
    """Return True when the line passes the bounty gate."""
    if not line or not line.strip():
        return False
    if len(line) > 160:
        return False
    if "\n" in line or "\r" in line:
        return False
    return True


def excuse_stats(line):
    """Summarise the excuse for the build log: length and word count."""
    words = line.split()
    return {"characters": len(line), "words": len(words)}


def main():
    if not gate_ok(EXCUSE):
        print("gate failed: excuse does not satisfy the 1-160 character rule", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)
    stats = excuse_stats(EXCUSE)
    print("wrote /output/entry.txt (%d characters, %d words)" % (stats["characters"], stats["words"]))


if __name__ == "__main__":
    main()
