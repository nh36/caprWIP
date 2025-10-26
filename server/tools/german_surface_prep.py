#!/usr/bin/env python3
"""Split German IPA clusters and wrap segments for the existing surface filter.

Usage:
    printf "kniː\nbroːt\n" | python server/tools/german_surface_prep.py

Each input line is split into recognised clusters/vowels, then each segment is
emitted inside the curly-braced alphabet used by `GermanSurface`. This mirrors
what we eventually want to bake into the FST, but running it as a stand-alone
script keeps Foma from blowing its stack while we iterate.
"""

from __future__ import annotations

import sys

# Longest-first order so greedy matching works.
CLUSTERS = [
    "ts",
    "pf",
    "kn",
    "gn",
    "gr",
    "gl",
    "kr",
    "kl",
    "br",
    "bl",
    "pr",
    "pl",
    "fr",
    "fl",
    "dr",
    "tr",
    "sp",
    "st",
    "sk",
    "sl",
    "sm",
    "sn",
]

MULTI_VOWELS = ["aː", "eː", "iː", "oː", "uː", "ai", "au", "ɔy"]

SEGMENT_MAP = {**{c: f"{{{c}}}" for c in [
    "k","n","g","ŋ","b","d","t","p","f","v","s","z","ʃ",
    "h","j","l","m","r","w","x","a","ɔ","ə","ɛ","ɪ","ʊ"
]},
    "pf": "{pf}", "ts": "{ts}",
    "aː": "{aː}", "eː": "{eː}", "iː": "{iː}", "oː": "{oː}", "uː": "{uː}",
    "ai": "{ai}", "au": "{au}", "ɔy": "{ɔy}",
}

def tokenize(word: str) -> list[str]:
    segs: list[str] = []
    i = 0
    while i < len(word):
        match = next((c for c in CLUSTERS if word.startswith(c, i)), None)
        if match:
            segs.extend(list(match))
            i += len(match)
            continue
        vowel = next((v for v in MULTI_VOWELS if word.startswith(v, i)), None)
        if vowel:
            segs.append(vowel)
            i += len(vowel)
            continue
        segs.append(word[i])
        i += 1
    return segs

def wrap(word: str) -> str:
    segs = tokenize(word)
    return ''.join(SEGMENT_MAP.get(seg, seg) for seg in segs)

def main() -> None:
    for line in sys.stdin:
        token = line.rstrip('\n')
        if not token:
            print()
            continue
        print(wrap(token))

if __name__ == "__main__":
    main()
