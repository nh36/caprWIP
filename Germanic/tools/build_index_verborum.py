#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
BOOK_DIR = REPO_ROOT / "Germanic/docs/book"
ASSEMBLY_DIR = REPO_ROOT / "Germanic/docs/assembly"
INTRO_PATH = ASSEMBLY_DIR / "capr_book_intro_alpha_01.md"
README_PATH = BOOK_DIR / "index_verborum_README.md"
MANIFEST_PATH = ASSEMBLY_DIR / "manifest_all_by_class.tsv"
COMPACT_PATH = REPO_ROOT / "Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md"
CHRONOLOGY_PATH = REPO_ROOT / "Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.md"
MODEL_ENTRIES_DIR = REPO_ROOT / "Germanic/docs/lexeme_reports/model_entries"
FORMS_PATH = BOOK_DIR / "index_verborum_forms.tsv"
OVERRIDES_PATH = BOOK_DIR / "index_verborum_overrides.tsv"
AUDIT_PATH = BOOK_DIR / "index_verborum_audit.md"
UNRESOLVED_BASELINE_PATH = BOOK_DIR / "index_verborum_unresolved_baseline.tsv"
LANGUAGE_REGISTRY_PATH = BOOK_DIR / "index_verborum_languages.tsv"
INDEX_HEADER_PATH = ASSEMBLY_DIR / "book_draft_index_registry.tex"

PRODUCTION_FIELDS = [
    "language",
    "form",
    "display",
    "sort_key",
    "form_role",
    "source_scope",
    "source_ref",
    "origin",
    "status",
]
OVERRIDE_FIELDS = [
    "action",
    "language",
    "form",
    "display",
    "sort_key",
    "source_scope",
    "source_ref",
    "note",
]


def load_language_registry() -> tuple[list[dict[str, str]], list[str], dict[str, str], dict[str, str]]:
    with LANGUAGE_REGISTRY_PATH.open(encoding="utf-8") as handle:
        rows = [
            {key: (value or "").strip() for key, value in row.items()}
            for row in csv.DictReader(handle, delimiter="\t")
        ]
    order = [row["code"] for row in rows]
    titles = {row["code"]: row["title"] for row in rows}
    columns = {row["code"]: row["columns"] for row in rows}
    return rows, order, titles, columns


LANGUAGE_REGISTRY, LANGUAGE_ORDER, LANGUAGE_TITLES, LANGUAGE_COLUMNS = load_language_registry()
KNOWN_LANGUAGE_CODES = {row["code"] for row in LANGUAGE_REGISTRY}
ALLOWED_FORM_ROLES = {
    "evidence_form",
    "source_protoform",
    "selected_input",
    "target_form",
    "comparison_form",
    "regular_output",
}
FORM_RE = re.compile(r"[*A-Za-zÀ-ɏḀ-ỿͰ-Ͽἀ-῿þðæǣœȳċġǭǫáéíóúāēīōūḗḯ'().-]+")
MARKUP_FORM_RE = re.compile(r"\\emph\{([^}]+)\}|`([^`]+)`")
EXPLICIT_TAG_RE = re.compile(r"\[(?P<content>[^\]]+)\]\{\.iv(?P<attrs>[^}]*)\}")
ATTR_RE = re.compile(r"(?P<key>[A-Za-z_][A-Za-z0-9_-]*)=(?P<value>\"[^\"]*\"|[^\s}]+)")
STAGE_FORM_RE = re.compile(
    r"(?P<label>(?:PGmc|Proto-Germanic|PWGmc|Proto-West Germanic|Proto-West-Germanic|"
    r"NWGmc|Proto-Northwest Germanic|Proto-Northwest-Germanic|OE|Old English|"
    r"West Saxon|WS|Anglo Frisian|Anglian)[^:\n<]{0,80}):\s*(?P<form>\*?[A-Za-zÀ-ɏḀ-ỿþðæǣœȳċġǭǫáéíóúāēīōūḗḯ'./()-]+)"
)
FAILURE_EXAMPLE_RE = re.compile(
    r"(?P<label>PGmc|PWGmc|NWGmc|OE|Old English)\s+\\emph\{(?P<input>[^}]+)\}\s+"
    r"yields\s+(?P<yield>\*?[A-Za-zÀ-ɏḀ-ỿþðæǣœȳċġǭǫáéíóúāēīōūḗḯ'./()-]+)\s+"
    r"(?:rather than expected(?: OE)?|instead of(?: expected(?: OE)?)?)\s+"
    r"(?P<expected>\*?[A-Za-zÀ-ɏḀ-ỿþðæǣœȳċġǭǫáéíóúāēīōūḗḯ'./()-]+)"
)
NOISE_LINE_PREFIXES = (
    "#",
    "PROTO:",
    "PROTOFORM:",
    "COUNTERPART:",
    "DERIVATION_CLASS:",
    "### Transducer input and output",
    "|",
    r"\begingroup",
    r"\endgroup",
)
TABLE_AUDIT_HEADING_KEYWORDS = ("comparison", "status")
TABLE_AUDIT_HEADER_KEYWORDS = ("form", "input", "outcome", "comparison", "branch")
TABLE_AUDIT_HEADER_EXCLUDE = ("result", "status", "relevance")
BARE_TABLE_CELL_RE = re.compile(r"^\s*\*?[A-Za-zÀ-ɏḀ-ỿͰ-Ͽἀ-῿þðæǣœȳċġǭǫáéíóúāēīōūḗḯ.-]+\s*(?:/\s*\*?[A-Za-zÀ-ɏḀ-ỿͰ-Ͽἀ-῿þðæǣœȳċġǭǫáéíóúāēīōūḗḯ.-]+\s*)*$")
TRANSLIT_MAP = {
    "þ": "th",
    "ð": "d",
    "æ": "ae",
    "ǣ": "ae",
    "œ": "oe",
    "ċ": "c",
    "ġ": "g",
    "ȳ": "y",
    "ǭ": "o",
    "ǫ": "o",
    "ā": "a",
    "ē": "e",
    "ī": "i",
    "ō": "o",
    "ū": "u",
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u",
    "ḗ": "e",
    "ḯ": "i",
    "ṛ": "r",
    "ṝ": "r",
    "ḷ": "l",
    "ḹ": "l",
    "ṃ": "m",
    "ṁ": "m",
    "ḥ": "h",
    "ś": "s",
    "ṣ": "s",
    "ñ": "n",
    "ṇ": "n",
    "ṭ": "t",
    "ḍ": "d",
    "α": "a",
    "β": "b",
    "γ": "g",
    "δ": "d",
    "ε": "e",
    "ζ": "z",
    "η": "e",
    "θ": "th",
    "ι": "i",
    "κ": "k",
    "λ": "l",
    "μ": "m",
    "ν": "n",
    "ξ": "x",
    "ο": "o",
    "π": "p",
    "ρ": "r",
    "σ": "s",
    "ς": "s",
    "τ": "t",
    "υ": "u",
    "φ": "ph",
    "χ": "ch",
    "ψ": "ps",
    "ω": "o",
}


def write_index_registry_header(production_rows: list[ProductionOccurrence]) -> None:
    languages_in_use = {row.language for row in production_rows}
    lines = []
    for row in LANGUAGE_REGISTRY:
        if row["code"] not in languages_in_use:
            continue
        lines.append(
            rf"\makeindex[name={row['code']},title={{{row['title']}}},columns={row['columns']}]"
        )
    INDEX_HEADER_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


README_LANG_BEGIN = "<!-- BEGIN AUTO-LANGUAGE-LIST -->"
README_LANG_END = "<!-- END AUTO-LANGUAGE-LIST -->"


def rewrite_readme_language_block() -> None:
    if not README_PATH.exists():
        return
    text = README_PATH.read_text(encoding="utf-8")
    if README_LANG_BEGIN not in text or README_LANG_END not in text:
        return
    body_lines = []
    for row in LANGUAGE_REGISTRY:
        if row.get("active") != "1":
            continue
        body_lines.append(f"- `{row['code']}` — {row['title']}")
    replacement = README_LANG_BEGIN + "\n" + "\n".join(body_lines) + "\n" + README_LANG_END
    text = re.sub(
        re.escape(README_LANG_BEGIN) + r".*?" + re.escape(README_LANG_END),
        replacement,
        text,
        flags=re.S,
    )
    README_PATH.write_text(text, encoding="utf-8")


@dataclass
class ProductionOccurrence:
    language: str
    form: str
    display: str
    sort_key: str
    form_role: str
    source_scope: str
    source_ref: str
    origins: set[str] = field(default_factory=set)
    status: str = "auto"

    @property
    def key(self) -> tuple[str, str, str, str, str]:
        return (self.language, self.form, self.display, self.source_scope, self.source_ref)


@dataclass(frozen=True)
class CandidateOccurrence:
    form: str
    source_ref: str
    source_path: str
    line_no: int
    heading: str
    line_text: str
    candidate_origin: str = "broad_prose_candidate"


def transliterate_sort_key(text: str) -> str:
    text = text.lstrip("*").casefold()
    normalized = unicodedata.normalize("NFKD", text)
    stripped = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    replaced = "".join(TRANSLIT_MAP.get(ch, ch) for ch in stripped)
    return re.sub(r"[^a-z0-9]+", "", replaced)


def run_sort_key_assertions() -> None:
    assert transliterate_sort_key("þanc") == "thanc", transliterate_sort_key("þanc")
    assert transliterate_sort_key("bæþ") == "baeth", transliterate_sort_key("bæþ")
    assert transliterate_sort_key("bǣr") == "baer", transliterate_sort_key("bǣr")
    assert transliterate_sort_key("ġiefan") == "giefan", transliterate_sort_key("ġiefan")
    assert transliterate_sort_key("sċuldrum") == "sculdrum", transliterate_sort_key("sċuldrum")


def strip_markup(text: str) -> str:
    value = text.strip()
    for prefix, suffix in ((r"\emph{", "}"), ("`", "`"), ("*", "*"), ("_", "_")):
        if value.startswith(prefix) and value.endswith(suffix):
            value = value[len(prefix) : len(value) - len(suffix)]
            break
    return value.strip("`.,;:!?()[]{}“”\"' ")


def oe_target_display(counterpart: str, derivation_class: str) -> str:
    return f"*{counterpart}" if derivation_class == "reconstructed_oe" else counterpart


def heading_ref(lexical_item: str, counterpart: str, derivation_class: str = "") -> str:
    return f"{lexical_item} — OE {oe_target_display(counterpart, derivation_class)}"


def looks_formlike(text: str) -> bool:
    if not text:
        return False
    if "/" in text and not text.startswith("*"):
        return False
    if ".md" in text or ".pdf" in text or ".tsv" in text or "\\" in text or "<" in text or ">" in text:
        return False
    if sum(1 for ch in text.lstrip("*") if unicodedata.category(ch).startswith("L")) < 2:
        return False
    return True


def normalize_form(text: str) -> str:
    cleaned = strip_markup(text)
    return cleaned if looks_formlike(cleaned) else ""


def relative_source_path(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def stage_to_language(label: str, form: str) -> str:
    compact = label.strip()
    if compact.startswith(("PGmc", "Proto-Germanic")):
        return "pgmc"
    if compact.startswith(("PWGmc", "Proto-West Germanic", "Proto-West-Germanic")):
        return "pwgmc"
    if compact.startswith(("NWGmc", "Proto-Northwest Germanic", "Proto-Northwest-Germanic")):
        return "nwgmc"
    if compact.startswith(("Old Norse", "ON")):
        return "on"
    if compact.startswith(("Old Saxon", "OS")):
        return "os"
    if compact.startswith(("Old High German", "OHG")):
        return "ohg"
    if compact.startswith(("Old Frisian", "OFri")):
        return "ofris"
    if compact.startswith(("Gothic", "Goth")):
        return "goth"
    if compact.startswith(("Old Dutch",)):
        return "odutch"
    if compact.startswith(("Middle Dutch",)):
        return "mdutch"
    if compact.startswith(("Dutch",)):
        return "dutch"
    if compact.startswith(("German",)):
        return "german"
    if compact.startswith(("Latin", "Lat.")):
        return "lat"
    if compact.startswith(("Greek", "Gk.")):
        return "greek"
    if compact.startswith(("Sanskrit", "Skt.")):
        return "skt"
    if compact.startswith(("Middle English",)):
        return "me"
    if compact.startswith(("Modern English",)):
        return "modeng"
    if compact.startswith(("Old Irish",)):
        return "oirish"
    return "preoe" if form.startswith("*") else "oe"


def add_production(
    store: dict[tuple[str, str, str, str, str], ProductionOccurrence],
    *,
    language: str,
    form: str,
    form_role: str,
    source_scope: str,
    source_ref: str,
    origin: str,
    display: str | None = None,
    sort_key: str | None = None,
    status: str = "auto",
) -> None:
    cleaned = normalize_form(form)
    if not cleaned or not language:
        return
    if language not in KNOWN_LANGUAGE_CODES:
        raise ValueError(f"Unknown index verborum language code: {language}")
    if form_role not in ALLOWED_FORM_ROLES:
        raise ValueError(f"Unknown index verborum form role: {form_role}")
    visible = display or cleaned
    key = (language, cleaned, visible, source_scope, source_ref)
    if key not in store:
        store[key] = ProductionOccurrence(
            language=language,
            form=cleaned,
            display=visible,
            sort_key=sort_key or transliterate_sort_key(visible),
            form_role=form_role,
            source_scope=source_scope,
            source_ref=source_ref,
            status=status,
        )
    store[key].origins.add(origin)
    if status == "override":
        store[key].status = "override"


def parse_manifest_rows() -> list[dict[str, str]]:
    with MANIFEST_PATH.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def parse_compact_entries() -> list[dict[str, object]]:
    text = COMPACT_PATH.read_text(encoding="utf-8")
    chunks: list[list[str]] = []
    current: list[str] = []
    for line in text.splitlines():
        if line.startswith("# "):
            if current:
                chunks.append(current)
            current = [line]
        elif current:
            current.append(line)
    if current:
        chunks.append(current)

    entries: list[dict[str, object]] = []
    for chunk in chunks:
        block = "\n".join(chunk)
        title = chunk[0][2:].strip()
        proto_match = re.search(r"^PROTO:\s*(.+)$", block, re.M)
        expected_match = re.search(r"^EXPECTED:\s*(.+)$", block, re.M)
        outputs_match = re.search(r"^OUTPUTS:\s*(.+)$", block, re.M)
        proto_input_match = re.search(r"^Proto Input:\s*(.+)$", block, re.M)
        table_lines: list[str] = []
        in_table = False
        for line in chunk:
            if line.startswith("| Earlier Germanic developments | Old English developments |"):
                in_table = True
            if in_table and line.startswith("|"):
                table_lines.append(line)
                continue
            if in_table and not line.startswith("|"):
                break
        stages: list[tuple[str, str]] = []
        table_text = "\n".join(table_lines).replace("<br>", "\n")
        for stage_match in STAGE_FORM_RE.finditer(table_text):
            label = stage_match.group("label").strip()
            if ";" in label:
                continue
            form = normalize_form(stage_match.group("form"))
            if not form:
                continue
            stages.append((label, form))
        entries.append(
            {
                "title": title,
                "proto": proto_match.group(1).strip() if proto_match else "",
                "expected": expected_match.group(1).strip() if expected_match else "",
                "outputs": [item.strip() for item in outputs_match.group(1).split(",")] if outputs_match else [],
                "proto_input": proto_input_match.group(1).strip() if proto_input_match else "",
                "stages": stages,
            }
        )
    return entries


def parse_attr_string(raw: str) -> dict[str, str]:
    attrs: dict[str, str] = {}
    for match in ATTR_RE.finditer(raw):
        value = match.group("value").strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        attrs[match.group("key")] = value
    return attrs


def iter_explicit_tags(path: Path) -> list[dict[str, str]]:
    tags: list[dict[str, str]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        for match in EXPLICIT_TAG_RE.finditer(line):
            attrs = parse_attr_string(match.group("attrs"))
            tags.append(
                {
                    "content": match.group("content"),
                    "line_no": str(line_no),
                    "lang": attrs.get("lang", "").strip(),
                    "sort": attrs.get("sort", "").strip(),
                    "display": attrs.get("display", "").strip(),
                    "role": attrs.get("role", "").strip(),
                }
            )
    return tags


def source_files_for_tags() -> list[Path]:
    return [INTRO_PATH, CHRONOLOGY_PATH, *sorted(MODEL_ENTRIES_DIR.glob("*.model.md"))]


def source_files_for_audit() -> list[Path]:
    return [INTRO_PATH, CHRONOLOGY_PATH, *sorted(MODEL_ENTRIES_DIR.glob("*.model.md"))]


def explicit_tag_occurrences(paths: list[Path] | None = None) -> list[dict[str, str]]:
    occurrences: list[dict[str, str]] = []
    for path in paths or source_files_for_tags():
        rel = relative_source_path(path)
        for tag in iter_explicit_tags(path):
            occurrences.append(
                {
                    "language": tag["lang"],
                    "form": strip_markup(tag["content"]),
                    "display": tag["display"] or strip_markup(tag["content"]),
                    "sort_key": tag["sort"] or transliterate_sort_key(strip_markup(tag["content"])),
                    "form_role": tag["role"] or "evidence_form",
                    "source_scope": "explicit_tag",
                    "source_ref": f"{rel}:{tag['line_no']}",
                    "origin": rel,
                }
            )
    return occurrences


def reader_facing_failure_occurrences() -> list[dict[str, str]]:
    occurrences: list[dict[str, str]] = []
    rel = CHRONOLOGY_PATH.relative_to(REPO_ROOT).as_posix()
    for line_no, line in enumerate(CHRONOLOGY_PATH.read_text(encoding="utf-8").splitlines(), start=1):
        for match in FAILURE_EXAMPLE_RE.finditer(line):
            input_form = strip_markup(match.group("input"))
            yielded = strip_markup(match.group("yield"))
            expected = strip_markup(match.group("expected"))
            occurrences.append(
                {
                    "language": stage_to_language(match.group("label"), input_form),
                    "form": input_form,
                    "display": input_form,
                    "sort_key": transliterate_sort_key(input_form),
                    "form_role": "selected_input",
                    "source_scope": "reader_failure_input",
                    "source_ref": f"{rel}:{line_no}",
                    "origin": rel,
                }
            )
            for form, scope in ((yielded, "reader_failure_output"), (expected, "reader_failure_expected")):
                occurrences.append(
                    {
                        "language": "preoe" if form.startswith("*") else "oe",
                        "form": form,
                        "display": form,
                        "sort_key": transliterate_sort_key(form),
                        "form_role": "regular_output" if scope == "reader_failure_output" else "comparison_form",
                        "source_scope": scope,
                        "source_ref": f"{rel}:{line_no}",
                        "origin": rel,
                    }
                )
    return occurrences


def split_markdown_table_row(line: str) -> list[str]:
    raw = line.strip()
    if raw.startswith("|"):
        raw = raw[1:]
    if raw.endswith("|"):
        raw = raw[:-1]
    return [cell.strip() for cell in raw.split("|")]


def is_markdown_table_delimiter(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells)


def heading_supports_table_audit(heading: str) -> bool:
    lowered = heading.casefold()
    return any(keyword in lowered for keyword in TABLE_AUDIT_HEADING_KEYWORDS)


def header_supports_table_audit(header: str) -> bool:
    lowered = re.sub(r"\s+", " ", header.casefold())
    if any(keyword in lowered for keyword in TABLE_AUDIT_HEADER_EXCLUDE):
        return False
    if lowered in {"item", "value"}:
        return False
    return any(keyword in lowered for keyword in TABLE_AUDIT_HEADER_KEYWORDS)


def extract_forms_from_markup(text: str) -> list[str]:
    forms: list[str] = []
    seen: set[str] = set()
    for match in EXPLICIT_TAG_RE.finditer(text):
        form = normalize_form(match.group("content"))
        if form and form not in seen:
            forms.append(form)
            seen.add(form)
    scrubbed = EXPLICIT_TAG_RE.sub(" ", text)
    for match in MARKUP_FORM_RE.finditer(scrubbed):
        raw = next(group for group in match.groups() if group)
        form = normalize_form(raw.replace("<br>", " "))
        if form and form not in seen:
            forms.append(form)
            seen.add(form)
    bare = scrubbed.strip()
    if BARE_TABLE_CELL_RE.fullmatch(bare):
        for chunk in re.split(r"\s*/\s*", bare):
            form = normalize_form(chunk.strip())
            if form and form not in seen:
                forms.append(form)
                seen.add(form)
    return forms


def table_candidates_from_path(path: Path, *, allow_non_model_entry: bool = False) -> list[CandidateOccurrence]:
    if not allow_non_model_entry and path.parent != MODEL_ENTRIES_DIR:
        return []
    rel = relative_source_path(path)
    lines = path.read_text(encoding="utf-8").splitlines()
    candidates: list[CandidateOccurrence] = []
    current_heading = ""
    idx = 0
    while idx < len(lines):
        stripped = lines[idx].strip()
        if stripped.startswith("#"):
            current_heading = stripped
        if (
            not heading_supports_table_audit(current_heading)
            or not stripped.startswith("|")
            or idx + 1 >= len(lines)
        ):
            idx += 1
            continue
        header_cells = split_markdown_table_row(lines[idx])
        delimiter_cells = split_markdown_table_row(lines[idx + 1].strip())
        if len(header_cells) != len(delimiter_cells) or not is_markdown_table_delimiter(delimiter_cells):
            idx += 1
            continue
        relevant_columns = {
            col_idx for col_idx, header in enumerate(header_cells) if header_supports_table_audit(header)
        }
        idx += 2
        while idx < len(lines) and lines[idx].strip().startswith("|"):
            row_line = lines[idx]
            row_cells = split_markdown_table_row(row_line)
            for col_idx in relevant_columns:
                if col_idx >= len(row_cells):
                    continue
                for form in extract_forms_from_markup(row_cells[col_idx]):
                    candidates.append(
                        CandidateOccurrence(
                            form=form,
                            source_ref=f"{rel}:{idx + 1}",
                            source_path=rel,
                            line_no=idx + 1,
                            heading=current_heading,
                            line_text=row_line.strip(),
                            candidate_origin="table_candidate",
                        )
                    )
            idx += 1
    return candidates


def excluded_intermediate_trace_forms() -> list[dict[str, str]]:
    manifest_rows = parse_manifest_rows()
    manifest_by_title = {
        (row["lexical_item"], row["counterpart"], row["protoform"]): row
        for row in manifest_rows
    }
    entries: list[dict[str, str]] = []
    for entry in parse_compact_entries():
        manifest_row = manifest_by_title.get((entry["title"], entry["expected"], entry["proto"]))
        if manifest_row is not None:
            ref = heading_ref(manifest_row["lexical_item"], manifest_row["counterpart"], manifest_row["derivation_class"])
        else:
            ref = heading_ref(str(entry["title"]), str(entry["expected"]))
        for label, form in entry["stages"]:
            entries.append(
                {
                    "form": form,
                    "source_ref": ref,
                    "source_path": COMPACT_PATH.relative_to(REPO_ROOT).as_posix(),
                    "heading": label,
                    "category": "intermediate_trace_form",
                    "context": label,
                    "sort_key": transliterate_sort_key(form),
                }
            )
    entries.sort(key=lambda row: (row.get("sort_key", ""), row["form"], row["source_ref"]))
    return entries


def broad_candidates_from_path(path: Path) -> list[CandidateOccurrence]:
    rel = relative_source_path(path)
    candidates: list[CandidateOccurrence] = []
    in_fence = False
    current_heading = ""
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("#"):
            current_heading = stripped
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or stripped.startswith(NOISE_LINE_PREFIXES) or stripped.startswith("\\"):
            continue
        if stripped.startswith("|") or stripped.startswith("define "):
            continue
        scrubbed = EXPLICIT_TAG_RE.sub("", line)
        for match in MARKUP_FORM_RE.finditer(scrubbed):
            raw = next(group for group in match.groups() if group)
            form = strip_markup(raw)
            if form:
                candidates.append(
                    CandidateOccurrence(
                        form=form,
                        source_ref=f"{rel}:{line_no}",
                        source_path=rel,
                        line_no=line_no,
                        heading=current_heading,
                        line_text=stripped,
                        candidate_origin="broad_prose_candidate",
                    )
                )
        for match in re.finditer(r"\b(?:PGmc|PWGmc|NWGmc|OE|ON|OHG|OFri|Goth)\s+(\*?[A-Za-zÀ-ɏḀ-ỿþðæǣœȳċġǭǫáéíóúāēīōūḗḯ'./()\-]+)", scrubbed):
            form = strip_markup(match.group(1))
            if form:
                candidates.append(
                    CandidateOccurrence(
                        form=form,
                        source_ref=f"{rel}:{line_no}",
                        source_path=rel,
                        line_no=line_no,
                        heading=current_heading,
                        line_text=stripped,
                        candidate_origin="broad_prose_candidate",
                    )
                )
    return candidates


def candidate_category(form: str) -> str:
    if not form or ".md" in form or ".pdf" in form or "/" in form or "<" in form or ">" in form or "\\" in form:
        return "possible_garbage"
    if " " in form or "," in form or "_" in form:
        return "possible_garbage"
    if form.startswith("*") and (len(form.lstrip("*")) <= 4 or form.endswith("-")):
        return "ignored_fragment"
    if form.startswith("-") or form.endswith("-") or "(" in form or ")" in form:
        return "ignored_fragment"
    if re.fullmatch(r"[a-z]{1,4}", form):
        return "ignored_fragment"
    if re.fullmatch(r"\*?[A-Za-zÀ-ɏḀ-ỿþðæǣœȳċġǭǫáéíóúāēīōūḗḯ]{1,2}", form):
        return "ignored_fragment"
    if not looks_formlike(form):
        return "possible_garbage"
    return "needs_review"


def load_overrides() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    if not OVERRIDES_PATH.exists():
        return [], []
    with OVERRIDES_PATH.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        rows = [{key: (value or "").strip() for key, value in row.items()} for row in reader]
    adds = [row for row in rows if row.get("action") == "add"]
    ignores = [row for row in rows if row.get("action") == "ignore"]
    return adds, ignores


def override_matches(override: dict[str, str], *, form: str, source_scope: str = "", source_ref: str = "", language: str = "") -> bool:
    for key, value in (("form", form), ("source_scope", source_scope), ("source_ref", source_ref), ("language", language)):
        expected = override.get(key, "")
        if expected and expected != value:
            return False
    return True


def build_production_rows(add_overrides: list[dict[str, str]] | None = None, ignore_overrides: list[dict[str, str]] | None = None) -> list[ProductionOccurrence]:
    manifest_rows = parse_manifest_rows()
    manifest_by_title = {
        (row["lexical_item"], row["counterpart"], row["protoform"]): row
        for row in manifest_rows
    }
    store: dict[tuple[str, str, str, str, str], ProductionOccurrence] = {}
    for row in manifest_rows:
        ref = heading_ref(row["lexical_item"], row["counterpart"], row["derivation_class"])
        oe_display = oe_target_display(row["counterpart"], row["derivation_class"])
        add_production(store, language="oe", form=row["counterpart"], display=oe_display, form_role="target_form", source_scope="lexical_heading", source_ref=ref, origin="manifest")
        add_production(store, language="pgmc", form=row["protoform"], form_role="source_protoform", source_scope="lexical_protoform", source_ref=ref, origin="manifest")
        if row["proto"] and row["proto"] != row["protoform"]:
            add_production(store, language="pgmc", form=row["proto"], form_role="source_protoform", source_scope="lexical_proto", source_ref=ref, origin="manifest")

    for entry in parse_compact_entries():
        manifest_row = manifest_by_title.get((entry["title"], entry["expected"], entry["proto"]))
        if manifest_row is not None:
            ref = heading_ref(manifest_row["lexical_item"], manifest_row["counterpart"], manifest_row["derivation_class"])
            oe_display = oe_target_display(manifest_row["counterpart"], manifest_row["derivation_class"])
        else:
            ref = heading_ref(str(entry["title"]), str(entry["expected"]))
            oe_display = str(entry["expected"])
        if entry["proto_input"]:
            add_production(store, language="pgmc", form=str(entry["proto_input"]), form_role="selected_input", source_scope="trace_proto_input", source_ref=ref, origin="compact")

    for row in explicit_tag_occurrences():
        if row["language"]:
            add_production(
                store,
                language=row["language"],
                form=row["form"],
                display=row["display"],
                sort_key=row["sort_key"],
                form_role=row["form_role"],
                source_scope=row["source_scope"],
                source_ref=row["source_ref"],
                origin=row["origin"],
            )

    for row in reader_facing_failure_occurrences():
        if row["language"]:
            add_production(
                store,
                language=row["language"],
                form=row["form"],
                display=row["display"],
                sort_key=row["sort_key"],
                form_role=row["form_role"],
                source_scope=row["source_scope"],
                source_ref=row["source_ref"],
                origin=row["origin"],
            )

    if add_overrides is None or ignore_overrides is None:
        add_overrides, ignore_overrides = load_overrides()
    for row in add_overrides:
        add_production(
            store,
            language=row["language"],
            form=row["form"],
            display=row["display"] or row["form"],
            sort_key=row["sort_key"] or transliterate_sort_key(row["display"] or row["form"]),
            form_role="comparison_form",
            source_scope=row["source_scope"] or "override",
            source_ref=row["source_ref"] or "override",
            origin="override",
            status="override",
        )

    filtered: list[ProductionOccurrence] = []
    for entry in store.values():
        ignored = any(
            override_matches(
                override,
                form=entry.form,
                source_scope=entry.source_scope,
                source_ref=entry.source_ref,
                language=entry.language,
            )
            for override in ignore_overrides
        )
        if not ignored:
            filtered.append(entry)
    return sorted(
        filtered,
        key=lambda entry: (
            LANGUAGE_ORDER.index(entry.language) if entry.language in LANGUAGE_ORDER else len(LANGUAGE_ORDER),
            entry.sort_key,
            entry.display,
            entry.source_ref,
            entry.source_scope,
        ),
    )


FALSE_POSITIVE_FORMS = {
    "attestation",
    "attested_variant",
    "breaking",
    "citation",
    "comparator",
    "derivation",
    "development",
    "evidence",
    "family",
}


def guess_unresolved_category(candidate: CandidateOccurrence) -> str:
    text = candidate.line_text
    form = candidate.form
    label_map = [
        (("Old Norse", "ON "), "likely_on"),
        (("Old Saxon", "OS "), "likely_os"),
        (("Old High German", "OHG "), "likely_ohg"),
        (("Old Frisian", "OFris", "OFri "), "likely_ofris"),
        (("Gothic", "Goth."), "likely_goth"),
        (("Old Dutch",), "likely_odutch"),
        (("Middle Dutch",), "likely_mdutch"),
        (("Dutch",), "likely_dutch"),
        (("German",), "likely_german"),
        (("Latin", "Lat."), "likely_lat"),
        (("Greek", "Gk."), "likely_greek"),
        (("Sanskrit", "Skt."), "likely_skt"),
        (("Middle English",), "likely_me"),
        (("Modern English",), "likely_modeng"),
        (("Old Irish",), "likely_oirish"),
        (("PGmc", "Proto-Germanic"), "likely_pgmc"),
        (("PWGmc", "Proto-West Germanic", "Proto-West-Germanic"), "likely_pwgmc"),
        (("NWGmc", "Proto-Northwest Germanic", "Proto-Northwest-Germanic"), "likely_nwgmc"),
        (("Old English", "OE "), "likely_oe"),
    ]
    for needles, category in label_map:
        if any(needle in text for needle in needles):
            return category
    if form in FALSE_POSITIVE_FORMS:
        return "likely_false_positive"
    if candidate.heading.startswith("### Old English evidence"):
        return "likely_oe"
    if candidate.source_path.endswith("reader_facing_local_section_19.md"):
        return "likely_preoe" if form.startswith("*") else "likely_oe"
    if form.startswith("*"):
        return "likely_pgmc"
    if any(ch in form for ch in "þðæǣœȳċġǭǫáéíóúāēīōūḗḯ"):
        return "likely_oe"
    return "likely_false_positive"


def build_audit_rows(
    production_rows: list[ProductionOccurrence],
    candidates: list[CandidateOccurrence] | None = None,
    ignore_overrides: list[dict[str, str]] | None = None,
) -> dict[str, list[dict[str, str]]]:
    production_occurrences = {(row.form, row.source_ref) for row in production_rows}
    if ignore_overrides is None:
        _, ignore_overrides = load_overrides()
    buckets: dict[str, list[dict[str, str]]] = defaultdict(list)
    seen: set[tuple[str, str]] = set()
    source_candidates = candidates
    if source_candidates is None:
        source_candidates = []
        for path in source_files_for_audit():
            source_candidates.extend(broad_candidates_from_path(path))
            source_candidates.extend(table_candidates_from_path(path))
    for candidate in source_candidates:
        if (candidate.form, candidate.source_ref) in seen:
            continue
        seen.add((candidate.form, candidate.source_ref))
        if (candidate.form, candidate.source_ref) in production_occurrences:
            continue
        category = candidate_category(candidate.form)
        if any(override_matches(override, form=candidate.form, source_ref=candidate.source_ref) for override in ignore_overrides):
            category = "ignored_by_override"
        entry = {
            "form": candidate.form,
            "source_ref": candidate.source_ref,
            "source_path": candidate.source_path,
            "heading": candidate.heading,
            "context": re.sub(r"\s+", " ", candidate.line_text).strip()[:160],
            "sort_key": transliterate_sort_key(candidate.form),
            "candidate_origin": candidate.candidate_origin,
        }
        if category == "needs_review":
            entry["category"] = guess_unresolved_category(candidate)
        buckets[category].append(entry)
    for rows in buckets.values():
        rows.sort(key=lambda row: (row.get("sort_key", ""), row["form"], row["source_ref"]))
    return buckets


def write_forms(rows: list[ProductionOccurrence]) -> None:
    with FORMS_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=PRODUCTION_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "language": row.language,
                    "form": row.form,
                    "display": row.display,
                    "sort_key": row.sort_key,
                    "form_role": row.form_role,
                    "source_scope": row.source_scope,
                    "source_ref": row.source_ref,
                    "origin": "; ".join(sorted(row.origins)),
                    "status": row.status,
                }
            )


def unresolved_baseline_key(entry: dict[str, str]) -> tuple[str, str, str, str, str]:
    return (
        (entry.get("form") or "").strip(),
        (entry.get("source_path") or "").strip(),
        (entry.get("heading") or "").strip(),
        (entry.get("category") or "").strip(),
        (entry.get("context") or "").strip(),
    )


def load_unresolved_baseline(path: Path) -> dict[tuple[str, str, str, str, str], dict[str, str]]:
    if not path.exists():
        return {}
    with path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return {
            unresolved_baseline_key({key: (value or "").strip() for key, value in row.items()}): {key: (value or "").strip() for key, value in row.items()}
            for row in reader
        }


def write_unresolved_baseline(path: Path, entries: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            delimiter="\t",
            fieldnames=["form", "source_path", "source_ref", "heading", "category", "sort_key", "context", "note"],
        )
        writer.writeheader()
        for entry in sorted(entries, key=lambda row: (row.get("sort_key", ""), row["form"], row["source_ref"])):
            writer.writerow(
                {
                    "form": entry["form"],
                    "source_path": entry.get("source_path", ""),
                    "source_ref": entry["source_ref"],
                    "heading": entry.get("heading", ""),
                    "category": entry.get("category", ""),
                    "sort_key": entry.get("sort_key", ""),
                    "context": entry.get("context", ""),
                    "note": "",
                }
            )


def compare_against_baseline(
    entries: list[dict[str, str]],
    baseline: dict[tuple[str, str, str, str, str], dict[str, str]],
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    current = {unresolved_baseline_key(entry): entry for entry in entries}
    new_entries = [entry for key, entry in current.items() if key not in baseline]
    resolved_entries = [baseline[key] for key in baseline if key not in current]
    new_entries.sort(key=lambda row: (row.get("sort_key", ""), row["form"], row["source_ref"]))
    resolved_entries.sort(key=lambda row: (row.get("sort_key", ""), row.get("form", ""), row.get("source_ref", "")))
    return new_entries, resolved_entries


def write_audit(
    rows: list[ProductionOccurrence],
    buckets: dict[str, list[dict[str, str]]],
    baseline: dict[tuple[str, str, str, str, str], dict[str, str]],
) -> int:
    counts_by_language = Counter(row.language for row in rows)
    unique_by_language = {
        language: len({row.display for row in rows if row.language == language})
        for language in counts_by_language
    }
    needs_review_entries = buckets.get("needs_review", [])
    excluded_trace_entries = excluded_intermediate_trace_forms()
    new_entries, resolved_entries = compare_against_baseline(needs_review_entries, baseline)
    lines = [
        "# Index verborum audit",
        "",
        f"- Production indexed occurrences: {len(rows)}",
        f"- Production unique forms: {len({(row.language, row.display) for row in rows})}",
        f"- Audit-only candidates needing review: {len(needs_review_entries)}",
        f"- Ignored fragments or sequences: {len(buckets.get('ignored_fragment', [])) + len(buckets.get('ignored_by_override', []))}",
        f"- Possible extraction garbage: {len(buckets.get('possible_garbage', []))}",
        f"- Excluded intermediate trace forms: {len(excluded_trace_entries)}",
        f"- New unresolved candidates relative to baseline: {len(new_entries)}",
        f"- Baseline candidates now resolved or ignored: {len(resolved_entries)}",
        "",
        "## Production indexed forms by language",
        "",
        "| Language | Occurrences | Unique forms |",
        "| --- | ---: | ---: |",
    ]
    for language in LANGUAGE_ORDER:
        if counts_by_language.get(language):
            lines.append(f"| {LANGUAGE_TITLES[language]} | {counts_by_language[language]} | {unique_by_language[language]} |")
    lines.extend(["", "## Examples of production indexed forms", ""])
    for language in LANGUAGE_ORDER:
        sample = [row for row in rows if row.language == language][:5]
        if not sample:
            continue
        lines.append(f"### {LANGUAGE_TITLES[language]}")
        lines.append("")
        for row in sample:
            lines.append(f"- `{row.display}` ({row.source_scope}; {row.source_ref})")
        lines.append("")

    role_counts = Counter(row.form_role for row in rows)
    lines.extend(["## Production indexed forms by role", "", "| Role | Occurrences |", "| --- | ---: |"])
    for role in (
        "target_form",
        "source_protoform",
        "selected_input",
        "comparison_form",
        "regular_output",
        "evidence_form",
    ):
        if role_counts.get(role):
            lines.append(f"| {role} | {role_counts[role]} |")
    lines.append("")

    def render_bucket(title: str, entries: list[dict[str, str]], columns: tuple[str, ...] = ("form", "source_ref")) -> None:
        lines.append(f"## {title}")
        lines.append("")
        if not entries:
            lines.append("_None._")
            lines.append("")
            return
        label_map = {
            "form": "Form",
            "source_ref": "Source",
            "category": "Category",
            "count": "Count",
            "source_path": "Source file",
            "heading": "Nearest heading",
            "context": "Context",
            "candidate_origin": "Candidate origin",
        }
        lines.append("| " + " | ".join(label_map[col] for col in columns) + " |")
        lines.append("| " + " | ".join("---" for _ in columns) + " |")
        for entry in entries:
            parts = []
            for col in columns:
                value = entry.get(col, "")
                parts.append(f"`{value}`" if col == "form" else str(value))
            lines.append("| " + " | ".join(parts) + " |")
        lines.append("")

    guess_groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for entry in needs_review_entries:
        guess_groups[entry["category"]].append(entry)
    for group in guess_groups.values():
        group.sort(key=lambda row: (row.get("sort_key", ""), row["form"], row["source_ref"]))
    likely_columns = ("form", "source_ref", "candidate_origin")
    render_bucket("Likely Old English forms", guess_groups.get("likely_oe", []), columns=likely_columns)
    render_bucket("Likely Proto-Germanic forms", guess_groups.get("likely_pgmc", []), columns=likely_columns)
    render_bucket("Likely Proto-West Germanic forms", guess_groups.get("likely_pwgmc", []), columns=likely_columns)
    render_bucket("Likely Proto-Northwest Germanic forms", guess_groups.get("likely_nwgmc", []), columns=likely_columns)
    render_bucket("Likely pre-Old-English or model-internal forms", guess_groups.get("likely_preoe", []), columns=likely_columns)
    render_bucket("Likely Old Norse forms", guess_groups.get("likely_on", []), columns=likely_columns)
    render_bucket("Likely Old Saxon forms", guess_groups.get("likely_os", []), columns=likely_columns)
    render_bucket("Likely Old High German forms", guess_groups.get("likely_ohg", []), columns=likely_columns)
    render_bucket("Likely Old Frisian forms", guess_groups.get("likely_ofris", []), columns=likely_columns)
    render_bucket("Likely Gothic forms", guess_groups.get("likely_goth", []), columns=likely_columns)
    render_bucket("Likely Old Dutch forms", guess_groups.get("likely_odutch", []), columns=likely_columns)
    render_bucket("Likely Middle Dutch forms", guess_groups.get("likely_mdutch", []), columns=likely_columns)
    render_bucket("Likely Dutch forms", guess_groups.get("likely_dutch", []), columns=likely_columns)
    render_bucket("Likely German forms", guess_groups.get("likely_german", []), columns=likely_columns)
    render_bucket("Likely Latin forms", guess_groups.get("likely_lat", []), columns=likely_columns)
    render_bucket("Likely Greek forms", guess_groups.get("likely_greek", []), columns=likely_columns)
    render_bucket("Likely Sanskrit forms", guess_groups.get("likely_skt", []), columns=likely_columns)
    render_bucket("Likely Middle English forms", guess_groups.get("likely_me", []), columns=likely_columns)
    render_bucket("Likely Modern English linguistic forms", guess_groups.get("likely_modeng", []), columns=likely_columns)
    render_bucket("Likely Old Irish forms", guess_groups.get("likely_oirish", []), columns=likely_columns)
    render_bucket("Likely ordinary-language false positives", guess_groups.get("likely_false_positive", []), columns=likely_columns)
    render_bucket(
        "Table-scanned unresolved candidates",
        [entry for entry in needs_review_entries if entry.get("candidate_origin") == "table_candidate"],
        columns=("form", "source_ref", "heading", "context"),
    )
    render_bucket("Ignored fragments or sequences", buckets.get("ignored_fragment", []))
    render_bucket("Ignored by override", buckets.get("ignored_by_override", []))
    render_bucket("Possible extraction garbage", buckets.get("possible_garbage", []))
    render_bucket("Excluded intermediate trace forms", excluded_trace_entries[:50], columns=("form", "source_ref", "heading"))

    top_forms = Counter(entry["form"] for entry in needs_review_entries)
    render_bucket(
        "Top repeated unresolved forms",
        [{"form": form, "count": count} for form, count in top_forms.most_common(20)],
        columns=("form", "count"),
    )
    by_source = Counter(entry["source_path"] for entry in needs_review_entries)
    render_bucket(
        "Unresolved forms by source file",
        [{"source_path": source, "count": count} for source, count in by_source.most_common(20)],
        columns=("source_path", "count"),
    )
    table_by_source = Counter(
        entry["source_path"]
        for entry in needs_review_entries
        if entry.get("candidate_origin") == "table_candidate"
    )
    render_bucket(
        "Top unresolved table files",
        [{"source_path": source, "count": count} for source, count in table_by_source.most_common(20)],
        columns=("source_path", "count"),
    )
    render_bucket("New unresolved candidates relative to baseline", new_entries, columns=("form", "source_ref", "category", "heading"))
    render_bucket("Resolved or ignored baseline candidates", resolved_entries, columns=("form", "source_ref", "category", "heading"))
    AUDIT_PATH.write_text("\n".join(lines), encoding="utf-8")
    unresolved = len(needs_review_entries)
    if unresolved:
        print(f"Warning: unresolved index candidates = {unresolved}; see {AUDIT_PATH}")
    return unresolved


def ensure_override_file() -> None:
    if OVERRIDES_PATH.exists():
        return
    with OVERRIDES_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=OVERRIDE_FIELDS)
        writer.writeheader()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="Alias for --strict-mode=all.")
    parser.add_argument(
        "--strict-mode",
        choices=("off", "baseline", "all"),
        default="off",
        help="Strictness policy for unresolved audit candidates.",
    )
    parser.add_argument(
        "--baseline",
        type=Path,
        default=UNRESOLVED_BASELINE_PATH,
        help="Baseline TSV used by --strict-mode=baseline.",
    )
    parser.add_argument(
        "--write-unresolved-baseline",
        action="store_true",
        help="Rewrite the unresolved-candidate baseline from the current needs_review set.",
    )
    args = parser.parse_args()
    run_sort_key_assertions()
    BOOK_DIR.mkdir(parents=True, exist_ok=True)
    ensure_override_file()
    rewrite_readme_language_block()
    production_rows = build_production_rows()
    write_index_registry_header(production_rows)
    write_forms(production_rows)
    audit_buckets = build_audit_rows(production_rows)
    baseline = load_unresolved_baseline(args.baseline.expanduser().resolve())
    needs_review_entries = audit_buckets.get("needs_review", [])
    if args.write_unresolved_baseline:
        write_unresolved_baseline(args.baseline.expanduser().resolve(), needs_review_entries)
        baseline = load_unresolved_baseline(args.baseline.expanduser().resolve())
    unresolved = write_audit(production_rows, audit_buckets, baseline)
    strict_mode = "all" if args.strict else args.strict_mode
    if strict_mode == "all":
        raise SystemExit(1 if unresolved else 0)
    if strict_mode == "baseline":
        new_entries, _ = compare_against_baseline(needs_review_entries, baseline)
        raise SystemExit(1 if new_entries else 0)
    raise SystemExit(0)


if __name__ == "__main__":
    main()
