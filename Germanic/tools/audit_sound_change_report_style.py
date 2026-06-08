#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]
REPORTS_DIR = REPO_ROOT / "Germanic/docs/sound_changes/change_reports"
MANIFEST_PATH = REPORTS_DIR / "report_manifest.tsv"
SCAFFOLD_PATH = REPORTS_DIR / "sound_change_half_scaffold.tsv"
STYLE_STANDARD_PATH = REPORTS_DIR / "STYLE_STANDARD.md"
OUTPUT_PATH = REPORTS_DIR / "sound_change_style_audit.md"

PRODUCTION_STATUSES = {"pilot", "full"}
REQUIRED_HEADINGS = [
    "Historical formulation",
    "Source tradition",
    "CAPR implementation",
    "Place in the cascade",
    "Order evidence",
    "Interpretation",
    "Remaining cautions",
]

FENCED_CODE_BLOCK_RE = re.compile(r"(?ms)^```[^\n]*\n.*?^```[ \t]*\n?")
PROJECT_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("promotion language", re.compile(r"\bpromot(?:e|ed|es|ion)\b", re.IGNORECASE)),
    ("production-report language", re.compile(r"\bproduction\s+report\b", re.IGNORECASE)),
    ("production-prose language", re.compile(r"\bproduction\s+prose\b", re.IGNORECASE)),
    ("pilot-corridor language", re.compile(r"\bpilot\s+corridor\b", re.IGNORECASE)),
    ("assembled-half language", re.compile(r"\bassembled\s+half\b", re.IGNORECASE)),
    ("chapter-architecture language", re.compile(r"\bchapter\s+architecture\b", re.IGNORECASE)),
    ("book-architecture language", re.compile(r"\bbook\s+architecture\b", re.IGNORECASE)),
    ("finished-prose language", re.compile(r"\bfinished\s+prose\b", re.IGNORECASE)),
    ("final-printed-version language", re.compile(r"\bfinal\s+printed\s+version\b", re.IGNORECASE)),
    ("book-facing language", re.compile(r"\bbook-facing\b", re.IGNORECASE)),
    ("reader-facing language", re.compile(r"\breader-facing\b", re.IGNORECASE)),
    ("model-facing language", re.compile(r"\bmodel-facing\b", re.IGNORECASE)),
]
RAW_FOMA_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("inline rewrite rule", re.compile(r"\{[^{}\n]+\}\s*->\s*[^`\n]+?\|\|")),
    ("inline compose chain", re.compile(r"(?m)^\s*\.o\.\s+\S+")),
    ("inline define statement", re.compile(r"(?m)^\s*define\s+\S+")),
]
BARE_RULE_NAME_RE = re.compile(
    r"(?<![`A-Za-z])\b(?:OE|PGmc|PWGmc|NWGmc|WGmc|Angl|WS)[A-Z][A-Za-z]+(?:[A-Z][A-Za-z]+)+\b(?!`)"
)
UNBACKTICKED_RELATION_RE = re.compile(r"(?<!`)SC\d{3}(?:\s*(?:<|>|=)\s*SC\d{3})+(?!`)")
UNBACKTICKED_RANGE_RE = re.compile(r"(?<!`)SC\d{3}-SC\d{3}(?!`)")


@dataclass(frozen=True)
class Issue:
    category: str
    label: str
    count: int
    examples: tuple[str, ...]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def extract_sections(text: str) -> dict[str, str]:
    heading_matches = list(re.finditer(r"^#### (.+)$", text, re.MULTILINE))
    sections: dict[str, str] = {}
    for idx, match in enumerate(heading_matches):
        heading = match.group(1).strip()
        start = match.end()
        end = heading_matches[idx + 1].start() if idx + 1 < len(heading_matches) else len(text)
        sections[heading] = text[start:end].strip()
    return sections


def strip_fenced_code(text: str) -> str:
    return FENCED_CODE_BLOCK_RE.sub("", text)


def collect_pattern_issue(
    category: str,
    label: str,
    pattern: re.Pattern[str],
    text: str,
    max_examples: int = 3,
    ignore_negated: bool = False,
) -> Issue | None:
    matches = list(pattern.finditer(text))
    if ignore_negated:
        matches = [match for match in matches if not looks_negated(text, match.start())]
    if not matches:
        return None
    examples = tuple(sorted({match.group(0).strip() for match in matches})[:max_examples])
    return Issue(category=category, label=label, count=len(matches), examples=examples)


def sentence_window(text: str, start: int) -> str:
    sentence_start = max(
        text.rfind(".", 0, start),
        text.rfind("!", 0, start),
        text.rfind("?", 0, start),
        text.rfind(":", 0, start),
    )
    next_candidates = [
        pos
        for pos in (
            text.find(".", start),
            text.find("!", start),
            text.find("?", start),
        )
        if pos != -1
    ]
    sentence_end = min(next_candidates) if next_candidates else len(text)
    window = text[max(0, sentence_start) : sentence_end].lower()
    return window.replace("*", "").replace("`", "")


def looks_negated(text: str, start: int) -> bool:
    window = sentence_window(text, start)
    return any(
        marker in window
        for marker in (
            " not ",
            " no ",
            " without ",
            " rather than ",
            " do not ",
            " does not ",
            " should not ",
            " must not ",
            "no positive",
            "rewritten",
            "turned into",
        )
    )


def looks_runner_context(text: str, start: int) -> bool:
    window = sentence_window(text, start)
    return any(marker in window for marker in ("runner", "pwgmcchanges", "sc087"))


def chronology_issues(text: str, chronology_status: str) -> list[Issue]:
    lowered = chronology_status.lower()
    issues: list[Issue] = []
    stripped_text = strip_fenced_code(text)
    if (
        "boundary-limited" in lowered
        or "negative" in lowered
        or "runner-bounded" in lowered
        or "broad/far" in lowered
    ):
        claim_issue = collect_pattern_issue(
            "chronology wording",
            "must-precede-sc087 claim",
            re.compile(r"\bmust (?:historically )?(?:precede|follow) SC087\b", re.IGNORECASE),
            stripped_text,
            ignore_negated=True,
        )
        if claim_issue:
            issues.append(claim_issue)
    if "runner-bounded" in lowered:
        matches = [
            match
            for match in re.finditer(r"\bhistorical (?:left|right)? ?boundary\b", stripped_text, re.IGNORECASE)
            if not looks_negated(stripped_text, match.start()) and looks_runner_context(stripped_text, match.start())
        ]
        if matches:
            examples = tuple(sorted({match.group(0).strip() for match in matches})[:3])
            issues.append(
                Issue(
                    "chronology wording",
                    "historical-boundary claim in runner-bounded unit",
                    len(matches),
                    examples,
                )
            )
    return issues


def structural_issues(text: str) -> list[Issue]:
    issues: list[Issue] = []
    if "### Sound-change report" not in text:
        issues.append(Issue("structure", "missing report wrapper", 1, ("### Sound-change report",)))

    headings = re.findall(r"^#### (.+)$", text, re.MULTILINE)
    counts = Counter(headings)

    missing = [heading for heading in REQUIRED_HEADINGS if counts[heading] == 0]
    if missing:
        issues.append(Issue("structure", "missing required headings", len(missing), tuple(missing)))

    duplicated = [heading for heading in REQUIRED_HEADINGS if counts[heading] > 1]
    if duplicated:
        issues.append(Issue("structure", "duplicated required headings", len(duplicated), tuple(duplicated)))

    unexpected = [heading for heading in headings if heading not in REQUIRED_HEADINGS]
    if unexpected:
        deduped = tuple(sorted(dict.fromkeys(unexpected)))
        issues.append(Issue("structure", "unexpected section headings", len(deduped), deduped))

    sections = extract_sections(text)
    empty = [heading for heading in REQUIRED_HEADINGS if heading in sections and not sections[heading].strip()]
    if empty:
        issues.append(Issue("structure", "empty sections", len(empty), tuple(empty)))

    ordered_present = [heading for heading in headings if heading in REQUIRED_HEADINGS]
    if ordered_present and ordered_present != REQUIRED_HEADINGS:
        issues.append(
            Issue(
                "structure",
                "section-order drift",
                1,
                (" -> ".join(ordered_present),),
            )
        )
    return issues


def prose_issues(text: str, chronology_status: str) -> list[Issue]:
    issues: list[Issue] = []
    stripped = strip_fenced_code(text)
    for label, pattern in PROJECT_PATTERNS:
        issue = collect_pattern_issue("project-facing wording", label, pattern, stripped)
        if issue:
            issues.append(issue)

    for label, pattern in RAW_FOMA_PATTERNS:
        issue = collect_pattern_issue("raw FOMA prose", label, pattern, stripped)
        if issue:
            issues.append(issue)

    drift_checks = [
        ("bare CamelCase rule name", BARE_RULE_NAME_RE),
        ("unbackticked change relation", UNBACKTICKED_RELATION_RE),
        ("unbackticked change range", UNBACKTICKED_RANGE_RE),
    ]
    for label, pattern in drift_checks:
        issue = collect_pattern_issue("formatting drift", label, pattern, stripped)
        if issue:
            issues.append(issue)

    issues.extend(chronology_issues(text, chronology_status))
    return issues


def audit_report(row: dict[str, str], chronology_status: str) -> list[Issue]:
    source_path = REPORTS_DIR / (row.get("REPORT_PATH") or "").strip()
    text = source_path.read_text(encoding="utf-8")
    return structural_issues(text) + prose_issues(text, chronology_status)


def build_report(audited: list[tuple[dict[str, str], str, list[Issue]]]) -> str:
    all_issues = [issue for _, _, issues in audited for issue in issues]
    category_counts = Counter(issue.category for issue in all_issues)
    issue_total = sum(issue.count for issue in all_issues)
    reports_with_issues = sum(1 for _, _, issues in audited if issues)

    lines = [
        "# Sound-change report style audit",
        "",
        "_Generated from `report_manifest.tsv`, `sound_change_half_scaffold.tsv`, and `STYLE_STANDARD.md`._",
        "",
        "## Summary",
        "",
        f"- Reports checked: {len(audited)}.",
        f"- Reports with one or more findings: {reports_with_issues}.",
        f"- Total findings counted: {issue_total}.",
        f"- Structure findings: {category_counts.get('structure', 0)}.",
        f"- Project-facing wording findings: {category_counts.get('project-facing wording', 0)}.",
        f"- Chronology-wording findings: {category_counts.get('chronology wording', 0)}.",
        f"- Raw FOMA prose findings: {category_counts.get('raw FOMA prose', 0)}.",
        f"- Formatting-drift findings: {category_counts.get('formatting drift', 0)}.",
        "",
        "## Findings by report",
        "",
    ]

    clean_reports = 0
    for row, chronology_status, issues in audited:
        unit_id = (row.get("ID") or "").strip()
        title = (row.get("TITLE") or "").strip()
        report_path = (row.get("REPORT_PATH") or "").strip()
        status = (row.get("STATUS") or "").strip()
        if not issues:
            clean_reports += 1
            continue
        lines.extend(
            [
                f"### {unit_id} — {title}",
                "",
                f"- Status: `{status}`",
                f"- Report path: `{report_path}`",
                f"- Chronology status: {chronology_status}",
            ]
        )
        grouped: dict[str, list[Issue]] = {}
        for issue in issues:
            grouped.setdefault(issue.category, []).append(issue)
        for category, category_issues in grouped.items():
            lines.append(f"- {category.capitalize()}:")
            for issue in category_issues:
                example_text = "; ".join(issue.examples)
                lines.append(f"  - {issue.label} ({issue.count}): {example_text}")
        lines.append("")

    if clean_reports:
        lines.extend(
            [
                "## Reports with no findings",
                "",
                f"- {clean_reports} report(s) matched the current audit without findings.",
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    if not STYLE_STANDARD_PATH.exists():
        raise FileNotFoundError(f"Missing style standard: {STYLE_STANDARD_PATH}")

    manifest_rows = [
        row
        for row in read_tsv(MANIFEST_PATH)
        if (row.get("STATUS") or "").strip() in PRODUCTION_STATUSES
    ]
    scaffold_rows = {row.get("UNIT_ID") or "": row for row in read_tsv(SCAFFOLD_PATH)}

    audited: list[tuple[dict[str, str], str, list[Issue]]] = []
    for row in manifest_rows:
        unit_id = (row.get("ID") or "").strip()
        scaffold_row = scaffold_rows.get(unit_id)
        if scaffold_row is None:
            raise KeyError(f"Missing scaffold row for manifest unit {unit_id}")
        chronology_status = (scaffold_row.get("CHRONOLOGY_STATUS") or "").strip()
        audited.append((row, chronology_status, audit_report(row, chronology_status)))

    OUTPUT_PATH.write_text(build_report(audited), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
