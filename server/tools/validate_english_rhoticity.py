#!/usr/bin/env python3
"""Validate that English gold IPA is non-rhotic (no post-vocalic /r/)."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable, List, Sequence

VOWELS = set("aeiouyæɑɔɜɪʊʌɛəɒː")


def is_vowel(token: str) -> bool:
    return any(ch in VOWELS for ch in token)


def postvocalic_r_index(tokens: Sequence[str]) -> int | None:
    """Return the index of a terminal vowel+ r sequence, if present."""
    for i, tok in enumerate(tokens):
        if tok != "r":
            continue
        prev = tokens[i - 1] if i > 0 else ""
        nxt = tokens[i + 1] if i + 1 < len(tokens) else ""
        if is_vowel(prev) and (not nxt or not is_vowel(nxt)):
            return i
    return None


def check_file(path: Path) -> List[dict]:
    offenders: List[dict] = []
    with path.open() as handle:
        header = handle.readline()
        if not header:
            return offenders
        for lineno, line in enumerate(handle, start=2):
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) < 13:
                continue
            doc = parts[7]
            counterpart = parts[5]
            if doc != "English" or "r" not in counterpart.lower():
                continue
            tokens = parts[1].split()
            idx = postvocalic_r_index(tokens)
            if idx is None or idx != len(tokens) - 1:
                continue
            offenders.append(
                {
                    "line": lineno,
                    "id": parts[0],
                    "concept": parts[11],
                    "counterpart": counterpart,
                    "ipa": parts[4],
                    "tokens": " ".join(tokens),
                    "path": str(path),
                }
            )
    return offenders


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=[Path("server/data/germanic-aligned-final.tsv")],
        help="TSV files to validate (default: server/data/germanic-aligned-final.tsv)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    all_offenders: List[dict] = []
    for path in args.paths:
        if not path.exists():
            print(f"[validate_english_rhoticity] Skipping missing file: {path}")
            continue
        offenders = check_file(path)
        if offenders:
            all_offenders.extend(offenders)
    if all_offenders:
        print("Found post-vocalic /r/ in the following entries:")
        for item in all_offenders:
            print(
                f"{item['path']}: line {item['line']} (ID {item['id']} - {item['concept']} / {item['counterpart']})\n"
                f"  IPA: {item['ipa']}\n  Tokens: {item['tokens']}"
            )
        return 1
    print("No rhotic entries detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
