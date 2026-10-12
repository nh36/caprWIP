---
row_id: 2221
concept: stool
counterpart: stōl
proto: *stōlaz
protoform: *stōlaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2221 stool / stōl

## Current row state

- The live TSV row reads `CONCEPT = stool`, `COUNTERPART = stōl`, `PROTO = *stōlaz`, `PROTOFORM = *stōlaz`, `DERIVATION_CLASS = regular`, with no row note and only duplicated generic source provenance strings from Wiktionary [Germanic/data/germanic-aligned-final.tsv:1130-1130].
- `PROTO` and `PROTOFORM` currently coincide, so there is no live row-level split between cognate-set headword and OE-facing input. That needs to stay distinct from handbook stem citation practice, however: the comparative literature often cites the same noun as stem-form `*stōla-`, while the live row stores nominative-style `*stōlaz` [Germanic/data/germanic-aligned-final.tsv:1130-1130; @Kroonen2013, p. 481; @Orel2003, p. 379].
- The current published derivation trace is completely regular and requires no rescue machinery: `Proto Input: *stōlaz`, then `PGmc Final Z Deletion: *stōla`, then `PWGmc Final Bare A Loss: *stōl`, with final outcome `stōl` exactly matching the row target [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4747-4765].
- `oe_known_problems.tsv` has no row-local exception entry for row `2221` or for `*stōlaz`, so the item is not currently being tracked as an OE problem case [Germanic/data/oe_known_problems.tsv:1-8].
- No packet or research memo stem currently exists for `stool / stōl`, so this slice uses the canonical row-based filename rather than reusing an existing report stem.

## Detailed development-note summary

Surviving DEV_NOTES support for row `2221` is extremely thin and indirect. A direct search for `stool`, `stōl`, `*stōlaz`, or `*stōla-` in `Germanic/docs/DEV_NOTES.md` does **not** produce a dedicated row-specific note about the OE lexeme. The only actual hit is a shared comparative-morphology remark inside a much later adjudication for another lexical family, where `*stōla-` is named among Bammesberger's `*-la-` nouns. That means the replacement working note has to be conservative: it can preserve one useful typological fragment from DEV_NOTES, but it should not pretend that the repo already contains a stool-specific controversy dossier.

The one usable DEV_NOTES claim is still worth keeping because it bears directly on how the comparative form should be understood. In the `nablan-` adjudication, DEV_NOTES says that Bammesberger's `*-la-` list `(*fugla-, *setla-, *tagla-, *þwahla-, *webla-, *mēla-, *stōla-) independently confirms the typology: bare *-l-*, no inherited medial vowel between root and *l*` [Germanic/docs/DEV_NOTES.md:32120-32125]. For row `2221`, that is not an OE-specific sound-change note; it is a comparative morphology note. Its practical force is simply that the live row's `*stōlaz` belongs to an ordinary Proto-Germanic `*-la-` noun family and does not need a special explanatory vowel between root and `l` [@Bammesberger1990, pp. 75-76].

That shared DEV_NOTES remark aligns cleanly with the handbook entries already present in the repo. Kroonen gives `*stōla- m. 'chair, seat'` with OE `stōl` among the reflexes [@Kroonen2013, p. 481; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:24751-24754]. Orel likewise gives `*stōlaz sb.m.` with `OE stól` and the same broad Germanic comparanda [@Orel2003, p. 379; docs/references/orel_handbook_germanic_etymology.vision.txt:42124-42128]. Clark Hall's OE lexicon is equally straightforward: `stōl I. m. 'stool,' chair, seat` [@ClarkHall1960, s.v. "stōl"; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:38343-38343]. Together these sources support the live row as an ordinary inherited noun rather than as a problematic or heavily editorially reconstructed item.

The main caution for later work is therefore not philological difficulty but scope discipline. The DEV_NOTES fragment uses stem-form `*stōla-`, while the live row stores `*stōlaz`; that is a notation difference between comparative stem citation and the row's nominative-style proto label, not evidence for two different reconstructions. Likewise, because the published derivation trace already yields `stōl` by routine final-segment loss, there is no basis in surviving DEV_NOTES to recast the row as exceptional or analogical [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4755-4765]. The honest replacement note for this row is therefore a thin one: ordinary lexical support is good, but row-local DEV_NOTES support remains shared and indirect.

## Relevant DEV_NOTES fragments

### DEV_NOTES:no-row-specific-hit-for-stool-stōl

- Source heading: no dedicated `stool / stōl` note survives in `DEV_NOTES.md`
- Source line or section hint: negative-result sweep; only attachable direct hit is at `lines 32120-32125`
- Fragment type: `unclear_needs_human_review`
- Status: `current_negative_result`
- Issue tags: `missing_row_specific_authority`; `shared_typology_only`; `do_not_overindex`
- Recommended next use: `keep_as_working_note_only`
- Shared with row IDs:

This negative result is the most important documentary fact for the row. `DEV_NOTES.md` does not currently preserve a stool-specific repair note, rule-ordering audit, or source dispute. Later writers should not infer one from the mere presence of a regular live row or from external dictionary entries. The slice is useful precisely because it records that the live row is stable **without** having a dedicated DEV_NOTES dossier behind it.

### DEV_NOTES:line-32120-32125

- Source heading: `Adjudication: which camp do the new sources favour?`
- Source line or section hint: `lines 32120-32125`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current_but_indirect`
- Issue tags: `comparative_morphology`; `*-la-_type`; `proto_vs_protoform`; `shared_fragment`
- Recommended next use: `cite_in_final_report_with_caution`
- Shared with row IDs:

This is the only directly attachable DEV_NOTES fragment for row `2221`, and it should be preserved in essentially its original force. DEV_NOTES says that Kroonen's general `*-l-an-/-l-a-*` template and Bammesberger's list `(*fugla-, *setla-, *tagla-, *þwahla-, *webla-, *mēla-, *stōla-)` together confirm the same typology: `bare *-l-*, no inherited medial vowel between root and *l*` [Germanic/docs/DEV_NOTES.md:32120-32125]. For `stōl`, this is useful as comparative classification, not as a special OE derivational patch. It supports reading the live row's `*stōlaz` as the ordinary nominative-style representation of the same `*stōla-` noun family cited in the dictionaries [@Kroonen2013, p. 481; @Bammesberger1990, pp. 75-76].

## Superseded or diagnostic material

- No row-specific superseded DEV_NOTES analysis currently survives for `stool / stōl`. The real diagnostic fact is simply that the row lacks a dedicated project-history note, not that it preserves a rejected competing derivation.
- The only notation issue worth fencing off is `*stōla-` versus `*stōlaz`. In this repo's current state, the former is comparative stem citation from dictionaries and from the shared DEV_NOTES typology remark, while the latter is the live row's `PROTO`/`PROTOFORM` spelling. They should not be misreported as distinct lexical proposals [Germanic/data/germanic-aligned-final.tsv:1130-1130; Germanic/docs/DEV_NOTES.md:32120-32125; @Kroonen2013, p. 481].
- The duplicated Wiktionary source strings in the live TSV row are provenance only. They do not replace a project-authored DEV_NOTES argument and should not be cited as if they were a lexeme report [Germanic/data/germanic-aligned-final.tsv:1130-1130].

## Open questions for later work

- If later indexing work wants to attach this row to `index.tsv`, decide first whether a single shared typology fragment is enough to justify indexing, or whether the row should wait for a small packet/memo that quotes the actual `*stōla- / stōl` dictionary evidence directly.
- If later report prose cites Bammesberger here, confirm whether page `76` contains a fuller discussion of `*stōla-` beyond the repo-local index/list evidence currently visible; the present slice can rely on DEV_NOTES plus Kroonen/Orel without needing that expansion [@Bammesberger1990, pp. 75-76].
- If future documentation distinguishes comparative lemma shape and FST input more aggressively, keep the wording explicit: `PROTO`/`PROTOFORM` are live-row `*stōlaz`, while shared literature and DEV_NOTES often cite the same noun as stem-form `*stōla-` [Germanic/data/germanic-aligned-final.tsv:1130-1130; @Kroonen2013, p. 481].
