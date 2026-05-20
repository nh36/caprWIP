# Compact volume targeted cleanup 03 report

## Summary

- Files changed:
  - `Germanic/docs/assembly/build_full_lexical_volume.py`
  - `Germanic/docs/assembly/book_prose/regular_all_01/2069-hedge-heġġ.book.md`
  - `Germanic/docs/assembly/book_prose/regular_all_01/2077-hold-healdan.book.md`
  - `Germanic/docs/lexeme_reports/model_entries/1980-cow-cȳ.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2013-fire-fȳre.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2114-lung-lungen.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2240-tap-tæppa.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2296-withy-wīþiġ.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2302-world-weorold.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2308-youth-ġeoguþ.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2318-show-(3sg)-sċēawaþ.model.md`
  - regenerated `Germanic/docs/assembly/lexical_volume_regular_compact_alpha_01.{md,tex,pdf}`
- Outputs were regenerated: yes.
- Generated broad citations remain zero: yes (`0` broad citations in the regenerated compact Markdown by Docker-Pandoc AST count).
- Citations changed: no.

## Fixed serious problems

- **withy / wīþiġ**: fixed the `hereation` typo and restored the sentence to “This derivation is regular for the form compared here.”
- **world / weorold**: fixed the duplicated `here here` wording and cleaned the nearby row/result wording so the West Saxon comparison reads naturally.
- **cow / cȳ**: corrected `datative singular` to `dative singular` and replaced the paradigm-comparison machinery sentence with reader-facing wording.
- **internal class-label leakage**: removed reader-facing `known_unmodelled` prose in `fire / fȳre` and `tap / tæppa`.
- **remaining selected/manual vocabulary**: cleaned the listed reader-facing remnants in `youth / ġeoguþ`, `show / sċēawaþ`, and the generated comparison/table layer; also updated the two regular-book-prose notes that were still using `selected target here`.
- **other serious mechanical issue found**: removed the remaining `selected form` substring leak in `lung / lungen` (“selected formation” in the generated result row).

## Remaining hits

- No remaining hits were found in `Germanic/docs/assembly/lexical_volume_regular_compact_alpha_01.md` for:
  - `hereation`
  - `here here`
  - `datative`
  - `known_unmodelled`
  - `selected input`
  - `selected target`
  - `selected form`
  - `selected cell`
  - `selected comparative label`
  - `selected OE-facing input`
  - `selected present`
  - `manual probe`
  - `manual comparison`
  - `documented output`
  - `trace output`
  - `compact-trace output`
  - `->`
  - `ḯ`

## Recommendation

A. Proceed to manual PDF review.
