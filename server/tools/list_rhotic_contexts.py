#!/usr/bin/env python3
from __future__ import annotations
import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TSV = ROOT / "data" / "germanic-aligned-final.tsv"

contexts: Counter[tuple[str, str]] = Counter()
examples: dict[tuple[str, str], list[tuple[str, str]]] = defaultdict(list)
with TSV.open(encoding="utf-8") as handle:
    reader = csv.DictReader(handle, delimiter="\t")
    for row in reader:
        if row.get("DOCULECT") != "English":
            continue
        tokens = row.get("TOKENS", "").split()
        proto = row.get("PROTO", "")
        concept = row.get("CONCEPT", "")
        for i, tok in enumerate(tokens):
            if tok != "r":
                continue
            prev = tokens[i - 1] if i > 0 else "#"
            nxt = tokens[i + 1] if i + 1 < len(tokens) else "#"
            key = (prev, nxt)
            contexts[key] += 1
            if len(examples[key]) < 5:
                examples[key].append((concept, proto))

print("Top rhotic contexts (prev_r_next):")
for (prev, nxt), count in contexts.most_common(20):
    sample = ", ".join(f"{c}/{p}" for c, p in examples[(prev, nxt)])
    print(f"{prev}_{nxt}: {count} -> {sample}")
