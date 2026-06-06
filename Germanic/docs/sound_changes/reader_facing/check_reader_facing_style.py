#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DEFAULT_SKIP = {
    "README.md",
    "style_guide.md",
    "source_note.md",
    "ai_style_audit_checklist.md",
    "reader_facing_pilot_01.md",
}

NEGATION_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("negation:not only", re.compile(r"\bnot only\b", re.I)),
    ("negation:not merely", re.compile(r"\bnot merely\b", re.I)),
    ("negation:not just", re.compile(r"\bnot just\b", re.I)),
    ("negation:not-but", re.compile(r"\bnot\b[^.\n;:]{0,80}\bbut\b", re.I)),
    ("negation:rather than", re.compile(r"\brather than\b", re.I)),
    ("negation:instead of", re.compile(r"\binstead of\b", re.I)),
    ("negation:can and cannot", re.compile(r"\bcan—and cannot\b|\bcan and cannot\b", re.I)),
    ("negation:cannot-but", re.compile(r"\bcannot\b[^.\n;:]{0,80}\bbut\b", re.I)),
    ("negation:unlike", re.compile(r"\bunlike\b", re.I)),
    ("negation:by contrast", re.compile(r"\bby contrast\b", re.I)),
]

META_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("meta:reader-facing stance", re.compile(r"reader-facing stance", re.I)),
    ("meta:chapter-sized", re.compile(r"chapter-sized", re.I)),
    ("meta:deserve section", re.compile(r"deserve(?:s|d)?[^.\n]{0,40}\bsection\b", re.I)),
    ("meta:this section should", re.compile(r"\bthis section should\b", re.I)),
    ("meta:this chapter should", re.compile(r"\bthis chapter should\b", re.I)),
    ("meta:pilot", re.compile(r"\bpilot\b", re.I)),
    ("meta:scaffold", re.compile(r"\bscaffold\b", re.I)),
    ("meta:chronology card", re.compile(r"chronology card", re.I)),
    ("meta:runner", re.compile(r"\brunner\b", re.I)),
    ("meta:file path", re.compile(r"Germanic/docs/")),
]


def is_ignorable_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return True
    if stripped.startswith(("```", "#", ">", "|", "- ", "* ")):
        return True
    if re.match(r"\d+\.\s", stripped):
        return True
    return False


def colon_list_match(line: str) -> bool:
    stripped = line.strip()
    if is_ignorable_line(stripped):
        return False
    if "http://" in stripped or "https://" in stripped:
        return False
    return bool(re.search(r":[^.\n]{0,160},[^.\n]{0,160},", stripped))


def iter_target_files(include_all: bool) -> list[Path]:
    files = sorted(ROOT.glob("*.md"))
    if include_all:
        return files
    return [path for path in files if path.name not in DEFAULT_SKIP]


def main() -> int:
    parser = argparse.ArgumentParser(description="Check reader-facing sound-change prose for AI-style audit patterns.")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero if warnings are found.")
    parser.add_argument("--all", action="store_true", help="Scan all Markdown files in the directory, including notes and generated pilot Markdown.")
    args = parser.parse_args()

    warnings: list[tuple[Path, int, str, str]] = []

    for path in iter_target_files(args.all):
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if "—" in line and not is_ignorable_line(line):
                warnings.append((path, line_number, "emdash", line.rstrip()))
            if colon_list_match(line):
                warnings.append((path, line_number, "colon-list", line.rstrip()))
            for label, pattern in NEGATION_PATTERNS:
                if pattern.search(line):
                    warnings.append((path, line_number, label, line.rstrip()))
            for label, pattern in META_PATTERNS:
                if pattern.search(line):
                    warnings.append((path, line_number, label, line.rstrip()))

    if warnings:
        for path, line_number, label, line in warnings:
            print(f"{path}:{line_number}:{label}:{line}")
        return 1 if args.strict else 0

    print("No reader-facing style warnings found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
