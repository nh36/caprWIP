#!/usr/bin/env python3
"""Build a graph/data export for the first-break chronology corpus."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
GRAPH_DIR = SCRIPT_PATH.parent
ORDER_TESTS_DIR = GRAPH_DIR.parent
SOUND_CHANGES_DIR = ORDER_TESTS_DIR.parent
CARDS_DIR = ORDER_TESTS_DIR / "chronology_cards"

INDEX_PATH = CARDS_DIR / "chronology_card_index.tsv"
SUMMARY_PATH = SOUND_CHANGES_DIR / "sound_change_order_sensitivity.tsv"
OVERVIEW_PATH = SOUND_CHANGES_DIR / "order_sensitivity_first_break_consolidated_overview.md"
AUDIT_PATH = CARDS_DIR / "chronology_card_quality_audit.md"

NODES_TSV_PATH = GRAPH_DIR / "first_break_nodes.tsv"
EDGES_TSV_PATH = GRAPH_DIR / "first_break_edges.tsv"
EDGES_DOT_PATH = GRAPH_DIR / "first_break_edges.dot"
EDGES_JSON_PATH = GRAPH_DIR / "first_break_edges.json"
SUMMARY_MD_PATH = GRAPH_DIR / "first_break_graph_summary.md"


RECIPROCAL_GROUPS = [
    ("RG01_SC016_SC017", "SC016", "SC017"),
    ("RG02_SC017_SC019", "SC017", "SC019"),
    ("RG03_SC019_SC020", "SC019", "SC020"),
    ("RG04_SC026_SC027", "SC026", "SC027"),
    ("RG05_SC029_SC030", "SC029", "SC030"),
    ("RG06_SC030_SC032", "SC030", "SC032"),
    ("RG07_SC031_SC034", "SC031", "SC034"),
    ("RG08_SC039_SC040", "SC039", "SC040"),
    ("RG09_SC042_SC043", "SC042", "SC043"),
    ("RG10_SC043_SC044", "SC043", "SC044"),
    ("RG11_SC044_SC045", "SC044", "SC045"),
    ("RG12_SC047_SC048", "SC047", "SC048"),
    ("RG13_SC052_SC055", "SC052", "SC055"),
    ("RG14_SC055_SC056", "SC055", "SC056"),
    ("RG15_SC064_SC072", "SC064", "SC072"),
    ("RG16_SC066_SC068", "SC066", "SC068"),
    ("RG17_SC070_SC071", "SC070", "SC071"),
    ("RG18_SC072_SC073", "SC072", "SC073"),
    ("RG19_SC074_SC075", "SC074", "SC075"),
    ("RG20_SC079_SC080", "SC079", "SC080"),
    ("RG21_SC081_SC082", "SC081", "SC082"),
    ("RG22_SC082_SC083", "SC082", "SC083"),
    ("RG23_SC085_SC086", "SC085", "SC086"),
]

RECIPROCAL_GROUP_BY_PAIR = {
    frozenset((left, right)): group_id
    for group_id, left, right in RECIPROCAL_GROUPS
}

BROAD_RECIPROCAL_GROUPS = {
    "RG12_SC047_SC048",
    "RG18_SC072_SC073",
}


NODE_FIELDS = [
    "change_id",
    "display_name",
    "current_order",
    "rule_name",
    "card_path",
    "card_type",
    "has_reciprocal_boundary",
    "short_summary",
]

EDGE_FIELDS = [
    "source_change_id",
    "target_change_id",
    "relation_type",
    "direction_basis",
    "representative_lexemes",
    "representative_forms",
    "strength",
    "interpretation_category",
    "reciprocal_group_id",
    "notes",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def extract_section(text: str, heading: str, next_heading: str) -> str:
    pattern = rf"## {re.escape(heading)}(.*?)## {re.escape(next_heading)}"
    match = re.search(pattern, text, re.S)
    return match.group(1) if match else ""


def extract_field(block: str, field_name: str) -> str:
    pattern = rf"- {re.escape(field_name)}:\s*(.*)"
    match = re.search(pattern, block)
    return clean_text(match.group(1)) if match else ""


def parse_card(card_path: Path) -> dict[str, str]:
    text = card_path.read_text()
    earlier_block = extract_section(text, "Earlier boundary", "Later boundary")
    later_block = extract_section(text, "Later boundary", "Chronology statement")
    chronology_block = extract_section(text, "Chronology statement", "Caveats")

    rule_match = re.search(r"- rule_name:\s*`([^`]+)`", text)
    current_order_match = re.search(r"- current_order:\s*`([^`]+)`", text)

    return {
        "rule_name": rule_match.group(1) if rule_match else "",
        "current_order": current_order_match.group(1) if current_order_match else "",
        "earlier_representative_forms": extract_field(earlier_block, "concrete failure example"),
        "later_representative_forms": extract_field(later_block, "concrete failure example"),
        "chronology_statement": clean_text(chronology_block),
    }


def node_category(index_row: dict[str, str]) -> str:
    earlier_type = index_row["earlier_boundary_type"]
    later_type = index_row["later_boundary_type"]
    has_recip = index_row["has_reciprocal_boundary"] == "yes"
    broad = index_row["broad_boundary_side"] not in ("", "none")
    earlier_failure_count = int(index_row["earlier_failure_count"] or "0")
    negative = (
        earlier_type == "blocked_by_runner_limitation"
        and later_type == "no_break_before_runner_boundary"
    )
    has_nonhistorical = (
        (earlier_type == "blocked_by_runner_limitation" and earlier_failure_count > 0)
        or later_type == "technical_marker"
    )
    historical_count = int(earlier_type == "historical_first_break") + int(
        later_type == "historical_first_break"
    )

    if negative:
        return "negative_boundary"
    if has_nonhistorical and (has_recip or broad or historical_count >= 1):
        return "mixed"
    if has_recip and broad:
        return "mixed"
    if has_recip:
        return "reciprocal_or_near_reciprocal"
    if broad:
        return "broad_far"
    if historical_count == 1:
        return "one_sided_historical"
    if has_nonhistorical or earlier_type in {"blocked_by_runner_limitation", "technical_marker"} or later_type in {
        "blocked_by_runner_limitation",
        "technical_marker",
    }:
        return "runner_limited_or_non_historical"
    return "mixed"


def representative_lexemes(index_row: dict[str, str], side: str) -> str:
    if side == "earlier":
        return index_row["earlier_example_lexemes"]
    return index_row["later_example_lexemes"]


def representative_forms(card_meta: dict[str, str], side: str) -> str:
    if side == "earlier":
        return card_meta["earlier_representative_forms"]
    return card_meta["later_representative_forms"]


def classify_historical_edge(
    source_row: dict[str, str],
    target_id: str,
    side: str,
) -> tuple[str, str, str]:
    pair_group = RECIPROCAL_GROUP_BY_PAIR.get(frozenset((source_row["change_id"], target_id)))
    broad_side = source_row["broad_boundary_side"]
    side_is_broad = broad_side in {side, "both"}

    if pair_group and (pair_group in BROAD_RECIPROCAL_GROUPS or side_is_broad):
        return "broad_far_historical", "broad_reciprocal", pair_group
    if pair_group:
        return "reciprocal_historical", "tight_local", pair_group
    if side_is_broad:
        return "broad_far_historical", "broad_far", ""
    return "one_sided_historical", "one_sided", ""


def diagnostic_target(index_row: dict[str, str], side: str) -> str:
    if side == "earlier":
        return index_row["earlier_boundary_change_id"] or "PWGmcChanges"
    if index_row["change_id"] == "SC087":
        return "RUNNER_LIMIT"
    return index_row["later_boundary_change_id"] or "RUNNER_LIMIT"


def build_nodes(index_rows: list[dict[str, str]], card_meta_by_id: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    nodes: list[dict[str, str]] = []
    for row in index_rows:
        change_id = row["change_id"]
        card_meta = card_meta_by_id[change_id]
        nodes.append(
            {
                "change_id": change_id,
                "display_name": row["display_name"],
                "current_order": row["current_order"],
                "rule_name": card_meta["rule_name"],
                "card_path": str(card_meta_by_id[change_id]["card_path"]),
                "card_type": node_category(row),
                "has_reciprocal_boundary": row["has_reciprocal_boundary"],
                "short_summary": row["notes"],
            }
        )
    return nodes


def build_edges(
    index_rows: list[dict[str, str]],
    card_meta_by_id: dict[str, dict[str, str]],
) -> list[dict[str, str]]:
    edges: list[dict[str, str]] = []
    for row in index_rows:
        change_id = row["change_id"]
        card_meta = card_meta_by_id[change_id]
        for side in ("earlier", "later"):
            boundary_type = row[f"{side}_boundary_type"]
            target_id = diagnostic_target(row, side)
            lexemes = representative_lexemes(row, side)
            forms = representative_forms(card_meta, side)
            notes = row["notes"]
            if boundary_type == "historical_first_break":
                relation_type, strength, reciprocal_group_id = classify_historical_edge(
                    row, target_id, side
                )
                interpretation_category = (
                    "reciprocal_or_near_reciprocal"
                    if reciprocal_group_id
                    else ("broad_far" if relation_type == "broad_far_historical" else "one_sided_historical")
                )
            elif boundary_type == "blocked_by_runner_limitation":
                failure_count = int(row[f"{side}_failure_count"] or "0")
                reciprocal_group_id = ""
                if failure_count > 0:
                    relation_type = "non_historical_computational"
                    strength = "bundled_stage"
                    interpretation_category = "non_historical_computational"
                else:
                    relation_type = "runner_limited_boundary"
                    strength = "search_limit"
                    interpretation_category = "runner_limited_boundary"
            elif boundary_type == "technical_marker":
                relation_type = "non_historical_computational"
                strength = "technical_marker"
                reciprocal_group_id = ""
                interpretation_category = "non_historical_computational"
            elif boundary_type == "no_break_before_runner_boundary":
                relation_type = "no_break_search_boundary"
                strength = "search_limit"
                reciprocal_group_id = ""
                interpretation_category = "no_break_search_boundary"
            else:
                raise ValueError(f"Unexpected boundary type {boundary_type!r} for {change_id} {side}")

            edges.append(
                {
                    "source_change_id": change_id,
                    "target_change_id": target_id,
                    "relation_type": relation_type,
                    "direction_basis": f"{side}_boundary",
                    "representative_lexemes": lexemes,
                    "representative_forms": forms,
                    "strength": strength,
                    "interpretation_category": interpretation_category,
                    "reciprocal_group_id": reciprocal_group_id,
                    "notes": notes,
                }
            )
    return edges


def edge_sort_key(edge: dict[str, str], order_by_id: dict[str, int]) -> tuple[int, int, str, str]:
    direction_rank = 0 if edge["direction_basis"] == "earlier_boundary" else 1
    return (
        order_by_id.get(edge["source_change_id"], 999),
        direction_rank,
        edge["relation_type"],
        edge["target_change_id"],
    )


def dot_node_style(card_type: str) -> tuple[str, str]:
    styles = {
        "reciprocal_or_near_reciprocal": ("ellipse", "#2f855a"),
        "one_sided_historical": ("box", "#4a5568"),
        "broad_far": ("box", "#2b6cb0"),
        "negative_boundary": ("octagon", "#c53030"),
        "runner_limited_or_non_historical": ("diamond", "#b7791f"),
        "mixed": ("hexagon", "#6b46c1"),
    }
    return styles[card_type]


def dot_edge_style(relation_type: str) -> tuple[str, str, str]:
    styles = {
        "reciprocal_historical": ("#2f855a", "solid", "2.2"),
        "near_reciprocal_historical": ("#2f855a", "dashed", "2.0"),
        "one_sided_historical": ("#4a5568", "solid", "1.5"),
        "broad_far_historical": ("#2b6cb0", "dashed", "1.8"),
        "non_historical_computational": ("#b7791f", "dotted", "1.6"),
        "no_break_search_boundary": ("#c53030", "dotted", "1.5"),
        "runner_limited_boundary": ("#c05621", "dashed", "1.5"),
    }
    return styles[relation_type]


def write_dot(
    nodes: list[dict[str, str]],
    edges: list[dict[str, str]],
    order_by_id: dict[str, int],
) -> None:
    corpus_node_ids = {node["change_id"] for node in nodes}
    extra_targets = sorted({edge["target_change_id"] for edge in edges if edge["target_change_id"] not in corpus_node_ids})

    lines = [
        "digraph first_break_chronology {",
        '  graph [rankdir=LR, fontsize=10, labelloc="t", label="First-break chronology graph"];',
        '  node [fontname="Helvetica", fontsize=10, style="filled"];',
        '  edge [fontname="Helvetica", fontsize=9];',
        "",
    ]

    for node in sorted(nodes, key=lambda item: int(item["current_order"])):
        shape, color = dot_node_style(node["card_type"])
        label = f'{node["change_id"]}\\n{node["display_name"]}'
        lines.append(
            f'  "{node["change_id"]}" [label="{label}", shape={shape}, fillcolor="{color}22", color="{color}"];'
        )

    if extra_targets:
        lines.append("")
    for target in extra_targets:
        if target == "PWGmcChanges":
            label = "PWGmcChanges\\nrunner boundary"
        elif target == "SC038":
            label = "SC038\\ntechnical marker"
        elif target == "RUNNER_LIMIT":
            label = "RUNNER_LIMIT\\nterminal search limit"
        else:
            label = target
        lines.append(
            f'  "{target}" [label="{label}", shape=diamond, fillcolor="#f7fafc", color="#718096"];'
        )

    lines.append("")
    for edge in sorted(edges, key=lambda item: edge_sort_key(item, order_by_id)):
        color, style, penwidth = dot_edge_style(edge["relation_type"])
        label_bits = [edge["relation_type"]]
        if edge["reciprocal_group_id"]:
            label_bits.append(edge["reciprocal_group_id"])
        label = "\\n".join(label_bits)
        lines.append(
            f'  "{edge["source_change_id"]}" -> "{edge["target_change_id"]}" '
            f'[label="{label}", color="{color}", fontcolor="{color}", style={style}, penwidth={penwidth}];'
        )

    lines.append("}")
    EDGES_DOT_PATH.write_text("\n".join(lines) + "\n")


def group_label(group_id: str) -> str:
    _, left, right = group_id.split("_", 2)
    return f"{left} / {right}"


def build_summary(
    nodes: list[dict[str, str]],
    edges: list[dict[str, str]],
    index_rows: list[dict[str, str]],
) -> str:
    def dedupe_semicolon_values(values: list[str]) -> str:
        seen: list[str] = []
        for raw in values:
            for part in [item.strip() for item in raw.split(";") if item.strip()]:
                if part not in seen:
                    seen.append(part)
        return "; ".join(seen)

    edge_counts = Counter(edge["relation_type"] for edge in edges)
    node_counts = Counter(node["card_type"] for node in nodes)
    broad_edges = [edge for edge in edges if edge["relation_type"] == "broad_far_historical"]
    negative_nodes = [node["change_id"] for node in nodes if node["card_type"] == "negative_boundary"]
    runner_limited_sources = sorted(
        edge["source_change_id"]
        for edge in edges
        if edge["relation_type"] == "runner_limited_boundary" and edge["target_change_id"] == "PWGmcChanges"
    )
    non_historical_edges = [
        edge
        for edge in edges
        if edge["relation_type"] == "non_historical_computational"
    ]
    search_boundary_sources = sorted(
        edge["source_change_id"]
        for edge in edges
        if edge["relation_type"] == "no_break_search_boundary"
    )

    lines = [
        "# First-break chronology graph summary",
        "",
        "## Scope",
        "",
        "This graph export was generated from the audited first-break chronology corpus. It reuses the current chronology-card, index, and summary-table layer only; no new first-break computations were run.",
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

    for card_type in sorted(node_counts):
        lines.append(f"| `{card_type}` | {node_counts[card_type]} |")

    lines.extend(
        [
            "",
            "### Edge counts by relation_type",
            "",
            "| relation_type | count |",
            "| --- | ---: |",
        ]
    )
    for relation_type in sorted(edge_counts):
        lines.append(f"| `{relation_type}` | {edge_counts[relation_type]} |")

    lines.extend(
        [
            "",
            "## Strongest reciprocal / near-reciprocal clusters",
            "",
        ]
    )

    grouped_edges: dict[str, list[dict[str, str]]] = {}
    for edge in edges:
        if edge["reciprocal_group_id"]:
            grouped_edges.setdefault(edge["reciprocal_group_id"], []).append(edge)

    for group_id, left, right in RECIPROCAL_GROUPS:
        cluster_edges = sorted(
            grouped_edges.get(group_id, []),
            key=lambda item: (item["source_change_id"], item["target_change_id"]),
        )
        if not cluster_edges:
            continue
        relation_labels = sorted({edge["relation_type"] for edge in cluster_edges})
        sample_lexemes = dedupe_semicolon_values(
            [edge["representative_lexemes"] for edge in cluster_edges if edge["representative_lexemes"]]
        )
        sample_forms = next(
            (edge["representative_forms"] for edge in cluster_edges if edge["representative_forms"]),
            "",
        )
        lines.append(
            f"1. `{left} / {right}` — `{', '.join(relation_labels)}`; representative lexemes: `{sample_lexemes or 'none recorded'}`; forms: {sample_forms or 'none recorded'}"
        )

    lines.extend(
        [
            "",
            "## Broad / far constraints",
            "",
        ]
    )
    for edge in sorted(broad_edges, key=lambda item: (item["source_change_id"], item["direction_basis"])):
        lines.append(
            f"1. `{edge['source_change_id']} -> {edge['target_change_id']}` ({edge['direction_basis']}) — lexemes: `{edge['representative_lexemes'] or 'none recorded'}`; forms: {edge['representative_forms'] or 'none recorded'}"
        )

    lines.extend(
        [
            "",
            "## Negative / boundary-only nodes",
            "",
            ", ".join(f"`{node}`" for node in negative_nodes),
            "",
            "## Runner-limited or non-historical cases",
            "",
            f"- earlier runner-limited boundaries to `PWGmcChanges`: {', '.join(f'`{cid}`' for cid in runner_limited_sources)}",
            f"- later no-break search-boundary cases before `SC087`: {', '.join(f'`{cid}`' for cid in search_boundary_sources)}",
            "- non-historical computational edges:",
        ]
    )
    for edge in sorted(non_historical_edges, key=lambda item: item["source_change_id"]):
        lines.append(
            f"  - `{edge['source_change_id']} -> {edge['target_change_id']}` ({edge['direction_basis']}) — {edge['notes']}"
        )

    lines.extend(
        [
            "",
            "## Recommendation for the next phase",
            "",
            "Use this export as the data layer for a visualization pass first: the node categories and relation types are now explicit enough to support static diagrams or chapter-planning views without reinterpreting the cards by hand. After that, the highest-value technical follow-up remains runner work that exposes bundled stages such as `PWGmcChanges` so the current runner-limited earlier boundaries can be turned into ordinary chronology targets.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_json(nodes: list[dict[str, str]], edges: list[dict[str, str]]) -> None:
    payload = {
        "sources": {
            "index_tsv": str(INDEX_PATH.relative_to(SOUND_CHANGES_DIR.parents[2])),
            "summary_tsv": str(SUMMARY_PATH.relative_to(SOUND_CHANGES_DIR.parents[2])),
            "overview_md": str(OVERVIEW_PATH.relative_to(SOUND_CHANGES_DIR.parents[2])),
            "audit_md": str(AUDIT_PATH.relative_to(SOUND_CHANGES_DIR.parents[2])),
        },
        "nodes": nodes,
        "edges": edges,
    }
    EDGES_JSON_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")


def main() -> None:
    index_rows = read_tsv(INDEX_PATH)
    summary_rows = read_tsv(SUMMARY_PATH)
    if len(index_rows) != 70:
        raise SystemExit(f"Expected 70 index rows, found {len(index_rows)}")
    if len(summary_rows) < len(index_rows):
        raise SystemExit("Summary TSV is unexpectedly shorter than the card index")

    card_meta_by_id: dict[str, dict[str, str]] = {}
    for row in index_rows:
        change_id = row["change_id"]
        matches = sorted(CARDS_DIR.glob(f"{change_id}-*.md"))
        if len(matches) != 1:
            raise SystemExit(f"Expected exactly one card file for {change_id}, found {len(matches)}")
        card_path = matches[0]
        card_meta = parse_card(card_path)
        card_meta["card_path"] = str(card_path.relative_to(SOUND_CHANGES_DIR.parents[2]))
        card_meta_by_id[change_id] = card_meta

    nodes = build_nodes(index_rows, card_meta_by_id)
    order_by_id = {node["change_id"]: int(node["current_order"]) for node in nodes}
    edges = build_edges(index_rows, card_meta_by_id)
    edges.sort(key=lambda item: edge_sort_key(item, order_by_id))

    write_tsv(NODES_TSV_PATH, nodes, NODE_FIELDS)
    write_tsv(EDGES_TSV_PATH, edges, EDGE_FIELDS)
    write_dot(nodes, edges, order_by_id)
    write_json(nodes, edges)
    SUMMARY_MD_PATH.write_text(build_summary(nodes, edges, index_rows))


if __name__ == "__main__":
    main()
