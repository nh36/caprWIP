#!/usr/bin/env python3
"""Collect surface symbol inventory for the German filter.

Reads the Stage-3 TSV (default path) and tokenises the German surface column
using the logic from ``german_surface_prep.py``. Outputs the sorted token sets
so the brace-based `GermanSurface` definitions can be updated with real data.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable, Set


LONG_VOWEL_MAP = {
    "aː": "ā",
    "eː": "ē",
    "iː": "ī",
    "oː": "ō",
    "uː": "ū",
}

COMBINING_TIE = "\u0361"
AFFRICATES = ("pf", "ts")
VOWEL_DIGRAPHS = ("ai", "au", "ɔy")

VOWEL_TOKENS = {
    "a",
    "ā",
    "e",
    "ē",
    "i",
    "ī",
    "o",
    "ō",
    "u",
    "ū",
    "y",
    "ɔ",
    "ə",
    "ɛ",
    "ɪ",
    "ʊ",
    "ø",
    "œ",
    *VOWEL_DIGRAPHS,
}


def normalise(word: str) -> str:
    """Map colon-marked long vowels to macron vowels for tokenisation."""

    for seq, repl in LONG_VOWEL_MAP.items():
        word = word.replace(seq, repl)
    word = word.replace(COMBINING_TIE, "")
    return word


def iter_tokens(word: str) -> Iterable[str]:
    i = 0
    while i < len(word):
        digraph = next((v for v in VOWEL_DIGRAPHS if word.startswith(v, i)), None)
        if digraph:
            yield digraph
            i += len(digraph)
            continue

        affricate = next((a for a in AFFRICATES if word.startswith(a, i)), None)
        if affricate:
            yield affricate
            i += len(affricate)
            continue

        yield word[i]
        i += 1


def collect_tokens(lines: Iterable[str]) -> tuple[Set[str], Set[str]]:
    vowels: Set[str] = set()
    consonants: Set[str] = set()

    for raw in lines:
        word = raw.strip()
        if not word or word.startswith("#"):
            continue
        norm = normalise(word)
        for token in iter_tokens(norm):
            if token in VOWEL_TOKENS:
                vowels.add(token)
            else:
                consonants.add(token)

    return vowels, consonants


def main() -> None:
    parser = argparse.ArgumentParser(description="Collect German surface inventory")
    parser.add_argument(
        "--tsv",
        default="server/pipeline/output/germanic/stage3/germanic-aligned-final.tsv",
        help="Stage 3 TSV file (default: %(default)s)",
    )
    args = parser.parse_args()

    tsv_path = Path(args.tsv)
    if not tsv_path.exists():
        raise SystemExit(f"Surface TSV not found: {tsv_path}")

    with tsv_path.open() as handle:
        german_lines = [
            line.split("\t")[4]
            for line in handle
            if line.strip() and "German" in line.split("\t")
        ]

    vowels, consonants = collect_tokens(german_lines)

    print("Vowels ({}):".format(len(vowels)))
    print(" ".join(sorted(vowels)))
    print()
    print("Consonants ({}):".format(len(consonants)))
    print(" ".join(sorted(consonants)))


if __name__ == "__main__":
    main()
