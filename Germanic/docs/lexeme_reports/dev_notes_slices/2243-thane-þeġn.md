---
row_id: 2243
concept: thane
counterpart: þeġn
proto: *θégnaz
protoform: *θégnaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2243 thane / þeġn

## Current row state

- CONCEPT: `thane`
- COUNTERPART: `þeġn`
- PROTO: `*θégnaz`
- PROTOFORM: `*θégnaz`
- DERIVATION_CLASS: `regular`
- Live TSV history: `Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh) | TSV fix: target þæġn → þeġn (R/T reconstruct *θegnaz with *e and give OE þegn, matching pipeline output).` [Germanic/data/germanic-aligned-final.tsv:1213-1213]
- The live row keeps `PROTO` and `PROTOFORM` identical. In other words, the project is not currently distinguishing a broader comparative headword from a separate OE-directed surrogate form for this row: the current comparative/project input is `*θégnaz`, and the OE target to be explained is `þeġn` [Germanic/data/germanic-aligned-final.tsv:1213-1213].
- The row's present policy is therefore narrow and explicit: keep the e-grade proto and the OE target `þeġn`, not the previously stored target `þæġn` [Germanic/data/germanic-aligned-final.tsv:1213-1213; @RingeTaylor2014, p. 322].
- Clark Hall's dictionary entry supports the current OE lexeme directly: `Þegn ... m. servant, minister, retainer, vassal, follower, disciple ... ['thane']` [@ClarkHall1960, s.v. "þegn"; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:42344-42350].
- No existing packet or research memo stem was found for row 2243 in the current lexeme-report infrastructure, so the slice uses the canonical row-based filename `2243-thane-þeġn.md` [Germanic/docs/lexeme_reports/research_memo_index.tsv:100-112].

## Detailed development-note summary

The surviving DEV_NOTES material for row 2243 is thin but still useful as a replacement working note, because it preserves the exact reason the OE target was corrected. The controlling statement is concise: `R/T reconstruct *þegnaz with *e and give OE þegn. The TSV target þæġn was incorrect; changed to þeġn to match both R/T and our pipeline output.` [DEV_NOTES:line-3100-3100]. That sentence should remain central, since it states the comparative authority, the rejected target, and the adopted target in one place.

For this row, the main analytical task is not to solve a large OE phonological puzzle but to keep the row fields distinct and prevent reintroduction of a superseded spelling. `PROTO` and `PROTOFORM` are both currently `*θégnaz`; `COUNTERPART` is `þeġn` [Germanic/data/germanic-aligned-final.tsv:1213-1213]. The DEV_NOTES correction and the TSV history both agree that the older target `þæġn` should be treated as abandoned project history rather than as a live rival form. The comparative support cited in-project is Ringe–Taylor's e-grade reconstruction and OE outcome `þegn` [Germanic/data/germanic-aligned-final.tsv:1213-1213; Germanic/docs/DEV_NOTES.md:3100-3100; @RingeTaylor2014, p. 322].

The row's place inside the broader March 2026 note cluster also matters. DEV_NOTES grouped `thane` with several apparent `*gw` cleanup cases and recorded the mismatch snapshot `*θegnăz → þeġn (expected þæġn): vowel_quality__ae_e_alternation` [DEV_NOTES:line-3090-3090]. For row 2243, however, that shared context is mainly bookkeeping history, not a substantive sound-change analysis parallel to `snow`, `swallow`, or `sing`. The thane note does not argue for a new OE rule; it records that the target in the TSV was wrong and needed to be aligned with comparative source authority and the already-obtained pipeline output [Germanic/docs/DEV_NOTES.md:3090-3100].

That is why the distinction between source notations matters here. The live row's `PROTO`/`PROTOFORM` is the project notation `*θégnaz`; DEV_NOTES phrases the same etymon once as `*θegnăz` in the mismatch list and once as `*þegnaz` in prose; the OE `COUNTERPART` is `þeġn` [Germanic/data/germanic-aligned-final.tsv:1213-1213; Germanic/docs/DEV_NOTES.md:3090-3100]. Those graphic differences should not be mistaken for competing lexical analyses. What matters for current row policy is the e-grade vocalism and the corrected OE target, not the incidental normalization differences between `θ` and `þ` or between acute and breve notation.

The implementation line is short but worth carrying over because it confirms that the correction was actually applied: `TSV changes: snow, swallow protos corrected; thane target corrected` [DEV_NOTES:line-3117-3117]. For row 2243 the full project chronology is therefore straightforward: an older TSV target `þæġn` created a mismatch against expected/project output, DEV_NOTES recorded Ringe–Taylor's support for `þegn`, and the row was repaired by changing the OE target to `þeġn` while leaving the row regular [Germanic/docs/DEV_NOTES.md:3090-3117; Germanic/data/germanic-aligned-final.tsv:1213-1213].

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-3090-3090

- Source heading: `The problem`
- Source line or section hint: `line 3090`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `old_mismatch_snapshot`; `old_target`; `ae_vs_e`; `project_history`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This line preserves the superseded mismatch state: `*θegnăz → þeġn (expected þæġn): vowel_quality__ae_e_alternation` [Germanic/docs/DEV_NOTES.md:3090-3090]. It is useful because it shows exactly what was wrong in the stored row state. It should not be cited as evidence that `þæġn` remains a plausible current target; it is only diagnostic history.

### DEV_NOTES:line-3100-3100

- Source heading: `Research`
- Source line or section hint: `line 3100`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `target_correction`; `comparative_support`; `e_grade`; `regular_row`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling row-specific fragment and should be preserved almost verbatim: `R/T reconstruct *þegnaz with *e and give OE þegn. The TSV target þæġn was incorrect; changed to þeġn to match both R/T and our pipeline output.` [Germanic/docs/DEV_NOTES.md:3100-3100]. It gives the source support, the rejected OE target, and the accepted correction without needing additional reconstruction.

### DEV_NOTES:line-3117-3117

- Source heading: `Implementation`
- Source line or section hint: `line 3117`
- Fragment type: `verification`
- Status: `current`
- Issue tags: `tsv_fix_applied`; `target_updated`; `project_chronology`
- Recommended next use: `cite_if_row_history_needed`
- Shared with row IDs: `2199`; `2234`

This implementation note is terse but materially relevant: `TSV changes: snow, swallow protos corrected; thane target corrected` [Germanic/docs/DEV_NOTES.md:3117-3117]. For row 2243 its value is strictly chronological: it confirms that the target correction recorded at line 3100 was actually pushed into live data.

## Superseded or diagnostic material

- The only clearly superseded lexical policy is the older OE target `þæġn`. The live row, the DEV_NOTES correction, and the quoted comparative support all now point to `þeġn` instead [Germanic/data/germanic-aligned-final.tsv:1213-1213; Germanic/docs/DEV_NOTES.md:3100-3100; @RingeTaylor2014, p. 322].
- The mismatch label `vowel_quality__ae_e_alternation` is useful as a record of what the system once flagged, but it does not by itself establish an open phonological problem. In the present project state it mainly records that the stored OE target had the wrong vowel [Germanic/docs/DEV_NOTES.md:3090-3090].
- The broader March 2026 `*gw` discussion is only indirectly relevant here. Unlike `snow`, `swallow`, and `sing`, row 2243 does not survive in DEV_NOTES as a case requiring a new rule or a corrected protoform; its surviving note value is simply the correction from `þæġn` to `þeġn` [Germanic/docs/DEV_NOTES.md:3086-3117].

## Open questions for later work

- If a later indexing pass decides to add this row, the only strong standalone fragment is `DEV_NOTES:line-3100-3100`; lines 3090 and 3117 are useful mainly as support and chronology.
- A fuller lexeme report could cite the dictionary entry for `þegn` more explicitly alongside Ringe–Taylor so that the OE target has independent lexical support, not only project-internal correction history [@ClarkHall1960, s.v. "þegn"].
- No current evidence suggests changing `PROTO`, `PROTOFORM`, `COUNTERPART`, or `DERIVATION_CLASS`. Later work here is more likely to be indexing cleanup or source-enrichment than lexical reanalysis.
