"""Preserve the distinction between SC039 computation and historical adequacy."""

import hashlib
import json
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "Germanic/docs/sound_changes/audits/sc039-experiments"
sys.path.insert(0, str(ROOT / "Germanic/tools"))
from executable_facts import parse_defines


def evidence():
    return json.loads((AUDIT / "evidence.json").read_text())


def test_current_rule_matches_the_actual_historical_control_experiment():
    manifest = json.loads((AUDIT / "manifest.json").read_text())
    assert hashlib.sha256((AUDIT / "experiments.zip").read_bytes()).hexdigest() == manifest["archive_sha256"]
    assert hashlib.sha256((AUDIT / "evidence.json").read_bytes()).hexdigest() == manifest["evidence_sha256"]
    with zipfile.ZipFile(AUDIT / "experiments.zip") as archive:
        name = next(n for n in archive.namelist()
                    if n.endswith("sc039-historical-controls-03/snapshot/source.txt"))
        source = archive.read(name)
    assert hashlib.sha256(source).hexdigest() == evidence()["fst_sha256"]
    tested = parse_defines(source.decode())
    current = parse_defines((ROOT / "Germanic/fsts/germanic.txt").read_text())
    assert current["OEWICombinativeUUmlaut"].body == tested["OEWICombinativeUUmlaut"].body


def test_widow_wood_and_week_change_but_missing_w_a_trigger_and_cluster_do_not():
    controls = {r["id"]: r for r in evidence()["controls"]}
    for name in ("widow", "wood", "week"):
        row = controls[name]
        assert row["actual"] == [row["expected"]]
        assert row["actual"] != [row["input"]]
    for name in ("no-w", "a-trigger", "cluster", "kw-proxy-limit"):
        row = controls[name]
        assert row["actual"] == [row["input"]]


def test_supported_know_comparison_is_not_disguised_as_a_synthetic_rejection():
    report = evidence()
    rows = {r["input"]: r for r in report["historical_controls"]}
    for row in rows.values():
        assert len(row["parser"]) == 1
        assert len(row["final"]) == 1
        assert row["encoded_input"] == row["input"].removeprefix("*")
    assert rows["*wíduwōn"]["final"] == ["wuduwe"]
    assert rows["*wíduz"]["final"] == ["wudu"]
    row = rows["*wítun"]
    assert row["before"] == ["*w*í*t*u*n"]
    assert row["after"] == ["*w*ú*t*u*n"]
    assert row["final"] == ["wutun"]
    assert row["final"] not in (["witon"], ["wioton"])
    assert rows["*wítaną"]["before"] == rows["*wítaną"]["after"]
    assert (report["selected_count"], report["selected_final_changes"]) == (391, 0)
