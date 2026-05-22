#!/usr/bin/env python3
"""Baseline and adjacent-swap order-sensitivity pilot for Old English."""

from __future__ import annotations

import argparse
import csv
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

from oe_full_trace_report import STAGES, apply_down, load_rows


RULE_NAME_RE = re.compile(r"define\s+([A-Za-z0-9]+)")
ENGLISH_PROTO_TO_OE_RE = re.compile(
    r"define EnglishProtoToOE \((.*?)\);\s*define EnglishProtoInput",
    re.DOTALL,
)

POST_CASCADE_RULES = [
    "OEEpentheticVowel",
    "OELateUnstressedAgSuffix",
    "OECjCleanup",
    "OEXsMerge",
    "OldEnglishOrthography",
    "OEGlideUToEO",
    "OldEnglishRemoveStars",
]


@dataclass(frozen=True)
class ChangeInfo:
    change_id: str
    display_name: str
    current_order: int
    rule_name: str
    entry_type: str
    include_in_volume: str
    notes: str


@dataclass(frozen=True)
class NeighborInfo:
    change_id: str
    display_name: str
    current_order: int
    rule_name: str
    entry_type: str


def repo_paths() -> Dict[str, Path]:
    tools_dir = Path(__file__).resolve().parent
    germanic_dir = tools_dir.parent
    repo_root = germanic_dir.parent
    summaries_dir = germanic_dir / "docs" / "sound_changes" / "order_tests" / "summaries"
    live_bin_candidates = [
        germanic_dir / "old_english.bin",
        repo_root / "backend" / "old_english.bin",
        repo_root / "old_english.bin",
        germanic_dir / "fsts" / "old_english.bin",
    ]
    live_bin = next((path for path in live_bin_candidates if path.exists()), live_bin_candidates[0])
    return {
        "tools_dir": tools_dir,
        "germanic_dir": germanic_dir,
        "repo_root": repo_root,
        "inventory": germanic_dir / "docs" / "sound_changes" / "sound_change_inventory.tsv",
        "germanic_txt": germanic_dir / "fsts" / "germanic.txt",
        "sandbox_txt": germanic_dir / "fsts" / "old_english_sandbox.txt",
        "aligned_tsv": germanic_dir / "data" / "germanic-aligned-final.tsv",
        "live_bin": live_bin,
        "baseline_tsv": summaries_dir / "order_sensitivity_baseline_01.tsv",
        "adjacent_tsv": summaries_dir / "order_sensitivity_adjacent_pilot_01.tsv",
        "adjacent_changes_tsv": summaries_dir / "order_sensitivity_adjacent_pilot_01_changes.tsv",
    }


def parse_args() -> argparse.Namespace:
    defaults = repo_paths()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", required=True, choices=("baseline", "adjacent-pilot"))
    parser.add_argument("--change", help="Target change_id for adjacent-pilot mode (e.g. SC043)")
    parser.add_argument("--inventory", default=str(defaults["inventory"]))
    parser.add_argument("--germanic", default=str(defaults["germanic_txt"]))
    parser.add_argument("--sandbox", default=str(defaults["sandbox_txt"]))
    parser.add_argument("--tsv", default=str(defaults["aligned_tsv"]))
    parser.add_argument("--bin", default=str(defaults["live_bin"]))
    parser.add_argument("--baseline-output", default=str(defaults["baseline_tsv"]))
    parser.add_argument("--summary-output", default=str(defaults["adjacent_tsv"]))
    parser.add_argument("--changes-output", default=str(defaults["adjacent_changes_tsv"]))
    args = parser.parse_args()
    if args.mode == "adjacent-pilot" and not args.change:
        parser.error("--change is required for --mode adjacent-pilot")
    return args


def extract_rule_name(anchor: str) -> str:
    match = RULE_NAME_RE.search(anchor or "")
    if not match:
        raise ValueError(f"Could not extract FOMA rule name from anchor: {anchor!r}")
    return match.group(1)


def load_inventory(path: Path) -> Tuple[Dict[str, ChangeInfo], List[ChangeInfo]]:
    by_id: Dict[str, ChangeInfo] = {}
    ordered: List[ChangeInfo] = []
    with path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            current_order = (row.get("current_order") or "").strip()
            if not current_order:
                continue
            info = ChangeInfo(
                change_id=(row.get("change_id") or "").strip(),
                display_name=(row.get("display_name") or "").strip(),
                current_order=int(current_order),
                rule_name=extract_rule_name(row.get("rule_source_anchor") or ""),
                entry_type=(row.get("entry_type") or "").strip(),
                include_in_volume=(row.get("include_in_volume") or "").strip(),
                notes=(row.get("notes") or "").strip(),
            )
            by_id[info.change_id] = info
            ordered.append(info)
    ordered.sort(key=lambda item: item.current_order)
    return by_id, ordered


def neighbors_for_change(change_id: str, ordered: Sequence[ChangeInfo]) -> Tuple[NeighborInfo | None, NeighborInfo | None]:
    for idx, item in enumerate(ordered):
        if item.change_id != change_id:
            continue
        earlier = ordered[idx - 1] if idx > 0 else None
        later = ordered[idx + 1] if idx + 1 < len(ordered) else None
        return (
            NeighborInfo(earlier.change_id, earlier.display_name, earlier.current_order, earlier.rule_name, earlier.entry_type) if earlier else None,
            NeighborInfo(later.change_id, later.display_name, later.current_order, later.rule_name, later.entry_type) if later else None,
        )
    raise KeyError(f"Change {change_id} not found in inventory")


def parse_english_proto_to_oe_order(germanic_path: Path) -> List[str]:
    text = germanic_path.read_text(encoding="utf-8")
    match = ENGLISH_PROTO_TO_OE_RE.search(text)
    if not match:
        raise RuntimeError(f"Could not locate EnglishProtoToOE block in {germanic_path}")
    block = match.group(1)
    stripped_lines = []
    for raw_line in block.splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if line:
            stripped_lines.append(line)
    cleaned = "\n".join(stripped_lines)
    order = [part.strip() for part in cleaned.split(".o.") if part.strip()]
    if not order:
        raise RuntimeError(f"EnglishProtoToOE block in {germanic_path} parsed to an empty rule list")
    return order


def format_outputs(outputs: Sequence[str]) -> str:
    return " | ".join(outputs) if outputs else "+?"


def result_key(row: Dict[str, object]) -> Tuple[str, str]:
    return (str(row["lexical_item"]), str(row["protoform"]))


def outputs_match_expected(outputs: Sequence[str], expected: str) -> bool:
    return expected in outputs


def baseline_note(outputs: Sequence[str], expected: str) -> str:
    if not outputs:
        return "no_output"
    if len(outputs) > 1 and expected in outputs:
        return "multiple_outputs_includes_expected"
    if len(outputs) > 1:
        return "multiple_outputs_missing_expected"
    if expected in outputs:
        return "exact_match"
    return "single_output_mismatch"


def evaluate_rows(rows: Sequence[Dict[str, str]], bin_path: Path) -> List[Dict[str, object]]:
    evaluated: List[Dict[str, object]] = []
    for row in rows:
        outputs = apply_down(bin_path, row["proto_norm"])
        expected = row["counterpart"]
        evaluated.append(
            {
                "lexical_item": row["concept"],
                "protoform": row["proto"],
                "proto_norm": row["proto_norm"],
                "expected_counterpart": expected,
                "outputs": outputs,
                "outputs_text": format_outputs(outputs),
                "matches_expected": outputs_match_expected(outputs, expected),
                "notes": baseline_note(outputs, expected),
            }
        )
    return evaluated


def summarize_evaluation(results: Sequence[Dict[str, object]]) -> Dict[str, int]:
    return {
        "total_rows_tested": len(results),
        "matches_expected": sum(1 for row in results if row["matches_expected"]),
        "fails_expected": sum(1 for row in results if not row["matches_expected"]),
        "no_output_rows": sum(1 for row in results if not row["outputs"]),
        "multi_output_rows": sum(1 for row in results if len(row["outputs"]) > 1),
    }


def write_baseline_tsv(results: Sequence[Dict[str, object]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "lexical_item",
        "protoform",
        "expected_counterpart",
        "current_outputs",
        "current_matches_expected",
        "notes",
    ]
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        for row in results:
            writer.writerow(
                {
                    "lexical_item": row["lexical_item"],
                    "protoform": row["protoform"],
                    "expected_counterpart": row["expected_counterpart"],
                    "current_outputs": row["outputs_text"],
                    "current_matches_expected": "yes" if row["matches_expected"] else "no",
                    "notes": row["notes"],
                }
            )


def build_variant_appendix(order: Sequence[str]) -> str:
    lines = [
        "",
        "# Variant Old English order generated by sound_change_order_sensitivity.py",
        "define VariantEnglishProtoToOE (",
    ]
    for index, rule in enumerate(order):
        prefix = "    " if index == 0 else "    .o. "
        lines.append(f"{prefix}{rule}")
    lines.extend(
        [
            ");",
            "",
            "define VariantOldEnglishCore EnglishProtoInput",
            "    .o. PGmcConsonantRules",
            "    .o. VariantEnglishProtoToOE;",
            "",
            "define VariantOldEnglishAfterEpenthesis VariantOldEnglishCore",
            "    .o. OEEpentheticVowel;",
            "",
            "define VariantOldEnglishRules VariantOldEnglishAfterEpenthesis",
        ]
    )
    for rule in POST_CASCADE_RULES:
        lines.append(f"    .o. {rule}")
    lines.extend(
        [
            "    ;",
            "",
            "define VariantOldEnglishReflexes VariantOldEnglishRules .o. OldEnglishSurface;",
            "",
            "clear stack",
            "regex VariantOldEnglishReflexes;",
            "save stack old_english_variant.bin",
            "",
        ]
    )
    return "\n".join(lines)


def compile_variant(
    germanic_path: Path,
    sandbox_path: Path,
    variant_id: str,
    order: Sequence[str],
) -> Tuple[str, Path | None, str]:
    with tempfile.TemporaryDirectory(prefix=f"{variant_id}_") as temp_dir:
        tmpdir = Path(temp_dir)
        tmp_germanic = tmpdir / "germanic.txt"
        tmp_sandbox = tmpdir / "old_english_sandbox.txt"
        shutil.copy2(germanic_path, tmp_germanic)
        shutil.copy2(sandbox_path, tmp_sandbox)
        with tmp_germanic.open("a", encoding="utf-8") as handle:
            handle.write(build_variant_appendix(order))
        manifest = tmpdir / "variant_manifest.txt"
        manifest.write_text("\n".join(order) + "\n", encoding="utf-8")
        proc = subprocess.run(
            ["foma", "-f", str(tmp_germanic.name)],
            cwd=tmpdir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        variant_bin = tmpdir / "old_english_variant.bin"
        if proc.returncode != 0 or not variant_bin.exists():
            log_tail = "\n".join((proc.stdout + "\n" + proc.stderr).splitlines()[-12:]).strip()
            return ("compile_failed", None, log_tail or "foma exited without producing old_english_variant.bin")
        persisted_bin = tmpdir / f"{variant_id}.bin"
        shutil.copy2(variant_bin, persisted_bin)
        final_copy = germanic_path.parent.parent / ".tmp_order_sensitivity"
        final_copy.mkdir(parents=True, exist_ok=True)
        retained_bin = final_copy / f"{variant_id}.bin"
        shutil.copy2(persisted_bin, retained_bin)
        return ("compiled", retained_bin, "")


def cleanup_retained_bins(path: Path) -> None:
    if not path.exists():
        return
    path.unlink()
    parent = path.parent
    if parent.name == ".tmp_order_sensitivity" and parent.exists() and not any(parent.iterdir()):
        parent.rmdir()


def swap_adjacent(order: Sequence[str], target_rule: str, movement: str) -> Tuple[List[str], str]:
    if target_rule not in order:
        raise KeyError(f"Rule {target_rule} does not appear in the live EnglishProtoToOE chain")
    idx = order.index(target_rule)
    if movement == "earlier":
        if idx == 0:
            raise ValueError(f"Rule {target_rule} cannot move one step earlier")
        neighbor_idx = idx - 1
    else:
        if idx + 1 >= len(order):
            raise ValueError(f"Rule {target_rule} cannot move one step later")
        neighbor_idx = idx + 1
    variant_order = list(order)
    variant_order[idx], variant_order[neighbor_idx] = variant_order[neighbor_idx], variant_order[idx]
    return variant_order, order[neighbor_idx]


def unique_preview(rows: Iterable[Dict[str, object]], field: str, limit: int = 5) -> str:
    values = sorted({str(row[field]) for row in rows if row.get(field)})
    return "; ".join(values[:limit])


def upsert_tsv(
    output_path: Path,
    fieldnames: Sequence[str],
    key_fields: Sequence[str],
    new_rows: Sequence[Dict[str, str]],
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    existing: List[Dict[str, str]] = []
    if output_path.exists():
        with output_path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            existing.extend(reader)
    new_keys = {tuple(row[field] for field in key_fields) for row in new_rows}
    merged = [row for row in existing if tuple(row[field] for field in key_fields) not in new_keys]
    merged.extend(new_rows)
    merged.sort(key=lambda row: tuple(row[field] for field in key_fields))
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(merged)


def status_change_label(baseline_match: bool, variant_match: bool, baseline_output: str, variant_output: str) -> str:
    if baseline_match and not variant_match:
        return "newly_failing"
    if (not baseline_match) and variant_match:
        return "newly_passing"
    if baseline_match and variant_match:
        return "changed_still_passing"
    if baseline_output == "+?" and variant_output != "+?":
        return "no_output_to_output"
    if baseline_output != "+?" and variant_output == "+?":
        return "output_to_no_output"
    return "changed_still_failing"


def run_adjacent_pilot(
    change: ChangeInfo,
    inventory_earlier: NeighborInfo | None,
    inventory_later: NeighborInfo | None,
    live_order: Sequence[str],
    rows: Sequence[Dict[str, str]],
    baseline_results: Sequence[Dict[str, object]],
    summary_output: Path,
    changes_output: Path,
    germanic_path: Path,
    sandbox_path: Path,
) -> List[Dict[str, str]]:
    stage_labels = {label for label, _ in STAGES}
    baseline_map = {result_key(row): row for row in baseline_results}
    baseline_stats = summarize_evaluation(baseline_results)
    summary_rows: List[Dict[str, str]] = []
    detail_rows: List[Dict[str, str]] = []
    for movement, inventory_neighbor in (("earlier", inventory_earlier), ("later", inventory_later)):
        variant_id = f"{change.change_id}_{movement}_adjacent"
        variant_order, chain_neighbor_rule = swap_adjacent(live_order, change.rule_name, movement)
        compilation_status = "compiled"
        compile_note = ""
        variant_bin: Path | None = None
        try:
            compilation_status, variant_bin, compile_note = compile_variant(
                germanic_path=germanic_path,
                sandbox_path=sandbox_path,
                variant_id=variant_id,
                order=variant_order,
            )
            if compilation_status == "compiled" and variant_bin is not None:
                variant_results = evaluate_rows(rows, variant_bin)
            else:
                variant_results = []
        finally:
            if variant_bin is not None:
                cleanup_retained_bins(variant_bin)
        variant_stats = summarize_evaluation(variant_results) if variant_results else {
            "total_rows_tested": len(rows),
            "matches_expected": 0,
            "fails_expected": len(rows),
            "no_output_rows": len(rows),
            "multi_output_rows": 0,
        }
        changed_rows: List[Dict[str, object]] = []
        if variant_results:
            for variant_row in variant_results:
                baseline_row = baseline_map[result_key(variant_row)]
                if baseline_row["outputs_text"] == variant_row["outputs_text"]:
                    continue
                status_change = status_change_label(
                    bool(baseline_row["matches_expected"]),
                    bool(variant_row["matches_expected"]),
                    str(baseline_row["outputs_text"]),
                    str(variant_row["outputs_text"]),
                )
                changed_rows.append(
                    {
                        "variant_id": variant_id,
                        "change_id": change.change_id,
                        "movement": movement,
                        "swapped_with_change_id": inventory_neighbor.change_id if inventory_neighbor else "",
                        "swapped_with_display_name": inventory_neighbor.display_name if inventory_neighbor else chain_neighbor_rule,
                        "swapped_with_rule_name": chain_neighbor_rule,
                        "lexical_item": variant_row["lexical_item"],
                        "protoform": variant_row["protoform"],
                        "expected_counterpart": variant_row["expected_counterpart"],
                        "baseline_output": baseline_row["outputs_text"],
                        "variant_output": variant_row["outputs_text"],
                        "baseline_matches_expected": "yes" if baseline_row["matches_expected"] else "no",
                        "variant_matches_expected": "yes" if variant_row["matches_expected"] else "no",
                        "status_change": status_change,
                        "likely_break_stage_or_note": (
                            f"Adjacent swap with {chain_neighbor_rule}; variant produced no output."
                            if variant_row["outputs_text"] == "+?"
                            else f"Adjacent swap with {chain_neighbor_rule} changed the output."
                        ),
                    }
                )
        newly_failing = [row for row in changed_rows if row["status_change"] == "newly_failing"]
        chain_vs_inventory_note = ""
        if inventory_neighbor and inventory_neighbor.rule_name != chain_neighbor_rule:
            chain_vs_inventory_note = (
                f"inventory neighbor {inventory_neighbor.rule_name} differs from live-chain neighbor {chain_neighbor_rule}"
            )
        elif inventory_neighbor and inventory_neighbor.rule_name not in stage_labels:
            chain_vs_inventory_note = f"inventory neighbor {inventory_neighbor.rule_name} is not a sandbox stage label"
        notes = [note for note in [compile_note, chain_vs_inventory_note] if note]
        if inventory_neighbor and inventory_neighbor.entry_type != "historical_sound_change":
            notes.append(f"swapped across non-historical neighbor {inventory_neighbor.change_id}")
        summary_rows.append(
            {
                "variant_id": variant_id,
                "change_id": change.change_id,
                "display_name": change.display_name,
                "movement": movement,
                "swapped_with_change_id": inventory_neighbor.change_id if inventory_neighbor else "",
                "swapped_with_display_name": inventory_neighbor.display_name if inventory_neighbor else chain_neighbor_rule,
                "compilation_status": compilation_status,
                "total_rows_tested": str(variant_stats["total_rows_tested"]),
                "baseline_matches": str(baseline_stats["matches_expected"]),
                "variant_matches": str(variant_stats["matches_expected"]),
                "changed_output_count": str(len(changed_rows)),
                "newly_failing_count": str(len(newly_failing)),
                "newly_passing_count": str(sum(1 for row in changed_rows if row["status_change"] == "newly_passing")),
                "no_output_count": str(variant_stats["no_output_rows"]),
                "representative_changed_lexemes": unique_preview(changed_rows, "lexical_item"),
                "representative_new_failures": unique_preview(newly_failing, "lexical_item"),
                "notes": "; ".join(notes),
            }
        )
        detail_rows.extend(
            {
                key: str(value)
                for key, value in row.items()
            }
            for row in changed_rows
        )
    summary_fieldnames = [
        "variant_id",
        "change_id",
        "display_name",
        "movement",
        "swapped_with_change_id",
        "swapped_with_display_name",
        "compilation_status",
        "total_rows_tested",
        "baseline_matches",
        "variant_matches",
        "changed_output_count",
        "newly_failing_count",
        "newly_passing_count",
        "no_output_count",
        "representative_changed_lexemes",
        "representative_new_failures",
        "notes",
    ]
    detail_fieldnames = [
        "variant_id",
        "change_id",
        "movement",
        "swapped_with_change_id",
        "swapped_with_display_name",
        "swapped_with_rule_name",
        "lexical_item",
        "protoform",
        "expected_counterpart",
        "baseline_output",
        "variant_output",
        "baseline_matches_expected",
        "variant_matches_expected",
        "status_change",
        "likely_break_stage_or_note",
    ]
    upsert_tsv(summary_output, summary_fieldnames, ("variant_id",), summary_rows)
    upsert_tsv(changes_output, detail_fieldnames, ("variant_id", "lexical_item", "protoform"), detail_rows)
    return summary_rows


def main() -> None:
    args = parse_args()
    inventory_path = Path(args.inventory).expanduser().resolve()
    germanic_path = Path(args.germanic).expanduser().resolve()
    sandbox_path = Path(args.sandbox).expanduser().resolve()
    tsv_path = Path(args.tsv).expanduser().resolve()
    bin_path = Path(args.bin).expanduser().resolve()
    baseline_output = Path(args.baseline_output).expanduser().resolve()
    summary_output = Path(args.summary_output).expanduser().resolve()
    changes_output = Path(args.changes_output).expanduser().resolve()

    inventory_by_id, ordered_inventory = load_inventory(inventory_path)
    live_order = parse_english_proto_to_oe_order(germanic_path)
    rows = load_rows(tsv_path)

    baseline_results = evaluate_rows(rows, bin_path)
    baseline_stats = summarize_evaluation(baseline_results)

    if args.mode == "baseline":
        write_baseline_tsv(baseline_results, baseline_output)
        print(
            "baseline "
            f"rows={baseline_stats['total_rows_tested']} "
            f"matches={baseline_stats['matches_expected']} "
            f"fails={baseline_stats['fails_expected']} "
            f"no_output={baseline_stats['no_output_rows']} "
            f"multi_output={baseline_stats['multi_output_rows']} "
            f"output={baseline_output}"
        )
        return

    change = inventory_by_id[args.change]
    earlier, later = neighbors_for_change(change.change_id, ordered_inventory)
    summary_rows = run_adjacent_pilot(
        change=change,
        inventory_earlier=earlier,
        inventory_later=later,
        live_order=live_order,
        rows=rows,
        baseline_results=baseline_results,
        summary_output=summary_output,
        changes_output=changes_output,
        germanic_path=germanic_path,
        sandbox_path=sandbox_path,
    )
    for row in summary_rows:
        print(
            f"{row['variant_id']} status={row['compilation_status']} "
            f"changed={row['changed_output_count']} "
            f"new_failures={row['newly_failing_count']} "
            f"variant_matches={row['variant_matches']}"
        )


if __name__ == "__main__":
    main()
