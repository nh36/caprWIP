---
row_id: 2036
concept: furrow
counterpart: furh
proto: "*fúrx"
protoform: "*fúrx"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: ""
linked_research_memo_file: ""
linked_dossier_or_analysis_files: ""
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2036 furrow / furh

## Current row state

- Live OE row 2036 is `furrow / furh`, with both `PROTO` and `PROTOFORM` set to `*fúrx` and `DERIVATION_CLASS` set to `regular`; the row currently carries no inline TSV note and no linked packet or research memo [Germanic/data/germanic-aligned-final.tsv:409-411; Germanic/docs/lexeme_reports/coverage_audit.md:248-255; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- `oe_known_problems.tsv` does not list `*fúrx`, which is consistent with the current repo state: this row is not being tracked as an exception, chronology regression, or unresolved mismatch bucket [Germanic/data/oe_known_problems.tsv:1-8].
- The publish trace and full trace both show a clean match: `PROTO: *fúrx`, `EXPECTED: furh`, `OUTPUTS: furh`. In the long trace essentially every historical rule is `[no-change]`; the only visible late difference is orthographic/surface rendering as `*fúrh`/`furh`, not any special repair or analogical detour [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1663-1683; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:11139-11253].
- The minimal external lexical support presently visible in-repo is the OE Wiktionary import line `furrow\tfurh\tinh\ttemplate:inh\tfurrow`, which at least agrees with the row's basic inheritance framing even though it is not a full philological dossier [Germanic/data/old_english_wiktionary.tsv:100-100].

## Development-note summary

No row-specific DEV_NOTES section for `furh` survives in the current repository snapshot. The only direct DEV_NOTES mention of this lexeme is shared background material from the `NWGmc u-lowering Exceptions Near Labials` discussion, where `furh` appears as one of the small set of archaic root nouns used to contrast with thematic nouns such as `wulf` and `fugol` [Germanic/docs/DEV_NOTES.md:108-114]. That is useful background, but it is not a dedicated furrow note and should not be overstated.

What that shared material does preserve is still relevant. DEV_NOTES reports Ringe–Taylor's observation that "nearly all a-stems exhibit lowering but no root-nouns do," then immediately warns that root nouns are a restricted archaic class and names `furh` among them: "Root nouns are a small, archaic class (burg, brust, furh, hnut-)" [Germanic/docs/DEV_NOTES.md:108-114]. For row 2036, the conservative takeaway is simply that the current project treats `furh` as an ordinary inherited root-noun type, not as part of the problematic `u`-retention exception cluster that required special handling elsewhere.

The live debug traces support that conservative reading. Unlike the exception rows that motivated the surrounding DEV_NOTES discussion, `*fúrx` reaches `furh` without any active mismatch, special bucket annotation, or paradigm-cell workaround: the transducer reports the expected OE form directly, and the detailed trace shows no phonological rule firing on this item beyond orthographic realization at the end of the pipeline [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1663-1683; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:11139-11253]. In other words, the replacement slice can preserve the shared root-noun remark, but the present row state is chiefly defined by the absence of row-specific trouble.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-108-114

- Source label: `DEV_NOTES:line-108-114`
- Source heading: `NWGmc u-lowering Exceptions Near Labials`
- Source line or section hint: `Approach C: Use the root-noun analysis (for words that could have been root nouns)`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `background_current`
- Issue tags: `root_noun`; `u_lowering_contrast`; `shared_material`; `methodology`
- Recommended next use: `cite_with_caution_as_shared_background`
- Shared with row IDs: `2030, 2162, 2298, 2300 (contrastive context rather than row-specific support)`

This is the one DEV_NOTES fragment that still mentions `furh` directly. Its immediate purpose is not to analyze row 2036, but to reject a bad repair strategy for the `wulf`/`fugol` type. DEV_NOTES first summarizes the handbook claim that "nearly all a-stems exhibit lowering but no root-nouns do," i.e. root nouns are not expected to pattern like the thematic nouns that regularly undergo NWGmc `u`-lowering [Germanic/docs/DEV_NOTES.md:108-109]. It then states why that line of rescue cannot simply be extended to the problematic lexemes: Kroonen reconstructs the relevant exception words as thematic stems, Gothic supports thematic inflection, and "Root nouns are a small, archaic class (burg, brust, furh, hnut-)" [Germanic/docs/DEV_NOTES.md:111-114].

For row 2036, the value of the fragment is indirect but real. It preserves repo-local acknowledgement that `furh` belongs, at least in this methodological contrast, to the archaic root-noun set rather than to the thematic nouns whose vowel behavior needed special apologetics. That does not by itself settle every philological detail of the lexeme, and it is not a substitute for a dedicated furrow dossier; but it does explain why no row-specific emergency note was needed here when neighboring `u`-items produced long DEV_NOTES discussions [Germanic/docs/DEV_NOTES.md:63-114].

## Superseded or diagnostic material

- A stale but potentially confusing diagnostic survives in `germanic_transducer_report.md`, where a 2026-01-27 dataset sweep for supposed liquid-lowering lists `*furxō → furh` among many proto forms in `*-ō` [Germanic/docs/germanic_transducer_report.md:19-31]. That passage belongs to a deleted rule investigation, not to current row-2036 lexeme policy, and it does **not** match the live row metadata, which now uses bare `*fúrx` for both `PROTO` and `PROTOFORM` [Germanic/data/germanic-aligned-final.tsv:409-411]. It should therefore be treated as superseded diagnostic residue, not as authority for revising this slice.
- The detailed OE trace is diagnostic rather than literary evidence, but for this row it is still worth preserving because it shows the opposite of a problem: `*fúrx` already lands on `furh` without a repair rule, exception bucket, or analogical retargeting [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:11139-11253]. If a later writer wants to explain current project behavior, that trace is the clearest technical witness.
- Because no packet, memo, or dedicated analysis file exists for row 2036 in the current manifest-bearing lexeme-report material, later researchers should resist importing argumentation from unrelated rows unless they are explicitly using it as shared background. At present, the safest statement is that row-specific DEV_NOTES substance mostly does **not** survive, and the row remains regular in the live pipeline [Germanic/docs/lexeme_reports/report_manifest.tsv:1-13; Germanic/docs/lexeme_reports/coverage_audit.md:248-255].

## Open questions for later work

- If this row ever needs a full lexeme report, verify whether the bare project input `*fúrx` should remain the reporting form or be accompanied by a fuller stem-class citation; this slice does not justify changing the TSV.
- If future documentation wants a literature-facing explanation of final `-h` here, add it from a dedicated sound-law note rather than inferring too much from the trace alone.
- If a later audit revisits root nouns systematically, check whether `furh` should be given a dedicated shared background note parallel to the existing exception-cluster slices, while keeping clear that row 2036 is currently regular, not a mismatch case.
