#!/usr/bin/env python3
"""Publish the pinned SC044 observations without changing canonical projections."""
import argparse
import csv
import hashlib
import io
import json
import sys
import zipfile
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
from cascade_baseline import legacy_subset
from experiment_snapshot import Snapshot


def tsv(path):
    return list(csv.DictReader(io.StringIO(path.read_text()), delimiter="\t"))


def write_tsv(path, rows):
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def differences(before, after):
    old = {r["row_id"]: r for r in before}
    new = {r["row_id"]: r for r in after}
    assert old.keys() == new.keys()
    return [
        {"row_id": identifier, "concept": old[identifier]["concept"],
         "changed": [key for key in old[identifier]
                     if old[identifier][key] != new[identifier][key]],
         "before": old[identifier], "after": new[identifier]}
        for identifier in old if old[identifier] != new[identifier]
    ]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("followup", type=Path)
    parser.add_argument("secondary", type=Path, nargs="?")
    args = parser.parse_args()
    snapshot = Snapshot(args.snapshot.resolve())
    snapshot.verify()
    followup = Snapshot(args.followup.resolve())
    followup.verify()
    assert followup.completion()["outcome"] == "passed"
    variants = snapshot.receipt()["variants"]
    work = ROOT / ".capr-work/sc044"
    results = {}
    for name in variants:
        path = work / (name + "-result.json")
        if not path.exists():
            path = work / "repair" / (name + "-result.json")
        results[name] = json.loads(path.read_text())
        assert results[name]["source_sha256"] == snapshot.receipt()["inputs"][name]["sha256"]
    repairs = {name: json.loads((work / "repair" / (name + "-result.json")).read_text())
               for name in followup.receipt()["variants"]}
    control = results["control"]
    records = control["corpus"]["records"]
    baseline_dir = ROOT / "Germanic/docs/sound_changes/cascade_baseline"
    legacy = legacy_subset(
        records, tsv(baseline_dir / "cascade_baseline_outputs_legacy380.tsv"),
        tsv(baseline_dir / "approved_input_migrations.tsv"))
    protected = {r["row_id"] for r in legacy}
    assert len(protected) == 380
    before = control["checkpoints"]["EAFBrighteningLongFinal"]
    after = control["checkpoints"]["OEBreaking"]
    census = []
    for row in records:
        identifier = row["row_id"]
        if before[identifier] == after[identifier]:
            continue
        assert len(before[identifier]) == len(after[identifier]) == 1
        incoming, outgoing = before[identifier][0], after[identifier][0]
        a, b = incoming.split("*")[1:], outgoing.split("*")[1:]
        index = next(i for i, pair in enumerate(zip(a, b)) if pair[0] != pair[1])
        assert a[index] in {"æ", "é"}
        context = "".join(a[index + 1:index + 3])
        census.append({
            "row_id": identifier, "concept": row["concept"], "selected_input": row["proto"],
            "counterpart": row["counterpart"],
            "component": "A" if a[index] == "æ" else "E",
            "input_vowel": a[index], "context": context,
            "immediate_input": incoming, "immediate_output": outgoing,
            "protected_legacy380": int(identifier in protected),
        })
    census.sort(key=lambda r: int(r["row_id"]))
    assert Counter(r["component"] for r in census) == {"A": 29, "E": 21}
    write_tsv(HERE / "firing-census.tsv", census)
    report = {
        "base_commit": variants and snapshot.receipt()["expected_outcomes"]["base_commit"],
        "snapshot_id": snapshot.receipt()["experiment_id"],
        "snapshot_outcome": snapshot.completion()["outcome"],
        "followup_snapshot_id": followup.receipt()["experiment_id"],
        "followup_inputs": followup.receipt()["inputs"],
        "inputs": snapshot.receipt()["inputs"],
        "summary": control["corpus"]["summary"],
        "protected_firing_count": sum(r["protected_legacy380"] for r in census),
        "frozen_baseline_diff": differences(
            tsv(baseline_dir / "cascade_baseline_outputs.tsv"), records),
        "experiments": {},
    }
    assert report["frozen_baseline_diff"] == []
    for name, result in results.items():
        published = {key: value for key, value in result.items()
                     if key not in {"corpus", "checkpoints"}}
        if result["corpus"] is not None:
            published["summary"] = result["corpus"]["summary"]
            published["corpus_delta"] = differences(records, result["corpus"]["records"])
            changed_ids = {row["row_id"] for row in published["corpus_delta"]}
            published["changed_row_checkpoints"] = {
                stage: {identifier: forms for identifier, forms in values.items()
                        if identifier in changed_ids}
                for stage, values in result["checkpoints"].items()
            }
        report["experiments"][name] = published
    adopted = repairs["candidate"]
    additional_roots = []
    if args.secondary:
        secondary = Snapshot(args.secondary.resolve())
        secondary.verify()
        assert secondary.completion()["outcome"] == "passed"
        report["secondary_snapshot_id"] = secondary.receipt()["experiment_id"]
        report["pre_secondary_carry"] = {
            key: value for key, value in adopted.items()
            if key not in {"corpus", "checkpoints"}}
        report["pre_secondary_carry"]["qualification"] = (
            "The first full strict run exposed two conditional-compound regressions. "
            "Its separate finite Anglian relations remain pinned historical evidence, "
            "not newly compiled production components.")
        adopted = json.loads((work / "stress-carry/result.json").read_text())
        assert adopted["source_sha256"] == secondary.receipt()["inputs"]["candidate"]["sha256"]
        additional_roots = [
            ROOT / ".capr-work/experiments/sc044-secondary-carry-f5edba0a",
            ROOT / ".capr-work/experiments/sc044-secondary-carry-a845fcd8",
            secondary.root,
        ]
    report["adopted"] = {key: value for key, value in adopted.items()
                         if key not in {"corpus", "checkpoints"}}
    report["adopted"]["summary"] = adopted["corpus"]["summary"]
    report["adopted"]["corpus_delta"] = differences(records, adopted["corpus"]["records"])
    report["repairs"] = {name: {key: value for key, value in result.items()
                               if key not in {"corpus", "checkpoints"}}
                         for name, result in repairs.items() if name != "candidate"}
    reverified = work / "reverification"
    report["reverification"] = [
        json.loads(path.read_text()) for path in sorted(reverified.glob("*.receipt.json"))]
    selected = {r["row_id"]: r for r in adopted["corpus"]["records"]}
    comparison = []
    for row in records:
        new = selected[row["row_id"]]
        comparison.append({
            "row_id": row["row_id"], "concept": row["concept"],
            "input_control": row["fst_input"], "input_candidate": new["fst_input"],
            "comparator_control": row["counterpart"], "comparator_candidate": new["counterpart"],
            "outputs_control": row["outputs"], "outputs_candidate": new["outputs"],
            "count_control": row["output_count"], "count_candidate": new["output_count"],
            "accepted_control": row["accepted"], "accepted_candidate": new["accepted"],
            "match_control": row["match"], "match_candidate": new["match"],
            "identical_record": int(row == new),
        })
    write_tsv(HERE / "corpus-comparison.tsv", comparison)
    (HERE / "observed.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    archive_path = HERE / "experiments.zip"
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for root in (snapshot.root, followup.root, *additional_roots):
            for path in sorted(root.rglob("*")):
                if path.is_file():
                    archive.write(path, root.name + "/" + str(path.relative_to(root)))
        for path in sorted(reverified.glob("*")):
            if path.is_file():
                archive.write(path, "reverification/" + path.name)
        if args.secondary:
            for receipt_path in sorted((work / "validation").glob("sc044-strict-serial-*.receipt.json")):
                receipt = json.loads(receipt_path.read_text())
                if receipt["ok"]:
                    continue
                paths = [receipt_path, Path(receipt["stdout_log"]), Path(receipt["stderr_log"])]
                if receipt.get("junit_path"):
                    paths.append(Path(receipt["junit_path"]))
                for path in paths:
                    archive.write(path, "prior-strict-failure/" + path.name)
    (HERE / "archive.sha256").write_text(
        hashlib.sha256(archive_path.read_bytes()).hexdigest() + "  experiments.zip\n")
    print(json.dumps({
        "summary": report["summary"], "firing_count": len(census),
        "protected_firings": report["protected_firing_count"],
        "candidate_delta": report["adopted"]["corpus_delta"],
        "archive_bytes": archive_path.stat().st_size,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
