---
row_id: 2153
concept: ride
counterpart: rīdan
proto: *rḯdaną
protoform: *rī́daną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2153 ride / rīdan

## Current row state

- CONCEPT: `ride`
- COUNTERPART: `rīdan`
- PROTO: `*rḯdaną`
- PROTOFORM: `*rī́daną`
- DERIVATION_CLASS: `regular`
- Live TSV row `2153` is the OE `ride` row and currently carries no row-specific explanatory note beyond inherited source markers [Germanic/data/germanic-aligned-final.tsv:866-866].
- `old_english_wiktionary.tsv` also maps English `ride` to OE `rīdan`, so the row target is the ordinary OE infinitive, not a special reconstructed replacement target [Germanic/data/old_english_wiktionary.tsv:214-214].
- Direct row/lexeme search of `Germanic/data/oe_known_problems.tsv` returned no hit, so this row is not currently tracked as an open OE exception.
- Current repo coverage still lists row `2153` as uncovered (`packet? no`, no memo/dossier yet), which is why this slice has blank packet and memo metadata fields [Germanic/docs/lexeme_reports/coverage_audit.md:326-326].
- The current derivation snapshot remains stable: `PROTO: *rḯdaną`, `EXPECTED: rīdan`, `OUTPUTS: rīdan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3630-3649].

## Development-note summary

The securely relevant DEV_NOTES material for row `2153` is narrow but current. There is no long ride-specific mismatch dossier, because the row is not a live failure case. Instead, DEV_NOTES treats `rīdan` as a **control case** in the audit of dental Verner verbs: the theoretical Proto-Germanic infinitive would be `*rīþaną`, but the project is allowed to use a leveled voiced dental in the OE-directed input because Old English generalized the Verner-grade `d` throughout the paradigm. The key wording is explicit: “Current TSV uses the leveled form with `*d`. This is correct for our purposes … The true PGmc infinitive would be `*rīþaną`, but OE generalized the Verner `d` throughout the paradigm. Since the infinitive IS the form we're targeting, using leveled `*rīdăną` is acceptable” [Germanic/docs/DEV_NOTES.md:7425-7440].

For this row, the most important distinction is therefore **not** a special OE sound-law repair, but the separation of three layers that could otherwise be conflated. The live row keeps `PROTO` `*rḯdaną` and `PROTOFORM` `*rī́daną`; DEV_NOTES does not try to replace either with a new row policy. What it adds is a phonological contrast between the **theoretical inherited infinitive** `*rīþaną` and the **acceptable leveled comparator** `*rīdăną`. The note's point is that the row may remain regular because the targeted OE form is the leveled infinitive itself, and the cascade already reaches `rīdan` from the present row input [Germanic/data/germanic-aligned-final.tsv:866-866; Germanic/docs/DEV_NOTES.md:7436-7440; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3630-3649].

DEV_NOTES is equally explicit about why `ride` does **not** need the special handling used for `findan`. In the same audit it says that only one explicit `*ð` form in the TSV is correct, because `findan` is unique: North Sea Lengthening specifically targets voiceless `*-nþ-`, so `*finþaną` misbehaves unless the row is redirected to a paradigm cell with regular voiced `*ð`. `rīdan` does not present that hazard. DEV_NOTES states this directly: the dental Verner verbs that already work with leveled protoforms are acceptable because leveling happened in PGmc/PWGmc, the leveled infinitive is exactly the form being derived, and “for `rīdan`, there's no `*n` before the dental, so no NSL issue” [Germanic/docs/DEV_NOTES.md:7444-7459].

The clarification block immediately following that audit is worth carrying over because it prevents a common misreading of the row. DEV_NOTES quotes Campbell and Fulk to say that PGmc `*d` and `*ð` were allophones, with stops “initially and after nasal consonants … otherwise voiced fricatives,” while the real contrast relevant for NSL is `*þ` (voiceless) versus `*ð` (voiced) [Germanic/docs/DEV_NOTES.md:7463-7518]. For row `2153`, that means a leveled `d`-spelling in the OE-directed comparator is **not** asserting some new phonemic `*d` opposed to `*ð`; it is just a safe way to encode the voiced dental outcome in a verb where no `*-nþ-` cluster exists to trigger false NSL [Germanic/docs/DEV_NOTES.md:7481-7534].

The only other direct DEV_NOTES attachment for this row is late verification, not a new analysis. In the `*ḯ` migration table, row `2153` appears in Batch 3 (`rīdan`, `sċīnan`, `sīde`) among forms “checked + committed,” which shows that the row stayed accepted after the long-vowel notation migration [Germanic/docs/DEV_NOTES.md:42018-42024]. Taken together with the current debug trace, that means the replacement working note for `rīdan` should preserve a very specific conclusion: this row is presently **stable and regular**, and the only reasoning later reviewers are likely to need is why the row may remain on a leveled voiced-dental comparator instead of being forced back to theoretical `*rīþaną` or to a special `*ð`-marked paradigm-cell workaround [Germanic/docs/DEV_NOTES.md:7425-7459,42018-42024; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3630-3649].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-7401-7459

- Source heading: `Further Research: Other Potential *ð Forms in TSV (2026-03-11)`
- Source line or section hint: `lines 7401-7459`
- fragment_type: `lexeme_specific`
- current_status: `current`
- Issue tags: `dental_verner`; `verners_law`; `leveling`; `protoform_vs_proto`; `NSL`
- recommended_next_use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling row-policy fragment. DEV_NOTES first sets up the broader audit of dental Verner verbs, then names `ride` directly in the status table as theoretical `*rīþaną` but live/project `*rīdăną -> rīdan` [Germanic/docs/DEV_NOTES.md:7401-7433]. The decisive row-specific prose follows immediately: “Current TSV uses the leveled form with `*d`. This is correct for our purposes,” because the “true PGmc infinitive would be `*rīþaną`, but OE generalized the Verner `d` throughout the paradigm,” and because “the infinitive IS the form we're targeting” [Germanic/docs/DEV_NOTES.md:7436-7440]. The same fragment also states the negative comparator that must be preserved: `findan` needed exceptional handling because NSL attacks `*-nþ-`, but “for `rīdan`, there's no `*n` before the dental, so no NSL issue” [Germanic/docs/DEV_NOTES.md:7444-7459]. For row `2153`, this fragment is the main authority for keeping the row regular and for not importing the `findan` workaround.

### DEV_NOTES:line-7461-7534

- Source heading: `Clarification: PGmc *d vs *ð — Allophony vs Phonemic Contrast`
- Source line or section hint: `lines 7461-7534`
- fragment_type: `phenomenon_context_for_lexeme`
- current_status: `current`
- Issue tags: `dental_verner`; `allophony`; `NSL`; `phonological_encoding`
- recommended_next_use: `cite_in_final_report`
- Shared with row IDs:

This is shared phonological context, but it matters directly for `rīdan` because it explains why the row can safely stay on a voiced-dental comparator without a special `*ð` notation. DEV_NOTES quotes Campbell §398.3 that “b, d existed only initially, and in the groups mb, nd … ð, v did not exist initially or after nasals,” and Fulk that “The characters b, d, g represent voiced stops initially and after nasal consonants … otherwise voiced fricatives” [Germanic/docs/DEV_NOTES.md:7469-7479]. It then sharpens the real contrast: NSL targets nasal + **voiceless** fricative (`*-nþ-`, `*-nf-`, `*-ns-`), but not `*-nð-` or `*-nd-` [Germanic/docs/DEV_NOTES.md:7481-7518]. The fragment's closing implication is the part to preserve for this row: writing `*d` rather than `*ð` does not claim a phonemic opposition between them; it marks a safe voiced-dental representation when no NSL-sensitive environment is at stake [Germanic/docs/DEV_NOTES.md:7520-7534].

### DEV_NOTES:line-42018-42024

- Source heading: `E. TSV migration (Phase 4)`
- Source line or section hint: `lines 42018-42024`
- fragment_type: `copied_shared_lexeme_fragment`
- current_status: `current`
- Issue tags: `vowel_notation`; `verification_history`; `batch_migration`; `protoform_vs_proto`
- recommended_next_use: `cite_in_final_report`
- Shared with row IDs: `2182`, `2188`

This is not a ride-specific argument block, but it is the only later DEV_NOTES passage that names row `2153` again after the March dental-Verner audit. The table lists Batch 3 as `2153, 2182, 2188 | rīdan, sċīnan, sīde` under forms “checked + committed” during the `*ḯ` migration [Germanic/docs/DEV_NOTES.md:42018-42024]. For this slice the fragment establishes a narrow but useful fact: whatever notation-layer distinction the live row now preserves between `*rḯdaną` and `*rī́daną`, DEV_NOTES treats row `2153` as already verified under the migrated long-vowel notation rather than as an open cleanup item.

## Superseded or diagnostic material

- The misleading move for this row would be to copy `findan`'s repair strategy over to `ride`. DEV_NOTES explicitly says `findan` is special because NSL targets `*-nþ-`, whereas `rīdan` has no pre-dental nasal cluster and therefore no corresponding NSL problem [Germanic/docs/DEV_NOTES.md:7444-7459].
- The theoretical infinitive `*rīþaną` remains valuable comparative background, but it is **not** current row policy by itself. The current project decision is to allow the leveled voiced-dental comparator for the OE infinitive target, not to retarget the row to a different paradigm cell and not to treat `*rīþaną` as a mandatory live-row rewrite [Germanic/docs/DEV_NOTES.md:7425-7440].
- The late `*ḯ` migration note is verification-only. It should not be over-read as a new philological argument about `rīdan`; its value is simply that row `2153` stayed checked after notation cleanup [Germanic/docs/DEV_NOTES.md:42018-42024].

## Open questions for later work

- If later reporting needs a more explicit philological account, add a short source audit tying the ordinary OE infinitive `rīdan` to the DEV_NOTES claim that the historical infinitive was `*rīþaną` but was leveled to `d` before the OE stage; current DEV_NOTES authority is adequate for row policy, but terse on broader comparative attestation.
- If `Germanic/docs/lexeme_reports/dev_notes_slices/index.tsv` is updated later, index this row with one current row-specific decision fragment (`7401-7459`), one current shared phonology fragment (`7461-7534`), and one current verification fragment (`42018-42024`).
- If notation cleanup is revisited later, document more explicitly how live-row `PROTO` `*rḯdaną` and `PROTOFORM` `*rī́daną` relate to DEV_NOTES' comparison forms `*rīþaną` and `*rīdăną`, so future reviewers do not mistake notation-layer differences for conflicting lexical analyses.
