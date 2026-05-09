---
row_id: 2080
concept: hood
counterpart: hōd
proto: *ōdaz
protoform: *ōdaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/debug_snapshots/oe_full_trace_report.txt
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2080 hood / hōd

## Current row state

- The live aligned OE row is now a clean regular entry: `ID 2080 | CONCEPT hood | COUNTERPART hōd | PROTO *xōdaz | PROTOFORM *xōdaz | DERIVATION_CLASS regular`, with empty `NOTE` and only duplicated Wiktionary inheritance provenance in `HISTORY` [Germanic/data/germanic-aligned-final.tsv:580-581]. The assignment metadata for this slice normalizes the protoform as `*ōdaz`, but the live row and all current trace snapshots use the repo's `*xōdaz` spelling for the initial OE `h` reflex [Germanic/data/germanic-aligned-final.tsv:580-581; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2495-2515].
- Current trace state is fully regular and minimal. The published derivation report gives `PROTO: *xōdaz`, `EXPECTED: hōd`, `OUTPUTS: hōd`, with only `PGmc Final Z Deletion: *xōda` and `PWGmc Final Bare A Loss: *xōd` before surface `hōd` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2495-2515].
- The full trace confirms that no hidden repair machinery is involved. After `PGmcFinalZDeletion` and `PWGmcFinalBareALoss`, every subsequent OE phonological rule remains `[no-change]`; orthography then maps `*x*ō*d` to `*h*ō*d, h*ō*d`, and `OldEnglishRemoveStars` yields `hōd` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:16243-16357].
- Coverage infrastructure still treats the row as uncovered and unattached: `| 2080 | hood | hōd | regular | no | - | - | - | none |`, and the manifest still lists only the small pilot set, with no entry for row `2080` [Germanic/docs/lexeme_reports/coverage_audit.md:281-281; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- `oe_known_problems.tsv` has no `*xōdaz` / `*ōdaz` / `hōd` entry, which matches the live traces: this row is not currently tracked as an exception, mismatch, or unresolved bug [Germanic/data/oe_known_problems.tsv:1-8].

## Development-note summary

No current row-specific DEV_NOTES block survives for the live `*xōdaz > hōd` row. What survives instead is a small superseded diagnostic trail from the period when this cognate set was apparently aligned with the wrong proto input `*xattuz`, producing `hatt` while the row target remained `hōd` [Germanic/docs/DEV_NOTES.md:1767-1772,2622-2624].

That surviving material is still worth preserving because it states the project's conclusion very clearly: the problem was **data alignment rather than phonology**. DEV_NOTES explicitly says the item is not a long-vowel-rule problem and that the provided proto stem was simply the wrong one: “`expected reflex doesn’t match the provided proto stem (phonologically it yields OE “hat”); fix data alignment rather than phonology`” [Germanic/docs/DEV_NOTES.md:1772-1772]. In current row state, that diagnostic has already been absorbed into the data: the live aligned row now uses `*xōdaz`, and the current derivation reaches `hōd` with no special handling [Germanic/data/germanic-aligned-final.tsv:580-581; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2495-2515].

So the conservative replacement note is simple but important: there is no surviving DEV_NOTES evidence for a bespoke sound change problem in row `2080`; the only row-specific DEV_NOTES evidence is superseded mismatch diagnostics from an earlier misaligned protoform. All positive support for the row's present analysis comes from the live TSV plus current trace snapshots, not from a dedicated `DEV_NOTES.md` lexeme discussion [Germanic/docs/DEV_NOTES.md:1767-1772,2622-2624; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:16243-16357].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1767-1767

- Source heading: `OE epenthesis update (2026-01-04)` / mismatch carryover notes
- Source line or section hint: `line 1767`
- Fragment type: `shared_bucket_boundary`
- Status: `superseded_but_still_relevant_as_scope_control`
- Issue tags: `long_vowel_bucket_boundary`; `misclassification_warning`; `diagnostic_only`
- Recommended next use: `cite_when_explaining_what_the_row_was_not`
- Shared with rows if relevant: `other non-long-vowel items briefly parked beside *end and *utrăz`

This tiny fragment is still useful because it sets the negative frame for row `2080`. DEV_NOTES says: “`Other` misses (e.g., `*end→ān`, `*utrăz→nǣdre`, `*xattuz→hōd`) are not long-vowel rules; treat separately” [Germanic/docs/DEV_NOTES.md:1767-1767]. For this row, the value is not positive phonological explanation but boundary marking. The note shows that even during the earlier mismatch phase, the project had already decided that the `hōd` problem did **not** belong in the active long-vowel-fix agenda. That matters because the current row now has long `ō`, but DEV_NOTES had already concluded the old mismatch was not evidence for a missing “make `ō` longer” rule.

### DEV_NOTES:line-1772-1772

- Source heading: `OE epenthesis update (2026-01-04)` / 2026-01-10 tracing follow-up
- Source line or section hint: `line 1772`
- Fragment type: `lexeme_specific_diagnostic`
- Status: `superseded`
- Issue tags: `data_alignment`; `wrong_proto_input`; `not_a_phonology_fix`; `hat_vs_hōd`
- Recommended next use: `preserve_as_the_main_row_specific_DEV_NOTES_statement`
- Shared with rows if relevant: `row-specific to the old hood mismatch`

This is the strongest surviving row-specific DEV_NOTES sentence and should be preserved almost verbatim because it states the project's judgement without hedging: “`*xattuz → hōd`: expected reflex doesn’t match the provided proto stem (phonologically it yields OE “hat”); fix data alignment rather than phonology`” [Germanic/docs/DEV_NOTES.md:1772-1772]. That sentence does three jobs at once. First, it records the older bad pairing `*xattuz` ~ `hōd`. Second, it states the predicted OE outcome of that protoform (`hat`/`hatt`) plainly enough that later writers do not mistake the mismatch for a mysterious irregularity. Third, it gives the resolution path: change the data, not the sound laws.

For present row work, this fragment is therefore **superseded but central**. The live row no longer uses `*xattuz`; it uses `*xōdaz`, and the current grammar derives `hōd` regularly [Germanic/data/germanic-aligned-final.tsv:580-581; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2495-2515]. But if someone later asks why DEV_NOTES ever mentioned `hood / hōd` at all, this one-line correction is the answer.

### DEV_NOTES:line-2622-2624

- Source heading: `OE diagnostics: mismatch closeness + diacritics (2026-01-02)`
- Source line or section hint: `lines 2622-2624`
- Fragment type: `diagnostic_bucket_listing`
- Status: `superseded`
- Issue tags: `long_vowel_missing_bucket`; `early_mismatch_snapshot`; `hatt_expected_hōd`; `diagnostic_only`
- Recommended next use: `use_only_for_debugging_chronology`
- Shared with rows if relevant: `the six-item long-vowel-missing probe list`

This earlier bucket listing preserves the raw mismatch state before the later data-alignment conclusion was written out. DEV_NOTES records the then-current six-item probe list as including “`*xattuz → hatt (expected hōd)`” beside `ċeowwan`, `hærw`, `ān`, `sleaan`, and `weġ` cases [Germanic/docs/DEV_NOTES.md:2622-2624]. The important thing to preserve is that this was a **diagnostic list**, not a settled analysis. In other words, row `2080` first appeared in DEV_NOTES as part of a rough long-vowel-missing bucket, but it did not stay there.

Read against the later line-1772 note, this fragment documents the superseded state of understanding: an apparent long-vowel issue was later reinterpreted as bad lexical alignment [Germanic/docs/DEV_NOTES.md:1772-1772,2622-2624]. For the replacement slice, that means this fragment should be used only to reconstruct debugging chronology, never as current evidence that `hōd` still requires a phonological repair.

## Superseded or diagnostic material

- The only surviving row-specific DEV_NOTES material is diagnostic and superseded. It concerns `*xattuz` / `hatt`, not the live current row spelling `*xōdaz > hōd` [Germanic/docs/DEV_NOTES.md:1772-1772,2622-2624; Germanic/data/germanic-aligned-final.tsv:580-581].
- The main superseded interpretation is the old placement of this item inside the long-vowel-missing probe list. DEV_NOTES itself later corrected that classification by saying the item was “not long-vowel rules” material and needed data alignment instead [Germanic/docs/DEV_NOTES.md:1767-1772,2622-2624].
- The current traces leave no residue of the old problem state. They show a trivial regular derivation with no special OE rule firing beyond final-segment loss and orthographic `x > h`, so any future note that still presents row `2080` as a live sound-law problem would be stale [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2495-2515; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:16243-16357].
- No packet, research memo, or dedicated analysis file for row `2080` surfaced in the current repo search, and coverage still says `none`, so this slice should not imply that a richer lexeme dossier survives elsewhere in-repo [Germanic/docs/lexeme_reports/coverage_audit.md:281-281; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].

## Open questions for later work

- Decide whether any future full report should normalize the protoform as `*ōdaz` for presentation while keeping explicit note that the live aligned row and trace machinery currently use `*xōdaz` notation for initial `h` [Germanic/data/germanic-aligned-final.tsv:580-581; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2495-2515].
- If later archival cleanup revisits early mismatch snapshots, consider whether the old `*xattuz → hatt (expected hōd)` references should be cross-linked more explicitly to the corrected live row, so future slicers do not mistake them for evidence of an unresolved phonological exception [Germanic/docs/DEV_NOTES.md:1772-1772,2622-2624].
- If a later lexeme report is commissioned, the first philological task is not sound-law debugging but provenance cleanup: determine when and why the cognate set moved from the old `*xattuz` diagnostic to the current `*xōdaz` alignment, because DEV_NOTES preserves the correction judgement but not the full re-alignment history [Germanic/docs/DEV_NOTES.md:1772-1772; Germanic/data/germanic-aligned-final.tsv:580-581].
