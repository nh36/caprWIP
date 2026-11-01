#!/usr/bin/env python3
"""Snapshot-pinned lexical research; writes only private experimental evidence."""
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = "8f7713c39f26a7f81ef04d29d54070f1b83ab0e0"
RESEARCH = "Germanic/docs/sound_changes/audits/earthly-regular-cell"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_json(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def definitions(previous):
    parser = "define RCellTail" + previous.EARLY_DEFINITIONS.split(
        "define RCellTail", 1)[1]
    parser = parser.replace(
        "define RCellTail [",
        "define RCellTail [\n    {ai}:{*ai} m:{*m} i:{*i} z:{*z} |")
    final = []
    for plain, grave in zip("aeiou", "àèìòù"):
        final.append(
            f"{{*{plain}}} -> {{*{grave}}} || "
            ".#. RPrefix RFirst RRest* {ᵇ} RC* _ RC RC+ .#.")
    return parser + previous.foot_definitions() + """
define RLastAccent [RAccent .o. [""" + ", ".join(final) + """]];
define RLastFoot SentenceCtx([RSyll .o. RLastAccent .o. RUnsyll]);
define RLastLate [RLastFoot .o. OEMedUnstressedULowering .o. RDecode];
define RRSync FootCtx([
    [{*e}|{*æ}] -> 0 ||
        [RShort & [PGmcStarAcuteVowel|PGmcStarGraveVowel]]
        RC RC+ _ {*r} RV
]);
define RRSlice [RFoot .o. RRSync .o. RDecode];
"""


def plan(previous, oe_pipeline, root):
    original = [
        s.foma_identifier if s.kind == "named" else s.inline_text
        for s in oe_pipeline.stages()]

    def replace(sequence, old, new):
        result = list(sequence)
        assert result.count(old) == 1
        result[result.index(old)] = new
        return result

    gate = replace(original, "EnglishProtoInput", "RInput")
    earlier = replace(gate, previous.LATE, "RLate")
    final = replace(gate, previous.LATE, "RLastLate")

    def syncope(sequence):
        result = list(sequence)
        result.insert(result.index("OEUnstressedLongVowelShortening") + 1, "RRSlice")
        return result

    models = {
        "identity": original,
        "parser-only": gate,
        "earlier-prominence": earlier,
        "single-onset-sensitivity": replace(gate, previous.LATE, "RLateOne"),
        "final-overheavy-sensitivity": final,
        "r-syncope-slice": syncope(earlier),
        "combined-sensitivity": syncope(final),
    }
    candidates = dict(previous.CANDIDATES)
    candidates.update({
        "earthly-feminine-genitive-iz": "*érθa-kùnðizōz",
        "earthly-weak-neuter-ending-o-diagnostic": "*érθa-kùnðō",
        "earthly-weak-neuter-ending-on-diagnostic": "*érθa-kùnðōn",
        "godcund-feminine-genitive": "*gúða-kùnðaizōz",
        "godcund-feminine-genitive-iz": "*gúða-kùnðizōz",
        "earthly-strong-dative-plural": "*érθa-kùnðaimiz",
        "godcund-strong-dative-plural": "*gúða-kùnðaimiz",
        "earthly-strong-neuter-accusative-nasal": "*érθa-kùnðą",
        "earthly-strong-masculine-accusative-nasal": "*érθa-kùnðanǭ",
        "godcund-strong-masculine-accusative-nasal": "*gúða-kùnðanǭ",
        "earthly-weak-neuter-unaugmented-nasal": "*érθa-kùnðǭ",
        "godcund-weak-neuter-unaugmented-nasal": "*gúða-kùnðǭ",
        "earthly-unsupported-trimoric-nasal-trial": "*érθa-kùnðôⁿ",
    })
    rows = oe_pipeline.load_rows(root / "Germanic/data/germanic-aligned-final.tsv")
    baseline = root / "Germanic/docs/sound_changes/cascade_baseline"
    with (baseline / "cascade_baseline_outputs_legacy380.tsv").open() as handle:
        immutable = list(csv.DictReader(handle, delimiter="\t"))
    components = dict(previous.COMPONENTS)
    components.update({
        "late-godcund-uninflected": previous.star("gódkund"),
        "late-godcund-accusative": previous.star("gódkundne"),
        "late-godcund-feminine-genitive": previous.star("gódkundre"),
        "late-eorpthcundre": previous.star("éorθkundre"),
        "late-final-overheavy-LH-synthetic": previous.star("kúning"),
        "syncope-headed-heavy-r": previous.star("gódkundere"),
        "syncope-light-r-negative": previous.star("góbere"),
        "syncope-no-following-vowel-negative": previous.star("gódkunder"),
        "syncope-long-vowel-negative": previous.star("gódkundēre"),
    })
    text = definitions(previous)
    whole = {}
    for index, name in enumerate((
            "identity", "earlier-prominence", "final-overheavy-sensitivity",
            "combined-sensitivity")):
        ident = f"RWhole{index}"
        whole[name] = ident
        text += "\ndefine " + ident + " " + " .o. ".join(models[name]) + ";\n"
    checked = sorted({
        stage for sequence in models.values() for stage in sequence
    } | set(whole.values()) | {
        "RFoot", "RFootOne", "RSyll", "RLastFoot", "RLastLate",
        "RRSlice", "RRSync", "RDecode"})
    return {
        "base_commit": BASE, "models": models, "whole": whole,
        "candidates": candidates, "components": components, "rows": rows,
        "immutable380": immutable,
        "corpus_inputs": [oe_pipeline.evaluation_input(row) for row in rows],
        "immutable_inputs": [oe_pipeline.evaluation_input(row) for row in immutable],
        "candidate_inputs": [
            oe_pipeline.evaluation_input({"proto_norm": oe_pipeline.normalize_proto(raw)})
            for raw in candidates.values()],
        "recipe": {
            "definitions": text, "insert_after": "", "insert_rule": "", "replace": {},
            "component_checks": [{"component": name} for name in checked]},
    }


def container_run(snapshot, build, output):
    sys.path.insert(0, "/usr/app/tools")
    from sound_change_order_sensitivity import batch_apply_down
    receipt = json.loads((snapshot / "snapshot_receipt.json").read_text())
    for entry in receipt["inputs"].values():
        assert digest(snapshot / entry["snapshot_name"]) == entry["sha256"]
    for label, entry in receipt["inputs"].items():
        if label.startswith("tool_"):
            assert digest(Path("/usr/app/tools") / Path(entry["original_path"]).name) == entry["sha256"]
    assert digest("/usr/app/oe_input_context.py") == receipt["inputs"]["input_context"]["sha256"]
    previous_path = snapshot / "library/Germanic/docs/sound_changes/audits/previous/experiment.py"
    previous_path.parent.mkdir(parents=True)
    shutil.copy2(snapshot / receipt["inputs"]["previous"]["snapshot_name"], previous_path)
    assert digest(previous_path) == receipt["inputs"]["previous"]["sha256"]
    previous = load_module(previous_path, "earlier")
    from capr_runtime import RuntimeLayout
    canonical = RuntimeLayout(Path("/usr/app"), Path("/usr/app"), Path("/usr/app"), True)
    protected_before = previous.protected_files(canonical)
    data = json.loads((snapshot / receipt["inputs"]["plan"]["snapshot_name"]).read_text())
    bins = {key: Path(value) for key, value in build["bins"].items()}
    corpus = data["corpus_inputs"]
    immutable = data["immutable_inputs"]
    initial = corpus + immutable + data["candidate_inputs"]
    offset = len(corpus) + len(immutable)
    results = {}
    for name, order in data["models"].items():
        print("Tracing", name, flush=True)
        final, traces = previous.trace_model(order, bins, initial)
        if name in data["whole"]:
            assert batch_apply_down(bins["component:" + data["whole"][name]], initial) == final
        reference = final if name == "identity" else results["identity"]["final"]
        candidates = {}
        for number, (label, raw) in enumerate(data["candidates"].items(), offset):
            candidates[label] = {
                "input": raw, "evaluator_input": initial[number],
                "parser_accepted": bool(traces[0]["after"][number]),
                "final": final[number],
                "steps": [{
                    "step": step["step"], "stage": step["stage"],
                    "before": step["before"][number], "after": step["after"][number]}
                    for step in traces],
            }
        aligned = {
            "RInput": "EnglishProtoInput", "RLate": previous.LATE,
            "RLateOne": previous.LATE, "RLastLate": previous.LATE,
        }
        reference_steps = traces if name == "identity" else results["identity"]["traces"]
        by_stage = {step["stage"]: step for step in reference_steps}
        delta = [{
            "step": step["step"], "stage": step["stage"],
            "rows": [row["row_id"] for index, row in enumerate(data["rows"])
                     if step["after"][index] != by_stage[aligned.get(
                         step["stage"], step["stage"])]["after"][index]],
            "immutable_indices": [
                index for index in range(len(immutable))
                if step["after"][len(corpus) + index] != by_stage[aligned.get(
                    step["stage"], step["stage"])]["after"][len(corpus) + index]],
        } for step in traces if aligned.get(step["stage"], step["stage"]) in by_stage]
        results[name] = {
            "order": order, "final": final, "traces": traces,
            "candidates": candidates, "counts": previous.counts(data["rows"], final[:len(corpus)]),
            "composed_crosscheck": name in data["whole"],
            "selected_final_delta_ids": [
                row["row_id"] for row, old, new in zip(data["rows"], reference, final)
                if old != new],
            "immutable_final_delta_indices": [
                index for index in range(len(immutable))
                if reference[len(corpus) + index] != final[len(corpus) + index]],
            "aligned_intermediate_deltas": delta,
        }
        internal = []
        expanded = {
            "RLate": ("RFoot", previous.LATE, "RDecode"),
            "RLateOne": ("RFootOne", previous.LATE, "RDecode"),
            "RLastLate": ("RLastFoot", previous.LATE, "RDecode"),
            "RRSlice": ("RFoot", "RRSync", "RDecode"),
        }
        for step in traces:
            if step["stage"] not in expanded:
                continue
            states = step["before"]
            operations = []
            for component in expanded[step["stage"]]:
                after = previous.apply_sets(bins["component:" + component], states)
                assert all(len(value) <= 1 for value in after)
                operations.append({"component": component, "before": states, "after": after})
                states = after
            assert states == step["after"]
            internal.append({"stage": step["stage"], "operations": operations})
        results[name]["internal_operations"] = internal
    with (snapshot / receipt["inputs"]["active_baseline"]["snapshot_name"]).open() as handle:
        accepted = list(csv.DictReader(handle, delimiter="\t"))
    reference_by_id = {
        row["row_id"]: value for row, value in zip(
            data["rows"], results["identity"]["final"][:len(corpus)])}
    assert len(accepted) == len(corpus) == 390
    assert results["identity"]["counts"]["matched"] == 382
    assert all(reference_by_id[row["row_id"]] == row["outputs"].split("|")
               for row in accepted)
    from cascade_baseline import legacy_subset, projection_sha256
    with (snapshot / receipt["inputs"]["migrations"]["snapshot_name"]).open() as handle:
        migrations = list(csv.DictReader(handle, delimiter="\t"))
    active = legacy_subset(accepted, data["immutable380"], migrations)
    summary = json.loads((snapshot / receipt["inputs"]["summary"]["snapshot_name"]).read_text())
    populations = {
        "selected390_evaluator_sha256": projection_sha256(accepted, "fst_input"),
        "selected390_lexical_sha256": projection_sha256(accepted, "proto_norm"),
        "active380_count": len(active),
        "active380_sha256": hashlib.sha256("".join(
            row["proto_norm"] + "\x1f" + row["outputs"] + "\x1e" for row in active).encode()).hexdigest(),
        "immutable380_count": len(immutable),
        "immutable380_rejected": sum(not value for value in results["identity"]["final"][len(corpus):offset]),
        "immutable380_ambiguous": sum(len(value) > 1 for value in results["identity"]["final"][len(corpus):offset]),
    }
    assert populations["selected390_evaluator_sha256"] == summary["outputs_sha256"]
    assert populations["active380_sha256"] == summary["legacy_subset_sha256"]
    checks = {}
    for name in (
            previous.LATE, "RFoot", "RFootOne", "RLastFoot", "RLate",
            "RLateOne", "RLastLate", "RRSync", "RRSlice"):
        checks[name] = dict(zip(data["components"], batch_apply_down(
            bins["component:" + name], list(data["components"].values()))))
        assert all(len(value) == 1 for value in checks[name].values())
    formal = {}
    for name in ("RFoot", "RLate", "RLastFoot", "RLastLate", "RRSlice"):
        binary = bins["component:" + name]
        command = ["foma", "-q", "-e", "load stack " + str(binary),
                   "-e", "test functional", "-e", "quit"]
        run = subprocess.run(command, capture_output=True, text=True, check=True, timeout=120)
        formal[name] = {"argv": command, "stdout": run.stdout, "stderr": run.stderr}
    result = {
        "base_commit": BASE, "snapshot": receipt, "plan": data,
        "models": results, "component_results": checks, "formal": formal,
        "population_checks": populations,
        "foma": subprocess.check_output(["foma", "-v"], text=True).strip(),
        "flookup": subprocess.check_output(["flookup", "-v"], text=True).strip(),
        "canonical_before": protected_before,
        "canonical_after": previous.protected_files(canonical),
    }
    assert result["canonical_before"] == result["canonical_after"]
    for entry in receipt["inputs"].values():
        assert digest(snapshot / entry["snapshot_name"]) == entry["sha256"]
    with output.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0) as compressed:
            compressed.write(json.dumps(result, ensure_ascii=False, separators=(",", ":")).encode())


def host_run(identifier, compiled_snapshot=None):
    ROOT = HERE.parents[4]
    sys.path.insert(0, str(ROOT / "Germanic/tools"))
    import adjudication_control as control
    import experiment_snapshot
    import oe_pipeline
    subprocess.run(
        ["git", "diff", "--exit-code", BASE, "--", ".", f":(exclude){RESEARCH}"],
        cwd=ROOT, stdout=subprocess.DEVNULL, check=True)
    os.environ["COMPOSE_PROJECT_NAME"] = "capr"
    before = {
        path: digest(ROOT / path) for path in subprocess.check_output(
            ["git", "ls-tree", "-r", "--name-only", BASE], cwd=ROOT, text=True).splitlines()
        if (ROOT / path).is_file()}
    previous_path = HERE.parent / "rainbow-earthly-secondary-stress/experiment.py"
    previous = load_module(previous_path, "earlier")
    data = plan(previous, oe_pipeline, ROOT)
    scratch = ROOT / ".capr-work/earthly-assay-inputs"
    scratch.mkdir(parents=True, exist_ok=True)
    write_json(scratch / "plan.json", data)
    write_json(scratch / "recipe.json", data["recipe"])
    baseline = ROOT / "Germanic/docs/sound_changes/cascade_baseline"
    inputs = {
        "source": ROOT / "Germanic/fsts/germanic.txt",
        "corpus": ROOT / "Germanic/data/germanic-aligned-final.tsv",
        "context": ROOT / "Germanic/data/entry_context_metadata.tsv",
        "input_context": ROOT / "backend/oe_input_context.py",
        "immutable": baseline / "cascade_baseline_outputs_legacy380.tsv",
        "active_baseline": baseline / "cascade_baseline_outputs.tsv",
        "migrations": baseline / "approved_input_migrations.tsv",
        "summary": baseline / "cascade_baseline_summary.json",
        "previous": previous_path, "worker": Path(__file__).resolve(),
        "plan": scratch / "plan.json", "recipe": scratch / "recipe.json",
    }
    for name in (
            "oe_pipeline", "capr_runtime", "anglo_frisian_experiments",
            "sound_change_order_sensitivity", "executable_facts", "cascade_baseline"):
        inputs["tool_" + name] = ROOT / "Germanic/tools" / (name + ".py")
    environment = {
        "compose_project": "capr", "container": "capr-backend-1",
        "image_id": subprocess.check_output(
            ["docker", "inspect", "-f", "{{.Image}}", "capr-backend-1"], text=True).strip(),
        "runtime_lock_holder_before": control.runtime_lock_holder(),
        "shared_runtime_written": False,
    }
    runtime_command = [
        "docker", "compose", "exec", "-T", "backend", "python3", "-c",
        "import pathlib,hashlib,json; r=pathlib.Path('/usr/app'); "
        "p=[*r.glob('*.bin'),r/'oe_build_manifest.json']; "
        "print(json.dumps({x.name:hashlib.sha256(x.read_bytes()).hexdigest() for x in p}))"]
    runtime_before = json.loads(subprocess.check_output(runtime_command, cwd=ROOT, text=True))
    environment["runtime_bins_before"] = runtime_before
    snapshot = experiment_snapshot.create_snapshot(
        identifier, "One regular earthly grammatical cell; no production adoption",
        inputs, variants={name: "\n".join(order) for name, order in data["models"].items()},
        probes=["every physical stage, selected390 + original immutable380 + full cells"],
        negative_controls=list(data["components"]),
        expected_outcomes={"selected_count": 390, "matched": 382, "immutable_count": 380},
        environment=environment)
    logs = snapshot.root / "logs"
    preflights = []
    for sc in ("SC065", "SC066", "SC068"):
        receipt = control.run_logged(
            [sys.executable, "Germanic/tools/adjudicate.py", sc, "--preflight",
             "--for", "investigate", "--json"], cwd=ROOT, label=sc + "-preflight", log_dir=logs)
        control.verify_receipt(receipt, current=False)
        preflights.append(receipt)
    if compiled_snapshot:
        origin = experiment_snapshot.Snapshot(compiled_snapshot.resolve())
        origin.verify()
        old = origin.receipt()["inputs"]
        new = snapshot.receipt()["inputs"]
        assert set(old) == set(new)
        assert all(old[label]["sha256"] == new[label]["sha256"]
                   for label in old if label not in {"worker", "plan"})
        assert origin.receipt()["environment"]["image_id"] == environment["image_id"]
        build = json.loads((origin.results_dir / "build.json").read_text())
        control.verify_receipt(build["receipt"], current=False)
        private = snapshot.stage_in_container()
        build = {**build, "container_source": private,
                 "compile_origin_snapshot": str(origin.root)}
    else:
        build = snapshot.compile_isolated("source", "recipe", components_only=True)
    for stream in ("stdout", "stderr"):
        shutil.copy2(build["receipt"][stream + "_log"], logs)
    shutil.copy2(build["receipt"]["receipt_path"], logs)
    private = build["container_source"]
    write_json(snapshot.staging_dir / "snapshot_receipt.json", snapshot.receipt())
    write_json(snapshot.staging_dir / "build.json", build)
    for filename in ("snapshot_receipt.json", "build.json"):
        subprocess.run(["docker", "compose", "cp", str(snapshot.staging_dir / filename),
                        "backend:" + private + "/" + filename], cwd=ROOT, check=True)
    worker = snapshot.input_path("worker").name
    run = control.run_logged(
        ["docker", "compose", "exec", "-T", "backend", "python3", private + "/" + worker,
         "--container", private, private + "/build.json", private + "/results.json.gz"],
        cwd=ROOT, label="earthly-full-assay", log_dir=logs, timeout=1200)
    control.verify_receipt(run, current=False, allow_source_change=True)
    subprocess.run(["docker", "compose", "cp", "backend:" + private + "/results.json.gz",
                    str(snapshot.staging_dir / "results.json.gz")], cwd=ROOT, check=True)
    after = {path: digest(ROOT / path) for path in before}
    assert before == after, "A tracked production file changed during lexical research"
    runtime_after = json.loads(subprocess.check_output(runtime_command, cwd=ROOT, text=True))
    assert runtime_before == runtime_after, "Canonical runtime changed during lexical research"
    write_json(snapshot.staging_dir / "protection.json", {
        "before": before, "after": after, "production_unchanged": True,
        "runtime_before": runtime_before, "runtime_after": runtime_after,
        "runtime_lock_holder_after": control.runtime_lock_holder()})
    snapshot.verify()
    completion = snapshot.complete(
        "passed", "Executed isolated complete-cascade research; not approval of every variant",
        command_receipts=preflights + [build["receipt"], run],
        evidence={"protected_tracked_files": len(before), "production_unchanged": True})
    # Keep the authentic compiler receipt's original log paths resolvable.
    snapshot.staging_dir.symlink_to("results", target_is_directory=True)
    shutil.copy2(snapshot.results_dir / "results.json.gz", HERE / "results.json.gz")
    shutil.copy2(snapshot.results_dir / "protection.json", HERE / "protection.json")
    shutil.copy2(snapshot.receipt_path, HERE / "snapshot.json")
    shutil.copy2(snapshot.completion_path, HERE / "completion.json")
    print(json.dumps({"snapshot": str(snapshot.root), "outcome": completion["outcome"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id")
    parser.add_argument("--compiled-snapshot", type=Path)
    parser.add_argument("--container", nargs=3, type=Path)
    args = parser.parse_args()
    if args.container:
        snapshot, build, output = args.container
        container_run(snapshot, json.loads(build.read_text()), output)
    elif args.id:
        host_run(args.id, args.compiled_snapshot)
    else:
        parser.error("--id or --container is required")
