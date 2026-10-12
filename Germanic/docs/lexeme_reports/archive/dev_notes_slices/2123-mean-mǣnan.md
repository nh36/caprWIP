---
row_id: 2123
concept: mean
counterpart: mǣnan
proto: '*máinijaną'
protoform: '*máinijaną'
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/debug_snapshots/oe_full_trace_report.txt
current_status: current_exact_match_shared_notes_only
needs_literature_agent: no
---

# DEV_NOTES material — 2123 mean / mǣnan

## Current row state

- The live OE row is `ID 2123`, `CONCEPT mean`, `COUNTERPART mǣnan`, `PROTO = PROTOFORM = *máinijaną`, `DERIVATION_CLASS regular`, with no live row note and only generic source tags in the TSV. The same cognate set also contains Dutch `menen`, English `mean`, and German `meinen`, all aligned to the same protoform [Germanic/data/germanic-aligned-final.tsv:747-750].
- The current published OE derivation is an exact match: `PROTO: *máinijaną`, `EXPECTED: mǣnan`, `OUTPUTS: mǣnan`. The compact trace makes the operative chain explicit: `PWGmc Ai Monophthongization: *mānijaną`, then `OE Heavy Syllable Nasal Apocope`, `OE Secondary Nasalization`, `Sievers Law Syncope`, `OE I Umlaut`, `OE Weak Tail Reduction`, and `OE J Loss After Heavy`, ending at `mǣnan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3184-3203].
- The full trace confirms that the live proto input really contains separate `i + j` material, not a bare `-j-` tail: `ProtoInput: *m*ái*n*i*j*a*n*ą`, `PWGmcAiMonophthongization: *m*ā*n*i*j*a*n*ą`, `SieversLawSyncope: *m*ā*n*j*ą*n`, `OEIUmlaut: *m*ǣ*n*j*ą*n`, `OEWeakTailReduction: *m*ǣ*n*j*a*n`, `OEJLossAfterHeavy: *m*ǣ*n*a*n`, then `OldEnglishRemoveStars: mǣnan` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:21232-21345].
- `oe_known_problems.tsv` has no reservation for row 2123, for `mǣnan`, or for `*máinijaną`; the live OE exception register currently lists unrelated exception/wontfix cases only [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure still treats the row as an uncovered regular row with no NOTE requirement trigger: `| 2123 | mean | mǣnan | regular | no | - | - | - | none |`. `report_manifest.tsv` likewise has no manifest-backed entry for row 2123 [Germanic/docs/lexeme_reports/coverage_audit.md:307-309; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].

## Development-note summary

No dedicated prose block keyed specifically to `2123 / mean / mǣnan / *máinijaną` survives in `DEV_NOTES.md`. That needs to be said plainly. The usable DEV_NOTES material for this row is instead a mix of (i) one directly relevant implementation-status table entry naming the older and newer proto shapes for this lexeme, and (ii) shared background sections explaining why heavy-stem Class I weak verbs keep PGmc `-ij-` notation and why stressed root `*ai` becomes PWGmc `*ā` before later OE developments [Germanic/docs/DEV_NOTES.md:8903-8927; Germanic/docs/DEV_NOTES.md:8763-8833; Germanic/docs/DEV_NOTES.md:13943-13975].

The row should therefore be read conservatively as a regular heavy-stem Class I weak verb whose current live protoform already incorporates the March 2026 Sievers-law notation decision. In project terms, the important surviving point is not an idiosyncratic lexical story about `mean`; it is that this lexeme was explicitly moved out of older `*mainjăną`-style notation and into heavy-stem `*-ijăną` notation, after which the grammar handles the expected `*-CijV- > *-CjV-` syncope and later OE umlaut/j-loss automatically [Germanic/docs/DEV_NOTES.md:8911-8927; Germanic/docs/DEV_NOTES.md:8795-8805; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:21294-21326].

A second distinction worth preserving is the level structure. `PROTO`/`PROTOFORM` here belong to the PGmc-facing input side and still contain the heavy-stem Class I weak `-ij-` sequence (`*máinijaną` in the live TSV; `*mainijăną` in the older DEV_NOTES notation table). The target counterpart is the attested OE infinitive `mǣnan`, after monophthongization, syncope, i-umlaut, weak-tail reduction, and `j`-loss [Germanic/data/germanic-aligned-final.tsv:749-749; Germanic/docs/DEV_NOTES.md:8925-8927; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3193-3203].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-8903-8927

- Source heading: `## Sievers' Law Implementation Status (2026-03-13)`
- Source line hint: `changes made` plus `updated forms` table
- Fragment type: `direct_row_relevant_implementation_update`
- Status: `current`
- Issue tags: `heavy_stem_class_i_weak`; `pgmc_input_notation`; `old_vs_new_proto`; `sievers_syncope`
- Recommended next use: `primary citation for why this row keeps PGmc -ij- rather than bare -j-`
- Shared-with rows if relevant: `2041; 2093; 2102; 2217; other heavy-stem Class I weak verb rows updated in the same March 2026 sweep`

This is the closest surviving DEV_NOTES material to a row-specific note. It says the grammar change added an `*-ijăną` pattern and a `SieversLawSyncope` rule, then records that the TSV was updated so that “ALL heavy-stem Class I weak verbs” now use `*-ijăną` notation [Germanic/docs/DEV_NOTES.md:8903-8913]. The row-relevant line is explicit: `| *mainjăną | *mainijăną | by analogy (CVVC heavy) |` [Germanic/docs/DEV_NOTES.md:8917-8927].

That entry should be treated as surviving direct evidence for this lexeme’s project history. It shows that the older short-suffix form `*mainjăną` was superseded inside DEV_NOTES itself, and that the reason was structural rather than semantic: the root was treated as CVVC/heavy, so the row was brought into the same heavy-stem Class I weak-verb bucket as other `-ij-` infinitives [Germanic/docs/DEV_NOTES.md:8911-8927]. The live TSV’s stress-marked `*máinijaną` is consistent with that change in structure even though the notation is now more explicit about stress than the table entry was [Germanic/data/germanic-aligned-final.tsv:749-749].

### DEV_NOTES:line-8763-8833

- Source heading: `## DECISION UPDATE (2026-03-13): Adopting PGmc Input Notation`
- Source line hint: `decision made` and `technical research` subsections
- Fragment type: `shared_policy_with_row_level_consequences`
- Status: `current`
- Issue tags: `pgmc_vs_pwgmc`; `sievers_law`; `cijv_syncope`; `infinitive_history`
- Recommended next use: `cite when explaining why PROTO/PROTOFORM retain -ij- while the OE output does not`
- Shared-with rows if relevant: `all heavy-stem Class I weak infinitive rows, especially those moved from *-jăną to *-ijăną`

This section preserves the governing policy that makes the live row intelligible. DEV_NOTES states: “we are adopting **PGmc** (Proto-Germanic) input notation, NOT PWGmc,” and immediately draws the operational consequence: “**Heavy-stem Class I weak verbs need `*-ijăną`, not `*-jăną`**” [Germanic/docs/DEV_NOTES.md:8767-8773]. It then distinguishes two phenomena that should not be collapsed: analogical leveling of stem-vowel alternation in certain present forms, and a separate sound change affecting infinitives, quoted as “the sequence `*-CijV-` was syncopated to `*-CjV-`” [Germanic/docs/DEV_NOTES.md:8778-8799].

For row 2123, that distinction is the substance. The row target is not supposed to preserve visible `-ij-` all the way to OE; rather, the PGmc-side input keeps `-ij-`, and the grammar later syncopates it. DEV_NOTES even preserves a directly parallel handbook example: `PGmc *sōkijană 'to look for, to seek' ... > PWGmc *sōkijan > *sōkjan > OE sēċan` [Germanic/docs/DEV_NOTES.md:8801-8805]. The live `*máinijaną > *mānijaną > ... > *mānjąn > *mǣnjąn > mǣnan` trace is therefore behaving exactly like the policy says a heavy-stem infinitive should behave [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3193-3203; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:21294-21326].

### DEV_NOTES:line-13943-13975

- Source heading: `### Revised analysis: Two separate changes for *ai (2026-04-06)`
- Source line hint: `chronological facts from R/T`
- Fragment type: `shared_background_for_root_vowel`
- Status: `current`
- Issue tags: `stressed_ai`; `pwgmc_monophthongization`; `chronology`; `shared_background_only`
- Recommended next use: `use for the root-vowel stage only, not for the later -ij- behavior`
- Shared-with rows if relevant: `all rows whose stressed proto root contains *ai, including dǣl- and hǣþ-type outcomes`

This fragment is not row-specific prose, but it is the cleanest surviving DEV_NOTES statement of what happens to the root diphthong in `*máinijaną`. DEV_NOTES insists that stressed and unstressed `*ai` are separate historical developments: “**PWGmc *ai → *ā (stressed)**” versus “**NWGmc *ai → *ē (unstressed)**” [Germanic/docs/DEV_NOTES.md:13949-13975]. The preserved example `PGmc *hailaz → PWGmc *hālaz → OE hāl` is not this lexeme, but the structural point carries over directly to the stressed root syllable of `*mái-` [Germanic/docs/DEV_NOTES.md:13951-13953].

For this row, the fragment’s role is narrow but important. It explains why the current derivation starts with `PWGmc Ai Monophthongization: *mānijaną` before the OE-side umlaut and `j`-loss rules ever come into play [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3193-3199]. It should be used as shared background only: it supports the `*mái- > *mā-` portion of the row, not the later heavy-stem infinitive behavior, which is governed by the separate Sievers-law material above.

## Superseded or diagnostic material

- DEV_NOTES preserves an older cleanup note that is still useful diagnostically: “Removed `OldEnglishAiMonophthongization` (never fires because WG monophthongization already rewrites `*ai → *ā`).” For row 2123, that matters because any explanation that tries to get from `*mái-` to `mǣ-` by an OE-only `ai` rule is explicitly superseded inside the notes; the monophthongization belongs earlier, before the OE umlaut stage [Germanic/docs/DEV_NOTES.md:2608-2610; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:21245-21245; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:21302-21302].
- The most obviously stale row-local artifact now lives outside the published trace docs: the sandbox JSON still contains `concept: "mean"`, `proto: "*mainjăną"`, `counterpart: "mǣnan"`, with `outputs: []`, and its staged dump eventually wanders to bad surface `mānġana` after an early failure marker [Germanic/tmp/old_english_sandbox_results_current.json:1833-1837; Germanic/tmp/old_english_sandbox_results_with_stages.json:27483-27622]. In light of the March 2026 DEV_NOTES update from `*mainjăną` to heavy-stem `*mainijăną` and the current published exact-match trace for live `*máinijaną`, that sandbox state should be treated as diagnostic residue from older notation, not as current row truth [Germanic/docs/DEV_NOTES.md:8911-8927; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3184-3203].
- No older row-specific prose argument survives beyond that notation history. There is no preserved DEV_NOTES mini-dossier arguing for a different OE target, a different derivation class, or a distinct row-specific exception status. The superseded material is chiefly about proto-input notation and stale diagnostics, not about a rejected lexical analysis of OE `mǣnan` itself [Germanic/docs/DEV_NOTES.md:8903-8927; Germanic/data/oe_known_problems.tsv:1-8].

## Open questions for later work

- If a later packet or memo is prepared, keep three forms distinct unless a source explicitly equates them: stale sandbox `*mainjăną`, DEV_NOTES implementation-table `*mainijăną`, and live stress-marked TSV `*máinijaną` [Germanic/tmp/old_english_sandbox_results_current.json:1833-1837; Germanic/docs/DEV_NOTES.md:8917-8927; Germanic/data/germanic-aligned-final.tsv:749-749].
- The repo should eventually regenerate or retire the stale sandbox artifact for this lexeme so that ad hoc row checks do not contradict the published exact-match trace [Germanic/tmp/old_english_sandbox_results_with_stages.json:27483-27622; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3184-3203].
- If fuller philological documentation is ever needed, it would have to come from external lexicographic or textual evidence for OE `mǣnan`; the surviving DEV_NOTES material is enough to document project-internal proto notation and derivational ordering, but not to replace a dedicated lexical dossier [Germanic/docs/DEV_NOTES.md:8763-8833; Germanic/docs/DEV_NOTES.md:13943-13975].
