#!/usr/bin/env python3
"""Reproduce a bounded Farman accent-control sample.

The panel compares fixed lexical controls in the printed Farman glosses.
It is a matched sample, not a random or corpus-wide estimate. Editorial
footnotes are excluded; ambiguous gangan-related forms are reported apart.
"""

import collections
import re
import unicodedata
from pathlib import Path

from extract_farman_accents import END, SOURCE, START

OUT = Path(__file__).resolve().parent / "FARMAN_ACCENT_CALIBRATION.tsv"
TOKEN_RE = re.compile(r"[^\s,.;:·‘’()\[\]0-9&=ˉ]+")
FOLIO_RE = re.compile(r"\[folio\s+(\d+[rv])\]")
NOTE_RE = re.compile(r"^\s*\d+\.")

PANEL = (
    (
        "short-V+palatal-glide",
        "weg",
        {"weg", "wege", "weges", "wegæ", "wæg", "wæge"},
        "Short-vowel noun ‘way’; spelling variants are retained.",
    ),
    (
        "short-V+palatal-glide",
        "dæg",
        {"dæg", "dæge", "dæges", "dægne"},
        "Short-vowel noun ‘day’; compounds are excluded.",
    ),
    (
        "long-V+palatal-glide",
        "stīg",
        {"stīg", "stīge", "stīges", "stīgas"},
        "Long-vowel path noun; only two tokens occur in the bounded text.",
    ),
    (
        "short-HL",
        "gangan",
        {
            "gangan", "gangande", "gangende", "gangaþ", "gangenne",
            "gangandne", "gangene", "gange", "gangænde",
        },
        "Short a before homorganic ng; clear verbal forms only.",
    ),
    (
        "short-HL",
        "lond",
        {"lond", "londe", "londes", "londæ"},
        "Short vowel before nd.",
    ),
    (
        "short-HL",
        "word",
        {"word", "worde", "wordes", "wordum"},
        "Short vowel before rd.",
    ),
    (
        "short-HL",
        "hond",
        {"hond", "honda", "honde", "hondum", "hondæ"},
        "Short vowel before nd.",
    ),
    (
        "short-HL",
        "cild",
        {"cild", "cilde", "cildes", "cildum"},
        "Short vowel before ld; included as a potential lengthening control.",
    ),
)

UNCERTAIN_FORMS = {
    "gang", "ganges", "gongende", "gongas",
}


def fold(token):
    return "".join(
        char
        for char in unicodedata.normalize("NFD", token.casefold())
        if not unicodedata.combining(char)
    )


def surface_type(token):
    decomposed = unicodedata.normalize("NFD", token.casefold())
    return unicodedata.normalize(
        "NFC", "".join(char for char in decomposed if char != "\u0301")
    )


def accented(token):
    return "\u0301" in unicodedata.normalize("NFD", token)


def collect_tokens():
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    wanted = {}
    for quantity_class, lemma, forms, _ in PANEL:
        for form in forms:
            wanted.setdefault(fold(form), []).append((quantity_class, lemma))
    for form in UNCERTAIN_FORMS:
        wanted.setdefault(fold(form), []).append(("uncertain-short-HL", "gang-family"))

    occurrences = collections.defaultdict(list)
    folio = "1r"
    in_note = False
    for index in range(START, END):
        line = lines[index]
        marker = FOLIO_RE.search(line)
        if marker:
            folio = marker.group(1)
            in_note = False
        if NOTE_RE.match(line):
            in_note = True
            continue
        if in_note:
            continue
        for token in TOKEN_RE.findall(line):
            for key in wanted.get(fold(token), ()):
                occurrences[key].append((index + 1, folio, token))
    return occurrences


def summarize(tokens):
    types = {surface_type(token) for _, _, token in tokens}
    marked = [token for _, _, token in tokens if accented(token)]
    marked_types = {surface_type(token) for token in marked}
    return {
        "token_count": len(tokens),
        "accented_tokens": len(marked),
        "unaccented_tokens": len(tokens) - len(marked),
        "surface_types": len(types),
        "accented_surface_types": len(marked_types),
        "folios": " ".join(dict.fromkeys(folio for _, folio, _ in tokens)),
        "file_lines": " ".join(str(line) for line, _, _ in tokens),
    }


def main():
    occurrences = collect_tokens()
    rows = []
    by_class = collections.defaultdict(list)
    for quantity_class, lemma, forms, notes in PANEL:
        tokens = occurrences[(quantity_class, lemma)]
        row = summarize(tokens)
        row.update(
            record_type="control",
            quantity_class=quantity_class,
            lemma=lemma,
            lexical_types_with_accent=int(row["accented_tokens"] > 0),
            lexical_types_total=1,
            notes=notes,
        )
        rows.append(row)
        by_class[quantity_class].append(tokens)

    uncertain = occurrences[("uncertain-short-HL", "gang-family")]
    uncertain_row = summarize(uncertain)
    uncertain_row.update(
        record_type="uncertain",
        quantity_class="uncertain-short-HL",
        lemma="gang-family",
        lexical_types_with_accent=int(uncertain_row["accented_tokens"] > 0),
        lexical_types_total=1,
        notes="Bare gang, ganges, and gongan-spelled forms; excluded from rates.",
    )
    rows.append(uncertain_row)

    summary_classes = (
        "short-V+palatal-glide",
        "long-V+palatal-glide",
        "short-HL",
    )
    class_totals = {}
    for quantity_class in summary_classes:
        tokens = [
            token
            for lemma_tokens in by_class[quantity_class]
            for token in lemma_tokens
        ]
        summary = summarize(tokens)
        lexemes = [
            row for row in rows
            if row["record_type"] == "control"
            and row["quantity_class"] == quantity_class
        ]
        summary.update(
            record_type="class-total",
            quantity_class=quantity_class,
            lemma="ALL",
            lexical_types_with_accent=sum(
                row["lexical_types_with_accent"] for row in lexemes
            ),
            lexical_types_total=len(lexemes),
            notes="Descriptive counts; repeated tokens are not independent.",
        )
        summary["folios"] = ""
        summary["file_lines"] = ""
        rows.append(summary)
        class_totals[quantity_class] = summary

    for quantity_class, included in (
        (
            "sensitivity-HL-as-short",
            ("short-V+palatal-glide", "short-HL"),
        ),
        (
            "sensitivity-HL-as-lengthened",
            ("long-V+palatal-glide", "short-HL"),
        ),
    ):
        totals = [
            class_totals[name]
            for name in included
        ]
        sensitivity = {
            key: sum(row[key] for row in totals)
            for key in (
                "token_count",
                "accented_tokens",
                "unaccented_tokens",
                "surface_types",
                "accented_surface_types",
                "lexical_types_with_accent",
                "lexical_types_total",
            )
        }
        sensitivity.update(
            record_type="sensitivity",
            quantity_class=quantity_class,
            lemma="ALL",
            folios="",
            file_lines="",
            notes="Descriptive only; short-HL controls reclassified as stated.",
        )
        rows.append(sensitivity)

    fields = (
        "record_type", "quantity_class", "lemma", "token_count",
        "accented_tokens", "unaccented_tokens", "surface_types",
        "accented_surface_types", "lexical_types_with_accent",
        "lexical_types_total", "folios", "file_lines", "notes",
    )
    with OUT.open("w", encoding="utf-8") as output:
        output.write("\t".join(fields) + "\n")
        for row in rows:
            output.write("\t".join(str(row[field]) for field in fields) + "\n")

    print(f"Wrote {OUT}")
    for row in rows:
        if row["record_type"] == "class-total":
            print(
                f"{row['quantity_class']}: "
                f"{row['accented_tokens']}/{row['token_count']} tokens; "
                f"{row['accented_surface_types']}/{row['surface_types']} "
                f"surface types; "
                f"{row['lexical_types_with_accent']}/"
                f"{row['lexical_types_total']} lexical types"
            )
        elif row["record_type"] == "uncertain":
            print(
                f"{row['quantity_class']}: "
                f"{row['accented_tokens']}/{row['token_count']} tokens "
                "(excluded from rates)"
            )
        elif row["record_type"] == "sensitivity":
            print(
                f"{row['quantity_class']}: "
                f"{row['accented_tokens']}/{row['token_count']} tokens; "
                f"{row['accented_surface_types']}/{row['surface_types']} "
                f"surface types; "
                f"{row['lexical_types_with_accent']}/"
                f"{row['lexical_types_total']} lexical types"
            )


if __name__ == "__main__":
    main()
