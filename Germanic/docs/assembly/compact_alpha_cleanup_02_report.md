# Compact alpha cleanup 02 report

## Summary

- Added a **print-normalization layer** to `Germanic/docs/assembly/build_full_lexical_volume.py`.
- Removed **`ḯ` from reader-facing Markdown and TeX**, and from PDF text extraction; internal source/model notation remains unchanged.
- Normalized **tilde spacing** for linguistic alternative forms in the assembled output.
- Fixed the **`PNWGmce`** artifact in the breeches entry.
- Fixed the malformed **`*wīþja--type`** / `*wīþja-_-type` phrasing in the withy entry.
- Regenerated:
  - `Germanic/docs/assembly/lexical_volume_regular_compact_alpha_01.md`
  - `Germanic/docs/assembly/lexical_volume_regular_compact_alpha_01.tex`
  - `Germanic/docs/assembly/lexical_volume_regular_compact_alpha_01.pdf`

## Print-normalization layer

The new normalizer lives in:

- `Germanic/docs/assembly/build_full_lexical_volume.py`
- helper: `normalize_print_text(text: str) -> str`

It is applied in the assembly path at these points:

- inline-code normalization (`normalize_inline_code_content`)
- prose cleanup (`tidy_prose`)
- form rendering (`italicize_form`, `latex_form`)
- trace-label rendering (`format_trace_change_label`)
- regular book-prose insertion (`rewrite_book_prose_entry`)
- front-matter/introduction assembly
- final assembled buffer immediately before write-out

This keeps internal computational/source notation available in model metadata and trace matching while preventing it from leaking into reader-facing output.

The exact replacement is:

- `ḯ` -> `ī́`

where `ī́` is:

1. U+012B LATIN SMALL LETTER I WITH MACRON
2. U+0301 COMBINING ACUTE ACCENT

The same helper also:

- strips the stray print-only stem-final asterisk in forms such as `*hemina-*`
- normalizes linguistic alternation spacing to `form ~ form`

## Issue inventory

The full inventory is in `Germanic/docs/assembly/compact_alpha_cleanup_02_inventory.tsv`.

Fixed artifacts in this pass:

- heaven / heofon: `*hemina-*~ *hemna-*` -> `*hemina- ~ *hemna-`
- water / wæter: `*watar-~*watan-` -> `*watar- ~ *watan-`
- follow / fylġan: normalized/verified spaced alternatives around `~`
- withy / wīþiġ: `*wḯθagą` -> `*wī́θagą`
- whine / hwīnan: `*xwḯnaną` -> `*xwī́naną`
- swine / swīn: `*swḯną` -> `*swī́ną`
- tide / tīd: `*tḯdiz` -> `*tī́diz`
- withy / wīþiġ: malformed `*wīþja--type`-style phrasing -> `a comparative headword of the *wīþja- type`
- breeches / brēċ: `PNWGmce *brokiz > *breeci > OE bréc` -> `PNWGmc *brokiz > *breeci > OE bréc`
- shilling / sċilling: long trace label now wraps instead of visually crowding the form

## Verification

Searches over regenerated Markdown and TeX:

| Check | Markdown | TeX |
| --- | ---: | ---: |
| `ḯ` | 0 | 0 |
| `PNWGmce` | 0 | 0 |
| `--type` | 0 | 0 |
| `*~` | 0 | n/a |
| `~*` | 0 | n/a |
| `-~` | 0 | n/a |
| `~-` | 0 | n/a |
| `wī́θagą` | 6 | 6 |
| `xwī́naną` | 5 | 5 |
| `swī́ną` | 6 | 6 |
| `tī́diz` | 3 | 3 |

Searches over PDF text extraction:

| Check | PDF extraction |
| --- | ---: |
| `ḯ` | 0 |
| `PNWGmce` | 0 |
| `--type` | 0 |
| `*~` / `~*` / `-~` / `~-` | 0 |

Notes:

- The PDF extraction is reliable for **negative checks** here: it confirms that `ḯ`, `PNWGmce`, raw `--type`, and raw unspaced `~` artifacts no longer survive into the rendered PDF text.
- It is **not reliable for positive counting of the new combining-accent spellings**: `pdftotext` does not preserve those sequences consistently, so the positive `ī́` verification is taken from Markdown and TeX.

## Visual checks

- **heaven / heofon:** prints `*hemina- ~ *hemna-`
- **water / wæter:** prints `*watar- ~ *watan-`
- **follow / fylġan:** prints `PNWGmc *fulgija- ~ *fulgai- > OE fylgan ~ folgian`
- **withy / wīþiġ:** no malformed `*wīþja--type`; prose now reads naturally as `headword of the *wīþja- type`
- **breeches / brēċ:** `PNWGmce` is gone; the stage phrase now prints as `PNWGmc *brokiz > *breeci > OE bréc`
- **shilling / sċilling:** inspected on PDF page 17. The label no longer collapses into the form; it wraps as `PGmc Final Z` / `Deletion`, and the first-line word boxes show a positive gap before `*skíllinga` instead of overlap

## Scope confirmation

- No TSV source data were edited.
- No FST files were edited.
- No compact trace source was edited.
- No bibliography files were edited.
- No generated TeX/PDF was hand-edited.

## Recommendation

**A. Cleanup successful; proceed to broader visual/prose review.**
