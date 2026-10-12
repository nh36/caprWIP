---
row_id: 2023
concept: foal
counterpart: fola
proto: *fúlô
protoform: *fúlô
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/dossier-shoulder-paradigm-survey-2026.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2023 foal / fola

## Current row state

- CONCEPT: `foal`
- COUNTERPART: `fola`
- PROTO: `*fúlô`
- PROTOFORM: `*fúlô`
- DERIVATION_CLASS: `regular`
- Live TSV state: row 2023 is already a clean regular row with `COUNTERPART=fola`, `PROTO=*fúlô`, and no row note or exception flag; the adjacent English/German rows keep the same cognate set [Germanic/data/germanic-aligned-final.tsv:359-360].
- Current derivation trace state: the published OE trace now gives `OUTPUTS: fola`, explicitly showing `Proto Input: *fúlô`, NWGmc u-lowering `*fólô`, OE unstressed long-vowel shortening `*fóla`, and final `Outcome: fola` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1463-1482].
- Coverage / problem-list state: the coverage audit still marks row 2023 as uncovered (`no`, `none`), and `oe_known_problems.tsv` currently contains only unrelated items, with no `*fúlô` / `fola` entry [Germanic/docs/lexeme_reports/coverage_audit.md:245-245; Germanic/data/oe_known_problems.tsv:1-8].
- OE attestation baseline: the repo's OE lexical extract includes `foal	fola	inh	template:inh	foal`; this supports `fola` as an attested repository target, but only at that lexicographic / ingest level, not as a fresh manuscript review inside this slice [Germanic/data/old_english_wiktionary.tsv:88-88].
- Morphological encoding background: the shoulder paradigm survey lists `*fúlô` among the project's trimoric oral `*ō` / `ô` inputs used for weak masculine n-stem nominative singulars, so the row's input shape is not ad hoc even though row-specific DEV_NOTES material is thin [Germanic/docs/dossier-shoulder-paradigm-survey-2026.md:60-67].

## Development-note summary

No substantial row-specific DEV_NOTES dossier survives for row 2023. The only direct, unmistakable foal/fola note in `DEV_NOTES.md` is a short diagnostic bucket entry recording an older failure state `*fulô → fula (expected fola)` and classifying that failure as a **bug**, not as an accepted lexical exception [Germanic/docs/DEV_NOTES.md:2967-2973]. That fragment matters because it preserves the row's former problem very clearly, but it is no longer current row state: the live trace now gives regular `fola` from `*fúlô` without repair prose or exception handling [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1463-1482].

The best surviving shared DEV_NOTES material is therefore negative-control material. The long NWGmc u-lowering section establishes the general rule `*u → *o` before a following non-high vowel and then discusses a set of genuine lexical **u-retention** exceptions such as `wulf`, `fugol`, and `bucc` [Germanic/docs/DEV_NOTES.md:63-138]. But row 2023 must be kept out of that exception bucket. DEV_NOTES itself says so explicitly: "`buga/boga, fula/fola are different: the expected form IS the lowered one (boga, fola), so u-retention here is a FST bug, not a documented exception`" [Germanic/docs/DEV_NOTES.md:2973-2973]. In other words, the shared u-lowering discussion is relevant here chiefly because it prevents a false analogy with the accepted labial-exception lexemes.

The conservative replacement-note position for this row is therefore straightforward. `PROTO` and `PROTOFORM` are the same (`*fúlô`), the row target is attested `fola` at least in the repo's lexical source layer, and the current cascade already derives that target regularly by the expected lowering and later weak-tail shortening / surface adjustments [Germanic/data/germanic-aligned-final.tsv:360-360; Germanic/data/old_english_wiktionary.tsv:88-88; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1472-1482]. What survives from DEV_NOTES is mainly the memory of an old bug and the explicit warning not to confuse this row with the real u-preserving exception set.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2967-2973

- Source heading: `Remaining root-level issues (shared with other lexemes)` / `A. u-lowering (u → o before back vowel)`
- Source line or section hint: `lines 2967-2973`
- Fragment type: `lexeme_specific_diagnostic`
- Status: `superseded`
- Issue tags: `u_lowering`; `bug_history`; `not_an_exception`; `weak_masc_n_stem`
- Recommended next use: `use_to_explain_former_bug_not_current_analysis`
- Shared with row IDs: `not enumerated in the note; the same bucket also mentions *burô, *bugô, and *uxsô cases`

This is the only securely row-specific DEV_NOTES fragment that actually names the foal item. It preserves the earlier failure in exact form: "`Affected: *burô → bura (expected bora), also *bugô → buga (expected boga), *fulô → fula (expected fola), *uxsô → uxa (expected oxa)`" [Germanic/docs/DEV_NOTES.md:2969-2969]. The accompanying diagnosis is equally important: "`NWGmcULowering should lower *u → *o before non-high vowels in a following syllable. But these n-stem nominatives with {*ô} suffix retain u`" [Germanic/docs/DEV_NOTES.md:2971-2971]. That is the clearest surviving record of what was wrong with the row before the current regular trace existed.

The note must also be preserved because it draws the boundary that later writers could easily blur. DEV_NOTES adds: "`Some u-retentions are documented exceptions (bucc, fugol, wulf — see DEV_NOTES §1 above). But buga/boga, fula/fola are different: the expected form IS the lowered one (boga, fola), so u-retention here is a FST bug, not a documented exception`" [Germanic/docs/DEV_NOTES.md:2973-2973]. For replacement-note purposes, that sentence is the row's most important surviving DEV_NOTES quotation. It means that any future prose should treat `fula` only as superseded debugging history and should not recast `fola` as philologically irregular merely because other labial-adjacent words preserve `u`.

### DEV_NOTES:line-63-138

- Source heading: `NWGmc u-lowering Exceptions Near Labials`
- Source line or section hint: `lines 63-138`
- Fragment type: `shared_rule_and_exception_context`
- Status: `current_as_shared_background`
- Issue tags: `u_lowering`; `documented_exceptions`; `negative_control`; `shared_policy`
- Recommended next use: `cite_as_shared_background_only`
- Shared with row IDs: `1973 and other u-retention / labial-adjacent rows; for 2023 this fragment is contrastive rather than directly row-specific`

This fragment is relevant because it states the sound law that row 2023 now follows. DEV_NOTES says: "`Our NWGmcULowering rule lowers stressed *u → *o before non-high vowels in a following syllable ... This is correct and well-established`" [Germanic/docs/DEV_NOTES.md:70-70]. It then lists the genuine u-preserving counterexamples `*fullăz → full`, `*wulfăz → wulf`, `*fuglăz → fugol`, `*bukkăz → bucc`, `*wullō → wulle`, `*lubō → lufu`, and `*rustō → rust` [Germanic/docs/DEV_NOTES.md:70-78]. That shared policy matters here because `fola` belongs on the rule-following side of the divide, not in the exception list.

The section also preserves useful quoted source language that helps keep the tone conservative. Bülbring is quoted as conceding that "`meist steht jedoch der Hauptregel gemäß o`" — usually the main rule gives `o` — even in the wider labial / velar neighborhood that sometimes shows exceptional `u` [Germanic/docs/DEV_NOTES.md:82-82]. DEV_NOTES then reaches its own project-level decision: "`The u-preserving forms are genuine lexical exceptions for which no phonological conditioning has been established`" [Germanic/docs/DEV_NOTES.md:134-136]. For row 2023, the point is not that foal/fola joins those exceptions, but almost the reverse: this shared fragment provides the background needed to understand why the later row-specific bug note could insist that `fula` was wrong precisely because `fola` is the regular lowered outcome.

## Superseded or diagnostic material

- The only surviving row-specific DEV_NOTES material is the old `*fulô → fula` bucket note. It should now be read strictly as debugging chronology, because the current published trace already yields `fola` by regular development [Germanic/docs/DEV_NOTES.md:2967-2973; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1463-1482].
- The long labial-exception section is relevant only as shared background and as a warning against misclassification. Reusing its `wulf` / `fugol` / `bucc` discussion as if it were direct support for row 2023 would reverse DEV_NOTES' own distinction between genuine lexical exceptions and the now-fixed `fula` bug [Germanic/docs/DEV_NOTES.md:63-138,2969-2973].
- The shoulder paradigm survey is diagnostic support rather than DEV_NOTES authority: it helps explain why `*fúlô` is a normal project input shape (`ô` for trimoric oral *ō in weak masculine n-stem nominative singulars), but it does not itself preserve a row-specific foal note [Germanic/docs/dossier-shoulder-paradigm-survey-2026.md:60-67].
- Coverage remains sparse. The audit still says `none` for row 2023, and no row-specific packet or research memo surfaced during repo search, so this slice should not pretend that a larger dedicated foal/fola research trail survives elsewhere in-repo [Germanic/docs/lexeme_reports/coverage_audit.md:245-245].

## Open questions for later work

- If a full lexeme report is ever commissioned for row 2023, verify manuscript / dictionary support for `fola` beyond the repo's current Wiktionary-derived lexical line; this slice should not overclaim beyond that attestation baseline [Germanic/data/old_english_wiktionary.tsv:88-88].
- If the project later audits weak-masculine `*ô` rows in one batch, re-check that the repaired u-lowering behavior remains stable across the old diagnostic bucket (`*burô`, `*bugô`, `*fulô`, `*uxsô`) and keep row 2023 separated from the genuine u-retention exceptions [Germanic/docs/DEV_NOTES.md:2969-2973; Germanic/docs/dossier-shoulder-paradigm-survey-2026.md:63-67].
- If future indexing adds packet or memo coverage for this row, keep the note conservative: the surviving DEV_NOTES evidence is still mainly a former-bug record plus shared policy context, not a rich row-specific philological dossier.
