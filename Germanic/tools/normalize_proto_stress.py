#!/usr/bin/env python3
"""
Normalize the PROTO column across cogsets:

1. In every PROTO value, replace any vowel+diaeresis (used as a length-
   marker proxy in some OE rows) with vowel+macron. The PROTOFORM
   column is left untouched (it keeps the diaeresis encoding for FST
   technical reasons).
2. For each cogset (COGIDS), take the OE row's normalized PROTO as the
   stress-canonical form. For each non-OE row in the same cogset whose
   PROTO matches the OE PROTO modulo combining marks (acute, grave,
   macron, diaeresis, breve, ogonek), replace its PROTO with the OE
   row's normalized PROTO, propagating stress accents.
3. Substantive disagreements (where base letters differ) are left alone
   and reported.

Idempotent. Run once.
"""

from __future__ import annotations

import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

TSV = Path(__file__).resolve().parent.parent / "data" / "germanic-aligned-final.tsv"

COMBINING_MARKS = {0x0301, 0x0300, 0x0304, 0x0308, 0x0306, 0x0328}

def replace_diaeresis_with_macron(s: str) -> str:
    """In NFD form, replace U+0308 (diaeresis) with U+0304 (macron)."""
    nfd = unicodedata.normalize("NFD", s)
    nfd2 = nfd.replace("\u0308", "\u0304")
    return unicodedata.normalize("NFC", nfd2)

def base_only(s: str) -> str:
    """Strip leading * and all combining marks."""
    s = s.lstrip("*").strip()
    return "".join(
        c for c in unicodedata.normalize("NFD", s)
        if ord(c) not in COMBINING_MARKS
    )

def main() -> int:
    raw = TSV.read_text(encoding="utf-8")
    lines = raw.split("\n")
    if lines and lines[-1] == "":
        trailing_nl = True
        lines = lines[:-1]
    else:
        trailing_nl = False

    header = lines[0].split("\t")
    idx = {col: i for i, col in enumerate(header)}
    p_i = idx["PROTO"]
    cog_i = idx["COGIDS"]
    doc_i = idx["DOCULECT"]
    id_i = idx["ID"]

    body = [ln.split("\t") for ln in lines[1:]]

    # Pass 1: in OE rows, replace diaeresis with macron in PROTO.
    diaeresis_fixes = []
    for row in body:
        if row[doc_i] == "Old_English":
            old = row[p_i]
            new = replace_diaeresis_with_macron(old)
            if new != old:
                diaeresis_fixes.append((row[id_i], old, new))
                row[p_i] = new

    # Pass 2: build cogset index.
    by_cog: dict[str, list[list[str]]] = defaultdict(list)
    for row in body:
        cog = row[cog_i].strip()
        if cog:
            by_cog[cog].append(row)

    # Pass 3: propagate OE PROTO stress marks to other doculects.
    propagations = []
    substantive: list[tuple[str, str, str, str, str]] = []
    for cog, members in by_cog.items():
        oes = [r for r in members if r[doc_i] == "Old_English"]
        if not oes:
            continue
        # Use the first OE row's PROTO as the canonical (typically only one).
        oe_proto = oes[0][p_i].strip()
        if not oe_proto:
            continue
        oe_base = base_only(oe_proto)
        for r in members:
            if r[doc_i] == "Old_English":
                continue
            other = r[p_i].strip()
            if not other:
                continue
            if other == oe_proto:
                continue
            if base_only(other) == oe_base:
                propagations.append((r[id_i], r[doc_i], other, oe_proto))
                r[p_i] = oe_proto
            else:
                substantive.append((cog, r[id_i], r[doc_i], other, oe_proto))

    # Write back.
    out_lines = ["\t".join(header)] + ["\t".join(r) for r in body]
    out = "\n".join(out_lines)
    if trailing_nl:
        out += "\n"
    TSV.write_text(out, encoding="utf-8")

    print(f"Diaeresis→macron fixes in OE-row PROTO: {len(diaeresis_fixes)}")
    for rid, old, new in diaeresis_fixes[:10]:
        print(f"  ID={rid:>5}  {old!r}  →  {new!r}")
    if len(diaeresis_fixes) > 10:
        print(f"  ... and {len(diaeresis_fixes)-10} more")

    print(f"\nStress propagations to non-OE PROTO: {len(propagations)}")
    by_doc = defaultdict(int)
    for _, doc, _, _ in propagations:
        by_doc[doc] += 1
    for doc, n in sorted(by_doc.items()):
        print(f"  {doc}: {n}")

    print(f"\nSubstantive cogset-PROTO disagreements (base letters differ): {len(substantive)}")
    for cog, rid, doc, other, oe in substantive:
        print(f"  COG={cog:<6} ID={rid:>5} {doc:<14} other={other:<22} OE={oe}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
