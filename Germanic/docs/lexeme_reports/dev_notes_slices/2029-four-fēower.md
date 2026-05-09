---
row_id: 2029
concept: four
counterpart: fēower
proto: '*fédwōr'
protoform: '*fédwōr'
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2029 four / fēower

## Current row state

- The live row currently reads `CONCEPT = four`, `COUNTERPART = fēower`, `PROTO = *fédwōr`, `PROTOFORM = *fédwōr`, and `DERIVATION_CLASS = regular`; in other words, the row now treats the accented long-`ō` proto input and the OE target as fully aligned rather than as an unresolved mismatch [Germanic/data/germanic-aligned-final.tsv:384-384].
- `PROTO` and `PROTOFORM` are identical in the live TSV. That matters here because much of the surviving DEV_NOTES discussion uses intermediate spellings such as `*fedwōrez`, `*fedwor`, or `*fedwar`; those are part of the project's diagnostic history, not the row's current stored metadata [Germanic/data/germanic-aligned-final.tsv:384-384; Germanic/docs/DEV_NOTES.md:16233-16317,16499-16516].
- `oe_known_problems.tsv` has no row-level exception entry for `*fédwōr`, `fēower`, or `four`, so the row is not currently being carried as a live OE problem case [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure still shows row `2029 | four | fēower | regular | no | - | - | - | none`, and `report_manifest.tsv` has no row-2029 pilot/report entry; no row-specific packet or research memo currently survives to override the preferred slice stem, so `2029-four-fēower.md` is the correct filename for this replacement note [Germanic/docs/lexeme_reports/coverage_audit.md:249-249; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- The current published derivation trace is already an exact match: `PROTO: *fédwōr`, `EXPECTED: fēower`, `OUTPUTS: fēower`, with the compact chain `PWGmc Final Or Lowering: *fédwar`, `PWGmc Coronal W Assimilation: *féwwar`, `OE WW Simplification: *féwar`, `OE Ew Long Diphthong: *fēowar`, `Anglo Frisian Brightening: *fēowær`, `OE Unstressed AE Merger: *fēower` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1563-1582].

## Development-note summary

DEV_NOTES support for row 2029 is substantial and unusually concentrated, but it has to be read as a sequence of April 2026 problem-solving passes rather than as one stable note from the start. The earliest surviving fēower section correctly identified the crucial West Germanic consonant step `*dw → *ww` and preserved Ringe–Taylor's basic chain `*fedwor > *fewwar > *feuwar > OE féower`; however, that first pass still framed the mismatch as `*fedwōrez -> fedwore (expected fēower)` and still treated the proto vowel quantity and suffixing somewhat incorrectly for current row purposes [Germanic/docs/DEV_NOTES.md:16229-16349].

The second pass is diagnostically important because it shows the project's intermediate state after the coronal-`w` assimilation had been implemented but before the final-syllable issue was settled. DEV_NOTES records `Input: *fedwor`, `Output: fēowor`, `Expected: fēower`, then isolates the decisive phonological question: why does the final syllable have `-or` instead of the `-er` that the OE target requires? [Germanic/docs/DEV_NOTES.md:16352-16477]. That section is no longer current as row policy, but it preserves the right transition problem.

The controlling current material is the immediately following updated research and Stiles summary. There DEV_NOTES explicitly revises the reconstruction to long-`ō`: Fulk is quoted, “Final r was also preserved, and before it ō apparently remained in Gothic and developed to a in WGmc. (> OE OFris. e), as in Go. fidwōr, OE fēower ...”; Ringe–Taylor are quoted, “Word-finally, and before word-final *r, surviving bimoric long ō-vowels became PWGmc *a ...”; and DEV_NOTES then writes out the now-controlling derivation `PGmc *fedwōr ... *fedwar ... *fewwar ... PWGmc *feuwar ... *fēowær ... OE fēower ✓` [Germanic/docs/DEV_NOTES.md:16488-16516]. The later Stiles summary reinforces the same point with the stronger specialist wording that “the Proto-Germanic sequence *-ōr was shortened to *-ar in West Germanic” and that `WGmc. *-ðw- > *-ww-` is an early change [Germanic/docs/DEV_NOTES.md:16723-16762].

For present row handling, the main distinction to keep explicit is therefore not between competing OE targets but between superseded diagnostic inputs and the live row metadata. The current row's `COUNTERPART = fēower` is not in doubt; the live trace matches it exactly; and the row's `regular` status means the repo now treats the two crucial shared developments — PWGmc `*ō → *a` before final `*r` and PWGmc `*dw → *ww` before later OE `ēo` development — as already implemented rather than as open repairs [Germanic/data/germanic-aligned-final.tsv:384-384; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1563-1582; Germanic/docs/DEV_NOTES.md:16782-16798,20562-20563].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-16229-16349

- Source heading: `OE fēower 'four': PWGmc *dw → *ww Assimilation (2026-04-09)`
- Source line or section hint: `lines 16229-16349`
- Fragment type: `lexeme_specific_but_partly_superseded`
- Status: `mixed_current_and_superseded`
- Issue tags: `dw_to_ww`; `early_fix_pass`; `older_proto_guess`; `spurious_suffix_history`
- Recommended next use: `cite_for_project_history_and_core_assimilation_claim`
- Shared with row IDs:

This is the first real row-local DEV_NOTES section and it still preserves the core consonantal insight that solved the opening mismatch. DEV_NOTES quotes Ringe–Taylor: “The most unusual sound change shared by all the WGmc languages was clearly a PWGmc innovation: the intervocalic sequences `*zw` and `*dw` were assimilated to `*ww` ... PGmc `*fedwor` 'four' (Goth. fidwor) > `*fewwar` > PWGmc `*feuwar` ... > OE féower” [Germanic/docs/DEV_NOTES.md:16242-16258]. It then restates the chain in its own words: `PGmc *fedwor` → `*fewwar` → `*feuwar` → OE `fēower` [Germanic/docs/DEV_NOTES.md:16277-16285].

What remains current in this fragment is the identification of the `*dw → *ww` step and its chronological placement before later WGmc / OE vocalic developments. What is not current is the section's surrounding mismatch frame `*fedwōrez -> fedwore (expected fēower)` and its recommendation that the TSV should simply be corrected to short-vowel, suffixless `*fedwor` [Germanic/docs/DEV_NOTES.md:16233-16238,16288-16333]. Later DEV_NOTES work replaced that live-row recommendation with long-`ō` `*fedwōr`, so this fragment should now be used for the assimilation claim and project chronology, not as the last word on the stored protoform.

### DEV_NOTES:line-16352-16477

- Source heading: `Research: The fēower Final Syllable Problem (-or vs -er) (2026-04-09)`
- Source line or section hint: `lines 16352-16477`
- Fragment type: `diagnostic_transition_fragment`
- Status: `diagnostic_only`
- Issue tags: `partial_fix`; `final_syllable`; `or_vs_er`; `intermediate_state`
- Recommended next use: `use_to_explain_why_the_first_fix_was_only_partial`
- Shared with row IDs:

This section is diagnostically valuable because it captures the exact intermediate state after the coronal-`w` rule had improved the word but had not finished it: “Input: `*fedwor` — Output: `fēowor` — Expected: `fēower`” [Germanic/docs/DEV_NOTES.md:16356-16361]. DEV_NOTES then writes out the fuller chain `PGmc *fedwor ... → *fewwar ... → PWGmc *feuwar ... → *feuwæer ... → OE *féowæer ... → fēower`, correctly noticing that some `*-ar > -er` development had to be present in the background even if the section had not yet pinned it down cleanly [Germanic/docs/DEV_NOTES.md:16363-16416].

The reason this fragment is diagnostic rather than current is that it still treated the `*o → *a` step as somewhat speculative and recommended an interim `*fedwar` solution: “Option C seems most practical ... Using `*fedwar` captures the pre-WGmc form that feeds regular rules” [Germanic/docs/DEV_NOTES.md:16457-16467]. That recommendation was soon superseded by the next section's explicit long-`ō` analysis. Still, this fragment should be preserved because it explains why the row once looked nearly correct (`fēowor`) yet still needed one more phonological clarification.

### DEV_NOTES:line-16482-16603

- Source heading: `Updated Research: The -ōr → -ar → -er Chain (2026-04-09)`
- Source line or section hint: `lines 16482-16603`
- Fragment type: `lexeme_specific_current_authority`
- Status: `current`
- Issue tags: `long_o_before_final_r`; `current_reconstruction`; `fulk_quote`; `ringe_taylor_quote`
- Recommended next use: `primary_fragment_for_final_report`
- Shared with row IDs: `2298; 2287`

This is the controlling current DEV_NOTES fragment for row 2029. It preserves the two quotations that shift the row from provisional repair to settled analysis. First Fulk: “Final r was also preserved, and before it ō apparently remained in Gothic and developed to a in WGmc. (> OE OFris. e), as in Go. fidwōr, OE fēower, OS fi(u)war 'four' ...” [Germanic/docs/DEV_NOTES.md:16488-16491]. Then Ringe–Taylor: “Word-finally, and before word-final *r, surviving bimoric long ō-vowels became PWGmc *a, while trimoric long ō-vowels became PWGmc *ō” [Germanic/docs/DEV_NOTES.md:16493-16495]. DEV_NOTES immediately draws the row-level consequence: “The correct PGmc reconstruction is `*fedwōr` (with long `*ō`)” [Germanic/docs/DEV_NOTES.md:16537-16540].

The same fragment also supplies the best compact derivational paragraph for the slice. DEV_NOTES writes: `PGmc *fedwōr ... *fedwar ... *fewwar ... PWGmc *feuwar ... pre-OE *feuwær ... *fēowær ... OE fēower ✓` [Germanic/docs/DEV_NOTES.md:16499-16516]. That chain is materially closer to the live trace than the older April 9 sections are, even though the live TSV now uses the project's accented notation `*fédwōr` rather than unaccented `*fedwōr` [Germanic/data/germanic-aligned-final.tsv:384-384; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1572-1576]. For current replacement-note purposes, this is the fragment that most clearly justifies both the long-`ō` protoform and the regular status of the OE output.

### DEV_NOTES:line-16715-16803

- Source heading: `Stiles 1985-6 on the Numeral 'four': Research Summary (2026-04-10)`
- Source line or section hint: `lines 16715-16803`
- Fragment type: `lexeme_specific_literature_validation`
- Status: `current`
- Issue tags: `stiles`; `specialist_support`; `dw_to_ww`; `or_to_ar`
- Recommended next use: `cite_when_specialist_support_is_needed`
- Shared with row IDs: `1992; 2298; 2287`

This fragment is narrower in scope than the previous one but stronger in specialist emphasis. DEV_NOTES says Stiles' three-part NOWELE article “is the definitive study of the numeral 'four' across Germanic,” then preserves the key line that West Germanic `four`-forms require a preform in `*-ar`: “the Proto-Germanic sequence `*-ōr` was shortened to `*-ar` in West Germanic” [Germanic/docs/DEV_NOTES.md:16723-16747]. It also keeps the corresponding consonantal claim: “WGmc. `*-ðw- > *-ww-` ... This soundchange must be very early” [Germanic/docs/DEV_NOTES.md:16752-16762].

The practical value of the section is that it turns the row from an internal FST repair story into a literature-backed one. DEV_NOTES explicitly validates the implemented rule set with the table entry ``*fedwōr | *ō → *a before *r# | *fedwar → (breaking) → fēower ✓`` [Germanic/docs/DEV_NOTES.md:16780-16789]. Because the live trace now shows the same path in operational form, this fragment is best used when later work needs to justify that the row is regular on external philological grounds, not merely because the transducer happens currently to output the expected spelling [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1572-1576].

### DEV_NOTES:line-20562-20563

- Source heading: `regression stocktake after the §17 refactor baseline`
- Source line or section hint: `lines 20562-20563`
- Fragment type: `brief_current_ledger`
- Status: `current`
- Issue tags: `resolved_item`; `post_fix_ledger`; `not_a_live_mismatch`
- Recommended next use: `cite_only_as_short_confirmation`
- Shared with row IDs: `2042; 2058; 2140; 2308`

This tiny fragment has little philological content, but it is a useful current-state guardrail. DEV_NOTES' later mismatch stocktake lists “**8 items fixed** (no longer mismatching): `*fédwōr`, `*fríjōndz`, ...” [Germanic/docs/DEV_NOTES.md:20562-20563]. For row 2029, that confirms the practical outcome of the earlier April 9-10 research: by the time of the later audit, `*fédwōr` had moved out of the live mismatch set.

## Superseded or diagnostic material

- The oldest row-local mismatch string `*fedwōrez -> fedwore (expected fēower)` is superseded as live row status. Its value now is historical only: it shows the pre-fix failure mode, not the current row metadata or output [Germanic/docs/DEV_NOTES.md:16233-16238].
- DEV_NOTES spellings `*fedwor` and `*fedwar` should not be copied mechanically into row metadata. `*fedwor` belongs to an earlier analytical pass that had not yet restored the long vowel; `*fedwar` was a provisional workaround stage used while the `*-ōr → *-ar` question was still being sorted out [Germanic/docs/DEV_NOTES.md:16281-16333,16457-16467]. The live row now stores `*fédwōr` / `*fédwōr` and reaches `fēower` by rule application, not by keeping those provisional forms in TSV metadata [Germanic/data/germanic-aligned-final.tsv:384-384].
- No row-specific packet or research memo currently survives, and no `oe_known_problems.tsv` entry carries the row as an exception. The slice therefore has to stand on its own as a replacement working note, anchored chiefly in DEV_NOTES and the current trace output rather than in separate lexeme-report scaffolding [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/coverage_audit.md:249-249; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].

## Open questions for later work

- If a full lexeme report is written later, decide whether the prose should cite the row's live protoform as accented project notation `*fédwōr` throughout, or whether it should explicitly pair that with the unaccented handbook-style `*fedwōr` used in the April 2026 DEV_NOTES quotations. The slice should not collapse those notation layers silently [Germanic/data/germanic-aligned-final.tsv:384-384; Germanic/docs/DEV_NOTES.md:16499-16516].
- If later reporting expands the `PWGmcFinalOrLowering` cluster, keep row 2029 attached to the shared `*ō → *a before final *r` discussion together with comparators like `watōr > wæter`, rather than presenting `fēower` as if it depended only on a special numeral-only repair. Stiles makes the numeral historically distinctive, but the implemented vowel-shortening rule is shared in the project [Germanic/docs/DEV_NOTES.md:16780-16789].
- If future literature review is undertaken, the most obvious value-add would be direct reuse of Stiles' article itself rather than relying only on the quotations already preserved in DEV_NOTES. That is not necessary for the present slice, but it would strengthen any later final report that wants fuller specialist apparatus [Germanic/docs/DEV_NOTES.md:16715-16803].
