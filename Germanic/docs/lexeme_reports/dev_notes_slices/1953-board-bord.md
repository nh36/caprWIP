---
row_id: 1953
concept: board
counterpart: bord
proto: *búrdą
protoform: *búrdą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/non_firing_rules_analysis.md
  - Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1953 board / bord

## Current row state

- CONCEPT: `board`
- COUNTERPART: `bord`
- PROTO: `*búrdą`
- PROTOFORM: `*búrdą`
- DERIVATION_CLASS: `regular`
- The live TSV row is stable and note-light: row `1953` currently reads `board / bord / *búrdą / regular`, with no row-specific explanatory note beyond inherited-etymology placeholders [Germanic/data/germanic-aligned-final.tsv:84-84].
- The current published derivation trace already returns the target with no workaround: `PROTO: *búrdą`, `EXPECTED: bord`, `OUTPUTS: bord`, with the compact stage chain `NWGmc U Lowering: *bórdą` and then `OE Heavy Syllable Nasal Apocope: *bórd` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:309-328].
- `oe_known_problems.tsv` is relevant only as a negative control here: it tracks several `u_lowering_near_labial` exceptions such as `*búkkaz`, `*fúglaz`, `*wúlfaz`, `*wúllō`, and `*rústō`, but it does not list `*búrdą`; the row is therefore not currently being handled as an OE exception bucket [Germanic/data/oe_known_problems.tsv:1-8].

## Development-note summary

No dedicated lexeme-specific DEV_NOTES section for row `1953` was located. The relevant DEV_NOTES authority is therefore **shared rule discussion plus one later regression note**, not a bespoke board dossier. That support is thin but still materially useful, and it supports a conservative reading: `bord` is being treated as an ordinary regular reflex, not as a debated target or special repair item [Germanic/data/germanic-aligned-final.tsv:84-84; Germanic/docs/DEV_NOTES.md:68-86].

The main shared rule note is the early NWGmc u-lowering discussion. DEV_NOTES states plainly that the project rule “lowers stressed `*u → *o` before non-high vowels in a following syllable” and calls that rule “correct and well-established” [Germanic/docs/DEV_NOTES.md:70-70]. The same section then spends its effort on the **exceptional** words that keep `u` near labials (`full`, `wulf`, `fugol`, `bucc`, `wulle`, `lufu`, `rust`) and on why those should be accepted as lexical exceptions rather than rewritten into fake regularity [Germanic/docs/DEV_NOTES.md:72-78,134-138]. For row `1953`, that shared note matters precisely because `*búrdą` is **not** presented as one of those exceptions: with a following non-high vowel `*ą`, the current grammar's regular path is `*búrdą > *bórdą > bord`, exactly as the live trace now shows [Germanic/docs/DEV_NOTES.md:70-70,136-138; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:318-328].

The second materially relevant DEV_NOTES passage is later and diagnostic. During the §17.13 cleanup that tried to remove residual `{*ă}` engineering markup, DEV_NOTES records that a blanket sweep caused a large regression in the bucket `vowel_quality__u_o_alternation`, explicitly including the example “`*búrdą → burd` expected `bord`” [Germanic/docs/DEV_NOTES.md:28164-28179]. The note's stated lesson is that “`{*ă}` was carrying phonology, not just marking,” and the successful staged migration then restored the grammar to the earlier mismatch count while keeping the cascade “breve-free at every live code site” [Germanic/docs/DEV_NOTES.md:28179-28232,28290-28300]. For row `1953`, this is not a philological reanalysis of the lexeme; it is implementation history showing that `bord` functions as a real regression sentinel for preserving the regular `u/o` alternation and final heavy-syllable apocope together.

Taken together, the current replacement note should preserve three points and not overclaim more. First, the live row is regular and currently derives correctly [Germanic/data/germanic-aligned-final.tsv:84-84; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:309-328]. Second, DEV_NOTES support is mostly **shared** rather than lexeme-local: it gives the general rule for stressed `*u > *o` and a later regression example using `*búrdą`, but not a row-specific source audit for `bord` [Germanic/docs/DEV_NOTES.md:68-86,134-138,28164-28300]. Third, because the row is absent from the repo's exception register, later writing should resist inflating the note into an exception narrative merely because `*búrdą` happened to appear in one regression bucket [Germanic/data/oe_known_problems.tsv:1-8].

## Relevant DEV_NOTES fragments

### Germanic/docs/DEV_NOTES.md:68-86,134-138

- Source heading: `NWGmc u-lowering Exceptions Near Labials`
- Source line or section hint: `lines 68-86 and 134-138`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `nwgmc_u_lowering`; `shared_sound_change`; `exception_boundary`; `regular_reflex`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1951; 1973; 2043; 2082`

This is the main DEV_NOTES authority that bears on `bord`, even though it is not row-specific. Its most reusable sentence is the opening claim that the NWGmc rule “lowers stressed `*u → *o` before non-high vowels in a following syllable” and that this is “correct and well-established” [Germanic/docs/DEV_NOTES.md:70-70]. The section then carefully narrows the exception space by listing the genuinely problematic `u`-preserving lexemes and later making the implementation decision explicit: “Accept the mismatches. The FST correctly models the regular NWGmc u-lowering as a phonological rule. The u-preserving forms are genuine lexical exceptions for which no phonological conditioning has been established” [Germanic/docs/DEV_NOTES.md:72-78,136-138]. For row `1953`, that negative framing is the important part: `*búrdą` is not one of the exception items, so the shared note supports treating `bord` as the regular lowered outcome, not as a labial-retention case [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:318-328].

### Germanic/docs/DEV_NOTES.md:28164-28300

- Source heading: `§17.13.2 Failed naïve sweep (archived, for future-warning)` through `§17.13.6 Outcome`
- Source line or section hint: `lines 28164-28300`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current_diagnostic`
- Issue tags: `regression_history`; `vowel_quality__u_o_alternation`; `breve_cleanup`; `board_regression_sentinel`
- Recommended next use: `use_to_explain_implementation_history`
- Shared with row IDs: `1951; 1953; 1992`

This fragment is worth preserving because it names the row's protoform directly. DEV_NOTES says a first blanket removal of `{*ă}` references regressed mismatches from `33 → 71`, with `vowel_quality__u_o_alternation ×22` including the explicit example “`*búrdą → burd` expected `bord`” [Germanic/docs/DEV_NOTES.md:28166-28175]. The next sentence gives the engineering takeaway in a form that should be copied almost verbatim: “The lesson: `{*ă}` was carrying phonology, not just marking” [Germanic/docs/DEV_NOTES.md:28179-28180]. The successful staged rewrite then held the mismatch count at `33` and left the grammar “breve-free at every live code site” [Germanic/docs/DEV_NOTES.md:28232-28300]. For row `1953`, this is not evidence of lexical uncertainty; it is evidence that `bord` had to be preserved through a structural refactor because the row exposes a real interaction between the `u > o` development and later loss of final heavy-syllable `-ą`.

## Superseded or diagnostic material

- Two non-DEV_NOTES analysis files preserve an older failure state in which the row still surfaced with extra final `-a`: `*burdą -> burda (expected bord)` appears in `non_firing_rules_analysis.md` and again in `final_vowel_apocope_investigation.md` [Germanic/docs/non_firing_rules_analysis.md:99-109; Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:273-280]. These are useful diagnostics for project chronology, but they are superseded by the current published derivation trace, which already returns `bord` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:309-328].
- No row-specific DEV_NOTES source audit for dictionary attestations of OE `bord` was found. That absence should be stated plainly rather than patched over: the current slice is grounded in shared rule notes and implementation history, not in a lexeme-local literature review.
- The absence of `*búrdą` from `oe_known_problems.tsv` is diagnostic bookkeeping, not independent philological proof. It is useful because it shows the row is not being treated like `bucc`/`fugol`/`wulf`/`wulle`/`rust`, but it does not by itself prove that every aspect of the `bord` row has been literature-audited [Germanic/data/oe_known_problems.tsv:1-8].

## Open questions for later work

- If a later report needs lexeme-local philological authority rather than shared rule authority, add a packet or memo for row `1953`; at present, the row has good implementation support but thin lexeme-specific DEV_NOTES support.
- If future indexing work triages slices by distinctiveness, row `1953` probably belongs in a low-priority or no-index bucket unless more lexeme-specific source discussion is added. The current value of the slice is real, but it is mostly as a shared-rule/regression record rather than as a standalone exception narrative.
- If the row is ever cited alongside the `u`-preserving labial exceptions, keep the contrast explicit: `bord` is the regular lowered case, whereas the exception list in DEV_NOTES is about lexemes that unexpectedly keep `u` [Germanic/docs/DEV_NOTES.md:70-78,136-138; Germanic/data/oe_known_problems.tsv:1-8].
