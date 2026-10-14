"""Verify the general nasal-bimoric repair against the frozen investigation."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
import tempfile
from pathlib import Path

import anglo_frisian_experiments as assay
import oe_pipeline
from capr_runtime import layout
from executable_facts import parse_defines


CLASSES = (
    "pgrmLongVowel", "pgrmWeakTailVowel", "PGmcStarVowel",
    "PGmcStarBackVowel", "EnglishStarLongVowel",
    "EnglishWeakTailVowelStar", "EnglishStarNonHighVowel",
)


def preservation_report(root: Path) -> dict:
    investigation = root / "Germanic/docs/sound_changes/audits/sc017-sc019-wull-investigation"
    original = json.loads((investigation / "wull-production-protection-before.json").read_text())
    source_changes = {
        "Germanic/fsts/germanic.txt",
    }
    generated_changes = {
        "backend/oe_build_manifest.json",
        "Germanic/docs/sound_changes/cascade_baseline/oe_equivalence_report.json",
        "Germanic/docs/sound_changes/cascade_baseline/cascade_interaction_matrix.tsv",
        "Germanic/docs/sound_changes/cascade_baseline/cascade_interaction_provenance.json",
        "Germanic/docs/sound_changes/cascade_baseline/cascade_interaction_report.md",
    }
    records = []
    for name, checksum in original.items():
        current = hashlib.sha256((root / name).read_bytes()).hexdigest()
        changed = current != checksum
        if not changed:
            classification = "unchanged"
        elif name in source_changes:
            classification = "authorized_source_repair"
        elif name in generated_changes or (name.startswith("backend/") and name.endswith(".bin")):
            classification = "required_generated_rebuild"
        else:
            raise RuntimeError(f"Unauthorized protected-file change: {name}")
        records.append({"path": name, "before": checksum, "after": current,
                        "classification": classification})
    with (investigation / "publication-sha256.tsv").open() as handle:
        for line in list(handle)[1:]:
            name, checksum = line.rstrip("\r\n").split("\t")
            if hashlib.sha256((investigation / name).read_bytes()).hexdigest() != checksum:
                raise RuntimeError(f"Frozen investigation artifact changed: {name}")
    if len(records) != 163:
        raise RuntimeError("Original protection set no longer contains 163 files")
    return {
        "protected_files": len(records),
        "unchanged": sum(row["classification"] == "unchanged" for row in records),
        "authorized_source_repairs": sum(
            row["classification"] == "authorized_source_repair" for row in records),
        "required_generated_rebuilds": sum(
            row["classification"] == "required_generated_rebuild" for row in records),
        "frozen_investigation_verified": True,
        "files": records,
    }


def consumer_audit(text: str) -> dict[str, list[str]]:
    definitions = parse_defines(text)
    dependencies = {
        name: set(re.findall(r"\b[A-Za-z][A-Za-z0-9]*\b", fact.body)) & definitions.keys()
        for name, fact in definitions.items()
    }
    result = {}
    for changed in CLASSES:
        reachable = {changed}
        while True:
            expanded = reachable | {
                name for name, refs in dependencies.items() if refs & reachable
            }
            if expanded == reachable:
                break
            reachable = expanded
        result[changed] = sorted(reachable - {changed})
    return result


def verify() -> dict:
    runtime = layout()
    if not runtime.is_container:
        raise RuntimeError("Run this isolated assay inside the backend container")
    frozen = runtime.docs_dir / "sound_changes/audits/sc017-sc019-wull-investigation"
    baseline = json.loads(gzip.decompress((frozen / "identity-replay.json.gz").read_bytes()))
    stage_map = json.loads((frozen / "stage_map.json").read_text())
    recipe = {
        "id": "sc017-nasal-bimoric-adoption", "definitions": "",
        "replace": {}, "insert_rule": "", "insert_before": "", "insert_after": "",
        "component_checks": [
            {"component": name} for name in (
                *CLASSES, "EnglishProtoInput", "PNWGmcULowering", "PNWGmcILowering",
                "PNWGmcFinalLongORaising", "PNWGmcStressedMonosyllableORaising",
            )
        ],
    }
    order = assay.complete_variant_order(recipe)
    if order != [item["expression"] for item in stage_map]:
        raise RuntimeError("Executable ordering differs from the frozen investigation")
    rows = assay.corpus_rows(runtime.corpus_tsv)
    old = baseline["rows"]
    if len(rows) != 387 or [row["id"] for row in rows] != [row["id"] for row in old]:
        raise RuntimeError("Selected population changed")
    for row, prior in zip(rows, old):
        for key in ("proto", "counterpart", "fst_input"):
            if row[key] != prior[key]:
                raise RuntimeError(f"{row['id']}: selected {key} changed")
    protected = [
        runtime.germanic_fst, runtime.corpus_tsv, runtime.build_manifest,
        runtime.bin_dir / "old_english.bin", runtime.sandbox_fst,
        *(runtime.bin_dir / name for name in oe_pipeline.expected_snapshot_bins()),
    ]
    before = {str(path): assay.digest(path) for path in protected}
    checks = []
    with tempfile.TemporaryDirectory(prefix="capr_nasal_bimoric_") as temporary:
        bins = assay.compile_isolated(
            runtime.germanic_fst, recipe, [], Path(temporary), diagnostic_stages=order,
        )

        def check(component, form, expected):
            actual = assay.batch_apply_down(bins[f"component:{component}"], [form])[0]
            if actual != expected:
                raise RuntimeError(f"{component}: {form!r}: {actual!r} != {expected!r}")
            checks.append({"component": component, "input": form, "outputs": actual})

        for name in ("PGmcStarVowel", "PGmcStarBackVowel", "EnglishStarLongVowel",
                     "EnglishStarNonHighVowel", "EnglishWeakTailVowelStar"):
            check(name, "*ǭ", ["*ǭ"])
        for name in ("pgrmLongVowel", "pgrmWeakTailVowel"):
            for raw in ("ō", "ǭ", "ô"):
                check(name, raw, ["*" + raw])
        for raw in ("wúllō", "wúllǭ", "wullǭ", "wúllô"):
            check("EnglishProtoInput", raw, ["".join("*" + char for char in raw)])
        check("EnglishProtoInput", "wúllôz", [])
        for prefix in ("", "*ᵘ", "*ᶜ"):
            for ending, root in (("ō", "ó"), ("ǭ", "ó"), ("ô", "ó"),
                                 ("ą", "ó"), ("ę", "ú"), ("ų", "ú"), ("u", "ú")):
                check("PNWGmcULowering", prefix + "*w*ú*l*l*" + ending,
                      [prefix + "*w*" + root + "*l*l*" + ending])
            check("PNWGmcILowering", prefix + "*n*í*s*ǭ", [prefix + "*n*é*s*ǭ"])
            check("PNWGmcILowering", prefix + "*n*í*s*ų", [prefix + "*n*í*s*ų"])
            check("PNWGmcULowering", prefix + "*w*ú*n*d*ǭ", [prefix + "*w*ú*n*d*ǭ"])
            check("PNWGmcULowering", prefix + "*w*ú*l*j*ǭ", [prefix + "*w*ú*l*j*ǭ"])
        for ending, output in (("ō", "u"), ("ǭ", "ǭ"), ("ô", "ô")):
            check("PNWGmcFinalLongORaising", "*w*ó*l*l*" + ending,
                  ["*w*ó*l*l*" + output])
        check("PNWGmcStressedMonosyllableORaising", "*d*ō", ["*d*ū"])
        forms = [oe_pipeline.evaluation_input(row) for row in rows]
        states = [[form] for form in forms]
        compared = 0
        for position, item in enumerate(stage_map):
            states = assay.batch_apply_down(
                bins[f"diagnostic:{position}"], [output[0] for output in states],
            )
            for row, prior, actual in zip(rows, old, states):
                expected = prior["intermediates"][item["probe"]]["baseline"]
                if actual != expected or len(actual) != 1:
                    raise RuntimeError(f"{row['id']}/{item['expression']}: {actual} != {expected}")
                compared += 1
        full = assay.batch_apply_down(bins["final"], forms)
        if states != full or full != [row["baseline_outputs"] for row in old]:
            raise RuntimeError("Full wrapper, stage replay and frozen finals disagree")
        cells = ["wúllō", "wúllǭ", "wullō", "wullǭ"]
        cell_outputs = assay.batch_apply_down(bins["final"], cells)
        if cell_outputs != [["woll"], ["wolle"], ["woll"], ["wolle"]]:
            raise RuntimeError(f"Declared wool nominative/accusative outcomes failed: {cell_outputs}")
        you = next(i for i, row in enumerate(rows) if row["id"] == "2326")
        if not forms[you].startswith("ᵘ"):
            raise RuntimeError("Row 2326 lost its selected prosodic context")
    if before != {str(path): assay.digest(path) for path in protected}:
        raise RuntimeError("Isolated assay modified canonical artifacts")
    mismatches = [row["id"] for row, output in zip(rows, full)
                  if output != [row["counterpart"]]]
    if mismatches != baseline["baseline_mismatch_ids"]:
        raise RuntimeError(f"Mismatch membership changed: {mismatches}")
    return {
        "fst_sha256": assay.digest(runtime.germanic_fst),
        "corpus_sha256": assay.digest(runtime.corpus_tsv),
        "selected_rows": len(rows), "checkpoint_count": len(stage_map),
        "identical_row_checkpoints": compared, "changed_derivation_ids": [],
        "changed_final_ids": [], "mismatch_ids": mismatches,
        "rejected_ids": [], "ambiguous_ids": [], "component_checks": checks,
        "wool_raw_cells": dict(zip(cells, cell_outputs)),
        "you_context_input": forms[you], "you_output": full[you],
        "class_consumers": consumer_audit(runtime.germanic_fst.read_text()),
        "canonical_artifacts_unchanged": True,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--preservation-root", type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError(f"Refusing to replace an existing receipt: {args.output}")
    report = (preservation_report(args.preservation_root)
              if args.preservation_root else verify())
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({key: value for key, value in report.items()
                      if key not in ("class_consumers", "component_checks", "files")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
