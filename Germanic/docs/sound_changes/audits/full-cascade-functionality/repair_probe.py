#!/usr/bin/env python3
"""Private SC052 candidate exports; never write production source or bins."""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
SOURCE_HASH = "18f69deaeb2385c94d65a9599f97a96aed9da2fd3065d908e194e9ab3e6cdb0f"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def variants(source, facts):
    from executable_facts import _blank_comments

    body = facts["OEVelarPalatalizationStops"].body
    pieces = body.split(".o.")
    assert len(pieces) == 3
    clauses = pieces[1].strip()[1:-1].split(",")
    assert len(clauses) == 5
    four = "[" + ",".join(clauses[:4]) + "]"
    pair = "[" + clauses[4] + "]"
    serial = pieces[0] + ".o." + four + ".o." + pair + ".o." + pieces[2]
    point = clauses[:4] + ["{*g} -> {*ʤ} || _ {*g} {*j}"]
    pointwise = pieces[0] + ".o.[" + ",".join(point) + "].o." + pieces[2]
    result = {}
    definition = re.search(
        r"(?m)^define OEVelarPalatalizationStops\s+.*?;",
        _blank_comments(source), re.S)
    assert definition
    for label, replacement in (("serial", serial), ("pointwise", pointwise)):
        result[label] = (source[:definition.start()]
                         + "define OEVelarPalatalizationStops " + replacement + ";"
                         + source[definition.end():])
    commas = [definition.start() + match.start()
              for match in re.finditer(",", definition.group())]
    assert len(commas) == 4
    offset = commas[-1]
    result["scoped"] = source[:offset] + "," + source[offset:]
    return result


def worker(snapshot, output):
    from executable_facts import define_facts
    from probe import native

    source = (snapshot / "fst.txt").read_text()
    assert hashlib.sha256(source.encode()).hexdigest() == SOURCE_HASH
    output.mkdir()
    facts = define_facts(snapshot / "fst.txt")
    sequence = json.loads((snapshot / "sequence.json").read_text())
    assert sequence[61]["name"] == "OEVelarPalatalization"
    paths = {}
    for name, text in variants(source, facts).items():
        path = output / f"{name}.txt"
        path.write_text(text)
        paths[name] = path
    probes = {
        "mini_original": "[a -> b || _ e, a a -> b b || _ j]",
        "mini_serial": "[a -> b || _ e] .o. [a a -> b b || _ j]",
        "mini_pointwise": "[a -> b || _ [e | a j]] .o. [a -> b || _ j]",
    }
    commands = []
    for name, expression in probes.items():
        commands += ["clear stack", f"regex [[a|b|e|j]* .o. [{expression}]];",
                     f"save stack {name}.bin", f"write att > {name}.att",
                     "test functional"]
    result = native(commands, output)
    (output / "mini-native.json").write_text(json.dumps(result, indent=2))
    for label in ("original", "serial", "pointwise"):
        path = snapshot / "fst.txt" if label == "original" else paths[label]
        commands = [f"source {path}", "clear stack"]
        for name in ("OEVelarPalatalizationStops", "OEVelarPalatalization"):
            commands += ["clear stack",
                         f"regex [[EnglishStarAlphabet | EnglishPalatalConsonant]* .o. {name}];",
                         f"save stack {label}-{name}.bin",
                         f"write att > {label}-{name}.att", "test functional"]
        if label == "pointwise":
            commands += ["clear stack", "regex OldEnglish;",
                         "save stack candidate.bin", "write att > candidate.att",
                         "test functional"]
            for index in range(60, len(sequence)):
                prefix = (" .o. ".join(s["expression"] for s in sequence[:61])
                          if index == 60 else f"RepairPrefix{index - 1} .o. "
                          + sequence[index]["expression"])
                commands += [f"define RepairPrefix{index} [{prefix}];",
                             "clear stack", f"regex RepairPrefix{index};",
                             f"save stack candidate-prefix-{index:03}.bin"]
        receipt = native(commands, output)
        (output / f"{label}-native.json").write_text(json.dumps(receipt, indent=2))
        if receipt["returncode"] or not (output / f"{label}-OEVelarPalatalization.bin").exists():
            raise RuntimeError(f"Compilation failed: {label}")
    (output / "candidate-comparison.json").write_text(json.dumps({
        "method": "byte-identical actual ATT relations, not transducer subtraction",
        "equal": (output / "serial-OEVelarPalatalizationStops.att").read_bytes()
        == (output / "pointwise-OEVelarPalatalizationStops.att").read_bytes(),
    }, indent=2))
    print("Private candidate relations and actual downstream prefixes exported", flush=True)


def analyze(output):
    proof = load("repair_functionality", HERE.parent / "parser-formal-resolution/functionality.py")
    summary = {}
    for path in sorted(output.glob("*.att")):
        if path.name == "candidate-stop-difference.att":
            continue
        text = path.read_text()
        result = proof.analyze(text)
        if result["functional"]:
            proof.verify(text, result)
        target = path.with_suffix(".proof.json")
        target.write_text(json.dumps(result))
        summary[path.stem] = {k: v for k, v in result.items() if k != "delays"}
        (output / "proof-summary.json").write_text(json.dumps(summary, indent=2))
        print(path.name, json.dumps(summary[path.stem]), flush=True)


def scoped_worker(snapshot, output):
    from executable_facts import define_facts
    from probe import native

    source = (snapshot / "fst.txt").read_text()
    assert hashlib.sha256(source.encode()).hexdigest() == SOURCE_HASH
    output.mkdir()
    candidate = output / "scoped.txt"
    candidate.write_text(variants(source, define_facts(snapshot / "fst.txt"))["scoped"])
    commands = [f"source {candidate}", "clear stack"]
    for name in ("OEVelarPalatalizationStops", "OEVelarPalatalization"):
        commands += ["clear stack",
                     f"regex [[EnglishStarAlphabet | EnglishPalatalConsonant]* .o. {name}];",
                     f"save stack scoped-{name}.bin",
                     f"write att > scoped-{name}.att", "test functional"]
    commands += ["clear stack", "regex OldEnglish;", "save stack scoped.bin",
                 "write att > scoped.att", "test functional", "clear stack",
                 "regex [[a|b|e|j]* .o. [a -> b || _ e ,, a a -> b b || _ j]];",
                 "write att > mini_scoped.att", "test functional"]
    result = native(commands, output)
    (output / "scoped-native.json").write_text(json.dumps(result, indent=2))
    assert result["returncode"] == 0 and (output / "scoped.att").is_file()
    print("Scoped-context candidate exported", flush=True)


def regress(rows_path, original, candidate, output):
    rows = json.loads(rows_path.read_text())
    words = [row["fst_input"] for row in rows]
    probes = ["ggai", "g-géua", "ɣó", "ò-oxun", "ó-oxun", "ó-óxun"]

    def lookup(path, inputs):
        result = subprocess.run(
            ["flookup", "-i", str(path)], input="\n".join(inputs) + "\n",
            text=True, capture_output=True, check=True)
        blocks = result.stdout.strip().split("\n\n")
        assert len(blocks) == len(inputs), (path, len(blocks), len(inputs))
        outputs = []
        for word, block in zip(inputs, blocks):
            values = set()
            for line in block.splitlines():
                echoed, value = line.split("\t", 1)
                assert echoed == word
                if value != "+?":
                    values.add(value)
            outputs.append(sorted(values))
        return outputs

    result = {"rows": rows, "stage_changes": [], "probe_traces": []}
    for index in range(110):
        old = original / f"prefix-{index:03}.bin"
        new = (old if index < 60
               else candidate / f"candidate-prefix-{index:03}.bin")
        before = lookup(old, words + probes)
        after = lookup(new, words + probes)
        result["stage_changes"] += [
            {"offset": index, "row_id": row["row_id"], "old": a, "new": b}
            for row, a, b in zip(rows, before, after) if a != b]
        result["probe_traces"].append({
            "offset": index, "old": dict(zip(probes, before[len(rows):])),
            "candidate": dict(zip(probes, after[len(rows):]))})
        if index == 60:
            pre_sc052 = before[:len(rows)]
        if index == 61:
            result["sc052_census"] = [
                {"row_id": row["row_id"], "concept": row["concept"],
                 "before": a, "original": b, "candidate": c}
                for row, a, b, c in zip(rows, pre_sc052, before, after)
                if a != b]
        if index == 109:
            result["candidate_finals"] = after[:len(rows)]
            result["original_finals"] = before[:len(rows)]
    result["population"] = len(rows)
    result["matches"] = sum(
        row["counterpart"] in values for row, values
        in zip(rows, result["candidate_finals"]))
    result["mismatches"] = [
        row["row_id"] for row, values in zip(rows, result["candidate_finals"])
        if row["counterpart"] not in values]
    result["missing"] = sum(not values for values in result["candidate_finals"])
    result["ambiguous"] = sum(len(values) > 1 for values in result["candidate_finals"])
    output.write_text(json.dumps(result, indent=2))
    print(json.dumps({key: value for key, value in result.items()
                      if key not in ("rows", "probe_traces", "candidate_finals",
                                     "original_finals", "sc052_census")}), flush=True)


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "--worker":
        worker(Path(sys.argv[2]), Path(sys.argv[3]))
    elif len(sys.argv) == 3 and sys.argv[1] == "--analyze":
        analyze(Path(sys.argv[2]))
    elif len(sys.argv) == 6 and sys.argv[1] == "--regress":
        regress(*(Path(path) for path in sys.argv[2:]))
    elif len(sys.argv) == 4 and sys.argv[1] == "--scoped":
        scoped_worker(Path(sys.argv[2]), Path(sys.argv[3]))
    else:
        raise SystemExit("Use --worker IMMUTABLE_SNAPSHOT NEW_OUTPUT or --analyze LOCAL_OUTPUT")
