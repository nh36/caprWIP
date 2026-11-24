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
        {"weg", "wege", "weges", "wegæ", "wæg", "wæge", "weig"},
        "Short-vowel noun ‘way’; spelling variants are retained.",
    ),
    (
        "short-V+palatal-glide",
        "dæg",
        {"dæg", "dæge", "dæges"},
        "Short-vowel noun ‘day’; uncertain dægne and plural variants are reported apart.",
    ),
    (
        "long-V+palatal-glide",
        "stīg",
        {"stīg", "stīge", "stīges", "stīgas"},
        "Long-vowel path noun; two following-vowel forms, verified in Tamoto pp. 8 and 104.",
    ),
    (
        "long-V+palatal-glide",
        "stīgan",
        {
            "astig", "astigæ", "astigen", "astigende", "astigest",
            "niþer-stigendne", "niþer-stigendum", "stigende",
        },
        "Long-ī verb forms with final g or g before a front-vowel ending; 12 tokens, one related lexical type, no monosyllabic word-form.",
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

UNCERTAIN_DAY_FORMS = {"dægne"}

AUDIT_ONLY = (
    (
        "day-plural-variants",
        "dæg",
        {"dagas", "daga", "dagum", "dagana"},
        "Inflected day-forms with different syllable structures; excluded from the matched monosyllabic panel.",
    ),
    (
        "long-V+back-vowel-g-verb-exclusions",
        "stīgan",
        {"astigan", "astigað", "stigað"},
        "Infinitive and finite forms with g before a back-vowel ending; excluded from the palatal-glide panel.",
    ),
)

FORM_METADATA = {
    ("short-V+palatal-glide", "weg", "weg"): (
        "closed monosyllable",
        "Bare form; case depends on the individual context.",
    ),
    ("short-V+palatal-glide", "weg", "wæg"): (
        "closed monosyllable",
        "Bare spelling variant; case depends on the individual context.",
    ),
    ("short-V+palatal-glide", "weg", "weig"): (
        "closed monosyllable",
        "Spelling variant in the Mark 1:3 gloss ‘prepare the way of the Lord’.",
    ),
    ("short-V+palatal-glide", "weg", "wege"): (
        "following vowel graph",
        "Inflected -e form; case varies or is unresolved across tokens.",
    ),
    ("short-V+palatal-glide", "weg", "wæge"): (
        "following vowel graph",
        "Inflected -e spelling variant; case varies or is unresolved across tokens.",
    ),
    ("short-V+palatal-glide", "weg", "wegæ"): (
        "following vowel graph",
        "Inflected spelling variant; exact case is unresolved.",
    ),
    ("short-V+palatal-glide", "dæg", "dæg"): (
        "closed monosyllable",
        "Bare singular form; nominative/accusative distinction is contextual.",
    ),
    ("short-V+palatal-glide", "dæg", "dæge"): (
        "following vowel graph",
        "Inflected -e form, generally dative singular in context.",
    ),
    ("short-V+palatal-glide", "dæg", "dæges"): (
        "following vowel graph",
        "Genitive singular.",
    ),
    ("long-V+palatal-glide", "stīg", "stigas"): (
        "following vowel graph",
        "Plural form; the Mt 3:3 context and Latin semitas support accusative plural.",
    ),
    ("long-V+palatal-glide", "stīg", "stīgas"): (
        "following vowel graph",
        "Plural spelling variant; grammatical case depends on context.",
    ),
    ("long-V+palatal-glide", "stīg", "stige"): (
        "following vowel graph",
        "Alternative gloss beside gongas; case and number are not secure.",
    ),
    ("long-V+palatal-glide", "stīgan", "astig"): (
        "closed stressed root syllable in a prefixed form",
        "Mt 27:40 imperative singular; Latin descende nunc de cruce. The word is prefixed and disyllabic; final g follows the independently long-ī root.",
    ),
    ("long-V+palatal-glide", "stīgan", "astigæ"): (
        "multisyllabic",
        "Mt 27:42 subjunctive singular; Latin descendat nunc de cruce.",
    ),
    ("long-V+palatal-glide", "stīgan", "astigen"): (
        "multisyllabic",
        "Past participle after wæs; the root vowel is independently long.",
    ),
    ("long-V+palatal-glide", "stīgan", "astigende"): (
        "multisyllabic",
        "Present participle; five tokens in the bounded corpus.",
    ),
    ("long-V+palatal-glide", "stīgan", "astigest"): (
        "multisyllabic",
        "Finite second-person form; the root vowel is independently long.",
    ),
    ("long-V+palatal-glide", "stīgan", "niþer-stigendne"): (
        "multisyllabic",
        "Inflected present participle; Latin discendentem.",
    ),
    ("long-V+palatal-glide", "stīgan", "niþer-stigendum"): (
        "multisyllabic",
        "Inflected present participle; Latin descendentibus.",
    ),
    ("long-V+palatal-glide", "stīgan", "stigende"): (
        "multisyllabic",
        "Present participle in the Mark 1:10 context.",
    ),
    ("short-HL", "gangan", "gangan"): (
        "multisyllabic",
        "Infinitive or verbal form; exact function varies by context.",
    ),
    ("short-HL", "gangan", "gangande"): (
        "multisyllabic",
        "Participial verbal form.",
    ),
    ("short-HL", "gangan", "gangende"): (
        "multisyllabic",
        "Participial verbal form.",
    ),
    ("short-HL", "gangan", "gangandne"): (
        "multisyllabic",
        "Inflected participial spelling; exact form is uncertain.",
    ),
    ("short-HL", "gangan", "gangaþ"): (
        "multisyllabic",
        "Finite verbal form; person and number depend on context.",
    ),
    ("short-HL", "gangan", "gange"): (
        "following vowel graph",
        "Inflected verbal form; mood and person are unresolved.",
    ),
    ("short-HL", "gangan", "gangene"): (
        "multisyllabic",
        "Inflected verbal form; exact analysis is unresolved.",
    ),
    ("short-HL", "gangan", "gangenne"): (
        "multisyllabic",
        "Inflected verbal form; exact analysis is unresolved.",
    ),
    ("short-HL", "gangan", "gangænde"): (
        "multisyllabic",
        "Participial spelling variant.",
    ),
    ("short-HL", "lond", "lond"): (
        "closed monosyllable",
        "Bare form; case depends on the individual context.",
    ),
    ("short-HL", "lond", "londe"): (
        "following vowel graph",
        "Inflected -e form; case varies or is unresolved across tokens.",
    ),
    ("short-HL", "lond", "londes"): (
        "following vowel graph",
        "Genitive singular.",
    ),
    ("short-HL", "lond", "londæ"): (
        "following vowel graph",
        "Inflected spelling variant; exact case is unresolved.",
    ),
    ("short-HL", "word", "word"): (
        "closed monosyllable",
        "Bare form; case depends on the individual context.",
    ),
    ("short-HL", "word", "worde"): (
        "following vowel graph",
        "Inflected -e form; case varies or is unresolved across tokens.",
    ),
    ("short-HL", "word", "wordes"): (
        "following vowel graph",
        "Genitive singular.",
    ),
    ("short-HL", "word", "wordum"): (
        "following vowel graph",
        "Dative plural.",
    ),
    ("short-HL", "hond", "hond"): (
        "closed monosyllable",
        "Bare form; case depends on the individual context.",
    ),
    ("short-HL", "hond", "honda"): (
        "following vowel graph",
        "Inflected plural or oblique form; case depends on context.",
    ),
    ("short-HL", "hond", "honde"): (
        "following vowel graph",
        "Inflected -e form; case varies or is unresolved across tokens.",
    ),
    ("short-HL", "hond", "hondum"): (
        "following vowel graph",
        "Dative plural.",
    ),
    ("short-HL", "hond", "hondæ"): (
        "following vowel graph",
        "Inflected spelling variant; exact case is unresolved.",
    ),
    ("short-HL", "cild", "cild"): (
        "closed monosyllable",
        "Bare form; number and case depend on the individual context.",
    ),
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


def source_form(token):
    return unicodedata.normalize("NFC", token.casefold())


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
    for form in UNCERTAIN_DAY_FORMS:
        wanted.setdefault(fold(form), []).append(
            ("uncertain-short-V+palatal-glide", "dæg")
        )
    for group, lemma, forms, _ in AUDIT_ONLY:
        for form in forms:
            wanted.setdefault(fold(form), []).append((group, lemma))

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
    spelling_types = {source_form(token) for _, _, token in tokens}
    marked = [token for _, _, token in tokens if accented(token)]
    marked_types = {surface_type(token) for token in marked}
    return {
        "token_count": len(tokens),
        "accented_tokens": len(marked),
        "unaccented_tokens": len(tokens) - len(marked),
        "surface_types": len(types),
        "raw_spelling_types": len(spelling_types),
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
            surface_form="ALL",
            source_forms="|".join(
                sorted({source_form(token) for _, _, token in tokens})
            ),
            graphical_structure="mixed",
            grammatical_form="multiple; see surface-form rows",
            notes=notes,
        )
        rows.append(row)
        by_class[quantity_class].append(tokens)

        for form in sorted(
            {surface_type(token) for _, _, token in tokens}
        ):
            form_tokens = [
                token for token in tokens if surface_type(token[2]) == form
            ]
            form_row = summarize(form_tokens)
            structure, grammatical_form = FORM_METADATA.get(
                (quantity_class, lemma, form),
                ("other/uncertain", "Not classified."),
            )
            form_row.update(
                record_type="surface-form",
                quantity_class=quantity_class,
                lemma=lemma,
                lexical_types_with_accent=int(form_row["accented_tokens"] > 0),
                lexical_types_total=1,
                surface_form=form,
                source_forms="|".join(
                    sorted(
                        {
                            source_form(token[2])
                            for token in form_tokens
                        }
                    )
                ),
                graphical_structure=structure,
                grammatical_form=grammatical_form,
                notes="Surface type ignores acute marking; source_forms preserves the transcribed variants.",
            )
            rows.append(form_row)

    uncertain = occurrences[("uncertain-short-HL", "gang-family")]
    uncertain_row = summarize(uncertain)
    uncertain_row.update(
        record_type="uncertain",
        quantity_class="uncertain-short-HL",
        lemma="gang-family",
        lexical_types_with_accent=int(uncertain_row["accented_tokens"] > 0),
        lexical_types_total=1,
        surface_form="ALL",
        source_forms="|".join(
            sorted({source_form(token) for _, _, token in uncertain})
        ),
        graphical_structure="mixed/uncertain",
        grammatical_form="uncertain verbal forms",
        notes="Bare gang, ganges, and gongan-spelled forms; excluded from rates.",
    )
    rows.append(uncertain_row)

    uncertain_day = occurrences[
        ("uncertain-short-V+palatal-glide", "dæg")
    ]
    uncertain_day_row = summarize(uncertain_day)
    uncertain_day_row.update(
        record_type="uncertain",
        quantity_class="uncertain-short-V+palatal-glide",
        lemma="dæg",
        lexical_types_with_accent=int(uncertain_day_row["accented_tokens"] > 0),
        lexical_types_total=1,
        surface_form="dægne",
        source_forms="dægne",
        graphical_structure="other/uncertain",
        grammatical_form="lexical and inflectional analysis unresolved",
        notes="One unaccented token; excluded from the matched sample.",
    )
    rows.append(uncertain_day_row)

    for group, lemma, _, notes in AUDIT_ONLY:
        tokens = occurrences[(group, lemma)]
        row = summarize(tokens)
        row.update(
            record_type="audit-only",
            quantity_class=group,
            lemma=lemma,
            lexical_types_with_accent=int(row["accented_tokens"] > 0),
            lexical_types_total=1,
            surface_form="ALL",
            source_forms="|".join(
                sorted({source_form(token) for _, _, token in tokens})
            ),
            graphical_structure="different structure or lexeme",
            grammatical_form="multiple; see token forms",
            notes=notes,
        )
        rows.append(row)
        for form in sorted({surface_type(token) for _, _, token in tokens}):
            form_tokens = [
                token for token in tokens if surface_type(token[2]) == form
            ]
            form_row = summarize(form_tokens)
            form_row.update(
                record_type="audit-only-form",
                quantity_class=group,
                lemma=lemma,
                lexical_types_with_accent=int(form_row["accented_tokens"] > 0),
                lexical_types_total=1,
                surface_form=form,
                source_forms="|".join(
                    sorted(
                        {
                            source_form(token[2])
                            for token in form_tokens
                        }
                    )
                ),
                graphical_structure="different structure or lexeme",
                grammatical_form="excluded from matched panel",
                notes=notes,
            )
            rows.append(form_row)

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
            surface_form="ALL",
            source_forms="",
            graphical_structure="mixed",
            grammatical_form="multiple; see surface-form rows",
            notes="Descriptive counts; repeated tokens are not independent.",
        )
        summary["folios"] = ""
        summary["file_lines"] = ""
        rows.append(summary)
        class_totals[quantity_class] = summary

        by_structure = collections.defaultdict(list)
        for panel_row in lexemes:
            lemma = panel_row["lemma"]
            tokens = occurrences[(quantity_class, lemma)]
            for token in tokens:
                form = surface_type(token[2])
                structure, _ = FORM_METADATA.get(
                    (quantity_class, lemma, form),
                    ("other/uncertain", "Not classified."),
                )
                if structure in {
                    "closed monosyllable",
                    "closed stressed root syllable in a prefixed form",
                    "following vowel graph",
                    "multisyllabic",
                }:
                    by_structure[structure].append((lemma, token))
        for structure, grouped_tokens in sorted(by_structure.items()):
            structure_tokens = [token for _, token in grouped_tokens]
            structure_summary = summarize(structure_tokens)
            lemmas = {lemma for lemma, _ in grouped_tokens}
            marked_lemmas = {
                lemma
                for lemma, token in grouped_tokens
                if accented(token[2])
            }
            structure_summary.update(
                record_type="structure-total",
                quantity_class=quantity_class,
                lemma="ALL",
                lexical_types_with_accent=len(marked_lemmas),
                lexical_types_total=len(lemmas),
                surface_form="ALL",
                source_forms="",
                graphical_structure=structure,
                grammatical_form="multiple; see surface-form rows",
                notes="Descriptive stratum; repeated tokens are not independent.",
            )
            rows.append(structure_summary)

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
        sensitivity_tokens = [
            token
            for name in included
            for lemma_tokens in by_class[name]
            for token in lemma_tokens
        ]
        sensitivity["raw_spelling_types"] = len(
            {source_form(token[2]) for token in sensitivity_tokens}
        )
        sensitivity.update(
            record_type="sensitivity",
            quantity_class=quantity_class,
            lemma="ALL",
            surface_form="ALL",
            source_forms="",
            graphical_structure="mixed",
            grammatical_form="multiple",
            folios="",
            file_lines="",
            notes="Descriptive only; short-HL controls reclassified as stated.",
        )
        rows.append(sensitivity)

    fields = (
        "record_type", "quantity_class", "lemma", "surface_form",
        "source_forms",
        "graphical_structure", "grammatical_form", "token_count",
        "accented_tokens", "unaccented_tokens", "surface_types",
        "raw_spelling_types",
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
        elif row["record_type"] == "uncertain":
            print(
                f"{row['quantity_class']}: "
                f"{row['accented_tokens']}/{row['token_count']} tokens "
                "(reported separately)"
            )


if __name__ == "__main__":
    main()
