#!/usr/bin/env python3
"""Two-input, finite-domain SC044/SC055 comparison on pinned current source."""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import threading
import time
from unittest.mock import patch

sys.path.insert(0, "/usr/app/tools")


def worker(snapshot):
    import anglo_frisian_experiments as compiler
    import oe_pipeline
    from capr_runtime import check_build_manifest, layout
    from sound_change_order_sensitivity import batch_apply_down

    started = time.perf_counter()
    runtime = layout()
    source = snapshot / "source.txt"
    plan = json.loads((snapshot / "plan.json").read_text())
    assert hashlib.sha256(source.read_bytes()).hexdigest() == hashlib.sha256(
        runtime.germanic_fst.read_bytes()).hexdigest()
    for name, digest in plan["helpers"].items():
        assert hashlib.sha256((runtime.tools_dir / name).read_bytes()).hexdigest() == digest, name
    stages = oe_pipeline.stages()
    names = [s.foma_identifier for s in stages]
    start, mutation = names.index("OEBreaking"), names.index("OEIUmlaut")
    late = names.index("OEWsPalatalUmlaut")
    assert all(names[start:])
    checkpoint_names = [
        "EAFBrightening", "EAFBrighteningLongFinal", "OEBreaking",
        "OEVelarFricativePalatalization", "OEIUmlaut", "OEWsPalatalUmlaut",
    ]
    bins = {name: runtime.bin_dir / oe_pipeline.stage_for(name).snapshot_bin
            for name in checkpoint_names}
    problems = check_build_manifest(oe_pipeline.expected_snapshot_bins() + ["old_english.bin"])
    if problems:
        raise ValueError(problems)
    assert (snapshot / "corpus.tsv").read_bytes() == runtime.corpus_tsv.read_bytes()
    selected = {row["row_id"]: row for row in oe_pipeline.load_rows(runtime.corpus_tsv)}
    for row in plan["rows"]:
        actual = selected[row["row_id"]]
        assert actual["proto_norm"] == row["input"] and actual["counterpart"] == row["target"]
    raw = [selected[row["row_id"]]["fst_input"] for row in plan["rows"]]
    live = {name: batch_apply_down(path, raw) for name, path in bins.items()}
    endpoints = batch_apply_down(runtime.bin_dir / "old_english.bin", raw)
    incoming = live["EAFBrighteningLongFinal"]
    if any(len(value) != 1 for value in incoming):
        raise ValueError("shared checkpoint must have one surviving state per input")
    forms = [value[0] for value in incoming]
    middle = names[start + 1:mutation]
    # Local vowel-only relations keep the same consonants and i/j on both sides.
    queries = {
        "breaking": ["OEBreaking"],
        "mutation": ["OEIUmlaut"],
        "breaking_then_mutation": ["OEBreaking", "OEIUmlaut"],
        "mutation_then_breaking": ["OEIUmlaut", "OEBreaking"],
    }
    orders = {
        "mutation_early": ["OEIUmlaut", "OEBreaking", *middle, *names[mutation + 1:]],
        "breaking_late": [*middle, "OEIUmlaut", "OEBreaking", *names[mutation + 1:]],
    }
    for variant, order in orders.items():
        for label, stop in (
            ("palatalization", "OEVelarFricativePalatalization"),
            ("second_operation", "OEBreaking"),
            ("before_late_palatal", names[late - 1]),
            ("late_palatal", "OEWsPalatalUmlaut"),
            ("final", names[-1]),
        ):
            queries[variant + ":" + label] = order[:order.index(stop) + 1]
    domain = compiler.foma_domain(forms)
    definitions = []
    checks = []
    labels = {}
    for index, (label, members) in enumerate(queries.items()):
        name = "AFWS" + str(index)
        definitions.append("define " + name + " [" + domain + " .o. "
                           + " .o. ".join(members) + "];")
        checks.append({"component": name})
        labels[label] = name
    recipe = {"definitions": "\n".join(definitions), "replace": {},
              "insert_rule": None, "insert_after": None, "component_checks": checks}
    memory = []

    def measured_compile(script, directory):
        # wait4 measures the actual Foma child, not the Python driver/container.
        with tempfile.TemporaryFile() as stdout, tempfile.TemporaryFile() as stderr:
            begun = time.perf_counter()
            process = subprocess.Popen(
                ["foma", "-q", "-f", script.name], cwd=directory,
                stdout=stdout, stderr=stderr)
            deadline = threading.Timer(600, process.kill)
            deadline.start()
            try:
                _, status, usage = os.wait4(process.pid, 0)
            finally:
                deadline.cancel()
            process.returncode = os.waitstatus_to_exitcode(status)
            stdout.seek(0)
            stderr.seek(0)
            memory.append({"seconds": time.perf_counter() - begun,
                           "peak_rss_kib": usage.ru_maxrss,
                           "returncode": process.returncode})
            log = stdout.read().decode() + "\n" + stderr.read().decode()
            if process.returncode or re.search(r"(?im)\b(error|syntax error|not defined)\b", log):
                raise RuntimeError("isolated Foma compilation failed:\n" + log[-6000:])

    with tempfile.TemporaryDirectory(prefix="capr_sc044_ws_") as temporary:
        directory = Path(temporary)
        with patch.object(compiler, "_compile_foma", measured_compile):
            compiled = compiler.compile_isolated(
                source, recipe, [], directory, components_only=True,
                use_definition_image=bool(os.environ.get("CAPR_FOMA_DEFINITION_IMAGE")))
        script = (directory / "experiment.foma").read_text()
        outputs = {label: batch_apply_down(compiled["component:" + name], forms)
                   for label, name in labels.items()}
    return {
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "entry": {"stage": "OEBreaking", "side": "before", "forms": forms},
        "rows": plan["rows"], "live": live, "endpoints": endpoints,
        "queries": {name: {"members": members, "inputs": forms, "outputs": outputs[name]}
                    for name, members in queries.items()},
        "cost": {"variants": 2, "networks": len(queries), "compiler_calls": len(memory),
                 "foma_processes": memory, "image_loaded": script.startswith("load defined "),
                 "definition_preparation_calls": 0,
                 "seconds": time.perf_counter() - started},
    }


def capture(prefix, root):
    import shlex
    import uuid
    from adjudication_control import run_logged
    from capr_runtime import container_command
    from experiment_snapshot import create_snapshot

    source = root / "Germanic/fsts/germanic.txt"
    here = Path(__file__).resolve().parent
    work = root / ".capr-work/sc044-followup"
    work.mkdir(parents=True, exist_ok=True)
    rows = [{"row_id": "1945", "input": "bálgiz", "target": "bielġ"},
            {"row_id": "2092", "input": "xláxjaną", "target": "hliehhan"}]
    helpers = [
        "anglo_frisian_experiments.py", "oe_pipeline.py", "capr_runtime.py",
        "sound_change_order_sensitivity.py", "executable_facts.py",
    ]
    plan = {
        "rows": rows,
        "hypothesis": "At identical prebreaking states, mutation first yields e; "
                      "revised E-breaking does not break e before lg. Laugh's "
                      "consonantal j-palatalization and later vowel convergence "
                      "must be evaluated independently.",
        "helpers": {name: hashlib.sha256((root / "Germanic/tools" / name).read_bytes()).hexdigest()
                    for name in helpers},
    }
    plan_path = work / "west-saxon-plan.json"
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2))
    snapshot = create_snapshot(
        "sc044-west-saxon-" + uuid.uuid4().hex[:8],
        "Separate vowel order from fricative palatalization on two selected WS witnesses",
        {"source": source, "plan": plan_path, "worker": Path(__file__),
         "corpus": root / "Germanic/data/germanic-aligned-final.tsv",
         **{Path(name).stem: root / "Germanic/tools" / name for name in helpers}},
        variants={"current_source": source.read_text()}, probes=rows,
        expected_outcomes={"local": {"breaking_first": "ie", "mutation_first": "e"},
                           "final_reverse": "observe; do not infer from local vowel"},
        negative_controls=["revised e-breaking before lg", "unchanged consonants in local pairs"])
    container = snapshot.stage_in_container()
    command = container_command(
        "cd /usr/app && " + prefix + "python3 " + shlex.quote(container + "/worker.py")
        + " --worker " + shlex.quote(container))
    receipt = run_logged(command, label="sc044-west-saxon", log_dir=snapshot.staging_dir)
    snapshot.complete("passed" if receipt["ok"] else "failed",
                      "Live production/cumulative records and bounded two-order relations",
                      [receipt])
    if not receipt["ok"]:
        raise RuntimeError((snapshot.results_dir / Path(receipt["stderr_log"]).name).read_text())
    result = json.loads((snapshot.results_dir / Path(receipt["stdout_log"]).name).read_text())
    (work / "west-saxon-latest.json").write_text(json.dumps(
        {"snapshot_root": str(snapshot.root), "result": result}, ensure_ascii=False, indent=2))
    return result


if __name__ == "__main__":
    print(json.dumps(worker(Path(sys.argv[2])), ensure_ascii=False))
