#!/usr/bin/env python3
"""Incremental regression: compare the current model with its predecessor.

The ordinary comparison for development is between two adjacent source
states, never a succession of historical grammars:

* dirty working tree (any executable input differs from HEAD):
  **worktree vs HEAD**;
* clean tree: **HEAD vs HEAD^1** (first parent; a merge commit is compared
  against its first parent and the report says so; a missing parent is an
  explicit error).

Both states are identified explicitly (commit id or ``worktree`` plus
content digests). For each state the full cascade is compiled in a
disposable container and evaluated over the state's own selected corpus:
final Old English outputs, every named-stage snapshot output, rule order
and corpus membership/inputs. Compiled builds and evaluation results are
reused through the content-addressed cache (``compile_cache.py``), so a
state whose executable inputs are unchanged is never recompiled or
re-executed; identical keys for both states short-circuit to an explicit
"executable inputs identical" report with no Foma execution at all.

Differences are reported for documentation and adjudication, not
automatically rejected: an intentional model change legitimately alters
outputs, and the immediate parent is a reference for identifying change,
not an independent guarantee of correctness. Protected scientific
fingerprints and frozen baselines remain separate assertions in the
ordinary suite precisely because consecutive comparisons cannot detect
cumulative drift. See docs/HISTORICAL_REPLAY.md.
"""
from __future__ import annotations

import argparse
import json
import shlex
import subprocess
import sys
import tempfile
from hashlib import sha256
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from compile_cache import (  # noqa: E402
    BUILD_ARTIFACT_GLOBS, cached_build, cached_evaluation, compile_cache_key,
    store_build, store_evaluation)

ROOT = Path(__file__).resolve().parents[2]

# The executable inputs of the Old English cascade: the state of exactly
# these files defines a compared model state.
INPUT_PATHS = (
    "Germanic/fsts/germanic.txt",
    "Germanic/data/germanic-aligned-final.tsv",
    "Germanic/data/entry_context_metadata.tsv",
    "backend/oe_input_context.py",
)

_EVAL_SCRIPT = """
import json, sys
from pathlib import Path
sys.path.insert(0, '/usr/app/tools')
import oe_pipeline
from sound_change_order_sensitivity import batch_apply_down
rows = oe_pipeline.load_rows(Path('/usr/app/data/germanic-aligned-final.tsv'))
forms = [oe_pipeline.evaluation_input(row) for row in rows]
bin_dir = Path('/usr/app')
result = {
    'stage_order': [s.foma_identifier for s in oe_pipeline.named_stages()],
    'corpus': {row['row_id']: row['fst_input'] for row in rows},
    'concepts': {row['row_id']: row['concept'] for row in rows},
    'finals': {row['row_id']: outputs for row, outputs in
               zip(rows, batch_apply_down(bin_dir / 'old_english.bin', forms))},
    'snapshots': {name: {row['row_id']: outputs for row, outputs in
                         zip(rows, batch_apply_down(bin_dir / name, forms))}
                  for name in oe_pipeline.expected_snapshot_bins()},
}
print(json.dumps(result, ensure_ascii=False))
"""


class StateError(SystemExit):
    """Explicit, non-silent failure to identify or build a compared state."""


def _git(*arguments: str) -> str:
    return subprocess.check_output(["git", *arguments], cwd=ROOT, text=True)


def _commit_bytes(commit: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)


def state_files(label: str) -> dict[str, bytes]:
    if label == "worktree":
        return {path: (ROOT / path).read_bytes() for path in INPUT_PATHS}
    return {path: _commit_bytes(label, path) for path in INPUT_PATHS}


def resolve_states() -> dict:
    """Identify the two compared source states, explicitly."""
    head = _git("rev-parse", "HEAD").strip()
    worktree = state_files("worktree")
    committed = state_files(head)
    if worktree != committed:
        return {"current": "worktree", "reference": head,
                "basis": "uncommitted executable inputs vs HEAD"}
    line = _git("rev-list", "--parents", "-n", "1", "HEAD").split()
    parents = line[1:]
    if not parents:
        raise StateError(
            f"HEAD ({head[:12]}) has no parent: a root or shallow commit has "
            "no immediate predecessor to compare against. Fetch history or "
            "pass --reference explicitly.")
    basis = "HEAD vs first parent (HEAD^1)"
    if len(parents) > 1:
        basis = ("HEAD is a merge commit; compared against its FIRST parent "
                 "only (HEAD^1), not the merged branch")
    return {"current": head, "reference": parents[0], "basis": basis}


def state_digest(files: dict[str, bytes]) -> dict[str, str]:
    return {path: sha256(payload).hexdigest() for path, payload in files.items()}


def backend_image() -> str:
    image = subprocess.check_output(
        ["docker", "compose", "images", "-q", "backend"], cwd=ROOT,
        text=True).strip()
    if not image:
        raise StateError("the backend image must exist for incremental regression")
    return image


def evaluate_state(label: str, files: dict[str, bytes], image: str) -> dict:
    """Evaluate one source state, reusing cached builds and evaluations."""
    source = files["Germanic/fsts/germanic.txt"]
    corpus = files["Germanic/data/germanic-aligned-final.tsv"]
    extra = {path: files[path] for path in INPUT_PATHS[2:]}
    key = compile_cache_key(image, source, corpus, extra=extra)
    cached = cached_evaluation(key)
    if cached is not None:
        return {**cached, "state": label, "cache_key": key,
                "evaluation": "cached", "digests": state_digest(files)}
    record = _run_evaluation(label, files, image, key)
    store_evaluation(key, record)
    return {**record, "state": label, "cache_key": key,
            "evaluation": "fresh", "digests": state_digest(files)}


def _run_evaluation(label: str, files: dict[str, bytes], image: str,
                    key: str) -> dict:
    mounts = [(ROOT / "Germanic/tools", "/usr/app/tools"),
              (ROOT / "Germanic/data", "/usr/app/data_host")]
    command = ["docker", "create", "--workdir", "/usr/app",
               "--entrypoint", "sleep"]
    for host, container in mounts:
        command += ["--volume", f"{host}:{container}:ro"]
    container_id = subprocess.check_output(
        command + [image, "infinity"], cwd=ROOT, text=True).strip()
    try:
        subprocess.run(["docker", "start", container_id], cwd=ROOT,
                       capture_output=True, check=True)

        def feed(destination: str, payload: bytes) -> None:
            subprocess.run(
                ["docker", "exec", "-i", container_id, "sh", "-c",
                 f"cat > {shlex.quote(destination)}"],
                input=payload, cwd=ROOT, capture_output=True, check=True)

        subprocess.run(
            ["docker", "exec", container_id, "sh", "-c",
             "mkdir -p /usr/app/fsts && cp -a /usr/app/data_host /usr/app/data"],
            cwd=ROOT, capture_output=True, check=True)
        feed("/usr/app/fsts/germanic.txt", files["Germanic/fsts/germanic.txt"])
        feed("/usr/app/data/germanic-aligned-final.tsv",
             files["Germanic/data/germanic-aligned-final.tsv"])
        feed("/usr/app/data/entry_context_metadata.tsv",
             files["Germanic/data/entry_context_metadata.tsv"])
        feed("/usr/app/oe_input_context.py", files["backend/oe_input_context.py"])

        def execute(script: str, timeout: int = 1800):
            return subprocess.run(
                ["docker", "exec", container_id, "sh", "-c", script],
                cwd=ROOT, capture_output=True, check=True, timeout=timeout)

        build = cached_build(key)
        if build is not None:
            subprocess.run(
                ["docker", "exec", "-i", container_id, "sh", "-c",
                 "cd /usr/app && tar xf -"],
                input=build, cwd=ROOT, capture_output=True, check=True)
            compiled = "cached"
        else:
            execute(
                "python3 tools/generate_oe_sandbox.py > /dev/null && "
                "foma -q -f fsts/old_english_sandbox.txt -e quit > /dev/null && "
                "PYTHONPATH=tools python3 -c "
                "'import oe_pipeline; from capr_runtime import write_build_manifest; "
                'write_build_manifest(oe_pipeline.expected_snapshot_bins() + ["old_english.bin"])'
                "'")
            exported = subprocess.run(
                ["docker", "exec", container_id, "sh", "-c",
                 f"cd /usr/app && tar cf - {BUILD_ARTIFACT_GLOBS}"],
                cwd=ROOT, capture_output=True, check=False)
            if exported.returncode == 0:
                store_build(key, exported.stdout, label)
            compiled = "fresh"
        evaluated = execute("python3 -c " + shlex.quote(_EVAL_SCRIPT))
        record = json.loads(evaluated.stdout.decode("utf-8"))
        record["compiled"] = compiled
        return record
    finally:
        subprocess.run(["docker", "rm", "--force", container_id], cwd=ROOT,
                       capture_output=True, check=True)


def fired_rows(record: dict) -> dict[str, list[str]]:
    """Rows changed by each stage, between consecutive named snapshots."""
    order = record["stage_order"]
    snapshots = record["snapshots"]
    bins = list(snapshots)
    fired: dict[str, list[str]] = {}
    for previous, current, identifier in zip(bins, bins[1:], order[1:]):
        fired[identifier] = sorted(
            row for row in snapshots[current]
            if snapshots[current][row] != snapshots[previous].get(row))
    return fired


def compare(current: dict, reference: dict) -> dict:
    shared = sorted(set(current["corpus"]) & set(reference["corpus"]))
    changed_finals = [row for row in shared
                      if current["finals"].get(row) != reference["finals"].get(row)]
    first_divergence = {}
    reference_bins = set(reference["snapshots"])
    for row in changed_finals:
        for name in current["snapshots"]:
            if (name in reference_bins and current["snapshots"][name].get(row)
                    != reference["snapshots"][name].get(row)):
                first_divergence[row] = name
                break
        else:
            first_divergence[row] = "final composition only"
    current_fired, reference_fired = fired_rows(current), fired_rows(reference)
    firing_changes = {
        identifier: {
            "gained": sorted(set(current_fired[identifier])
                             - set(reference_fired[identifier])),
            "lost": sorted(set(reference_fired[identifier])
                           - set(current_fired[identifier])),
        }
        for identifier in sorted(set(current_fired) & set(reference_fired))
        if set(current_fired[identifier]) != set(reference_fired[identifier])}
    return {
        "identical_executable_inputs":
            current["cache_key"] == reference["cache_key"],
        "stage_order_changed":
            current["stage_order"] != reference["stage_order"],
        "stages_added": sorted(set(current["stage_order"])
                               - set(reference["stage_order"])),
        "stages_removed": sorted(set(reference["stage_order"])
                                 - set(current["stage_order"])),
        "rows_added": sorted(set(current["corpus"]) - set(reference["corpus"])),
        "rows_removed": sorted(set(reference["corpus"]) - set(current["corpus"])),
        "inputs_changed": sorted(
            row for row in shared
            if current["corpus"][row] != reference["corpus"][row]),
        "finals_changed": {
            row: {"concept": current["concepts"].get(row, ""),
                  "reference": reference["finals"].get(row),
                  "current": current["finals"].get(row),
                  "first_divergence": first_divergence[row]}
            for row in changed_finals},
        "firing_population_changes": firing_changes,
    }


def summarize(states: dict, current: dict, reference: dict, report: dict) -> str:
    lines = [
        "INCREMENTAL REGRESSION",
        f"  current:   {states['current']} "
        f"(evaluation {current['evaluation']}, build {current.get('compiled', 'cached')})",
        f"  reference: {states['reference']} "
        f"(evaluation {reference['evaluation']}, build {reference.get('compiled', 'cached')})",
        f"  basis:     {states['basis']}",
    ]
    if report["identical_executable_inputs"]:
        lines.append(
            "  executable inputs identical (same content key): no model "
            "difference is possible; the evaluation is shared, not repeated")
        return "\n".join(lines)
    for field in ("stages_added", "stages_removed", "rows_added",
                  "rows_removed", "inputs_changed"):
        if report[field]:
            lines.append(f"  {field}: {', '.join(report[field])}")
    if report["stage_order_changed"] and not (
            report["stages_added"] or report["stages_removed"]):
        lines.append("  stage order changed (same membership)")
    finals = report["finals_changed"]
    lines.append(f"  changed final outputs: {len(finals)}")
    for row, change in sorted(finals.items()):
        lines.append(
            f"    row {row} ({change['concept']}): {change['reference']} -> "
            f"{change['current']} [first divergence: {change['first_divergence']}]")
    if report["firing_population_changes"]:
        lines.append("  firing-population changes:")
        for identifier, change in report["firing_population_changes"].items():
            lines.append(f"    {identifier}: +{change['gained']} -{change['lost']}")
    lines.append(
        "  NOTE: differences identify change relative to the immediate "
        "predecessor; they are adjudicated, not automatically rejected, and "
        "the reference is not an independent guarantee of correctness.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--reference", help=(
        "explicit reference commit (overrides HEAD/HEAD^1 resolution)"))
    parser.add_argument("--json", type=Path, help="write the full report here")
    parser.add_argument("--fail-on-change", action="store_true", help=(
        "exit 3 when any model difference is found (for gating contexts; "
        "the default reports differences for adjudication)"))
    arguments = parser.parse_args(argv)
    states = resolve_states()
    if arguments.reference:
        states["reference"] = _git("rev-parse", arguments.reference).strip()
        states["basis"] += " (reference overridden on the command line)"
    image = backend_image()
    current = evaluate_state(states["current"],
                             state_files(states["current"]), image)
    reference = evaluate_state(states["reference"],
                               state_files(states["reference"]), image)
    report = compare(current, reference)
    print(summarize(states, current, reference, report))
    if arguments.json:
        arguments.json.write_text(json.dumps({
            "states": states,
            "current": {k: current[k] for k in
                        ("state", "cache_key", "evaluation", "digests")},
            "reference": {k: reference[k] for k in
                          ("state", "cache_key", "evaluation", "digests")},
            "report": report,
        }, ensure_ascii=False, indent=1) + "\n")
    changed = not report["identical_executable_inputs"] and (
        report["stage_order_changed"] or report["rows_added"]
        or report["rows_removed"] or report["inputs_changed"]
        or report["finals_changed"] or report["firing_population_changes"])
    return 3 if (arguments.fail_on_change and changed) else 0


if __name__ == "__main__":
    sys.exit(main())
