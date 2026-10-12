#!/usr/bin/env python3
"""Read-only research bridge; generated views are written only by adjudicate --refresh."""
from __future__ import annotations

import argparse
import csv
import io
from collections import Counter, defaultdict
from pathlib import Path

import cascade_baseline
import oe_lexeme_report_coverage as coverage
import pgmc_reconstruction_survey as survey

ROOT = survey.ROOT
DIRECTORY = Path("Germanic/docs/lexeme_reports/pgmc_integration")
CATEGORIES = {
    "substantive_disagreement", "qualified_alternative",
    "non_substantive_difference", "no_special_discussion",
}
CASE_FIELDS = [
    "case_id", "row_id", "scope", "category", "evidence_ids",
    "judgement", "missing_premise", "example_path",
    "requires_extended_discussion", "publication_source",
]
OUTPUT_NAMES = ("population_crosswalk.tsv", "editorial_inventory.tsv", "population_summary.md")


def table(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def unique(rows: list[dict[str, str]], key: str, label: str) -> dict:
    result = {}
    for row in rows:
        identifier = row[key]
        if not identifier or identifier in result:
            raise ValueError(f"{label}: empty or duplicate {key}: {identifier}")
        result[identifier] = row
    return result


def tsv(rows: list[dict], fields: list[str]) -> str:
    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue()


def load_cases(root: Path, corpus: dict, forms: dict) -> list[dict]:
    path = root / DIRECTORY / "editorial_cases.tsv"
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != CASE_FIELDS:
            raise ValueError("editorial case header mismatch")
        cases = list(reader)
    unique(cases, "case_id", "editorial SOURCE")
    for case in cases:
        row_id = case["row_id"]
        if row_id not in corpus or case["category"] not in CATEGORIES:
            raise ValueError(f"invalid editorial row/category: {case['case_id']}")
        if not case["scope"] or not case["judgement"]:
            raise ValueError(f"missing scoped judgement: {case['case_id']}")
        if case["category"] == "qualified_alternative" and not case["missing_premise"]:
            raise ValueError(f"qualified alternative needs its missing premise: {case['case_id']}")
        selected = case["requires_extended_discussion"]
        if selected not in {"0", "1"}:
            raise ValueError(f"explicit editorial decision required: {case['case_id']}")
        if selected == "1":
            if case["category"] not in {"substantive_disagreement", "qualified_alternative"}:
                raise ValueError(f"non-substantive case cannot require extended discussion: {case['case_id']}")
            source = Path(case["publication_source"])
            if (not case["publication_source"] or source.is_absolute() or ".." in source.parts
                    or source.parts[0] not in {"model_entries", "research_memos"}
                    or not source.name.startswith(row_id + "-") or source.suffix != ".md"):
                raise ValueError(f"unsafe or wrong-row publication source: {case['case_id']}")
            if not (root / "Germanic/docs/lexeme_reports" / source).is_file():
                raise ValueError(f"missing publication source: {source}")
        elif case["publication_source"]:
            raise ValueError(f"unselected case has publication source: {case['case_id']}")
        evidence_ids = survey.ids(case["evidence_ids"])
        if not evidence_ids:
            raise ValueError(f"uncited editorial judgement: {case['case_id']}")
        for evidence_id in evidence_ids:
            form = forms.get(evidence_id)
            if form is None or row_id not in survey.ids(form["row_ids"]):
                raise ValueError(f"wrong-row editorial evidence: {case['case_id']}/{evidence_id}")
            if not form["printed_pages"] or not form["source_key"]:
                raise ValueError(f"missing source/page: {evidence_id}")
        if case["example_path"]:
            relative = Path(case["example_path"])
            if relative.is_absolute() or ".." in relative.parts or relative.parts[:1] != ("examples",):
                raise ValueError(f"unsafe provisional example path: {relative}")
            prose = (root / DIRECTORY / relative).read_text(encoding="utf-8")
            for field in ("proto", "protoform"):
                if "\\emph{" + corpus[row_id][field] + "}" not in prose:
                    raise ValueError(f"example {relative} omits live {field}")
            if corpus[row_id]["target"] not in prose:
                raise ValueError(f"example {relative} omits live target")
    return cases


def publication_sources(root: Path = ROOT) -> dict[str, tuple[str, list[str]]]:
    """Reuse the sole scoped judgement owner, never audit routing or type tags."""
    audit = root / survey.DIRECTORY
    corpus = unique(table(audit / "corpus_inventory.tsv"), "row_id", "audit population")
    forms = unique(table(audit / "forms.tsv"), "evidence_id", "audit evidence")
    selected: dict[str, tuple[str, list[str]]] = {}
    for case in load_cases(root, corpus, forms):
        if case["requires_extended_discussion"] != "1":
            continue
        row_id, source = case["row_id"], case["publication_source"]
        if corpus[row_id]["runnable"] != "1":
            raise ValueError(f"research-only editorial publication: {row_id}")
        if row_id in selected and selected[row_id][0] != source:
            raise ValueError(f"competing publication owners for row {row_id}")
        selected.setdefault(row_id, (source, []))[1].append(case["case_id"])
    return selected


def screen(comparisons: list[dict]) -> str:
    """Route inspection, never infer an editorial verdict from audit flags."""
    if any(c["scope"] != "core_triage" and c["comparability"] == "substantive_difference"
           for c in comparisons):
        return "focused_comparison_review"
    if any(c["comparability"] == "substantive_difference" for c in comparisons):
        return "candidate_comparison_review"
    if any(c["comparability"] == "different_units" for c in comparisons):
        return "unit_comparability_review"
    return "ordinary_evidence_review"


def build(root: Path = ROOT, *, mode: str = "full") -> tuple[list[dict], list[dict], dict]:
    corpus_rows, _, form_rows, reviews = survey.load(root, mode=mode)
    analytical = survey.load_analysis(root, corpus_rows, form_rows)
    corpus = unique(corpus_rows, "row_id", "live audit population")
    forms = unique(form_rows, "evidence_id", "audit evidence")
    cases = load_cases(root, corpus, forms)
    base = root / "Germanic/docs/sound_changes/cascade_baseline"
    current = table(base / "cascade_baseline_outputs.tsv")
    baseline = unique(current, "row_id", "selected baseline")
    legacy = cascade_baseline.legacy_subset(
        current, table(base / "cascade_baseline_outputs_legacy380.tsv"),
        table(base / "approved_input_migrations.tsv"))
    legacy_ids = {row["row_id"] for row in legacy}
    runnable = {row_id for row_id, row in corpus.items() if row["runnable"] == "1"}
    if set(baseline) != runnable:
        raise ValueError("selected baseline and runnable audit IDs differ")
    for row_id in runnable:
        row, record = corpus[row_id], baseline[row_id]
        if (row["protoform"], row["target"], row["concept"]) != (
                record["proto"], record["counterpart"], record["concept"]):
            raise ValueError(f"baseline/live selected identity differs: {row_id}")
    reports = root / "Germanic/docs/lexeme_reports"
    oe_rows = coverage.load_oe_rows(root / "Germanic/data/germanic-aligned-final.tsv")
    oe = unique([vars(r) for r in oe_rows], "row_id", "report population")
    if set(oe) != runnable:
        raise ValueError("live report population and runnable IDs differ")
    manifest = coverage.load_manifest(reports / "report_manifest.tsv")
    diagnostics, _ = coverage.apply_manifest(
        oe_rows, manifest, reports, coverage.load_report_files(reports))
    if diagnostics:
        raise ValueError("; ".join(diagnostics))
    models = unique(table(root / "Germanic/docs/assembly/manifest_all_by_class.tsv"),
                    "row_id", "lexical assembly")
    for row_id, model in models.items():
        if row_id not in runnable:
            raise ValueError(f"non-runnable model ID: {row_id}")
        row = corpus[row_id]
        if (model["proto"], model["protoform"], model["counterpart"],
                model["derivation_class"]) != (
                row["proto"], row["protoform"], row["target"], row["derivation_class"]):
            raise ValueError(f"model/live identity mismatch: {row_id}")
        if not (root / model["model_entry_path"]).is_file():
            raise ValueError(f"missing model entry: {row_id}")
    material = defaultdict(list)
    for directory in ("packets", "research_memos", "dev_notes_slices", "model_entries"):
        for path in sorted((reports / directory).glob("*.md")):
            prefix = path.name.split("-", 1)[0]
            if prefix in corpus:
                material[prefix].append(path.relative_to(root).as_posix())
    comparisons_by_row = defaultdict(list)
    for comparison in analytical["comparisons"]:
        for row_id in survey.ids(comparison["row_ids"]):
            comparisons_by_row[row_id].append(comparison)
    cases_by_row = defaultdict(list)
    for case in cases:
        cases_by_row[case["row_id"]].append(case)
    review_counts = Counter(review["row_id"] for review in reviews)
    form_counts = Counter(row_id for form in form_rows for row_id in survey.ids(form["row_ids"]))
    crosswalk, inventory = [], []
    for row_id in sorted(corpus, key=int):
        row = corpus[row_id]
        report = next((r for r in oe_rows if r.row_id == row_id), None)
        selected_cases = cases_by_row[row_id]
        core = next(c for c in comparisons_by_row[row_id] if c["scope"] == "core_triage")
        crosswalk.append({
            "row_id": row_id, "concept": row["concept"], "target": row["target"],
            "legacy380": int(row_id in legacy_ids), "selected387": int(row_id in runnable),
            "audit393": 1, "proto": row["proto"], "proto_stage": row["proto_stage"],
            "protoform": row["protoform"], "input_stage": row["input_stage"],
            "input_variety": row["input_variety"], "stage_basis": row["stage_basis"],
            "word_stress": row["word_stress"], "phonological_finality": row["phonological_finality"],
            "derivation_class": row["derivation_class"],
            "documented_outputs": baseline[row_id]["outputs"] if row_id in baseline else "",
            "audit_alignment": core["alignment_status"], "audit_evidence_count": form_counts[row_id],
            "actual_source_reviews": review_counts[row_id],
            "old_policy_requires_report": int(report.requires_report) if report else 0,
            "old_policy_basis": report.requirement_basis if report else "research_only",
            "production_manifest_status": report.production_status if report else "-",
            "production_manifest_paths": ";".join(report.manifest_report_paths) if report else "",
            "assembled_model_path": models.get(row_id, {}).get("model_entry_path", ""),
            "stable_id_material_paths": ";".join(material[row_id]),
            "editorial_case_ids": ";".join(c["case_id"] for c in selected_cases),
        })
        inventory.append({
            "row_id": row_id, "concept": row["concept"], "screen_route": screen(comparisons_by_row[row_id]),
            "editorial_review": "scoped_review" if selected_cases else "not_editorially_reviewed",
            "reviewed_categories": ";".join(sorted({c["category"] for c in selected_cases})),
            "case_ids": ";".join(c["case_id"] for c in selected_cases),
            "comparison_ids": ";".join(c["comparison_id"] for c in comparisons_by_row[row_id]),
            "remaining_audit_premise": core["alignment_limits"],
            "requires_extended_discussion": int(any(c["requires_extended_discussion"] == "1"
                                                     for c in selected_cases)),
            "publication_source": ";".join(sorted({c["publication_source"] for c in selected_cases
                                                    if c["publication_source"]})),
        })
    required = {r.row_id for r in oe_rows if r.requires_report}
    philological = {c["row_id"] for c in cases if c["requires_extended_discussion"] == "1"}
    stats = {
        "audit": len(corpus), "selected": len(runnable), "legacy": len(legacy_ids),
        "required": len(required), "legacy_current_required": len(required & legacy_ids),
        "assembled": len(models), "production_pilots": sum(r.has_production_manifest_report for r in oe_rows),
        "format_tests": sum(r.has_format_test_manifest_report for r in oe_rows),
        "added_selected": sorted(runnable - legacy_ids, key=int),
        "research_only": sorted(set(corpus) - runnable, key=int),
        "required_not_assembled": sorted(required - set(models), key=int),
        "assembled_not_required": sorted(set(models) - required, key=int),
        "routes": dict(sorted(Counter(r["screen_route"] for r in inventory).items())),
        "reviewed_rows": len({case["row_id"] for case in cases}), "scoped_cases": len(cases),
        "philological_selected": len(philological),
        "pilot_current_required": len(required | philological),
    }
    return crosswalk, inventory, stats


def render(root: Path = ROOT, *, mode: str = "full") -> dict[Path, str]:
    crosswalk, inventory, stats = build(root, mode=mode)
    summary = [
        "# Population reconciliation (GENERATED)", "",
        "Authority: live corpus/sidecars, validated audit, exact approved legacy migrations,",
        "report manifest and class assembly manifest. Regenerate only with",
        "`python3 Germanic/tools/adjudicate.py --refresh`.", "",
        "| Measure | Count |", "| --- | ---: |",
    ]
    for key in ("legacy", "selected", "audit", "legacy_current_required", "required",
                "assembled", "production_pilots", "format_tests", "reviewed_rows", "scoped_cases",
                "philological_selected", "pilot_current_required"):
        summary.append(f"| {key} | {stats[key]} |")
    for key in ("added_selected", "research_only", "required_not_assembled", "assembled_not_required"):
        summary.extend(["", f"{key}: " + ", ".join(stats[key]) + "."])
    summary.extend(["", "## Automated inspection routes, not controversy counts", ""])
    for route, count in stats["routes"].items():
        summary.append(f"- {route}: {count}")
    summary.extend(["", "A scoped review is not whole-row closure. All other rows retain",
                    "not_editorially_reviewed; bounded_limit and type tags assign no editorial category.",
                    "required preserves the older selective policy; pilot_current_required also includes",
                    "explicit scoped philological decisions. Prototype examples remain outside production.",
                    "See README.md and the live report_schema.md for the pilot policy.", ""])
    return {
        root / DIRECTORY / OUTPUT_NAMES[0]: tsv(crosswalk, list(crosswalk[0])),
        root / DIRECTORY / OUTPUT_NAMES[1]: tsv(inventory, list(inventory[0])),
        root / DIRECTORY / OUTPUT_NAMES[2]: "\n".join(summary),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("full", "portable"), default="full")
    parser.add_argument("--check", action="store_true", help="check committed projection freshness without writing")
    args = parser.parse_args()
    try:
        rendered = render(mode=args.mode)
        if args.check:
            stale = [str(path.relative_to(ROOT)) for path, text in rendered.items()
                     if not path.exists() or path.read_text(encoding="utf-8") != text]
            if stale:
                raise ValueError("stale integration projections: " + ", ".join(stale))
        print(f"Validated {DIRECTORY}; {len(rendered)} projections; no scientific adoption.")
    except (ValueError, OSError, survey.SurveyError, survey.analytical.AnalysisError) as exc:
        parser.exit(1, f"integration error: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
