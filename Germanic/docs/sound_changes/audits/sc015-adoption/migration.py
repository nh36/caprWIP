#!/usr/bin/env python3
"""Record and verify the separately authorized SC015 rule and target transition."""
from __future__ import annotations

import csv
import gzip
import hashlib
import io
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
import cascade_baseline as baseline

BASE_COMMIT = "23c146eddd2d9f7527a05363b6768e352eddeb54"
BASE = ROOT / "Germanic/docs/sound_changes/cascade_baseline"
CORPUS = ROOT / "Germanic/data/germanic-aligned-final.tsv"
TARGETS = {"2095": "leornian", "2313": "leorna", "2314": "leornaþ"}
SOURCES = {
    "2095": "Crawford1922 p.71; Ælfric's Treatise: þu scealt leornian (infinitive)",
    "2313": "Crawford1922 p.351; Deuteronomy14:23: leorna (imperative2sg)",
    "2314": "Miller1891 p.380 ll.26–27; Bede IV.31: leornað with singular swa hwylc swa; ð→þ",
}


def committed(path: Path) -> bytes:
    return subprocess.check_output(
        ["git", "show", f"{BASE_COMMIT}:{path.relative_to(ROOT).as_posix()}"], cwd=ROOT)


def rows(data: bytes) -> list[dict]:
    return list(csv.DictReader(io.StringIO(data.decode()), delimiter="\t"))


def build() -> dict:
    old, new = rows(committed(CORPUS)), rows(CORPUS.read_bytes())
    if [r["ID"] for r in old] != [r["ID"] for r in new]:
        raise ValueError("corpus row identities or order changed")
    changes = {}
    before = baseline.read_baseline(
        BASE / "cascade_baseline_outputs_pre_sc015.tsv",
        BASE / "cascade_baseline_summary_pre_sc015.json")
    after = baseline.read_baseline(
        BASE / "cascade_baseline_outputs.tsv", BASE / "cascade_baseline_summary.json")
    approval = json.loads((BASE / "approved_sc015_targets_migration.json").read_text())
    baseline.validate_cell_transition(before, after, approval)
    previous = {r["row_id"]: r for r in before["records"]}
    current = {r["row_id"]: r for r in after["records"]}
    for a, b in zip(old, new, strict=True):
        fields = {key for key in a if a[key] != b[key]}
        if not fields:
            continue
        identifier = b["ID"]
        expected = {"COUNTERPART", "TOKENS", "NOTE"} | (
            {"IPA"} if identifier in {"2313", "2314"} else set())
        if identifier not in TARGETS or fields != expected or b["COUNTERPART"] != TARGETS[identifier]:
            raise ValueError(f"unapproved corpus field change: {identifier}: {fields}")
        changes[identifier] = {
            "before": a, "after": b, "changed_fields": sorted(fields),
            "predicted_before": previous[identifier]["outputs"],
            "predicted_after": current[identifier]["outputs"],
            "match_before": previous[identifier]["match"],
            "match_after": current[identifier]["match"],
            "target_evidence": SOURCES[identifier],
            "authorization": "SC015 canonical adjudication; explicit 16 October 2026 user instruction",
        }
    if changes.keys() != TARGETS.keys():
        raise ValueError("incomplete three-cell selection transition")
    captured_before = json.loads(gzip.decompress((HERE / "before.json.gz").read_bytes()))
    captured_after = json.loads(gzip.decompress((HERE / "after.json.gz").read_bytes()))
    protected = captured_before["protected_archives"]
    for name, digest in protected.items():
        if hashlib.sha256((BASE / name).read_bytes()).hexdigest() != digest:
            raise ValueError(f"pre-existing approval/archive changed: {name}")
    for stem, suffix in (("outputs", "tsv"), ("summary", "json")):
        if (BASE / f"cascade_baseline_{stem}_pre_sc015.{suffix}").read_bytes() != committed(
                BASE / f"cascade_baseline_{stem}.{suffix}"):
            raise ValueError("pre-SC015 archive differs from actual incumbent")
    return {
        "base_commit": BASE_COMMIT, "adjudication": "SC015",
        "scientific_decision": "Adopt consonant-conditioned Candidate B at unchanged position.",
        "lexical_decision": "Select three independently attested leorn- targets; retain all inherited inputs.",
        "changes": changes, "previous_summary": before["summary"], "current_summary": after["summary"],
        "matched_three_states": captured_after["matched_three_states"],
        "final_changed_ids": list(captured_after["final_deltas"]),
        "intermediate_changed_ids": list(captured_after["intermediate_deltas"]),
        "preserved_approval_archive_sha256": protected,
    }


if __name__ == "__main__":
    (HERE / "migration.json").write_text(
        json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Verified three exact corpus changes, strict migration and every preceding approval/archive.")
