#!/usr/bin/env python3
from __future__ import annotations

import csv
import os
import re
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
REPORTS_DIR = REPO_ROOT / "Germanic/docs/sound_changes/change_reports"
MANIFEST_PATH = REPORTS_DIR / "report_manifest.tsv"


def env_path(name: str) -> Path | None:
    raw = os.environ.get(name)
    if not raw:
        return None
    path = Path(raw)
    return path if path.is_absolute() else SCRIPT_DIR / path


OUTPUT_PATH = env_path("SOUND_CHANGE_VOLUME_OUTPUT_MD") or (SCRIPT_DIR / "sound_change_volume_alpha_01.md")
ALLOWED_STATUSES = {"pilot", "full"}
INLINE_CODE_RE = re.compile(r"`([^`\n]+)`")
BOLD_SPAN_RE = re.compile(r"(?<!\*)\*\*([^*\n]+)\*\*(?!\*)")
ITALIC_SPAN_RE = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")
FORM_CONNECTOR_WORDS = {"and", "or", "written", "spelled", "vs", "with"}
INLINE_CONNECTOR_WORDS = FORM_CONNECTOR_WORDS | {"from", "to", "through", "beside", "via"}
STAGE_LABELS = {
    "PGmc",
    "PWGmc",
    "WGmc",
    "NWGmc",
    "Angl",
    "Anglian",
    "OE",
    "WS",
    "West Saxon",
    "Mercian",
    "Northumbrian",
    "Kentish",
}
INLINE_SEPARATOR_CHARS = {"~", "/", ">", "<", "=", ",", ";", "(", ")", "[", "]", "{", "}"}
PRINT_LONG_I_ACUTE = "\u00ed"
PRINT_TILDE_EDGE_CHAR_CLASS = r"A-Za-z\u00C0-\u024F\u00F0\u00FE\u00DE\u00C6\u00E6\u0152\u0153\u014A\u014B" + PRINT_LONG_I_ACUTE
RECONSTRUCTED_STEM_TRAILING_STAR_RE = re.compile(
    rf"(?<=\*)([{PRINT_TILDE_EDGE_CHAR_CLASS}][{PRINT_TILDE_EDGE_CHAR_CLASS}0-9'./-]*)\*(?=(?:\s|$|[.,;:!?)]))"
)
FORM_TILDE_SPACING_RE = re.compile(rf"(?<=[{PRINT_TILDE_EDGE_CHAR_CLASS}0-9])~(?=[{PRINT_TILDE_EDGE_CHAR_CLASS}0-9])")
FENCED_CODE_BLOCK_RE = re.compile(r"(?ms)(^```[^\n]*\n.*?^```[ \t]*\n?)")


def normalize_print_text(text: str) -> str:
    text = RECONSTRUCTED_STEM_TRAILING_STAR_RE.sub(r"\1", text)
    return FORM_TILDE_SPACING_RE.sub(" ~ ", text)


def italicize_form(text: str) -> str:
    text = normalize_print_text(text)
    if not text:
        return text
    stripped = text.strip()
    if not stripped:
        return text
    leading = text[: len(text) - len(text.lstrip())]
    trailing = text[len(text.rstrip()) :]
    core = stripped
    if core.startswith("*") and len(core) > 1:
        return f"{leading}*{core[1:]}*{trailing}"
    return f"{leading}*{core}*{trailing}"


def keep_as_code(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if "/" in stripped or "\\" in stripped or stripped.startswith("--") or "::" in stripped:
        return True
    if re.search(r"[A-Za-z0-9_-]+\.[A-Za-z0-9._-]+", stripped):
        return True
    if re.search(r"[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+/[A-Za-z0-9_.\-/]+", stripped):
        return True
    if re.search(r"\b(?:SC|GO|RU)\d{2,4}\b", stripped):
        return True
    if re.search(r"(?:\[\{.*?\}\s*->|->\s*0\b.*\|\||\|\||\.\#\.)", stripped):
        return True
    return False


def normalize_inline_code_content(text: str) -> str:
    return normalize_print_text(text.replace("\\_", "_"))


def is_token_boundary(text: str, index: int) -> bool:
    return index <= 0 or index >= len(text) or not text[index].isalnum()


def tokenize_linguistic_span(text: str) -> list[tuple[str, str]]:
    tokens: list[tuple[str, str]] = []
    current = []
    mode = None

    def flush() -> None:
        nonlocal current, mode
        if current:
            tokens.append((mode or "sep", "".join(current)))
            current = []
            mode = None

    for char in text:
        char_mode = "word" if (char.isalnum() or char in {"*", "-", "'", ".", PRINT_LONG_I_ACUTE}) else "sep"
        if char_mode != mode:
            flush()
            mode = char_mode
        current.append(char)
    flush()
    return tokens


def next_non_whitespace_token(tokens: list[tuple[str, str]], start: int, step: int) -> tuple[str, str] | None:
    idx = start + step
    while 0 <= idx < len(tokens):
        if tokens[idx][1].strip():
            return tokens[idx]
        idx += step
    return None


def is_form_token(
    token: str,
    previous: tuple[str, str] | None = None,
    following: tuple[str, str] | None = None,
) -> bool:
    stripped = token.strip()
    if not stripped:
        return False
    lowered = stripped.lower()
    if lowered in INLINE_CONNECTOR_WORDS:
        return False
    if stripped in STAGE_LABELS:
        return False
    if stripped.startswith("*"):
        return True
    if any(char in stripped for char in ("þ", "ð", "æ", "ǣ", "œ", "ȳ", "á", "é", "í", "ó", "ú", "ā", "ē", "ī", "ō", "ū")):
        return True
    if previous and previous[0] == "sep" and any(ch in previous[1] for ch in INLINE_SEPARATOR_CHARS):
        return True
    if following and following[0] == "sep" and any(ch in following[1] for ch in INLINE_SEPARATOR_CHARS):
        return True
    if stripped.islower() and len(stripped) >= 2:
        return True
    return False


def format_linguistic_inline_code(text: str) -> str:
    normalized = normalize_inline_code_content(text)
    if keep_as_code(normalized):
        return f"`{normalized}`"
    tokens = tokenize_linguistic_span(normalized)
    if not tokens:
        return italicize_form(normalized)

    rendered: list[str] = []
    saw_form = False
    for idx, (kind, token) in enumerate(tokens):
        if kind != "word":
            rendered.append(token)
            continue
        previous = next_non_whitespace_token(tokens, idx, -1)
        following = next_non_whitespace_token(tokens, idx, 1)
        if is_form_token(token, previous=previous, following=following):
            rendered.append(italicize_form(token))
            saw_form = True
        else:
            rendered.append(token)
    if saw_form:
        return "".join(rendered)
    return italicize_form(normalized)


def convert_inline_code(text: str) -> str:
    return INLINE_CODE_RE.sub(lambda match: format_linguistic_inline_code(match.group(1)), text)


def has_linguistic_inline_code(text: str) -> bool:
    for match in INLINE_CODE_RE.finditer(text):
        if not keep_as_code(normalize_inline_code_content(match.group(1))):
            return True
    return False


def looks_like_linguistic_markup(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if keep_as_code(stripped):
        return False
    if any(char in stripped for char in ("*", "~", ">", "<", "/", "þ", "ð", "æ", "ǣ", "œ", "ȳ", "á", "é", "í", "ó", "ú", "ā", "ē", "ī", "ō", "ū")):
        return True
    if stripped in STAGE_LABELS:
        return True
    if re.search(r"\b(?:OE|PGmc|PWGmc|WGmc|NWGmc)\b", stripped):
        return True
    if stripped.islower() and len(stripped) >= 3:
        return True
    return False


def demote_bold_forms(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        inner = match.group(1)
        if not looks_like_linguistic_markup(inner):
            return match.group(0)
        inner = normalize_print_text(inner)
        return italicize_form(inner)

    return BOLD_SPAN_RE.sub(repl, text)


def unwrap_bolded_linguistic_markup(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        inner = match.group(1)
        if not looks_like_linguistic_markup(inner):
            return match.group(0)
        return normalize_print_text(inner)

    return ITALIC_SPAN_RE.sub(repl, text)


def tidy_prose(text: str) -> str:
    text = normalize_print_text(text)
    text = convert_inline_code(text)
    text = demote_bold_forms(text)
    text = unwrap_bolded_linguistic_markup(text)
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    text = re.sub(r" +", " ", text)
    return text


def tidy_markdown_prose(text: str) -> str:
    parts = FENCED_CODE_BLOCK_RE.split(text)
    cleaned_parts: list[str] = []
    for idx, part in enumerate(parts):
        if idx % 2 == 1:
            cleaned_parts.append(part)
        else:
            cleaned_parts.append(tidy_prose(part))
    return "".join(cleaned_parts)


def load_manifest_rows() -> list[dict[str, str]]:
    with MANIFEST_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        rows = [row for row in reader if (row.get("STATUS") or "").strip() in ALLOWED_STATUSES]
    if not rows:
        raise ValueError(f"No pilot/full rows found in {MANIFEST_PATH}")
    return rows


def normalize_entry_markdown(title: str, text: str) -> str:
    stripped = text.lstrip()
    lines = stripped.splitlines()
    if lines and lines[0].startswith("# "):
        body = "\n".join(lines[1:]).lstrip()
        return f"## {title}\n\n{body}".rstrip()
    return f"## {title}\n\n{stripped}".rstrip()


def build_volume_text(rows: list[dict[str, str]]) -> str:
    parts: list[str] = [
        "# Sound-change reports, alpha 01",
        "",
        "_Generated from `Germanic/docs/sound_changes/change_reports/report_manifest.tsv`. "
        "This assembly includes only manifest-backed `pilot` and `full` production reports._",
        "",
    ]

    for row in rows:
        title = (row.get("TITLE") or "").strip()
        report_path = (row.get("REPORT_PATH") or "").strip()
        if not title:
            raise ValueError(f"Manifest row is missing TITLE: {row}")
        if not report_path:
            raise ValueError(f"Manifest row is missing REPORT_PATH: {row}")

        source_path = REPORTS_DIR / report_path
        if not source_path.exists():
            raise FileNotFoundError(f"Report file not found: {source_path}")

        entry_text = tidy_markdown_prose(source_path.read_text(encoding="utf-8"))
        parts.append(normalize_entry_markdown(title, entry_text))
        parts.append("")

    return "\n".join(parts).rstrip() + "\n"


def main() -> int:
    rows = load_manifest_rows()
    output_text = build_volume_text(rows)
    OUTPUT_PATH.write_text(output_text, encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH} with {len(rows)} assembled sound-change report(s).")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise
