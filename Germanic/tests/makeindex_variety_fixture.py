#!/usr/bin/env python3
"""Synthetic MakeIndex fixture for Old English variety discrimination.

Builds a ``.idx`` file containing the SAME lexical spelling under every variety
(blank, ews, lws, angl, merc, north, kent), runs real ``makeindex``, and
inspects the resulting ``.ilg`` (accepted/rejected) and ``.ind`` (final order).

If ``makeindex`` is not on PATH, the fixture re-executes itself inside the
canonical ``pandoc/latex`` Docker image (which ships makeindex).

Assertions:
- makeindex exit code 0;
- rejected entries == 0;
- accepted entries == 7;
- blank-variety entry prints with no ``(...)`` suffix and sorts first;
- EWS, LWS, Angl., Merc., North., Kent. all appear, ordered by display_order;
- no ``(WS)`` label anywhere;
- the hidden discriminator digits do not appear in printed output.
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "Germanic" / "tools"))
import index_verborum_render as ivr  # noqa: E402

SPELLING = "dæg"
SORT = "daeg"
VARIETIES = ["", "ews", "lws", "angl", "merc", "north", "kent"]
EXPECTED_LABEL_ORDER = ["", "EWS", "LWS", "Angl.", "Merc.", "North.", "Kent."]


def build_idx_lines() -> list[str]:
    lang_meta = ivr.load_language_registry()
    var_registry = ivr.load_variety_registry()
    lines: list[str] = []
    for page, variety in enumerate(VARIETIES, start=1):
        cmd = ivr.index_command(
            "oe", SORT, SPELLING, variety, lang_meta=lang_meta, var_registry=var_registry
        )
        body = cmd[len(r"\index[iv]{"):-1]
        lines.append(rf"\indexentry{{{body}}}{{{page}}}")
    return lines


def run_makeindex(workdir: Path) -> tuple[int, str, str]:
    idx = workdir / "fixture.idx"
    idx.write_text("\n".join(build_idx_lines()) + "\n", encoding="utf-8")
    if shutil.which("makeindex") is not None:
        proc = subprocess.run(
            ["makeindex", "fixture.idx"], cwd=workdir, capture_output=True, text=True
        )
        code = proc.returncode
    else:
        image = os.environ.get("ASSEMBLY_DOCKER_IMAGE", "pandoc/latex:latest")
        platform = os.environ.get("ASSEMBLY_DOCKER_PLATFORM", "linux/amd64")
        proc = subprocess.run(
            [
                "docker", "run", "--rm", "--platform", platform,
                "--entrypoint", "makeindex",
                "-v", f"{workdir}:/w", "-w", "/w",
                image, "fixture.idx",
            ],
            capture_output=True, text=True,
        )
        code = proc.returncode
    ilg = (workdir / "fixture.ilg").read_text(encoding="utf-8") if (workdir / "fixture.ilg").exists() else ""
    ind = (workdir / "fixture.ind").read_text(encoding="utf-8") if (workdir / "fixture.ind").exists() else ""
    return code, ilg, ind


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp)
        code, ilg, ind = run_makeindex(workdir)

    accepted = None
    rejected = None
    m = re.search(r"(\d+)\s+entries accepted", ilg)
    if m:
        accepted = int(m.group(1))
    m = re.search(r"(\d+)\s+rejected", ilg)
    if m:
        rejected = int(m.group(1))

    print(f"makeindex exit={code} accepted={accepted} rejected={rejected}")
    print("----- .ind -----")
    print(ind)

    assert code == 0, f"makeindex failed with exit {code}: {ilg}"
    assert rejected == 0, f"makeindex rejected {rejected} entries: {ilg}"
    assert accepted == len(VARIETIES), f"expected {len(VARIETIES)} accepted, got {accepted}"
    # Labels appear inside the second \ivoeentry argument; the parentheses are
    # added by the LaTeX macro at render time, so check the raw label token.
    assert r"{WS}" not in ind, "no (WS) label may appear"
    assert r"\ivoeentry{dæg}{}" in ind, "blank variety must render with an empty label group"

    positions = []
    for label in EXPECTED_LABEL_ORDER:
        if label == "":
            continue
        needle = rf"\ivoeentry{{dæg}}{{{label}}}"
        assert needle in ind, f"missing printed label {label!r}"
        positions.append((label, ind.index(needle)))
    assert positions == sorted(positions, key=lambda x: x[1]), (
        f"labels out of registry order: {positions}"
    )

    # Blank must sort first.
    assert ind.index(r"\ivoeentry{dæg}{}") < ind.index(r"\ivoeentry{dæg}{EWS}"), (
        "blank-variety entry must sort before labelled varieties"
    )

    # Hidden discriminator digits (e.g. the '02'..'07' appended to the sort key)
    # must not leak into printed output as a standalone token next to the form.
    assert not re.search(r"dæg0\d", ind), "hidden discriminator leaked into printed output"

    print("MakeIndex variety fixture passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
