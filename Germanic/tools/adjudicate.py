#!/usr/bin/env python3
"""Narrow adjudication interface for one SC.

    python3 Germanic/tools/adjudicate.py SC024 --prepare
        Assemble a compact packet from canonical sources: registry row, rule
        text and executable position, chronology relations and witnesses,
        existing memo/dossiers, frozen fingerprints, and the commands needed
        for tracing/census work.

    python3 Germanic/tools/adjudicate.py SC024 --check
        Validate that a completed adjudication has been propagated
        consistently before commit.

Canonical sources read: registry/sc_registry.tsv, registry/chronology_edges.tsv,
Germanic/fsts/germanic.txt, cascade_baseline/cascade_order_manifest.tsv,
cascade_baseline/cascade_baseline_summary.json. Archive files are never read.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "Germanic/tools"))

from generate_registry_views import (  # noqa: E402
    EDGE_REGISTRY,
    SC_REGISTRY,
    VERDICT_VOCABULARY,
    build_all,
    read_tsv,
)

SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
FST = REPO_ROOT / "Germanic/fsts/germanic.txt"
ORDER_MANIFEST = SC_DIR / "cascade_baseline/cascade_order_manifest.tsv"
BASELINE_SUMMARY = SC_DIR / "cascade_baseline/cascade_baseline_summary.json"
TEMPLATE = SC_DIR / "audits/ADJUDICATION_TEMPLATE.md"
PROTOCOL = REPO_ROOT / "Germanic/docs/RESEARCH_ADJUDICATION_PROTOCOL.md"

VERDICT_LINE_RE = re.compile(r"^Registry-verdict:\s*(.+)$", re.MULTILINE)


def load_registry_row(sc_id):
    for row in read_tsv(SC_REGISTRY):
        if row["sc_id"] == sc_id:
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


def related_documents(sc_id):
    num = sc_id.lower()
    hits = []
    for base in (SC_DIR / "audits", REPO_ROOT / "Germanic/docs",
                 SC_DIR / "book_dossiers", SC_DIR / "literature_dossiers"):
        if not base.is_dir():
            continue
        for p in sorted(base.glob("*.md")):
            if num in p.name.lower():
                hits.append(p.relative_to(REPO_ROOT))
    return hits


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
    print("\n## Existing memo / related documents")
    memo = row["adjudication_memo"]
    print(f"- memo: {memo or '(none yet)'}")
    for p in related_documents(sc_id):
        print(f"- related: {p}")
    print("\n## Frozen fingerprints (observations, not goals)")
    summary = json.loads(BASELINE_SUMMARY.read_text(encoding="utf-8"))
    print(f"- expanded-{summary['total_lexemes']}: {summary['outputs_sha256']}")
    print(f"- legacy-{summary['legacy_subset_count']}: {summary['legacy_subset_sha256']}")
    print("\n## Standard commands")
    print("- compile FST (in container): docker compose exec -T backend bash -lc "
          "'cd /usr/app && foma -q -l fsts/germanic.txt -e quit'")
    print("- firing census / traces (in container): docker compose exec -T backend "
          "python3 /usr/app/tools/oe_full_trace_report.py  (see protocol step 3-4)")
    print("- regenerate views after registry edits: python3 Germanic/tools/generate_registry_views.py")
    print(f"- validate propagation: python3 Germanic/tools/adjudicate.py {sc_id} --check")
    print("- full suite: cd Germanic/tests && python3 -m pytest -q")
    return 0


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
    if len(args) != 2 or args[1] not in ("--prepare", "--check") or not re.fullmatch(r"SC\d{3}", args[0]):
        print(__doc__.strip(), file=sys.stderr)
        return 2
    sc_id, mode = args
    return prepare(sc_id) if mode == "--prepare" else check(sc_id)


if __name__ == "__main__":
    raise SystemExit(main())
