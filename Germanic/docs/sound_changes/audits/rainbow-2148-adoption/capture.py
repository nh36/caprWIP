#!/usr/bin/env python3
"""Fresh canonical adoption observations; frozen research is never rewritten."""
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
from capr_runtime import check_build_manifest, layout  # noqa: E402
from anglo_frisian_experiments import compile_isolated  # noqa: E402
from executable_facts import parse_defines  # noqa: E402
from oe_pipeline import evaluation_input, load_rows, named_stages  # noqa: E402
from sound_change_order_sensitivity import batch_apply_down  # noqa: E402

BASE = "1bfdd0794b65d8a6abad698a651ca426a1061c29"
BEFORE_SOURCE_SHA256 = "3725fca7dc8e377657a9d2987d1ced9d88c1e55d8aa180b7a8e56a36e327dd27"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def capture():
    rt = layout()
    if not rt.is_container:
        raise RuntimeError("Run inside the backend container.")
    stages = named_stages()
    errors = check_build_manifest(
        [stage.snapshot_bin for stage in stages] + ["old_english.bin"], rt)
    if errors:
        raise RuntimeError("; ".join(errors))
    rows = load_rows(rt.corpus_tsv)
    legacy_path = rt.docs_dir / (
        "sound_changes/cascade_baseline/cascade_baseline_outputs_legacy380.tsv")
    with legacy_path.open() as handle:
        legacy = list(csv.DictReader(handle, delimiter="\t"))
    inputs = [evaluation_input(row) for row in rows + legacy]
    split = len(rows)
    states = [[form] for form in inputs]
    transitions = []
    for stage in stages:
        after = batch_apply_down(rt.bin_dir / stage.snapshot_bin, inputs)
        if any(len(outputs) > 1 for outputs in after):
            raise RuntimeError(f"ambiguous forward output at {stage.foma_identifier}")
        transitions.append({
            "stage": stage.foma_identifier, "exec_index": stage.exec_index,
            "changes": [
                {"row_id": row["row_id"], "concept": row["concept"],
                 "before": old, "after": new}
                for row, old, new in zip(rows, states[:split], after[:split])
                if old != new],
            "selected_states": after[:split],
            "immutable380_states": after[split:],
        })
        states = after
    final = batch_apply_down(rt.bin_dir / "old_english.bin", inputs)
    if final != states:
        raise RuntimeError("last snapshot differs from the production wrapper")
    return {
        "base_commit": BASE,
        "source_sha256": digest(rt.germanic_fst),
        "corpus_sha256": digest(rt.corpus_tsv),
        "context_sha256": digest(rt.data_dir / "entry_context_metadata.tsv"),
        "immutable380_sha256": digest(legacy_path),
        "definitions": {
            name: fact.body for name, fact in
            parse_defines(rt.germanic_fst.read_text()).items()},
        "rows": rows, "immutable380_rows": legacy,
        "selected_inputs": inputs[:split],
        "immutable380_inputs": inputs[split:],
        "transitions": transitions,
        "selected_final": final[:split],
        "immutable380_final": final[split:],
        "mismatch_ids": [
            row["row_id"] for row, outputs in zip(rows, final)
            if outputs != [row["counterpart"]]],
    }


def compare(before, after):
    for key in ("rows", "immutable380_rows", "selected_inputs",
                "immutable380_inputs", "corpus_sha256", "context_sha256",
                "immutable380_sha256", "selected_final", "immutable380_final",
                "mismatch_ids"):
        if before[key] != after[key]:
            raise RuntimeError(f"unauthorized adoption difference: {key}")
    old, new = before["definitions"], after["definitions"]
    if old.keys() != new.keys():
        raise RuntimeError("adoption added or removed an executable identity")
    changed = [name for name in old if old[name] != new[name]]
    if changed != ["PNWGmcULowering"]:
        raise RuntimeError(f"unexpected definition changes: {changed}")
    if len(before["transitions"]) != len(after["transitions"]):
        raise RuntimeError("sound-change stage count changed")
    deltas = []
    for old_step, new_step in zip(before["transitions"], after["transitions"]):
        if old_step["stage"] != new_step["stage"]:
            raise RuntimeError("sound-change order changed")
        for row, old_outputs, new_outputs in zip(
                after["rows"], old_step["selected_states"],
                new_step["selected_states"]):
            if old_outputs != new_outputs:
                deltas.append({"row_id": row["row_id"],
                               "stage": new_step["stage"],
                               "before_adoption": old_outputs,
                               "after_adoption": new_outputs})
    if {row["row_id"] for row in deltas} != {"2148"}:
        raise RuntimeError("intermediate changes are not confined to rainbow")
    after["comparison"] = {
        "changed_definitions": changed,
        "selected_final_changes": [],
        "immutable380_final_changes": [],
        "selected_stage_differences": deltas,
        "order_unchanged": True,
    }


def controls(before):
    rt = layout()
    if not rt.is_container:
        raise RuntimeError("Run Foma controls inside the backend container.")
    grave = """Ctx([
        {*ù} -> {*ò} || _
        [EnglishStarConsonantNoJ - EnglishStarNasal]
        EnglishStarConsonantNoJ* EnglishStarNonHighVowel
    ])"""
    compound = grave.replace(
        "|| _", "|| .#. EnglishStarConsonant* PGmcStarAcuteVowel "
        "[EnglishStarVocalic|EnglishStarConsonant]* _")
    definitions = (
        "define RBase " + before["definitions"]["PNWGmcULowering"] + ";\n"
        "define RSubordinate " + grave + ";\n"
        "define RCompoundOnly " + compound + ";\n"
        "define RCompound [RBase .o. RCompoundOnly];\n"
        "define RDomain [ContextSegments|{*ᶠ}|{*ᵘ}|{*ᶜ}]*;\n"
        "define RFunctional [RDomain .o. PNWGmcULowering];\n")
    names = ("PNWGmcULowering", "RCompound", "RFunctional",
             "EnglishProtoInput", "OECompoundLinkingSyncope",
             "OEStripSecondaryStress")
    recipe = dict(
        definitions=definitions, insert_after="", insert_rule="", replace={},
        component_checks=[dict(component=name) for name in names])
    probes = {
        "subordinate-root": "régnabùgô",
        "independent-bow": "búgô",
        "high-trigger": "bùgi",
        "nasal-first": "bùnô",
        "intervening-j": "bùgja",
        "plain-weak-medial": "régnabugô",
        "grave-without-primary-synthetic": "bùgô",
        "later-nasal-literal-guard": "sátùgna",
    }
    inputs = ["".join("*" + letter for letter in value)
              for value in probes.values()]
    source_hash = digest(rt.germanic_fst)
    with tempfile.TemporaryDirectory(prefix="capr_rainbow_adopt_") as temporary:
        bins = compile_isolated(
            rt.germanic_fst, recipe, [], Path(temporary), components_only=True)
        outputs = {
            name: dict(zip(probes, batch_apply_down(
                bins["component:" + name], inputs)))
            for name in ("PNWGmcULowering", "RCompound")}
        pre = next(step for step in before["transitions"]
                   if step["exec_index"] == 19)["selected_states"]
        forms = [state[0] for state in pre]
        early = {name: batch_apply_down(bins["component:" + name], forms)
                 for name in ("PNWGmcULowering", "RCompound")}
        if early["PNWGmcULowering"] != early["RCompound"]:
            raise RuntimeError("general/compound clauses differ on selected rows")
        linked = batch_apply_down(
            bins["component:OECompoundLinkingSyncope"],
            [outputs["PNWGmcULowering"]["subordinate-root"][0]])
        stripped = batch_apply_down(bins["component:OEStripSecondaryStress"], linked[0])
        functional = subprocess.run(
            ["foma", "-q", "-e",
             "load stack " + str(bins["component:RFunctional"]),
             "-e", "test functional", "-e", "quit"],
            capture_output=True, text=True, timeout=120, check=True)
        answer = re.findall(r"(?m)^([01]) \(1 = TRUE, 0 = FALSE\)$",
                            functional.stdout)
        if answer != ["1"]:
            raise RuntimeError("adopted early operation is not forward-functional")
        parser = batch_apply_down(
            bins["component:EnglishProtoInput"],
            ["biu", "régna-bùgô", "búgô", "régna-bùgōzz"])
    if source_hash != digest(rt.germanic_fst):
        raise RuntimeError("source changed during private control compilation")
    return {
        "source_sha256": source_hash,
        "definitions": definitions,
        "inputs": dict(zip(probes, inputs)),
        "outputs": outputs,
        "selected_general_compound_equivalent": True,
        "selected_early_states": early["PNWGmcULowering"],
        "linked": linked, "stripped": stripped,
        "forward_functional": True,
        "functional_stdout": functional.stdout,
        "parser": dict(zip(
            ["known-biu-ambiguity", "rainbow", "bow", "invalid-ending"], parser)),
        "scope": "Synthetic controls are not corpus admissions or attestations.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--before", type=Path)
    parser.add_argument("--controls", action="store_true")
    args = parser.parse_args()
    before = None
    if args.before:
        with gzip.open(args.before, "rt") as handle:
            before = json.load(handle)
    if args.controls:
        if before is None:
            parser.error("--controls requires --before")
        report = controls(before)
    else:
        report = capture()
        if before:
            compare(before, report)
        elif report["source_sha256"] != BEFORE_SOURCE_SHA256:
            parser.error("pre-adoption capture requires the recorded baseline "
                         "source; use --before to compare the adopted model")
    with args.output.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0) as compressed:
            compressed.write(json.dumps(
                report, ensure_ascii=False, sort_keys=True,
                separators=(",", ":")).encode())
    print(json.dumps({
        "forward_functional": report["forward_functional"],
        "selected_general_compound_equivalent":
            report["selected_general_compound_equivalent"],
    } if args.controls else {
        "selected_rows": len(report["rows"]),
        "stages": len(report["transitions"]),
        "mismatch_ids": report["mismatch_ids"],
        "firings": {step["stage"]: len(step["changes"])
                    for step in report["transitions"] if step["stage"] in
                    ("PNWGmcULowering", "OEMedUnstressedULowering")},
        "compared": bool(args.before),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
