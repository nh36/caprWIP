#!/usr/bin/env python3
"""Complete corrected SC040 assay, reusing source-identical private components."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4] if len(HERE.parents) > 4 else Path("/usr/app")


def load(path, name):
    import importlib.util
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def worker(directory, build):
    receipt = json.loads((directory / "snapshot_receipt.json").read_text())
    research = load(directory / receipt["inputs"]["research"]["snapshot_name"], "research")
    output = directory / "corrected-results.json.gz"
    research.container_run(directory, build, output)
    sys.path.insert(0, "/usr/app/tools")
    from sound_change_order_sensitivity import batch_apply_down
    previous = load(directory / "library/Germanic/docs/sound_changes/audits/previous/experiment.py",
                    "previous")
    data = json.loads(gzip.decompress(output.read_bytes()))
    for name, head in (("production-proposal", "QFoot"),
                       ("single-onset-proposal", "QFootOne")):
        model = data["models"][name]
        step = next(s for s in model["traces"] if s["stage"] in ("QLate", "QLateOne"))
        states, operations = step["before"], []
        for component in (head, "QULower", "QDecode"):
            after = previous.apply_sets(Path(build["bins"]["component:" + component]), states)
            assert all(len(value) <= 1 for value in after)
            operations.append({"component": component, "before": states, "after": after})
            states = after
        assert states == step["after"]
        model["internal_operations"].append({"stage": step["stage"], "operations": operations})
        assert not model["selected_final_delta_ids"] and not model["immutable_final_delta_indices"]
        assert all(not s["rows"] and not s["immutable_indices"]
                   for s in model["aligned_intermediate_deltas"])
        assert model["candidates"]["earthly-weak-neuter-unaugmented-nasal"]["final"] == ["eorþcunde"]
        assert model["candidates"]["earthly-genitive-grave"]["final"] == ["eorþcundes"]
    for name in ("QSyll", "QFoot", "QFootOne", "QULower", "QDecode", "QLate", "QLateOne"):
        binary = build["bins"]["component:" + name]
        result = subprocess.run(["foma", "-q", "-e", "load stack " + binary,
                                 "-e", "test functional", "-e", "quit"],
                                capture_output=True, text=True, check=True)
        assert "1 (1 = TRUE, 0 = FALSE)" in result.stdout, (name, result.stdout)
        data["formal"][name] = {"argv": result.args, "stdout": result.stdout, "stderr": result.stderr}
        values = batch_apply_down(Path(binary), list(data["plan"]["components"].values()))
        assert all(len(value) == 1 for value in values)
        data["component_results"][name] = dict(zip(data["plan"]["components"], values))
    data["compile_origins"] = build["compile_origins"]
    data["assay_status"] = "passed"
    with output.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0) as compressed:
            compressed.write(json.dumps(data, ensure_ascii=False, separators=(",", ":")).encode())
    print(json.dumps({n: m["counts"] for n, m in data["models"].items()}))


def host(identifier, compiled_snapshot=None):
    os.environ.update(COMPOSE_PROJECT_NAME="capr-earthly-sc040",
                      COMPOSE_FILE=str(ROOT / "docker-compose.yml") + ":" + str(ROOT / ".capr-work/compose.yml"))
    sys.path.insert(0, str(ROOT / "Germanic/tools"))
    import adjudication_control as control
    import adjudication_run
    import experiment_snapshot
    import oe_pipeline
    previous_path = HERE.parent / "rainbow-earthly-secondary-stress/experiment.py"
    research_path = HERE.parent / "earthly-regular-cell/experiment.py"
    previous, research = load(previous_path, "previous"), load(research_path, "research")
    failed, formal = load(HERE / "experiment.py", "failed"), load(HERE / "formal_resolution.py", "formal")
    data = failed.make_plan(previous, research, oe_pipeline)
    definitions = "\n".join(re.findall(r"define Q\w+ .*?;", formal.recipe()["definitions"], re.S))
    source_recipe = {"insert_after": "", "insert_rule": "", "replace": {}, "definitions": definitions}
    for name, target, whole in (("production-proposal", "QLate", "QWhole"),
                                ("single-onset-proposal", "QLateOne", "QWholeOne")):
        data["models"][name] = [target if stage == previous.LATE else stage
                                for stage in data["models"]["identity"]]
        data["whole"][name] = whole
        source_recipe["definitions"] += "\ndefine " + whole + " " + " .o. ".join(data["models"][name]) + ";\n"
    source_recipe["component_checks"] = [{"component": n} for n in ("QWhole", "QWholeOne")]
    data["recipe"] = source_recipe
    scratch = ROOT / ".capr-work/sc040-corrected-inputs"
    scratch.mkdir(parents=True, exist_ok=True)
    write(scratch / "plan.json", data)
    write(scratch / "recipe.json", source_recipe)
    old = experiment_snapshot.Snapshot(ROOT / ".capr-work/experiments/sc040-general-prominence-03")
    formal_origin = experiment_snapshot.Snapshot(ROOT / ".capr-work/experiments/sc040-formal-composition-02")
    old.verify()
    formal_origin.verify()
    old_build = json.loads((old.results_dir / "build.json").read_text())
    formal_build = json.loads((formal_origin.results_dir / "build.json").read_text())
    for origin, build in ((old, old_build), (formal_origin, formal_build)):
        assert origin.receipt()["inputs"]["source"]["sha256"] == hashlib.sha256(
            (ROOT / "Germanic/fsts/germanic.txt").read_bytes()).hexdigest()
        control.verify_receipt(build["receipt"], current=False)
    inputs = {n: Path(v["original_path"]) for n, v in old.receipt()["inputs"].items()
              if n not in ("worker", "plan", "recipe")}
    inputs.update(worker=Path(__file__), plan=scratch / "plan.json", recipe=scratch / "recipe.json",
                  old_build=old.results_dir / "build.json", formal_build=formal_origin.results_dir / "build.json")
    snapshot = experiment_snapshot.create_snapshot(
        identifier, "Corrected general medial footing after reduced formal resolution",
        inputs, variants={n: "\n".join(o) for n, o in data["models"].items()},
        probes=list(data["candidates"]), negative_controls=list(data["components"]),
        expected_outcomes={"selected390_conserved": True, "immutable380_conserved": True,
                           "weak_neuter": "eorþcunde", "genitive": "eorþcundes"},
        environment={"compose_project": "capr-earthly-sc040", "reused_components_are_not_fresh_compilations": True})
    adjudication_run.load("SC040").complete_stage("SNAPSHOT", evidence={"snapshot_root": str(snapshot.root)})
    if compiled_snapshot:
        origin = experiment_snapshot.Snapshot(compiled_snapshot.resolve())
        origin.verify()
        for label, entry in snapshot.receipt()["inputs"].items():
            if label != "worker":
                assert entry["sha256"] == origin.receipt()["inputs"][label]["sha256"]
        build = json.loads((origin.results_dir / "build.json").read_text())
        control.verify_receipt(build["receipt"], current=False)
        build["container_source"] = snapshot.stage_in_container()
        build["compile_reuse_snapshot"] = str(origin.root)
    else:
        build = snapshot.compile_isolated("source", "recipe", components_only=True)
        new_bins = dict(build["bins"])
        build["bins"] = {**old_build["bins"], **formal_build["bins"], **new_bins}
        build["compile_origins"] = [old_build["receipt"], formal_build["receipt"], build["receipt"]]
    original_decode = re.search(r"define RDecode .*?;", previous.foot_definitions(), re.S).group()
    corrected_decode = re.search(r"define QDecode .*?;", definitions, re.S).group()
    assert original_decode.replace("RDecode", "QDecode") == corrected_decode
    build["bins"]["component:QDecode"] = old_build["bins"]["component:RDecode"]
    build["decode_reuse_basis"] = "Exactly identical definition under identifier renaming; identical verified source and context inventories"
    private = build["container_source"]
    write(snapshot.staging_dir / "snapshot_receipt.json", snapshot.receipt())
    write(snapshot.staging_dir / "build.json", build)
    for name in ("snapshot_receipt.json", "build.json"):
        subprocess.run(["docker", "compose", "cp", str(snapshot.staging_dir / name),
                        "backend:" + private + "/" + name], check=True, capture_output=True)
    receipt = control.run_logged(
        ["docker", "compose", "exec", "-T", "backend", "python3", private + "/worker.py",
         "--container", private], cwd=ROOT, label="SC040-corrected-full-assay",
        log_dir=snapshot.staging_dir, timeout=1200)
    control.verify_receipt(receipt)
    subprocess.run(["docker", "compose", "cp", "backend:" + private + "/corrected-results.json.gz",
                    str(snapshot.staging_dir / "corrected-results.json.gz")], check=True, capture_output=True)
    snapshot.complete("passed", "Corrected full cells, formal wrappers and both population comparisons executed",
                      command_receipts=[build["receipt"], receipt])
    snapshot.staging_dir.symlink_to("results", target_is_directory=True)
    print(Path(receipt["stdout_log"]).read_text())
    print(snapshot.root)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--id")
    parser.add_argument("--compiled-snapshot", type=Path)
    parser.add_argument("--container", type=Path)
    args = parser.parse_args()
    if args.container:
        worker(args.container, json.loads((args.container / "build.json").read_text()))
    else:
        host(args.id, args.compiled_snapshot)
