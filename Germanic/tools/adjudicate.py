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
        Deterministically gather the executable evidence: rebuild the full
        OE cascade and every stage bin from Germanic/fsts/old_english_sandbox.txt
        inside the backend container, verify bin freshness against the
        rebuild timestamp, and print the complete live firing census for the
        SC's executable rule (lexeme, protoform, form immediately before the
        rule, form immediately after), plus before/after lines for the SC's
        chronology witnesses. No manual foma/flookup work is ever needed.

    python3 Germanic/tools/adjudicate.py SC024 --finalize
        Deterministic finalization: regenerate all registry views, rebuild
        the chained audit-table and rename-manifest artifacts, then run the
        propagation consistency checks. Run this after editing SOURCE files.

    python3 Germanic/tools/adjudicate.py SC024 --check
        Validate propagation consistency only (no regeneration).

Canonical sources read: registry/sc_registry.tsv, registry/chronology_edges.tsv,
registry/sc_inventory_annotations.tsv, Germanic/fsts/germanic.txt,
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

SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
FST = REPO_ROOT / "Germanic/fsts/germanic.txt"
SANDBOX_FST = REPO_ROOT / "Germanic/fsts/old_english_sandbox.txt"
# Canonical container layout (docker-compose.yml): ./backend -> /usr/app,
# ./Germanic/{data,fsts,tools,docs} -> /usr/app/{data,fsts,tools,docs}.
# foma writes compiled bins into its working directory, so the ONLY
# authoritative bin location is /usr/app (host: backend/). Bins found under
# fsts/ are stale duplicates and are never read.
CONTAINER_APP = "/usr/app"
ORDER_MANIFEST = SC_DIR / "cascade_baseline/cascade_order_manifest.tsv"
BASELINE_SUMMARY = SC_DIR / "cascade_baseline/cascade_baseline_summary.json"
TEMPLATE = SC_DIR / "audits/ADJUDICATION_TEMPLATE.md"
PROTOCOL = REPO_ROOT / "Germanic/docs/RESEARCH_ADJUDICATION_PROTOCOL.md"
CHAINED_BUILDERS = (
    REPO_ROOT / "Germanic/tools/build_historical_audit_table.py",
    REPO_ROOT / "Germanic/tools/build_rename_migration_manifest.py",
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
    highest adjudicated SC in the canonical registry."""
    rows = read_tsv(SC_REGISTRY)
    threshold = max(
        (sc_num(r["sc_id"]) for r in rows if r["adjudication_status"] == "adjudicated"),
        default=0,
    )
    candidates = sorted(
        (sc_num(r["sc_id"]), r["sc_id"])
        for r in rows
        if r["lifecycle_status"] == "active"
        and r["adjudication_status"] != "adjudicated"
        and sc_num(r["sc_id"]) > threshold
    )
    return candidates[0][1] if candidates else None


def container_command(inner):
    """Wrap a shell command for the backend container (canonical layout)."""
    return ["docker", "compose", "exec", "-T", "backend", "sh", "-lc", inner]


def evidence_rebuild_command():
    """Command that rebuilds ALL executable evidence artifacts.

    old_english_sandbox.txt begins with `source fsts/germanic.txt`, so this
    single deterministic compile rebuilds the full OE cascade AND every
    stage-by-stage sandbox bin, writing them into the canonical bin
    directory (the foma working directory, /usr/app).
    """
    return container_command(
        f"cd {CONTAINER_APP} && foma -q -l fsts/old_english_sandbox.txt -e quit"
    )


def evidence_census_command(fst_identifier, min_mtime, witnesses):
    inner = (f"cd {CONTAINER_APP} && python3 tools/sc_evidence.py "
             f"{shlex.quote(fst_identifier)}")
    if min_mtime is not None:
        inner += f" --min-mtime {int(min_mtime)}"
    if witnesses:
        inner += f" --witnesses {shlex.quote(witnesses)}"
    return container_command(inner)


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

    if not SANDBOX_FST.is_file():
        print(f"EVIDENCE FAILED: missing {SANDBOX_FST}", file=sys.stderr)
        return 1
    clock = subprocess.run(container_command("date +%s"),
                           cwd=REPO_ROOT, capture_output=True, text=True)
    if clock.returncode != 0:
        print(clock.stderr, file=sys.stderr)
        print("EVIDENCE FAILED: backend container is not reachable "
              "(is `docker compose up -d` running?)", file=sys.stderr)
        return 1
    min_mtime = int(clock.stdout.strip())

    print("\n## Rebuilding full cascade + stage bins "
          "(fsts/old_english_sandbox.txt sources fsts/germanic.txt) ...")
    rebuild = subprocess.run(evidence_rebuild_command(),
                             cwd=REPO_ROOT, capture_output=True, text=True)
    if rebuild.returncode != 0:
        print(rebuild.stdout, file=sys.stderr)
        print(rebuild.stderr, file=sys.stderr)
        print("EVIDENCE FAILED: foma rebuild exited "
              f"{rebuild.returncode}", file=sys.stderr)
        return 1
    tail = [l for l in rebuild.stdout.splitlines() if l.strip()][-3:]
    for line in tail:
        print(f"  {line}")
    print("rebuild ok")

    print("\n## Firing census (fresh stage bins only)")
    sys.stdout.flush()
    census = subprocess.run(
        evidence_census_command(ident, min_mtime, witnesses), cwd=REPO_ROOT)
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
    """Deterministic finalization: regenerate everything, then check.

    Always runs the full regeneration chain — the agent never decides
    whether 'staging changed'. All generators are deterministic and safe
    to run unconditionally.
    """
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
    # generated views must be clean
    for path, expected in build_all().items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != expected:
            errors.append(f"stale generated view: {path.relative_to(REPO_ROOT)} — "
                          "run generate_registry_views.py")
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
