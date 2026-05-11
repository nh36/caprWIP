# Production batch 14 report

## Entries selected

The following 10 rows were selected from
`Germanic/docs/lexeme_reports/production_backlog.tsv` using these criteria:

- `PRIORITY_TIER = P3_manifest_pilot_review_or_upgrade`
- `PRODUCTION_STATUS` is `manifest_pilot` or `format_test`
- `SOURCE_MATERIAL_STATUS = manifest_backed`
- an existing pilot path or equivalent manifest-backed source is present
- no pre-existing current `.model.md` entry in
  `Germanic/docs/lexeme_reports/model_entries/`
- ascending ID order
- live backlog metadata, pilot path, and current-model absence verified before drafting

Selected entries:

1. `1933 adder / nǣdre` — `PROTOFORM *nḗdrōn` — `regular` —
   `NOTE_PRESENT no` — `PRODUCTION_STATUS format_test` — pilot path:
   `pilot/adder.md`
2. `1936 ban / bannes` — `PROTOFORM *bánnas` — `late_analogy` —
   `NOTE_PRESENT yes` — `PRODUCTION_STATUS manifest_pilot` — pilot path:
   `pilot/ban.md`
3. `1946 berry / berġes` — `PROTOFORM *bázjas` — `late_analogy` —
   `NOTE_PRESENT yes` — `PRODUCTION_STATUS manifest_pilot` — pilot path:
   `pilot/berry.md`
4. `1959 bottom / botm` — `PROTOFORM *búttmaz` — `early_analogy` —
   `NOTE_PRESENT yes` — `PRODUCTION_STATUS manifest_pilot` — pilot path:
   `pilot/bottom.md`
5. `1973 buck / bucc` — `PROTOFORM *búkkaz` —
   `unexplained_unmodelled` — `NOTE_PRESENT yes` —
   `PRODUCTION_STATUS manifest_pilot` — pilot path: `pilot/buck.md`
6. `1981 craft / cræft` — `PROTOFORM *kráftaz` — `early_analogy` —
   `NOTE_PRESENT yes` — `PRODUCTION_STATUS manifest_pilot` — pilot path:
   `pilot/craft.md`
7. `1983 cud / cwedu` — `PROTOFORM *kwéðuz` — `attested_variant` —
   `NOTE_PRESENT yes` — `PRODUCTION_STATUS manifest_pilot` — pilot path:
   `pilot/cud.md`
8. `2151 reek / rēac` — `PROTOFORM *ráukaz` — `reconstructed_oe` —
   `NOTE_PRESENT yes` — `PRODUCTION_STATUS manifest_pilot` — pilot path:
   `pilot/reek.md`
9. `2203 span / spanne` — `PROTOFORM *spánnai` — `late_analogy` —
   `NOTE_PRESENT yes` — `PRODUCTION_STATUS manifest_pilot` — pilot path:
   `pilot/span.md`
10. `2240 tap / tæppa` — `PROTOFORM *táppô` — `known_unmodelled` —
    `NOTE_PRESENT yes` — `PRODUCTION_STATUS manifest_pilot` — pilot path:
    `pilot/tap.md`

## Entries skipped and why

- `2013 fire / fȳre` met the backlog tier and manifest-backed criteria, but was
  skipped because a current model entry already exists at
  `Germanic/docs/lexeme_reports/model_entries/2013-fire-fȳre.model.md`.
- `2240 tap / tæppa` was therefore taken as the 10th reviewed row in ascending
  ID order.

## Files inspected

- `Germanic/docs/lexeme_reports/pilot/adder.md`
- `Germanic/docs/lexeme_reports/pilot/ban.md`
- `Germanic/docs/lexeme_reports/pilot/berry.md`
- `Germanic/docs/lexeme_reports/pilot/bottom.md`
- `Germanic/docs/lexeme_reports/pilot/buck.md`
- `Germanic/docs/lexeme_reports/pilot/craft.md`
- `Germanic/docs/lexeme_reports/pilot/cud.md`
- `Germanic/docs/lexeme_reports/pilot/reek.md`
- `Germanic/docs/lexeme_reports/pilot/span.md`
- `Germanic/docs/lexeme_reports/pilot/tap.md`
- row-local research memos for `1936`, `1946`, `1959`, `1973`, `1981`, `1983`,
  `2151`, `2203`, `2240`
- row-local DEV_NOTES slice for `1933`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `docs/refs.bib`
- local reference files cited by the pilot material and row-local memos/slice

## Outcome by entry

| Entry | Outcome |
| :--- | :--- |
| `1933 adder / nǣdre` | upgrade now |
| `1936 ban / bannes` | upgrade now |
| `1946 berry / berġes` | upgrade now |
| `1959 bottom / botm` | upgrade now |
| `1973 buck / bucc` | rewrite needed but completed |
| `1981 craft / cræft` | upgrade now |
| `1983 cud / cwedu` | rewrite needed but completed |
| `2151 reek / rēac` | upgrade now |
| `2203 span / spanne` | upgrade now |
| `2240 tap / tæppa` | rewrite needed but completed |

No row in this batch was deferred.

## Files created

- `1933 adder / nǣdre`
  - `Germanic/docs/lexeme_reports/model_entries/1933-adder-nǣdre.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/1933-adder-nǣdre.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/1933-adder-nǣdre.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/1933-adder-nǣdre.model_implementation_report.md`
- `1936 ban / bannes`
  - `Germanic/docs/lexeme_reports/model_entries/1936-ban-bannes.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/1936-ban-bannes.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/1936-ban-bannes.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/1936-ban-bannes.model_implementation_report.md`
- `1946 berry / berġes`
  - `Germanic/docs/lexeme_reports/model_entries/1946-berry-berġes.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/1946-berry-berġes.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/1946-berry-berġes.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/1946-berry-berġes.model_implementation_report.md`
- `1959 bottom / botm`
  - `Germanic/docs/lexeme_reports/model_entries/1959-bottom-botm.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/1959-bottom-botm.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/1959-bottom-botm.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/1959-bottom-botm.model_implementation_report.md`
- `1973 buck / bucc`
  - `Germanic/docs/lexeme_reports/model_entries/1973-buck-bucc.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/1973-buck-bucc.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/1973-buck-bucc.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/1973-buck-bucc.model_implementation_report.md`
- `1981 craft / cræft`
  - `Germanic/docs/lexeme_reports/model_entries/1981-craft-cræft.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/1981-craft-cræft.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/1981-craft-cræft.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/1981-craft-cræft.model_implementation_report.md`
- `1983 cud / cwedu`
  - `Germanic/docs/lexeme_reports/model_entries/1983-cud-cwedu.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/1983-cud-cwedu.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/1983-cud-cwedu.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/1983-cud-cwedu.model_implementation_report.md`
- `2151 reek / rēac`
  - `Germanic/docs/lexeme_reports/model_entries/2151-reek-rēac.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/2151-reek-rēac.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2151-reek-rēac.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/2151-reek-rēac.model_implementation_report.md`
- `2203 span / spanne`
  - `Germanic/docs/lexeme_reports/model_entries/2203-span-spanne.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/2203-span-spanne.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2203-span-spanne.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/2203-span-spanne.model_implementation_report.md`
- `2240 tap / tæppa`
  - `Germanic/docs/lexeme_reports/model_entries/2240-tap-tæppa.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/2240-tap-tæppa.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2240-tap-tæppa.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/2240-tap-tæppa.model_implementation_report.md`
- Batch report
  - `Germanic/docs/lexeme_reports/model_entries/production_batch_14_report.md`

## Checklist results

| Entry | Result |
| :--- | :--- |
| `1933 adder / nǣdre` | pass with caveat |
| `1936 ban / bannes` | pass with caveat |
| `1946 berry / berġes` | pass with caveat |
| `1959 bottom / botm` | pass with caveat |
| `1973 buck / bucc` | pass with caveat |
| `1981 craft / cræft` | pass with caveat |
| `1983 cud / cwedu` | pass with caveat |
| `2151 reek / rēac` | pass with caveat |
| `2203 span / spanne` | pass with caveat |
| `2240 tap / tæppa` | pass with caveat |

## Significant human-review issues

1. `1933 adder / nǣdre` — keep feminine `*nēdrōn-` distinct from masculine
   `*nadra-`, and keep `næddre` subordinate to `nǣdre`.
2. `1936 ban / bannes` — keep the noun distinct from older verbal material, and
   do not overstate direct attestation for exact `bannes`.
3. `1946 berry / berġes` — keep citation-form `berige/berġe` distinct from the
   selected gen.sg. `berġes`, and do not recast the row as a hidden `*rj`
   gemination case.
4. `1959 bottom / botm` — keep lexeme-level `*búdmaz` distinct from derivational
   `*búttmaz`, and keep the analogy early and stem-level.
5. `1973 buck / bucc` — keep `bucc` distinct from parallel `bucca`, and do not
   let the withdrawn cell-switch rescue re-enter later scaling work.
6. `1981 craft / cræft` — keep comparative stem-class disagreement distinct from
   the selected pre-OE input `*kráftaz`.
7. `1983 cud / cwedu` — keep `cwedu` distinct from the wider variant set
   `cwidu/cweodu/cwudu/cudu`, and keep the stale TSV `PROTO` issue out of final
   prose.
8. `2151 reek / rēac` — keep attested noun `rēc` distinct from reconstructed noun
   `rēac`, and keep verbal `rēac` out of the noun evidence line except as
   contrastive background.
9. `2203 span / spanne` — keep the noun distinct from the separate verb row
   `spannan`, and do not overstate direct attestation for exact `spanne`.
10. `2240 tap / tæppa` — keep attested noun `tæppa` distinct from regular trace
    output `tappa`, and do not revive the rejected noun-oblique or j-verb
    rescues.

## Citation-key problems

- None found in the final `.model.md` entries.

## OCR/encoding or source-transcription issues found

- No unresolved OCR or encoding artifact was reproduced in final prose.
- Existing local vision-backed dictionary and handbook files were used where
  headword, variant, or citation-form distinctions mattered.
- The most important source-ranking issue in this batch was not raw OCR damage
  but editorial distinction: exact target forms `bannes`, `berġes`, and
  `spanne` are less directly cited than the surrounding noun lexemes; `cud`
  carries stale TSV proto metadata; and `reek` required a strict separation of
  reconstructed noun target from attested noun headword.

## Google Vision consultation

- Existing local vision-backed reference files were consulted across the batch,
  especially for `1933`, `1936`, `1973`, `1981`, `1983`, `2151`, `2203`, and
  `2240`.
- No special Google Vision rescue beyond those local vision/reference files was
  needed for this batch.

## Source-material sufficiency

- Source material was sufficient for all 10 reviewed rows.
- `1933 adder / nǣdre` had thinner row-local project infrastructure than the
  other rows: no packet and no dedicated research memo were present on disk, but
  the DEV_NOTES slice, pilot note, current trace, and reference files were
  sufficient for an upgrade.
- `1936 ban / bannes`, `1946 berry / berġes`, and `2203 span / spanne` have
  sufficient material for careful current-format entries, but the exact selected
  inflected targets are less directly cited than the noun lexemes themselves.
- `1983 cud / cwedu` has sufficient source material for the attested-variant
  treatment, though the live TSV `PROTO` metadata remains stale outside this
  pass.

## Entries that should not be scaled from without human review

- `1936 ban / bannes`
- `1946 berry / berġes`
- `1973 buck / bucc`
- `1981 craft / cræft`
- `1983 cud / cwedu`
- `2151 reek / rēac`
- `2203 span / spanne`
- `2240 tap / tæppa`

These rows now have current-format entries, but each depends on a visible
distinction between citation headword and selected conservative cell,
comparative headword and modelling input, attested form and reconstructed
target, or regular output and documented exception. `1933 adder / nǣdre` and
`1959 bottom / botm` are the cleanest straightforward upgrades in the batch.

## Style issues noticed across the batch

- Batch 14 shifts from compact P2 regular-with-note drafting into the more
  varied P3 review-or-upgrade mode.
- The main style risk across the batch was flattening distinctions that the
  current model-entry format needs to keep visible: citation headword versus
  selected input (`1936`, `1946`, `1959`, `1981`, `2203`), attested variant
  versus wider lexical set (`1983`), attested headword versus reconstructed
  target (`2151`), and regular output versus documented exception (`1973`,
  `2240`).
- No final `.model.md` entry was allowed to drift back into pilot-report or
  dossier prose.

## Post-review genre-polish pass

- Final-prose references to rows, live comparator runs, and
  decisive-comparison phrasing were removed from the relevant batch-14 model
  entries.
- The substantive analyses, citations, tables, and caveats were not changed.
- No TSV, FST, manifest, pilot, packet, memo, bibliography, derivation trace,
  existing model entry outside batch 14, or writing-skill file was changed.

## Scope confirmation

- No TSV, FST, manifest, packet, memo, bibliography, derivation trace, existing
  pilot report, existing model entry, or writing-skill file was changed.
