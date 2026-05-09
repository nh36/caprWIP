---
row_id: 2025
concept: fold
counterpart: fealdan
proto: *fálθaną
protoform: *fálθaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current_shared_only
needs_literature_agent: no
---

# DEV_NOTES material — 2025 fold / fealdan

## Current row state

- CONCEPT: `fold`
- COUNTERPART: `fealdan`
- PROTO: `*fálθaną`
- PROTOFORM: `*fálθaną`
- DERIVATION_CLASS: `regular`
- Live TSV row 2025 currently gives Old English `fealdan` from `*fálθaną`; the row carries no lexeme-specific explanatory note of its own, only the generic source-history field, so the substantive support for the row has to be reconstructed from shared DEV_NOTES material rather than from a dedicated row memo [Germanic/data/germanic-aligned-final.tsv:366-369].
- `coverage_audit.md` still marks row 2025 as having no packet, no research memo, no dossier linkage, and no previously extracted DEV_NOTES slice; this replacement slice therefore has to stand in for all surviving row-level documentation [Germanic/docs/lexeme_reports/coverage_audit.md:246-248].
- The most directly relevant current diagnostic is the published OE derivation trace: `PROTO: *fálθaną`, `EXPECTED: fealdan`, `OUTPUTS: fealdan`, with the staged path `*fálθaną -> *fáldaną -> *fældaną -> *fealdaną -> fealdan` under `PWGmc L Th Voicing`, `Anglo Frisian Brightening`, `OE Breaking`, and weak-tail cleanup. That trace shows the row presently behaves as a successful regular derivation, not as an open mismatch [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1503-1517].
- No dedicated `oe_known_problems.tsv` entry was found for `*fálθaną` / `fealdan` during row-specific search. In current repo practice that absence matters: unlike rows such as `fȳre` or `tæppa`, row 2025 is not being carried as a documented exception ledger item.

## Development-note summary

No clearly row-specific DEV_NOTES subsection for `fold / fealdan` survives. The usable evidence is shared material: a general DEV_NOTES section on PWGmc `*lþ -> *ld`, a later shared chronology note on OE breaking, and a cluster inventory that explicitly classifies row 2025 as a breaking case [Germanic/docs/DEV_NOTES.md:1324-1359; Germanic/docs/DEV_NOTES.md:2575-2579; Germanic/docs/DEV_NOTES.md:30604-30623]. The slice should therefore say plainly that support is mostly shared-policy and diagnostic material, not a dedicated lexeme dossier.

The most solid inherited claim is the consonant step. DEV_NOTES treats `fold` as one of the "clear examples" where word-internal `*lþ -> *ld` is simply regular in PWGmc/NWGmc, giving `*falþaną -> *faldaną`; it further says that where this ordinary sound change already gives the right OE direction, "we use it (gold, feld, fealdan, etc.)" instead of invoking an unresolved Verner-style alternation [Germanic/docs/DEV_NOTES.md:1324-1359]. For this row, that means the consonantism should be presented as regular and already adequately covered by shared project policy.

The vowel history is also recoverable, but again mainly through shared rule notes rather than a fold-specific discussion. The breaking note says the project now aligns OE breaking as `*a/*æ -> *ea`, `*e -> *eo`, `*i -> *ie` in `rC/lC/h/w` contexts, and the later cluster inventory labels row 2025 simply `breaking` [Germanic/docs/DEV_NOTES.md:2575-2579; Germanic/docs/DEV_NOTES.md:30604-30623]. Read together with the current trace, the repo's working derivation is effectively `*fálθaną -> *fáldaną -> *fældaną -> *fealdaną -> fealdan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1510-1517]. That is enough to describe the row as regular, but it is worth remaining cautious: the preserved DEV_NOTES material does not include a fold-specific literature discussion devoted to whether the crucial OE trigger should be described as `lþ`, `ld`, or a more general post-brightening `lC` environment.

The extra analysis material is supportive but not foundational. The A-restoration research note includes row 2025 in a broader inventory of `*a/á + r/l + non-front` shapes and glosses it as `breaking before *lþ`; that is useful because it shows later project work continued to classify the row as ordinary breaking rather than as an unresolved special case, but it is still a survey table, not a row-specific argument from the handbooks [Germanic/docs/analysis/arestoration_r_l_research.md:722-733]. A conservative final report should therefore treat row 2025 as a regular success with shared-rule support, while openly noting that no richer row-specific DEV_NOTES narrative survives.

## Relevant DEV_NOTES fragments

### Fragment A — DEV_NOTES:1324-1359

- Source label: `DEV_NOTES:1324-1359`
- Source heading: `PWGmc *lþ → *ld Voicing and Verner's Law Overlap`
- Source line or section hint: `The rule`; `Clear examples`; `Scope of Verner's Law in the project`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `l_th_voicing`; `regular_sound_change`; `verner_scope`; `consonant_history`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the main surviving DEV_NOTES authority for the consonant history of row 2025. The note states, in explicit rule language, that "word-internal `*lþ → *ld` was a regular sound change in Northern WGmc (= PWGmc)," and then gives `fold` as one of the section's "clear examples": ``*falþaną → *faldaną → OE fealdan`` [Germanic/docs/DEV_NOTES.md:1324-1333]. That is unusually direct as shared material goes: even though the section is not a dedicated row memo, it names this lexeme outright and treats it as unproblematic.

The same fragment is also useful for boundary-setting. DEV_NOTES contrasts `fealdan` with genuine unresolved Verner cases and says that where the regular `*lþ -> ld` change already yields the right answer, "we use it (gold, feld, fealdan, etc.)" [Germanic/docs/DEV_NOTES.md:1349-1359]. For later report writing, that means row 2025 should not be narrated as if its `d` depended on a speculative paradigm alternation; within current project logic, the row belongs on the regular side of that divide.

### Fragment B — DEV_NOTES:2575-2579

- Source label: `DEV_NOTES:2575-2579`
- Source heading: `OE breaking reorder + diagnostics (2025-12-22)`
- Source line or section hint: `breaking chronology and rule statement`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `oe_breaking`; `chronology`; `shared_rule`; `vowel_history`
- Recommended next use: `cite_with_caution_for_row`
- Shared with row IDs: `1975; 2002; 2008; 2077; 2118; 2166; 2289; 2297`

This fragment is shared rather than lexeme-specific, but it supplies the surviving project statement for the crucial OE vowel step. DEV_NOTES says that "Breaking now precedes GH-marking and W-glide" and that the sandbox/production rule set is now aligned to Old English with `*a/*æ -> *ea`, `*e -> *eo`, `*i -> *ie` in `rC/lC/h/w` environments [Germanic/docs/DEV_NOTES.md:2575-2579]. For row 2025, that is the best surviving explanation for the transition from brightened `*fældaną` to broken `*fealdaną`.

The caution is that `fealdan` is not named in this fragment, and the examples in the adjoining diagnostic sentence are other lexemes. So this passage should be used as shared rule support, not as proof that DEV_NOTES preserved a separate fold-specific argument. Its value is chronological and methodological: it tells later readers which version of OE breaking the project means when it labels row 2025 a regular breaking outcome.

### Fragment C — DEV_NOTES:30604-30623

- Source label: `DEV_NOTES:30604-30623`
- Source heading: `Words in the TSV with proto *-aCl-* or *-aCr-* before a back-vowel tail`
- Source line or section hint: `cluster inventory table`
- Fragment type: `diagnostic_shared_inventory`
- Status: `current`
- Issue tags: `row_inventory`; `breaking_classification`; `shared_diagnostic`; `not_row_specific`
- Recommended next use: `use_as_classification_support`
- Shared with row IDs: `1975; 2002; 2008; 2030; 2050; 2052; 2077; 2118; 2166; 2167; 2289; 2297`

This inventory occurs inside another investigation, not inside a `fold` note, but it still matters because it shows how row 2025 was being classified in later cross-row work. The table of OE rows with proto `*aCl/*aCr` shape includes the entry `| 2025 | *fálθaną | fealdan | breaking |` [Germanic/docs/DEV_NOTES.md:30606-30623]. That tells us that by this stage the project considered row 2025 part of the breaking cluster set, not part of the A-restoration problem that motivated the section.

The fragment is therefore diagnostic rather than argumentative. It does not add new philology beyond the label `breaking`, and it should not be made to carry more weight than that. Still, it is useful because it corroborates the other shared evidence: when DEV_NOTES surveys potentially affected rows, `fealdan` continues to sort with regular breaking forms.

## Superseded or diagnostic material

No clearly superseded row-specific DEV_NOTES section for `fold / fealdan` appears to survive. Unlike rows that were repeatedly re-analysed, row 2025 mostly shows up in stable shared-rule notes and later diagnostics. The main consequence is practical rather than interpretive: there is little old row-specific prose to preserve, but also little evidence of abandoned analyses that need to be warned off.

Two non-DEV_NOTES items are still worth retaining as diagnostics. First, the analysis inventory in `arestoration_r_l_research.md` lists row 2025 as `breaking before *lþ`, confirming that later repo work kept treating the row as an ordinary member of the broader `a + liquid` breaking set rather than as a special exception [Germanic/docs/analysis/arestoration_r_l_research.md:722-733]. Second, the published OE derivation trace gives the actual current path `*fálθaną -> *fáldaną -> *fældaną -> *fealdaną -> fealdan`, which is the clearest evidence that the live analyzer already reaches the target successfully [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1503-1517].

The coverage audit is also diagnostic of documentation state. It records row 2025 as having `no` packet, `-` for memo/dossier links, and `none` under extracted note status [Germanic/docs/lexeme_reports/coverage_audit.md:246-248]. That does not say anything new about the historical derivation itself, but it explains why this slice has to be explicit about the absence of surviving row-specific DEV_NOTES substance.

## Open questions for later work

- If a later literature pass wants stronger row-specific support, look for handbook discussion that explicitly addresses OE breaking in forms of the `fealdan` type after PWGmc `*lþ -> *ld`; the present slice relies mostly on shared project notes plus the current trace.
- If a future packet or research memo is created, keep the distinction clear between what is strongly supported here (regular `*lþ -> *ld`, regular OE breaking, successful current output) and what is only inferred from shared-rule context (the exact philological phrasing of the conditioning cluster).
- If later debugging ever causes row 2025 to fail again, compare against the existing trace before reopening the historical analysis: the current published diagnostic already shows the row succeeding through voicing, brightening, breaking, and weak-tail cleanup [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1503-1517].
