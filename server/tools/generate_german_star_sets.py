#!/usr/bin/env python3
"""Generate literal GermanStar* inventories from the proto mappings."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Set

TOKEN_PATTERN = re.compile(r"(?P<src>\{[^}]+\}|[^{}\s|]+):\{\*(?P<dst>[^}]+)\}")
BLOCK_PATTERN = re.compile(r"define\s+(?P<name>\w+)\s*\[(?P<body>.*?)\];", re.DOTALL)

VOWEL_MACROS = ("pgrmShortVowel", "pgrmLongVowel", "pgrmNasalVowel")
DIPHTHONG_MACROS = ("pgrmDiphthong",)
CONSONANT_MACROS = (
    "pgrmInitSimple",
    "pgrmMedial",
    "pgrmOnsetCore",
    "pgrmCodaSimple",
    "pgrmCodaComplex",
    "pgrmWeakOnset",
    "pgrmWeakCoda",
)

EXTRA_VOWEL_TOKENS = ["{*æ}", "{*ɑ}", "{*ɔ}", "{*ə}", "{*ɛ}", "{*ɜ}", "{*ʉ}", "{*ʊ}", "{*ø}", "{*œ}"]
EXTRA_DIPHTHONG_TOKENS = ["{*ei}"]

GERMAN_FRONT_VOWEL_SET = {"{*i}", "{*ī}", "{*e}", "{*ē}", "{*æ}", "{*ɛ}", "{*ø}", "{*œ}", "{*y}", "{*ʉ}"}
GERMAN_BACK_VOWEL_SET = {"{*a}", "{*ā}", "{*ɑ}", "{*o}", "{*ō}", "{*u}", "{*ū}", "{*ɔ}", "{*ʊ}"}
GERMAN_FRONT_TRIGGER_EXTRA = ["{*ai}", "{*ei}", "{*eu}", "{*iu}"]


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("server/fsts/germanic.txt"))
    parser.add_argument("--output", type=Path)
    return parser.parse_args(argv)


def extract_blocks(text: str) -> Dict[str, str]:
    blocks: Dict[str, str] = {}
    for match in BLOCK_PATTERN.finditer(text):
        blocks[match.group("name")] = match.group("body")
    return blocks


def collect_tokens(block: str) -> Set[str]:
    tokens: Set[str] = set()
    for match in TOKEN_PATTERN.finditer(block):
        dst = match.group("dst")
        tokens.add(f"{{*{dst}}}")
    return tokens


def gather(blocks: Dict[str, str], names: Iterable[str]) -> Set[str]:
    out: Set[str] = set()
    for name in names:
        body = blocks.get(name)
        if not body:
            raise KeyError(f"Missing definition for {name}")
        out.update(collect_tokens(body))
    return out


def render_union(name: str, tokens: Sequence[str]) -> str:
    body = " |\n    ".join(tokens)
    return f"define {name} [\n    {body}\n];"


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    text = args.source.read_text(encoding="utf-8")
    blocks = extract_blocks(text)

    vowels = sorted(gather(blocks, VOWEL_MACROS))
    full_vowels = sorted(set(vowels) | set(EXTRA_VOWEL_TOKENS))
    diphthongs = sorted(set(gather(blocks, DIPHTHONG_MACROS)) | set(EXTRA_DIPHTHONG_TOKENS))
    consonants = sorted(gather(blocks, CONSONANT_MACROS))

    parts: List[str] = []
    parts.append(render_union("GermanStarVowel", full_vowels))
    parts.append(render_union("GermanStarDiphthong", diphthongs))
    parts.append(render_union("GermanStarVocalic", ["GermanStarVowel", "GermanStarDiphthong"]))
    parts.append(render_union("GermanStarConsonant", consonants))

    front_vowels = [tok for tok in full_vowels if tok in GERMAN_FRONT_VOWEL_SET]
    back_vowels = [tok for tok in full_vowels if tok in GERMAN_BACK_VOWEL_SET]
    parts.append(render_union("GermanStarFrontVowel", front_vowels))
    parts.append(render_union("GermanStarBackVowel", back_vowels))
    parts.append(render_union("GermanStarFrontTrigger", ["GermanStarFrontVowel"] + GERMAN_FRONT_TRIGGER_EXTRA))

    output = "\n\n".join(parts) + "\n"
    if args.output:
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(__import__("sys").argv[1:]))
