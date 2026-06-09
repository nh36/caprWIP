#!/usr/bin/env python3
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT_PATH = ROOT / "reader_facing_chronology_evidence_check_01.md"
DEFAULT_SKIP = {
    "README.md",
    "style_guide.md",
    "source_note.md",
    "source_note_pilot_02.md",
    "ai_style_audit_checklist.md",
    "reader_facing_pilot_01.md",
    "reader_facing_pilot_02.md",
    "reader_facing_pilot_02_report.md",
    "reader_facing_local_section_01.md",
    "reader_facing_local_section_01_report.md",
    "reader_facing_local_section_02.md",
    "reader_facing_local_section_02_report.md",
    "reader_facing_chronology_evidence_audit_01.md",
    "reader_facing_chronology_evidence_qc_01_report.md",
}

RULE_HEADING_RE = re.compile(r"^##\s+(SC\d{3}\.[^\n]+)$", re.M)
CODE_BLOCK_RE = re.compile(r"(?ms)^```.*?^```[ \t]*\n?")
RELATION_RE = re.compile(r"SC\d{3}\s*<\s*SC\d{3}")

MOVE_PATTERNS = [
    re.compile(r"if [^.]*moved", re.I),
    re.compile(r"when [^.]*moved", re.I),
    re.compile(r"if [^.]*delayed", re.I),
    re.compile(r"if [^.]*applied", re.I),
]
OUTPUT_PATTERNS = [
    re.compile(r"\byields?\b", re.I),
    re.compile(r"\bproduces?\b", re.I),
    re.compile(r"\bno output\b", re.I),
]
LIMITATION_PATTERNS = [
    re.compile(r"no exact wrong", re.I),
    re.compile(r"no single .* wrong form", re.I),
    re.compile(r"no comparably sharp", re.I),
    re.compile(r"no explicit .* boundary", re.I),
    re.compile(r"no positive .* boundary", re.I),
    re.compile(r"boundary-limited", re.I),
    re.compile(r"one-sided", re.I),
    re.compile(r"no decisive wrong form", re.I),
]


@dataclass
class SectionCheck:
    file_name: str
    heading: str
    has_move: bool
    has_expected: bool
    has_output: bool
    has_boundary: bool
    has_limitation: bool
    warnings: list[str]


def iter_target_files() -> list[Path]:
    return [path for path in sorted(ROOT.glob("*.md")) if path.name not in DEFAULT_SKIP]


def split_sections(text: str) -> list[tuple[str, str]]:
    matches = list(RULE_HEADING_RE.finditer(text))
    sections: list[tuple[str, str]] = []
    for idx, match in enumerate(matches):
        heading = match.group(1).strip()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        body = text[start:end]
        sections.append((heading, body))
    return sections


def strip_code(text: str) -> str:
    return CODE_BLOCK_RE.sub("", text)


def check_section(file_name: str, heading: str, body: str) -> SectionCheck:
    prose = strip_code(body)
    has_move = any(pattern.search(prose) for pattern in MOVE_PATTERNS)
    has_expected = "expected" in prose.lower()
    has_output = any(pattern.search(prose) for pattern in OUTPUT_PATTERNS)
    has_boundary = "boundary" in prose.lower() or bool(RELATION_RE.search(prose))
    has_limitation = any(pattern.search(prose) for pattern in LIMITATION_PATTERNS)

    warnings: list[str] = []
    if not has_move:
        warnings.append("missing move-condition wording")
    if not has_output and not has_limitation:
        warnings.append("missing explicit wrong-output/result wording")
    if not has_expected and not has_limitation:
        warnings.append("missing expected-form wording")
    if not has_boundary and not has_limitation:
        warnings.append("missing explicit boundary conclusion")

    return SectionCheck(
        file_name=file_name,
        heading=heading,
        has_move=has_move,
        has_expected=has_expected,
        has_output=has_output,
        has_boundary=has_boundary,
        has_limitation=has_limitation,
        warnings=warnings,
    )


def render_report(results: list[SectionCheck]) -> str:
    warning_count = sum(1 for result in results if result.warnings)
    lines = [
        "# Reader-facing chronology evidence check 01",
        "",
        "_Generated from the current SC-numbered rule sections in the reader-facing chapter files._",
        "",
        "## Summary",
        "",
        f"- Sections checked: {len(results)}.",
        f"- Sections with warnings: {warning_count}.",
        "",
        "| File | Rule section | Move wording | Expected form | Wrong output/result | Boundary wording | Limitation wording | Warnings |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    for result in results:
        lines.append(
            "| "
            + " | ".join(
                [
                    result.file_name,
                    result.heading,
                    "yes" if result.has_move else "no",
                    "yes" if result.has_expected else "no",
                    "yes" if result.has_output else "no",
                    "yes" if result.has_boundary else "no",
                    "yes" if result.has_limitation else "no",
                    "; ".join(result.warnings) if result.warnings else "—",
                ]
            )
            + " |"
        )

    return "\n".join(lines) + "\n"


def main() -> int:
    results: list[SectionCheck] = []
    for path in iter_target_files():
        text = path.read_text(encoding="utf-8")
        for heading, body in split_sections(text):
            results.append(check_section(path.name, heading, body))

    OUTPUT_PATH.write_text(render_report(results), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")
    warning_count = sum(1 for result in results if result.warnings)
    print(f"Sections checked: {len(results)}; warnings: {warning_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
