---
row_id: 2046
concept: grave
counterpart: grafan
proto: *grábaną
protoform: *grábaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2046-grave-grafan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2046-grave-grafan.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2046 grave / grafan

## Current row state

- CONCEPT: `grave`
- COUNTERPART: `grafan`
- PROTO: `*grábaną`
- PROTOFORM: `*grábaną`
- DERIVATION_CLASS: `regular`
- Live TSV note (quoted closely): `OE target: græf→græfan (inf. of str.v. class VI 'to dig, grave') | OE target: grafan (not græfan); Hogg §5.3.1, Hall s.v. grafan. Proto encoding: -aną for A-restoration; R/T §6.3.1.` The second clause matches the live row policy, but the opening `græf→græfan` wording is stale and conflates the verb row with separate noun material; the research memo explicitly flags that as misleading [Germanic/data/germanic-aligned-final.tsv:450; Germanic/docs/lexeme_reports/research_memos/2046-grave-grafan.md:11-20, 76-86].
- Packet / memo state: the packet's compact derivation already outputs `grafan`, with Anglo-Frisian brightening followed by OE A-restoration before the infinitival tail; the memo likewise treats the row as a settled verbal infinitive row whose main remaining problem is stale note wording, not unresolved phonology [Germanic/docs/lexeme_reports/packets/2046-grave-grafan.md:17-42; Germanic/docs/lexeme_reports/research_memos/2046-grave-grafan.md:13-20, 57-66].
- `oe_known_problems.tsv`: no row-local entry for `2046`, `*grábaną`, `*grabaną`, `grafan`, or `græf`; absence there is bookkeeping only, not contrary lexical evidence [Germanic/data/oe_known_problems.tsv:1-9].
- `report_manifest.tsv`: no manifest entry for this row, so this slice has to function as the replacement working note for the row's DEV_NOTES material [Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].

## Development-note summary

This row does have securely attachable DEV_NOTES authority, but most of it survives as **shared Class VI / A-restoration material plus one exact row inventory line**, not as a long grafan-only discussion. That is still enough for normal workflow, because all surviving current notes point in the same direction: row 2046 is the regular strong-verb infinitive `grafan` from live input `*grábaną`, and the relevant phonological issue is ordinary OE A-restoration before the back-vocalic infinitive tail, not any special exception status [DEV_NOTES:line-21738-21749; DEV_NOTES:line-30604-30620; Germanic/data/germanic-aligned-final.tsv:450].

The philological baseline should stay explicit because the English gloss *grave* is lexically ambiguous. The row target is the **verb** `grafan` 'to dig, grave', not the noun `græf` 'grave, trench'. The memo is right to preserve that warning, since the live TSV note still opens with the stale formulation `græf→græfan`, while the row itself, the packet, and the later note all converge on infinitive `grafan` [Germanic/docs/lexeme_reports/research_memos/2046-grave-grafan.md:13-20, 46-66, 76-86; Germanic/docs/lexeme_reports/packets/2046-grave-grafan.md:5-10, 17-42]. No DEV_NOTES fragment argues for `græfan` as the row target; the only durable DEV_NOTES material treats `grafan` as a textbook restored-`a` infinitive.

The clearest surviving current-policy DEV_NOTES note is the April empirical probe on Class VI strong verb infinitives. It contrasts `*bákăną` → `bæcan` with `*bákaną` → `bacan`, then states that the ten Class VI verbs including `grábaną` rely on **plain suffix `a`**, because `OEARestorationTriggerVowel` includes `{*a}` but not `{*ă}` [DEV_NOTES:line-21738-21749]. For row 2046 this means the current live `PROTOFORM = *grábaną` is not an arbitrary legacy spelling. It is the explicit row policy needed to get regular `grafan`; the earlier breve-marked workaround belongs to superseded project chronology, not to current row description.

DEV_NOTES also preserves the superseded detour clearly enough that later writers should not rediscover it. In March 2026 the project temporarily rewrote strong verb infinitives from `-aną` to `-ăną`, including `*grabaną → *grabăną`, and the targeted output improved to `grabăną → grafan ✓ (was græfen)` [DEV_NOTES:line-9497-9539]. But the same fragment immediately marks the approach as a failure, because admitting `{*ă}` as an A-restoration trigger caused broad regressions in unrelated rows such as `craft`, `dag`, and `mast` [DEV_NOTES:line-9520-9553]. For row 2046, therefore, `*grabăną` is important only as superseded debugging history.

The later chronology repair is the note that turns the right output into current policy rather than a brittle workaround. DEV_NOTES' March 14 results list `*grafaną → grafan ✓ (was græfen)` among the repaired strong verb infinitives, then explains that infinitives and participles must be distinguished by their original suffix structure: infinitival `*-aną` keeps the nasal in coda position early enough for secondary nasalization to block fronting, whereas participial `*-anăz` does not, so participles still surface with `-en` [DEV_NOTES:line-10083-10205]. The follow-up remark “The nasalization fix ... was tested on **infinitives** (which worked correctly: `bacan`, `grafan`, `wadan`, etc.)” is especially useful here because it shows that `grafan` is part of the repaired regular infinitive behavior, not a row-specific exception [DEV_NOTES:line-10202-10205].

The handbook-facing DEV_NOTES material is equally stable and should be quoted directly when this row is written up elsewhere. Campbell's canonical statement is preserved twice in DEV_NOTES, once as a direct quotation and once in the later literature-consensus table: “The restoration of *a* is common before all single consonants and geminates, e.g. *faran* go, *calan* be cold, *bacan* bake, *gnagan* gnaw, *grafan* dig ...” [DEV_NOTES:line-22573-22576; DEV_NOTES:line-36524-36533; @Campbell1959, §158]. DEV_NOTES then makes the row-local application completely explicit in the later inventory of OE rows with `*-aCl-*` or `*-aCr-*` before a back-vowel tail: `| 2046 | *grábaną | grafan | single *b*, A-restoration fires correctly |` [DEV_NOTES:line-30604-30620]. That exact line is the most secure row-specific DEV_NOTES authority surviving for 2046.

The smaller current verification note at `DEV_NOTES:line-3138-3151` is also worth keeping attached to this row. It records a later trigger-set cleanup and then reports: “All A-restoration-dependent forms verified: bacan, wadan, wascan, hlaþan, grafan, ġeall, hamer all correct.” That matters because it confirms that `grafan` remained stable after the trigger logic was narrowed again; the row does not depend on the discarded `{*ă}` workaround or on a stale over-broad trigger definition [DEV_NOTES:line-3138-3151].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-9497-9542

- Source heading: `Changes made / Results / Analysis: Why the Fix Fails`
- Source line or section hint: `lines 9497-9542`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `breve_workaround`; `class_vi_infinitives`; `a_restoration_trigger_set`; `regression_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs: `1934, 2266, 2268, 2272, 2292`

This fragment records the abandoned `-ăną` workaround in the exact form later report writers are most likely to need. DEV_NOTES says the FST was changed so `{*ă}` counted as a back-vowel trigger and the TSV strong-verb infinitives were rewritten, including `*grabaną → *grabăną`; the targeted results then improved to `grabăną → grafan ✓ (was græfen)` [DEV_NOTES:line-9497-9513]. But the same note immediately marks the experiment as a failure because the trigger-set expansion over-applied A-restoration across the lexicon, yielding regressions such as `kraftăz → craft`, `dagăz → dag`, and `mastăz → mast` [DEV_NOTES:line-9520-9542]. For row 2046 this is valuable only as superseded project chronology.

### DEV_NOTES:line-10083-10205

- Source heading: `Results / Why This Works / Why This Wasn't Caught Earlier`
- Source line or section hint: `lines 10083-10205`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `chronology_fix`; `infinitive_vs_participle`; `secondary_nasalization`; `verification_history`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1934, 2266, 2268, 2272`

This is the main current phonological explanation to keep with the row. DEV_NOTES lists `*grafaną → grafan ✓ (was græfen)` among the repaired strong-verb infinitives, then explains why the repaired chronology distinguishes infinitives from participles: infinitival `*-aną` is nasalized in the right structural position, so fronting is blocked and `-an` survives, whereas participial `*-anăz` still develops `-en` [DEV_NOTES:line-10083-10201]. The final remark that the fix had already been tested on infinitives “which worked correctly: `bacan`, `grafan`, `wadan`, etc.” makes the fragment row-relevant even though the note is shared across several verbs [DEV_NOTES:line-10202-10205].

### DEV_NOTES:line-21738-21749

- Source heading: `A. Empirical probes (stems with root *á, Class VI strong verb infinitives)`
- Source line or section hint: `lines 21738-21749`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `current_row_policy`; `protoform_encoding`; `class_vi_infinitives`; `a_restoration`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1934, 2088, 2266, 2268, 2272`

This fragment is the best current-policy authority for the live protoform. DEV_NOTES contrasts `*bákăną` → `bæcan` with `*bákaną` → `bacan`, then states that the Class VI strong verbs including `grábaną` rely on **plain** infinitival `a` because `OEARestorationTriggerVowel` includes `{*a}` but not `{*ă}` [DEV_NOTES:line-21742-21749]. Even though `grafan` is not spelled out in the probe table itself, the prose explicitly names `grábaną` among the governed verbs, so this fragment should be cited whenever the final row write-up needs to justify why the live row keeps `*grábaną` instead of the older `*grabăną` experiment.

### DEV_NOTES:line-36524-36533

- Source heading: `The canonical conditioning of A-restoration (literature consensus)`
- Source line or section hint: `lines 36524-36533`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `handbook_consensus`; `literature_quote`; `regular_comparator`; `a_restoration`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1934, 2003`

This literature table is the most reusable compact handbook fragment for row 2046. It preserves Campbell's quotation in exactly the form later notes should keep: “The restoration of *a* is common before all single consonants and geminates, e.g. ... *grafan* dig ...” and pairs it with Ringe-Taylor's rule that stressed `*æ` before a single or geminate consonant or `sC` cluster followed by a back vowel became `a` [DEV_NOTES:line-36529-36533; @Campbell1959, §158; @RingeTaylor2014, §6.3.1]. For this row the value is straightforward: `grafan` is not merely compatible with the general rule; it is one of the handbook examples of that rule.

### DEV_NOTES:line-30604-30620

- Source heading: `Words in the TSV with proto *-aCl-* or *-aCr-* before a back-vowel tail`
- Source line or section hint: `lines 30604-30620`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `row_exact_inventory`; `a_restoration`; `single_consonant_environment`; `row_policy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the surviving exact-pair DEV_NOTES fragment for the row itself. In the inventory of OE rows with `*-aCl-*` or `*-aCr-*` before a back-vowel tail, DEV_NOTES gives row 2046 explicitly: `| 2046 | *grábaną | grafan | single *b*, A-restoration fires correctly |` [DEV_NOTES:line-30609-30620]. That sentence-length table entry matters because it converts the broader handbook rule into direct row-local policy: the relevant conditioning is **single intervening `*b`**, so there is no liquid-blocking or cluster problem to solve here.

### DEV_NOTES:line-3138-3151

- Source heading: `Fix / Derivation / Impact`
- Source line or section hint: `lines 3138-3151`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `trigger_set_correction`; `verification_history`; `a_restoration`; `post_fix_validation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1934, 2088, 2266, 2272`

This verification fragment is brief but still useful. DEV_NOTES tightens the trigger set to genuine back vowels and then reports: “All A-restoration-dependent forms verified: bacan, wadan, wascan, hlaþan, grafan, ġeall, hamer all correct” [DEV_NOTES:line-3140-3151]. For row 2046 that confirms that `grafan` remained correct after later cleanup of the trigger logic, so the present row is supported by the repaired general system rather than by a one-off exception patch.

## Superseded or diagnostic material

The main superseded material for this row is **not** a competing philological claim that OE infinitive `græfan` is correct. What DEV_NOTES actually preserves as superseded is a project-debugging path: first `græfen` as the wrong infinitival output, then `*grabăną` as a temporary workaround that forced `grafan`, then the later repaired chronology that restored `grafan` under regular `*grábaną`/`*grafaną` handling [DEV_NOTES:line-9497-9542; DEV_NOTES:line-10083-10205]. The stale `græf→græfan` wording now surviving in the live TSV note belongs in the same diagnostic bucket, but it is TSV/memo history rather than surviving DEV_NOTES authority [Germanic/data/germanic-aligned-final.tsv:450; Germanic/docs/lexeme_reports/research_memos/2046-grave-grafan.md:13-20, 48-66, 76-86].

## Open questions for later work

- If row-level note cleanup is later allowed, remove the stale `græf→græfan` clause from the TSV note so the row no longer blurs noun `græf` with verb `grafan` [Germanic/data/germanic-aligned-final.tsv:450; Germanic/docs/lexeme_reports/research_memos/2046-grave-grafan.md:80-86].
- If a final lexeme report wants one compact authority for the target form, prefer the row-exact inventory line `single *b*, A-restoration fires correctly` together with the Campbell quotation naming `grafan` directly [DEV_NOTES:line-30604-30620; DEV_NOTES:line-36524-36533].
- If later Class VI rows are sliced together, keep the chronology explicit: wrong `græfen` output, then discarded `*grabăną` workaround, then restored plain-`a` policy under the repaired chronology [DEV_NOTES:line-9497-9542; DEV_NOTES:line-10083-10205; DEV_NOTES:line-21738-21749].
