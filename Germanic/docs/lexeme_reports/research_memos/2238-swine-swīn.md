# Research memo — 2238 swine / swīn

## Starting point

- **ID:** 2238
- **CONCEPT:** swine
- **COUNTERPART:** swīn
- **PROTO:** *swī́ną
- **PROTOFORM:** *swḯną
- **DERIVATION_CLASS:** regular
- **NOTE:** Proto: oblique *swīnăn→*swīną (n. a-stem nom.sg.; Kroonen) §17.46 Phase 2: PROTOFORM accented (ḯ = stressed long *ī, U+1E2F) so NWGmcInStemNLoss does not fire on the root *ī.

This is a note-bearing `regular` row in `coverage_audit.md`. There is no pilot lexeme report for this lexeme under `Germanic/docs/lexeme_reports/pilot/`, so the memo has to separate current evidence from older project debugging history.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the compact/live trace material showing `*swḯną -> swīn`; `oe_derivation_class_trace_report.txt`, which gives the current note and `ProtoInput: *s*w*ḯ*n*ą`; and `DEV_NOTES.md` §17.46, where the stressed-`*ḯ` tier is introduced and explicitly verified with `swḯną -> swīn`.
- **Useful background:** `DEV_NOTES.md` §17.45.3g, which diagnoses the regression `*swīną -> swī` and explains why monosyllabic root `*swīn` must keep final `-n`; `old_english_wiktionary.tsv`; Clark Hall; and the older TSV backup showing the pre-migration project state `*swīnăn`.
- **Stale or superseded:** the packet's `DEV_NOTES.md:41257` hit calling `*swīną` an accusative singular neuter n-stem unaffected by the rule; the 2026-03-11 full-trace snapshot that still prints unaccented `*swīną`; and the February backup row with `PROTO/PROTOFORM = *swīnăn`. Those are useful for chronology, but they are not the current project analysis.
- **Irrelevant or misleading if over-read:** Orel's alternate etymological headword `*swinan` is real comparative background, but it is not the live project input and should not override the row's present `PROTO`/`PROTOFORM` distinction by itself.

## Additional repo research

Beyond the packet I checked:

- `Germanic/docs/DEV_NOTES.md` at 41250-41258, 41751-41867, 41893-42041, and 42334-42339.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt`.
- `Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `Germanic/data/germanic-aligned-final.tsv.backup-2026-02-06`.
- `Germanic/data/oe_known_problems.tsv` (no entry for this row/lexeme).
- `Germanic/data/old_english_wiktionary.tsv`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `Germanic/docs/lexeme_reports/pilot/` (no existing pilot report for swine).

Main result of that wider pass: the current row is best understood as a resolved project-input problem, not as an unresolved philological one. The repo's live materials now agree on OE `swīn`; the uncertainty lies in how to represent the pre-OE form and how to keep stale regression notes from being mistaken for current evidence.

## Reconstruction and early-stage forms

This row needs the full three-way distinction.

1. **Cognate-set proto / project headword:** TSV `PROTO` `*swī́ną` is the current lexeme-level proto used for the swine cognate set. It is the project's human-readable head form, not the old stem notation `*swīnăn` and not Orel's alternate dictionary headword `*swinan`.
2. **Project derivational input:** TSV `PROTOFORM` `*swḯną` is the same nominative-singular/bare-cell form rewritten with the special stressed-`*ḯ` symbol. Its purpose is technical but principled: it marks the root `*ī` as stressed so `NWGmcInStemNLoss` applies only to unstressed suffixal `*-īn`, not here.
3. **OE target represented by the row:** `swīn`, the Old English singular headword/citation form.

Kroonen's entry is stem-based (`*swina-`), while the project note explicitly says the row proceeds from oblique `*swīnăn` to nominative `*swīną`. That means `*swīnăn` is useful background on stem shape, but not the live derivational input. The current row's real project choice is `*swī́ną` / `*swḯną` for the bare neuter a-stem citation cell.

## Old English philology

OE `swīn` is an attested noun, not a reconstructed pseudo-form. `old_english_wiktionary.tsv` gives `swīn`, and Clark Hall has `swin (y) n. wild boar, pig, hog, pl. swine`. That is enough repo-local support for the row target as a normal OE headword.

The important philological distinction is citation form versus stem/paradigm background. The row target is not the oblique stem `*swīnăn`, and it is not a plural form glossed by Modern English *swine*; it is the OE singular citation form `swīn`. I did not find repo-local evidence requiring a narrower dialect or manuscript claim than that.

## Project problem and solution

The project problem was a modelling/regression issue, not a disputed OE output. When `NWGmcInStemNLoss` was broadened, the cascade temporarily over-applied and produced `*swīną -> swī`. `DEV_NOTES.md` §17.45.3g correctly diagnosed that this was wrong because the row's `ī` is the stressed root vowel, not an unstressed in-stem suffix.

The current solution in §17.46 is the right one: keep the lexeme on the bare nominative/citation-form cell, but encode the derivational input as `*swḯną` so the rule can distinguish stressed root `*ī` from unstressed suffixal `*ī`. That yields `swīn` without reclassifying the row as analogical or exceptional. The older `*swīnăn` state and the stale `acc.sg. neut. n-stem` note should now be treated as superseded project history only.

## Paradigm probe

A paradigm probe is **not required** for this memo.

The row does not depend on choosing among competing OE paradigm cells, and the live derivation already verifies the relevant point directly: `swḯną -> swīn`, contrasted in `DEV_NOTES.md` with unstressed-suffix `swīną -> swī`. If the supervisor later wants an optional regression-control table, the useful controls would be the citation-form cell `*swḯną` plus parallel monosyllabic controls such as `*līną` and `*wīną`, but that is not necessary for the lexeme report recommendation.

## Recommended final report

Recommend a short final report stating that row 2238 represents attested OE `swīn` from the project's bare neuter citation cell `*swī́ną`, with `PROTOFORM` `*swḯną` used only to encode stressed root `*ī` and prevent the old false derivation `*swīną -> swī`. It should explicitly label `*swīnăn` and the old n-stem/accusative note as superseded project history, not current evidence.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** change recommended for clarity. The current note is basically right, but it would be clearer if it explicitly said that `PROTO = *swī́ną` is the project headword, `PROTOFORM = *swḯną` is the stress-tier input encoding, and `*swīnăn` is only background stem/paradigm history.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` text:** change recommended in a limited cleanup sense. The stale line at 41257 (`acc.sg. neut. n-stem`) should be marked or cross-referenced as superseded by §17.46 so future packeting does not keep surfacing it as live-looking evidence.
- **Dossier text:** no change recommended; no dedicated swine dossier turned up in the repo, and there is no named analysis file for this row that needs revision.

Overall recommendation: keep the live row values, do not add a known-problems entry, and focus any cleanup on clarifying the note/history boundary rather than changing the lexeme itself.
