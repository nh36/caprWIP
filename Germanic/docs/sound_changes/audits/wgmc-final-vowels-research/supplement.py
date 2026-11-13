"""Additional pinned controls using the first run's authenticated binaries."""

import json
from pathlib import Path
import subprocess
import sys


def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def host(mode="controls"):
    root = Path.cwd()
    sys.path.insert(0, str(root / "Germanic/tools"))
    import adjudication_control as control
    import experiment_snapshot as snapshots

    work = root / ".capr-work/wgmc-final-vowels-research"
    receipt = json.loads((work / "research-receipt.json").read_text())
    directory = str(Path(next(a for a in receipt["argv"] if a.endswith(".py"))).parent)
    predictions = {
        "parent_container": directory,
        "clay": {"input": "*θ*ō*x*ǣ", "entry_before": "OEVelarFricativePalatalization",
                 "expected": {"current-identity": ["þōhe"], "model-b": ["þō"], "model-c": ["þō"]},
                 "status": "Independent attested-stage witness, not a complete PGmc derivation."},
        "component_checks": [
            {"id": "feminine_citation", "stage": "PNWGmcNStemNLoss",
             "input": "*t*u*n*g*ō*n", "expected": "*t*u*n*g*ǭ"},
            {"id": "masculine_trimoric", "stage": "PNWGmcNStemNLoss",
             "input": "*n*a*m*ô", "expected": "*n*a*m*ô"},
            {"id": "flask_oblique", "stage": "OEARestoration",
             "input": "*f*l*æ*s*k*ō*n", "expected": "*f*l*a*s*k*ō*n"},
            {"id": "mare_oblique", "stage": "OEARestoration",
             "input": "*m*æ*r*ō*n", "expected": "*m*a*r*ō*n"},
            {"id": "flask_nominative", "stage": "OEARestoration",
             "input": "*f*l*æ*s*k*ǣ", "expected": "*f*l*æ*s*k*ǣ"},
            {"id": "mare_nominative", "stage": "OEARestoration",
             "input": "*m*æ*r*ǣ", "expected": "*m*æ*r*ǣ"},
            {"id": "sp_negative", "stage": "OEARestoration",
             "input": "*f*l*æ*s*p*ō*n", "expected": "*f*l*æ*s*p*ō*n"},
            {"id": "sk_front", "stage": "OESkPalatalization",
             "input": "*f*l*æ*s*k*ǣ", "expected": "*f*l*æ*ʃ*ǣ"},
            {"id": "sk_back", "stage": "OESkPalatalization",
             "input": "*f*l*a*s*k*ō*n", "expected": "*f*l*a*s*k*ō*n"},
        ],
        "h_order": {"input": "*t*ā*ç*e", "normal": "*t*ā", "reversed": "*t*ā*e"},
        "palatal_mutation_order": {"input": "*k*ā*j*æ", "normal": "*k*ǣ*j*æ",
                                  "reversed": "*ʧ*ǣ*j*æ"},
        "raw_clay_limit": "θánxōn is rejected by EnglishProtoInput; normalize_proto leaves it "
                          "unchanged. Raw nx is not in the admitted consonant-cluster alphabet. "
                          "Do not change the production parser or invent a mixed-stage input.",
    }
    if mode == "clay":
        predictions = {
            "parent_container": directory,
            "clay": {"input": "*θ*á*n*x*ō*n", "entry_before": "PGmcNasalLossBeforeX",
                     "expected": {name: ["þō"] for name in
                                  ("current-identity", "model-b", "model-c")},
                     "status": "Source-reconstructed phonological input after parsing; "
                               "raw nx is not admitted. No parser change or lexical admission."},
            "component_checks": [],
            "expected_palatal_stage": {
                "current-identity": ["*θ*ō*x*ǭ"],
                "model-b": ["*θ*ō*ç*ǣ"], "model-c": ["*θ*ō*ç*ǣ"]},
            "expected_early_nasal_stage": ["*θ*ã*x*ō*n"],
            "source": "RingeTaylor2014:44,139-142,314; Campbell1959:§119,§128n1; "
                      "SC103 encodes long nasal low vowel as precomposed ã.",
        }
    prefix = "clay" if mode == "clay" else "supplement"
    request = work / (prefix + "-predictions.json")
    dump(request, predictions)
    snapshot = snapshots.create_snapshot(
        "wgmc-final-vowels-controls-20261113" + ("-clay" if mode == "clay" else ""),
        "Previously pinned witnesses as explicit stage controls; no model or corpus re-execution.",
        {"driver": Path(__file__).resolve(), "predictions": request,
         "parent_observations": work / "research-observations.json",
         "parent_receipt": work / "research-receipt.json"},
        variants={}, probes=[], expected_outcomes=predictions,
        negative_controls=["masculine_trimoric", "flask_nominative", "mare_nominative",
                           "sp_negative", "sk_back"],
    )
    with control.runtime_lock("Held-out final-vowel stage controls"):
        container = snapshot.stage_in_container()
        args = [container + "/" + snapshot.input_path(key).name
                for key in ("driver", "predictions", "parent_observations")]
        output = container + "/" + prefix + "-observations.json"
        receipt = control.run_logged(
            ["docker", "compose", "exec", "-T", "backend", "python3", "-u",
             *args, output], label="wgmc-final-vowels-held-out",
            cwd=root, log_dir=work / "validation",
        )
        subprocess.run(["docker", "compose", "cp", "backend:" + output,
                        str(work / (prefix + "-observations.json"))], check=True)
    snapshot.complete("passed" if receipt["ok"] else "failed",
                      "Execution status; individual pinned expectations remain separately visible.",
                      [receipt])
    dump(work / (prefix + "-receipt.json"), receipt)
    print(Path(receipt["stdout_log"]).read_text())
    print(Path(receipt["stderr_log"]).read_text())
    raise SystemExit(receipt["returncode"])


def container(request, parent, output):
    sys.path.insert(0, "/usr/app/tools")
    import anglo_frisian_experiments as af
    from sound_change_order_sensitivity import batch_apply_down

    predictions, prior = json.loads(request.read_text()), json.loads(parent.read_text())
    result = {"predictions": predictions, "parent_sha256": af.digest(parent), "variants": {}}
    for model, original in prior["variants"].items():
        directory = Path(predictions["parent_container"]) / model
        order = original["order"]
        bins = {}
        for i, stage in enumerate(order):
            path = directory / f"af_diagnostic_{i:03d}.bin"
            assert af.digest(path) == original["binary_sha256"]["diagnostic:" + str(i)]
            bins[stage] = path

        def apply(stages, value):
            states = [value]
            trace = []
            for stage in stages:
                states = sorted({v for outputs in batch_apply_down(bins[stage], states) for v in outputs})
                trace.append({"stage": stage, "outputs": states})
            return {"outputs": states, "trace": trace}

        checks = []
        for case in predictions["component_checks"]:
            value = apply([case["stage"]], case["input"])
            checks.append({**case, **value, "passed": value["outputs"] == [case["expected"]]})
        clay = predictions["clay"]
        clay_result = apply(order[order.index(clay["entry_before"]):], clay["input"])
        clay_result["passed"] = clay_result["outputs"] == clay["expected"][model]
        extra = {}
        if "expected_early_nasal_stage" in predictions:
            early = clay_result["trace"][0]["outputs"]
            palatal = next(s["outputs"] for s in clay_result["trace"]
                           if s["stage"] == "OEVelarFricativePalatalization")
            extra["early_nasal"] = {
                "outputs": early, "expected": predictions["expected_early_nasal_stage"],
                "passed": early == predictions["expected_early_nasal_stage"]}
            extra["palatal_checkpoint"] = {
                "outputs": palatal, "expected": predictions["expected_palatal_stage"][model],
                "passed": palatal == predictions["expected_palatal_stage"][model]}
        elif model != "current-identity":
            h = predictions["h_order"]
            for label, sequence in (("normal", ["AFH", "OEContraction"]),
                                    ("reversed", ["OEContraction", "AFH"])):
                value = apply(sequence, h["input"])
                extra["h_" + label] = {**value, "expected": h[label],
                                       "passed": value["outputs"] == [h[label]]}
            p = predictions["palatal_mutation_order"]
            for label, sequence in (("normal", ["AFG", "OEIUmlaut"]),
                                    ("reversed", ["OEIUmlaut", "AFG"])):
                value = apply(sequence, p["input"])
                extra["palatal_" + label] = {**value, "expected": p[label],
                                             "passed": value["outputs"] == [p[label]]}
        result["variants"][model] = {"components": checks, "clay": clay_result, "order": extra}
        dump(output, result)
        print(model, "clay", clay_result["outputs"],
              "failed_components", [c["id"] for c in checks if not c["passed"]],
              "order_checks", {k: v["passed"] for k, v in extra.items()}, flush=True)


if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1:] == ["--clay"]:
        host("clay" if len(sys.argv) == 2 else "controls")
    else:
        container(*map(Path, sys.argv[1:]))
