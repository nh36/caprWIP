#!/usr/bin/env python3
"""SC004 split component-behavior probe (permanent evidence generator).

After the SC004 Outcome-C split, the bundled PWGmcAiMonophthongization is
separated into two production rules that live at different cascade stages:

  SC014  PNWGmcUnstressedAiMonophthongization : {*ai} -> {*e} || _ .#.
         (word-final unstressed *ai; Proto-Northwest Germanic, early)
  SC004  EAFAiMonophthongization              : [{*ai}->{*a} || _ ?] .o. [{*ai(acute)}->{*a}]
         (general/root *ai/*ai(acute); Early Anglo-Frisian, later)

This tool applies each production define (and the retained compatibility alias
PWGmcAiMonophthongization) to a curated set of internal star-representation
probe forms and records the observed output against the expected output. It is
the foma-backed evidence behind tests/test_sc004_component_split.py.

Runs inside the backend container (needs foma/flookup); CWD = /usr/app.
Writes a TSV to --out (default the committed evidence path).

The probes deliberately include the fem. o-stem dat.sg. *spannai (word-final
unstressed *ai): it has no corpus attestation but is the canonical form the
final/general split must keep distinct, so it is the clearest demonstration
that SC014 (final only) and SC004 (nonfinal/stressed only) do not overlap.
"""
from __future__ import annotations

import argparse
import csv
import subprocess
import tempfile
from pathlib import Path

# Regex the three production defines straight out of germanic.txt (they already
# exist there after the split) and snapshot each to its own bin.
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
    # SC014 performs the word-final unstressed *ai -> *e change.
    ("final_ai_to_e", "SC014_PNWGmcUnstressedAiMonophthongization",
     "*s*p*a*n*n*ai", "*s*p*a*n*n*ē",
     "fem. o-stem dat.sg *spannai: word-final unstressed *ai -> *e"),
    # SC014 does NOT perform the general/root *ai -> *a development.
    ("sc014_leaves_stressed", "SC014_PNWGmcUnstressedAiMonophthongization",
     "*s*ái*w*a*l*ō", "*s*ái*w*a*l*ō",
     "soul: stressed root *ai(acute) is untouched by SC014 (final-only)"),
    ("sc014_leaves_nonfinal", "SC014_PNWGmcUnstressedAiMonophthongization",
     "*l*ai*m*ō*n", "*l*ai*m*ō*n",
     "loam: nonfinal unaccented *ai is untouched by SC014 (final-only)"),
    # SC004 performs stressed *ai(acute) -> *a.
    ("sc004_stressed_ai_to_a", "SC004_EAFAiMonophthongization",
     "*s*ái*w*a*l*ō", "*s*ā*w*a*l*ō",
     "soul: stressed root *ai(acute) -> *a (SC036 boundary witness)"),
    # SC004 handles the two unaccented root cases (no accent in the data).
    ("sc004_loam_nonfinal", "SC004_EAFAiMonophthongization",
     "*l*ai*m*ō*n", "*l*ā*m*ō*n",
     "loam: unaccented nonfinal *ai -> *a"),
    ("sc004_whine_nonfinal", "SC004_EAFAiMonophthongization",
     "*w*ai*n*ō*j*a*n*ą", "*w*ā*n*ō*j*a*n*ą",
     "whine: unaccented nonfinal *ai -> *a"),
    # SC004 does NOT touch word-final unstressed *ai (clean separation from SC014).
    ("sc004_leaves_final", "SC004_EAFAiMonophthongization",
     "*s*p*a*n*n*ai", "*s*p*a*n*n*ai",
     "fem. o-stem dat.sg *spannai: word-final unstressed *ai untouched by SC004"),
    # Compatibility alias reproduces the bundled relation A .o. (B .o. C).
    ("alias_final_path", "ALIAS_PWGmcAiMonophthongization",
     "*s*p*a*n*n*ai", "*s*p*a*n*n*ē",
     "alias == A.o.(B.o.C): final *ai -> *e via A"),
    ("alias_stressed_path", "ALIAS_PWGmcAiMonophthongization",
     "*s*ái*w*a*l*ō", "*s*ā*w*a*l*ō",
     "alias == A.o.(B.o.C): stressed *ai(acute) -> *a via C"),
    ("alias_nonfinal_path", "ALIAS_PWGmcAiMonophthongization",
     "*l*ai*m*ō*n", "*l*ā*m*ō*n",
     "alias == A.o.(B.o.C): nonfinal *ai -> *a via B"),
]


def flookup_one(bin_path: str, form: str) -> str:
    proc = subprocess.run(["flookup", "-i", "-x", bin_path],
                          input=(form + "\n").encode("utf-8"),
                          stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    outs = [ln for ln in proc.stdout.decode("utf-8", "replace").splitlines() if ln.strip()]
    # An identity rule leaves the form unchanged; flookup -x echoes the single
    # output. "+?" marks no analysis (should not happen for these total rules).
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
        print(f"  [{flag}] {r['probe_id']:24s} {r['input']} -> {r['output']} (expect {r['expected']})")
    print(f"wrote {args.out}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
