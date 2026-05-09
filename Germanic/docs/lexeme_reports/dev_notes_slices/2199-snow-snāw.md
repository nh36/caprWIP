---
row_id: 2199
concept: snow
counterpart: snāw
proto: *snáiwaz
protoform: *snáiwaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2199 snow / snāw

## Current row state

- CONCEPT: `snow`
- COUNTERPART: `snāw`
- PROTO: `*snáiwaz`
- PROTOFORM: `*snáiwaz`
- DERIVATION_CLASS: `regular`
- Live TSV note: `TSV fix: proto *snaigwăz → *snaiwăz (Kroonen *snaiwa-, R/T *snaiwaz; no labiovelar in this etymology).` [Germanic/data/germanic-aligned-final.tsv:1043-1043]
- The live row currently keeps `PROTO` and `PROTOFORM` identical, so there is no active project split between a comparative headword and a separate row-specific derivational surrogate. The comparative source forms cited in the TSV note — Kroonen's `*snaiwa-` and Ringe–Taylor's `*snaiwaz` — function as supporting source notations, while the row's present FST input is `*snáiwaz` and the OE target is `snāw` [Germanic/data/germanic-aligned-final.tsv:1043-1043; @Kroonen2013, p. 460; @RingeTaylor2014, p. 171].
- OE lexical identification is straightforward: Clark Hall lists `snāw m. 'snow'`, which aligns with the row's current `COUNTERPART` and gives no reason to suspect a rival target form [@ClarkHall1960, s.v. "snāw"].

## Detailed development-note summary

The surviving DEV_NOTES support for row 2199 is narrow but clear. Its main value is not a bespoke OE sound-law analysis for `snāw`; it is the record of a proto-entry correction. The controlling row-specific note says: `"Both Kroonen (p.460, *snaiwa-) and R/T (p.171, *snaiwaz) reconstruct PGmc with *w, not *gw. There was never a labiovelar in this word. The TSV proto was simply wrong, likely from automated extraction confusion."` [Germanic/docs/DEV_NOTES.md:3094-3094]. That sentence should be preserved almost verbatim because it states both the comparative support and the project decision with minimal ambiguity.

For this row, the crucial distinction is between the superseded bad TSV proto and the current row policy. The abandoned form was `*snaigwăz`, which produced the old mismatch snapshot `*snaigwăz → snāgw (expected snāw)` [Germanic/docs/DEV_NOTES.md:3087-3087]. The live row no longer uses that form. Its current fields are `PROTO = PROTOFORM = *snáiwaz`, and its OE `COUNTERPART` remains `snāw` [Germanic/data/germanic-aligned-final.tsv:1043-1043]. `*snaiwa-` and `*snaiwaz` are comparative corroborants; `*snáiwaz` is the row's present project input; `snāw` is the OE output to be explained. Nothing in the surviving material suggests a need to split `PROTO` from `PROTOFORM`, retarget the OE form, or treat the lexeme as anything other than regular [@Kroonen2013, p. 460; @RingeTaylor2014, p. 171].

The shared `*gw` discussion in DEV_NOTES matters only as contrastive background. The note explains that Ringe–Taylor §6.4.2 treats `"Loss of *w after non-initial velars"` and distinguishes the outcomes of genuine `*ngw`, `*Vgw`, and `*lgw` clusters, but it then states: `"For cases 2-3, we corrected the TSV proto-forms to remove the spurious *g. For case 1, we added the OEPostVelarWLoss rule."` [Germanic/docs/DEV_NOTES.md:3104-3111; @RingeTaylor2014, §6.4.2]. Row 2199 belongs to the corrected-data side of that contrast, not to the genuine-labiovelar side represented by `sing`. In other words, `snāw` is not an OE outcome derived by deleting `g` from an inherited `*Vgw` cluster; the row is regular precisely because the inherited etymon already lacked that `g`.

The implementation note confirms that this was a data correction rather than a new row-specific OE rule. DEV_NOTES records `"TSV changes: snow, swallow protos corrected; thane target corrected"` [Germanic/docs/DEV_NOTES.md:3117-3117]. For row 2199, that is the operative project chronology: a wrong protoform briefly entered the TSV, comparative dictionaries showed that `snow` never had the relevant labiovelar, and the row was repaired by correcting the proto entry while leaving the OE target `snāw` intact. The result is a row whose remaining note value is mostly provenance and diagnostic history, not ongoing lexical uncertainty.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-3087-3087

- Source heading: `The problem`
- Source line or section hint: `line 3087`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `old_mismatch_snapshot`; `bad_proto_entry`; `spurious_labiovelar`; `project_history`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This one-line mismatch snapshot preserves the abandoned state that later writers would otherwise have to reconstruct from repository history: `*snaigwăz → snāgw (expected snāw): cons_mismatch__g_vs_w` [Germanic/docs/DEV_NOTES.md:3087-3087]. It should be retained only as diagnostic chronology. The line does **not** show that `snāgw` was ever a serious OE target; it shows that the row once carried a spurious `g` in the proto entry.

### DEV_NOTES:line-3094-3094

- Source heading: `Research`
- Source line or section hint: `line 3094`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `protoform_correction`; `comparative_support`; `no_labiovelar`; `regular_row`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling row-specific fragment and should be preserved nearly verbatim: `"Both Kroonen (p.460, *snaiwa-) and R/T (p.171, *snaiwaz) reconstruct PGmc with *w, not *gw. There was never a labiovelar in this word. The TSV proto was simply wrong, likely from automated extraction confusion."` [Germanic/docs/DEV_NOTES.md:3094-3094]. It identifies both the source support and the exact project decision: the correction is to the proto entry, not to the OE target.

### DEV_NOTES:line-3104-3111

- Source heading: `Analysis of *gw developments`
- Source line or section hint: `lines 3104-3111`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `shared_sound_change_context`; `contrast_with_genuine_gw_cases`; `spurious_g_removed`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs: `2190`; `2234`

This shared fragment is useful because it prevents later work from treating `snow`, `swallow`, and `sing` as the same kind of case. DEV_NOTES says Ringe–Taylor §6.4.2 covers `"Loss of *w after non-initial velars"` and then concludes: `"For cases 2-3, we corrected the TSV proto-forms to remove the spurious *g. For case 1, we added the OEPostVelarWLoss rule."` [Germanic/docs/DEV_NOTES.md:3104-3111]. Row 2199 belongs to the former group: its resolution is removal of a false `g`, not addition of a new OE-side repair rule.

### DEV_NOTES:line-3117-3117

- Source heading: `Implementation`
- Source line or section hint: `line 3117`
- Fragment type: `verification`
- Status: `current`
- Issue tags: `tsv_fix_applied`; `row_local_verification`; `project_chronology`
- Recommended next use: `cite_if_row_history_needed`
- Shared with row IDs: `2234`

This implementation line is terse but directly relevant: `"TSV changes: snow, swallow protos corrected; thane target corrected"` [Germanic/docs/DEV_NOTES.md:3117-3117]. It confirms that the project treated `snow` as a corrected-data case and that the correction was actually applied, rather than merely proposed.

## Superseded or diagnostic material

The only genuinely superseded material is the bad proto spelling `*snaigwăz` and the mismatch it produced. That form should not drift back into later report prose as though it were a legitimate comparator. The row's own TSV note already neutralizes it by stating the correction `*snaigwăz → *snaiwăz`, and the live row fields go further by normalizing the active project input as `*snáiwaz` [Germanic/data/germanic-aligned-final.tsv:1043-1043]. The useful history is therefore narrow: a wrong `g` entered the TSV, comparative dictionaries showed that `snow` never had that labiovelar, and the row was repaired by correcting the protoform rather than by revising the OE target.

The shared `*gw` discussion remains diagnostically useful, but it should not be over-read. It explains why the old output `snāgw` might have looked like a genuine `*Vgw` problem, yet the final DEV_NOTES decision is explicit that this is the wrong etymology for `snow` [Germanic/docs/DEV_NOTES.md:3094-3111]. Any later report should keep that contrast clear so that row 2199 is not accidentally grouped with genuinely inherited labiovelar items.

## Open questions for later work

- If `index.tsv` is updated later, the strongest standalone fragment to index is `DEV_NOTES:line-3094-3094`; the broader `DEV_NOTES:line-3104-3111` passage is useful background but mostly shared sound-change context.
- If a fuller lexeme report is ever written, it may be worth citing an explicit OE dictionary witness such as `snāw m. 'snow'` alongside the existing TSV fix note so that the target form is sourced independently of project-internal correction history [@ClarkHall1960, s.v. "snāw"].
- No current evidence suggests a `PROTO`/`PROTOFORM` split, a `COUNTERPART` change, or a derivation-class change. Any later work here is more likely to be bibliographic or indexing cleanup than lexical reanalysis.
