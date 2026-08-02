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

# Collision probe: under the OLD scheme (bare 2-digit suffix) a BLANK occurrence
# whose lexical sort key is "col05" would produce the same MakeIndex sort field
# ("col05") as a MERCIAN occurrence (display_order 5) of lexical form "col". The
# "~" separator makes these "col05" vs "col~05" — provably distinct.
COLLISION_SPELLING = "col"
COLLISION_ENTRIES = [
    ("col05", ""),      # blank occurrence, lexical sort key literally "col05"
    ("col", "merc"),    # Mercian occurrence of "col" -> col~05 under new scheme
]

# Cross-language entries: prove non-Old-English forms ALSO use the italicizing
# \iventry macro, and that a reconstructed form keeps exactly one asterisk.
CROSS_LANGUAGE_ENTRIES = [
    # (language, sort, display)
    ("on", "brjost", "brjóst"),      # Old Norse, attested
    ("ohg", "scouwon", "scouwōn"),   # Old High German, attested
    ("pgmc", "nedron", "*nḗdrōn"),   # Proto-Germanic, reconstructed
    ("lat", "aqua", "aqua"),         # Latin, attested
]


def build_idx_lines() -> list[str]:
    lang_meta = ivr.load_language_registry()
    var_registry = ivr.load_variety_registry()
    lines: list[str] = []
    page = 0
    for variety in VARIETIES:
        page += 1
        cmd = ivr.index_command(
            "oe", SORT, SPELLING, variety, lang_meta=lang_meta, var_registry=var_registry
        )
        body = cmd[len(r"\index[iv]{"):-1]
        lines.append(rf"\indexentry{{{body}}}{{{page}}}")
    for sort_key, variety in COLLISION_ENTRIES:
        page += 1
        cmd = ivr.index_command(
            "oe", sort_key, COLLISION_SPELLING, variety, lang_meta=lang_meta, var_registry=var_registry
        )
        body = cmd[len(r"\index[iv]{"):-1]
        lines.append(rf"\indexentry{{{body}}}{{{page}}}")
    for language, sort_key, display in CROSS_LANGUAGE_ENTRIES:
        page += 1
        cmd = ivr.index_command(
            language, sort_key, display, "", lang_meta=lang_meta, var_registry=var_registry
        )
        body = cmd[len(r"\index[iv]{"):-1]
        lines.append(rf"\indexentry{{{body}}}{{{page}}}")
    return lines


TOTAL_ENTRIES = len(VARIETIES) + len(COLLISION_ENTRIES) + len(CROSS_LANGUAGE_ENTRIES)


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
    assert accepted == TOTAL_ENTRIES, f"expected {TOTAL_ENTRIES} accepted, got {accepted}"
    # Labels appear inside the second \iventry argument; the parentheses are
    # added by the LaTeX macro at render time, so check the raw label token.
    assert r"{WS}" not in ind, "no (WS) label may appear"
    assert r"\iventry{dæg}{}" in ind, "blank variety must render with an empty label group"

    positions = []
    for label in EXPECTED_LABEL_ORDER:
        if label == "":
            continue
        needle = rf"\iventry{{dæg}}{{{label}}}"
        assert needle in ind, f"missing printed label {label!r}"
        positions.append((label, ind.index(needle)))
    assert positions == sorted(positions, key=lambda x: x[1]), (
        f"labels out of registry order: {positions}"
    )

    # Blank must sort first.
    assert ind.index(r"\iventry{dæg}{}") < ind.index(r"\iventry{dæg}{EWS}"), (
        "blank-variety entry must sort before labelled varieties"
    )

    # Collision probe: the blank "col05" and the Mercian "col" survived as two
    # DISTINCT accepted entries (no merge, no rejection). Their printed forms are
    # the bare lexical spelling "col"; the discriminator lives only in the hidden
    # sort field (col05 vs col~05), so both variants appear separately.
    assert r"\iventry{col}{}" in ind, "blank col entry missing (collision not preserved)"
    assert r"\iventry{col}{Merc.}" in ind, "Mercian col entry missing (collision not preserved)"
    assert ind.count(r"\subitem \iventry{col}") == 2, (
        "collision probe must yield two distinct 'col' subitems, not a merged entry"
    )

    # Hidden discriminator digits and separator must not leak into printed output.
    assert not re.search(r"dæg[~0]\d", ind), "hidden discriminator leaked into printed output"
    assert "~" not in ind, "discriminator separator leaked into printed output"

    # Cross-language: every non-Old-English form is italicized through \iventry
    # too, reconstructed forms keep exactly one asterisk, and headings remain
    # structurally distinct from form entries (\item vs \subitem).
    for language, sort_key, display in CROSS_LANGUAGE_ENTRIES:
        needle = rf"\iventry{{{display}}}{{}}"
        assert needle in ind, f"{language} form not italicized via \\iventry: expected {needle!r}"
    assert ind.count(r"*nḗdrōn") == 1, "reconstructed PGmc form must keep exactly one asterisk"
    assert "**" not in ind, "no doubled asterisk permitted"
    # Headings use \item \ivlangheader{...}; form entries use \subitem \iventry{...}.
    assert r"\item \ivlangheader" in ind, "language headings must remain \\item \\ivlangheader"
    assert r"\subitem \iventry" in ind, "form entries must remain \\subitem \\iventry"
    assert r"\iventry" not in ind.split(r"\subitem", 1)[0], (
        "no \\iventry form entry should precede the first \\subitem (headings are not forms)"
    )

    print("MakeIndex variety fixture passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
