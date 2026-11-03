#!/usr/bin/env python3
"""Pinned native parser graphs and independent twin-machine certificates."""
import argparse
from functools import lru_cache
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "Germanic/tools").is_dir())
sys.path.insert(0, str(ROOT / "Germanic/tools"))
sys.path.insert(0, str(ROOT / ".capr-work"))
sys.path.insert(0, str(HERE))
import functionality


DEFINITIONS = """
define PGNew [[PGCellInput.u - EnglishProtoNative.u] .o. PGCellInput];
define PGFirst [[pgrmStrongPlainHeavy|pgrmStrongPlainHeavyPrefixed] PGCellStem* PGCellEnd];
define ProbeFunctional [a:x];
define ProbeMany [a:x | b:x];
define ProbeBad [a:x | a:y];
define ProbeDelay [{ab}:0 0:{ab}];
define ProbeCycle [a:{xy}]*;
define ProbeEpsCycle [0:x]*;
define ProbeSegmentation [[b:{*b} i:{*i} u:{*u}] | [b:{*b} {iu}:{*iu}]];
"""
NAMES = ["EnglishProtoNative", "EnglishProtoInput", "PGCellRoot", "PGCellPlain",
         "PGCellPrefixed", "PGCellInput", "PGNew", "PGFirst",
         "ProbeFunctional", "ProbeMany", "ProbeBad", "ProbeDelay",
         "ProbeCycle", "ProbeEpsCycle", "ProbeSegmentation"]
PROBES = ["biu", "bíu", "biú", "gailanai", "gaílanai", "biulanai", "biúlanai",
          "gailanananai", "biulanananai", "sáiwalǭ", "fúnðanai"]


def fixed_paths(text, word):
    arcs, finals = functionality.read_att(text)
    outgoing = {}
    for i, arc in enumerate(arcs):
        outgoing.setdefault(arc[0], []).append(i)
    active = set()

    @lru_cache(None)
    def visit(state, offset):
        key = (state, offset)
        if key in active:
            raise ValueError("Fixed-word enumeration requires epsilon-input acyclicity")
        active.add(key)
        results = {(): ()} if state in finals and offset == len(word) else {}
        for i in outgoing.get(state, []):
            _, target, upper, lower = arcs[i]
            consumed = "" if upper == functionality.EPSILON else upper
            if not word.startswith(consumed, offset):
                continue
            for ending, path in visit(target, offset + len(consumed)).items():
                prefix = () if lower == functionality.EPSILON else (lower,)
                results.setdefault(prefix + ending, (i,) + path)
        active.remove(key)
        return results

    return [dict(symbols=list(output), text="".join(output), arc_path=list(path))
            for output, path in sorted(visit(0, 0).items())]


def worker(output):
    import adoption_assay
    from anglo_frisian_experiments import compile_isolated, prepare_definition_image
    from sound_change_order_sensitivity import batch_apply_down

    if not Path("/.dockerenv").exists():
        raise RuntimeError("Container-only native execution")
    output.mkdir()
    recipe = dict(
        definitions=DEFINITIONS, insert_after="", insert_rule="", replace={},
        component_checks=[dict(component=name) for name in NAMES])
    report = dict(components={}, foma=subprocess.check_output(["foma", "-v"], text=True))
    with tempfile.TemporaryDirectory(prefix="capr_parser_proof_") as temporary:
        directory = Path(temporary)
        image = prepare_definition_image(adoption_assay.G / "fsts/germanic.txt", directory)
        if image:
            os.environ["CAPR_FOMA_DEFINITION_IMAGE"] = str(image)
        bins = compile_isolated(
            adoption_assay.G / "fsts/germanic.txt", recipe, [], directory, components_only=True)
        for name in NAMES:
            binary = bins["component:" + name]
            att = output / (name + ".att")
            commands = ["load stack " + str(binary), "print size", "print sigma",
                        "test functional", "test unambiguous", "write att > " + str(att)]
            argv = ["foma", "-q"]
            for command in commands + ["quit"]:
                argv.extend(["-e", command])
            result = subprocess.run(argv, capture_output=True, text=True, check=True, timeout=180)
            text = att.read_text()
            proof = functionality.analyze(text)
            if proof["functional"]:
                functionality.verify(text, proof)
            (output / (name + "-proof.json")).write_text(json.dumps(proof, ensure_ascii=False))
            report["components"][name] = dict(
                argv=argv, stdout=result.stdout, stderr=result.stderr,
                independent={k: v for k, v in proof.items() if k != "delays"})
            if name in NAMES[:8]:
                actual = batch_apply_down(binary, PROBES)
                parsed = {w: fixed_paths(text, w) for w in PROBES}
                assert [sorted({r["text"] for r in parsed[w]}) for w in PROBES] == [
                    sorted(set(values)) for values in actual]
                report["components"][name]["parses"] = parsed
            if name in ("PGCellRoot", "PGCellPlain", "PGNew", "ProbeDelay"):
                square = output / (name + "-square.att")
                argv = ["foma", "-q", "-e", "load stack " + str(binary),
                        "-e", "define T;", "-e", "regex [T.i .o. T];",
                        "-e", "test identity", "-e", "write att > " + str(square),
                        "-e", "quit"]
                result = subprocess.run(argv, capture_output=True, text=True, check=True)
                report["components"][name]["square"] = dict(
                    stdout=result.stdout, sha256=hashlib.sha256(square.read_bytes()).hexdigest())
    (output / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(json.dumps({n: v["independent"]["functional"]
                      for n, v in report["components"].items()}))


def host(identifier, entry=None, extra_files=()):
    from adjudication_control import run_logged
    from experiment_snapshot import create_snapshot

    old = ROOT / ".capr-work/prior/experiments/nonhigh-parser-root-repair-02"
    receipt = json.loads((old / "receipt.json").read_text())
    mapping = json.loads((old / "snapshot/layout.json").read_text())
    inputs = {k: old / "snapshot" / v["snapshot_name"]
              for k, v in receipt["inputs"].items() if k != "layout"}
    entry = entry or Path(__file__)
    for label, path, relative in [
        ("proof", HERE / "functionality.py", str((HERE / "functionality.py").relative_to(ROOT))),
        ("worker", entry, str(entry.relative_to(ROOT))),
        ("baseline", ROOT / "Germanic/fsts/germanic.txt", ".capr-work/baseline-source.txt"),
        *[(f"extra{i}", path, str(path.relative_to(ROOT)))
          for i, path in enumerate(extra_files)],
    ]:
        inputs[label] = path
        mapping[label] = relative
    for p in sorted((ROOT / ".capr-work/pinned-foma").iterdir()):
        label = "pinned_" + p.stem
        inputs[label] = p
        mapping[label] = ".capr-work/pinned-foma/" + p.name
    layout = ROOT / ".capr-work/proof-layout.json"
    layout.write_text(json.dumps(mapping))
    inputs["layout"] = layout
    snapshot = create_snapshot(
        identifier, "New authorized exact-relation parser functionality investigation",
        inputs, variants={"controls": DEFINITIONS}, probes=PROBES,
        expected_outcomes={"independent_complete_analysis": True, "production_modified": False},
        environment={"compose_project": "capr-parser-formal", "native_commit":
                     "82f9acdef234eae8b7619ccc3a386cc0d7df62bc"})
    container = snapshot.stage_in_container()
    destination = container + "/../" + identifier + "-results"
    bootstrap = """
import json,shutil,sys,tempfile,subprocess
from pathlib import Path
src=Path(sys.argv[1]);mapping=json.loads((src/'layout.json').read_text())
root=Path(tempfile.mkdtemp(prefix='capr_parser_proof_source_'))
try:
 for label,relative in mapping.items():
  matches=list(src.glob(label+'.*'));assert len(matches)==1
  p=root/relative;p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(matches[0],p)
 for name in ('compare_fst.py','oe_input_context.py'):
  shutil.copyfile(root/'backend'/name,root/'Germanic'/name)
 subprocess.run(['python3',str(root/sys.argv[3]),'--worker',sys.argv[2]],check=True)
finally:shutil.rmtree(root)
"""
    result = run_logged(
        ["docker", "compose", "exec", "-T", "backend", "python3", "-c",
         bootstrap, container, destination, str(entry.relative_to(ROOT))],
        label="independent-parser-proof", log_dir=snapshot.staging_dir, timeout=900)
    present = subprocess.run(
        ["docker", "compose", "exec", "-T", "backend", "test", "-d", destination]).returncode == 0
    if present:
        subprocess.run(["docker", "compose", "cp", "backend:" + destination + "/.",
                        str(snapshot.staging_dir)], check=True)
    snapshot.complete(
        "passed" if result["ok"] else "failed",
        "Diagnostic/proof execution; production decision remains separate",
        command_receipts=[result])
    snapshot.staging_dir.symlink_to("results", target_is_directory=True)
    print(snapshot.root)
    if not result["ok"]:
        print(Path(result["stderr_log"]).read_text())
        raise SystemExit(1)
    print(Path(result["stdout_log"]).read_text())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--id")
    parser.add_argument("--worker", type=Path)
    args = parser.parse_args()
    worker(args.worker) if args.worker else host(args.id)
