#!/usr/bin/env python3
"""Export actual ordered prefixes in a private container, then prove or refute."""
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def native(commands, directory, timeout=1200):
    argv = ["foma", "-q"]
    for command in commands + ["quit"]:
        argv += ["-e", command]
    result = subprocess.run(argv, cwd=directory, text=True, capture_output=True,
                            timeout=timeout)
    return dict(argv=argv, returncode=result.returncode,
                stdout=result.stdout, stderr=result.stderr)


def worker(output):
    sys.path.insert(0, "/usr/app/tools")
    import oe_pipeline
    output.mkdir()
    source = Path("/usr/app/fsts/germanic.txt")
    assert sha(source) == "18f69deaeb2385c94d65a9599f97a96aed9da2fd3065d908e194e9ab3e6cdb0f"
    shutil.copy2(source, output / "germanic.txt")
    stages = oe_pipeline.stages()
    sequence = [dict(index=s.exec_index, name=s.foma_identifier,
                     expression=s.foma_identifier or s.inline_text)
                for s in stages]
    (output / "sequence.json").write_text(json.dumps(sequence, indent=2))
    commands = ["source germanic.txt"]
    for i, stage in enumerate(sequence):
        body = stage["expression"] if i == 0 else f"Cp{i-1} .o. {stage['expression']}"
        commands += [f"define Cp{i} [{body}];", "clear stack",
                     f"regex Cp{i};", f"save stack prefix-{i:03}.bin"]
    commands += ["clear stack", "regex OldEnglish;", "save stack actual.bin"]
    result = native(commands, output)
    (output / "compile.json").write_text(json.dumps(result, indent=2))
    if result["returncode"] or not (output / "actual.bin").exists():
        raise RuntimeError("Compilation incomplete; preserve compile.json")
    for i, stage in enumerate(sequence):
        label = f"prefix-{i:03}"
        result = native([f"load stack {label}.bin",
                         f"write att > {label}.att",
                         "test functional"], output, 180)
        (output / f"{label}-native.json").write_text(json.dumps(result, indent=2))
        print(json.dumps(dict(prefix=i, name=stage["name"],
                              native_returncode=result["returncode"],
                              native=result["stdout"][-100:])), flush=True)
    result = native(["load stack actual.bin", "write att > actual.att",
                     "test functional"], output, 180)
    (output / "actual-native.json").write_text(json.dumps(result, indent=2))
    (output / "provenance.json").write_text(json.dumps(dict(
        fst_sha256=sha(source), snapshot_sha256=sha(output / "germanic.txt"),
        actual_bin_sha256=sha(output / "actual.bin"),
        foma_version=subprocess.check_output(["foma", "-v"], text=True).strip(),
    ), indent=2))


def analyze(output):
    helper = Path(__file__).resolve().parents[1] / "parser-formal-resolution"
    spec = importlib.util.spec_from_file_location(
        "cascade_functionality", helper / "functionality.py")
    proof = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(proof)
    sequence = json.loads((output / "sequence.json").read_text())
    summary = []
    for i, stage in enumerate(sequence):
        text = (output / f"prefix-{i:03}.att").read_text()
        try:
            result = proof.analyze(text)
            if result["functional"]:
                proof.verify(text, result)
        except ValueError as exc:
            result = dict(status="inapplicable", reason=str(exc))
        (output / f"prefix-{i:03}-proof.json").write_text(json.dumps(result))
        row = dict(stage, **{k: v for k, v in result.items() if k != "delays"})
        summary.append(row)
        (output / "prefix-analysis.json").write_text(json.dumps(summary, indent=2))
        print(json.dumps(row), flush=True)
        if result.get("functional") is False or result.get("status") == "inapplicable":
            break


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--worker":
        worker(Path(sys.argv[2]))
    elif len(sys.argv) == 3 and sys.argv[1] == "--analyze":
        analyze(Path(sys.argv[2]))
    else:
        raise SystemExit("Use --worker CONTAINER_OUTPUT or --analyze LOCAL_OUTPUT")
