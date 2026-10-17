#!/usr/bin/env python3
"""Source-derived, research-only full-wrapper experiments (no adopted recipes).

Default: validate a declarative JSON specification without invoking Foma.
Execution additionally requires --execute, --witnesses and --work-dir, inside
the backend container. See --help. Never rebuilds or writes canonical bins.

Schema 1:
  pins: {germanic_fst, corpus_tsv, context, context_helper}: SHA256 strings;
  base_commit: exact source commit; witness_sha256: verified witness-table SHA;
  recipes: [{id, architecture: A|B|C|D, representation, evidence, assumptions,
    definitions: {short_new_identifier: Foma_expression},
    source_replacements: [{old, new, reason, consumers: [identifier,...]}],
    symbols: [{symbol: single_codepoint, role, consumers: [identifier,...]}],
    edits: [{action: insert|move|replace|remove, target, [rule], [side]}]}];
  probes: [{id, fst_input, kind, evidence, historical_stage, reconstruction_level,
    [entry_stage, side, context]}].
All scientific fields are supplied by the investigator, not inferred from fit.
Insert/move use target as anchor and side before|after; replace uses rule as the
replacement. Production rows cannot be overridden. Comparative probes are
reported separately, never treated as Old English selections.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import re
import shutil
import signal
import subprocess
import sys
import time
import unicodedata
import uuid
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[4] / "tools"
sys.path.insert(0, str(TOOLS))
import anglo_frisian_experiments as assay
import oe_pipeline
from capr_runtime import check_build_manifest, layout
from oe_input_context import InputContext, METADATA_FILENAME

NAME = re.compile(r"[A-Za-z][A-Za-z0-9_]*\Z")
NEW_NAME = re.compile(r"XR[A-Za-z0-9]{1,12}\Z")
SHA = re.compile(r"[a-f0-9]{64}\Z")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_order(source):
    return [s.foma_identifier if s.kind == "named" else s.inline_text
            for s in oe_pipeline.parse_stages(source)]


def exactly_once(items, target):
    require(items.count(target) == 1, f"expected exactly one target: {target}")
    return items.index(target)


def edited_order(original, recipe):
    order = list(original)
    for edit in recipe["edits"]:
        action = edit["action"]
        target = edit["target"]
        index = exactly_once(order, target)
        if action == "remove":
            order.pop(index)
        elif action == "replace":
            require(edit["rule"] not in order, "replacement already in composition")
            order[index] = edit["rule"]
        else:
            rule = edit["rule"]
            if action == "move":
                require(rule != target, "cannot move relative to itself")
                order.pop(exactly_once(order, rule))
                index = exactly_once(order, target)
            else:
                require(rule not in order, "inserted operation already present")
            order.insert(index + (edit["side"] == "after"), rule)
    require(len(order) == len(set(order)), "duplicate event identities")
    return order


def transformed_source(text, recipe):
    for change in recipe["source_replacements"]:
        require(text.count(change["old"]) == 1,
                f"source replacement did not match exactly once: {change['old']!r}")
        text = text.replace(change["old"], change["new"], 1)
    return text


def safe_source(text):
    """Only allow inherited script IO with flat local save destinations."""
    for line in oe_pipeline._strip_comments(text).splitlines():
        match = re.match(r"\s*(source|save stack|load stack|system|quit|exit)\b(.*)", line)
        if not match:
            continue
        command, argument = match.groups()
        require(command == "save stack", f"unsupported source command: {command}")
        require(re.fullmatch(r"\s*[A-Za-z0-9_]+\.bin\s*", argument),
                "source save destination is not a flat local bin")


def validate(spec, source):
    require(spec.get("schema_version") == 1, "unsupported schema")
    require(re.fullmatch(r"[a-f0-9]{40}", spec.get("base_commit", "")), "missing base commit")
    require(SHA.fullmatch(spec.get("witness_sha256", "")), "missing witness SHA256")
    require(set(spec.get("pins", {})) == {
        "germanic_fst", "corpus_tsv", "context", "context_helper",
    }, "all four source/context pins required")
    require(all(isinstance(v, str) and SHA.fullmatch(v) for v in spec["pins"].values()),
            "invalid source pin")
    text = source.read_text(encoding="utf-8")
    safe_source(text)
    bodies = oe_pipeline._define_bodies(oe_pipeline._strip_comments(text))
    original = source_order(source)
    require(isinstance(spec.get("recipes"), list) and spec["recipes"], "recipes required")
    ids = set()
    for recipe in spec["recipes"]:
        require(isinstance(recipe.get("id"), str)
                and re.fullmatch(r"[a-z][a-z0-9-]*", recipe["id"])
                and recipe["id"] not in ids, "invalid/duplicate recipe ID")
        ids.add(recipe["id"])
        require(recipe.get("architecture") in {"A", "B", "C", "D"}, "architecture A-D required")
        for key in ("representation", "evidence", "assumptions"):
            require(isinstance(recipe.get(key), str) and recipe[key].strip(), f"{key} required")
        require(isinstance(recipe.get("definitions"), dict), "definition map required")
        for name, expression in recipe["definitions"].items():
            require(NEW_NAME.fullmatch(name) and name not in bodies, "invalid/new definition collision")
            require(isinstance(expression, str) and expression.strip()
                    and ";" not in expression and "#" not in expression.replace(".#.", "")
                    and not re.search(r"\b(define|save|load|source|system|quit|regex)\b", expression),
                    "new definition must be an expression, not commands")
        require(isinstance(recipe.get("source_replacements"), list), "replacement list required")
        for change in recipe["source_replacements"]:
            require(set(change) == {"old", "new", "reason", "consumers"}
                    and all(isinstance(change[k], str) and change[k] for k in ("old", "new", "reason"))
                    and change["old"] != change["new"] and change["consumers"],
                    "source replacement needs exact old/new text, reason and consumers")
            require(all(c in bodies for c in change["consumers"]), "unknown source-change consumer")
        changed = transformed_source(text, recipe)
        safe_source(changed)
        changed_bodies = oe_pipeline._define_bodies(oe_pipeline._strip_comments(changed))
        require(set(changed_bodies) == set(bodies), "source edits may not add/remove definitions")
        bundles = oe_pipeline._bundle_names(text)
        require(all(changed_bodies[b] == bodies[b] for b in bundles),
                "composition changes must use declarative edits, not source replacement")
        require(isinstance(recipe.get("symbols"), list), "symbol audit list required")
        declared_symbols = set()
        for item in recipe["symbols"]:
            symbol = item.get("symbol")
            require(isinstance(symbol, str) and len(symbol) == 1
                    and symbol.isalpha() and not unicodedata.combining(symbol)
                    and symbol not in declared_symbols,
                    "experimental symbol must be one unique Unicode letter/codepoint")
            declared_symbols.add(symbol)
            require(item.get("role") and item.get("consumers"), "symbol role/consumers required")
            require(all(c in changed_bodies or c in recipe["definitions"]
                        for c in item["consumers"]), "unknown symbol consumer")
        original_characters = set(text)
        added_characters = set(changed) | set("".join(recipe["definitions"].values()))
        require(not {c for c in added_characters - original_characters
                     if c.isalpha() and not c.isascii()} - declared_symbols,
                "new alphabetic codepoints must be declared in symbols")
        original_atoms = set(re.findall(r"\{\*([^}]+)\}", text))
        candidate_atoms = set(re.findall(
            r"\{\*([^}]+)\}", changed + "\n" + "\n".join(recipe["definitions"].values())))
        require(not any(any(unicodedata.combining(c) for c in atom)
                        for atom in candidate_atoms - original_atoms),
                "new starred symbols may not contain combining diacritics")
        require(isinstance(recipe.get("edits"), list), "edit list required")
        for edit in recipe["edits"]:
            action = edit.get("action")
            require(action in {"insert", "move", "replace", "remove"}, "unknown edit action")
            expected = {"action", "target"} | ({"rule"} if action != "remove" else set())
            if action in {"insert", "move"}:
                expected.add("side")
                require(edit.get("side") in {"before", "after"}, "explicit side required")
            require(set(edit) == expected, "invalid edit fields")
            require(all(isinstance(edit[k], str) and NAME.fullmatch(edit[k])
                        for k in ("target",) + (() if action == "remove" else ("rule",))),
                    "edit identities must be named stages")
        order = edited_order(original, recipe)
        require(all(event in changed_bodies or event in recipe["definitions"]
                    or event in original for event in order), "undefined edited event")
        require(order[0] == original[0] and order[-1] == original[-1],
                "full-wrapper input and surface endpoints must be retained")
    require(isinstance(spec.get("probes"), list), "probe list required (may be empty)")
    ids = set()
    for probe in spec["probes"]:
        require(isinstance(probe.get("id"), str) and re.fullmatch(r"[a-z][a-z0-9-]*", probe["id"])
                and probe["id"] not in ids, "invalid/duplicate probe")
        ids.add(probe["id"])
        for key in ("fst_input", "kind", "evidence", "historical_stage", "reconstruction_level"):
            require(isinstance(probe.get(key), str) and probe[key].strip(), f"probe {key} required")
        require(not any(c in probe["fst_input"] for c in "\n\r\t"), "multiline probe input")
        require(probe.get("side", "before") in {"before", "after"}, "invalid probe side")
        if "context" in probe:
            InputContext(**probe["context"])
        if "entry_stage" in probe:
            for recipe in spec["recipes"]:
                exactly_once(edited_order(original, recipe), probe["entry_stage"])
            exactly_once(original, probe["entry_stage"])
            require("context" not in probe, "staged probes must encode context explicitly")
    return original


def pin_paths(rt):
    return {"germanic_fst": rt.germanic_fst, "corpus_tsv": rt.corpus_tsv,
            "context": rt.data_dir / METADATA_FILENAME,
            "context_helper": rt.bin_dir / "oe_input_context.py"}


def protected_hashes(rt):
    excluded = Path(__file__).resolve().parent
    paths = set()
    for root in (rt.fsts_dir, rt.data_dir, rt.tools_dir,
                 rt.docs_dir / "sound_changes", rt.docs_dir / "archive"):
        for path in root.rglob("*"):
            if path.is_file() and not path.is_relative_to(excluded) and "__pycache__" not in path.parts:
                paths.add(path)
    paths.update(rt.bin_dir.glob("*.bin"))
    paths.update((rt.build_manifest, rt.bin_dir / "oe_input_context.py"))
    paths.update(path for path in rt.docs_dir.glob("*.md") if path.is_file())
    return {str(p): digest(p) for p in sorted(paths)}


def compile_checkpoints(source_text, recipe, order, directory):
    safe_source(source_text)
    definitions = "\n".join(f"define {name} {body};"
                            for name, body in recipe["definitions"].items())
    lines = [source_text, definitions]
    prefix = None
    checkpoints = []
    for index, event in enumerate(order):
        name = f"XQ{index:03d}"
        body = event if prefix is None else f"{prefix} .o. {event}"
        filename = f"checkpoint_{index:03d}.bin"
        lines.extend((f"define {name} {body};", "clear stack", f"regex {name};",
                      f"save stack {filename}"))
        checkpoints.append(directory / filename)
        prefix = name
    # Stage-entry probes get cumulative suffix checkpoints, not a second cascade.
    suffixes = {}
    for start in recipe.get("_suffix_starts", []):
        previous = None
        suffixes[start] = []
        for index in range(start, len(order)):
            name = f"XS{start:03d}K{index:03d}"
            filename = f"suffix_{start:03d}_{index:03d}.bin"
            body = order[index] if previous is None else f"{previous} .o. {order[index]}"
            lines.extend((f"define {name} {body};", "clear stack", f"regex {name};",
                          f"save stack {filename}"))
            suffixes[start].append(directory / filename)
            previous = name
    script = "\n".join(lines) + "\nquit\n"
    (directory / "experiment.foma").write_text(script, encoding="utf-8")
    result = subprocess.run(["foma", "-q", "-f", "experiment.foma"], cwd=directory,
                            capture_output=True, text=True, timeout=1800)
    log = result.stdout + "\n" + result.stderr
    (directory / "compile.log").write_text(log, encoding="utf-8")
    if result.returncode or re.search(r"(?im)\b(error|not defined|syntax error)\b", log):
        raise RuntimeError(f"Foma compilation failed in {directory}: {log[-6000:]}")
    required = checkpoints + [directory / "old_english.bin"] + [
        path for values in suffixes.values() for path in values]
    require(all(p.is_file() and p.stat().st_size > 0 for p in required),
            f"missing/empty required isolated bin in {directory}")
    return checkpoints, suffixes, {"script": script, "script_sha256": digest(directory / "experiment.foma"),
                                  "compile_log": log}


def apply(bin_path, inputs):
    def expired(_signum, _frame):
        raise TimeoutError(f"flookup exceeded 120 seconds: {bin_path}")

    previous = signal.signal(signal.SIGALRM, expired)
    timer = signal.setitimer(signal.ITIMER_REAL, 120)
    started = time.monotonic()
    try:
        outputs = assay.batch_apply_down(bin_path, inputs)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)
        if timer[0]:
            signal.setitimer(signal.ITIMER_REAL, max(0.001, timer[0] - (time.monotonic() - started)),
                             timer[1])
    require(len(outputs) == len(inputs), "flookup lost input rows")
    return [sorted(set(values)) for values in outputs]


def traces(paths, events, inputs, ids, start=0):
    before = [[form] for form in inputs]
    result = {identifier: [] for identifier in ids}
    census = []
    for index, (event, path) in enumerate(zip(events[start:], paths), start):
        after = apply(path, inputs)
        firings = []
        for identifier, old, new in zip(ids, before, after):
            status = "rejected" if not new else "ambiguous" if len(new) > 1 else "unique"
            state = {"event": event, "index": index + 1, "before": old, "after": new,
                     "status": status}
            result[identifier].append(state)
            if old != new:
                firings.append({"id": identifier, **state})
        census.append({"event": event, "index": index + 1, "firings": firings})
        before = after
    return result, census, before


def entry_index(probe, order):
    if "entry_stage" not in probe:
        return 0
    index = exactly_once(order, probe["entry_stage"]) + (probe.get("side", "before") == "after")
    require(index < len(order), "probe entry leaves no cascade suffix")
    return index


def evaluate(source_text, recipe, order, rows, probes, directory):
    recipe = {**recipe, "_suffix_starts": sorted({
        entry_index(p, order) for p in probes if entry_index(p, order) > 0})}
    paths, suffixes, compiler = compile_checkpoints(source_text, recipe, order, directory)
    ids = [row["id"] for row in rows]
    inputs = [oe_pipeline.evaluation_input(row) for row in rows]
    row_traces, census, finals = traces(paths, order, inputs, ids)
    supplemental = []
    for start in sorted({entry_index(p, order) for p in probes}):
        group = [p for p in probes if entry_index(p, order) == start]
        forms = [InputContext(**p["context"]).encode(p["fst_input"])
                 if "context" in p else p["fst_input"] for p in group]
        history, fires, outputs = traces(suffixes[start] if start else paths, order,
                                        forms, [p["id"] for p in group], start)
        for probe, form, output in zip(group, forms, outputs):
            supplemental.append({**probe, "evaluation_input": form, "entry_index": start + 1,
                                 "trace": history[probe["id"]], "outputs": output,
                                 "firing_events": [c["event"] for c in fires
                                                   if any(f["id"] == probe["id"] for f in c["firings"])]})
    return {"recipe": {k: v for k, v in recipe.items() if not k.startswith("_")},
            "order": order, "compiler": compiler, "traces": row_traces,
            "census": census, "outputs": dict(zip(ids, finals)), "probes": supplemental,
            "source_native_outputs": apply(directory / "old_english.bin", inputs)}


def verify_baseline(rows, outputs, rt):
    with (rt.docs_dir / "sound_changes/cascade_baseline/cascade_baseline_outputs.tsv").open(
            encoding="utf-8", newline="") as handle:
        frozen = list(csv.DictReader(handle, delimiter="\t"))
    require(len(rows) == len(frozen) == 387, "full selected387 corpus required")
    by_id = {row["row_id"]: row for row in frozen}
    require(len(by_id) == 387 and {r["id"] for r in rows} == set(by_id), "frozen row IDs differ")
    for row in rows:
        old = by_id[row["id"]]
        require(all(row[key] == old[key] for key in (
            "proto", "proto_norm", "fst_input", "counterpart", "word_stress", "phonological_finality")),
            f"selected identity differs from frozen row {row['id']}")
        require(outputs[row["id"]] == [old["outputs"]],
                f"isolated baseline differs from frozen row {row['id']}")


def write_receipt(path, report):
    require(not path.exists(), f"refusing to overwrite receipt: {path}")
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "wt", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def execute(spec, witnesses, work_dir, receipt):
    rt = layout()
    require(rt.is_container, "--execute is allowed only inside the backend container")
    require(shutil.which("foma") and shutil.which("flookup"), "foma/flookup missing")
    require(work_dir.is_relative_to(rt.germanic_dir / "docs/sound_changes/audits/"
                                   "sc015-r-adverb-lengthening-investigation"),
            "work directory must be inside this investigation, never canonical runtime or /tmp")
    require(receipt.is_relative_to(Path(__file__).resolve().parent),
            "receipt must be inside this investigation")
    require(not receipt.exists() and receipt.parent.is_dir(), "receipt needs a new path in an existing directory")
    require(digest(witnesses) == spec["witness_sha256"], "historical witness table missing or changed")
    original = validate(spec, rt.germanic_fst)
    for key, path in pin_paths(rt).items():
        require(digest(path) == spec["pins"][key], f"source pin changed: {key}")
    errors = check_build_manifest(oe_pipeline.expected_snapshot_bins() + ["old_english.bin"], rt)
    require(not errors, f"canonical bin provenance stale; do not rebuild during research: {errors}")
    rows = assay.corpus_rows(rt.corpus_tsv)
    require(len(rows) == 387, "387 original selected rows required")
    before = protected_hashes(rt)
    report = {"schema_version": 1, "status": "started", "specification": spec,
              "driver_sha256": digest(Path(__file__)), "rows": rows,
              "protected_before": before, "models": []}
    work_dir.mkdir(parents=True, exist_ok=True)
    scratch = work_dir / ("run-" + uuid.uuid4().hex)
    scratch.mkdir()
    try:
        version = subprocess.run(["foma", "-v"], check=True, capture_output=True, text=True)
        report["foma_version"] = version.stdout + version.stderr
        text = rt.germanic_fst.read_text(encoding="utf-8")
        identity = {"id": "identity", "definitions": {}, "source_replacements": [], "edits": []}
        directory = scratch / "identity"
        directory.mkdir()
        baseline = evaluate(text, identity, original, rows, spec["probes"], directory)
        native = apply(rt.bin_dir / "old_english.bin",
                       [oe_pipeline.evaluation_input(row) for row in rows])
        require(list(baseline["outputs"].values()) == baseline["source_native_outputs"] == native,
                "full-wrapper identity differs from isolated native or canonical native")
        verify_baseline(rows, baseline["outputs"], rt)
        report["baseline"] = baseline
        for recipe in spec["recipes"]:
            directory = scratch / recipe["id"]
            directory.mkdir()
            model = evaluate(transformed_source(text, recipe), recipe, edited_order(original, recipe),
                             rows, spec["probes"], directory)
            model["deltas"] = [
                {"id": row["id"], "concept": row["concept"],
                 "baseline": baseline["outputs"][row["id"]], "variant": model["outputs"][row["id"]]}
                for row in rows if baseline["outputs"][row["id"]] != model["outputs"][row["id"]]]
            model["rejected_ids"] = [k for k, v in model["outputs"].items() if not v]
            model["ambiguous_ids"] = [k for k, v in model["outputs"].items() if len(v) > 1]
            model["rejected_probes"] = [p["id"] for p in model["probes"] if not p["outputs"]]
            model["ambiguous_probes"] = [p["id"] for p in model["probes"] if len(p["outputs"]) > 1]
            model["evaluation_status"] = (
                "recorded_with_rejections_or_ambiguity"
                if any(model[key] for key in ("rejected_ids", "ambiguous_ids",
                                             "rejected_probes", "ambiguous_probes"))
                else "recorded_unique_outputs"
            )
            report["models"].append(model)
        report["status"] = "complete"
    except Exception as error:
        report["status"] = "failed"
        report["error"] = f"{type(error).__name__}: {error}"
        report["diagnostic_directory"] = str(scratch)
        raise
    finally:
        after = protected_hashes(rt)
        report["protected_after"] = after
        report["protected_unchanged"] = before == after
        report["protected_changes"] = [p for p in sorted(before.keys() | after.keys())
                                       if before.get(p) != after.get(p)]
        if before != after:
            report["status"] = "failed"
            report["protection_error"] = "protected artifacts changed during experiment"
        write_receipt(receipt, report)
        if report["status"] == "complete":
            shutil.rmtree(scratch)
    require(report["protected_unchanged"], "protected artifacts changed; see failure receipt")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("specification", type=Path)
    parser.add_argument("--execute", action="store_true", help="explicitly enable isolated container Foma")
    parser.add_argument("--witnesses", type=Path, help="source-verified table; SHA must match specification")
    parser.add_argument("--work-dir", type=Path, help="isolated scratch root inside this investigation")
    parser.add_argument("--receipt", type=Path, help="new JSON or .json.gz receipt; never overwritten")
    args = parser.parse_args()
    spec = json.loads(args.specification.read_text(encoding="utf-8"))
    order = validate(spec, layout().germanic_fst)
    for key, path in pin_paths(layout()).items():
        require(digest(path) == spec["pins"][key], f"source pin changed: {key}")
    if not args.execute:
        print(json.dumps({"status": "validated_without_foma", "events": len(order),
                          "recipes": [r["id"] for r in spec["recipes"]]}, indent=2))
        return
    require(all((args.witnesses, args.work_dir, args.receipt)),
            "--execute requires --witnesses, --work-dir and --receipt")
    started = time.monotonic()
    report = execute(spec, args.witnesses.resolve(), args.work_dir.resolve(), args.receipt.resolve())
    print(json.dumps({"status": report["status"], "receipt": str(args.receipt),
                      "seconds": round(time.monotonic() - started, 2)}, indent=2))


if __name__ == "__main__":
    main()
