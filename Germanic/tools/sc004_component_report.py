#!/usr/bin/env python3
"""Deterministic SC004 component application report (research only).

Splits the production rule PWGmcAiMonophthongization into its three Foma rewrites
and reports, for every corpus lexeme whose derivation passes an *ai / *ái input,
which component applies, the form before/after that component, and whether the
component is necessary for the final Old English output.

Components (research names):
  A  SC004FinalAiToE      {*ai} -> {*ē} || _ .#.   (word-final unstressed *ai)
  B  SC004AiToA           {*ai} -> {*ā}            (remaining unstressed *ai)
  C  SC004AiStressedToA   {*ái} -> {*ā}            (stressed *ái)

Runs inside the backend container (needs foma/flookup); CWD = /usr/app.
Writes a TSV to --out.
"""
from __future__ import annotations

import argparse
import csv
import re
import subprocess
import tempfile
from pathlib import Path

FOMA_SCRIPT = r"""
source fsts/germanic.txt
define SC004FinalAiToE      [ {*ai} -> {*ē} || _ .#. ];
define SC004AiToA           [ {*ai} -> {*ā} ];
define SC004AiStressedToA   [ {*ái} -> {*ā} ];
define Sc4Before   [ EnglishProtoInput .o. EarlyGermanicConsonantPipeline ];
define Sc4AfterA   [ Sc4Before .o. SC004FinalAiToE ];
define Sc4AfterAB  [ Sc4AfterA .o. SC004AiToA ];
define Sc4Full     [ Sc4AfterAB .o. SC004AiStressedToA ];
clear stack
regex Sc4Before;
save stack {tmp}/sc4_before.bin
clear stack
regex Sc4AfterA;
save stack {tmp}/sc4_afterA.bin
clear stack
regex Sc4AfterAB;
save stack {tmp}/sc4_afterAB.bin
clear stack
regex Sc4Full;
save stack {tmp}/sc4_full.bin
quit
"""


def normalize_proto(proto: str) -> str:
    # Same normalization as the apply-down path: strip markup, th -> theta.
    s = re.sub(r"[{}\*\s/()]", "", proto)
    s = s.replace("þ", "θ")
    return s


def flookup(bin_path: str, forms: list[str]) -> dict[str, list[str]]:
    inp = "\n".join(forms) + "\n"
    proc = subprocess.run(["flookup", "-i", bin_path],
                          input=inp.encode("utf-8"),
                          stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    out: dict[str, list[str]] = {f: [] for f in forms}
    # flookup (without -x) prints "input\toutput" lines; blank line ends a word.
    for line in proc.stdout.decode("utf-8", "replace").splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) >= 2 and parts[1] not in ("+?", ""):
            out.setdefault(parts[0], []).append(parts[1])
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--tsv", default="data/germanic-aligned-final.tsv")
    ap.add_argument("--out", default="docs/sound_changes/order_tests/sc004_component_application_report.tsv")
    args = ap.parse_args()

    tmp = tempfile.mkdtemp()
    script = FOMA_SCRIPT.replace("{tmp}", tmp)
    sp = Path(tmp) / "build.foma"
    sp.write_text(script, encoding="utf-8")
    subprocess.run(["foma", "-q", "-f", str(sp)], stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, check=True)

    rows = list(csv.DictReader(open(args.tsv, encoding="utf-8"), delimiter="\t"))
    oe = [r for r in rows if r["DOCULECT"] == "Old_English"]
    # candidates: OE rows whose proto carries ai / ái
    cands = []
    for r in oe:
        proto = r.get("PROTO") or r.get("PROTOFORM") or ""
        if "ai" in proto or "ái" in proto:
            cands.append(r)

    forms = [normalize_proto(r.get("PROTO") or r.get("PROTOFORM") or "") for r in cands]
    before = flookup(f"{tmp}/sc4_before.bin", forms)
    afterA = flookup(f"{tmp}/sc4_afterA.bin", forms)
    afterAB = flookup(f"{tmp}/sc4_afterAB.bin", forms)
    full = flookup(f"{tmp}/sc4_full.bin", forms)

    def one(d: dict[str, list[str]], f: str) -> str:
        vs = d.get(f, [])
        return vs[0] if vs else "<none>"

    out_rows = []
    for r, f in zip(cands, forms):
        b, a, ab, fu = one(before, f), one(afterA, f), one(afterAB, f), one(full, f)
        comps = []
        if b != a:
            comps.append("A_final_ai_to_e")
        if a != ab:
            comps.append("B_nonfinal_ai_to_a")
        if ab != fu:
            comps.append("C_stressed_ai_to_a")
        out_rows.append({
            "concept": r["CONCEPT"],
            "proto_input": r.get("PROTO") or r.get("PROTOFORM") or "",
            "expected_oe": r.get("COUNTERPART", ""),
            "before_sc004": b,
            "after_A": a,
            "after_AB": ab,
            "after_full_sc004": fu,
            "components_applied": ";".join(comps) if comps else "NONE",
            "derivation_class": r.get("DERIVATION_CLASS", ""),
        })

    out_rows.sort(key=lambda x: (x["components_applied"], x["concept"]))
    with open(args.out, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out_rows[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(out_rows)

    # summary to stdout
    from collections import Counter
    c = Counter(x["components_applied"] for x in out_rows)
    print(f"candidates: {len(out_rows)}")
    for k, v in sorted(c.items()):
        print(f"  {k}: {v}")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
