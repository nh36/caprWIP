# Model entry implementation report — 2254 three / þrīe

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2254-three-þrīe.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2254-three-þrīe.md`
- `Germanic/docs/lexeme_reports/research_memos/2254-three-þrīe.md`
- `Germanic/docs/lexeme_reports/research_memos/batch_06_summary.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1980-cow-cȳ.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2027-follow-fylġan.model.md`
- `Germanic/docs/lexeme_reports/model_entries/1958-both-bū.model.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_01_report.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_02_report.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_02_revision_report.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_03_report.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_04_report.md`
- `Germanic/docs/lexeme_reports/model_entries/production_batch_04_revision_report.md`
- `Germanic/docs/lexeme_reports/writing_skill/README.md`
- `Germanic/docs/lexeme_reports/writing_skill/source_ledger_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/book_entry_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/writing_skill/anti_patterns.md`
- `Germanic/docs/lexeme_reports/writing_skill/scaling_plan.md`
- `docs/refs.bib`
- local reference files for Campbell, Fulk, Kroonen, and supporting handbook extracts reused in `DEV_NOTES`

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2254-three-þrīe.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2254-three-þrīe.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2254-three-þrīe.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2254-three-þrīe.model_implementation_report.md`

## Notes on this pass

- Drafted the entry as an `attested_variant` case centered on the masculine
  nominative-accusative **`þrīe`**.
- Treated **`þrī`** as a later reduced variant or headword-style citation, not
  as the same paradigm cell.
- Used a manual `Variant comparison`; no new paradigm-probe artifact was added.
- Checked citation keys against `docs/refs.bib` and scanned the `.model.md`
  prose for forbidden project-facing phrases.
- No repository lint/build/test target was run; this pass only creates markdown
  production files, and no docs-specific automated target was identified.

## Citation-key check

Checked against `docs/refs.bib`:

- `Campbell1959`
- `Fulk2018`
- `Kroonen2013`

## OCR / source-transcription checks

- Reused the decisive Campbell paradigm quotation through the current
  `DEV_NOTES` extract because it preserves the relevant wording cleanly.
- Consulted Google Vision reference files where available for supporting
  handbooks; no corrupted form needed to be quoted in the final entry.

## Unresolved points

- The main review-sensitive point is still the distinction between attested
  **`þrīe`** and later reduced/headword **`þrī`**.
- Comparative dictionaries cite the numeral more broadly than the specific
  masculine cell modeled here.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  batch report was changed.
