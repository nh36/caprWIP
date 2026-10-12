---
row_id: 1942
concept: beech
counterpart: bōc
proto: *bōkō
protoform: *bōkō
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/1942-beech-bōc.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/1942-beech-bōc.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1942 beech / bōc

## Current row state

- CONCEPT: `beech`
- COUNTERPART: `bōc`
- PROTO: `*bōkō`
- PROTOFORM: `*bōkō`
- DERIVATION_CLASS: `regular`
- Live TSV note: `Kroonen *bōk(j)ō- f. > OE bōc (nom.sg.); bēċe is oblique form.` [@Kroonen2013, p. 72]

## Development-note summary

The live row now treats `*bōkō -> bōc` as a regular nominative-singular outcome, and the note on the row already separates that target from the wider lexeme-family material. Kroonen's comparative entry gives `*bōk(j)ō-` as the etymological headword and lists Old English `boc, bēce` together under the beech lexeme [@Kroonen2013, p. 72], but the aligned TSV narrows the present row to nominative `bōc` and treats `bēċe` only as oblique-form background. That distinction is essential here: regular comparator `bōc`, related attested paradigm material `bēċe`, and superseded project target `bēċe-from-*bōkō` are not the same claim.

DEV_NOTES still matters because earlier OE debugging mixed those levels. The first explicit row-level failure note, DEV_NOTES:line-1715-1725, put `*bōkō` in `palatalization_missing`: the trace gave `bōcō`, the expected form was `bēċe`, and the note observed that no fronting stage had created the front-vowel context needed for palatalization. That fragment is no longer current row policy, but it preserves the abandoned project detour exactly: the system was once being asked to derive an oblique-style palatalized form directly from the row input `*bōkō`.

The later OE bucket audit corrected that diagnosis without yet changing the row target. DEV_NOTES:line-2588-2593 says the surviving `palatalization_missing` items were not genuine palatalization-rule failures, because the front-vowel context was absent upstream; `*bōkō` is named among the cases where fronting or breaking would have to create the trigger first. The companion subgroup snapshot at DEV_NOTES:line-2595-2605 keeps the concrete mismatch `*bōkō -> bucō` vs `bēċe`. Those fragments therefore remain useful as chronology: they supersede the crude “missing palatalization rule” story, but they still belong to the older phase in which `bēċe` was treated as the row-level expectation.

The current sound-change point that survives into the live row is different. DEV_NOTES:line-1762-1767 states that “OE ō before velars should stay long” and uses `bōc/bōg` as the comparator. Together with DEV_NOTES:line-20574-20578, which uses `*bōkō` as the model example for an unstressed long inflectional vowel, this gives the present row its technical baseline: the row input really is `*bōkō`, the final `ō` notation is intentional, and the regular OE output for the nominative-singular row is `bōc`, not a shortened `buc` and not the oblique/palatalized `bēċe`.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-20574-20578

Source heading: `inventory note on unstressed long-vowel notation`  
Source line or section hint: lines 20574-20578  
Status: current  
Issue tags: protoform_notation; unstressed_long_vowel; row_input  
Recommended use: cite_in_final_report  
Shared with row IDs:
Text or paraphrase:
This fragment is a small but current guardrail for the row input itself. DEV_NOTES lists `*bōkō` as the example for “unstressed long vowel in inflection,” which confirms that the second `ō` in the live `PROTOFORM` is deliberate notation rather than an accenting mistake. Later report work should keep that point explicit, because the row's present regular analysis depends on reading `*bōkō` exactly as the model input that apocopates to `bōc`.

### DEV_NOTES:line-1715-1725

Source heading: `Concrete “rule not firing” evidence (2026-02-01 trace)`  
Source line or section hint: lines 1715-1725  
Status: superseded  
Issue tags: palatalization_missing; target_mismatch; chronology  
Recommended use: use_to_explain_superseded_analysis  
Shared with row IDs:
Text or paraphrase:
This is the clearest surviving note from the old mismatch phase. It records `*bōkō` under `palatalization_missing`, gives the actual trace output `bōcō` against expected `bēċe`, and already suspects that the problem may be “rule/chronology or etymon/expected mismatch” rather than a simple one-rule bug. The fragment is superseded because the live row no longer targets `bēċe`, but it should be preserved so later writers can see exactly how the obsolete row expectation entered the project history.

### DEV_NOTES:line-1762-1767

Source heading: `Long-vowel-missing deep dive (2026-01-02)`  
Source line or section hint: lines 1762-1767  
Status: current  
Issue tags: long_vowel_preservation; regular_comparator; vowel_quantity  
Recommended use: cite_in_final_report  
Shared with row IDs:
Text or paraphrase:
This fragment is the current phonological guardrail that still matters directly for row 1942. DEV_NOTES says “OE ō before velars should stay long” and gives `bōc/bōg` as the example. For this slice that matters less as a repair proposal than as a statement of the regular comparator: once the row is kept on nominative `bōc`, the expected OE outcome is the long-vowel form before velar `c`, not a shortened reflex.

### DEV_NOTES:line-2588-2593

Source heading: `OE palatalization vs fronting/umlaut split (2025-12-23)`  
Source line or section hint: lines 2588-2593  
Status: diagnostic_only  
Issue tags: upstream_context; fronting_missing; palatalization_reanalysis  
Recommended use: use_to_explain_superseded_analysis  
Shared with row IDs:
Text or paraphrase:
This fragment partly corrects the older `palatalization_missing` label. It says the seven remaining cases were not true palatalization-rule failures, because the front-vowel environment never arose, and it names `*bōkō` among the rows that would need upstream fronting or breaking changes before palatalization could even be expected. The note is still diagnostic rather than current policy for row 1942, but it is the key correction that turns the old story from “missing palatalization pass” into “missing front-vowel trigger.”

### DEV_NOTES:line-2595-2605

Source heading: `OE i-umlaut/fronting bucket diagnostics (2026-01-01)`  
Source line or section hint: lines 2595-2605  
Status: diagnostic_only  
Issue tags: diagnostic_snapshot; fronting_bucket; obsolete_expected_form  
Recommended use: use_to_explain_superseded_analysis  
Shared with row IDs:
Text or paraphrase:
The subgroup snapshot keeps the later concrete mismatch state in one line: `*bōkō -> bucō` versus expected `bēċe`. That makes it useful chronology even though it is no longer live evidence. The fragment shows that the project had moved beyond the earlier `bōcō` trace but was still evaluating the row against the obsolete palatalized/oblique comparator, so later reports should use it only to document the superseded debugging path.

## Superseded or diagnostic material

The superseded phase here is not a different proto-etymology but a different expectation about which Old English paradigm form the row should target. Older DEV_NOTES fragments treated `bēċe` as the row-level expected outcome and then tried to explain why palatalization or upstream fronting had failed to produce it from `*bōkō`. The live row resolves that tension by keeping `*bōkō -> bōc` as the regular nominative-singular path and demoting `bēċe` to related paradigm background.

## Open questions for later work

- If the final lexeme report mentions `bēċe`, keep the wording cautious unless a separate paradigm source is added; the current row note only guarantees that it is an oblique form, not which exact cell should headline the report.
- Warn explicitly against conflating row 1942 `bōc` ‘beech’ with row 1955 `bōc` ‘book’; the homograph risk is real even though it is not the row's main sound-change issue.
- If later paradigm work uses project-internal probes such as `*bōkjō` or `*bōkjōz`, keep those probes clearly separate from the live row target `*bōkō -> bōc`.
