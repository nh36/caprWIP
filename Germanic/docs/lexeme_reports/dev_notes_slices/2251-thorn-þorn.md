---
row_id: 2251
concept: thorn
counterpart: þorn
proto: *θúrnaz
protoform: *θúrnaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2251-thorn-þorn.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2251-thorn-þorn.md
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2251 thorn / þorn

## Current row state

- CONCEPT: `thorn`
- COUNTERPART: `þorn`
- PROTO: `*θúrnaz`
- PROTOFORM: `*θúrnaz`
- DERIVATION_CLASS: `regular`
- Live TSV row: row `2251` currently reads `thorn / þorn / *θúrnaz / regular` and carries the note `Adopt *θurnăz (m. a-stem; Kroonen *θurna-). A u-stem reformation *θurnuz is reflected in Gothic þaurnus (u-stem), and Old Norse also shows an ija-stem variant þyrnir 'thorn' (alongside þorn).` [Germanic/data/germanic-aligned-final.tsv:1245-1245].
- Existing row infrastructure: both packet and research memo already use the stem `2251-thorn-þorn`, so the slice reuses that same stem rather than inventing a new filename [Germanic/docs/lexeme_reports/packets/2251-thorn-þorn.md:1-18; Germanic/docs/lexeme_reports/research_memos/2251-thorn-þorn.md:1-13; Germanic/docs/lexeme_reports/research_memo_index.tsv:113-113].
- Known-problems status: no `oe_known_problems.tsv` entry was located for row `2251`, `*θúrnaz`, `*θurnuz`, or `þorn`, so this row is not being managed as a live OE exception bucket.
- Comparative source baseline: Kroonen has `*þurna- m. 'thorn, briar' ... ON þorn m. 'id.', OE porn m. 'id.'`, while Orel keeps the broader masculine pair `*þurnuz *þurnaz sb.m.: Goth þaurnus 'thorn-plant', ON þorn 'thorn', OE ðorn id.`; Bright's glossary also preserves ordinary OE `þorn, m., thorn` with plural `þornas` [@Kroonen2013, pp. 552-553; @Orel2003, p. 430; @BrightCassidyRingler1971].

## Detailed development-note summary

Current row policy is straightforward, but surviving `DEV_NOTES.md` support is thin and mostly historical. The live row itself is coherent: `PROTO` and `PROTOFORM` are both the project input `*θúrnaz`, `COUNTERPART` is the ordinary OE lemma `þorn`, and `DERIVATION_CLASS` is `regular` [Germanic/data/germanic-aligned-final.tsv:1245-1245]. Nothing in the current repo indicates that the row now depends on a special paradigm-cell substitute, a dialect-only target, or a still-open FST rescue.

The philological background preserved in the live TSV note is defensible, but it needs to be read with the row-state distinctions kept explicit. Kroonen's comparative headword is `*þurna- m. 'thorn, briar'`, with OE `þorn` among the reflexes; Orel presents the same lexical family as masculine `*þurnuz *þurnaz`, explicitly citing Gothic `þaurnus`, Old Norse `þorn`, and OE `ðorn` [@Kroonen2013, pp. 552-553; @Orel2003, p. 430]. That means the row's current `PROTO = PROTOFORM = *θúrnaz` is not an arbitrary invention: it is a permissible project input within a comparative set that also preserves a Gothic u-stem reformation. The OE target itself is ordinary and well supported, not a project-only convenience form [@BrightCassidyRingler1971].

What `DEV_NOTES.md` actually contributes for this row is mostly chronology. One early note says that “thorn” had been among the items resolved by “adopting a paradigm form in which the phonological development is lautgesetzlich” [DEV_NOTES:line-90-90]. Taken by itself, that sentence suggests an older project stage in which the thorn row was handled by swapping to a special inflectional or stem-class form. The live row no longer looks like that. It now keeps the citation-form-style target `þorn`, uses `*θúrnaz` directly as both `PROTO` and `PROTOFORM`, and classifies the derivation as regular [Germanic/data/germanic-aligned-final.tsv:1245-1245]. The older DEV_NOTES line is therefore best preserved as superseded project history, not as current instruction for how row 2251 is supposed to work.

A later DEV_NOTES audit preserves a second piece of chronology: `*θurnuz → þōrn` appears in a list of “diacritic mismatch traces” that were judged to be orthography/alignment issues rather than phonology failures [DEV_NOTES:line-2621-2621]. This matters because it shows what at least one earlier probe looked like. The project had, at some stage, explicitly tested the u-stem-style input `*θurnuz` and obtained `þōrn`, i.e. a near-miss differing in diacritic/quantity from the intended target. That trace is valuable diagnostic history, but it is not the live row design. The row no longer uses `*θurnuz` as `PROTOFORM`, and the current TSV note treats the u-stem as comparative background reflected in Gothic rather than as the active OE derivational input [Germanic/data/germanic-aligned-final.tsv:1245-1245].

Accordingly, this slice should function as a conservative replacement working note. The current project decision is simply to keep row 2251 as regular `*θúrnaz -> þorn`, while preserving two older DEV_NOTES signals: first, that thorn once circulated in a paradigm-form-fix discussion; second, that a u-stem diagnostic probe `*θurnuz -> þōrn` also existed in project history [DEV_NOTES:line-90-90,2621-2621]. Those signals are useful for later report writers because they explain why the TSV note mentions Gothic `þaurnus` and stem-formation alternatives without implying that the live row still requires any such workaround.

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-88-93

- Source heading: `Could we use paradigm forms? (Why we decided not to)`
- Source line or section hint: `lines 88-93`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `paradigm_form_history`; `historical_fix_claim`; `thorn_named_explicitly`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This fragment is the only place in surviving DEV_NOTES where `thorn` is named directly in a row-relevant way. Its crucial sentence is: “For other problematic items (fire, brand, berry, thorn), we successfully resolved mismatches by adopting a paradigm form in which the phonological development is lautgesetzlich” [DEV_NOTES:line-90-90]. For row 2251 that statement should be carried forward, but only as chronology. It records an earlier project understanding that thorn had once been solved by switching to a paradigm form; it does **not** describe the present live row, which now keeps `PROTO = PROTOFORM = *θúrnaz` and `COUNTERPART = þorn` as a regular derivation [Germanic/data/germanic-aligned-final.tsv:1245-1245].

### DEV_NOTES:line-2621-2621

- Source heading: `Diacritic mismatch traces`
- Source line or section hint: `line 2621`
- Fragment type: `diagnostic_trace_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `u_stem_probe`; `orthography_alignment`; `historical_near_miss`; `not_live_row_state`
- Recommended next use: `use_only_for_project_history`
- Shared with row IDs:

This fragment preserves the later diagnostic trace `*θurnuz → þōrn` inside a note saying these cases are “orthography/diacritic alignment issues rather than phonology failures” [DEV_NOTES:line-2621-2621]. For row 2251 the value is narrow but real: it shows that the project explicitly tested the u-stem-style form and treated the result as a near-miss, not as the final row policy. That helps explain why the current TSV note mentions Gothic `þaurnus` and `*θurnuz` as background while still keeping the live input at `*θúrnaz` [Germanic/data/germanic-aligned-final.tsv:1245-1245; @Orel2003, p. 430].

## Superseded or diagnostic material

- The strongest surviving DEV_NOTES statement for this lexeme is also the stalest one: the line naming `thorn` among paradigm-form fixes reflects older workflow, not the current row state [DEV_NOTES:line-90-90].
- The diagnostic `*θurnuz -> þōrn` trace should not be promoted into live row policy. It shows a comparative/u-stem probe that landed near the target, but the current row does **not** use `*θurnuz` as its `PROTOFORM` [DEV_NOTES:line-2621-2621; Germanic/data/germanic-aligned-final.tsv:1245-1245].
- No dedicated thorn dossier, analysis file, or row-local DEV_NOTES section was located beyond those brief historical/diagnostic mentions. The usable support for later reporting is therefore mostly the live TSV row plus comparative dictionary evidence, not a substantial thorn-specific DEV_NOTES argument [Germanic/docs/lexeme_reports/packets/2251-thorn-þorn.md:49-55,79-83; Germanic/docs/lexeme_reports/research_memos/2251-thorn-þorn.md:15-20,54-63].
- Because the surviving DEV_NOTES material is thin/shared/stale, the safest later reporting posture is conservative: keep the row as regular and document the comparative alternatives only as background, unless fresh lexeme-specific evidence turns up.

## Open questions for later work

- If a later final report wants a fuller source paragraph, verify whether the project should cite Kroonen alone for the comparative headword or explicitly pair Kroonen's `*þurna-` with Orel's `*þurnuz ~ *þurnaz` every time the Gothic u-stem background is mentioned [@Kroonen2013, pp. 552-553; @Orel2003, p. 430].
- If the project later reopens old paradigm-form repairs, determine what exact earlier thorn preform lay behind the DEV_NOTES claim at line 90; the surviving note names the strategy but does not preserve the full row-local derivation.
- If future index work wants this row represented, decide whether the two surviving DEV_NOTES fragments are enough to justify indexing, or whether row 2251 should remain unindexed until a more substantive thorn-specific note or report exists.
