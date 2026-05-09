---
row_id: 2081
concept: hoof
counterpart: hōf
proto: *xōfaz
protoform: *xōfaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: ""
linked_research_memo_file: ""
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2081 hoof / hōf

## Current row state

- Live OE row `2081` currently reads `CONCEPT = hoof`, `COUNTERPART = hōf`, `PROTO = *xōfaz`, `PROTOFORM = *xōfaz`, `DERIVATION_CLASS = regular`; the row carries no exception note and only duplicated Wiktionary inheritance sourcing, so `PROTO` and `PROTOFORM` are currently identical and there is no alternate paradigm-cell input in play [Germanic/data/germanic-aligned-final.tsv:585-585].
- `old_english_wiktionary.tsv` also gives `hoof | hōf | inh | template:inh`, so the aligned OE counterpart is at least consistent with the repo’s lexical-source table [Germanic/data/old_english_wiktionary.tsv:144-144].
- `oe_known_problems.tsv` has no entry for row `2081`, `*xōfaz`, or `hōf`; this row is not currently treated as an exception bucket, unresolved mismatch, or documented OE problem [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure still lists `2081 | hoof | hōf | regular | no | - | - | - | none`, and `report_manifest.tsv` still contains only the pilot-report rows, so there is no manifest-backed packet, research memo, or prior lexeme-report stub to inherit here [Germanic/docs/lexeme_reports/coverage_audit.md:281-282; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- The current published derivation trace is an exact match and a very compressed one: `PROTO: *xōfaz`, `EXPECTED: hōf`, `OUTPUTS: hōf`, with the only displayed historical steps being `PGmc Final Z Deletion: *xōfa` and then `PWGmc Final Bare A Loss: *xōf`, followed by orthographic `h*ōf` and outcome `hōf` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2516-2536]. The compact and non-publish lexeme trace snapshots repeat the same two-step analysis and same outcome [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md:2951-2971; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.md:2780-2800].
- The fuller March 2026 trace is useful as a diagnostic witness because it shows that every other named stage is effectively a no-op for this row: after `ProtoInput: *x*ō*f*ă*z`, the root vowel remains `*ō`, the consonant frame remains `*x...f`, `ConsonantRules` removes final `*z`, `FinalWeakSchwaApocope` removes final `*ă`, and the word then passes unchanged to `Orthography: hōf` / `Surface: hōf` [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:7153-7206].

## Development-note summary

No row-specific `DEV_NOTES.md` block for `hoof / hōf / *xōfaz` survives. This slice therefore has to be built conservatively from (a) the live row and live trace state, plus (b) shared-background `DEV_NOTES` material on the chronology of final `*-z` loss and subsequent loss of final bare `*-a`. There is no dedicated hoof essay to preserve.

The surviving support is therefore uneven and should be labeled explicitly. **Row-specific support:** none located. **Shared-background-only support:** yes, especially the current final-`*z` chronology note and an older internal PWGmc ordering summary [Germanic/docs/DEV_NOTES.md:3459-3494,1525-1533]. **Superseded or purely diagnostic material:** yes, mainly the earlier 2026-02-07 PWGmc staging note and the full debug trace, both useful for checking the derivation but not lexeme-specific argumentation [Germanic/docs/DEV_NOTES.md:1525-1544; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:7153-7206].

For row 2081 itself, the operative claim is narrow: the project currently treats the form as fully regular, with stressed root `*ō` preserved and only the weak tail changing, i.e. `*xōfaz -> *xōfa -> *xōf -> hōf` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2523-2536]. Nothing in the current material suggests an analogical workaround, alternate `PROTOFORM`, or row-local exception class.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-3459-3494

- Source heading: `Historical phonology of final *-z loss and its interaction with rhotacism`
- Source line hint: `lines 3459-3494`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `final_z_loss`; `rhotacism_ordering`; `regular_weak_tail`; `consonant_history`
- Recommended next use: `cite_when_explaining_why_*xōfaz_loses_final_z_without_any_*r_stage`
- Shared-with rows if relevant: `2080`; simple OE monosyllables in `*-az` with matched outputs

This is the strongest surviving `DEV_NOTES` material actually relevant to row 2081. The key quotation is R/T as preserved in `DEV_NOTES`: “On the WGmc side, the loss of word-final *z in unstressed syllables ... must likewise have preceded the merger of *z with *r,” followed by the project’s plain-language inference: “Final *-z was **never rhotacized**. It was already gone by the time rhotacism occurred” [Germanic/docs/DEV_NOTES.md:3463-3477]. The same block also preserves Hogg’s summary, “in final position it is generally lost,” and restates the implemented order: `PGmcFinalZLoss` before `PGmcRhotacism` [Germanic/docs/DEV_NOTES.md:3467-3494].

Applied to `*xōfaz`, the substance is straightforward and row-relevant even though the note was not written for `hoof`: the final `*z` in the weak tail is simply deleted in WGmc, giving the trace stage `*xōfa`; there is no intermediate `*xōfar`, and nothing about this row belongs to the inherited-`*r` problem discussed elsewhere in the same section [Germanic/docs/DEV_NOTES.md:3471-3494; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2523-2536]. For this row, that shared fragment supplies essentially the whole consonant-history explanation.

### DEV_NOTES:line-1525-1533

- Source heading: `Proto-West Germanic Stage Implementation (2026-02-07) - EARLIER`
- Source line hint: `lines 1525-1533`
- Fragment type: `diagnostic`
- Status: `superseded_but_still_useful_for_alignment`
- Issue tags: `early_internal_summary`; `z_loss`; `bare_a_loss`; `stage_order`
- Recommended next use: `use_only_as_internal_consistency_check_for_the_*xōfaz_->_*xōfa_->_*xōf_sequence`
- Shared-with rows if relevant: `all simple PWGmc rows whose weak tail is just *-az or *-ą`

This is not a hoof-specific note and it is explicitly an earlier staging memo, but it survives as a concise summary of the exact order the current trace still shows: “Critical PWGmc developments: 1. **Loss of final *-z after unstressed vowels** (first change) 2. **Loss of word-final *-a and *-ą** (immediately after)” [Germanic/docs/DEV_NOTES.md:1529-1533]. That is almost a prose gloss on the live condensed trace for row 2081, where `PGmc Final Z Deletion` yields `*xōfa` and `PWGmc Final Bare A Loss` then yields `*xōf` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2523-2536].

Because this fragment is older and programmatic, it should not be treated as the row’s primary authority. Still, it is valuable as diagnostic confirmation that the row’s present derivation is not an accidental artifact of one debug snapshot: the internal chronology note written months earlier already expected exactly this weak-tail sequence [Germanic/docs/DEV_NOTES.md:1525-1544].

## Superseded or diagnostic material

- No dedicated `DEV_NOTES.md` discussion of `hoof / hōf / *xōfaz` has been located, so there is no surviving row-specific lexeme block to mark as superseded. The replacement slice therefore has to say this plainly: the row is currently documented only through shared chronology notes plus live trace output, not through a preserved hoof memorandum.
- The 2026-02-07 PWGmc implementation note is diagnostically helpful but not the final project formulation. Use it only to corroborate the weak-tail order `*-az -> *-a -> zero`; prefer the later z-loss/rhotacism note when stating current chronology [Germanic/docs/DEV_NOTES.md:1525-1544,3459-3494].
- The large `DEV_NOTES` analyses of bimoraic vs. trimoraic final `*-ō` / `*-ô` are mostly a false lead for this row. Row 2081 contains stressed root `*ō` plus ordinary masculine `*-az`, not a problematic weak-tail long-`ō` suffix, so those sections are background for other noun classes rather than direct support for `*xōfaz -> hōf` [Germanic/docs/DEV_NOTES.md:3542-3592].
- The full March 2026 trace is diagnostic rather than interpretive. Its value is that it shows no hidden vowel change or compensatory repair: after loss of final `*z` and final `*ă`, every downstream stage leaves the form alone until orthography [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:7153-7206].

## Open questions for later work

- If later packetization wants a fuller philological note, the obvious missing piece is not a sound-law fix but a direct scholarly lexical citation for OE `hōf` / PGmc `*xōfaz` beyond the repository’s Wiktionary-derived source table [Germanic/data/old_english_wiktionary.tsv:144-144]. At present, though, the row is matched and unproblematic enough that `needs_literature_agent: no` remains the conservative status.
- If a later DEV_NOTES indexing pass tries to assign every slice a row-local note, row 2081 should remain explicitly tagged as a background-built slice unless new hoof-specific material is found. The current evidence base does not justify pretending that a dedicated hoof block once existed.
- If future debugging ever changes the row from `regular`, re-check the simple two-step weak-tail derivation first. The present snapshots agree that the row’s entire OE-side history is basically `*xōfaz -> *xōfa -> *xōf -> hōf`; any future complication would therefore be a real change in analysis, not something already latent in the current notes [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2523-2536; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:7153-7206].
