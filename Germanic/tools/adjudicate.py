#!/usr/bin/env python3
"""Narrow adjudication interface for one SC.

    python3 Germanic/tools/adjudicate.py --next
        Report the next SC to adjudicate, derived from the canonical
        registry (first active SC after the highest adjudicated SC).

    python3 Germanic/tools/adjudicate.py SC024 --prepare
        Assemble a compact packet from canonical sources: registry row, rule
        text and executable position, chronology relations and witnesses,
        an explicit registry-driven reading list (required sources, existing
        adjudication, chronology evidence, publication prose, historical
        support), frozen fingerprints, and the standard commands.

    python3 Germanic/tools/adjudicate.py SC024 --evidence
        Deterministically gather the executable (runtime) evidence: first
        regenerate the purely mechanical prerequisites (derived registry
        cascade positions, executable manifests, generated sandbox,
        chronology-card positions), then rebuild
        the full OE cascade and every stage bin from
        Germanic/fsts/old_english_sandbox.txt inside the backend container,
        write the build manifest, prove production-vs-generated-sandbox
        semantic equivalence over the full selected corpus, regenerate the
        canonical full trace report if it is stale, and print the complete
        live firing census for the SC's executable rule (lexeme, protoform,
        form immediately before the rule, form immediately after), plus
        before/after lines for the SC's chronology witnesses. No manual
        foma/flookup work is ever needed.

    python3 Germanic/tools/adjudicate.py SC024 --finalize
        Deterministic host-side finalization: sync derived registry columns
        (cascade_position) from the executable model, regenerate all registry
        views and chained model projections (order manifest, generated
        sandbox, chronology-card positions, coverage census), then run the
        propagation consistency checks. Never fabricates runtime evidence
        (the census fails closed on stale trace evidence — run --evidence
        first) and never rewrites ARCHIVE/FROZEN snapshots. Run after
        editing SOURCE files.

    python3 Germanic/tools/adjudicate.py SC024 --check
        Validate propagation consistency only (no regeneration).

Canonical sources read: registry/sc_registry.tsv, registry/chronology_edges.tsv,
registry/sc_inventory_notes.tsv, Germanic/fsts/germanic.txt,
cascade_baseline/cascade_order_manifest.tsv,
cascade_baseline/cascade_baseline_summary.json. Archive files are never read.
"""

from __future__ import annotations

import json
import re
import shlex
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "Germanic/tools"))

from generate_registry_views import (  # noqa: E402
    ANNOTATIONS,
    EDGE_REGISTRY,
    SC_REGISTRY,
    VERDICT_VOCABULARY,
    build_all,
    read_tsv,
)

import oe_pipeline  # noqa: E402
from capr_runtime import layout, run_in_runner, write_build_manifest  # noqa: E402
from oe_full_trace_report import trace_provenance_problems  # noqa: E402

SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
FST = REPO_ROOT / "Germanic/fsts/germanic.txt"
SANDBOX_FST = REPO_ROOT / "Germanic/fsts/old_english_sandbox.txt"
# Runtime layout (authoritative bin dir, runner) comes from capr_runtime.
ORDER_MANIFEST = SC_DIR / "cascade_baseline/cascade_order_manifest.tsv"
BASELINE_SUMMARY = SC_DIR / "cascade_baseline/cascade_baseline_summary.json"
TEMPLATE = SC_DIR / "audits/ADJUDICATION_TEMPLATE.md"
PROTOCOL = REPO_ROOT / "Germanic/docs/RESEARCH_ADJUDICATION_PROTOCOL.md"
CHAINED_BUILDERS = (
    # Executable-order projections of the shared model (oe_pipeline):
    REPO_ROOT / "Germanic/tools/cascade_order_manifest.py",
    REPO_ROOT / "Germanic/tools/generate_oe_sandbox.py",
    REPO_ROOT / "Germanic/tools/sync_chronology_card_positions.py",
    # Reads the committed full trace report; fails closed if that runtime
    # evidence is stale (run --evidence first).
    REPO_ROOT / "Germanic/tools/rule_coverage_census.py",
)
# ARCHIVE/FROZEN artifacts (historical_audit_table.tsv,
# rename_migration_manifest.tsv) are deliberately NOT in the chain: frozen
# snapshots are never rewritten by finalization.

# Derived SOURCE-file columns synchronized from the executable model before
# any view regeneration (registry cascade_position is derived, not hand-edited).
DERIVED_COLUMN_SYNCS = (
    REPO_ROOT / "Germanic/tools/sync_registry_cascade_positions.py",
)

# Generated artifacts that must be clean before executable evidence is
# gathered and after finalization (fail-closed: never census stale order).
GENERATED_CHECKS = (
    ("sync_registry_cascade_positions.py", ["--check"]),
    ("cascade_order_manifest.py", ["--check"]),
    ("generate_oe_sandbox.py", ["--check"]),
    ("sync_chronology_card_positions.py", ["--check"]),
)

# Purely mechanical prerequisites for runtime evidence, regenerated
# automatically by --evidence before compiling (derived registry columns,
# executable manifests, generated sandbox, card positions). Never touches
# scientific SOURCE metadata beyond explicitly derived columns.
MECHANICAL_PREREQS = DERIVED_COLUMN_SYNCS + (
    REPO_ROOT / "Germanic/tools/cascade_order_manifest.py",
    REPO_ROOT / "Germanic/tools/generate_oe_sandbox.py",
    REPO_ROOT / "Germanic/tools/sync_chronology_card_positions.py",
)

# Canonical directories in which bare-filename registry pointers may live.
DOC_SEARCH_DIRS = (
    SC_DIR / "audits",
    SC_DIR / "book_dossiers",
    SC_DIR / "literature_dossiers",
    SC_DIR / "reader_facing",
    SC_DIR / "order_tests/chronology_cards",
    REPO_ROOT / "Germanic/docs",
    SC_DIR,
)

VERDICT_LINE_RE = re.compile(r"^Registry-verdict:\s*(.+)$", re.MULTILINE)


def load_registry_row(sc_id):
    for row in read_tsv(SC_REGISTRY):
        if row["sc_id"] == sc_id:
            return row
    return None


def load_annotation_row(sc_id):
    for row in read_tsv(ANNOTATIONS):
        if row["change_id"] == sc_id:
            return row
    return None


def find_rule(fst_identifier):
    if not fst_identifier:
        return None, None
    for lineno, line in enumerate(FST.read_text(encoding="utf-8").splitlines(), 1):
        if re.match(rf"\s*define\s+{re.escape(fst_identifier)}\b", line):
            return lineno, line.strip()
    return None, None


def edges_for(sc_id):
    return [
        e
        for e in read_tsv(EDGE_REGISTRY)
        if sc_id in (e["source_change_id"], e["target_change_id"])
    ]


def resolve_doc(ref):
    """Resolve one registry document pointer to a repo-relative Path.

    A pointer containing '/' is repo-relative; a bare filename is looked up
    in the canonical document directories. Returns None if unresolvable.
    """
    ref = ref.strip()
    if not ref:
        return None
    if "/" in ref:
        p = REPO_ROOT / ref
        return p.relative_to(REPO_ROOT) if p.is_file() else None
    for d in DOC_SEARCH_DIRS:
        p = d / ref
        if p.is_file():
            return p.relative_to(REPO_ROOT)
    return None


def split_refs(value):
    return [part.strip() for part in value.split(";") if part.strip()]


def reading_list(row, ann):
    """Build the registry-driven reading list for one SC.

    Returns (sections, warnings) where sections is an ordered dict of
    section title -> list of repo-relative path strings, and warnings lists
    registry pointers that failed to resolve. No filename guessing: every
    entry comes from an explicit canonical registry/annotation field.
    """
    sections = {
        "REQUIRED CURRENT SOURCES": [],
        "EXISTING ADJUDICATION": [],
        "CHRONOLOGY EVIDENCE": [],
        "PUBLICATION PROSE (inspect/update after verdict)": [],
        "OPTIONAL / HISTORICAL SUPPORT": [],
    }
    warnings = []

    def add(section, ref):
        p = resolve_doc(ref)
        if p is None:
            warnings.append(f"unresolvable registry pointer: {ref!r}")
            return
        s = str(p)
        if s not in sections[section]:
            sections[section].append(s)

    if ann and ann.get("rule_source_path"):
        anchor = ann.get("rule_source_anchor", "")
        entry = ann["rule_source_path"] + (f"  ({anchor})" if anchor else "")
        sections["REQUIRED CURRENT SOURCES"].append(entry)
    for ref in split_refs(row.get("capr_evidence", "")):
        p = resolve_doc(ref)
        if p is None:
            warnings.append(f"unresolvable registry pointer: {ref!r}")
            continue
        parent = p.parts[-2] if len(p.parts) > 1 else ""
        if parent == "literature_dossiers":
            section = "OPTIONAL / HISTORICAL SUPPORT"
        elif parent in ("book_dossiers", "reader_facing"):
            section = "PUBLICATION PROSE (inspect/update after verdict)"
            # Grouped book dossiers are also primary CAPR evidence.
            if str(p) not in sections["REQUIRED CURRENT SOURCES"]:
                sections["REQUIRED CURRENT SOURCES"].append(str(p))
        else:
            section = "REQUIRED CURRENT SOURCES"
        if str(p) not in sections[section]:
            sections[section].append(str(p))
    if row.get("adjudication_memo"):
        add("EXISTING ADJUDICATION", row["adjudication_memo"])
    if row.get("chronology_card"):
        add("CHRONOLOGY EVIDENCE", row["chronology_card"])
    if row.get("source_reader_facing_file"):
        add("PUBLICATION PROSE (inspect/update after verdict)",
            row["source_reader_facing_file"])
    return sections, warnings


def sc_num(sc_id):
    return int(sc_id[2:5])


def next_sc():
    """Next SC to adjudicate: first active, unadjudicated SC after the
    contiguous run of adjudicated SCs in the canonical registry.

    Out-of-band identities adjudicated ahead of sequence (e.g. SC101,
    created and settled by the SC024 e1-complex split) must not raise
    the threshold past the pending mainline SCs: the threshold is the
    highest end of a contiguous adjudicated run that still has pending
    SCs above it, not the global maximum."""
    rows = read_tsv(SC_REGISTRY)
    adjudicated = sorted(
        sc_num(r["sc_id"]) for r in rows if r["adjudication_status"] == "adjudicated"
    )
    # Ends of each contiguous adjudicated run, e.g. {16,17,23,24,25,101}
    # -> [17, 25, 101].
    run_ends = [
        n
        for i, n in enumerate(adjudicated)
        if i + 1 == len(adjudicated) or adjudicated[i + 1] != n + 1
    ]
    pending = sorted(
        (sc_num(r["sc_id"]), r["sc_id"])
        for r in rows
        if r["lifecycle_status"] == "active"
        and r["adjudication_status"] != "adjudicated"
    )
    for threshold in reversed(run_ends or [0]):
        candidates = [(n, sc) for n, sc in pending if n > threshold]
        if candidates:
            return candidates[0][1]
    return pending[0][1] if pending and not run_ends else None


def run_generated_checks() -> list:
    """Run the --check mode of every generated-artifact builder."""
    failures = []
    for script, extra in GENERATED_CHECKS:
        result = subprocess.run(
            [sys.executable, str(REPO_ROOT / "Germanic/tools" / script), *extra],
            cwd=REPO_ROOT, capture_output=True, text=True)
        if result.returncode != 0:
            detail = (result.stderr or result.stdout).strip().splitlines()
            failures.append(f"{script}: {detail[-1] if detail else 'stale'}")
    return failures


def evidence(sc_id) -> int:
    """Deterministically gather the executable evidence for one SC.

    Fails loudly at every step; never falls back to stale artifacts.
    """
    row = load_registry_row(sc_id)
    if row is None:
        print(f"{sc_id} not found in {SC_REGISTRY.relative_to(REPO_ROOT)}", file=sys.stderr)
        return 1
    ident = row["fst_identifier"]
    if not ident:
        print(f"EVIDENCE FAILED: {sc_id} has no executable fst_identifier in the "
              f"registry (lifecycle: {row['lifecycle_status']}); there is no live "
              "rule to census.", file=sys.stderr)
        return 1
    edges = edges_for(sc_id)
    witnesses = "; ".join(
        w for e in edges for w in split_refs(e["representative_lexemes"]))

    print(f"# Executable evidence: {sc_id} ({ident})")
    print("\n## Chronology relations and witnesses (canonical edge registry)")
    if not edges:
        print("- none recorded")
    for e in edges:
        print(f"- {e['source_change_id']} -> {e['target_change_id']} "
              f"[{e['relation_type']}; {e['evidence_basis']}; "
              f"role: {e['witness_role'] or '-'}]")
        if e["representative_lexemes"]:
            print(f"  witnesses: {e['representative_lexemes']}")
        if e["representative_forms"]:
            print(f"  forms: {e['representative_forms']}")

    # Regenerate the mechanical prerequisites of runtime evidence in place
    # (§ ordinary workflow: --evidence, --finalize, tests — no bounce cycle).
    print("\n## Regenerating mechanical prerequisites (model projections) ...")
    for builder in MECHANICAL_PREREQS:
        result = subprocess.run(
            [sys.executable, str(builder)], cwd=REPO_ROOT,
            capture_output=True, text=True)
        tail = (result.stdout or result.stderr).strip().splitlines()
        print(f"{builder.name}: {tail[-1] if tail else 'ok'}")
        if result.returncode != 0:
            print(result.stderr, file=sys.stderr)
            print(f"EVIDENCE FAILED: {builder.name} exited {result.returncode}",
                  file=sys.stderr)
            return 1
    stale = run_generated_checks()
    if stale:
        for s in stale:
            print(f"EVIDENCE FAILED (stale generated artifact): {s}",
                  file=sys.stderr)
        print("A generated artifact stayed stale after regeneration; fix the "
              "generator before gathering evidence.", file=sys.stderr)
        return 1
    if not SANDBOX_FST.is_file():
        print(f"EVIDENCE FAILED: missing {SANDBOX_FST}", file=sys.stderr)
        return 1
    try:
        clock = run_in_runner("date +%s", capture_output=True, text=True)
    except RuntimeError as exc:
        print(f"EVIDENCE FAILED: {exc}", file=sys.stderr)
        return 1
    if clock.returncode != 0:
        print(clock.stderr, file=sys.stderr)
        print("EVIDENCE FAILED: backend container is not reachable "
              "(is `docker compose up -d` running?)", file=sys.stderr)
        return 1
    min_mtime = int(clock.stdout.strip())

    print("\n## Rebuilding full cascade + stage bins "
          "(fsts/old_english_sandbox.txt sources fsts/germanic.txt) ...")
    rebuild = run_in_runner("foma -q -l fsts/old_english_sandbox.txt -e quit",
                            capture_output=True, text=True)
    if rebuild.returncode != 0:
        print(rebuild.stdout, file=sys.stderr)
        print(rebuild.stderr, file=sys.stderr)
        print("EVIDENCE FAILED: foma rebuild exited "
              f"{rebuild.returncode}", file=sys.stderr)
        return 1
    tail = [l for l in rebuild.stdout.splitlines() if l.strip()][-3:]
    for line in tail:
        print(f"  {line}")
    manifest_path = write_build_manifest(
        oe_pipeline.expected_snapshot_bins() + ["old_english.bin"])
    print(f"rebuild ok; build manifest: {manifest_path}")

    print("\n## Production vs generated-sandbox semantic equivalence")
    sys.stdout.flush()
    equiv = run_in_runner("python3 tools/check_production_sandbox_equivalence.py")
    if equiv.returncode != 0:
        print("EVIDENCE FAILED: production/sandbox semantic equivalence check "
              f"exited {equiv.returncode}", file=sys.stderr)
        return 1

    # Canonical full trace: runtime-derived upstream evidence for the
    # coverage census. Regenerate only when stale (~16 min when needed).
    trace_path = REPO_ROOT / "Germanic/docs/debug_snapshots/oe_full_trace_report.txt"
    trace_problems = (trace_provenance_problems(
        trace_path.read_text(encoding="utf-8"))
        if trace_path.is_file() else ["missing canonical full trace report"])
    if trace_problems:
        print("\n## Canonical full trace is stale; regenerating from the "
              "validated bins (~16 min) ...")
        for problem in trace_problems:
            print(f"  - {problem}")
        sys.stdout.flush()
        trace = run_in_runner("python3 tools/oe_full_trace_report.py --all")
        if trace.returncode != 0:
            print(f"EVIDENCE FAILED: trace report exited {trace.returncode}",
                  file=sys.stderr)
            return 1
    else:
        print("\n## Canonical full trace is fresh; skipping regeneration")

    print("\n## Firing census (fresh stage bins only)")
    sys.stdout.flush()
    inner = f"python3 tools/sc_evidence.py {shlex.quote(ident)} --min-mtime {min_mtime}"
    if witnesses:
        inner += f" --witnesses {shlex.quote(witnesses)}"
    census = run_in_runner(inner)
    if census.returncode != 0:
        print(f"EVIDENCE FAILED: census exited {census.returncode}", file=sys.stderr)
        return 1
    return 0


def prepare(sc_id) -> int:
    row = load_registry_row(sc_id)
    if row is None:
        print(f"{sc_id} not found in {SC_REGISTRY.relative_to(REPO_ROOT)}", file=sys.stderr)
        return 1
    print(f"# Adjudication packet: {sc_id}")
    print(f"\n## Protocol\nFollow {PROTOCOL.relative_to(REPO_ROOT)} and fill "
          f"{TEMPLATE.relative_to(REPO_ROOT)} (copy to "
          f"Germanic/docs/sound_changes/audits/{sc_id.lower()}-adjudication.md).")
    print("\n## Registry row (canonical metadata)")
    for key, value in row.items():
        if value:
            print(f"- {key}: {value}")
    print("\n## Executable rule")
    lineno, text = find_rule(row["fst_identifier"])
    if lineno:
        print(f"- {row['fst_identifier']} at Germanic/fsts/germanic.txt line {lineno}:")
        print(f"  {text}")
        manifest = {r["foma_identifier"]: r["position"] for r in read_tsv(ORDER_MANIFEST)}
        pos = manifest.get(row["fst_identifier"])
        if pos:
            print(f"- executable cascade position (order manifest): {pos}")
    else:
        print(f"- no live `define {row['fst_identifier'] or '?'}` in germanic.txt "
              f"(lifecycle: {row['lifecycle_status']})")
    print("\n## Chronology relations (canonical edge registry)")
    edges = edges_for(sc_id)
    if not edges:
        print("- none recorded")
    for e in edges:
        print(f"- {e['source_change_id']} -> {e['target_change_id']} "
              f"[{e['relation_type']}; {e['evidence_basis']}; role: {e['witness_role'] or '-'}] "
              f"lexemes: {e['representative_lexemes'] or '-'}")
    print("\n## Reading list (registry-driven; no repository searching needed)")
    sections, warnings = reading_list(row, load_annotation_row(sc_id))
    for title, entries in sections.items():
        print(f"\n### {title}")
        if not entries:
            print("- (none recorded)")
        for entry in entries:
            print(f"- {entry}")
    for w in warnings:
        print(f"WARNING: {w}", file=sys.stderr)
    print("\n## Frozen fingerprints (observations, not goals)")
    summary = json.loads(BASELINE_SUMMARY.read_text(encoding="utf-8"))
    print(f"- expanded-{summary['total_lexemes']}: {summary['outputs_sha256']}")
    print(f"- legacy-{summary['legacy_subset_count']}: {summary['legacy_subset_sha256']}")
    print("\n## Standard commands")
    print(f"- executable evidence (rebuild + firing census): "
          f"python3 Germanic/tools/adjudicate.py {sc_id} --evidence")
    print(f"- finalize after SOURCE edits: python3 Germanic/tools/adjudicate.py {sc_id} --finalize")
    print("- full suite: cd Germanic/tests && python3 -m pytest -q")
    print("All container FST work (rebuild, freshness checks, firing census, "
          "witness pre/post) is encapsulated by --evidence; never compile or "
          "probe transducers by hand.")
    return 0


def finalize(sc_id) -> int:
    """Deterministic host-side finalization: regenerate projections, then check.

    Always runs the full regeneration chain — the agent never decides
    whether 'staging changed'. All generators are deterministic and safe to
    run unconditionally. Order: derived SOURCE columns are synchronized from
    the executable model first, then registry views, then chained projections.
    Runtime-derived evidence is never fabricated here: rule_coverage_census
    fails closed on stale trace evidence with an instruction to run
    --evidence first, and ARCHIVE/FROZEN snapshots are never rewritten.
    """
    print("== syncing derived registry columns (from the executable model) ==")
    for builder in DERIVED_COLUMN_SYNCS:
        result = subprocess.run(
            [sys.executable, str(builder)], cwd=REPO_ROOT,
            capture_output=True, text=True,
        )
        tail = (result.stdout or result.stderr).strip().splitlines()
        print(f"{builder.name}: {tail[-1] if tail else 'ok'}")
        if result.returncode != 0:
            print(result.stderr, file=sys.stderr)
            print(f"FINALIZE FAILED: {builder.name} exited {result.returncode}",
                  file=sys.stderr)
            return 1
    print("== regenerating registry views ==")
    for path, text in build_all().items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != text:
            path.write_text(text, encoding="utf-8")
            print(f"wrote {path.relative_to(REPO_ROOT)}")
    print("== rebuilding chained artifacts ==")
    for builder in CHAINED_BUILDERS:
        result = subprocess.run(
            [sys.executable, str(builder)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        tail = (result.stdout or result.stderr).strip().splitlines()
        print(f"{builder.name}: {tail[-1] if tail else 'ok'}")
        if result.returncode != 0:
            print(result.stderr, file=sys.stderr)
            print(f"FINALIZE FAILED: {builder.name} exited {result.returncode}",
                  file=sys.stderr)
            return 1
    print("== propagation checks ==")
    return check(sc_id)


def check(sc_id) -> int:
    errors = []
    row = load_registry_row(sc_id)
    if row is None:
        print(f"{sc_id} not found in registry", file=sys.stderr)
        return 1
    if row["adjudication_status"] != "adjudicated":
        errors.append(f"registry adjudication_status is {row['adjudication_status']!r}, not 'adjudicated'")
    verdict = row["verdict"]
    if not verdict:
        errors.append("registry verdict is empty")
    else:
        for token in verdict.split("/"):
            if token not in VERDICT_VOCABULARY:
                errors.append(f"verdict token {token!r} not in controlled vocabulary")
    memo_rel = row["adjudication_memo"]
    if not memo_rel:
        errors.append("registry adjudication_memo is empty")
    else:
        memo_path = REPO_ROOT / memo_rel
        if not memo_path.is_file():
            errors.append(f"memo missing: {memo_rel}")
        else:
            text = memo_path.read_text(encoding="utf-8")
            match = VERDICT_LINE_RE.search(text)
            if not match:
                errors.append(f"memo {memo_rel} has no 'Registry-verdict:' line")
            else:
                declared = dict(
                    part.split("=", 1)
                    for part in (p.strip() for p in match.group(1).split(";"))
                    if "=" in part
                )
                if declared.get(sc_id) != verdict:
                    errors.append(
                        f"memo Registry-verdict {declared.get(sc_id)!r} != registry verdict {verdict!r}"
                    )
    if "RETIRE" in (verdict or ""):
        if row["lifecycle_status"] != "retired":
            errors.append("verdict RETIRE but lifecycle_status is not 'retired'")
    if row["lifecycle_status"] == "retired":
        lineno, _ = find_rule(row["fst_identifier"])
        if lineno:
            errors.append(
                f"retired SC still has a live define {row['fst_identifier']} "
                f"at germanic.txt line {lineno}"
            )
    # registry structured position must match the executable model
    if row["lifecycle_status"] == "active" and row["fst_identifier"]:
        model_pos = oe_pipeline.cascade_position(row["fst_identifier"])
        if str(model_pos) != row["cascade_position"]:
            errors.append(
                f"registry cascade_position {row['cascade_position']!r} != "
                f"executable model position {model_pos!r} for "
                f"{row['fst_identifier']}")
    # generated views must be clean
    for path, expected in build_all().items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != expected:
            errors.append(f"stale generated view: {path.relative_to(REPO_ROOT)} — "
                          "run generate_registry_views.py")
    for stale_item in run_generated_checks():
        errors.append(f"stale generated artifact: {stale_item}")
    if errors:
        for e in errors:
            print(f"CHECK FAILED: {e}", file=sys.stderr)
        return 1
    print(f"{sc_id}: propagation checks passed. Remember: cd Germanic/tests && python3 -m pytest -q")
    return 0


def main() -> int:
    args = sys.argv[1:]
    if args == ["--next"]:
        nxt = next_sc()
        if nxt is None:
            print("no unadjudicated active SC remains after the highest adjudicated SC")
            return 1
        print(nxt)
        return 0
    if (len(args) != 2
            or args[1] not in ("--prepare", "--check", "--finalize", "--evidence")
            or not re.fullmatch(r"SC\d{3}", args[0])):
        print(__doc__.strip(), file=sys.stderr)
        return 2
    sc_id, mode = args
    if mode == "--prepare":
        return prepare(sc_id)
    if mode == "--evidence":
        return evidence(sc_id)
    if mode == "--finalize":
        return finalize(sc_id)
    return check(sc_id)


if __name__ == "__main__":
    raise SystemExit(main())
