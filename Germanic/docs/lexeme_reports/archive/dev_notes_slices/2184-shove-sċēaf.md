---
row_id: 2184
concept: shove
counterpart: sċēaf
proto: *skéubaną
protoform: *skáub
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2184-shove-sċēaf.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2184-shove-sċēaf.md
linked_dossier_or_analysis_files: Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md; Germanic/docs/dossiers/bugun-scufun-attestation.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2184 shove / sċēaf

## Current row state

- The live OE row now reads `CONCEPT = shove`, `COUNTERPART = sċēaf`, `PROTO = *skéubaną`, `PROTOFORM = *skáub`, `DERIVATION_CLASS = late_analogy`, with the TSV note explicitly saying that the row is the **1/3 sg. preterite** of `sċūfan`, retargeted away from older `*skúbun → sċufon`, because `sċēaf` is the genuinely Lautgesetzlich and corpus-attested cell while the infinitive `sċūfan` has analogical `ū` back-formed from the singular-preterite stem [Germanic/data/germanic-aligned-final.tsv:985-985].
- `PROTO` and `PROTOFORM` are intentionally **not** the same layer. `*skéubaną` is the cognate-set / lexical headword for the verb ‘shove’; older DEV_NOTES and dossier passages often write the same infinitive-layer headword as `*skeubăną`, which is a notation-layer difference in older project spelling, not a different paradigm cell [Germanic/data/germanic-aligned-final.tsv:985-985; Germanic/docs/DEV_NOTES.md:14363-14365; Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:273-279]. `*skáub`, by contrast, is not a notation variant of the infinitive at all: it is the PGmc **1/3 sg. preterite** cell selected as the row-level derivational input [Germanic/data/germanic-aligned-final.tsv:985-985; Germanic/docs/DEV_NOTES.md:43964-43966].
- The packet and research memo already agree with the live row state: both treat `*skéubaną` as the cognate-set proto headword, `*skáub` as the selected paradigm-cell protoform, and `sċēaf` as the attested OE target, while preserving older `*skúbun → sċufon` material only as superseded project history [Germanic/docs/lexeme_reports/packets/2184-shove-sċēaf.md:5-42; Germanic/docs/lexeme_reports/research_memos/2184-shove-sċēaf.md:3-25].
- `oe_known_problems.tsv` has no surviving row-specific exception entry for `2184`, for `shove`, or for `sċēaf`; that is consistent with the present state of the row, because the retargeting was meant to remove the live mismatch rather than to preserve it as an active known-problem item [Germanic/data/oe_known_problems.tsv:1-8].
- `coverage_audit.md` still inventories `2184 | shove | sċēaf | late_analogy` as uncovered (`- | - | -`), so the audit is stale relative to the now-existing packet, memo, and this slice; that stale audit state is diagnostic infrastructure lag, not evidence against the live row analysis [Germanic/docs/lexeme_reports/coverage_audit.md:132-132].
- The published derivation traces now match the row exactly. The compact publish snapshot gives `PROTO: *skáub`, `EXPECTED: sċēaf`, `OUTPUTS: sċēaf`, and the full trace shows the active ordered steps `OEAuFronting: *skáeub`, `OEDiphthongLeveling: *skēab`, `PGmcBAllophony: *skēaβ`, `OESkPalatalization: *ʃēaβ`, `OldEnglishOrthography: *sċ*ēa*β`, `OldEnglishRemoveStars: sċēaf` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7483-7502; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28076-28189].

## Development-note summary

The live row is correctly read as a **paradigm-cell retarget**, not as a direct derivation of the ordinary citation infinitive. The cognate-set headword remains `PROTO = *skéubaną`, i.e. the inherited class-II strong verb ‘to shove’; older DEV_NOTES prose often writes the same infinitive-layer form as `*skeubăną`, and handbook material also cites OE present-system forms such as `scēofan`, `scūfan`, or Ringe–Taylor's normalized `sciifan` [Germanic/data/germanic-aligned-final.tsv:985-985; Germanic/docs/DEV_NOTES.md:14363-14365,14420-14424; docs/references/ringe_taylor_linguistic_history_vol2.txt:3042-3043; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:23015-23020]. None of those are competing row targets. They are the citation-form layer of the verb's present system. The live `PROTOFORM = *skáub` is a genuinely different ablaut cell, namely the PGmc singular preterite, and the live OE target `sċēaf` is the corresponding attested singular preterite outcome [Germanic/docs/DEV_NOTES.md:43964-43966; Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:280-283,314-320].

DEV_NOTES first reached this row through the class-II `eu/ū` problem. In its April 2026 analysis it explicitly set out the mismatch `*skeubăną → sċēofan` versus attested `sċūfan`, then copied the standard handbook explanation that the `ū` present is analogical, not a regular PGmc→OE sound-law output. The preserved quotation from Ringe–Taylor is that “a considerable group of verbs have *ū instead of *ēo in the present system,” with `būgan` and `scūfan` named among them; Campbell is quoted to the same effect [Germanic/docs/DEV_NOTES.md:14358-14365,14372-14405]. This matches the external handbook record: Ringe–Taylor contrasts OE `sciifan` with Gothic `afskiuban` and OHG `skioban`, and Kroonen explicitly gives the pair `*skeuban- ~ *skūban-`, i.e. inherited `eu` beside the later `ū` present-system remodelling [docs/references/ringe_taylor_linguistic_history_vol2.txt:3042-3043; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:23015-23020]. For row policy, that means the infinitive `sċūfan` cannot be treated as the clean Lautgesetzlich target even though it is the ordinary dictionary headword.

The project's first repair was to switch away from the analogical infinitive and onto the older 3pl preterite `*skúbun → sċufon`. That earlier state is worth preserving because it was not random: at the time, FST inversion showed `*skubun → sċufon`, and DEV_NOTES therefore announced the issue resolved by using the past plural instead of the infinitive [Germanic/docs/DEV_NOTES.md:14458-14513]. But §17.51.A1 later changed the phonological understanding of exactly this environment. Once widow-related stem-`u` harmony blocking was restored, the regular FST output for that plural cell became `sċufun`, not `sċufon`, because `-un > -on` is blocked after stressed stem `u` plus a single consonant in the environment these verbs occupy [Germanic/docs/DEV_NOTES.md:43943-43958; Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:137-176]. The companion attestation dossier then makes the philological consequence explicit: `sċufun` is **not** attested for this lexeme, while the corpus gives only later or levelled `-on` forms such as `scufon`, `bescufon`, `āsceáfon`, `sceufon`, and Northumbrian `scyufon`, all still with `-on` [Germanic/docs/dossiers/bugun-scufun-attestation.md:144-218]. So the older 3pl target survives only as a diagnostic stage in project history, not as current row policy.

The decisive row-specific note is the later paradigm-cell review in DEV_NOTES §17.51.A1.4. That note says the full survey found **two** cells for `sċūfan` that are both Lautgesetzlich and securely attested: 1/3 sg. pret. `*skáub → sċēaf` and past participle `*skúbanaz → sċofen` [Germanic/docs/DEV_NOTES.md:43960-43970]. The review then states why the row prefers `sċēaf`: the singular preterite is “the morphological pivot on which the analogical *ū-present is itself built,” it requires the fewest cascade rules, and it is attested in canonical poetic and prose loci [Germanic/docs/DEV_NOTES.md:43972-43977]. The companion dossier makes that practical by listing the paradigm `sċūfan / sċēaf / sċufon / sċofen`, quoting Bosworth-Toller citations such as “Hé hit **āsceaf** fram his mūðe, Hml. Th. ii. 254, 17” and “**Sceaf** þā mid þām scylde, þæt se sceaft tōbærst, Byrhtnoth,” and noting that Clark Hall and Bright both cite the same principal parts [Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:285-310; docs/references/sweet_anglo_saxon_primer.txt:1890-1894; docs/references/bright_anglo_saxon_reader.txt:16515-16516,24592-24594]. The result is that `sċēaf` is not a workaround invented to rescue the row; it is the attested paradigm cell that best matches the project's phonological modelling policy.

The live trace confirms that the current row is now mechanically clean. Starting from selected `PROTOFORM *skáub`, the grammar applies `OEAuFronting` and `OEDiphthongLeveling` to reach `*skēab`, then `PGmcBAllophony` produces final `*β`, and `OESkPalatalization` gives initial `*ʃ`, after which the orthographic layer yields `sċēaf` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28120-28147,28186-28189]. The row note compresses this as “*au > ēa, *sk- > sċ-, *-b- final devoicing > -f” [Germanic/data/germanic-aligned-final.tsv:985-985], and the trace shows exactly where those pieces live in the current cascade. This is a materially different evidentiary state from the older `sċufon` row: the selected cell is now both live-FST exact and philologically secure.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-14356-14513

Source heading: class-II `eu/ū` mismatch analysis and first paradigm-cell retargeting  
Source line or section hint: lines 14356-14513  
Fragment type: superseded_or_diagnostic_for_lexeme  
Status: superseded  
Issue tags: analogical_present;paradigm_cell;project_history;protoform_vs_proto  
Recommended next use: use_to_explain_superseded_analysis  
Shared with row IDs: 1962  
Text or paraphrase:
This older DEV_NOTES block still matters because it preserves the project's first correct diagnosis of the problem. It explicitly contrasts regular infinitive-level `*skeubăną → sċēofan` with attested `sċūfan`, then quotes Ringe–Taylor and Campbell on the analogical `ū`-present in class II verbs rather than treating the mismatch as a missing sound law [Germanic/docs/DEV_NOTES.md:14358-14405]. It then records the first attempted solution — retargeting row 2184 to `*skubun → sċufon` — because, at that April 2026 stage, the FST still appeared to make the 3pl preterite the first regular escape cell [Germanic/docs/DEV_NOTES.md:14458-14513]. The analysis is superseded as row policy, but it remains necessary history because it explains why older packet and dossier material still talks about `sċufon`.

### DEV_NOTES:line-1455-1464

Source heading: research-phase completion recap for the bow/shove retargeting  
Source line or section hint: lines 1455-1464  
Fragment type: copied_shared_lexeme_fragment  
Status: current  
Issue tags: project_history;paradigm_cell;row_policy;attestation  
Recommended next use: cite_in_final_report  
Shared with row IDs: 1962  
Text or paraphrase:
The April-30 project-status recap is brief but authoritative about final state. DEV_NOTES says the widow-related research thread ended by retargeting the bow/shove rows “from 3pl pret. (analogical overlay) to 1/3 sg pret. (genuinely Lautgesetzlich + universally attested: `*báug → bēag`, `*skáub → sċēaf`)” [Germanic/docs/DEV_NOTES.md:1460-1464]. For row 2184, this is the compact statement that the repo's settled policy is now `sċēaf`, not the older `sċufon` stopgap.

### DEV_NOTES:line-43937-43959

Source heading: origin of the older `*skúbun → sċufon` row and why it stopped working  
Source line or section hint: lines 43937-43959  
Fragment type: copied_shared_lexeme_fragment  
Status: current  
Issue tags: project_history;u_harmony;paradigm_cell;analogical_overlay  
Recommended next use: cite_in_final_report  
Shared with row IDs: 1962  
Text or paraphrase:
This fragment is the key to understanding why the older row was not merely reverted on taste grounds. DEV_NOTES says the 3pl choice for row 2184 was made because it was “the first paradigm cell that mapped regularly through the FST as it stood at the time,” but adds that the later widow-driven stem-`u` harmony block invalidated that result: with the corrected phonology in place, `*skúbun` now yields regular `sċufun`, not attested `sċufon` [Germanic/docs/DEV_NOTES.md:43943-43958]. That is exactly the point confirmed by the separate attestation dossier, which shows `sċufon`/`scyufon` in the corpus but no `sċufun` for this verb [Germanic/docs/dossiers/bugun-scufun-attestation.md:177-218]. For later reporting, this fragment is current and central, because it states why the plural cell ceased to be defensible.

### DEV_NOTES:line-43960-43998

Source heading: paradigm-cell survey, preference for `sċēaf`, and final implementation  
Source line or section hint: lines 43960-43998  
Fragment type: copied_shared_lexeme_fragment  
Status: current  
Issue tags: row_policy;attestation;protoform_vs_proto;late_analogy  
Recommended next use: cite_in_final_report  
Shared with row IDs: 1962  
Text or paraphrase:
This is the decisive replacement-note fragment for the live row. DEV_NOTES says the completed survey found two clean and attested cells for `sċūfan`: 1/3 sg. pret. `*skáub → sċēaf` and past ptcp. `*skúbanaz → sċofen` [Germanic/docs/DEV_NOTES.md:43960-43970]. It then explains why the singular preterite is preferred: it is the morphological pivot behind the analogical `ū`-present, it requires the fewest cascade steps, and it appears in canonical loci where the participle does not [Germanic/docs/DEV_NOTES.md:43972-43977]. The decision lines then make the row-level consequence explicit — row 2184 is retargeted from `*skúbun → sċufon` to `*skáub → sċēaf` — and the closing implementation note records that the row has been upgraded from an analogical-overlay workaround to a “genuinely Lautgesetzlich + corpus-attested” target, with direct FST verification [Germanic/docs/DEV_NOTES.md:43979-43990].

## Superseded or diagnostic material

The superseded material is the whole older idea that row 2184 should be anchored on the past plural `*skúbun → sċufon`. That idea was useful as an intermediate diagnosis because it correctly abandoned the analogical infinitive `sċūfan`, but it depended on an FST state from before the widow research restored stem-`u` harmony blocking. After that correction, the truly regular plural output is `sċufun`, while the corpus keeps only analogical or levelled `-on` forms (`scufon`, `bescufon`, `āsceáfon`, `sceufon`, Northumbrian `scyufon`) for this lexeme [Germanic/docs/DEV_NOTES.md:43943-43958; Germanic/docs/dossiers/bugun-scufun-attestation.md:152-218].

The citation-form material `sċūfan / scēofan / sciifan` is also diagnostic rather than row-defining here. It remains essential for explaining the `late_analogy` label and for showing what was analogically remodelled in OE, but it should not be allowed to collapse the row's distinction between lexical headword and selected paradigm cell [Germanic/docs/DEV_NOTES.md:14358-14513; docs/references/ringe_taylor_linguistic_history_vol2.txt:3042-3043; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:23015-23020]. Likewise the shovel-derived material in packet generation is root-family background only, not evidence for the selected target `sċēaf` [Germanic/docs/lexeme_reports/packets/2184-shove-sċēaf.md:203-225].

## Open questions for later work

- If `dev_notes_slices/index.tsv` is updated, row 2184 now has enough row-specific current DEV_NOTES material to index directly; the remaining open question is not analytical adequacy but how much of the superseded `sċufon` history should be indexed alongside the current `sċēaf` resolution.
- A later final report should keep the four layers explicit near the top: cognate-set `PROTO *skéubaną`; older DEV_NOTES spelling `*skeubăną` for the same infinitive-layer headword; superseded plural cell `*skúbun → sċufon`; and live selected singular-preterite cell `*skáub → sċēaf`.
- The past participle `*skúbanaz → sċofen` remains a real alternative clean cell. Later prose should note it as the rejected-but-valid option, not as evidence that the row choice is unstable.
- The remaining infrastructure task is presentational: `coverage_audit.md` still treats this row as uncovered even though packet, memo, and slice now exist; that stale audit status should be refreshed when index/report bookkeeping is next regenerated.
