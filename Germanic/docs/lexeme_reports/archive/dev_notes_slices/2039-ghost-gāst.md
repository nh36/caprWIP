---
row_id: 2039
concept: ghost
counterpart: gāst
proto: *gáistaz
protoform: *gáistaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2039 ghost / gāst

## Current row state

- CONCEPT: `ghost` [Germanic/data/germanic-aligned-final.tsv:422-422]
- COUNTERPART: `gāst` [Germanic/data/germanic-aligned-final.tsv:422-422]
- PROTO: `*gáistaz` [Germanic/data/germanic-aligned-final.tsv:422-422]
- PROTOFORM: `*gáistaz` [Germanic/data/germanic-aligned-final.tsv:422-422]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:422-422]
- The aligned TSV currently gives no row-local explanatory prose beyond inherited source markers, so the live row itself does not preserve a lexeme-specific exception note or repair memo [Germanic/data/germanic-aligned-final.tsv:422-422].
- `old_english_wiktionary.tsv` independently maps English `ghost` to OE `gāst`, which at least confirms that the row target is the ordinary inherited OE lexeme rather than an ad hoc normalization invented only for the aligned TSV [Germanic/data/old_english_wiktionary.tsv:103-103].
- `oe_known_problems.tsv` has no entry for `*gáistaz`, `gāst`, or `ghost`, so the row is not currently being managed as a live OE exception, unresolved mismatch, or accepted wontfix case [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage audit still lists row `2039 | ghost | gāst | regular | no | - | - | - | none`, i.e. no packet, research memo, dossier, or prior report stem currently stands behind the row; this slice therefore has to function as the replacement working note by itself [Germanic/docs/lexeme_reports/coverage_audit.md:255-255].
- The current published derivation trace is fully successful and very short: `PROTO: *gáistaz`, `EXPECTED: gāst`, `OUTPUTS: gāst`, with the intermediate path `PWGmc Ai Monophthongization: *gāstaz`, then `PGmc Final Z Deletion: *gāsta`, then `PWGmc Final Bare A Loss: *gāst`, before surface `Outcome: gāst` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1704-1723].

## Development-note summary

No dedicated `ghost / gāst / *gáistaz` dossier currently survives in `DEV_NOTES.md`. For row `2039`, the replacement note therefore has to be built from shared rule-history material plus the current successful derivation trace, and that limitation should be stated plainly rather than hidden. The support here is real, but it is mostly shared infrastructure support, not a row-specific philological memo [Germanic/docs/lexeme_reports/coverage_audit.md:255-255; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1704-1723].

The live row itself is uncomplicated. `PROTO` and `PROTOFORM` are both `*gáistaz`, so this row currently preserves no internal split between comparative-form notation and OE-facing input notation; the row simply asks whether the regular pathway from that protoform reaches OE `gāst`, and the published trace says that it does [Germanic/data/germanic-aligned-final.tsv:422-422; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1704-1723].

What DEV_NOTES still contributes is a shared chronology that matches that trace closely. One later shared note insists that stressed vs. unstressed `*ai` must be treated as “TWO SEPARATE CHANGES,” and it summarizes the stressed development as “**PWGmc `*ai → *ā` (stressed): Traditional West Germanic monophthongization**” [Germanic/docs/DEV_NOTES.md:13945-13953]. Another infrastructure note lists as “Critical PWGmc developments” the “**Loss of final `*-z` after unstressed vowels**” and the subsequent “**Loss of word-final `*-a` and `*-ą`**” [Germanic/docs/DEV_NOTES.md:1529-1533]. Those shared notes are not about row `2039` in particular, but together they fit the published row trace exactly: `*gáistaz > *gāstaz > *gāsta > gāst` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1713-1723].

Because no row-specific DEV_NOTES prose survives, later writers should keep the tone conservative. The present documentation basis supports saying that row `2039` is currently a regular, successfully deriving control row whose outcome depends on ordinary stressed `*ai` monophthongization plus ordinary final-segment loss. It does **not** support claiming that DEV_NOTES ever preserved a separate ghost-specific controversy, exception analysis, or literature dossier that has since been lost.

## Relevant DEV_NOTES fragments

### DEV_NOTES:no-row-specific-ghost-dossier

- Source heading: no dedicated `ghost / gāst` section survives in `DEV_NOTES.md`
- Source line or section hint: direct row/lexeme search for `2039`, `ghost`, `gāst`, and `*gáistaz` yields no row-local analytical block
- Fragment type: `negative_result_with_current_implication`
- Status: `current`
- Issue tags: `missing_row_specific_authority`; `shared_rule_support_only`; `no_exception_dossier`
- Recommended next use: `preserve_as_no_index_context`
- Shared with row IDs:

The negative result is itself the first fact worth preserving. Unlike rows that carry a mismatch write-up, an exception memo, or a source dossier, row `2039` currently has no lexeme-specific block in `DEV_NOTES.md` that can simply be copied forward into a slice. That absence matters because coverage audit also still shows the row as uncovered and unsupported by any packet or memo, so later readers should not imagine that a hidden `ghost` research packet already exists somewhere else in the repository [Germanic/docs/lexeme_reports/coverage_audit.md:255-255].

Practically, this means the present slice has to lean on the shared sound-change notes that remain valid for many rows and on the current debug snapshot that shows the row working. That is enough for a careful replacement working note, but it is thinner than the evidence base available for genuinely disputed or previously broken rows [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1704-1723].

### DEV_NOTES:line-13945-13953

- Source heading: `Revised analysis: Two separate changes for *ai (2026-04-06)`
- Source line or section hint: `lines 13945-13953`
- Fragment type: `copied_shared_sound_change`
- Status: `current`
- Issue tags: `stressed_ai_monophthongization`; `shared_rule_support`; `chronology`
- Recommended next use: `cite_if_proto_vowel_chain_needs_justification`
- Shared with row IDs:

This is the most directly reusable DEV_NOTES fragment for the first step in the row's derivation. DEV_NOTES says that stressed and unstressed `*ai` should be treated as “**TWO SEPARATE CHANGES at different chronological stages**,” then states the relevant one for this row explicitly: “**PWGmc `*ai → *ā` (stressed): Traditional West Germanic monophthongization. Already in place in PWGmc for stressed syllables. Example: PGmc `*hailaz` → PWGmc `*hālaz` → OE `hāl`**” [Germanic/docs/DEV_NOTES.md:13945-13953].

For row `2039`, the value of this fragment is narrow but important. `*gáistaz` has stressed root `*ai`, so the fragment supplies shared project authority for the trace step `*gáistaz > *gāstaz` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1713-1717]. It should still be used cautiously: the fragment supports the general sound change, not a ghost-specific philological argument, and it does not by itself prove anything about attestation beyond the ordinary row target `gāst`.

### DEV_NOTES:line-1529-1533

- Source heading: `Proto-West Germanic Stage Implementation (2026-02-07) - EARLIER`
- Source line or section hint: `lines 1529-1533`
- Fragment type: `shared_chronology_note`
- Status: `diagnostic_only`
- Issue tags: `final_z_loss`; `final_a_loss`; `shared_stage_history`
- Recommended next use: `cite_with_trace_when_explaining_surface_shape`
- Shared with row IDs:

This older shared infrastructure fragment is still useful because it states the exact general chronology needed for the row's final two steps. DEV_NOTES lists among the “**Critical PWGmc developments (R/T §3.1.2)**”: “**Loss of final `*-z` after unstressed vowels (first change)**” and “**Loss of word-final `*-a` and `*-ą` (immediately after)**” [Germanic/docs/DEV_NOTES.md:1529-1533].

The passage is not a `ghost` note and should not be promoted into one. But it matches the current row trace closely enough to remain worth preserving here: after stressed `*ai > *ā`, the published snapshot shows exactly `*gāstaz > *gāsta > gāst` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1713-1723]. In other words, the fragment is best treated as shared stage-history support that happens to explain this row cleanly, not as evidence of any lost row-local debate.

### DEV_NOTES:line-11897-11905

- Source heading: `The FST needs a rule for loss of *w before unstressed *i`
- Source line or section hint: `lines 11897-11905`
- Fragment type: `diagnostic_shared_assumption`
- Status: `diagnostic_only`
- Issue tags: `ai_as_precondition`; `shared_pipeline_assumption`; `chronology`
- Recommended next use: `use_only_if_pipeline_order_needs_clarification`
- Shared with row IDs:

This fragment is only tangentially related, but it preserves a useful shared assumption about chronology. In the middle of a different lexeme problem, DEV_NOTES says the needed `*w`-loss rule should “**Apply after `*ai` monophthongization to `*ā`**” and places that prerequisite before later OE operations [Germanic/docs/DEV_NOTES.md:11897-11905]. That is not evidence about `ghost` as a lexeme, yet it confirms that elsewhere in the project the `*ai > *ā` development is already treated as an earlier settled stage rather than as a row-specific repair.

For row `2039`, this fragment is best kept as background only. It helps explain why the current trace can move straight from `*gáistaz` to `*gāstaz` before any later OE work is discussed, but it should never be cited as if it were a direct discussion of `gāst` itself [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1713-1717].

## Superseded or diagnostic material

- There is no row-specific superseded `ghost / gāst` diagnosis in surviving DEV_NOTES material. The superseded-vs-current contrast here is therefore not “old ghost theory versus new ghost theory,” but rather “shared historical pipeline notes” versus the current successful published trace [Germanic/docs/DEV_NOTES.md:1529-1533; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1704-1723].
- The `Proto-West Germanic Stage Implementation ... - EARLIER` section is useful only as shared chronology. It should not be overread as a row-level dossier, and any later report should pair it with the actual row trace rather than cite it alone [Germanic/docs/DEV_NOTES.md:1525-1544; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1713-1723].
- Because coverage audit still lists row `2039` as having no packet, memo, dossier, or report stem, this slice should be treated as a replacement working note assembled from thin but serviceable evidence, not as a compressed abstract of a fuller pre-existing lexeme file [Germanic/docs/lexeme_reports/coverage_audit.md:255-255].

## Open questions for later work

- If row `2039` later receives a full lexeme report, add direct lexicographic or etymological citations for the OE lexeme family itself (`gāst`, cognate `Geist`, reconstructed `*gáistaz`). The present slice can justify the internal project derivation, but its DEV_NOTES basis is mostly shared sound-change policy rather than a lexeme-specific literature dossier.
- If `dev_notes_slices/index.tsv` is updated later, treat this slice cautiously. The safest anchors are the shared stressed-`*ai` note at [Germanic/docs/DEV_NOTES.md:13945-13953] and the shared final-loss chronology at [Germanic/docs/DEV_NOTES.md:1529-1533], but the row may reasonably remain a thin-support slice because no row-local DEV_NOTES block currently survives.
- If future pipeline changes ever disturb this row, the first recheck should be the simple traced chain already published now: `*gáistaz > *gāstaz > *gāsta > gāst` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1713-1723].
