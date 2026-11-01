#!/usr/bin/env python3
"""Reduced, immutable SC040 composition diagnostics; no corpus replay."""
from __future__ import annotations

import argparse
from collections import defaultdict, deque
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4] if len(HERE.parents) > 4 else Path("/usr/app")


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def renamed(text, prefix):
    for name in sorted(set(re.findall(r"define (R\w+)", text)), key=len, reverse=True):
        text = re.sub(r"\b" + name + r"\b", prefix + name[1:], text)
    return text


def recipe():
    previous = load(HERE.parent / "rainbow-earthly-secondary-stress/experiment.py", "previous")
    failed = load(HERE / "experiment.py", "failed")
    original = previous.foot_definitions()
    definitions = original + failed.proposed_definitions(previous)
    checks = ["RFoot", "RFootOne", "RLate", "MSyll", "MAccent", "MUnsyll",
              "MInit", "MDrop", "MFoot", "MFootOne", "MPlainLower", "MDecode",
              "MLate", "MLateOne"]
    compositions = {
        "DiagSA": "MSyll .o. MAccent",
        "DiagCore": "MSyll .o. MAccent .o. MUnsyll",
        "DiagSent": "SentenceCtx([MSyll .o. MAccent .o. MUnsyll])",
        "DiagLower": "MFoot .o. MPlainLower",
        "MinIns": "[{*} -> {ᵇ*} || .#. _]",
        "MinDrop": "[{ᵇ} -> 0]",
        "MinComp": "MinIns .o. MinDrop",
        "MinMark": "[{*} -> {ᵇ*} || _ a]",
        "MinClean": "MinMark .o. MinDrop",
        "MinDelay": "{ab}:0 0:{ab}",
        "MinAligned": "a:0 b:a 0:b",
    }
    for name, body in compositions.items():
        definitions += "\ndefine " + name + " [" + body + "];\n"
        checks.append(name)
    for prefix, change in (("I", "init"), ("D", "drop"), ("P", "prefix"),
                           ("B", "both"), ("Q", "onset")):
        text = renamed(original, prefix)
        if change in ("init", "both"):
            text = text.replace(
                "define " + prefix + "Syll [",
                "define " + prefix + "Init [{*} -> {ᵇ*} || .#. _ "
                "[" + prefix + "VStart|b|β|d|f|g|k|l|m|n|p|r|s|t|w|x|z|θ|ð|ŋ|ɡ|ʧ|ʤ|ʝ|ʃ|ç|ʒ|j|h]];\n"
                "define " + prefix + "Syll [", 1)
            text = re.sub(r"(define " + prefix + r"Syll(?:One)? \[.*?)(\];)",
                          r"\1 .o. " + prefix + r"Init\2", text)
        if change in ("drop", "both"):
            text = text.replace(
                "define " + prefix + "Syll [",
                "define " + prefix + "Drop [{ᵇ} -> 0 || .#. {ᵇ} "
                + prefix + "C* _ " + prefix + "C* " + prefix + "V];\n"
                "define " + prefix + "Syll [", 1)
            text = re.sub(r"(define " + prefix + r"Syll(?:One)? \[.*?)(\];)",
                          r"\1 .o. " + prefix + r"Drop\2", text)
        if change in ("prefix", "onset"):
            text = text.replace(
                "define " + prefix + "Prefix [{*ᶠ} {ᵇ} " + prefix + "C* " + prefix + "Short|0];",
                "define " + prefix + "Prefix [{*ᶠ} {ᵇ} " + prefix + "C* " + prefix + "V " + prefix + "C*|0];")
        if change == "onset":
            text = text.replace(".#. QPrefix QFirst", ".#. QPrefix QC* QFirst")
        definitions += text
        checks.extend([prefix + "Syll", prefix + "Foot", prefix + "FootOne"])
    source = (ROOT / "Germanic/fsts/germanic.txt").read_text()
    lowering = re.search(
        r"define OEMedUnstressedULowering FootCtx\(\[.*?\]\);", source, re.S).group()
    lowering = lowering.replace("OEMedUnstressedULowering", "QULower")
    lowering = lowering.replace("[{*u}|{*ū}|{*ú}]", "[{*u}|{*ū}|{*ú}|{*ù}]")
    definitions += "\n" + lowering + "\n"
    definitions += "define QLate [QFoot .o. QULower .o. QDecode];\n"
    definitions += "define QLateOne [QFootOne .o. QULower .o. QDecode];\n"
    checks.extend(["QULower", "QLate", "QLateOne"])
    forms = {
        "world": "*w*éo*r*u*l*d*e*s",
        "earthly": "*éo*r*θ*k*u*n*d*e",
        "genitive": "*éo*r*θ*k*u*n*d*e*s",
        "kn": "*k*n*á*n*k*u*n*d*e",
        "hw": "*x*w*á*n*k*u*n*d*e",
        "initial-vowel": "*á*n*k*u*n*d*e",
        "pretonic": "*ᶠ*g*e*éo*r*θ*k*u*n*d*e",
        "heavy-prefix": "*ᶠ*a*n*d*éo*r*θ*k*u*n*d*e",
        "LL": "*á*θ*e*l*i*n*g*a*s",
        "LH": "*k*y*n*i*n*g*a*s",
        "final": "*g*ó*d*k*u*n*d",
        "follow-u": "*á*n*k*u*n*d*u*n",
    }
    return {
        "id": "sc040-formal-resolution", "description": "Reduced composition diagnosis",
        "definitions": definitions, "insert_after": "", "insert_rule": "", "replace": {},
        "sources": [], "assumptions": "Same verified source and Foma alphabet; no corpus filters",
        "limitations": "Diagnostic comparisons are not approved production rules",
        "component_checks": [{"component": n} for n in checks], "forms": forms,
    }


def identity_debt(att):
    edges, finals = defaultdict(list), set()
    for line in att.splitlines():
        fields = line.split("\t")
        if len(fields) == 1:
            finals.add(int(fields[0]))
        else:
            source, target, upper, lower = fields[:4]
            edges[int(source)].append((int(target), upper, lower))
    seen, pending = {0: ((), ())}, deque([0])
    maximum = 0
    while pending:
        state = pending.popleft()
        left, right = seen[state]
        if state in finals and (left or right):
            raise AssertionError(("nonidentity final", state, left, right))
        for target, upper, lower in edges[state]:
            if "UNKNOWN" in upper or "UNKNOWN" in lower:
                raise AssertionError("this bounded diagnostic does not prove unknown-symbol relations")
            if "IDENTITY" in upper or "IDENTITY" in lower:
                assert upper == lower and not left and not right
            a = left + (() if upper == "@0@" else (upper,))
            b = right + (() if lower == "@0@" else (lower,))
            while a and b and a[0] == b[0]:
                a, b = a[1:], b[1:]
            assert not (a and b), ("distinct symbols", state, target, a, b)
            maximum = max(maximum, len(a) + len(b))
            if target in seen:
                assert seen[target] == (a, b), ("inconsistent debt", state, target)
            else:
                seen[target] = (a, b)
                pending.append(target)
    return {"identity": True, "reachable_states": len(seen), "maximum_delay": maximum}


def worker(directory, build):
    sys.path.insert(0, "/usr/app/tools")
    from sound_change_order_sensitivity import batch_apply_down
    data = json.loads((directory / "recipe.json").read_text())
    report = {"foma": subprocess.check_output(["foma", "-v"], text=True).strip(),
              "components": {}, "forms": data["forms"]}
    for key, binary in sorted(build["bins"].items()):
        name = key.removeprefix("component:")
        argv = ["foma", "-q", "-e", "load stack " + binary, "-e", "print size",
                "-e", "print sigma", "-e", "test functional", "-e", "extract ambiguous",
                "-e", "print size", "-e", "print words", "-e", "quit"]
        result = subprocess.run(argv, capture_output=True, text=True, check=True, timeout=120)
        report["components"][name] = {
            "binary_sha256": hashlib.sha256(Path(binary).read_bytes()).hexdigest(),
            "argv": argv, "stdout": result.stdout, "stderr": result.stderr,
            "functional": "1 (1 = TRUE, 0 = FALSE)" in result.stdout,
            "outputs": dict(zip(data["forms"], batch_apply_down(
                Path(binary), list(data["forms"].values())))),
        }
        if name in ("DiagCore", "DiagSent", "MFoot", "QFoot", "QLate", "QLateOne",
                    "MinDelay", "MinAligned"):
            square = directory / (name + "-square.att")
            argv = ["foma", "-q", "-e", "load stack " + binary, "-e", "define T;",
                    "-e", "regex [T.i .o. T];", "-e", "test identity",
                    "-e", "write att > " + str(square), "-e", "quit"]
            result = subprocess.run(argv, capture_output=True, text=True, check=True)
            report["components"][name]["square"] = {
                "argv": argv, "stdout": result.stdout,
                "independent_identity": identity_debt(square.read_text()),
                "att_sha256": hashlib.sha256(square.read_bytes()).hexdigest(),
            }
            if name.startswith("Min"):
                result = subprocess.run(
                    ["flookup", "-i", binary], input="ab\n", capture_output=True,
                    text=True, check=True)
                report["components"][name]["ab_replay"] = result.stdout
    (directory / "formal-results.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({n: v["functional"] for n, v in report["components"].items()}))


def host(identifier):
    os.environ.update(
        COMPOSE_PROJECT_NAME="capr-earthly-sc040",
        COMPOSE_FILE=str(ROOT / "docker-compose.yml") + ":" + str(ROOT / ".capr-work/compose.yml"))
    sys.path.insert(0, str(ROOT / "Germanic/tools"))
    import adjudication_control as control
    import adjudication_run
    import experiment_snapshot
    scratch = ROOT / ".capr-work/sc040-formal-inputs"
    scratch.mkdir(parents=True, exist_ok=True)
    data = recipe()
    (scratch / "recipe.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    snapshot = experiment_snapshot.create_snapshot(
        identifier, "New authorised reduced formal-composition diagnosis after preserved DEFER",
        {"source": ROOT / "Germanic/fsts/germanic.txt", "recipe": scratch / "recipe.json",
         "worker": Path(__file__)}, variants={"diagnostic": data["definitions"]},
        probes=list(data["forms"]), negative_controls=["original RFoot and RLate"],
        expected_outcomes={"identify_first_failed_composition": True},
        environment={"compose_project": "capr-earthly-sc040", "production_modified": False})
    run = adjudication_run.load("SC040")
    if run.state()["stages"]["SNAPSHOT"]["status"] != "complete":
        run.complete_stage("SNAPSHOT", evidence={"snapshot_root": str(snapshot.root)})
    build = snapshot.compile_isolated("source", "recipe", components_only=True)
    private = build["container_source"]
    (snapshot.staging_dir / "build.json").write_text(json.dumps(build, indent=2) + "\n")
    subprocess.run(["docker", "compose", "cp", str(snapshot.staging_dir / "build.json"),
                    "backend:" + private + "/build.json"], check=True, capture_output=True)
    receipt = control.run_logged(
        ["docker", "compose", "exec", "-T", "backend", "python3", private + "/worker.py",
         "--container", private], cwd=ROOT, label="SC040-reduced-formal-diagnosis",
        log_dir=snapshot.staging_dir, timeout=600)
    control.verify_receipt(receipt)
    subprocess.run(["docker", "compose", "cp", "backend:" + private + "/formal-results.json",
                    str(snapshot.staging_dir / "formal-results.json")], check=True, capture_output=True)
    for name in ("DiagCore", "DiagSent", "MFoot", "QFoot", "QLate", "QLateOne",
                 "MinDelay", "MinAligned"):
        subprocess.run(["docker", "compose", "cp", "backend:" + private + "/" + name + "-square.att",
                        str(snapshot.staging_dir / (name + "-square.att"))],
                       check=True, capture_output=True)
    snapshot.complete("passed", "Reduced formal diagnostics executed; production approval remains separate",
                      command_receipts=[build["receipt"], receipt])
    snapshot.staging_dir.symlink_to("results", target_is_directory=True)
    print(Path(receipt["stdout_log"]).read_text())
    print(snapshot.root)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--id")
    parser.add_argument("--container", type=Path)
    args = parser.parse_args()
    if args.container:
        worker(args.container, json.loads((args.container / "build.json").read_text()))
    else:
        host(args.id)
