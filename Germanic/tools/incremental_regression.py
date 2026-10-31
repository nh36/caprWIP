#!/usr/bin/env python3
"""Incremental regression: compare consecutive canonical full-trace reports.

CAPR's authoritative record of the complete phonological derivations is the
committed full-trace report (Germanic/docs/debug_snapshots/
oe_full_trace_report.txt), generated once per model state by
tools/oe_full_trace_report.py through the artifact graph. Git already
stores every prior version of that report, so comparing the proposed model
with its immediate predecessor never compiles or evaluates anything:

* staged executable inputs differing from HEAD: **staged state vs HEAD**
  (unstaged work is ignored unless --worktree is passed explicitly);
* clean/unstaged-only tree: **HEAD vs HEAD^1** (first parent; a merge is
  compared against its first parent and the report says so; a missing
  parent is an explicit error);
* ``--worktree``: working tree vs HEAD, for development.

Each report is validated against the source files of its *own* version
(Git blobs for committed/staged states, live files for the working tree)
through the shared provenance core (oe_trace_parse.provenance_problems).
A missing, stale or non-canonical report is an explicit failure, never a
silent skip; a stale *working-tree* report is regenerated through the
canonical artifact-graph mechanism (runtime_bins + full_trace nodes) and
the comparison then operates on the refreshed report.

The comparison examines every corresponding named stage of every
corresponding lexical entry (identity: concept + PROTO + EXPECTED, the
stable row identity present in every report generation), so intermediate
changes that leave final outputs unaffected are reported, including the
first divergence and any later convergence. Rejection states and raw
context-marked forms come from the RAW STAGE FIDELITY section; for older
reports that lack it the comparison is display-level and says so
explicitly rather than reconstructing historical grammars.

Differences are reported for adjudication, not automatically rejected:
the predecessor identifies change, it is not an independent guarantee of
correctness. Protected fingerprints and frozen baselines remain separate
assertions precisely because consecutive comparisons cannot detect
cumulative drift. See docs/HISTORICAL_REPLAY.md.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from hashlib import sha256
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import oe_trace_parse  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
TRACE_PATH = "Germanic/docs/debug_snapshots/oe_full_trace_report.txt"
RESULTS_DIR = ROOT / ".ci-results"
SUMMARY_NAME = "incremental_regression.txt"
REPORT_NAME = "incremental_regression.json"

# Dependency classification for source-state identification. A change to
# any of these between the compared states is reported with its executable
# consequence; germanic.txt being unchanged never by itself makes a change
# to evaluation code computationally irrelevant.
RECOMPILE_PATHS = (
    "Germanic/fsts/germanic.txt",
    "Germanic/fsts/old_english_sandbox.txt",
    "Germanic/tools/generate_oe_sandbox.py",
)
# oe_pipeline.py is an evaluation dependency here: its compilation role is
# already visible through the generated sandbox hash (a pipeline change
# that alters the composition changes old_english_sandbox.txt), while its
# evaluation role (stage set, order, bin mapping) affects the trace with
# the existing binaries intact.
REEVALUATE_PATHS = (
    "Germanic/data/germanic-aligned-final.tsv",
    "Germanic/data/entry_context_metadata.tsv",
    "backend/oe_input_context.py",
    "Germanic/tools/oe_full_trace_report.py",
    "Germanic/tools/oe_pipeline.py",
    "Germanic/tools/sound_change_order_sensitivity.py",
    "Germanic/tools/capr_runtime.py",
)
DEPENDENCY_PATHS = RECOMPILE_PATHS + REEVALUATE_PATHS

STAGED = "STAGED"
WORKTREE = "WORKTREE"


class StateError(SystemExit):
    """Explicit, non-silent failure to identify or validate a compared state."""


def _git(*arguments: str, root: Path = None) -> str:
    return subprocess.check_output(["git", *arguments], cwd=root or ROOT,
                                   text=True)


def state_bytes(state: str, path: str, root: Path = None) -> bytes | None:
    """Content of *path* in *state* (commit id, STAGED or WORKTREE)."""
    root = root or ROOT
    if state == WORKTREE:
        target = root / path
        return target.read_bytes() if target.is_file() else None
    spec = f":{path}" if state == STAGED else f"{state}:{path}"
    proc = subprocess.run(["git", "show", spec], cwd=root,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.stdout if proc.returncode == 0 else None


def state_hash(state: str, path: str, root: Path = None) -> str | None:
    payload = state_bytes(state, path, root)
    return None if payload is None else sha256(payload).hexdigest()


def source_hashes(state: str, root: Path = None) -> dict:
    """sha256 of every provenance source *in the compared state itself*."""
    return {label: state_hash(state, path, root)
            for label, path in oe_trace_parse.SOURCE_PATHS.items()}


def resolve_states(reference: str | None = None, worktree: bool = False,
                   root: Path = None) -> dict:
    """Identify the two compared source states, explicitly."""
    root = root or ROOT
    head = _git("rev-parse", "HEAD", root=root).strip()
    if worktree:
        states = {"current": WORKTREE, "reference": head,
                  "basis": "working tree vs HEAD (explicit --worktree)"}
    else:
        tracked = DEPENDENCY_PATHS + (TRACE_PATH,)
        staged_differs = any(
            state_hash(STAGED, path, root) != state_hash(head, path, root)
            for path in tracked)
        if staged_differs:
            states = {"current": STAGED, "reference": head,
                      "basis": "staged proposed state vs HEAD (unstaged "
                               "work is NOT part of this comparison)"}
        else:
            line = _git("rev-list", "--parents", "-n", "1", "HEAD",
                        root=root).split()
            parents = line[1:]
            if not parents:
                raise StateError(
                    f"HEAD ({head[:12]}) has no parent: a root or shallow "
                    "commit has no immediate predecessor to compare against. "
                    "Fetch history or pass --reference explicitly.")
            basis = "HEAD vs first parent (HEAD^1)"
            if len(parents) > 1:
                basis = ("HEAD is a merge commit; compared against its FIRST "
                         "parent only (HEAD^1), not the merged branch")
            states = {"current": head, "reference": parents[0], "basis": basis}
    if reference:
        states["reference"] = _git("rev-parse", reference, root=root).strip()
        states["basis"] += " (reference overridden on the command line)"
    return states


def load_state(state: str, root: Path = None) -> dict:
    """Retrieve and validate one state's full-trace report (zero Foma).

    The report is validated against the source files of its own version:
    recorded provenance hashes vs that state's blobs, and the report's own
    build-manifest hashes vs its own source hashes. Build-identity checks
    against the *current* contract (expected-bin count, Foma version) are
    the live freshness tests' responsibility, not a historical check.
    """
    text_bytes = state_bytes(state, TRACE_PATH, root)
    if text_bytes is None:
        return {"state": state, "text": None,
                "problems": [f"state {state} has no full-trace report at "
                             f"{TRACE_PATH}"],
                "limitations": []}
    text = text_bytes.decode("utf-8")
    problems = oe_trace_parse.provenance_problems(
        text, source_hashes(state, root))
    problems.extend(oe_trace_parse.structural_problems(text))
    limitations = []
    prov = oe_trace_parse.parse_provenance(text)
    if prov.present and prov.version < oe_trace_parse.PROVENANCE_VERSION:
        limitations.append(
            f"report declares provenance contract v{prov.version}: changes "
            "to the evaluation helpers "
            f"({', '.join(oe_trace_parse.V2_SOURCE_PATHS)}) are not covered "
            "by its recorded provenance for this state")
    try:
        fidelity_absent = oe_trace_parse.parse_fidelity(text) is None
    except ValueError:
        fidelity_absent = False  # malformed: already reported as a problem
    if fidelity_absent:
        limitations.append(
            "report predates the RAW STAGE FIDELITY section: rejected stages "
            "are indistinguishable from no-change stages and context "
            "annotation marks are invisible; comparison is display-level "
            "for this state")
    return {"state": state, "text": text, "problems": problems,
            "limitations": limitations}


def _parsed(text: str) -> dict:
    entries = oe_trace_parse.parse_entries(text)
    firing = oe_trace_parse.parse_firing_summary(text)
    return {
        "entries": entries,
        "fidelity": oe_trace_parse.parse_fidelity(text),
        "firing": firing,
        "stage_order": list(firing),
    }


def _stage_results(entry, fidelity_for_entry: dict | None) -> dict:
    """label -> comparable stage result, exact where fidelity permits.

    A result is ("rejected",) for a stage that rejected its input, else the
    tuple of raw forms (from the fidelity section) or displayed forms. Two
    results are different exactly when the recorded evaluation differed.
    """
    results = {}
    for stage in entry.stages:
        record = (fidelity_for_entry or {}).get(stage.label)
        if record and record["rejected"]:
            results[stage.label] = ("rejected",)
        elif record and record["raw"] is not None:
            results[stage.label] = tuple(record["raw"])
        else:
            results[stage.label] = stage.forms
    return results


def compare(current: dict, reference: dict) -> dict:
    """Complete stage-by-stage comparison of two parsed reports."""
    cur, ref = _parsed(current["text"]), _parsed(reference["text"])
    order_cur, order_ref = cur["stage_order"], ref["stage_order"]
    shared_labels = [l for l in order_cur if l in set(order_ref)]
    cur_keys, ref_keys = set(cur["entries"]), set(ref["entries"])
    shared_keys = sorted(cur_keys & ref_keys)

    display_level = (cur["fidelity"] is None or ref["fidelity"] is None)
    entry_changes = {}
    for key in shared_keys:
        ecur, eref = cur["entries"][key], ref["entries"][key]
        rcur = _stage_results(
            ecur, None if display_level else cur["fidelity"].get(key))
        rref = _stage_results(
            eref, None if display_level else ref["fidelity"].get(key))
        divergent = [l for l in shared_labels
                     if rcur.get(l) != rref.get(l)]
        final_changed = ecur.outputs != eref.outputs
        context_changed = ecur.input_context != eref.input_context
        if not (divergent or final_changed or context_changed):
            continue
        change = {
            "concept": key[0], "proto": key[1], "expected": key[2],
            "divergent_stages": divergent,
            "first_divergence": divergent[0] if divergent else None,
            "reconverged": bool(divergent)
            and rcur.get(shared_labels[-1]) == rref.get(shared_labels[-1]),
            "intermediate_only": bool(divergent) and not final_changed,
            "final_changed": final_changed,
            "context_changed": context_changed,
        }
        if divergent:
            first = divergent[0]
            change["at_first_divergence"] = {
                "reference": list(rref.get(first, ())),
                "current": list(rcur.get(first, ())),
            }
            # Forms at EVERY divergent stage, with each version's actual
            # stage position and the rejection state, from the same
            # _stage_results representation (raw-fidelity where available).
            change["divergences"] = [
                {
                    "stage": label,
                    "position_current": order_cur.index(label),
                    "position_reference": order_ref.index(label),
                    "reference": list(rref.get(label, ())),
                    "current": list(rcur.get(label, ())),
                    "reference_rejected": rref.get(label) == ("rejected",),
                    "current_rejected": rcur.get(label) == ("rejected",),
                }
                for label in divergent
            ]
        if final_changed:
            change["final"] = {"reference": eref.outputs,
                               "current": ecur.outputs}
        entry_changes["{} | {} | {}".format(*key)] = change

    firing_changes = {}
    for label in shared_labels:
        cur_count, cur_pairs = cur["firing"][label]
        ref_count, ref_pairs = ref["firing"][label]
        gained = sorted(set(cur_pairs) - set(ref_pairs))
        lost = sorted(set(ref_pairs) - set(cur_pairs))
        if gained or lost or cur_count != ref_count:
            firing_changes[label] = {
                "reference_count": ref_count, "current_count": cur_count,
                "gained": [" :: ".join(p) for p in gained],
                "lost": [" :: ".join(p) for p in lost],
            }

    return {
        "stage_order_changed": order_cur != order_ref,
        "stages_added": sorted(set(order_cur) - set(order_ref)),
        "stages_removed": sorted(set(order_ref) - set(order_cur)),
        "entries_examined": len(shared_keys),
        "stages_examined": len(shared_labels),
        "entries_added": sorted("{} | {} | {}".format(*k)
                                for k in cur_keys - ref_keys),
        "entries_removed": sorted("{} | {} | {}".format(*k)
                                  for k in ref_keys - cur_keys),
        "entry_changes": entry_changes,
        "intermediate_only_changes": sorted(
            k for k, c in entry_changes.items() if c["intermediate_only"]),
        "final_output_changes": sorted(
            k for k, c in entry_changes.items() if c["final_changed"]),
        "context_changes": sorted(
            k for k, c in entry_changes.items() if c["context_changed"]),
        "firing_population_changes": firing_changes,
        "display_level_comparison": display_level,
    }


def classify_dependencies(states: dict, root: Path = None) -> dict:
    """Executable consequence of each changed dependency between the states."""
    recompile = [p for p in RECOMPILE_PATHS
                 if state_hash(states["current"], p, root)
                 != state_hash(states["reference"], p, root)]
    reevaluate = [p for p in REEVALUATE_PATHS
                  if state_hash(states["current"], p, root)
                  != state_hash(states["reference"], p, root)]
    report_changed = (state_hash(states["current"], TRACE_PATH, root)
                      != state_hash(states["reference"], TRACE_PATH, root))
    if recompile:
        consequence = "requires transducer recompilation"
    elif reevaluate:
        consequence = "requires renewed evaluation (no recompilation)"
    elif report_changed:
        consequence = "presentation-only report difference"
    else:
        consequence = "no effect on the executable model"
    return {"recompile_changed": recompile, "reevaluate_changed": reevaluate,
            "report_changed": report_changed, "consequence": consequence}


def refresh_worktree_trace() -> list:
    """Regenerate a stale working-tree trace through the canonical graph.

    Uses the existing artifact-graph runtime nodes (runtime_bins,
    full_trace) -- the same mechanism as artifact_graph --refresh -- never
    an independent generation path. Returns the actions taken.
    """
    import artifact_graph
    actions = []
    by_name = {node.name: node for node in artifact_graph.nodes()}
    for name in ("runtime_bins", "full_trace"):
        node = by_name[name]
        if node.verify():
            actions.extend(node.build())
    return actions


def run_comparison(reference: str | None = None, worktree: bool = False,
                   root: Path = None, allow_refresh: bool = False) -> dict:
    """Resolve, retrieve, validate and compare: the complete operation.

    Raises StateError when a state cannot be identified or a report is
    missing/invalid for its own version. Requires zero Foma invocations
    when both reports are valid; a stale working-tree report is refreshed
    through the artifact graph only when allow_refresh is set.
    """
    states = resolve_states(reference, worktree, root)
    current = load_state(states["current"], root)
    refreshed = []
    if (current["problems"] and states["current"] == WORKTREE
            and allow_refresh):
        refreshed = refresh_worktree_trace()
        current = load_state(states["current"], root)
    if current["problems"]:
        raise StateError(
            f"invalid full-trace report for state {states['current']}: "
            + "; ".join(current["problems"])
            + ("" if states["current"] == WORKTREE else
               " (regenerate via the artifact graph and commit/stage the "
               "refreshed report with its sources)"))
    deps = classify_dependencies(states, root)
    if (not deps["report_changed"] and not deps["recompile_changed"]
            and not deps["reevaluate_changed"]):
        # Fast path: identical reports and dependencies -- the current
        # report (provenance- and structure-validated in load_state above)
        # covers both states; terminate without a stage comparison.
        return {"states": states, "dependencies": deps,
                "identical": True, "refreshed": refreshed,
                "limitations": current["limitations"],
                "comparison": None, "foma_invocations": 0}
    reference_state = load_state(states["reference"], root)
    if reference_state["problems"]:
        raise StateError(
            f"invalid full-trace report for predecessor state "
            f"{states['reference']}: "
            + "; ".join(reference_state["problems"]))
    comparison = compare(current, reference_state)
    return {
        "states": states,
        "dependencies": deps,
        "identical": False,
        "refreshed": refreshed,
        "limitations": current["limitations"]
        + reference_state["limitations"],
        "comparison": comparison,
        "foma_invocations": 0,
    }


def summarize(result: dict) -> str:
    states, deps = result["states"], result["dependencies"]
    lines = [
        "INCREMENTAL REGRESSION (consecutive full-trace comparison)",
        f"  current:   {states['current']}",
        f"  reference: {states['reference']}",
        f"  basis:     {states['basis']}",
        f"  dependency consequence: {deps['consequence']}",
        "  foma invocations: 0 (Git-stored canonical reports reused)",
    ]
    for field in ("recompile_changed", "reevaluate_changed"):
        if deps[field]:
            lines.append(f"  {field}: {', '.join(deps[field])}")
    if result["refreshed"]:
        lines.append("  refreshed via artifact graph: "
                     + "; ".join(result["refreshed"]))
    for limitation in result["limitations"]:
        lines.append(f"  LIMITATION: {limitation}")
    if result["identical"]:
        lines.append("  reports and executable dependencies identical: no "
                     "model difference is possible")
        return "\n".join(lines)
    c = result["comparison"]
    lines.append(f"  entries examined: {c['entries_examined']}; "
                 f"stages examined: {c['stages_examined']}")
    if c["stage_order_changed"]:
        lines.append("  stage order changed"
                     + ("" if c["stages_added"] or c["stages_removed"]
                        else " (same membership)"))
    for field in ("stages_added", "stages_removed", "entries_added",
                  "entries_removed", "context_changes"):
        if c[field]:
            lines.append(f"  {field}: {', '.join(c[field])}")
    lines.append("  entries with changed intermediate derivations: "
                 f"{len(c['intermediate_only_changes'])}")
    lines.append("  entries with changed final outputs: "
                 f"{len(c['final_output_changes'])}")
    for key, change in sorted(c["entry_changes"].items()):
        detail = []
        if change["first_divergence"]:
            at = change.get("at_first_divergence", {})
            detail.append(
                f"first divergence {change['first_divergence']}: "
                f"{', '.join(at.get('reference', []))} -> "
                f"{', '.join(at.get('current', []))}")
            further = len(change.get("divergences", ())) - 1
            if further > 0:
                detail.append(f"+{further} further divergent stage(s); "
                              "complete forms in "
                              f".ci-results/{REPORT_NAME}")
            if change["reconverged"]:
                detail.append("reconverges before the final stage")
        if change["final_changed"]:
            detail.append(f"final: {change['final']['reference']} -> "
                          f"{change['final']['current']}")
        if change["context_changed"]:
            detail.append("input context changed")
        lines.append(f"    {key}: " + "; ".join(detail))
    if c["firing_population_changes"]:
        lines.append("  changed stage-transition populations "
                     "(cumulative checkpoints, not isolated rule firings):")
        for label, change in c["firing_population_changes"].items():
            lines.append(
                f"    {label}: {change['reference_count']} -> "
                f"{change['current_count']} "
                f"(+{len(change['gained'])}/-{len(change['lost'])})")
    lines.append(
        "  NOTE: differences identify change relative to the immediate "
        "predecessor; they are adjudicated, not automatically rejected, and "
        "the reference is not an independent guarantee of correctness.")
    return "\n".join(lines)


def write_diagnostics(result: dict, summary: str,
                      results_dir: Path = None) -> None:
    results_dir = results_dir or RESULTS_DIR
    results_dir.mkdir(exist_ok=True)
    (results_dir / SUMMARY_NAME).write_text(summary + "\n", encoding="utf-8")
    (results_dir / REPORT_NAME).write_text(
        json.dumps(result, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--reference", help=(
        "explicit reference commit (overrides HEAD/HEAD^1 resolution)"))
    parser.add_argument("--worktree", action="store_true", help=(
        "compare the working tree (not the staged state) with HEAD"))
    parser.add_argument("--no-refresh", action="store_true", help=(
        "fail on a stale working-tree report instead of regenerating it "
        "through the artifact graph"))
    parser.add_argument("--fail-on-change", action="store_true", help=(
        "exit 3 when any model difference is found (for gating contexts; "
        "the default reports differences for adjudication)"))
    arguments = parser.parse_args(argv)
    result = run_comparison(reference=arguments.reference,
                            worktree=arguments.worktree,
                            allow_refresh=not arguments.no_refresh)
    summary = summarize(result)
    print(summary)
    write_diagnostics(result, summary)
    changed = not result["identical"] and any(
        result["comparison"][field] for field in (
            "stage_order_changed", "entries_added", "entries_removed",
            "entry_changes", "firing_population_changes"))
    return 3 if (arguments.fail_on_change and changed) else 0


if __name__ == "__main__":
    sys.exit(main())
