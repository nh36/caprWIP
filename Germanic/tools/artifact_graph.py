#!/usr/bin/env python3
"""ONE declarative artifact graph for the Germanic control plane.

Every generated artifact in the sound-change control plane is a node here,
with its authority (the SOURCE it is projected from), its outputs, a
non-mutating freshness check, and a builder. Nothing else in the repository
may hand-pick builders: the adjudication front-end (adjudicate.py) and the
acceptance workflow both drive THIS graph.

The refresh contract
    python3 Germanic/tools/adjudicate.py --refresh

    * regenerates every stale projection from its authority, in dependency
      order, reaching a fixed point for the census<->views join;
    * rebuilds runtime evidence (stage bins, canonical full trace,
      interaction matrix) ONLY when its recorded input hashes show it stale
      — a no-op refresh never touches Docker;
    * ends by re-verifying every node and printing ``CONTROL PLANE CLEAN``,
      or one actionable error naming the authority to fix.

Node kinds
    projection  deterministic host-side render; check = render-and-compare
    regen       deterministic host-side builder without an in-memory render;
                check = snapshot outputs, rebuild, compare, restore
    runtime     container-built evidence with recorded input provenance;
                check = hash comparison (host-only, never fabricates)

Interaction-matrix provenance
    The matrix is CURRENT-STATE analysis. Its sidecar
    (cascade_baseline/cascade_interaction_provenance.json) records a hash
    over (a) the harness source, (b) the stage-derived pair list, and
    (c) the canonical one-line definitions of every Foma network reachable
    from EnglishProtoInput and the paired rules (executable_facts closure).
    A pure reorder of the cascade changes none of these, so legitimate moves
    do not force a matrix rebuild; editing any participating rule does.
    The corpus TSV is deliberately NOT hashed: matrix equivalence is decided
    over the EnglishProtoInput language, whose definition closure already
    lives in germanic.txt.

Usage
    python3 Germanic/tools/artifact_graph.py --check     # verify all nodes
    python3 Germanic/tools/artifact_graph.py --refresh   # rebuild stale ones
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))
REPO_ROOT = TOOLS.parents[1]
ASSEMBLY = REPO_ROOT / "Germanic/docs/assembly"

import build_reader_book  # noqa: E402
import cascade_order_manifest  # noqa: E402
import executable_facts  # noqa: E402
import generate_registry_views  # noqa: E402
import oe_pipeline  # noqa: E402
import rule_coverage_census  # noqa: E402
from capr_runtime import (  # noqa: E402
    check_build_manifest,
    run_in_runner,
    write_build_manifest,
)
from oe_full_trace_report import trace_provenance_problems  # noqa: E402

SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
BASELINE_DIR = SC_DIR / "cascade_baseline"
SANDBOX_FST = REPO_ROOT / "Germanic/fsts/old_english_sandbox.txt"
FULL_TRACE = REPO_ROOT / "Germanic/docs/debug_snapshots/oe_full_trace_report.txt"
BOOK_DIR = REPO_ROOT / "Germanic/docs/book"
INDEX_BUILDER = TOOLS / "build_index_verborum.py"
INDEX_HEADER = ASSEMBLY / "book_draft_index_registry.tex"
BOOK_DRAFT_BUILDER = ASSEMBLY / "build_capr_book_draft.py"

MATRIX = BASELINE_DIR / "cascade_interaction_matrix.tsv"
MATRIX_PROVENANCE = BASELINE_DIR / "cascade_interaction_provenance.json"
HARNESS = TOOLS / "cascade_interaction_harness.py"
STAGING_MAP = SC_DIR / "sound_change_historical_staging_map.tsv"
ORDER_MANIFEST = BASELINE_DIR / "cascade_order_manifest.tsv"
MATRIX_EARLIER_STAGES = "nwgmc,pnwgmc"
MATRIX_LATER_STAGES = "pwgmc"
MATRIX_ROOT_NETWORK = "EnglishProtoInput"

REFRESH_HINT = ("run the control-plane refresh: "
                "python3 Germanic/tools/adjudicate.py --refresh")


class GraphError(RuntimeError):
    """A node cannot be checked or built; message names the authority."""


def _rel(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


@dataclass(frozen=True)
class Node:
    name: str
    kind: str  # "projection" | "regen" | "runtime"
    authority: str  # the SOURCE (or runtime step) that owns this artifact
    verify: Callable[[], list]  # non-mutating; [] means fresh
    build: Callable[[], list]  # returns descriptions of what changed


# --------------------------------------------------------------------------
# projection nodes: deterministic in-memory render vs committed text
# --------------------------------------------------------------------------

def _projection(name: str, authority: str,
                render: Callable[[], dict]) -> Node:
    def verify() -> list:
        try:
            rendered = render()
        except SystemExit as exc:  # fail-closed renders (census)
            return [f"{name}: {exc}"]
        problems = []
        for path, text in rendered.items():
            current = (path.read_text(encoding="utf-8")
                       if path.exists() else None)
            if current != text:
                problems.append(
                    f"stale generated artifact {_rel(path)} "
                    f"(authority: {authority}); {REFRESH_HINT}")
        return problems

    def build() -> list:
        changed = []
        for path, text in render().items():
            current = (path.read_text(encoding="utf-8")
                       if path.exists() else None)
            if current != text:
                path.write_text(text, encoding="utf-8")
                changed.append(_rel(path))
        return changed

    return Node(name, "projection", authority, verify, build)


def _render_executable_order() -> dict:
    return {
        cascade_order_manifest.MANIFEST_OUT: cascade_order_manifest.manifest_text(),
        cascade_order_manifest.MODEL_OUT: cascade_order_manifest.model_text(),
    }


def _render_oe_sandbox() -> dict:
    return {SANDBOX_FST: oe_pipeline.sandbox_text()}


def _render_census() -> dict:
    return {rule_coverage_census.OUTPUT: rule_coverage_census.census_text()}


def _render_book_draft() -> dict:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "build_capr_book_draft", BOOK_DRAFT_BUILDER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return {mod.OUTPUT_PATH: mod.build_book_markdown()}


# --------------------------------------------------------------------------
# regen node: deterministic host builder without an in-memory render
# --------------------------------------------------------------------------

def _index_outputs() -> list:
    return sorted(p for p in BOOK_DIR.rglob("*") if p.is_file()) + [INDEX_HEADER]


def _run_index_builder() -> None:
    result = subprocess.run([sys.executable, str(INDEX_BUILDER)],
                            cwd=REPO_ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        raise GraphError(
            f"{_rel(INDEX_BUILDER)} exited {result.returncode}: "
            f"{(result.stderr or result.stdout).strip().splitlines()[-1:]}")


def _regen_index_verborum() -> Node:
    authority = ("book draft + reader section 20 + docs/book decision TSVs "
                 f"via {_rel(INDEX_BUILDER)}")

    def snapshot() -> dict:
        return {p: p.read_bytes() for p in _index_outputs()}

    def verify() -> list:
        before = snapshot()
        _run_index_builder()
        after = snapshot()
        stale = sorted(_rel(p) for p in set(before) | set(after)
                       if before.get(p) != after.get(p))
        if stale:
            # restore: the check must not mutate the tree
            for p in set(before) | set(after):
                if before.get(p) != after.get(p):
                    if p in before:
                        p.write_bytes(before[p])
                    else:
                        p.unlink()
            return [f"stale generated artifact {s} (authority: {authority}); "
                    f"{REFRESH_HINT}" for s in stale]
        return []

    def build() -> list:
        before = snapshot()
        _run_index_builder()
        after = snapshot()
        return sorted(_rel(p) for p in set(before) | set(after)
                      if before.get(p) != after.get(p))

    return Node("index_verborum", "regen", authority, verify, build)


# --------------------------------------------------------------------------
# runtime nodes: hash-checked container evidence
# --------------------------------------------------------------------------

def _expected_bins() -> list:
    return oe_pipeline.expected_snapshot_bins() + ["old_english.bin"]


def _bins_verify() -> list:
    problems = check_build_manifest(_expected_bins())
    return [f"stage bins stale: {p}; {REFRESH_HINT}" for p in problems]


def _bins_build() -> list:
    rebuild = run_in_runner("foma -q -l fsts/old_english_sandbox.txt -e quit",
                            capture_output=True, text=True)
    if rebuild.returncode != 0:
        raise GraphError("foma rebuild of fsts/old_english_sandbox.txt exited "
                         f"{rebuild.returncode}:\n{rebuild.stderr or rebuild.stdout}")
    manifest_path = write_build_manifest(_expected_bins())
    equiv = run_in_runner("python3 tools/check_production_sandbox_equivalence.py")
    if equiv.returncode != 0:
        raise GraphError("production/sandbox semantic equivalence check exited "
                         f"{equiv.returncode}")
    return [f"rebuilt stage bins + {manifest_path.name} "
            "(production/sandbox equivalence verified)"]


def _trace_verify() -> list:
    if not FULL_TRACE.is_file():
        return [f"missing canonical full trace {_rel(FULL_TRACE)}; {REFRESH_HINT}"]
    return [f"canonical full trace stale: {p}; {REFRESH_HINT}"
            for p in trace_provenance_problems(
                FULL_TRACE.read_text(encoding="utf-8"))]


def _trace_build() -> list:
    trace = run_in_runner("python3 tools/oe_full_trace_report.py --all")
    if trace.returncode != 0:
        raise GraphError(f"oe_full_trace_report.py --all exited {trace.returncode}")
    return [f"regenerated {_rel(FULL_TRACE)} (~16 min runtime evidence)"]


# --- interaction matrix provenance ----------------------------------------

_TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9]*")


def matrix_pairs() -> list:
    from cascade_interaction_harness import registry_rules_by_stage
    earlier = registry_rules_by_stage(
        STAGING_MAP, ORDER_MANIFEST, MATRIX_EARLIER_STAGES)
    later = registry_rules_by_stage(
        STAGING_MAP, ORDER_MANIFEST, MATRIX_LATER_STAGES)
    return [(e, l) for e in earlier for l in later]


def definition_closure(seeds: list) -> dict:
    """Canonical definitions of every network reachable from the seeds."""
    facts = executable_facts.define_facts()
    missing = sorted(n for n in seeds if n not in facts)
    if missing:
        raise GraphError(
            "matrix provenance: no live define for "
            f"{', '.join(missing)} in Germanic/fsts/germanic.txt")
    closure: dict = {}
    frontier = list(seeds)
    while frontier:
        name = frontier.pop()
        if name in closure:
            continue
        raw = facts[name].definition_raw
        closure[name] = raw
        frontier.extend(tok for tok in _TOKEN_RE.findall(raw)
                        if tok in facts and tok not in closure)
    return closure


def matrix_provenance() -> dict:
    """Recorded-input provenance for the CURRENT-STATE interaction matrix."""
    pairs = sorted(matrix_pairs())
    seeds = sorted({MATRIX_ROOT_NETWORK} | {r for p in pairs for r in p})
    closure = definition_closure(seeds)
    definitions_sha = hashlib.sha256(json.dumps(
        closure, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()
    payload = {
        "harness_sha256": hashlib.sha256(HARNESS.read_bytes()).hexdigest(),
        "earlier_stages": MATRIX_EARLIER_STAGES,
        "later_stages": MATRIX_LATER_STAGES,
        "pair_count": len(pairs),
        "pairs_sha256": hashlib.sha256(
            "\n".join(f"{e}\t{l}" for e, l in pairs).encode("utf-8")).hexdigest(),
        "definitions_sha256": definitions_sha,
        "definition_networks": len(closure),
    }
    payload["provenance_sha256"] = hashlib.sha256(json.dumps(
        payload, sort_keys=True).encode("utf-8")).hexdigest()
    return payload


def write_matrix_provenance() -> None:
    payload = matrix_provenance()
    payload["generator"] = "Germanic/tools/artifact_graph.py"
    payload["note"] = ("CURRENT-STATE analysis: hash covers harness source, "
                       "stage-derived pair list, and the executable_facts "
                       "definition closure; pure cascade reorders do not "
                       "invalidate it, rule edits do.")
    MATRIX_PROVENANCE.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _matrix_verify() -> list:
    if not MATRIX.is_file():
        return [f"missing {_rel(MATRIX)}; {REFRESH_HINT}"]
    if not MATRIX_PROVENANCE.is_file():
        return [f"missing {_rel(MATRIX_PROVENANCE)} (matrix has no recorded "
                f"input provenance); {REFRESH_HINT}"]
    recorded = json.loads(MATRIX_PROVENANCE.read_text(encoding="utf-8"))
    expected = matrix_provenance()
    if recorded.get("provenance_sha256") != expected["provenance_sha256"]:
        return [f"interaction matrix stale: recorded provenance in "
                f"{_rel(MATRIX_PROVENANCE)} does not match the live harness/"
                f"pair-list/rule-definition state; {REFRESH_HINT}"]
    # the matrix rows must cover exactly the stage-derived pair list
    rows = [line.split("\t") for line in
            MATRIX.read_text(encoding="utf-8").splitlines()[1:] if line]
    matrix_pair_set = {(r[0], r[1]) for r in rows}
    if matrix_pair_set != set(matrix_pairs()):
        return [f"interaction matrix rows disagree with the stage-derived "
                f"pair cross-product; {REFRESH_HINT}"]
    return []


def _matrix_build() -> list:
    result = run_in_runner(
        "python3 tools/cascade_interaction_harness.py --progress")
    if result.returncode != 0:
        raise GraphError(
            f"cascade_interaction_harness.py exited {result.returncode}")
    write_matrix_provenance()
    return [_rel(MATRIX), _rel(MATRIX_PROVENANCE)]


def _runtime(name: str, authority: str, verify, build) -> Node:
    return Node(name, "runtime", authority, verify, build)


# --------------------------------------------------------------------------
# the graph
# --------------------------------------------------------------------------

def nodes() -> tuple:
    return (
        _projection("executable_order",
                    "Germanic/fsts/germanic.txt via oe_pipeline",
                    _render_executable_order),
        _projection("oe_sandbox",
                    "Germanic/fsts/germanic.txt via oe_pipeline.sandbox_text",
                    _render_oe_sandbox),
        _runtime("runtime_bins",
                 "container foma build of fsts/old_english_sandbox.txt",
                 _bins_verify, _bins_build),
        _runtime("full_trace",
                 "container oe_full_trace_report.py --all over fresh bins",
                 _trace_verify, _trace_build),
        _projection("registry_views",
                    "registry SOURCE TSVs via generate_registry_views",
                    generate_registry_views.build_all),
        _projection("coverage_census",
                    "committed full trace + registry via rule_coverage_census",
                    _render_census),
        _projection("reader_book",
                    "reader SOURCE files + reader_manifest.tsv via "
                    "build_reader_book",
                    build_reader_book.render),
        _projection("book_draft",
                    "assembly sources via build_capr_book_draft",
                    _render_book_draft),
        _regen_index_verborum(),
        _runtime("interaction_matrix",
                 "container cascade_interaction_harness.py over the live "
                 "stage-derived pair list",
                 _matrix_verify, _matrix_build),
    )


# census reads the inventory view and the views annotate from the census, so
# these two projections are refreshed to a joint fixed point.
_FIXED_POINT = ("registry_views", "coverage_census")
_MAX_FIXED_POINT_PASSES = 4


def refresh(printer: Callable[[str], None] = print,
            force: frozenset = frozenset()) -> list:
    """Bring every node up to date; returns the list of changes made.

    Runtime nodes named in ``force`` are rebuilt unconditionally (used by
    the adjudication evidence step, which always re-derives stage bins).
    Raises GraphError with an authority-tied message on any failure.
    """
    changed: list = []
    graph = {n.name: n for n in nodes()}
    order = [n.name for n in nodes()]

    def run(node: Node) -> None:
        if node.kind == "runtime":
            problems = [] if node.name in force else node.verify()
            if not problems and node.name not in force:
                printer(f"  {node.name}: fresh (recorded provenance matches)")
                return
            for p in problems:
                printer(f"  {node.name}: {p}")
            printer(f"  {node.name}: rebuilding (container runtime) ...")
            for item in node.build():
                changed.append(f"{node.name}: {item}")
                printer(f"    rebuilt {item}")
            remaining = node.verify()
            if remaining:
                raise GraphError(
                    f"{node.name} still stale after rebuild: {remaining[0]}")
        else:
            for item in node.build():
                changed.append(f"{node.name}: {item}")
                printer(f"  {node.name}: wrote {item}")

    for name in order:
        if name in _FIXED_POINT:
            continue  # handled jointly below, in cascade position
        if name == "reader_book":
            # fixed point runs immediately before the reader chain
            for _ in range(_MAX_FIXED_POINT_PASSES):
                pass_changed = len(changed)
                for fp_name in _FIXED_POINT:
                    run(graph[fp_name])
                if len(changed) == pass_changed:
                    break
            else:
                raise GraphError(
                    "registry_views/coverage_census did not reach a fixed "
                    "point; a generator is nondeterministic")
        run(graph[name])
    return changed


def verify_all() -> list:
    problems: list = []
    for node in nodes():
        problems.extend(node.verify())
    return problems


def main() -> int:
    args = sys.argv[1:]
    if args == ["--check"]:
        problems = verify_all()
        for p in problems:
            print(f"STALE: {p}", file=sys.stderr)
        if problems:
            return 1
        print("CONTROL PLANE CLEAN")
        return 0
    if args == ["--refresh"]:
        try:
            refresh()
        except GraphError as exc:
            print(f"REFRESH FAILED: {exc}", file=sys.stderr)
            return 1
        problems = verify_all()
        if problems:
            for p in problems:
                print(f"STALE AFTER REFRESH: {p}", file=sys.stderr)
            return 1
        print("CONTROL PLANE CLEAN")
        return 0
    print(__doc__.strip(), file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
