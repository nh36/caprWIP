#!/usr/bin/env python3
"""Bounded symbol correction and legacy-comparator replay after factorial 01."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

import experiment as current

HERE, ROOT, GERMANIC = current.HERE, current.ROOT, current.GERMANIC


def worker(output):
    import oe_pipeline
    from anglo_frisian_experiments import compile_isolated, prepare_definition_image
    from sound_change_order_sensitivity import batch_apply_down

    if not Path("/.dockerenv").exists() or GERMANIC == Path("/usr/app"):
        raise RuntimeError("Requires container-private frozen sources")
    report = json.loads(gzip.decompress((HERE / "results.json.gz").read_bytes()))
    for path in ("fsts/germanic.txt", "data/germanic-aligned-final.tsv"):
        if current.sha(GERMANIC / path) != current.sha(Path("/usr/app") / path):
            raise RuntimeError("Scientific baseline drift")
    definitions = current.prior.DEFINITIONS + current.EXTRA
    if not report["definitions"].startswith(definitions + "\n"):
        raise RuntimeError("Factorial definition reuse is not exact")
    controls = dict(report["controls"])
    controls["lord-high-closed"] = ("drixtin", "drixtin")
    controls["beg-cluster-limit"] = ("bedekian", "bedekian")
    probes = {"kettle": "*kátilaz", "angel": "*ángilaz",
              "health": "*xáiliθō", "theft": "*θéubiθō", "warmth": "*wármiθō"}
    sequence = report["models"]["C-nonhigh"]["order"]
    definitions += "\ndefine TReview [" + " .o. ".join(sequence) + "];\n"
    rules = ["SNonHighSyn", "SFulkSyn", "SFulkApo", "TNonHigh"]
    recipe = dict(definitions=definitions, insert_after="", insert_rule="", replace={},
                  component_checks=[dict(component=name) for name in rules + ["TReview"]])
    with tempfile.TemporaryDirectory(prefix="capr_syncope_control_") as temporary:
        directory = Path(temporary)
        image = prepare_definition_image(GERMANIC / "fsts/germanic.txt", directory)
        if image:
            os.environ["CAPR_FOMA_DEFINITION_IMAGE"] = str(image)
        bins = compile_isolated(GERMANIC / "fsts/germanic.txt", recipe, [], directory,
                                components_only=True)
        component = {rule: dict(zip(controls, batch_apply_down(
            bins["component:" + rule], [current.prior.star(v[0]) for v in controls.values()])))
            for rule in rules}
        inputs = [oe_pipeline.evaluation_input(
            {"proto_norm": oe_pipeline.normalize_proto(raw)}) for raw in probes.values()]
        production = batch_apply_down(Path("/usr/app/old_english.bin"), inputs)
        candidate = batch_apply_down(bins["component:TReview"], inputs)
    result = dict(
        correction="h is orthographic; pre-orthographic drixtin uses the admitted x symbol",
        prior_invalid_control=report["component"]["SFulkSyn"]["lord-high-closed"],
        definitions_equal_to_factorial=True, reused_report_sha256=current.sha(HERE / "results.json.gz"),
        controls=controls, component=component,
        probes={key: dict(input=raw, production=a, C=b)
                for (key, raw), a, b in zip(probes.items(), production, candidate)},
        limits="bedekian lies outside the three-syllable fragment; its retention does not prove a cluster filter",
        base=current.BASE)
    with gzip.open(output, "wt", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, sort_keys=True)


def launch(experiment_id):
    import adjudication_control
    import adjudication_run
    from experiment_snapshot import create_snapshot

    previous = ROOT / ".capr-work/experiments/soul-syncope-resolution-01"
    receipt = json.loads((previous / "receipt.json").read_text())
    mapping = json.loads((previous / "snapshot/layout.json").read_text())
    inputs = {}
    for label, entry in receipt["inputs"].items():
        if label == "layout":
            continue
        path = ROOT / mapping[label]
        if current.sha(path) != entry["sha256"]:
            raise RuntimeError("Original compiler input changed: " + mapping[label])
        inputs[label] = path
    for label, path in (("followup", Path(__file__)), ("report01", HERE / "results.json.gz")):
        inputs[label] = path
        mapping[label] = str(path.relative_to(ROOT))
    layout = ROOT / ".capr-work/control-layout.json"
    layout.write_text(json.dumps(mapping))
    inputs["layout"] = layout
    run = adjudication_run.start("SC066")
    adjudication_run.set_scientific_reference(
        run, current.BASE, "Same approved source; bounded comparator and symbol follow-up")
    run.complete_stage("INSPECT", note="Current SC066 evidence, kettle/angel residue and factorial inspected")
    preflight = adjudication_control.preflight("SC066")
    if preflight.blocked:
        raise RuntimeError(preflight.render())
    run.complete_stage("PREFLIGHT", evidence=preflight.to_json())
    snapshot = create_snapshot(
        experiment_id, "Correct pre-orthographic h/x control and replay existing comparators",
        inputs, probes=["drixtin", "bedekian", "kettle", "angel", "health", "theft", "warmth"],
        expected_outcomes={"no_rule_change": "Exact factorial kernels and C serialization",
                           "angel": "Document inherited SC066 residue, never repair it here"},
        environment={"runner": "private capr-soul-syncope backend", "base": current.BASE})
    run.complete_stage("SNAPSHOT", evidence={"snapshot_root": str(snapshot.root)})
    container = snapshot.stage_in_container()
    bootstrap = """
import json,shutil,sys,tempfile,subprocess
from pathlib import Path
src=Path(sys.argv[1]); layout=json.loads((src/'layout.json').read_text())
root=Path(tempfile.mkdtemp(prefix='capr_syncope_control_source_'))
for label,relative in layout.items():
    files=list(src.glob(label+'.*'))
    if len(files)!=1: raise RuntimeError(label)
    dest=root/relative; dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(files[0],dest)
for name in ('compare_fst.py','oe_input_context.py'):
    shutil.copyfile(root/'backend'/name,root/'Germanic'/name)
worker=root/'Germanic/docs/sound_changes/audits/soul-syncope-resolution/control_assay.py'
subprocess.run(['python3',str(worker),'--worker','--output',sys.argv[2]],check=True)
"""
    destination = container + "/../" + experiment_id + "-results.json.gz"
    executed = adjudication_control.run_logged(
        ["docker", "compose", "exec", "-T", "backend", "python3", "-c",
         bootstrap, container, destination], label="syncope-controls", log_dir=snapshot.staging_dir)
    if executed["ok"]:
        subprocess.run(["docker", "compose", "cp", "backend:" + destination,
                        str(snapshot.staging_dir / "results.json.gz")], check=True)
    snapshot.complete("passed" if executed["ok"] else "failed",
                      "Bounded control execution, not a production adjudication",
                      command_receipts=[executed])
    (snapshot.root / "staging").symlink_to("results", target_is_directory=True)
    print(snapshot.root)
    if not executed["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--experiment-id")
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.worker:
        worker(args.output)
    elif args.experiment_id:
        launch(args.experiment_id)
    else:
        parser.error("--experiment-id or --worker is required")
