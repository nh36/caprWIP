#!/usr/bin/env python3
"""Audit DERIVATION_CLASS in germanic-aligned-final.tsv.

Reports:
  * counts per class
  * suspicious rows in four categories:
      1. Old_English with real COUNTERPART but blank DERIVATION_CLASS
      2. PROTOFORM != PROTO (modulo stress) but DERIVATION_CLASS == regular
      3. NOTE mentions paradigm-cell markers but DERIVATION_CLASS != late_analogy
      4. rows in oe_known_problems.tsv whose DERIVATION_CLASS is neither
         known_unmodelled nor unexplained_unmodelled
"""
from __future__ import annotations

import csv
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TSV = REPO / "Germanic/data/germanic-aligned-final.tsv"
KNOWN = REPO / "Germanic/data/oe_known_problems.tsv"

PARADIGM_MARKERS = (
    "gen.sg.", "gen sg", "genitive sg",
    "dat.sg.", "dat sg", "dative sg",
    "acc.sg.", "acc sg",
    "1sg", "2sg", "3sg",
    "1/3 sg", "1/3sg",
    "sg pret", "sg. pret.", "sg. pres.", "sg pres",
    "sg imperative", "imperative sg",
    "oblique", "paradigm cell",
    "gen.pl.", "gen pl", "dat.pl.", "dat pl",
)


def strip_acute(s: str) -> str:
    """Drop combining acute (stress); treat diaeresis as equivalent to macron
    (PROTOFORM uses i+diaeresis for technical FST reasons, PROTO uses i+macron;
    they encode the same long-vowel-with-stress in this project's convention)."""
    s = s.lstrip("*").strip()
    nfd = unicodedata.normalize("NFD", s)
    nfd = nfd.replace("\u0308", "\u0304")
    return unicodedata.normalize(
        "NFC", "".join(c for c in nfd if c != "\u0301")
    )


def main() -> int:
    with KNOWN.open(encoding="utf-8") as fh:
        known = {r["proto"].strip(): r for r in csv.DictReader(fh, delimiter="\t")}

    with TSV.open(encoding="utf-8") as fh:
        rdr = csv.DictReader(fh, delimiter="\t")
        rows = list(rdr)

    counts: dict[str, int] = {}
    blank_cp = 0
    non_oe_blank = 0
    susp1, susp2, susp3, susp4 = [], [], [], []

    seen_known: set[str] = set()

    for r in rows:
        cls = r.get("DERIVATION_CLASS", "")
        cp = r.get("COUNTERPART", "").strip()
        is_oe = r.get("DOCULECT") == "Old_English"
        real_cp = cp not in ("", "-", "?", "∅")

        if is_oe and real_cp:
            counts[cls or "(blank)"] = counts.get(cls or "(blank)", 0) + 1
            if not cls:
                susp1.append(r)
            pf, p = r.get("PROTOFORM", ""), r.get("PROTO", "")
            if cls == "regular" and strip_acute(pf) != strip_acute(p):
                susp2.append(r)
            note_l = r.get("NOTE", "").lower()
            if any(m in note_l for m in PARADIGM_MARKERS) and cls != "late_analogy":
                susp3.append(r)
            if pf in known:
                seen_known.add(pf)
                if cls not in ("known_unmodelled", "unexplained_unmodelled"):
                    susp4.append(r)
        else:
            if is_oe and not real_cp:
                blank_cp += 1
            else:
                non_oe_blank += 1

    # --- Output ---
    print("=" * 72)
    print("DERIVATION_CLASS audit")
    print("=" * 72)
    print()
    print("Counts (Old_English rows with real COUNTERPART):")
    total = sum(counts.values())
    for k in sorted(counts, key=lambda x: (-counts[x], x)):
        print(f"  {counts[k]:>4}  {k}")
    print(f"  {total:>4}  total")
    print()
    print(f"Old_English rows skipped (blank/`-` COUNTERPART): {blank_cp}")
    print(f"Non-OE rows (column intentionally blank):         {non_oe_blank}")
    print()

    def _show(label: str, items: list[dict[str, str]]) -> None:
        print(f"--- {label} ({len(items)}) ---")
        if not items:
            print("  none")
        for r in items:
            note = r.get("NOTE", "").replace("\t", " ")
            if len(note) > 70:
                note = note[:67] + "..."
            print(f"  ID={r.get('ID',''):>5}  "
                  f"PF={r.get('PROTOFORM',''):<18}  "
                  f"P={r.get('PROTO',''):<18}  "
                  f"CP={r.get('COUNTERPART',''):<14}  "
                  f"cls={r.get('DERIVATION_CLASS','') or '(blank)':<22}  "
                  f"NOTE={note}")
        print()

    _show("1. Old_English w/ real COUNTERPART but blank DERIVATION_CLASS", susp1)
    _show("2. PROTOFORM != PROTO (mod stress) but cls=regular", susp2)
    _show("3. NOTE mentions paradigm cell but cls != late_analogy", susp3)
    _show("4. row in oe_known_problems.tsv but cls not in {known,unexplained}_unmodelled", susp4)

    # Cross-check coverage of known-problems file
    missing = sorted(set(known) - seen_known)
    if missing:
        print(f"!! known-problems entries NOT seen in TSV: {missing}")
    else:
        print(f"All {len(known)} oe_known_problems.tsv entries matched a TSV row.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
