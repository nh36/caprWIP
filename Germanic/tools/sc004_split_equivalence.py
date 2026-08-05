#!/usr/bin/env python3
"""Formal equivalence proof: SC004 split candidate == PWGmcAiMonophthongization.

Sandbox / research only. Builds a behaviour-neutral component split of the
production rule and proves it is compositionally identical, both as an
unrestricted transducer relation and over the admitted input language
(EnglishProtoInput). Does NOT modify the production rule.

Split candidate (research names):
    SC004FinalAiToE      [ {*ai} -> {*ē} || _ .#. ]
    SC004GeneralAiToA    [ [{*ai} -> {*ā}] .o. [{*ái} -> {*ā}] ]
    SC004SplitCandidate  [ SC004FinalAiToE .o. SC004GeneralAiToA ]

Runs inside the backend container (needs foma); CWD = /usr/app.
"""
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

CANDIDATE = r"""
define SC004FinalAiToE      [ {*ai} -> {*ē} || _ .#. ];
define SC004GeneralAiToA    [ [{*ai} -> {*ā}] .o. [{*ái} -> {*ā}] ];
define SC004SplitCandidate  [ SC004FinalAiToE .o. SC004GeneralAiToA ];
"""

SCRIPT = r"""
source fsts/germanic.txt
""" + CANDIDATE + r"""
clear stack
regex SC004SplitCandidate;
regex PWGmcAiMonophthongization;
test equivalent
clear stack
regex [ EnglishProtoInput .o. SC004SplitCandidate ];
regex [ EnglishProtoInput .o. PWGmcAiMonophthongization ];
test equivalent
quit
"""

_RESULT_RE = re.compile(r"^(\d)\s*\(1 = TRUE")


def main() -> int:
    with tempfile.NamedTemporaryFile("w", suffix=".foma", delete=False, encoding="utf-8") as h:
        sp = Path(h.name)
        h.write(SCRIPT)
    try:
        proc = subprocess.run(["foma", "-q", "-f", str(sp)],
                              stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    finally:
        sp.unlink(missing_ok=True)
    results = [m.group(1) for line in proc.stdout.decode("utf-8", "replace").splitlines()
               if (m := _RESULT_RE.match(line.strip()))]
    if len(results) != 2:
        print(f"FAIL: expected 2 equivalence results, got {results}", file=sys.stderr)
        return 1
    unrestricted, admitted = results
    print(f"unrestricted relation equivalent: {'TRUE' if unrestricted=='1' else 'FALSE'}")
    print(f"equivalent over EnglishProtoInput: {'TRUE' if admitted=='1' else 'FALSE'}")
    if unrestricted == "1" and admitted == "1":
        print("SC004 SPLIT EQUIVALENCE PROVEN: SC004SplitCandidate == PWGmcAiMonophthongization")
        return 0
    print("SC004 SPLIT EQUIVALENCE FAILED", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
