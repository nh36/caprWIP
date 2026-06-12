#!/usr/bin/env python3
from __future__ import annotations

import ast
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DEFAULT_BUILD_SCRIPT = ROOT / "build_reader_facing_local_section_08_docker.sh"
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


def iter_chapter_source_paths() -> list[Path]:
    return sorted(ROOT.glob("[0-9]*.md"))


def extract_embedded_python(build_script: Path) -> str:
    text = build_script.read_text(encoding="utf-8")
    match = re.search(r"python3 - <<'PY'\n(.*?)\nPY", text, re.S)
    if not match:
        raise ValueError(f"Could not find embedded Python block in {build_script}")
    return match.group(1)


def parse_python_list_assignment(build_script: Path, name: str) -> list[str]:
    module = ast.parse(extract_embedded_python(build_script))
    for node in module.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == name:
                    return list(ast.literal_eval(node.value))
        if isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name) and node.target.id == name and node.value is not None:
                return list(ast.literal_eval(node.value))
    raise ValueError(f"Could not find {name} list assignment in {build_script}")


def parse_chapter_files(build_script: Path) -> list[str]:
    return parse_python_list_assignment(build_script, "chapter_files")


def parse_intro_parts(build_script: Path) -> list[str]:
    parts = parse_python_list_assignment(build_script, "parts")
    if "## Introduction" not in parts:
        raise ValueError(f"Could not find ## Introduction marker in {build_script}")
    start = parts.index("## Introduction") + 1
    return [part for part in parts[start:] if part.strip() and not part.startswith("#")]


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


def build_all_source_rule_heading_map() -> dict[str, RuleHeading]:
    mapping: dict[str, RuleHeading] = {}
    for path in iter_chapter_source_paths():
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
