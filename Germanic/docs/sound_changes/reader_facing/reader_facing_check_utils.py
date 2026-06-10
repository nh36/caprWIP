#!/usr/bin/env python3
from __future__ import annotations

import ast
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DEFAULT_BUILD_SCRIPT = ROOT / "build_reader_facing_local_section_03_docker.sh"
RULE_HEADING_RE = re.compile(
    r"^##\s+(SC\d{3})\.\s+(.*?)\s+\(`([^`]+)`\)\s+\{#(rule-[^}]+)\}\s*$"
)
CODE_FENCE_RE = re.compile(r"(?ms)^```.*?^```[ \t]*\n?")


@dataclass(frozen=True)
class RuleHeading:
    file_name: str
    sc_number: str
    title: str
    rule_name: str
    anchor: str


def parse_chapter_files(build_script: Path) -> list[str]:
    text = build_script.read_text(encoding="utf-8")
    match = re.search(r"chapter_files\s*=\s*(\[[^\]]*\])", text, re.S)
    if not match:
        raise ValueError(f"Could not find chapter_files list in {build_script}")
    return list(ast.literal_eval(match.group(1)))


def iter_build_chapter_paths(build_script: Path = DEFAULT_BUILD_SCRIPT) -> list[Path]:
    return [ROOT / name for name in parse_chapter_files(build_script)]


def extract_rule_headings(path: Path) -> list[RuleHeading]:
    headings: list[RuleHeading] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = RULE_HEADING_RE.match(line.strip())
        if match:
            headings.append(
                RuleHeading(
                    file_name=path.name,
                    sc_number=match.group(1),
                    title=match.group(2),
                    rule_name=match.group(3),
                    anchor=f"#{match.group(4)}",
                )
            )
    if not headings:
        raise ValueError(f"No SC-numbered rule headings found in {path}")
    return headings


def build_rule_heading_map(build_script: Path = DEFAULT_BUILD_SCRIPT) -> dict[str, RuleHeading]:
    mapping: dict[str, RuleHeading] = {}
    for path in iter_build_chapter_paths(build_script):
        for heading in extract_rule_headings(path):
            if heading.anchor in mapping:
                raise ValueError(f"Duplicate rule anchor {heading.anchor} in {path}")
            mapping[heading.anchor] = heading
    return mapping


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _mask_preserving_newlines(text: str) -> str:
    return "".join("\n" if char == "\n" else " " for char in text)


def mask_fenced_code(text: str) -> str:
    return CODE_FENCE_RE.sub(lambda match: _mask_preserving_newlines(match.group(0)), text)


def mask_spans(text: str, spans: list[tuple[int, int]]) -> str:
    if not spans:
        return text
    chars = list(text)
    for start, end in spans:
        for idx in range(start, end):
            if chars[idx] != "\n":
                chars[idx] = " "
    return "".join(chars)
