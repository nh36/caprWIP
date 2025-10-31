#!/usr/bin/env python3
"""Split German/English IPA clusters and wrap segments for brace-based filters.

Usage:
    printf "kniː\nbroːt\n" | python server/tools/german_surface_prep.py

German now handles braces internally; use this helper for diagnostics or while
porting English/Dutch to the brace alphabet. Each input line is tokenised and
segments are wrapped in `{…}`.
"""

from __future__ import annotations

import sys

# Longest-first order so greedy matching works.
CLUSTERS = [
    "ts", "pf", "kn", "gn", "gr", "gl", "kr", "kl", "br", "bl",
    "pr", "pl", "fr", "fl", "dr", "tr", "sp", "st", "sk", "sl",
    "sm", "sn", "th", "wh"
]

MULTI_VOWELS = ["ā", "ē", "ī", "ō", "ū", "ai", "au", "ɔy", "aɪ", "aʊ", "ɔɪ"]

SEGMENT_MAP = {**{c: f"{{{c}}}" for c in [
    "k","n","g","ŋ","b","d","t","p","f","v","s","z","ʃ","θ","ð",
    "h","j","l","m","r","w","x","a","ɔ","ə","ɛ","ɪ","ʊ","ʌ","ɑ","i","u","e","o",
    "ā","ē","ī","ō","ū"
]},
    "pf": "{pf}", "ts": "{ts}",
    "ai": "{ai}", "au": "{au}", "ɔy": "{ɔy}", "aɪ": "{aɪ}", "aʊ": "{aʊ}", "ɔɪ": "{ɔɪ}",
    "th": "{θ}", "wh": "{ʍ}",
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
