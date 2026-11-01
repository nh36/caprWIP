#!/usr/bin/env python3
"""SC040 snapshot assay using the existing complete-trace research worker."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4] if len(HERE.parents) > 4 else Path("/usr/app")
TOOLS = ROOT / "Germanic/tools"


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def dump(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def proposed_definitions(previous):
    text = previous.foot_definitions()
    names = set(re.findall(r"define (R\w+)", text))
    for name in sorted(names, key=len, reverse=True):
        text = re.sub(r"\b" + name + r"\b", "M" + name[1:], text)
    text = text.replace(
        "define MSyll [",
        "define MInit [{*} -> {ᵇ*} || .#. _ "
        "[MVStart|b|β|d|f|g|k|l|m|n|p|r|s|t|w|x|z|θ|ð|ŋ|ɡ|ʧ|ʤ|ʝ|ʃ|ç|ʒ|j|h]];\n"
        "define MDrop [{ᵇ} -> 0 || .#. {ᵇ} MC* _ MC* MV];\n"
        "define MSyll [", 1)
    text = re.sub(r"(define MSyll(?:One)? \[.*?)(\];)",
                  r"\1 .o. MInit .o. MDrop\2", text)
    text = text.replace(
        "define MPrefix [{*ᶠ} {ᵇ} MC* MShort|0];",
        "define MPrefix [{*ᶠ} {ᵇ} MC* MV MC*|0];")
    text = text.replace("OEMedUnstressedULowering", "MPlainLower")
    lowering = """
define MPlainLower FootCtx([
    {*u} -> {*o} ||
        [EnglishStarVocalic - [{*u}|{*ū}|{*ú}|{*ù}]]
        OEAnyConsonant+ _ [OEAnyConsonant - {*m}]
]);
"""
    return text.replace("\ndefine MLate ", lowering + "\ndefine MLate ", 1)


def make_plan(previous, research, pipeline):
    data = research.plan(previous, pipeline, ROOT)
    data["recipe"]["definitions"] += proposed_definitions(previous)
    original = data["models"]["identity"]
    for name, target in (("production-proposal", "MLate"),
                         ("single-onset-proposal", "MLateOne")):
        data["models"][name] = [
            target if stage == previous.LATE else stage for stage in original]
        ident = "MWhole" if name == "production-proposal" else "MWholeOne"
        data["whole"][name] = ident
        data["recipe"]["definitions"] += (
            "\ndefine " + ident + " " + " .o. ".join(data["models"][name]) + ";\n")
    data["models"] = {name: data["models"][name] for name in (
        "identity", "earlier-prominence", "production-proposal", "single-onset-proposal")}
    data["whole"] = {name: ident for name, ident in data["whole"].items()
                     if name in data["models"]}
    for name in ("MFoot", "MFootOne", "MSyll", "MAccent", "MPlainLower",
                 "MDecode", "MLate", "MLateOne", "MWhole", "MWholeOne"):
        data["recipe"]["component_checks"].append({"component": name})
    extra = {
        "initial-hw-heavy-medial": "*x*w*á*n*k*u*n*d*e",
        "initial-kn-heavy-medial": "*k*n*á*n*k*u*n*d*e",
        "initial-vowel-heavy-medial": "*á*n*k*u*n*d*e",
        "initial-light-heavy-medial": "*k*á*k*u*n*d*e",
        "initial-LL-heavy-medial": "*á*θ*e*l*i*n*g*a*s",
        "cyning-LH": "*k*y*n*i*n*g*a*s",
        "pretonic-heavy-medial": "*ᶠ*g*e*éo*r*θ*k*u*n*d*e",
        "pretonic-heavy-prefix": "*ᶠ*a*n*d*éo*r*θ*k*u*n*d*e",
        "nonhigh-heavy-medial": "*á*n*k*a*n*d*e",
        "headed-u-following-u": "*á*n*k*u*n*d*u*n",
        "final-heavy-negative": "*g*ó*d*k*u*n*d",
        "initial-LH-negative": "*w*é*r*u*l*d*e*s",
        "open-medial-negative": "*á*n*k*u*d*e",
    }
    data["components"].update(extra)
    return data


def worker(directory, build, output):
    receipt = json.loads((directory / "snapshot_receipt.json").read_text())
    research = load(directory / receipt["inputs"]["research"]["snapshot_name"], "research")
    research.container_run(directory, build, output)
    sys.path.insert(0, "/usr/app/tools")
    from sound_change_order_sensitivity import batch_apply_down
    data = json.loads(gzip.decompress(output.read_bytes()))
    previous = load(
        directory / "library/Germanic/docs/sound_changes/audits/previous/experiment.py",
        "previous")
    for name, head in (("production-proposal", "MFoot"),
                       ("single-onset-proposal", "MFootOne")):
        model = data["models"][name]
        step = next(s for s in model["traces"] if s["stage"] in ("MLate", "MLateOne"))
        states = step["before"]
        operations = []
        for component in (head, "MPlainLower", "MDecode"):
            after = previous.apply_sets(
                Path(build["bins"]["component:" + component]), states)
            assert all(len(value) <= 1 for value in after)
            operations.append({"component": component, "before": states, "after": after})
            states = after
        assert states == step["after"]
        model["internal_operations"].append({"stage": step["stage"], "operations": operations})
    for name in ("MFoot", "MFootOne", "MSyll", "MAccent", "MPlainLower",
                 "MDecode", "MLate", "MLateOne"):
        bin_path = Path(build["bins"]["component:" + name])
        data["component_results"][name] = dict(zip(
            data["plan"]["components"], batch_apply_down(
                bin_path, list(data["plan"]["components"].values()))))
        result = subprocess.run(
            ["foma", "-q", "-e", "load stack " + str(bin_path),
             "-e", "test functional", "-e", "quit"],
            capture_output=True, text=True, check=True)
        assert "1 (1 = TRUE, 0 = FALSE)" in result.stdout, (name, result.stdout)
        data["formal"][name] = {"argv": result.args, "stdout": result.stdout,
                               "stderr": result.stderr}
    with output.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0) as compressed:
            compressed.write(json.dumps(data, ensure_ascii=False, separators=(",", ":")).encode())


def host(identifier):
    os.environ.update(
        COMPOSE_PROJECT_NAME="capr-earthly-sc040",
        COMPOSE_FILE=str(ROOT / "docker-compose.yml") + ":" + str(ROOT / ".capr-work/compose.yml"))
    sys.path.insert(0, str(TOOLS))
    import adjudication_control as control
    import adjudication_run
    import experiment_snapshot
    import oe_pipeline
    previous_path = HERE.parent / "rainbow-earthly-secondary-stress/experiment.py"
    research_path = HERE.parent / "earthly-regular-cell/experiment.py"
    previous = load(previous_path, "previous")
    research = load(research_path, "research")
    data = make_plan(previous, research, oe_pipeline)
    scratch = ROOT / ".capr-work/sc040-inputs"
    scratch.mkdir(parents=True, exist_ok=True)
    dump(scratch / "plan.json", data)
    dump(scratch / "recipe.json", data["recipe"])
    (scratch / "proposal.txt").write_text(proposed_definitions(previous))
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
        "previous": previous_path, "research": research_path,
        "worker": Path(__file__), "plan": scratch / "plan.json",
        "recipe": scratch / "recipe.json",
    }
    for name in ("oe_pipeline", "capr_runtime", "anglo_frisian_experiments",
                 "sound_change_order_sensitivity", "executable_facts", "cascade_baseline"):
        inputs["tool_" + name] = TOOLS / (name + ".py")
    snapshot = experiment_snapshot.create_snapshot(
        identifier, "SC040 general medial prominence, before lexical admission",
        inputs, variants={name: "\n".join(order) for name, order in data["models"].items()},
        probes=list(data["candidates"]), negative_controls=list(data["components"]),
        expected_outcomes={"selected390_conserved": True, "original380_conserved": True,
                           "earthly_weak_neuter": "eorþcunde"},
        environment={"compose_project": "capr-earthly-sc040",
                     "container": "capr-earthly-sc040-backend-1",
                     "shared_production_runtime_written": False})
    run = adjudication_run.load("SC040")
    run.complete_stage("SNAPSHOT", evidence={"snapshot_root": str(snapshot.root)})
    build = snapshot.compile_isolated("source", "recipe", components_only=True)
    control.verify_receipt(build["receipt"], current=False)
    private = build["container_source"]
    dump(snapshot.staging_dir / "snapshot_receipt.json", snapshot.receipt())
    dump(snapshot.staging_dir / "build.json", build)
    for name in ("snapshot_receipt.json", "build.json"):
        subprocess.run(
            ["docker", "compose", "cp", str(snapshot.staging_dir / name),
             "backend:" + private + "/" + name], cwd=ROOT, check=True,
            capture_output=True)
    receipt = control.run_logged(
        ["docker", "compose", "exec", "-T", "backend", "python3",
         private + "/" + snapshot.input_path("worker").name,
         "--container", private, private + "/build.json", private + "/results.json.gz"],
        cwd=ROOT, label="SC040-full-assay", log_dir=snapshot.staging_dir, timeout=1200)
    control.verify_receipt(receipt, current=False)
    subprocess.run(
        ["docker", "compose", "cp", "backend:" + private + "/results.json.gz",
         str(snapshot.staging_dir / "results.json.gz")], cwd=ROOT, check=True,
        capture_output=True)
    snapshot.complete("passed", "Executed candidate comparison; scientific verdict remains separate",
                      command_receipts=[build["receipt"], receipt])
    snapshot.staging_dir.symlink_to("results", target_is_directory=True)
    for name, source in (("results.json.gz", snapshot.results_dir / "results.json.gz"),
                         ("snapshot.json", snapshot.receipt_path),
                         ("completion.json", snapshot.completion_path)):
        shutil.copy2(source, HERE / name)
    print(json.dumps({"snapshot_root": str(snapshot.root), "receipt": receipt}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--id")
    parser.add_argument("--container", nargs=3, type=Path)
    args = parser.parse_args()
    if args.container:
        directory, build, output = args.container
        worker(directory, json.loads(build.read_text()), output)
    else:
        host(args.id)
