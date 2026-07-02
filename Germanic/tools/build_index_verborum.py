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
BASELINE_PATH = BOOK_DIR / "index_verborum_baseline.tsv"

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


def broad_candidates_from_path(path: Path) -> list[CandidateOccurrence]:
    rel = path.relative_to(REPO_ROOT).as_posix()
    candidates: list[CandidateOccurrence] = []
    in_fence = False
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
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
                candidates.append(CandidateOccurrence(form=form, source_ref=f"{rel}:{line_no}", source_path=rel, line_no=line_no))
        for match in re.finditer(r"\b(?:PGmc|PWGmc|NWGmc|OE|ON|OHG|OFri|Goth)\s+(\*?[A-Za-zÀ-ɏḀ-ỿþðæǣœȳċġǭǫáéíóúāēīōūḗḯ'./()\-]+)", scrubbed):
            form = strip_markup(match.group(1))
            if form:
                candidates.append(CandidateOccurrence(form=form, source_ref=f"{rel}:{line_no}", source_path=rel, line_no=line_no))
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


def build_production_rows() -> list[ProductionOccurrence]:
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


def build_audit_rows(production_rows: list[ProductionOccurrence]) -> dict[str, list[dict[str, str]]]:
    production_forms = {row.form for row in production_rows}
    _, ignore_overrides = load_overrides()
    buckets: dict[str, list[dict[str, str]]] = defaultdict(list)
    seen: set[tuple[str, str]] = set()
    for path in source_files_for_audit():
        for candidate in broad_candidates_from_path(path):
            if (candidate.form, candidate.source_ref) in seen:
                continue
            seen.add((candidate.form, candidate.source_ref))
            if candidate.form in production_forms:
                continue
            category = candidate_category(candidate.form)
            if any(override_matches(override, form=candidate.form, source_ref=candidate.source_ref) for override in ignore_overrides):
                category = "ignored_by_override"
            buckets[category].append(
                {
                    "form": candidate.form,
                    "source_ref": candidate.source_ref,
                }
            )
    for rows in buckets.values():
        rows.sort(key=lambda row: (transliterate_sort_key(row["form"]), row["form"], row["source_ref"]))
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


def write_audit(rows: list[ProductionOccurrence], buckets: dict[str, list[dict[str, str]]]) -> int:
    counts_by_language = Counter(row.language for row in rows)
    unique_by_language = {
        language: len({row.display for row in rows if row.language == language})
        for language in counts_by_language
    }
    lines = [
        "# Index verborum audit",
        "",
        f"- Production indexed occurrences: {len(rows)}",
        f"- Production unique forms: {len({(row.language, row.display) for row in rows})}",
        f"- Audit-only candidates needing review: {len(buckets.get('needs_review', []))}",
        f"- Ignored fragments or sequences: {len(buckets.get('ignored_fragment', [])) + len(buckets.get('ignored_by_override', []))}",
        f"- Possible extraction garbage: {len(buckets.get('possible_garbage', []))}",
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

    def render_bucket(title: str, bucket_name: str) -> None:
        entries = buckets.get(bucket_name, [])
        lines.append(f"## {title}")
        lines.append("")
        if not entries:
            lines.append("_None._")
            lines.append("")
            return
        lines.append("| Form | Source |")
        lines.append("| --- | --- |")
        for entry in entries:
            lines.append(f"| `{entry['form']}` | {entry['source_ref']} |")
        lines.append("")

    render_bucket("Candidates needing language assignment", "needs_review")
    render_bucket("Ignored fragments or sequences", "ignored_fragment")
    render_bucket("Ignored by override", "ignored_by_override")
    render_bucket("Possible extraction garbage", "possible_garbage")
    AUDIT_PATH.write_text("\n".join(lines), encoding="utf-8")
    unresolved = len(buckets.get("needs_review", []))
    if unresolved:
        print(f"Warning: unresolved index candidates = {unresolved}; see {AUDIT_PATH}")
    return unresolved


def load_baseline(path: Path) -> dict[str, int]:
    metrics: dict[str, int] = {}
    if not path.exists():
        return metrics
    with path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            metric = (row.get("metric") or "").strip()
            value = (row.get("value") or "").strip()
            if metric and value:
                metrics[metric] = int(value)
    return metrics


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
        default=BASELINE_PATH,
        help="Baseline TSV used by --strict-mode=baseline.",
    )
    args = parser.parse_args()
    run_sort_key_assertions()
    BOOK_DIR.mkdir(parents=True, exist_ok=True)
    ensure_override_file()
    production_rows = build_production_rows()
    write_forms(production_rows)
    audit_buckets = build_audit_rows(production_rows)
    unresolved = write_audit(production_rows, audit_buckets)
    strict_mode = "all" if args.strict else args.strict_mode
    if strict_mode == "all":
        raise SystemExit(1 if unresolved else 0)
    if strict_mode == "baseline":
        baseline = load_baseline(args.baseline.expanduser().resolve())
        baseline_value = baseline.get("needs_review_candidates", 0)
        raise SystemExit(1 if unresolved > baseline_value else 0)
    raise SystemExit(0)


if __name__ == "__main__":
    main()
