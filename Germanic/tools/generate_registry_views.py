#!/usr/bin/env python3
"""Regenerate all derived views from the canonical SC registries.

SOURCE (hand-edited):
    Germanic/docs/sound_changes/registry/sc_registry.tsv
    Germanic/docs/sound_changes/registry/sc_inventory_annotations.tsv
    Germanic/docs/sound_changes/registry/chronology_edges.tsv

GENERATED (never hand-edited; written by this script):
    Germanic/docs/sound_changes/sound_change_historical_staging_map.tsv
    Germanic/docs/sound_changes/sound_change_inventory.tsv
    Germanic/docs/sound_changes/order_tests/chronology_graph/first_break_edges.tsv
    Germanic/docs/sound_changes/order_tests/chronology_graph/first_break_edges.json
    Germanic/docs/sound_changes/order_tests/chronology_graph/first_break_edges.dot
    Germanic/docs/sound_changes/order_tests/chronology_graph/first_break_nodes.tsv
    Germanic/docs/sound_changes/order_tests/chronology_graph/first_break_graph_summary.md
    Germanic/docs/sound_changes/registry/settled_verdicts.md

Downstream generated files produced by their own existing builders (chained
from the staging-map view): cascade_baseline/historical_audit_table.tsv
(tools/build_historical_audit_table.py) and
cascade_baseline/rename_migration_manifest.tsv
(tools/build_rename_migration_manifest.py).

Usage:
    python3 Germanic/tools/generate_registry_views.py            # write views
    python3 Germanic/tools/generate_registry_views.py --check    # verify clean
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
REGISTRY_DIR = SC_DIR / "registry"
GRAPH_DIR = SC_DIR / "order_tests/chronology_graph"

SC_REGISTRY = REGISTRY_DIR / "sc_registry.tsv"
ANNOTATIONS = REGISTRY_DIR / "sc_inventory_annotations.tsv"
EDGE_REGISTRY = REGISTRY_DIR / "chronology_edges.tsv"

# The complete list of inputs this generator may read. Guardrail tests
# assert that no archived file can silently become a current-state input.
DECLARED_INPUTS = (SC_REGISTRY, ANNOTATIONS, EDGE_REGISTRY)

STAGING_VIEW = SC_DIR / "sound_change_historical_staging_map.tsv"
INVENTORY_VIEW = SC_DIR / "sound_change_inventory.tsv"
EDGES_TSV = GRAPH_DIR / "first_break_edges.tsv"
EDGES_JSON = GRAPH_DIR / "first_break_edges.json"
EDGES_DOT = GRAPH_DIR / "first_break_edges.dot"
NODES_TSV = GRAPH_DIR / "first_break_nodes.tsv"
GRAPH_SUMMARY = GRAPH_DIR / "first_break_graph_summary.md"
SETTLED_VERDICTS = REGISTRY_DIR / "settled_verdicts.md"

CHRONOLOGY_RELATION_TYPES = {
    "broad_far_chronology",
    "near_reciprocal_chronology",
    "one_sided_chronology",
    "reciprocal_chronology",
}

VERDICT_VOCABULARY = {
    "RETAIN", "REFORMULATE", "RESTRICT", "SPLIT", "RETIRE", "REORDER", "DEFER",
}


def read_tsv(path: Path):
    header = None
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        fields = line.split("\t")
        if header is None:
            header = fields
        else:
            rows.append(dict(zip(header, fields)))
    return rows


def tsv_text(banner_lines, header, rows):
    lines = [f"# {b}" if b else "#" for b in banner_lines]
    lines.append("\t".join(header))
    for row in rows:
        lines.append("\t".join(row))
    return "\n".join(lines) + "\n"


def banner(source_desc):
    return [
        "GENERATED FILE — DO NOT EDIT.",
        f"Source: {source_desc}",
        "Generator: Germanic/tools/generate_registry_views.py (run after editing sources).",
    ]


def validate_registry(reg, edges):
    errors = []
    counts = Counter(r["sc_id"] for r in reg)
    for sc, n in counts.items():
        if n != 1:
            errors.append(f"registry: {sc} appears {n} times")
    ids = set(counts)
    for r in reg:
        if r["lifecycle_status"] not in ("active", "retired"):
            errors.append(f"registry: {r['sc_id']} bad lifecycle_status {r['lifecycle_status']!r}")
        if r["lifecycle_status"] == "retired":
            if r["cascade_position"]:
                errors.append(f"registry: retired {r['sc_id']} has a cascade_position")
            if r["staging_row"] == "yes":
                errors.append(f"registry: retired {r['sc_id']} marked as a staging row")
        if r["verdict"]:
            for token in r["verdict"].split("/"):
                if token not in VERDICT_VOCABULARY:
                    errors.append(f"registry: {r['sc_id']} verdict token {token!r} not in vocabulary")
            if r["adjudication_status"] != "adjudicated":
                errors.append(f"registry: {r['sc_id']} has a verdict but is not marked adjudicated")
            if not r["adjudication_memo"]:
                errors.append(f"registry: {r['sc_id']} has a verdict but no adjudication_memo")
            elif not (REPO_ROOT / r["adjudication_memo"]).is_file():
                errors.append(f"registry: {r['sc_id']} memo missing: {r['adjudication_memo']}")
    for e in edges:
        for endpoint in (e["source_change_id"], e["target_change_id"]):
            if endpoint.startswith("SC") and endpoint not in ids:
                errors.append(f"edges: unknown SC {endpoint}")
        if e["relation_type"] in CHRONOLOGY_RELATION_TYPES:
            if e["evidence_basis"] not in ("independently_demonstrated", "stage_entailed"):
                errors.append(
                    f"edges: {e['source_change_id']}->{e['target_change_id']} chronology edge "
                    f"with evidence_basis {e['evidence_basis']!r}"
                )
            if not e["witness_role"]:
                errors.append(f"edges: {e['source_change_id']}->{e['target_change_id']} missing witness_role")
            if not e["representative_lexemes"] or not e["representative_forms"] or not e["notes"]:
                errors.append(
                    f"edges: {e['source_change_id']}->{e['target_change_id']} chronology edge without "
                    "witness lexemes/forms/notes"
                )
            retired = {r["sc_id"] for r in reg if r["lifecycle_status"] == "retired"}
            if e["source_change_id"] in retired or e["target_change_id"] in retired:
                errors.append(
                    f"edges: retired SC on chronology edge {e['source_change_id']}->{e['target_change_id']}"
                )
    return errors


def build_staging_view(reg):
    header = [
        "sc_id", "fst_identifier", "display_name", "source_reader_facing_file",
        "cascade_position", "hist_stage", "hist_scope", "v1_chapter",
        "v1_reader_position", "confidence", "action_status", "capr_evidence",
        "chronology_problem", "notes",
    ]
    staged = [r for r in reg if r["staging_row"] == "yes"]
    staged.sort(key=lambda r: int(r["staging_order"]))
    rows = [
        [
            r["sc_id"], r["fst_identifier"], r["display_name"],
            r["source_reader_facing_file"], r["cascade_position"], r["hist_stage"],
            r["hist_scope"], r["v1_chapter"], r["v1_reader_position"], r["confidence"],
            r["action_status"], r["capr_evidence"], r["chronology_problem"],
            r["staging_notes"],
        ]
        for r in staged
    ]
    b = banner("registry/sc_registry.tsv (rows with staging_row=yes)") + [
        "Canonical SC-level historical staging map view for the Version 1 CAPR book.",
        "Chapters: 1=PGmc→PNWGmc | 2=PNWGmc→PWGmc | 3=PWGmc→Anglo-Frisian | 4=Anglo-Frisian→OE",
        "Confidence: A=secure | B=strong but analysis-dependent | C=genuinely unresolved",
    ]
    return tsv_text(b, header, rows)


def build_inventory_view(reg, ann):
    header = [
        "change_id", "current_order", "display_name", "stage", "trace_stage",
        "rule_source_path", "rule_source_anchor", "foma_definition_raw",
        "plain_description_draft", "appears_in_compact_trace", "trace_occurrence_count",
        "example_lexemes", "literature_status", "order_sensitivity_status", "notes",
        "entry_type", "include_in_volume", "historical_stage", "pipeline_stage",
        "canonical_change_id", "duplicate_group", "is_reader_facing", "review_note",
        "needs_human_review",
    ]
    ann_by_id = {a["change_id"]: a for a in ann}
    rows = []
    for r in sorted(reg, key=lambda r: r["sc_id"]):
        a = ann_by_id.get(r["sc_id"])
        if a is None:
            continue  # SCs without an inventory row (e.g. retired SC021)
        display = r["inventory_display_name"] or r["display_name"]
        rows.append([
            r["sc_id"], r["inventory_order"], display, r["stage_label"],
            a["trace_stage"], a["rule_source_path"], a["rule_source_anchor"],
            a["foma_definition_raw"], a["plain_description_draft"],
            a["appears_in_compact_trace"], a["trace_occurrence_count"],
            a["example_lexemes"], a["literature_status"], a["order_sensitivity_status"],
            a["notes"], r["entry_type"], r["include_in_volume"],
            r["historical_stage_label"], r["pipeline_stage"], r["canonical_change_id"],
            r["duplicate_group"], r["is_reader_facing"], a["review_note"],
            a["needs_human_review"],
        ])
    b = banner(
        "registry/sc_registry.tsv (metadata) + registry/sc_inventory_annotations.tsv (annotations)"
    )
    return tsv_text(b, header, rows)


def build_edges_tsv(edges):
    header = [
        "source_change_id", "target_change_id", "relation_type", "direction_basis",
        "representative_lexemes", "representative_forms", "strength",
        "interpretation_category", "reciprocal_group_id", "notes",
    ]
    rows = [[e[h] for h in header] for e in edges]
    return tsv_text(banner("registry/chronology_edges.tsv"), header, rows)


def node_rows(reg):
    rows = []
    for r in sorted(reg, key=lambda r: r["sc_id"]):
        if not r["chronology_card"]:
            continue
        order = "retired" if r["lifecycle_status"] == "retired" else r["inventory_order"]
        rows.append({
            "change_id": r["sc_id"],
            "display_name": r["display_name"],
            "current_order": order,
            "rule_name": r["fst_identifier"],
            "card_path": r["chronology_card"],
            "card_type": r["chronology_profile"],
            "has_reciprocal_boundary": r["chronology_has_reciprocal_boundary"],
            "short_summary": r["chronology_summary"],
        })
    return rows


def build_nodes_tsv(reg):
    header = [
        "change_id", "display_name", "current_order", "rule_name", "card_path",
        "card_type", "has_reciprocal_boundary", "short_summary",
    ]
    rows = [[n[h] for h in header] for n in node_rows(reg)]
    return tsv_text(
        banner("registry/sc_registry.tsv (rows with chronology-card facts)"), header, rows
    )


def build_edges_json(reg, edges):
    payload = {
        "generated_by": "Germanic/tools/generate_registry_views.py — GENERATED FILE, DO NOT EDIT",
        "sources": [
            "Germanic/docs/sound_changes/registry/sc_registry.tsv",
            "Germanic/docs/sound_changes/registry/chronology_edges.tsv",
        ],
        "nodes": node_rows(reg),
        "edges": [
            {
                "source_change_id": e["source_change_id"],
                "target_change_id": e["target_change_id"],
                "relation_type": e["relation_type"],
                "direction_basis": e["direction_basis"],
                "evidence_basis": e["evidence_basis"],
                "witness_role": e["witness_role"],
                "representative_lexemes": e["representative_lexemes"],
                "representative_forms": e["representative_forms"],
                "strength": e["strength"],
                "interpretation_category": e["interpretation_category"],
                "reciprocal_group_id": e["reciprocal_group_id"],
                "notes": e["notes"],
            }
            for e in edges
        ],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


EDGE_COLORS = {
    "reciprocal_chronology": "#2f855a",
    "near_reciprocal_chronology": "#2f855a",
    "one_sided_chronology": "#2b6cb0",
    "broad_far_chronology": "#2b6cb0",
    "runner_limited_boundary": "#c05621",
    "no_break_search_boundary": "#c05621",
    "technical_computational": "#718096",
}


def build_edges_dot(reg, edges):
    lines = [
        "// GENERATED FILE — DO NOT EDIT.",
        "// Source: registry/sc_registry.tsv + registry/chronology_edges.tsv",
        "// Generator: Germanic/tools/generate_registry_views.py",
        "digraph first_break_chronology {",
        "  rankdir=LR;",
        '  node [shape=box, style="rounded,filled", fillcolor="#ebf8ff", fontname="Helvetica"];',
    ]
    mentioned = set()
    for e in edges:
        mentioned.add(e["source_change_id"])
        mentioned.add(e["target_change_id"])
    for n in node_rows(reg):
        style = ""
        if n["current_order"] == "retired":
            style = ', fillcolor="#71809622", color="#718096"'
        lines.append(f'  "{n["change_id"]}" [label="{n["change_id"]}\\n{n["display_name"]}"{style}];')
    for name in sorted(mentioned):
        if not name.startswith("SC"):
            lines.append(f'  "{name}" [shape=ellipse, fillcolor="#faf089"];')
    for e in edges:
        color = EDGE_COLORS.get(e["relation_type"], "#4a5568")
        dashed = ", style=dashed" if e["relation_type"] not in CHRONOLOGY_RELATION_TYPES else ""
        lines.append(
            f'  "{e["source_change_id"]}" -> "{e["target_change_id"]}" '
            f'[label="{e["relation_type"]}", color="{color}", fontcolor="{color}"{dashed}];'
        )
    lines.append("}")
    return "\n".join(lines) + "\n"


def build_graph_summary(reg, edges):
    nodes = node_rows(reg)
    node_counts = Counter(n["card_type"] for n in nodes)
    edge_counts = Counter(e["relation_type"] for e in edges)
    lines = [
        "# First-break chronology graph summary",
        "",
        "GENERATED FILE — DO NOT EDIT. Source: `registry/sc_registry.tsv` +",
        "`registry/chronology_edges.tsv`. Generator:",
        "`Germanic/tools/generate_registry_views.py`.",
        "",
        "**Ordinary chronology** means a first-break relation between modeled",
        "sound-change rules. Runner-limited boundaries, no-break search",
        "boundaries and technical markers are diagnostic observations, not",
        "chronology constraints.",
        "",
        "## Totals",
        "",
        f"- total node count: `{len(nodes)}`",
        f"- total edge count: `{len(edges)}`",
        "",
        "### Node counts by card_type",
        "",
        "| card_type | count |",
        "| --- | ---: |",
    ]
    for k in sorted(node_counts):
        lines.append(f"| `{k}` | {node_counts[k]} |")
    lines += ["", "### Edge counts by relation_type", "", "| relation_type | count |", "| --- | ---: |"]
    for k in sorted(edge_counts):
        lines.append(f"| `{k}` | {edge_counts[k]} |")
    lines += ["", "## Chronology edges", ""]
    for e in edges:
        if e["relation_type"] not in CHRONOLOGY_RELATION_TYPES:
            continue
        lines.append(
            f"1. `{e['source_change_id']} -> {e['target_change_id']}` "
            f"({e['relation_type']}; {e['evidence_basis']}; witness role: {e['witness_role']}) — "
            f"lexemes: `{e['representative_lexemes']}`; forms: {e['representative_forms']}"
        )
    lines += ["", "## Boundary and technical observations", ""]
    for e in edges:
        if e["relation_type"] in CHRONOLOGY_RELATION_TYPES:
            continue
        lines.append(
            f"1. `{e['source_change_id']} -> {e['target_change_id']}` ({e['relation_type']})"
        )
    return "\n".join(lines) + "\n"


def build_settled_verdicts(reg):
    lines = [
        "# Settled adjudication verdicts",
        "",
        "GENERATED FILE — DO NOT EDIT. Source: `registry/sc_registry.tsv`.",
        "Generator: `Germanic/tools/generate_registry_views.py`.",
        "",
        "| SC | Display name | Lifecycle | Verdict | Memo |",
        "| --- | --- | --- | --- | --- |",
    ]
    for r in sorted(reg, key=lambda r: r["sc_id"]):
        if not r["verdict"]:
            continue
        lines.append(
            f"| {r['sc_id']} | {r['display_name']} | {r['lifecycle_status']} | "
            f"{r['verdict']} | `{r['adjudication_memo']}` |"
        )
    return "\n".join(lines) + "\n"


def build_all():
    reg = read_tsv(SC_REGISTRY)
    ann = read_tsv(ANNOTATIONS)
    edges = read_tsv(EDGE_REGISTRY)
    errors = validate_registry(reg, edges)
    if errors:
        for e in errors:
            print(f"REGISTRY ERROR: {e}", file=sys.stderr)
        raise SystemExit(1)
    return {
        STAGING_VIEW: build_staging_view(reg),
        INVENTORY_VIEW: build_inventory_view(reg, ann),
        EDGES_TSV: build_edges_tsv(edges),
        EDGES_JSON: build_edges_json(reg, edges),
        EDGES_DOT: build_edges_dot(reg, edges),
        NODES_TSV: build_nodes_tsv(reg),
        GRAPH_SUMMARY: build_graph_summary(reg, edges),
        SETTLED_VERDICTS: build_settled_verdicts(reg),
    }


def main() -> int:
    check = "--check" in sys.argv[1:]
    outputs = build_all()
    dirty = []
    for path, text in outputs.items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == text:
            continue
        if check:
            dirty.append(path)
        else:
            path.write_text(text, encoding="utf-8")
            print(f"wrote {path.relative_to(REPO_ROOT)}")
    if check:
        if dirty:
            for p in dirty:
                print(f"STALE VIEW: {p.relative_to(REPO_ROOT)} does not match its sources", file=sys.stderr)
            return 1
        print("all generated views are clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
