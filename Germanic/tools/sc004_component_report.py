#!/usr/bin/env python3
"""Deterministic SC004/SC014 component application report (PROTOFORM-based).

CORRECTION: the production baseline and trace tools derive Old English from the
Old-English-row ``PROTOFORM`` field (see cascade_baseline.load_oe_rows,
oe_full_trace_report.load_rows). This report therefore uses ``PROTOFORM`` as the
production input for every application conclusion, and only falls back to the
cognate-set ``PROTO`` field when a row has no ``PROTOFORM`` (recorded explicitly
in the ``prod_field`` column so the fallback is testable). It audits every Old
English row whose ``PROTO`` OR ``PROTOFORM`` carries an *ai*-diphthong, so the
PROTO/PROTOFORM disagreements that misled the previous report are visible.

Component rules (as adopted in germanic.txt after the correction):
  SC014  PNWGmcUnstressedAiMonophthongization : {*ai} -> {*ē}   (unstressed *ai)
  SC004  EAFAiMonophthongization              : {*ái} -> {*ā}   (stressed *ái)

Runs inside the backend container (needs foma/flookup); CWD = /usr/app.
"""
from __future__ import annotations

import argparse
import csv
import re
import subprocess
import tempfile
from pathlib import Path

# Base = post-consonant, pre-EarlyEnglishLineChanges (SC014's production input).
# Then apply the two production component rules in cascade order.
FOMA_SCRIPT = r"""
source fsts/germanic.txt
define RepBase   [ EnglishProtoInput .o. EarlyGermanicConsonantPipeline ];
define RepSC014  [ RepBase .o. PNWGmcUnstressedAiMonophthongization ];
define RepSC004  [ RepSC014 .o. EAFAiMonophthongization ];
clear stack
regex RepBase;
save stack {tmp}/base.bin
clear stack
regex RepSC014;
save stack {tmp}/sc014.bin
clear stack
regex RepSC004;
save stack {tmp}/sc004.bin
quit
"""

AI_DIPHTHONG_RE = re.compile(r"[aáàāă][iíìī]")


def normalize_proto(proto: str) -> str:
    # Identical to cascade_baseline.normalize_proto / oe_full_trace normalize.
    s = re.sub(r"[{}*\s/()]", "", proto or "")
    return s.replace("þ", "θ")


def flookup(bin_path: str, forms: list[str]) -> dict[str, list[str]]:
    inp = "\n".join(forms) + "\n"
    proc = subprocess.run(["flookup", "-i", bin_path],
                          input=inp.encode("utf-8"),
                          stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    out: dict[str, list[str]] = {f: [] for f in forms}
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
    oe = [r for r in rows if r.get("DOCULECT") == "Old_English"]

    # Audit every OE row whose PROTO or PROTOFORM carries an ai-diphthong.
    cands = []
    for r in oe:
        pf = (r.get("PROTOFORM") or "").strip()
        pr = (r.get("PROTO") or "").strip()
        if AI_DIPHTHONG_RE.search(pf) or AI_DIPHTHONG_RE.search(pr):
            cands.append(r)

    # Production input = PROTOFORM (fallback PROTO only if PROTOFORM empty).
    def prod_input(r: dict) -> tuple[str, str]:
        pf = (r.get("PROTOFORM") or "").strip()
        if pf:
            return normalize_proto(pf), "PROTOFORM"
        return normalize_proto((r.get("PROTO") or "").strip()), "PROTO(fallback)"

    inputs = [prod_input(r) for r in cands]
    forms = [i[0] for i in inputs]
    base = flookup(f"{tmp}/base.bin", forms)
    sc014 = flookup(f"{tmp}/sc014.bin", forms)
    sc004 = flookup(f"{tmp}/sc004.bin", forms)

    def one(d: dict[str, list[str]], f: str) -> str:
        vs = d.get(f, [])
        return vs[0] if vs else "<none>"

    out_rows = []
    for r, (form, field) in zip(cands, inputs):
        b, s14, s04 = one(base, form), one(sc014, form), one(sc004, form)
        sc014_applies = b != s14
        sc004_applies = s14 != s04
        if sc014_applies and sc004_applies:
            rewrite = "SC014:{*ai}->{*ē};SC004:{*ái}->{*ā}"
        elif sc014_applies:
            rewrite = "SC014:{*ai}->{*ē}"
        elif sc004_applies:
            rewrite = "SC004:{*ái}->{*ā}"
        else:
            rewrite = "none"
        pf = (r.get("PROTOFORM") or "").strip()
        pr = (r.get("PROTO") or "").strip()
        pf_ai = bool(AI_DIPHTHONG_RE.search(pf))
        pr_ai = bool(AI_DIPHTHONG_RE.search(pr))
        # Material disagreement: the ai-diphthong is present in one field but not
        # the other, or the two forms differ where the ai lives.
        disagree = "yes" if (pf_ai != pr_ai or (pf_ai and pr_ai and pf != pr)) else "no"
        note = re.sub(r"\s+", " ", (r.get("NOTE") or "").strip())
        if len(note) > 200:
            note = note[:197] + "..."
        out_rows.append({
            "concept": r.get("CONCEPT", ""),
            "row_id": r.get("ID", ""),
            "PROTO": pr,
            "PROTOFORM": pf,
            "prod_input_norm": form,
            "prod_field": field,
            "counterpart": r.get("COUNTERPART", ""),
            "derivation_class": r.get("DERIVATION_CLASS", ""),
            "sc014_applies": "yes" if sc014_applies else "no",
            "sc004_applies": "yes" if sc004_applies else "no",
            "rewrite_applied": rewrite,
            "proto_protoform_disagree": disagree,
            "before": b,
            "after_sc014": s14,
            "after_sc004": s04,
            "row_note": note,
        })

    out_rows.sort(key=lambda x: (x["rewrite_applied"], x["concept"]))
    with open(args.out, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out_rows[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(out_rows)

    from collections import Counter
    c = Counter(x["rewrite_applied"] for x in out_rows)
    print(f"candidates (PROTO or PROTOFORM has ai-diphthong): {len(out_rows)}")
    for k, v in sorted(c.items()):
        print(f"  {k}: {v}")
    sc014_n = sum(1 for x in out_rows if x["sc014_applies"] == "yes")
    sc004_n = sum(1 for x in out_rows if x["sc004_applies"] == "yes")
    disagree_n = sum(1 for x in out_rows if x["proto_protoform_disagree"] == "yes")
    print(f"SC014 applications: {sc014_n}; SC004 applications: {sc004_n}; "
          f"PROTO/PROTOFORM disagreements: {disagree_n}")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
