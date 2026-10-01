#!/usr/bin/env python3
"""Check fenced text diagrams, using only the Python standard library."""

import argparse
from pathlib import Path
import re
import sys
import unicodedata


# Ports are up, right, down, left. Arrows accept a line at their tail.
PORTS = {
    "─": "RL", "│": "UD", "┌": "RD", "┐": "DL", "└": "UR", "┘": "UL",
    "├": "URD", "┤": "UDL", "┬": "RDL", "┴": "URL", "┼": "URDL",
    "╭": "RD", "╮": "DL", "╰": "UR", "╯": "UL",
    "▼": "U", "▲": "D", "▶": "L", "◀": "R",
}
STEPS = {"U": (-1, 0, "D"), "R": (0, 1, "L"),
         "D": (1, 0, "U"), "L": (0, -1, "R")}


def cells(line):
    """Treat box glyphs as one terminal cell, wide text as two, marks as zero."""
    result = []
    for char in line:
        if unicodedata.combining(char):
            continue
        result.append(char)
        if unicodedata.east_asian_width(char) in {"W", "F"}:
            result.append(" ")
    return result


def check_diagram(text, max_width=88):
    rows = [cells(line) for line in text.splitlines()]
    errors = []
    titles = set()
    bottoms = set()
    edges = set()
    boxes = 0

    def error(y, x, message):
        errors.append(f"line {y + 1}, column {x + 1}: {message}")

    def at(y, x):
        if 0 <= y < len(rows) and 0 <= x < len(rows[y]):
            return rows[y][x]
        return " "

    for y, row in enumerate(rows):
        if "\t" in row:
            error(y, row.index("\t"), "use spaces, not tabs")
        if len(row) > max_width:
            error(y, max_width, f"width {len(row)} exceeds {max_width} columns")
        stack = []
        for x, char in enumerate(row):
            if char in "┌╭":
                stack.append(x)
            elif char in "┐╮":
                if not stack:
                    error(y, x, "top-right corner has no top-left corner")
                    continue
                left = stack.pop()
                # Inline titles are allowed on top borders only.
                for column in range(left + 1, x):
                    if at(y, column) not in PORTS:
                        titles.add((y, column))
                bottom = next((n for n in range(y + 1, len(rows))
                               if at(n, left) in "└╰"), None)
                if bottom is None and "┴" in row[left + 1:x]:
                    # A branch bus has corners, but is not a closed frame.
                    continue
                if bottom is None:
                    error(y, left, "box has no bottom-left corner in this column")
                    continue
                boxes += 1
                edges.update((n, edge) for n in range(y, bottom + 1) for edge in (left, x))
                edges.update((n, column) for n in (y, bottom) for column in range(left, x + 1))
                bottoms.add((bottom, left))
                if at(bottom, x) not in "┘╯":
                    error(bottom, x, "bottom-right corner is not aligned")
                else:
                    bottoms.add((bottom, x))
                for n in range(y + 1, bottom):
                    for edge in (left, x):
                        if not {"U", "D"}.issubset(PORTS.get(at(n, edge), "")):
                            error(n, edge, "box side is not aligned or is missing")
                for column in range(left + 1, x):
                    if not {"L", "R"}.issubset(PORTS.get(at(bottom, column), "")):
                        error(bottom, column, "bottom border is broken")
        for x in stack:
            error(y, x, "top-left corner has no top-right corner")

    if not boxes:
        errors.append("no closed box frames found")
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char in "▼▲▶◀":
                direction = {"▼": "D", "▲": "U", "▶": "R", "◀": "L"}[char]
                dy, dx, _ = STEPS[direction]
                if (y + dy, x + dx) not in edges:
                    error(y, x, "arrow does not point directly at a box border")
            if char in "└┘╰╯" and (y, x) not in bottoms:
                error(y, x, "bottom corner has no matching box")
            for port in PORTS.get(char, ""):
                dy, dx, opposite = STEPS[port]
                neighbor = at(y + dy, x + dx)
                if opposite in PORTS.get(neighbor, ""):
                    continue
                if neighbor == {"U": "▼", "R": "◀", "D": "▲", "L": "▶"}[port]:
                    continue
                if port in "LR" and (y, x + dx) in titles:
                    continue
                error(y, x, f"disconnected {port} port on {char}")
    return errors


def check_markdown(text, max_width=88):
    blocks = list(re.finditer(r"^```text[^\S\n]*\n(.*?)^```[^\S\n]*$", text,
                              re.MULTILINE | re.DOTALL))
    if not blocks:
        return ["no fenced text diagrams found"]
    errors = []
    for index, block in enumerate(blocks, 1):
        errors.extend(f"diagram {index}: {error}"
                      for error in check_diagram(block.group(1), max_width))
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="Markdown files, or - for stdin")
    parser.add_argument("--max-width", type=int, default=88)
    args = parser.parse_args()
    if args.max_width < 1:
        parser.error("--max-width must be positive")
    failed = False
    for name in args.paths or ["-"]:
        try:
            text = sys.stdin.read() if name == "-" else Path(name).read_text()
            errors = check_markdown(text, args.max_width)
        except (OSError, UnicodeError) as exc:
            errors = [str(exc)]
        for error in errors:
            print(f"{name}: {error}", file=sys.stderr)
        failed |= bool(errors)
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
