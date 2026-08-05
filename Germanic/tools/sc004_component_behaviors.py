#!/usr/bin/env python3
"""SC004/SC014 split component-behavior probe (permanent evidence generator).

After the corrective PROTOFORM pass, the two production rules are the
historically cleaner pair:

  SC014  PNWGmcUnstressedAiMonophthongization : {*ai} -> {*ē}
         (unstressed *ai, in final AND nonfinal environments; Ringe-Taylor's
         rule is unstressed *ai > *ē, not merely word-final)
  SC004  EAFAiMonophthongization              : {*ái} -> {*ā}
         (stressed/root *ái; Early Anglo-Frisian / North Sea Germanic)

This tool applies each production define (and the retained compatibility alias
PWGmcAiMonophthongization = SC014 .o. SC004) to internal star-representation
probes covering both Ringe-Taylor handbook paradigm examples (final AND nonfinal
unstressed *ai) and the actual corpus PROTOFORM values, and records observed vs
expected. It is the foma-backed evidence behind tests/test_sc004_component_split.py.

Runs inside the backend container (needs foma/flookup); CWD = /usr/app.
"""
from __future__ import annotations

import argparse
import csv
import subprocess
import tempfile
from pathlib import Path

FOMA_SCRIPT = r"""
source fsts/germanic.txt
clear stack
regex PNWGmcUnstressedAiMonophthongization;
save stack {tmp}/sc014.bin
clear stack
regex EAFAiMonophthongization;
save stack {tmp}/sc004.bin
clear stack
regex PWGmcAiMonophthongization;
save stack {tmp}/alias.bin
quit
"""

BIN_BY_RULE = {
    "SC014_PNWGmcUnstressedAiMonophthongization": "sc014.bin",
    "SC004_EAFAiMonophthongization": "sc004.bin",
    "ALIAS_PWGmcAiMonophthongization": "alias.bin",
}

# (probe_id, rule_key, input, expected_output, note)
PROBES = [
    # --- Ringe-Taylor handbook paradigm examples: unstressed *ai > *ē ---
    ("rt_final_dagai", "SC014_PNWGmcUnstressedAiMonophthongization",
     "*d*a*g*ai", "*d*a*g*ē",
     "R/T word-final unstressed *dagai > *dagē"),
    ("rt_nonfinal_berain", "SC014_PNWGmcUnstressedAiMonophthongization",
     "*b*e*r*ai*n", "*b*e*r*ē*n",
     "R/T NONFINAL unstressed *berain > *berēn (needs SC014 without ||_.#.)"),
    ("rt_nonfinal_habaisi", "SC014_PNWGmcUnstressedAiMonophthongization",
     "*h*a*b*ai*s*i", "*h*a*b*ē*s*i",
     "R/T nonfinal unstressed *habaisi > *habēsi at the SC014 checkpoint"),
    ("rt_nonfinal_godaimaz", "SC014_PNWGmcUnstressedAiMonophthongization",
     "*g*ō*d*ai*m*a*z", "*g*ō*d*ē*m*a*z",
     "R/T nonfinal unstressed *gōdaimaz > *gōdēmaz"),
    # SC014 does NOT touch stressed *ái.
    ("sc014_leaves_stressed", "SC014_PNWGmcUnstressedAiMonophthongization",
     "*s*t*ái*n*a*z", "*s*t*ái*n*a*z",
     "stressed *stáinaz untouched by SC014 (stressed is SC004)"),
    # --- stressed/root *ái > *ā (SC004) ---
    ("sc004_stressed_stainaz", "SC004_EAFAiMonophthongization",
     "*s*t*ái*n*a*z", "*s*t*ā*n*a*z",
     "stressed/root *stáinaz > *stānaz"),
    # SC004 does NOT touch unstressed *ai.
    ("sc004_leaves_unstressed", "SC004_EAFAiMonophthongization",
     "*s*p*á*n*n*ai", "*s*p*á*n*n*ai",
     "unstressed final *spánnai untouched by SC004 (unstressed is SC014)"),
    # --- actual corpus PROTOFORM values ---
    ("corpus_span_sc014", "SC014_PNWGmcUnstressedAiMonophthongization",
     "*s*p*á*n*n*ai", "*s*p*á*n*n*ē",
     "corpus span *spánnai (dat.sg) > *spánnē via SC014 (-> OE spanne)"),
    ("corpus_loam_sc004", "SC004_EAFAiMonophthongization",
     "*l*ái*m*ą", "*l*ā*m*ą",
     "corpus loam *láimą (stressed by its PROTOFORM) > *lāmą via SC004 (-> OE lām)"),
    ("corpus_whine_neither_sc014", "SC014_PNWGmcUnstressedAiMonophthongization",
     "*x*w*ḯ*n*a*n*ą", "*x*w*ḯ*n*a*n*ą",
     "corpus whine *xwḯnaną has no *ai in PROTOFORM: unchanged by SC014"),
    ("corpus_whine_neither_sc004", "SC004_EAFAiMonophthongization",
     "*x*w*ḯ*n*a*n*ą", "*x*w*ḯ*n*a*n*ą",
     "corpus whine *xwḯnaną has no *ai in PROTOFORM: unchanged by SC004"),
    # --- compatibility alias reproduces SC014 .o. SC004 ---
    ("alias_unstressed_path", "ALIAS_PWGmcAiMonophthongization",
     "*s*p*á*n*n*ai", "*s*p*á*n*n*ē",
     "alias == SC014 .o. SC004: unstressed *ai -> *ē via SC014"),
    ("alias_stressed_path", "ALIAS_PWGmcAiMonophthongization",
     "*s*t*ái*n*a*z", "*s*t*ā*n*a*z",
     "alias == SC014 .o. SC004: stressed *ái -> *ā via SC004"),
]


def flookup_one(bin_path: str, form: str) -> str:
    proc = subprocess.run(["flookup", "-i", "-x", bin_path],
                          input=(form + "\n").encode("utf-8"),
                          stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    outs = [ln for ln in proc.stdout.decode("utf-8", "replace").splitlines() if ln.strip()]
    return outs[0] if outs else "<none>"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out",
                    default="docs/sound_changes/order_tests/sc004_component_behaviors.tsv")
    args = ap.parse_args()

    tmp = tempfile.mkdtemp()
    script = FOMA_SCRIPT.replace("{tmp}", tmp)
    sp = Path(tmp) / "build.foma"
    sp.write_text(script, encoding="utf-8")
    subprocess.run(["foma", "-q", "-f", str(sp)], stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, check=True)

    rows = []
    all_pass = True
    for probe_id, rule_key, form, expected, note in PROBES:
        bin_path = f"{tmp}/{BIN_BY_RULE[rule_key]}"
        got = flookup_one(bin_path, form)
        ok = got == expected
        all_pass = all_pass and ok
        rows.append({
            "probe_id": probe_id,
            "rule": rule_key,
            "input": form,
            "output": got,
            "expected": expected,
            "pass": "1" if ok else "0",
            "note": note,
        })

    with open(args.out, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    for r in rows:
        flag = "ok " if r["pass"] == "1" else "FAIL"
        print(f"  [{flag}] {r['probe_id']:26s} {r['input']} -> {r['output']} (expect {r['expected']})")
    print(f"wrote {args.out}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
