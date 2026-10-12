---
row_id: 2076
concept: hoard
counterpart: hord
proto: "*xúzdą"
protoform: "*xúzdą"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/mismatch_dossier_mizdo.md
  - Germanic/docs/analysis/meord_med_chronological_review.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2076 hoard / hord

## Current row state

- CONCEPT: `hoard`
- COUNTERPART: `hord`
- PROTO: `*xúzdą`
- PROTOFORM: `*xúzdą`
- DERIVATION_CLASS: `regular`
- The live TSV row is sparse but internally coherent: row `2076` currently gives OE `hord` from `*xúzdą`, with `PROTO` and `PROTOFORM` identical and only duplicated generic source placeholders in the NOTE field rather than a substantive row-specific explanation [Germanic/data/germanic-aligned-final.tsv:565-567].
- The row is not in the OE exception ledger. `oe_known_problems.tsv` records several explicit OE exceptions and unmodelled cases, but no entry for `*xúzdą` / `hord`; current bookkeeping therefore treats row 2076 as a regular derivation, not as an accepted mismatch or pending repair [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage/audit state is likewise minimal: `coverage_audit.md` marks row `2076 | hoard | hord | regular | no | - | - | - | none |`, and `report_manifest.tsv` has no entry for this row at all, so this slice has to carry the row's detailed working note without relying on a manifest-backed packet or memo [Germanic/docs/lexeme_reports/coverage_audit.md:278-278; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- The current published derivation trace is clean and should be treated as the best statement of current row mechanics: `PROTO: *xúzdą`, `EXPECTED: hord`, `OUTPUTS: hord`, with explicit intermediate steps `Rhotacism: *xúrdą`, `NWGmc U Lowering: *xórdą`, `OE Heavy Syllable Nasal Apocope: *xórd`, and final orthography/surface `hord` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2410-2431; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:6878-6931].

## Development-note summary

No dedicated row-specific DEV_NOTES block survives for row 2076. The only direct DEV_NOTES hit that names this lexeme is an early **diagnostic** note from the period when `xuzdą` was still failing because `*z` was not rhotacizing; that material is useful project history, but it is superseded as a description of the live row because the current trace now shows the expected early `*z > r` step and a full exact match to `hord` [Germanic/docs/DEV_NOTES.md:2541-2548; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2410-2431].

What remains current is therefore mostly **shared-background-only** material plus current row state. The shared DEV_NOTES rule note on NWGmc u-lowering still matters because it states the rule in the form row 2076 needs: stressed `*u` lowers to `*o` before a following non-high vowel, and the project treats only a restricted set of `u`-retaining items as genuine exceptions [Germanic/docs/DEV_NOTES.md:68-86,134-138]. Row 2076 is not one of those exceptions; once rhotacism has produced `*xúrdą`, the trace's next step `*xórdą` is exactly the regular shared rule outcome [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:6886-6889].

The conservative row-specific take is therefore: `PROTO` and `PROTOFORM` are both the same inherited comparator `*xúzdą`; the attested/target OE form is `hord`; the decisive early operation is post-vocalic rhotacism of `*z` before `d`, after which ordinary NWGmc `u > o` and final heavy-syllable apocope yield the target. There is no surviving evidence in DEV_NOTES that the row was ever philologically controversial in its current form. The only controversy preserved in the documentation is diagnostic implementation history about getting `*z > r` to fire early enough and broadly enough [Germanic/docs/DEV_NOTES.md:2545-2547; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2419-2431].

Two non-DEV_NOTES analysis files are worth keeping in view, but only as support, not as replacement authority. `mismatch_dossier_mizdo.md` uses hoard as the clean comparator for `*-zd-` behavior and states the expected chain `*xúzdą -> *xúrdą -> *hordą -> hord` [Germanic/docs/analysis/mismatch_dossier_mizdo.md:462-463,509-509]. `meord_med_chronological_review.md` preserves Campbell's wording that Germanic `z` became `r` in North and West Germanic and that between vowel and consonant this `r` "usually remains, e.g. hord, reord, &c." [Germanic/docs/analysis/meord_med_chronological_review.md:232-237]. Both are useful corroboration, but they are **shared-background-only** and should not be misdescribed as a lost row-specific DEV_NOTES dossier.

## Relevant DEV_NOTES fragments

### Germanic/docs/DEV_NOTES.md:2541-2548

- Source heading: `OE diagnostics follow-up: orthography + rhotacism`
- Source line or section hint: `lines 2541-2548`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `rhotacism`; `postvocalic_z`; `implementation_history`; `surface_filter`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `1946; 2051; 2095; 2124`

This is the only direct DEV_NOTES fragment that actually names the row's protoform, and it has to be kept with a strong diagnostic label. DEV_NOTES says that seven items, including ``xuzdą``, lost outputs after the OE surface filter because "`EnglishZRhotacism` never fires" and "`ConsonantRules` leaves `{*z}` intact in every case" [Germanic/docs/DEV_NOTES.md:2544-2545]. It then gives the broader historical claim that even a repaired rule cannot stay narrowly intervocalic: "`PGmc *z should rhotacize in post-vocalic contexts like V-z-j/w/n/d-V (berry, hair, learn, meed, hoard)`," and the chronology note that this rhotacism must be early, before later glide and OE vowel changes [Germanic/docs/DEV_NOTES.md:2546-2547]. For row 2076, the lasting value of the fragment is not that it describes the current row state—it does not—but that it preserves the project's earlier realization that hoard belongs in the wider **post-vocalic `*z` before consonant** rhotacism environment, not in a tiny `V _ V` rule.

### Germanic/docs/DEV_NOTES.md:68-86,134-138

- Source heading: `NWGmc u-lowering Exceptions Near Labials`
- Source line or section hint: `lines 68-86 and 134-138`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `nwgmc_u_lowering`; `shared_sound_change`; `regular_reflex`; `exception_boundary`
- Recommended next use: `keep_as_shared_background`
- Shared with row IDs: `1953; 1973; 2030; 2298`

This is shared background rather than a hoard note, but it is still the current DEV_NOTES authority for the vowel step in row 2076. DEV_NOTES states that the rule "lowers stressed `*u → *o` before non-high vowels in a following syllable" and calls that rule "correct and well-established" [Germanic/docs/DEV_NOTES.md:70-70]. The same section then insists that the `u`-preserving forms should be treated as lexical exceptions and makes the project policy explicit: "`Accept the mismatches. The FST correctly models the regular NWGmc u-lowering as a phonological rule`" [Germanic/docs/DEV_NOTES.md:136-138]. For row 2076 the fragment's role is narrow but important: once rhotacism has already produced `*xúrdą`, the row simply follows the shared regular pathway to `*xórdą`, and nothing in DEV_NOTES marks hoard as an exception to that vowel history.

## Superseded or diagnostic material

- The December 2025 rhotacism note is superseded as a row description. It belongs to the earlier failure state where `xuzdą` still surfaced with unrepaired `z` and then disappeared at the OE surface filter; the live trace now explicitly shows `Rhotacism: *xúrdą` and reaches `hord` without residue [Germanic/docs/DEV_NOTES.md:2544-2547; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2419-2431].
- `mismatch_dossier_mizdo.md` is useful because it explicitly uses hoard as the clean comparator for `*-zd-` behavior and says "`*xúzdą` 'hoard' -> FST: `hord`" with the expected chain "`*xúzdą` -> `*xúrdą` -> `*hordą` -> `hord`" [Germanic/docs/analysis/mismatch_dossier_mizdo.md:462-463,509-509]. That is good support, but it is not a DEV_NOTES block and should be cited as **diagnostic/shared support**, not as row-specific inherited documentation.
- Likewise, the Campbell quotation preserved in `meord_med_chronological_review.md`—Germanic `z` became `r` in North and West Germanic, and between vowel and consonant `r` "usually remains, e.g. hord, reord, &c."—is valuable shared background for the `*xúrdą` stage, but it survives in an analysis memo rather than in a dedicated hoard note [Germanic/docs/analysis/meord_med_chronological_review.md:232-237].
- The absence of row 2076 from both `oe_known_problems.tsv` and `report_manifest.tsv`, together with `coverage_audit.md`'s `none` status line, is important negative evidence. It means later work should resist reconstructing a hidden exception narrative for this row merely because hoard once appeared in a rhotacism debugging sweep [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/coverage_audit.md:278-278; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].

## Open questions for later work

- If future rhotacism refactoring touches post-vocalic `*z` before consonants, keep row 2076 as a regression sentinel: the crucial ordered chain is `*xúzdą -> *xúrdą -> *xórdą -> hord`, not merely a final orthographic match [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:6883-6931].
- If a later packet or memo is created for this row, keep the evidence classification explicit: current support is mostly shared-background plus trace verification, because no surviving row-specific DEV_NOTES dossier exists.
- If bibliography work later adds a direct lexeme-level source for OE `hord < *xúzdą`, that source could replace some of the present shared-background scaffolding; until then, the conservative row note should continue to say plainly that the best surviving direct DEV_NOTES material is diagnostic rather than lexeme-specific.
