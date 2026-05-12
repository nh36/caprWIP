# Model entry implementation report — 2250 thistle / þistles

## Files inspected

- `Germanic/docs/lexeme_reports/pilot/thistle.md`
- `Germanic/docs/lexeme_reports/packets/2250-thistle-þistles.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2250-thistle-þistles.md`
- `Germanic/docs/lexeme_reports/research_memos/2250-thistle-þistles.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `docs/refs.bib`
- local reference files for `Campbell1959`, `ClarkHall1960`, `KlugeSeebold2011`, `Orel2003`

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2250-thistle-þistles.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2250-thistle-þistles.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2250-thistle-þistles.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2250-thistle-þistles.model_implementation_report.md`

## Outcome for this row

- **Rewrite needed but completed.** The pilot analysis was substantively usable, but the final entry needed a current-format rewrite that removed project-facing framing and centered the philological distinction between simplex `þistel` and selected genitive `þistles`.

## Notes on this pass

- Kept the three-way distinction between comparative label `*θéstilaz`, selected gen.sg. input `*θístilas`, and OE target `þistles`.
- Kept the simplex headword tradition `þistel/ðistel` in the OE evidence section rather than trying to suppress it.
- Used Campbell for the phonological contrast between broken simplex forms and unbroken oblique cluster forms.
- Did not let the final prose drift into pilot-report, manifest, or row-history language.
- Post-review source cleanup: corrected the suspicious Campbell example `tdcn` to `tacn` after rechecking the local Campbell file, which gives `tacn token` clearly at line 14506 and cross-references `tdcn` as the same word elsewhere.

## Citation-key check

Checked against `docs/refs.bib`:

- `Campbell1959`
- `ClarkHall1960`
- `KlugeSeebold2011`
- `Orel2003`

## Unresolved points

- Direct lexicographic support in the checked reference files is stronger for simplex `þistel/ðistel` than for exact gen.sg. `þistles`; the exact inflected target is better supported by the row-local memo, packet, and DEV_NOTES material.
- The comparative `*e/*i` disagreement remains real and should stay visible in any later scaling work.

## OCR and source-transcription checks

- No Campbell Google Vision-backed file was available locally.
- The local Campbell file was rechecked for the suspicious `tdcn`; a clearer internal occurrence gives `tacn token`, so the final prose and ledger now use `tacn`.
- No unresolved OCR or encoding issue was reproduced in final prose.

## Citation-locator pilot 01

- Added page-specific Pandoc locators to the paired model entry for
  `[@Orel2003, 458]`, `[@ClarkHall1960, 326]`, and `[@Campbell1959, 151]`.
- Left `KlugeSeebold2011` broad in this pilot because the local text file
  preserves the `Distel` entry without a reliable nearby page marker.

## Scope confirmation

- No TSV, FST, manifest, packet, memo, bibliography file, derivation trace, writing-skill file, pilot report, or existing model entry was changed.
