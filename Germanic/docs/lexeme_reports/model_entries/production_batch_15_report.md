# Production batch 15 report

## Entries selected

The following rows were selected from
`Germanic/docs/lexeme_reports/production_backlog.tsv` using these criteria:

- `PRIORITY_TIER = P3_manifest_pilot_review_or_upgrade`
- `PRODUCTION_STATUS` is `manifest_pilot` or `format_test`
- `SOURCE_MATERIAL_STATUS = manifest_backed`
- an existing pilot path or equivalent manifest-backed source is present
- no pre-existing current `.model.md` entry in
  `Germanic/docs/lexeme_reports/model_entries/`
- ascending ID order after the last reviewed P3 row from batch 14:
  `2240 tap / tæppa`
- live backlog metadata, pilot path, and current-model absence verified before drafting

This batch contained **fewer than 10** eligible P3 rows. All **1** remaining
eligible P3 row was reviewed, and **P3 is now exhausted**. The next project
phase should be decided separately.

Selected entry:

1. `2250 thistle / þistles` — `PROTOFORM *θístilas` — `late_analogy` —
   `NOTE_PRESENT yes` — `PRODUCTION_STATUS manifest_pilot` — pilot path:
   `pilot/thistle.md`

## Entries skipped and why

- No candidate rows were skipped after the final post-`2240` eligibility check.
- A full backlog pass after `2240 tap / tæppa` found only one remaining
  manifest-backed P3 row meeting the selection criteria:
  `2250 thistle / þistles`.

## Files inspected

- `Germanic/docs/lexeme_reports/pilot/thistle.md`
- `Germanic/docs/lexeme_reports/packets/2250-thistle-þistles.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2250-thistle-þistles.md`
- `Germanic/docs/lexeme_reports/research_memos/2250-thistle-þistles.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `docs/refs.bib`
- local reference files for `Campbell1959`, `ClarkHall1960`,
  `KlugeSeebold2011`, `Orel2003`

## Outcome by entry

| Entry | Outcome |
| :--- | :--- |
| `2250 thistle / þistles` | rewrite needed but completed |

No row in this batch was deferred.

## Files created

- `2250 thistle / þistles`
  - `Germanic/docs/lexeme_reports/model_entries/2250-thistle-þistles.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/2250-thistle-þistles.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2250-thistle-þistles.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/2250-thistle-þistles.model_implementation_report.md`
- Batch report
  - `Germanic/docs/lexeme_reports/model_entries/production_batch_15_report.md`

## Checklist results

| Entry | Result |
| :--- | :--- |
| `2250 thistle / þistles` | pass with caveat |

## Significant human-review issues

1. Keep simplex `þistel/ðistel` distinct from the selected genitive singular
   `þistles`.
2. Keep the comparative `*e/*i` disagreement distinct from the selected
   oblique-cell input `*θístilas`.
3. Do not generalize the thistle solution mechanically across other cluster
   nouns without separate review.

## Citation-key problems

- None found in the final `.model.md` entry.

## OCR/encoding or source-transcription issues found

- No unresolved OCR or encoding artifact was reproduced in final prose.
- Existing local vision-backed reference files were sufficient for the checked
  comparative and OE dictionary evidence.
- The main source-ranking issue in this batch was not OCR damage but evidence
  balance: the checked reference files support simplex `þistel/ðistel` more
  directly than the exact gen.sg. `þistles`, while the row-local memo, packet,
  and DEV_NOTES material support the selected inflected target and its
  phonological status.

## Google Vision consultation

- Existing local vision-backed reference files were consulted where the simplex
  headword and comparative forms mattered.
- No special Google Vision rescue beyond those local vision/reference files was
  needed for this batch.

## Source-material sufficiency

- Source material was sufficient to complete the entry.
- The pilot was structurally too project-facing for direct reuse as final prose,
  so the entry was rewritten in current book-style form.
- Direct lexicographic support in the checked reference files is stronger for
  simplex `þistel/ðistel` than for exact gen.sg. `þistles`, but the row-local
  packet, memo, DEV_NOTES slice, and live trace provide adequate support for the
  selected paradigm-cell treatment.

## Entries that should not be scaled from without human review

- `2250 thistle / þistles`

This entry now has a current-format model, but it depends on a visible
distinction between comparative headword and selected input, simplex headword
and selected oblique target, and cluster-class policy versus late West Saxon
parasiting.

## Style issues noticed across the batch

- Batch 15 contains a single remaining P3 row, so consistency pressure falls on
  maintaining the late-analogy style established in batch 14 rather than on
  balancing multiple row types.
- The main style risk was allowing the final prose to slip back into
  project-facing explanation of why the row changed. The completed entry keeps
  the discussion source-facing and philological instead.

## Post-review source-cleanup pass

- The suspicious Campbell example `tdcn` in `2250 thistle / þistles` was
  checked against the local Campbell file.
- It was corrected to `tacn` in the final model entry and source ledger.
- The substantive analysis and the record that P3 is exhausted were not changed.
- No TSV, FST, manifest, pilot, packet, memo, bibliography, derivation trace,
  existing model entry outside `2250`, or writing-skill file was changed.

## Scope confirmation

- No TSV, FST, manifest, packet, memo, bibliography, derivation trace, existing
  pilot report, existing model entry, or writing-skill file was changed.
