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
MANIFEST_PATH = ASSEMBLY_DIR / "manifest_all_by_class.tsv"
COMPACT_PATH = REPO_ROOT / "Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md"
CHRONOLOGY_PATH = REPO_ROOT / "Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.md"
MODEL_ENTRIES_DIR = REPO_ROOT / "Germanic/docs/lexeme_reports/model_entries"
FORMS_PATH = BOOK_DIR / "index_verborum_forms.tsv"
OVERRIDES_PATH = BOOK_DIR / "index_verborum_overrides.tsv"
AUDIT_PATH = BOOK_DIR / "index_verborum_audit.md"
UNRESOLVED_BASELINE_PATH = BOOK_DIR / "index_verborum_unresolved_baseline.tsv"

PRODUCTION_FIELDS = [
    "language",
    "form",
    "display",
    "sort_key",
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
LANGUAGE_ORDER = ["oe", "pgmc", "pwgmc", "nwgmc", "preoe", "on", "ohg", "ofris", "goth"]
LANGUAGE_TITLES = {
    "oe": "Old English forms",
    "pgmc": "Proto-Germanic forms",
    "pwgmc": "Proto-West Germanic forms",
    "nwgmc": "Proto-Northwest Germanic forms",
    "preoe": "Pre-Old-English and model-internal forms",
    "on": "Old Norse forms",
    "ohg": "Old High German forms",
    "ofris": "Old Frisian forms",
    "goth": "Gothic forms",
}
FORM_RE = re.compile(r"[A-Za-zÀ-ɏḀ-ỿþðæǣœȳċġǭǫáéíóúāēīōūḗḯ'./*()-]+")
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
}


@dataclass
class ProductionOccurrence:
    language: str
    form: str
    display: str
    sort_key: str
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


def transliterate_sort_key(text: str) -> str:
    text = text.lstrip("*").casefold()
    replaced = "".join(TRANSLIT_MAP.get(ch, ch) for ch in text)
    normalized = unicodedata.normalize("NFKD", replaced)
    stripped = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", "", stripped)


def run_sort_key_assertions() -> None:
    assert transliterate_sort_key("þanc") == "thanc"
    assert transliterate_sort_key("bæþ") == "baeth"
    assert transliterate_sort_key("bǣr") == "baer"
    assert transliterate_sort_key("ġiefan") == "giefan"
    assert transliterate_sort_key("sċuldrum") == "sculdrum"


def strip_markup(text: str) -> str:
    value = text.strip()
    for prefix, suffix in ((r"\emph{", "}"), ("`", "`"), ("*", "*"), ("_", "_")):
        if value.startswith(prefix) and value.endswith(suffix):
            value = value[len(prefix) : len(value) - len(suffix)]
            break
    return value.strip("`.,;:!?()[]{}“”\"' ")


def heading_ref(lexical_item: str, counterpart: str) -> str:
    return f"{lexical_item} — OE {counterpart}"


def looks_formlike(text: str) -> bool:
    if not text:
        return False
    if "/" in text and not text.startswith("*"):
        return False
    if ".md" in text or ".pdf" in text or ".tsv" in text or "\\" in text or "<" in text or ">" in text:
        return False
    if len(re.sub(r"[^A-Za-zÀ-ɏḀ-ỿþðæǣœȳċġǭǫáéíóúāēīōūḗḯ]+", "", text.lstrip("*"))) < 2:
        return False
    return True


def normalize_form(text: str) -> str:
    cleaned = strip_markup(text)
    return cleaned if looks_formlike(cleaned) else ""


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
    if compact.startswith(("Old High German", "OHG")):
        return "ohg"
    if compact.startswith(("Old Frisian", "OFri")):
        return "ofris"
    if compact.startswith(("Gothic", "Goth")):
        return "goth"
    return "preoe" if form.startswith("*") else "oe"


def add_production(
    store: dict[tuple[str, str, str, str, str], ProductionOccurrence],
    *,
    language: str,
    form: str,
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
    visible = display or cleaned
    key = (language, cleaned, visible, source_scope, source_ref)
    if key not in store:
        store[key] = ProductionOccurrence(
            language=language,
            form=cleaned,
            display=visible,
            sort_key=sort_key or transliterate_sort_key(visible),
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
                }
            )
    return tags


def source_files_for_tags() -> list[Path]:
    return [INTRO_PATH, CHRONOLOGY_PATH, *sorted(MODEL_ENTRIES_DIR.glob("*.model.md"))]


def source_files_for_audit() -> list[Path]:
    return [INTRO_PATH, CHRONOLOGY_PATH, *sorted(MODEL_ENTRIES_DIR.glob("*.model.md"))]


def explicit_tag_occurrences() -> list[dict[str, str]]:
    occurrences: list[dict[str, str]] = []
    for path in source_files_for_tags():
        rel = path.relative_to(REPO_ROOT).as_posix()
        for tag in iter_explicit_tags(path):
            occurrences.append(
                {
                    "language": tag["lang"],
                    "form": strip_markup(tag["content"]),
                    "display": tag["display"] or strip_markup(tag["content"]),
                    "sort_key": tag["sort"] or transliterate_sort_key(strip_markup(tag["content"])),
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
                        "source_scope": scope,
                        "source_ref": f"{rel}:{line_no}",
                        "origin": rel,
                    }
                )
    return occurrences


def broad_candidates_from_path(path: Path) -> list[CandidateOccurrence]:
    rel = path.relative_to(REPO_ROOT).as_posix()
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
        (row["lexical_item"], row["counterpart"], row["protoform"]): heading_ref(row["lexical_item"], row["counterpart"])
        for row in manifest_rows
    }
    store: dict[tuple[str, str, str, str, str], ProductionOccurrence] = {}
    for row in manifest_rows:
        ref = heading_ref(row["lexical_item"], row["counterpart"])
        add_production(store, language="oe", form=row["counterpart"], source_scope="lexical_heading", source_ref=ref, origin="manifest")
        add_production(store, language="pgmc", form=row["protoform"], source_scope="lexical_protoform", source_ref=ref, origin="manifest")
        if row["proto"] and row["proto"] != row["protoform"]:
            add_production(store, language="pgmc", form=row["proto"], source_scope="lexical_proto", source_ref=ref, origin="manifest")

    for entry in parse_compact_entries():
        ref = manifest_by_title.get((entry["title"], entry["expected"], entry["proto"])) or heading_ref(str(entry["title"]), str(entry["expected"]))
        if entry["proto_input"]:
            add_production(store, language="pgmc", form=str(entry["proto_input"]), source_scope="trace_proto_input", source_ref=ref, origin="compact")
        for form in entry["outputs"]:
            lang = "preoe" if form.startswith("*") else "oe"
            add_production(store, language=lang, form=form, source_scope="trace_output", source_ref=ref, origin="compact")
        for label, form in entry["stages"]:
            add_production(
                store,
                language=stage_to_language(label, form),
                form=form,
                source_scope="trace_stage",
                source_ref=ref,
                origin=f"compact:{label}",
            )

    for row in explicit_tag_occurrences():
        if row["language"]:
            add_production(
                store,
                language=row["language"],
                form=row["form"],
                display=row["display"],
                sort_key=row["sort_key"],
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
        (("Old High German", "OHG "), "likely_ohg"),
        (("Old Frisian", "OFris", "OFri "), "likely_ofris"),
        (("Gothic", "Goth."), "likely_goth"),
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
    production_forms = {row.form for row in production_rows}
    if ignore_overrides is None:
        _, ignore_overrides = load_overrides()
    buckets: dict[str, list[dict[str, str]]] = defaultdict(list)
    seen: set[tuple[str, str]] = set()
    source_candidates = candidates
    if source_candidates is None:
        source_candidates = []
        for path in source_files_for_audit():
            source_candidates.extend(broad_candidates_from_path(path))
    for candidate in source_candidates:
        if (candidate.form, candidate.source_ref) in seen:
            continue
        seen.add((candidate.form, candidate.source_ref))
        if candidate.form in production_forms:
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
    new_entries, resolved_entries = compare_against_baseline(needs_review_entries, baseline)
    lines = [
        "# Index verborum audit",
        "",
        f"- Production indexed occurrences: {len(rows)}",
        f"- Production unique forms: {len({(row.language, row.display) for row in rows})}",
        f"- Audit-only candidates needing review: {len(needs_review_entries)}",
        f"- Ignored fragments or sequences: {len(buckets.get('ignored_fragment', [])) + len(buckets.get('ignored_by_override', []))}",
        f"- Possible extraction garbage: {len(buckets.get('possible_garbage', []))}",
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

    render_bucket("Likely Old English forms", guess_groups.get("likely_oe", []))
    render_bucket("Likely Proto-Germanic forms", guess_groups.get("likely_pgmc", []))
    render_bucket("Likely Proto-West Germanic forms", guess_groups.get("likely_pwgmc", []))
    render_bucket("Likely Proto-Northwest Germanic forms", guess_groups.get("likely_nwgmc", []))
    render_bucket("Likely pre-Old-English or model-internal forms", guess_groups.get("likely_preoe", []))
    render_bucket("Likely Old Norse forms", guess_groups.get("likely_on", []))
    render_bucket("Likely Old High German forms", guess_groups.get("likely_ohg", []))
    render_bucket("Likely Old Frisian forms", guess_groups.get("likely_ofris", []))
    render_bucket("Likely Gothic forms", guess_groups.get("likely_goth", []))
    render_bucket("Likely ordinary-language false positives", guess_groups.get("likely_false_positive", []))
    render_bucket("Ignored fragments or sequences", buckets.get("ignored_fragment", []))
    render_bucket("Ignored by override", buckets.get("ignored_by_override", []))
    render_bucket("Possible extraction garbage", buckets.get("possible_garbage", []))

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
    production_rows = build_production_rows()
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
