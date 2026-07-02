#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
import unicodedata
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BOOK_DIR = REPO_ROOT / "Germanic/docs/book"
TSV_PATH = REPO_ROOT / "Germanic/data/germanic-aligned-final.tsv"
COMPACT_PATH = REPO_ROOT / "Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md"
CHRONOLOGY_PATH = REPO_ROOT / "Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.md"
MODEL_ENTRIES_DIR = REPO_ROOT / "Germanic/docs/lexeme_reports/model_entries"
FORMS_PATH = BOOK_DIR / "index_verborum_forms.tsv"
OVERRIDES_PATH = BOOK_DIR / "index_verborum_overrides.tsv"
AUDIT_PATH = BOOK_DIR / "index_verborum_audit.md"

LANGUAGE_ORDER = ["oe", "pgmc", "pwgmc", "nwgmc", "preoe", "on", "ohg", "ofris", "goth", ""]
LANGUAGE_TITLES = {
    "oe": "Old English",
    "pgmc": "Proto-Germanic",
    "pwgmc": "Proto-West Germanic",
    "nwgmc": "Proto-Northwest Germanic",
    "preoe": "Pre-Old-English and model-internal",
    "on": "Old Norse",
    "ohg": "Old High German",
    "ofris": "Old Frisian",
    "goth": "Gothic",
}
FORM_RE = re.compile(r"[A-Za-zÀ-ɏḀ-ỿþðæǣœȳċġǭǫáéíóúāēīōūḗḯ'./*-]+")
MARKUP_FORM_RE = re.compile(r"\\emph\{([^}]+)\}|`([^`]+)`|\*([^*\n]+)\*|_([^_\n]+)_")
CHANGE_LABEL_RE = re.compile(
    r"(?P<label>PGmc|Proto-Germanic|PWGmc|Proto-West-Germanic|NWGmc|Proto-Northwest-Germanic|"
    r"OE|Old English|WS|West Saxon|Anglian|Old Norse|ON|OHG|Old High German|"
    r"Old Frisian|OFri|Gothic|Goth)[^:\n]{0,80}:\s*(?P<form>\\emph\{[^}]+\}|`[^`]+`|\*[^*\n]+\*|_[^_\n]+_|[^\s<,;:()]+)"
)
IMMEDIATE_LABEL_RE = re.compile(
    r"(?P<label>PGmc|Proto-Germanic|PWGmc|Proto-West-Germanic|NWGmc|Proto-Northwest-Germanic|"
    r"OE|Old English|WS|West Saxon|Anglian|Old Norse|ON|OHG|Old High German|"
    r"Old Frisian|OFri|Gothic|Goth)\s+(?P<form>\\emph\{[^}]+\}|`[^`]+`|\*[^*\n]+\*|_[^_\n]+_|[^\s<,;:()]+)"
)


@dataclass
class FormCandidate:
    form: str
    sources: set[str] = field(default_factory=set)
    languages: set[str] = field(default_factory=set)
    status: str = "auto"


def strip_markup(text: str) -> str:
    value = text.strip()
    if "<" in value or ">" in value:
        return ""
    for prefix, suffix in ((r"\emph{", "}"), ("`", "`"), ("*", "*"), ("_", "_")):
        if value.startswith(prefix) and value.endswith(suffix):
            value = value[len(prefix) : len(value) - len(suffix)]
            break
    return value.strip("`.,;:!?()[]{}“”\"' ")


def looks_linguistic(text: str) -> bool:
    if not text or " " in text or "/" in text or ".md" in text or ".pdf" in text:
        return False
    if "*" in text and not text.startswith("*"):
        return False
    if len(re.sub(r"[^A-Za-zÀ-ɏḀ-ỿþðæǣœȳċġǭǫáéíóúāēīōūḗḯ]+", "", text.lstrip("*"))) < 2:
        return False
    if text.startswith("*"):
        return True
    if any(ch in text for ch in "þðæǣœȳċġǭǫáéíóúāēīōūḗḯ"):
        return True
    return False


def normalize_sort_key(text: str) -> str:
    text = text.lstrip("*").casefold()
    normalized = unicodedata.normalize("NFKD", text)
    stripped = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", "", stripped)


def default_regex(text: str) -> str:
    escaped = re.escape(text)
    return rf"(?<![A-Za-zÀ-ɏḀ-ỿþðæǣœȳċġǭǫáéíóúāēīōūḗḯ*]){escaped}(?![A-Za-zÀ-ɏḀ-ỿþðæǣœȳċġǭǫáéíóúāēīōūḗḯ])"


def label_to_language(label: str, form: str) -> str:
    if label in {"PGmc", "Proto-Germanic"}:
        return "pgmc"
    if label in {"PWGmc", "Proto-West-Germanic"}:
        return "pwgmc"
    if label in {"NWGmc", "Proto-Northwest-Germanic"}:
        return "nwgmc"
    if label in {"OE", "Old English", "WS", "West Saxon", "Anglian"}:
        return "preoe" if form.startswith("*") else "oe"
    if label in {"Old Norse", "ON"}:
        return "on"
    if label in {"OHG", "Old High German"}:
        return "ohg"
    if label in {"Old Frisian", "OFri"}:
        return "ofris"
    if label in {"Gothic", "Goth"}:
        return "goth"
    return ""


def add_candidate(store: dict[str, FormCandidate], form: str, source: str, language: str = "") -> None:
    cleaned = strip_markup(form)
    if not looks_linguistic(cleaned):
        return
    candidate = store.setdefault(cleaned, FormCandidate(form=cleaned))
    candidate.sources.add(source)
    if language:
        candidate.languages.add(language)


def extract_labeled_forms(text: str, source: str, store: dict[str, FormCandidate], include_broad: bool = False) -> None:
    for line in text.splitlines():
        for pattern in (CHANGE_LABEL_RE, IMMEDIATE_LABEL_RE):
            for match in pattern.finditer(line):
                form = strip_markup(match.group("form"))
                language = label_to_language(match.group("label"), form)
                add_candidate(store, form, source, language)
        if include_broad:
            for match in MARKUP_FORM_RE.finditer(line):
                raw = next(group for group in match.groups() if group)
                form = strip_markup(raw)
                if form and form not in store:
                    add_candidate(store, form, source)


def extract_tsv_rows(store: dict[str, FormCandidate]) -> None:
    with TSV_PATH.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            doculect = (row.get("DOCULECT") or "").strip()
            if doculect != "Old_English":
                continue
            counterpart = (row.get("COUNTERPART") or "").strip()
            if counterpart and counterpart != "-":
                add_candidate(store, counterpart, "tsv:COUNTERPART", "oe")
            for field in ("PROTO", "PROTOFORM"):
                value = (row.get(field) or "").strip()
                if value:
                    add_candidate(store, value, f"tsv:{field}", "pgmc")


def extract_compact_report(store: dict[str, FormCandidate]) -> None:
    for line in COMPACT_PATH.read_text(encoding="utf-8").splitlines():
        for prefix, language in (("PROTO:", "pgmc"), ("EXPECTED:", "oe")):
            if line.startswith(prefix):
                add_candidate(store, line.split(":", 1)[1].strip(), f"compact:{prefix[:-1]}", language)
        if line.startswith("OUTPUTS:"):
            for item in [part.strip() for part in line.split(":", 1)[1].split(",") if part.strip()]:
                add_candidate(store, item, "compact:OUTPUTS", "preoe" if item.startswith("*") else "oe")
        extract_labeled_forms(line, "compact:stage", store, include_broad=False)


def extract_model_entries(store: dict[str, FormCandidate]) -> None:
    for path in sorted(MODEL_ENTRIES_DIR.glob("*.model.md")):
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        if lines and "— OE " in lines[0]:
            add_candidate(store, lines[0].split("— OE ", 1)[1].strip(), f"{path.name}:heading", "oe")
        for line in lines:
            for prefix, language in (("PROTO:", "pgmc"), ("PROTOFORM:", "pgmc"), ("COUNTERPART:", "oe")):
                if line.startswith(prefix):
                    add_candidate(store, line.split(":", 1)[1].strip(), f"{path.name}:{prefix[:-1]}", language)
            extract_labeled_forms(line, path.name, store, include_broad=True)


def load_overrides() -> dict[str, dict[str, str]]:
    overrides: dict[str, dict[str, str]] = {}
    if not OVERRIDES_PATH.exists():
        return overrides
    with OVERRIDES_PATH.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            form = (row.get("form") or "").strip()
            if form:
                overrides[form] = {key: (value or "").strip() for key, value in row.items()}
    return overrides


def write_outputs(store: dict[str, FormCandidate], strict: bool) -> int:
    overrides = load_overrides()
    rows: list[dict[str, str]] = []
    unresolved: list[dict[str, str]] = []
    for form, candidate in store.items():
        row = {
            "language": "",
            "form": form,
            "display": form,
            "sort_key": normalize_sort_key(form),
            "regex": default_regex(form),
            "source": "; ".join(sorted(candidate.sources)),
            "status": candidate.status,
        }
        if form in overrides:
            row.update({key: value for key, value in overrides[form].items() if key in row and value})
            row["status"] = overrides[form].get("status") or "override"
        elif len(candidate.languages) == 1:
            row["language"] = next(iter(candidate.languages))
        elif len(candidate.languages) > 1:
            row["status"] = "ambiguous"
        else:
            row["status"] = "unassigned"
        rows.append(row)
        if row["status"] in {"ambiguous", "unassigned"}:
            unresolved.append(row)

    rows.sort(key=lambda row: (LANGUAGE_ORDER.index(row["language"]) if row["language"] in LANGUAGE_ORDER else len(LANGUAGE_ORDER), row["sort_key"], row["form"]))
    with FORMS_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=["language", "form", "display", "sort_key", "regex", "source", "status"])
        writer.writeheader()
        writer.writerows(rows)

    audit_lines = [
        "# Index verborum audit",
        "",
        f"- Total candidate forms: {len(rows)}",
        f"- Resolved forms: {len(rows) - len(unresolved)}",
        f"- Unresolved forms: {len(unresolved)}",
        "",
    ]
    if unresolved:
        audit_lines.extend([
            "## Unresolved forms",
            "",
            "| Form | Status | Sources |",
            "| --- | --- | --- |",
        ])
        for row in unresolved:
            audit_lines.append(f"| `{row['form']}` | {row['status']} | {row['source']} |")
        audit_lines.append("")
    else:
        audit_lines.extend(["_No unresolved forms._", ""])
    AUDIT_PATH.write_text("\n".join(audit_lines), encoding="utf-8")
    if unresolved:
        print(f"Warning: unresolved index forms = {len(unresolved)}; see {AUDIT_PATH}")
    return 1 if strict and unresolved else 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when unresolved forms remain.")
    args = parser.parse_args()
    BOOK_DIR.mkdir(parents=True, exist_ok=True)
    store: dict[str, FormCandidate] = {}
    extract_tsv_rows(store)
    extract_compact_report(store)
    extract_model_entries(store)
    extract_labeled_forms(CHRONOLOGY_PATH.read_text(encoding="utf-8"), "reader-facing", store, include_broad=True)
    raise SystemExit(write_outputs(store, strict=args.strict))


if __name__ == "__main__":
    main()
