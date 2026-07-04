#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
AUDIT_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_audit.md"
BASELINE_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_unresolved_baseline.tsv"
PRINT_MAIN_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_main.tsv"
PRINT_DECISIONS_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_decisions.tsv"
PRINT_ANOMALIES_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_anomalies.tsv"
LANGUAGE_REGISTRY_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_languages.tsv"
TEX_CHECK_SCRIPT_PATH = REPO_ROOT / "Germanic/tools/check_book_draft_tex_indexes.py"
DEFAULT_TEX_PATH = REPO_ROOT / "Germanic/docs/assembly/capr_book_draft_alpha_01.tex"
DEFAULT_TOC_PATH = REPO_ROOT / "Germanic/docs/assembly/capr_book_draft_alpha_01.toc"
PROSE_RULE_WORDS = {"form", "output", "expected", "stage", "rule"}


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_language_titles() -> dict[str, str]:
    rows = load_rows(LANGUAGE_REGISTRY_PATH)
    return {(row.get("code") or "").strip(): (row.get("title") or "").strip() for row in rows}


def parse_toc_titles(toc_text: str) -> list[str]:
    titles: list[str] = []
    pattern = re.compile(r"\\contentsline\s*\{[^}]+\}\{\s*(?:\\numberline\s*\{[^}]*\})?([^}]*)\}\{[^}]*\}")
    for match in pattern.finditer(toc_text):
        titles.append(match.group(1).strip())
    return titles


def normalized_token(value: str) -> str:
    return value.casefold().lstrip("*").strip("`.,;:!?()[]{}\"' ")


def audit_summary_value(label: str) -> int:
    pattern = re.compile(rf"^- {re.escape(label)}: (\d+)$", re.M)
    match = pattern.search(AUDIT_PATH.read_text(encoding="utf-8"))
    if not match:
        raise AssertionError(f"Missing audit summary line for '{label}'.")
    return int(match.group(1))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tex-path", type=Path, default=DEFAULT_TEX_PATH)
    parser.add_argument("--toc-path", type=Path, default=DEFAULT_TOC_PATH)
    args = parser.parse_args()

    assert audit_summary_value("True remaining unresolved") == 0
    assert audit_summary_value("Table-scanned unresolved candidates") == 0

    with BASELINE_PATH.open(encoding="utf-8") as handle:
        baseline_rows = list(csv.DictReader(handle, delimiter="\t"))
    assert not baseline_rows, "Unresolved baseline must remain empty apart from header."

    print_main_rows = load_rows(PRINT_MAIN_PATH)
    print_decisions = load_rows(PRINT_DECISIONS_PATH)
    print_anomaly_rows = load_rows(PRINT_ANOMALIES_PATH)
    language_titles = load_language_titles()

    explicit_regular_include_keys = {
        (
            (row.get("language") or "").strip(),
            (row.get("form") or "").strip(),
            (row.get("form_role") or "").strip(),
            (row.get("source_ref") or "").strip(),
        )
        for row in print_decisions
        if (row.get("action") or "").strip() == "include_main"
        and (row.get("form_role") or "").strip() == "regular_output"
    }

    for row in print_main_rows:
        assert row.get("language") != "preoe", f"preoe row leaked into print_main: {row}"
        assert not (row.get("source_scope") or "").startswith("reader_failure_"), f"reader_failure row leaked into print_main: {row}"
        if row.get("form_role") == "regular_output":
            key = (row.get("language", ""), row.get("form", ""), row.get("form_role", ""), row.get("source_ref", ""))
            assert key in explicit_regular_include_keys, f"Uncurated regular_output row leaked into print_main: {row}"
        assert ">" not in (row.get("form") or "") and ">" not in (row.get("display") or ""), f"Derivational expression leaked into print_main: {row}"
        display_token = normalized_token(row.get("display", ""))
        form_token = normalized_token(row.get("form", ""))
        assert display_token not in PROSE_RULE_WORDS and form_token not in PROSE_RULE_WORDS, f"Prose/rule token leaked into print_main: {row}"
        assert not re.fullmatch(r"SC\d{2,4}", row.get("display", "")), f"Rule label leaked into print_main: {row}"
        assert not re.fullmatch(r"SC\d{2,4}", row.get("form", "")), f"Rule label leaked into print_main: {row}"

    hard_anomalies = [row for row in print_anomaly_rows if (row.get("hard_error") or "").strip() == "yes"]
    assert not hard_anomalies, f"Hard print anomalies remain: {len(hard_anomalies)}"

    toc_path = args.toc_path.expanduser().resolve()
    if toc_path.exists():
        toc_text = toc_path.read_text(encoding="utf-8")
        toc_titles = parse_toc_titles(toc_text)
        assert "Index verborum" in toc_titles, "Expected Index verborum entry in ToC."
        print_languages = sorted({(row.get("language") or "").strip() for row in print_main_rows if (row.get("language") or "").strip()})
        for code in print_languages:
            title = language_titles.get(code, "")
            if not title:
                continue
            assert title not in toc_titles, f"Per-language index heading leaked into ToC: {title}"

    tex_path = args.tex_path.expanduser().resolve()
    if not tex_path.exists():
        raise AssertionError(f"TeX file not found for print-ready checks: {tex_path}")
    subprocess.run(
        [sys.executable, str(TEX_CHECK_SCRIPT_PATH), "--tex-path", str(tex_path)],
        cwd=REPO_ROOT,
        check=True,
    )

    print("print index readiness checks passed")


if __name__ == "__main__":
    main()
