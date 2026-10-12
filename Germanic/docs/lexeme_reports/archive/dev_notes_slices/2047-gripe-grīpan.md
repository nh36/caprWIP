---
row_id: 2047
concept: gripe
counterpart: grīpan
proto: "*grī́paną"
protoform: "*grḯpaną"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2047 gripe / grīpan

## Current row state

- The live OE row is currently `ID = 2047`, `CONCEPT = gripe`, `COUNTERPART = grīpan`, `PROTO = *grī́paną`, `PROTOFORM = *grḯpaną`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:454-454]. For this row, `PROTO` and `PROTOFORM` should not be collapsed: `PROTO = *grī́paną` is the comparative label retained in the aligned TSV, while `PROTOFORM = *grḯpaną` is the FST-facing encoding that carries the stressed-long-`ī` tier marker introduced in the later migration work [Germanic/data/germanic-aligned-final.tsv:454-454; Germanic/docs/DEV_NOTES.md:41923-41940,42006-42023].
- The current published derivation trace is fully regular and exact: `PROTO: *grḯpaną`, `EXPECTED: grīpan`, `OUTPUTS: grīpan`, with no alternate outputs listed [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1866-1869]. The OE-side steps preserved in the snapshot are `OE Heavy Syllable Nasal Apocope: *grḯpan`, `OE Secondary Nasalization: *grḯpąn`, and `OE Weak Tail Reduction: *grḯpan`, ending in `Outcome: grīpan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1877-1885]. Nothing in the live trace suggests an active exception bucket, rescue rule, or unresolved row-local mismatch.
- `coverage_audit.md` still marks row `2047` as uncovered regular material: `| 2047 | gripe | grīpan | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:260-260]. This matters because there is no already-linked packet, memo, or prior lexeme-report dossier carrying row-specific commentary that would need to be preserved here.
- `report_manifest.tsv` still lists only the small pilot/report rows and includes no entry for row `2047`; there is therefore no manifest-backed report path already assigned to this lexeme [Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- `oe_known_problems.tsv` contains no entry for `grīpan`, `gripe`, or row `2047`, so the row is not presently managed as a known OE exception or unresolved modelling problem [Germanic/data/oe_known_problems.tsv:1-8].

## Development-note summary

No dedicated row-specific DEV_NOTES block survives for `2047 gripe / grīpan`. The only DEV_NOTES passage that names this row or this lexeme directly is the stressed-long-`ī` migration table, where row `2047` appears in Batch 1 (`1998, 2047, 2101 | drīfan, grīpan, līf`) among rows migrated from plain `*ī` to stressed-root `*ḯ` and then rebuilt, probed, mismatch-checked, and committed [Germanic/docs/DEV_NOTES.md:42006-42023].

Accordingly, the row's surviving support is mostly **shared-background-only** rather than row-local philology. The important substance to preserve is: (a) why the live `PROTOFORM` now uses `*grḯpaną` rather than plain `*grīpaną`; (b) why that notation still correctly surfaces as OE `grīpan`; and (c) that the current trace shows a clean regular derivation with no active exception narrative [Germanic/docs/DEV_NOTES.md:41923-41957,42006-42023; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1866-1885].

Because there is no surviving row-specific mismatch note, this slice must be conservative. It should treat the DEV_NOTES evidence for row `2047` as primarily **verification history** plus **shared stress-tier implementation background**, not as a lexeme-specific literature dossier. No surviving DEV_NOTES fragment argues that `grīpan` needs a different target, a different derivation class, a paradigm-cell substitution, or an exception label.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-42006-42023

- Source heading: `§17.46 Stressed long-ī tier (*ḯ) — principled fix for the *swīn regression` / `E. TSV migration (Phase 4)`
- Source line hint: `lines 42006-42023`
- Fragment type: `verification_history`
- Status: `current`; `row_specific_but_workflow_only`
- Issue tags: `protoform_notation`; `stressed_long_i`; `row_verification`; `workflow_history`
- Recommended next use: `cite when explaining why PROTOFORM is *grḯpaną and why the row counts as post-migration verified`
- Shared-with rows if relevant: `1998`; `2101`

This is the only surviving DEV_NOTES fragment that names the row directly. DEV_NOTES inventories the Phase 4 migration of stressed-root long-`ī` rows and says: `* 16 OE rows have *ī in PROTOFORM.`, `* **15** are stressed-root *ī (in the first syllable, no preceding vowel) — migrated to *ḯ.`, and then lists Batch 1 as `1998, 2047, 2101 | drīfan, grīpan, līf` [Germanic/docs/DEV_NOTES.md:42010-42023]. For row `2047`, that is not a philological argument about the lexeme's semantics or inflectional class; it is row-specific workflow evidence that the current `PROTOFORM = *grḯpaną` is the verified post-migration state.

The fragment should be used narrowly but confidently. It supports the claim that row `2047` was explicitly included in the set of stressed-root `*ī` forms whose encoding changed, and that the row was rebuilt and mismatch-checked under that regime [Germanic/docs/DEV_NOTES.md:42017-42023]. It does **not** by itself provide extra lexical detail about `grīpan`; its value is to anchor current notation and to show that the row's present regular status is not accidental or pre-migration residue.

### DEV_NOTES:line-41923-41957

- Source heading: `§17.46 Stressed long-ī tier (*ḯ) — principled fix for the *swīn regression` / `B. Notation` and `C. Pipeline plumbing`
- Source line hint: `lines 41923-41957`
- Fragment type: `shared_background_support`
- Status: `current`; `shared-background-only`
- Issue tags: `proto_vs_protoform`; `tier_semantics`; `orthography`; `surface_mapping`
- Recommended next use: `cite when explaining why *grḯpaną is an encoding choice but the attested OE target remains grīpan`
- Shared-with rows if relevant: `all stressed-root *ī rows migrated under §17.46, including 1998 and 2101 in the same batch`

This is the key shared background needed to interpret the row correctly. DEV_NOTES explains that the project adopted a separate symbol for stressed long `*ī`, concluding that `ḯ (U+1E2F LATIN SMALL LETTER I WITH DIAERESIS AND ACUTE) — works, single codepoint. **Adopted.**` It then states the principle explicitly: `The diaeresis is purely notational. Semantically *ḯ = stressed long *ī.` [Germanic/docs/DEV_NOTES.md:41930-41940]. That sentence is crucial for row `2047`: it tells the reader not to over-interpret `PROTOFORM = *grḯpaną` as a different comparative reconstruction from `PROTO = *grī́paną`. The distinction is encoding/stage-sensitive, not a change of lexeme identity.

DEV_NOTES then adds the row-relevant orthographic consequence: `The surface mapping {*ḯ} -> ī is correct: OE orthography does **not** distinguish stressed-root from unstressed-suffix long ī. The tier exists only to gate one rule (NWGmcInStemNLoss); from the moment that rule fires (or doesn't), the two collapse for orthography` [Germanic/docs/DEV_NOTES.md:41954-41957]. For row `2047`, this is the most important surviving technical statement after the migration table itself. It directly explains why an FST input with `*ḯ` is expected to surface as ordinary OE `ī`, i.e. why live `PROTOFORM = *grḯpaną` and live `COUNTERPART = grīpan` are fully compatible.

### DEV_NOTES:line-42031-42052

- Source heading: `§17.46 Stressed long-ī tier (*ḯ) — principled fix for the *swīn regression` / `F. Verification`
- Source line hint: `lines 42031-42052`
- Fragment type: `shared_verification_background`
- Status: `current`; `shared-background-only`
- Issue tags: `post_migration_checks`; `probe_regime`; `mismatch_counts`; `stability`
- Recommended next use: `cite if later work questions whether Batch 1 rows were actually checked after migration`
- Shared-with rows if relevant: `the entire §17.46 migration cohort, including row 2047`

This fragment does not mention `grīpan` by name, but it preserves the verification discipline applied to the migration that included row `2047`. DEV_NOTES says the project ran `Probes after each batch`, then records representative successful outputs such as `swḯną → swīn` and `skḯnaną → sċīnan`, and it gives the mismatch totals across the branch, ending with `Phase 4 batches 1–5 | 13 (held throughout)` [Germanic/docs/DEV_NOTES.md:42031-42052]. For row `2047`, this is **shared verification background**, not row-local derivation substance.

The right use is diagnostic and procedural: if anyone later asks whether row `2047`'s `*ḯ` form was merely mass-edited in the TSV or was actually rechecked, this fragment supports the stronger answer that the migration batches were rebuilt and mismatch-watched as a process, and that the branch-wide mismatch count stayed stable through the Phase 4 batches that included `grīpan` [Germanic/docs/DEV_NOTES.md:42017-42018,42031-42052]. It still does not replace the live derivation trace, which remains the best row-local evidence that `*grḯpaną` currently lands on `grīpan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1866-1885].

## Superseded or diagnostic material

- No lexeme-specific superseded DEV_NOTES block survives for row `2047`. Unlike rows that preserve an older bad output or a named mismatch bucket, `grīpan` is not accompanied in DEV_NOTES by any obsolete row-local `expected X, got Y` note. The absence is itself important: the replacement slice should not invent an older exception narrative that DEV_NOTES does not actually preserve [Germanic/docs/DEV_NOTES.md:42006-42052].
- The only row-specific DEV_NOTES material is workflow history, not a discarded derivation theory. Batch 1 membership (`1998, 2047, 2101 | drīfan, grīpan, līf`) is current evidence for notation migration and re-verification, but it is not a special explanation of the lexeme beyond that [Germanic/docs/DEV_NOTES.md:42020-42023].
- The row's strongest genuinely row-local evidence now comes from current state rather than from archival DEV_NOTES prose: the live TSV has `PROTO = *grī́paną`, `PROTOFORM = *grḯpaną`, and the current published trace derives exact `grīpan` with ordinary OE weak-tail cleanup only [Germanic/data/germanic-aligned-final.tsv:454-454; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1866-1885]. That means later work should treat the row as currently regular unless new literature or a new regression appears.

## Open questions for later work

- If a later lexeme packet is created for strong verbs in `*-īpaną`, add external-source support for the comparative reconstruction and OE attestation of `grīpan`; the present slice is usable, but its surviving DEV_NOTES evidence is mostly migration/encoding background rather than row-specific philological quotation [Germanic/docs/DEV_NOTES.md:41923-41957,42006-42052].
- If future reporting needs to explain the row in one sentence, the safest wording is narrow: row `2047` has no surviving row-specific DEV_NOTES problem block; the live row is regular, and the important preserved note is that stressed-root plain `*ī` was migrated to `*ḯ`, with row `2047` explicitly included in that verified batch [Germanic/docs/DEV_NOTES.md:42010-42023; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1866-1885].
- If any future clean-up revisits notation, keep the distinction explicit between comparative `PROTO = *grī́paną`, FST-facing `PROTOFORM = *grḯpaną`, and attested/target OE `grīpan`. DEV_NOTES is explicit that `*ḯ` is purely a stress-tier notation and that `{*ḯ} -> ī` at the surface, so collapsing these levels would erase useful workflow and modelling information [Germanic/docs/DEV_NOTES.md:41938-41940,41954-41957; Germanic/data/germanic-aligned-final.tsv:454-454].
