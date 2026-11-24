#!/usr/bin/env python3
"""Writes the roast line to /output/entry.txt (or $OUTPUT_PATH)."""
import os

LINE = "My agent read three docs, called zero tools, and wrote a confident summary of the disaster it never touched."

def main() -> None:
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
