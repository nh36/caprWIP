#!/usr/bin/env python3
from __future__ import annotations

import csv
import os
import re
import sys
from collections import Counter
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
MANIFEST_PATH = SCRIPT_DIR / "manifest_all_by_class.tsv"
INTRO_PATH = SCRIPT_DIR / "section_introductions_draft.md"
TRACE_REPORT_PATH = REPO_ROOT / "Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md"
INLINE_CODE_RE = re.compile(r"`([^`]+)`")
BOLD_SPAN_RE = re.compile(r"\*\*(.+?)\*\*")
ITALIC_SPAN_RE = re.compile(r"_(?:\\.|[^_\n])+_")
FORM_CONNECTOR_WORDS = {"and", "or", "written", "spelled", "vs", "with", "plus"}
INLINE_CONNECTOR_WORDS = FORM_CONNECTOR_WORDS | {"from", "to", "through", "beside", "via"}
STAGE_LABELS = {
    "PGmc",
    "PWGmc",
    "PNWGmc",
    "NWGmc",
    "WGmc",
    "OE",
    "WS",
    "LWS",
    "Anglian",
    "West Saxon",
    "Old English",
    "Proto-Germanic",
    "West Germanic",
    "Northwest Germanic",
}
INLINE_SEPARATOR_CHARS = "<>,~/;:"
LONG_TRACE_FORM_LENGTH = 9
VERY_LONG_TRACE_FORM_LENGTH = 10
DENSE_TRACE_PANEL_ROWS = 6
LONG_TRACE_LABELS = {
    "OE High Vowel Apocope",
    "OE Unstressed Long Vowel Shortening",
    "OE Heavy Syllable Nasal Apocope",
    "NWGmc Final Long O Raising",
    "NWGmc Long E Lowering",
    "NWGmc Stressed Monosyllable O Raising",
    "PGmc Final Z Deletion",
    "NWGmc U Lowering",
}

SECTION_ORDER = [
    ("regular", "Part I. Regular derivations", "Regular derivations"),
    ("attested_variant", "Part II. Attested variants and selected comparison forms", "Attested variants and selected comparison forms"),
    ("early_analogy", "Part III. Early analogy and pre-Old-English input selection", "Early analogy and pre-Old-English input selection"),
    ("late_analogy", "Part IV. Late analogy and paradigm-cell selection", "Late analogy and paradigm-cell selection"),
    ("reconstructed_oe", "Part V. Reconstructed Old English comparators", "Reconstructed Old English comparators"),
    ("known_unmodelled", "Part VI. Known but unmodelled remodellings", "Known but unmodelled remodellings"),
    ("unexplained_unmodelled", "Part VII. Unexplained or deliberately unmodelled exceptions", "Unexplained or deliberately unmodelled exceptions"),
]

FRONT_MATTER_HEADINGS = {
    "Introduction": "Introduction",
    "Data and sources": "Data and sources",
    "Transducer and derivation method": "Transducer and derivation method",
    "Derivation classes": "Derivation classes",
}


def env_path(name: str) -> Path | None:
    raw = os.environ.get(name)
    if not raw:
        return None
    path = Path(raw)
    return path if path.is_absolute() else SCRIPT_DIR / path


OUTPUT_PATH = env_path("LEXICAL_VOLUME_OUTPUT_MD") or (SCRIPT_DIR / "lexical_volume_alpha_01.md")
REGULAR_BOOK_PROSE_DIR = env_path("LEXICAL_REGULAR_BOOK_PROSE_DIR")
PRINT_LONG_I_ACUTE = "ī\u0301"
PRINT_TILDE_EDGE_CHAR_CLASS = r"\w\u00C0-\u024F\u0300-\u036F*βʤʧþðæǣȳǭ\\_-"
RECONSTRUCTED_STEM_TRAILING_STAR_RE = re.compile(
    r"((?:\\)?\*[^\s`|<>]*?-)(?:\\)?\*(?=(?:\s|$|[`_.,;:!?)/\]\}>~]))"
)
FORM_TILDE_SPACING_RE = re.compile(
    rf"(?<=[{PRINT_TILDE_EDGE_CHAR_CLASS}])\s*~\s*(?=[{PRINT_TILDE_EDGE_CHAR_CLASS}])"
)


def parse_trace_entries(text: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
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

    for chunk in chunks:
        block = "\n".join(chunk).strip()
        lines = block.splitlines()
        table_lines: list[str] = []
        in_table = False
        for line in lines:
            if line.startswith("| Earlier Germanic developments | Old English developments |"):
                in_table = True
            if in_table and line.startswith("|"):
                table_lines.append(line)
                continue
            if in_table and not line.startswith("|"):
                break

        entries.append(
            {
                "title": lines[0][2:].strip(),
                "proto": re.search(r"^PROTO:\s*(.*)$", block, re.M).group(1).strip(),
                "expected": re.search(r"^EXPECTED:\s*(.*)$", block, re.M).group(1).strip(),
                "outputs": re.search(r"^OUTPUTS:\s*(.*)$", block, re.M).group(1).strip(),
                "proto_input": re.search(r"^Proto Input:\s*(.*)$", block, re.M).group(1).strip(),
                "outcome": re.search(r"^Outcome:\s*(.*)$", block, re.M).group(1).strip(),
                "table": "\n".join(table_lines).strip(),
            }
        )

    return entries


def normalize_print_text(text: str) -> str:
    normalized = text.replace("ḯ", PRINT_LONG_I_ACUTE)
    normalized = RECONSTRUCTED_STEM_TRAILING_STAR_RE.sub(r"\1", normalized)
    normalized = FORM_TILDE_SPACING_RE.sub(" ~ ", normalized)
    return normalized


def italicize_form(text: str) -> str:
    text = normalize_print_text(text)
    escaped = text.replace("\\", "\\\\").replace("*", r"\*").replace("|", r"\|")
    return f"_{escaped}_"


def keep_as_code(text: str) -> bool:
    return bool(
        re.search(r"(?:\.md\b|\.txt\b|\.pdf\b|\.py\b|\.sh\b|\.tsv\b|^@|^https?://|docs/|Germanic/|--\w)", text)
    )


def normalize_inline_code_content(text: str) -> str:
    return normalize_print_text(re.sub(r"\s*\n\s*", " ", text).strip())


def is_token_boundary(text: str, index: int) -> bool:
    return index >= len(text) or text[index].isspace() or text[index] in INLINE_SEPARATOR_CHARS


def tokenize_linguistic_span(text: str) -> list[tuple[str, str]]:
    tokens: list[tuple[str, str]] = []
    labels = sorted(STAGE_LABELS, key=len, reverse=True)
    i = 0

    while i < len(text):
        if text[i].isspace():
            j = i
            while j < len(text) and text[j].isspace():
                j += 1
            tokens.append(("sep", text[i:j]))
            i = j
            continue

        matched_label = None
        for label in labels:
            if text.startswith(label, i) and is_token_boundary(text, i + len(label)):
                matched_label = label
                break
        if matched_label is not None:
            tokens.append(("label", matched_label))
            i += len(matched_label)
            continue

        if text[i] in INLINE_SEPARATOR_CHARS:
            j = i
            while j < len(text) and text[j] in INLINE_SEPARATOR_CHARS:
                j += 1
            tokens.append(("sep", text[i:j]))
            i = j
            continue

        j = i
        while j < len(text) and not text[j].isspace() and text[j] not in INLINE_SEPARATOR_CHARS:
            j += 1
        tokens.append(("word", text[i:j]))
        i = j

    return tokens


def next_non_whitespace_token(
    tokens: list[tuple[str, str]], start: int, step: int
) -> tuple[str, str] | None:
    index = start
    while 0 <= index < len(tokens):
        kind, value = tokens[index]
        if kind != "sep" or value.strip():
            return tokens[index]
        index += step
    return None


def is_form_token(token: str, previous: tuple[str, str] | None, following: tuple[str, str] | None) -> bool:
    if token in STAGE_LABELS:
        return False
    if token.lower() in INLINE_CONNECTOR_WORDS:
        return False
    if token.startswith("*"):
        return True
    if re.search(r"[ǣæþðġċĀāĒēĪīŌōŪūȲȳÁÉÍÓÚáéíóúḗǭĕăβʤ]", token):
        return True
    if re.fullmatch(r"[a-z]+(?:[-'][a-z]+)*", token):
        if previous is not None and previous[0] == "label":
            return True
        if previous is not None and previous[0] == "sep" and previous[1] in {"<", ">", "~", "/"}:
            return True
        if following is not None and following[0] == "sep" and following[1] in {"<", ">", "~", "/"}:
            return True
    return False


def format_linguistic_inline_code(text: str) -> str:
    tokens = tokenize_linguistic_span(text)
    rendered: list[str] = []
    saw_form = False

    for index, token in enumerate(tokens):
        kind, value = token
        if kind == "sep":
            rendered.append(value)
            continue
        if kind == "label":
            rendered.append(value)
            continue

        previous = next_non_whitespace_token(tokens, index - 1, -1)
        following = next_non_whitespace_token(tokens, index + 1, 1)
        if is_form_token(value, previous, following):
            rendered.append(italicize_form(value))
            saw_form = True
        else:
            rendered.append(value)

    if not saw_form:
        return italicize_form(text)
    return "".join(rendered)


def convert_inline_code(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        inner = normalize_inline_code_content(match.group(1))
        return match.group(0) if keep_as_code(inner) else format_linguistic_inline_code(inner)

    return INLINE_CODE_RE.sub(repl, text)


def has_linguistic_inline_code(text: str) -> bool:
    code_spans = [normalize_inline_code_content(span) for span in INLINE_CODE_RE.findall(text)]
    return bool(code_spans) and any(not keep_as_code(span) for span in code_spans)


def looks_like_linguistic_markup(text: str) -> bool:
    if "\n" in text or not text.strip():
        return False

    has_form = False

    def mark_code(match: re.Match[str]) -> str:
        nonlocal has_form
        inner = normalize_inline_code_content(match.group(1))
        if keep_as_code(inner):
            return match.group(0)
        has_form = True
        return " FORM "

    def mark_italic(match: re.Match[str]) -> str:
        nonlocal has_form
        has_form = True
        return " FORM "

    working = INLINE_CODE_RE.sub(mark_code, text)
    working = ITALIC_SPAN_RE.sub(mark_italic, working)
    if not has_form:
        return False

    words = re.findall(r"[A-Za-z][A-Za-z/-]*", working)
    if any(word.lower() not in FORM_CONNECTOR_WORDS | {"form"} for word in words):
        return False

    remainder = re.sub(r"\bFORM\b", " ", working)
    remainder = re.sub(
        rf"\b(?:{'|'.join(sorted(FORM_CONNECTOR_WORDS))})\b",
        " ",
        remainder,
        flags=re.IGNORECASE,
    )
    remainder = re.sub(r"[\s,;/(){}\[\]<>~=:.\-]+", "", remainder)
    return remainder == ""


def demote_bold_forms(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        inner = match.group(1)
        if has_linguistic_inline_code(inner) or looks_like_linguistic_markup(inner):
            return inner
        return match.group(0)

    return BOLD_SPAN_RE.sub(repl, text)


def unwrap_bolded_linguistic_markup(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        inner = match.group(1)
        return inner if looks_like_linguistic_markup(inner) else match.group(0)

    return BOLD_SPAN_RE.sub(repl, text)


def tidy_prose(text: str) -> str:
    return normalize_print_text(
        unwrap_bolded_linguistic_markup(convert_inline_code(demote_bold_forms(normalize_print_text(text))))
    )


def display_stage_name(stage: str) -> str:
    if stage == "Proto-West Germanic":
        return "West Germanic"
    return stage


def parse_trace_cell(cell: str) -> list[tuple[str, list[tuple[str, str]]]]:
    pieces = [piece.strip() for piece in re.split(r"<br\s*/?>", cell) if piece.strip()]
    if not pieces:
        return []

    stages: list[tuple[str, list[str]]] = []
    current_stage = ""
    current_items: list[str] = []

    for piece in pieces:
        stage_match = re.fullmatch(r"\*\*([^*]+)\*\*", piece)
        if stage_match:
            if current_stage or current_items:
                stages.append((current_stage, current_items))
            current_stage = stage_match.group(1).strip()
            current_items = []
            continue
        current_items.append(piece)

    if current_stage or current_items:
        stages.append((current_stage, current_items))

    parsed_stages: list[tuple[str, list[tuple[str, str]]]] = []
    for stage, items in stages:
        parsed_items: list[tuple[str, str]] = []
        for item in items:
            if item == "[no change]":
                parsed_items.append((item, ""))
                continue
            if ":" in item:
                change, form = item.split(":", 1)
                change = change.strip()
                form = form.strip()
            else:
                change = item.strip()
                form = ""
            parsed_items.append((change, form))
        parsed_stages.append((display_stage_name(stage), parsed_items))

    return parsed_stages


def latex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in text)


def latex_form(text: str) -> str:
    return rf"\emph{{{latex_escape(normalize_print_text(text))}}}"


def humanize_derivation_class(label: str) -> str:
    mapping = {
        "regular": "regular",
        "attested_variant": "attested variant",
        "early_analogy": "early analogy",
        "late_analogy": "late analogy",
        "reconstructed_oe": "reconstructed Old English comparator",
        "known_unmodelled": "known but unmodelled remodelling",
        "unexplained_unmodelled": "unexplained exception",
    }
    return mapping.get(label, label.replace("_", " "))


def derivation_summary(model: dict[str, object], trace_entry: dict[str, str] | None) -> str:
    metadata = model["metadata"]
    citation = metadata.get("PROTO", "")
    selected = metadata.get("PROTOFORM", "")
    target = metadata.get("COUNTERPART", "")
    label = humanize_derivation_class(metadata.get("DERIVATION_CLASS", ""))
    arrow = ">"

    if trace_entry is None:
        return (
            f"Derivation: selected input {italicize_form(selected)} and target {italicize_form(target)}; "
            "no compact trace was confidently matched in this assembly pass."
        )

    output = trace_entry["outcome"]
    if citation == selected and output == target:
        return f"Derivation: {italicize_form(selected)} {arrow} {italicize_form(target)} ({label})."
    if citation != selected and output == target:
        return (
            f"Derivation: citation reconstruction {italicize_form(citation)}; "
            f"selected input {italicize_form(selected)} {arrow} {italicize_form(target)} ({label})."
        )
    if citation == selected and output != target:
        return (
            f"Derivation: {italicize_form(selected)} yields regular {italicize_form(output)}; "
            f"the selected target is {italicize_form(target)} ({label})."
        )
    return (
        f"Derivation: citation reconstruction {italicize_form(citation)}; "
        f"selected input {italicize_form(selected)} yields {italicize_form(output)}; "
        f"the selected target is {italicize_form(target)} ({label})."
    )


def panel_complexity(stage_blocks: list[tuple[str, list[tuple[str, str]]]]) -> dict[str, int]:
    row_count = 0
    total_change_length = 0
    max_change_length = 0
    long_label_count = 0
    form_count = 0
    total_form_length = 0
    max_form_length = 0
    long_form_count = 0

    for _, items in stage_blocks:
        for change, form in items:
            if change == "[no change]":
                continue
            row_count += 1
            change_length = len(change)
            total_change_length += change_length
            max_change_length = max(max_change_length, change_length)
            if change in LONG_TRACE_LABELS:
                long_label_count += 1
            if form:
                form_count += 1
                form_length = len(form)
                total_form_length += form_length
                max_form_length = max(max_form_length, form_length)
                if form_length >= LONG_TRACE_FORM_LENGTH:
                    long_form_count += 1

    return {
        "rows": row_count,
        "total_change_length": total_change_length,
        "max_change_length": max_change_length,
        "long_label_count": long_label_count,
        "form_count": form_count,
        "total_form_length": total_form_length,
        "max_form_length": max_form_length,
        "long_form_count": long_form_count,
    }


def choose_trace_widths(
    left_blocks: list[tuple[str, list[tuple[str, str]]]],
    right_blocks: list[tuple[str, list[tuple[str, str]]]],
) -> tuple[float, float]:
    left = panel_complexity(left_blocks)
    right = panel_complexity(right_blocks)

    if (
        left["max_form_length"] >= VERY_LONG_TRACE_FORM_LENGTH
        and right["max_form_length"] >= VERY_LONG_TRACE_FORM_LENGTH
    ):
        return 0.47, 0.47
    if left["long_label_count"] > 0 and right["long_label_count"] > 0:
        return 0.46, 0.46
    if left["rows"] <= 1 and (
        right["long_label_count"] > 0
        or right["max_change_length"] >= 24
        or right["max_form_length"] >= VERY_LONG_TRACE_FORM_LENGTH
    ):
        if right["rows"] >= DENSE_TRACE_PANEL_ROWS or right["max_form_length"] >= VERY_LONG_TRACE_FORM_LENGTH:
            return 0.28, 0.56
        return 0.30, 0.54
    if left["rows"] <= 2 and (
        right["total_change_length"] >= left["total_change_length"] + 30
        or right["max_form_length"] >= VERY_LONG_TRACE_FORM_LENGTH
    ):
        return 0.32, 0.52
    if right["rows"] <= 1 and (
        left["long_label_count"] > 0
        or left["max_change_length"] >= 24
        or left["max_form_length"] >= VERY_LONG_TRACE_FORM_LENGTH
    ):
        if left["rows"] >= DENSE_TRACE_PANEL_ROWS or left["max_form_length"] >= VERY_LONG_TRACE_FORM_LENGTH:
            return 0.56, 0.28
        return 0.54, 0.30
    if right["rows"] <= 2 and (
        left["total_change_length"] >= right["total_change_length"] + 30
        or left["max_form_length"] >= VERY_LONG_TRACE_FORM_LENGTH
    ):
        return 0.52, 0.32
    return 0.44, 0.44


def choose_panel_column_widths(panel_width: float, stats: dict[str, int]) -> tuple[float, float]:
    usable_width = 0.90
    min_label_width = 0.56 if panel_width > 0.36 else 0.52

    if stats["rows"] == 0:
        return 0.68, 0.18

    form_width = 0.16
    if stats["max_form_length"] >= 11:
        form_width = 0.26
    elif stats["max_form_length"] >= VERY_LONG_TRACE_FORM_LENGTH:
        form_width = 0.24
    elif stats["max_form_length"] >= LONG_TRACE_FORM_LENGTH:
        form_width = 0.22
    elif stats["max_form_length"] >= 8:
        form_width = 0.20

    if stats["rows"] >= DENSE_TRACE_PANEL_ROWS and stats["max_form_length"] >= LONG_TRACE_FORM_LENGTH:
        form_width = min(form_width + 0.02, 0.28)
    elif stats["rows"] >= 4 and stats["max_form_length"] >= VERY_LONG_TRACE_FORM_LENGTH:
        form_width = min(form_width + 0.02, 0.28)

    desired_label_width = 0.68
    if stats["long_label_count"] > 0:
        desired_label_width = 0.76 if stats["max_change_length"] >= 30 else 0.74
    elif stats["max_change_length"] >= 28:
        desired_label_width = 0.74
    elif stats["max_change_length"] >= 22:
        desired_label_width = 0.70
    elif panel_width <= 0.36 and stats["rows"] <= 1:
        desired_label_width = 0.64

    if stats["long_form_count"] > 0:
        desired_label_width -= 0.04
    if stats["rows"] >= DENSE_TRACE_PANEL_ROWS and stats["max_form_length"] >= LONG_TRACE_FORM_LENGTH:
        desired_label_width -= 0.06
    elif stats["rows"] >= 4 and stats["max_form_length"] >= VERY_LONG_TRACE_FORM_LENGTH:
        desired_label_width -= 0.04

    label_width = min(desired_label_width, usable_width - form_width)
    label_width = max(min_label_width, label_width)
    if label_width + form_width > usable_width:
        label_width = usable_width - form_width

    return label_width, form_width


def dense_long_form_panel(stats: dict[str, int]) -> bool:
    return stats["rows"] >= DENSE_TRACE_PANEL_ROWS and stats["max_form_length"] >= LONG_TRACE_FORM_LENGTH


def choose_trace_font_size(left_stats: dict[str, int], right_stats: dict[str, int]) -> str:
    if dense_long_form_panel(left_stats) or dense_long_form_panel(right_stats):
        return r"\footnotesize"
    return r"\small"


def format_trace_change_label(change: str, *, label_column_width: float) -> str:
    change = normalize_print_text(change)
    escaped = latex_escape(change)
    if change in LONG_TRACE_LABELS and len(change) <= 28 and label_column_width >= 0.70:
        return rf"\mbox{{{escaped}}}"
    return escaped


def render_trace_panel(
    stage_blocks: list[tuple[str, list[tuple[str, str]]]],
    *,
    suppress_old_english_stage: bool = False,
    label_column_width: float = 0.62,
    form_column_width: float = 0.24,
) -> list[str]:
    lines = [r"\raggedright"]

    for index, (stage, items) in enumerate(stage_blocks):
        show_stage_header = not (suppress_old_english_stage and stage == "Old English")
        if index:
            lines.append(r"\vspace{0.6em}")

        if show_stage_header:
            lines.extend(
                [
                    rf"\centering\textbf{{{latex_escape(stage)}}}\par",
                    r"\raggedright",
                    r"\vspace{0.2em}",
                ]
            )

        if not items:
            lines.append(r"\raggedright [no change]\par")
            continue

        if all(change == "[no change]" and not form for change, form in items):
            lines.append(r"\raggedright [no change]\par")
            continue

        lines.append(
            rf"\begin{{tabular}}{{@{{}}>{{\raggedright\arraybackslash}}p{{{label_column_width:.2f}\linewidth}}@{{\hspace{{0.55em}}}}>{{\raggedright\arraybackslash}}p{{{form_column_width:.2f}\linewidth}}@{{\hspace{{0.25em}}}}}}"
        )
        for change, form in items:
            if change == "[no change]" and not form:
                lines.append(r"\multicolumn{2}{@{}l@{}}{[no change]} \\")
            elif form:
                lines.append(
                    rf"{format_trace_change_label(change, label_column_width=label_column_width)} & {latex_form(form)} \\"
                )
            else:
                lines.append(
                    rf"\multicolumn{{2}}{{@{{}}l@{{}}}}{{{format_trace_change_label(change, label_column_width=label_column_width)}}} \\"
                )
        lines.append(r"\end{tabular}")

    return lines


def render_trace_table(trace_entry: dict[str, str]) -> list[str]:
    table_lines = trace_entry["table"].splitlines()
    if len(table_lines) < 3:
        return [normalize_print_text(trace_entry["table"])]

    row_parts = [part.strip() for part in table_lines[2].strip().strip("|").split("|")]
    if len(row_parts) != 2:
        return [normalize_print_text(trace_entry["table"])]

    left_blocks = parse_trace_cell(row_parts[0])
    right_blocks = parse_trace_cell(row_parts[1])
    left_width, right_width = choose_trace_widths(left_blocks, right_blocks)
    left_stats = panel_complexity(left_blocks)
    right_stats = panel_complexity(right_blocks)
    left_label_width, left_form_width = choose_panel_column_widths(left_width, left_stats)
    right_label_width, right_form_width = choose_panel_column_widths(right_width, right_stats)
    trace_font_size = choose_trace_font_size(left_stats, right_stats)
    left_panel = render_trace_panel(
        left_blocks,
        label_column_width=left_label_width,
        form_column_width=left_form_width,
    )
    right_panel = render_trace_panel(
        right_blocks,
        suppress_old_english_stage=True,
        label_column_width=right_label_width,
        form_column_width=right_form_width,
    )

    return [
        r"\begingroup",
        r"\setlength{\fboxsep}{6pt}",
        r"\noindent\fbox{%",
        r"\begin{minipage}{0.97\linewidth}",
        trace_font_size,
        rf"\begin{{tabularx}}{{\linewidth}}{{@{{}}>{{\raggedright\arraybackslash}}p{{{left_width:.3f}\linewidth}}>{{\centering\arraybackslash}}X>{{\raggedright\arraybackslash}}p{{{right_width:.3f}\linewidth}}@{{}}}}",
        r"\begin{minipage}[t]{\linewidth}",
        r"\centering\textbf{Earlier Germanic changes}\par",
        r"\vspace{0.35em}",
        *left_panel,
        r"\end{minipage}",
        r"&",
        r"&",
        r"\begin{minipage}[t]{\linewidth}",
        r"\centering\textbf{Old English changes}\par",
        r"\vspace{0.35em}",
        *right_panel,
        r"\end{minipage}",
        r"\\",
        r"\end{tabularx}",
        r"\end{minipage}%",
        r"}",
        r"\endgroup",
    ]


def parse_model_entry(path: Path) -> dict[str, object]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines:
        raise ValueError(f"empty model entry: {path}")

    title_line = next((line.strip() for line in lines if line.strip()), "")
    if not title_line.startswith("# "):
        raise ValueError(f"missing heading in model entry: {path}")

    metadata: dict[str, str] = {}
    title_index = lines.index(title_line)
    i = title_index + 1
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    while i < len(lines):
        match = re.match(r"^([A-Z_]+):\s*(.*)$", lines[i].strip())
        if not match:
            break
        metadata[match.group(1)] = match.group(2).strip()
        i += 1

    title = title_line[2:].strip()
    sections: list[tuple[str, str]] = []
    current_heading: str | None = None
    current_lines: list[str] = []
    for line in lines[i:]:
        if line.startswith("### "):
            if current_heading is not None:
                sections.append((current_heading, "\n".join(current_lines).strip()))
            current_heading = line.strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_heading is not None:
        sections.append((current_heading, "\n".join(current_lines).strip()))

    lexical_item = title.split(" — OE ", 1)[0].strip()
    return {
        "title": title,
        "lexical_item": lexical_item,
        "metadata": metadata,
        "sections": sections,
    }


def match_trace_entry(model: dict[str, object], trace_entries: list[dict[str, str]]) -> tuple[dict[str, str] | None, str, bool]:
    metadata = model["metadata"]
    lexical_item = model["lexical_item"]
    proto = metadata.get("PROTO", "")
    protoform = metadata.get("PROTOFORM", "")
    counterpart = metadata.get("COUNTERPART", "")

    candidates = [entry for entry in trace_entries if entry["title"] == lexical_item]
    scored: list[tuple[int, dict[str, str], list[str]]] = []
    for entry in candidates:
        score = 0
        basis: list[str] = ["lexical item"]
        if entry["proto"] == protoform:
            score += 10
            basis.append("PROTOFORM")
        if entry["proto"] == proto and proto:
            score += 4
            basis.append("PROTO")
        if entry["expected"] == counterpart and counterpart:
            score += 6
            basis.append("EXPECTED")
        if entry["outputs"] == counterpart and counterpart:
            score += 6
            basis.append("OUTPUTS")
        scored.append((score, entry, basis))

    if not scored:
        return None, "no lexical-item match", False

    scored.sort(key=lambda item: item[0], reverse=True)
    top_score, top_entry, basis = scored[0]
    confident = top_score >= 16 and (len(scored) == 1 or top_score > scored[1][0])
    return top_entry, " + ".join(basis), confident


def demote_model_heading(heading: str) -> str:
    return "#### " + heading.removeprefix("### ").strip()


def rewrite_entry(model: dict[str, object], trace_entry: dict[str, str] | None) -> str:
    out: list[str] = [f"### {model['title']}", "", derivation_summary(model, trace_entry)]

    if trace_entry is not None:
        out.extend(
            [
                "",
                "#### Derivation trace",
                "",
                f"Proto input: {italicize_form(trace_entry['proto_input'])}",
                "",
                *render_trace_table(trace_entry),
                "",
            ]
        )
        if trace_entry["outcome"] == model["metadata"].get("COUNTERPART", ""):
            out.append(f"Outcome: {italicize_form(trace_entry['outcome'])}")
        else:
            out.append(f"Transducer outcome: {italicize_form(trace_entry['outcome'])}")
            out.append("")
            out.append(f"Selected target: {italicize_form(model['metadata'].get('COUNTERPART', ''))}")

    for heading, body in model["sections"]:
        if heading == "### Transducer input and output":
            continue
        cleaned_body = tidy_prose(body)
        out.extend(["", demote_model_heading(heading), ""])
        if cleaned_body:
            out.append(cleaned_body)

    return "\n".join(out).strip()


def book_prose_path(entry_path: Path, prose_dir: Path) -> Path:
    return prose_dir / entry_path.name.replace(".model.md", ".book.md")


def rewrite_book_prose_entry(model: dict[str, object], trace_entry: dict[str, str] | None, body: str) -> str:
    out: list[str] = [f"### {model['title']}", "", derivation_summary(model, trace_entry)]
    if trace_entry is not None:
        out.extend(["", *render_trace_table(trace_entry)])
    if body.strip():
        out.extend(["", tidy_prose(body).strip()])
    return "\n".join(out).strip()


def render_entry(
    model: dict[str, object],
    trace_entry: dict[str, str] | None,
    *,
    entry_path: Path,
    regular_book_prose_dir: Path | None,
) -> str:
    if model["metadata"].get("DERIVATION_CLASS") == "regular" and regular_book_prose_dir is not None:
        prose_path = book_prose_path(entry_path, regular_book_prose_dir)
        if not prose_path.exists():
            raise FileNotFoundError(f"missing regular book prose file: {prose_path}")
        body = prose_path.read_text(encoding="utf-8")
        return rewrite_book_prose_entry(model, trace_entry, body)
    return rewrite_entry(model, trace_entry)


def parse_section_introductions(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    sections: dict[str, str] = {}
    current_heading: str | None = None
    current_lines: list[str] = []

    for line in text.splitlines():
        if line.startswith("## "):
            if current_heading is not None:
                sections[current_heading] = "\n".join(current_lines).strip()
            current_heading = line[3:].strip()
            current_lines = []
        elif current_heading is not None:
            current_lines.append(line)

    if current_heading is not None:
        sections[current_heading] = "\n".join(current_lines).strip()
    return sections


def build_front_matter(
    counts: Counter[str],
    intro_sections: dict[str, str],
    *,
    regular_book_prose_dir: Path | None,
) -> list[str]:
    compact_regular_active = regular_book_prose_dir is not None
    alpha_blurb = (
        "_Alpha 01 compact-regular assembly scaffold. This document assembles the current lexeme-report corpus in manifest order. Regular entries use the compact book-prose layer requested for rollout; non-regular entries retain the current model-entry prose._"
        if compact_regular_active
        else "_Alpha 01 assembly scaffold. This document assembles the current lexeme-report corpus in manifest order without revising entry-level prose, citations, locators, or transducer logic._"
    )
    method_paragraph = (
        "Regular entries use the compact book-prose overlay for this assembly pass, while the remaining derivation classes still reproduce the current model-entry prose. All entries retain a generated derivation summary and a boxed derivation trace split into Earlier Germanic changes and Old English changes."
        if compact_regular_active
        else "Each lexical entry retains the pilot structure: a generated derivation summary, a boxed derivation trace split into Earlier Germanic changes and Old English changes, and the current model-entry prose. The summary distinguishes citation reconstruction, selected input, transducer outcome, and selected target where those differ, and the boxed trace remains a compact PDF-oriented rendering of the current compact trace data."
    )
    lines = [
        "# Germanic Lexeme Reports: Lexical Derivation Volume",
        "",
        normalize_print_text(alpha_blurb),
        "",
        "## Introduction",
        "",
        tidy_prose(intro_sections["Introduction to the lexical catalogue"]),
        "",
        tidy_prose(intro_sections["Note on the later sound-change volume / report"]),
        "",
        "## Data and sources",
        "",
        normalize_print_text(
            "This alpha assembles the current model-entry corpus against the live manifest, compact derivation-trace report, and project bibliography. The lexical data layer is the current aligned Germanic dataset as represented by the model-entry metadata and the current compact trace source; comparative dictionaries, Old English dictionaries, and historical grammars remain in the entry prose exactly as already cited there."
        ),
        "",
        normalize_print_text(
            "Broad citations are carried forward honestly where the citation-layer audit already judged them mechanically acceptable for assembly. This alpha therefore tests book structure and technical integration rather than attempting a final source-polish pass."
        ),
        "",
        "## Transducer and derivation method",
        "",
        normalize_print_text(method_paragraph),
        "",
        "## Derivation classes",
        "",
        normalize_print_text(
            "The lexical catalogue is ordered by the seven live `DERIVATION_CLASS` values in the manifest. Counts in this alpha are taken directly from `manifest_all_by_class.tsv`:"
        ),
        "",
        f"- `regular`: **{counts['regular']}**",
        f"- `attested_variant`: **{counts['attested_variant']}**",
        f"- `early_analogy`: **{counts['early_analogy']}**",
        f"- `late_analogy`: **{counts['late_analogy']}**",
        f"- `reconstructed_oe`: **{counts['reconstructed_oe']}**",
        f"- `known_unmodelled`: **{counts['known_unmodelled']}**",
        f"- `unexplained_unmodelled`: **{counts['unexplained_unmodelled']}**",
    ]
    return lines


def append_references_scaffold(parts: list[str]) -> None:
    parts.extend(["", r"\clearpage", "", "## References", ""])


def assert_print_regressions(text: str) -> None:
    if "ḯ" in text:
        raise ValueError("reader-facing output still contains ḯ")
    if "PNWGmce" in text:
        raise ValueError("reader-facing output still contains PNWGmce")
    if "_\\*wīþja-_-type" in text:
        raise ValueError("reader-facing output still contains a malformed *wīþja--type phrase")
    expected_breeches_phrase = "PNWGmc _\\*brokiz_ > _\\*breeci_ > OE _bréc_"
    if "### breeches — OE brēċ" in text and expected_breeches_phrase not in text:
        raise ValueError("reader-facing output is missing the normalized breeches stage phrase")


def main() -> int:
    trace_entries = parse_trace_entries(TRACE_REPORT_PATH.read_text(encoding="utf-8"))
    intro_sections = parse_section_introductions(INTRO_PATH)

    with MANIFEST_PATH.open(encoding="utf-8", newline="") as handle:
        manifest_rows = list(csv.DictReader(handle, delimiter="\t"))

    counts = Counter(row["class_bucket"] for row in manifest_rows)
    parts: list[str] = build_front_matter(counts, intro_sections, regular_book_prose_dir=REGULAR_BOOK_PROSE_DIR)

    rows_by_bucket: dict[str, list[dict[str, str]]] = {}
    for bucket, _, _ in SECTION_ORDER:
        rows_by_bucket[bucket] = [row for row in manifest_rows if row["class_bucket"] == bucket]

    if REGULAR_BOOK_PROSE_DIR is not None:
        if not REGULAR_BOOK_PROSE_DIR.exists():
            raise FileNotFoundError(f"regular book prose directory not found: {REGULAR_BOOK_PROSE_DIR}")
        missing_regular = [
            str(book_prose_path(REPO_ROOT / row["model_entry_path"], REGULAR_BOOK_PROSE_DIR))
            for row in rows_by_bucket["regular"]
            if not book_prose_path(REPO_ROOT / row["model_entry_path"], REGULAR_BOOK_PROSE_DIR).exists()
        ]
        if missing_regular:
            missing_list = "\n".join(missing_regular)
            raise FileNotFoundError(f"missing regular book prose files:\n{missing_list}")

    for bucket, part_heading, intro_heading in SECTION_ORDER:
        parts.extend(["", r"\clearpage", "", f"## {part_heading}", "", tidy_prose(intro_sections[intro_heading])])
        for row in rows_by_bucket[bucket]:
            entry_path = REPO_ROOT / row["model_entry_path"]
            model = parse_model_entry(entry_path)
            trace_entry, basis, confident = match_trace_entry(model, trace_entries)
            if trace_entry is None or not confident:
                print(f"WARNING: trace match unresolved for {entry_path.name} ({basis})", file=sys.stderr)
                trace_entry = None
            else:
                print(
                    f"Matched {entry_path.name} -> {trace_entry['title']} / {trace_entry['proto']} / {trace_entry['outputs']} ({basis})",
                    file=sys.stderr,
                )
            parts.extend(
                [
                    "",
                    render_entry(
                        model,
                        trace_entry,
                        entry_path=entry_path,
                        regular_book_prose_dir=REGULAR_BOOK_PROSE_DIR,
                    ),
                ]
            )

    append_references_scaffold(parts)
    assembled = normalize_print_text("\n".join(parts).rstrip())
    assert_print_regressions(assembled)
    OUTPUT_PATH.write_text(assembled + "\n", encoding="utf-8")
    print(f"Generated {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
