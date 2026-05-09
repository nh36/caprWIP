---
row_id: 2273
concept: wasp
counterpart: wæfs
proto: *wábsaz
protoform: *wábsaz
derivation_class: attested_variant
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2273-wasp-wæfs.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2273-wasp-wæfs.md
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2273 wasp / wæfs

## Current row state

- CONCEPT: `wasp` [Germanic/data/germanic-aligned-final.tsv:1331-1331]
- COUNTERPART: `wæfs` [Germanic/data/germanic-aligned-final.tsv:1331-1331]
- PROTO: `*wábsaz` [Germanic/data/germanic-aligned-final.tsv:1331-1331]
- PROTOFORM: `*wábsaz` [Germanic/data/germanic-aligned-final.tsv:1331-1331]
- DERIVATION_CLASS: `attested_variant` [Germanic/data/germanic-aligned-final.tsv:1331-1331]
- Live TSV note already states the current project position in compressed form: the row was retargeted from late West Saxon `wæsp` to earliest attested OE `wæfs`, citing Épinal-Corpus `waefs`, Bülbring on late-WS `wasp < wæps < waefs`, Fulk's ordering `wæfs (also wæsp, wæps)`, and Brunner's split treatment of `fs > ps` and `ps > sp` [Germanic/data/germanic-aligned-final.tsv:1331-1331].
- The duplicated TSV source-note field still only says `Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh)`; that inherited source marker is not the real authority for the row's present targeting policy, which instead comes from the handbook-backed DEV_NOTES dossier and the row note just summarized [Germanic/data/germanic-aligned-final.tsv:1331-1331].
- Row-specific support files do exist and should be kept linked: packet `Germanic/docs/lexeme_reports/packets/2273-wasp-wæfs.md` and memo `Germanic/docs/lexeme_reports/research_memos/2273-wasp-wæfs.md` [Germanic/docs/lexeme_reports/packets/2273-wasp-wæfs.md:1-230; Germanic/docs/lexeme_reports/research_memos/2273-wasp-wæfs.md:1-81]. No row-specific pilot file was found under `Germanic/docs/lexeme_reports/pilot/`.
- The packet is useful but partly stale: it still preserves the older mismatch state `*wábsaz | wæfs | wæsp` and even a now-misleading paradigm-probe prompt, while the memo correctly reclassifies the problem as lexical-variant chronology rather than paradigm-cell selection [Germanic/docs/lexeme_reports/packets/2273-wasp-wæfs.md:48-72,146-229; Germanic/docs/lexeme_reports/research_memos/2273-wasp-wæfs.md:9-13,54-80].

## Development-note summary

This row now has strong row-specific DEV_NOTES support, and the support is unusually explicit about chronology. The decisive point is not that `wæsp` or `wasp` are unreal. It is that the live row should target the earliest attested and lautgesetzlich derivable Old English form, `wæfs`, while treating `wæps` and `wæsp/wasp` as later doublets created by restricted metatheses [Germanic/docs/DEV_NOTES.md:42191-42342]. The DEV_NOTES section is therefore a target-selection dossier, not an exception memo asking the FST to generate every later lexical variant.

The row still needs the three-way label distinction stated explicitly, even though `PROTO` and `PROTOFORM` are identical strings in the live TSV. `PROTO = *wábsaz` is the comparative Germanic headword for the cognate set; `PROTOFORM = *wábsaz` is also the OE-facing input currently fed to the derivation; `COUNTERPART = wæfs` is the selected Old English attested variant that the row chooses to represent [Germanic/data/germanic-aligned-final.tsv:1331-1331]. Later OE forms `wæps`, `wæsp`, and `wasp` are not rival protoforms and not rival FST inputs; they are subsequent lexical developments within the OE record, after the regular early cascade has already reached `wæfs` [Germanic/docs/DEV_NOTES.md:42272-42283; Germanic/docs/lexeme_reports/research_memos/2273-wasp-wæfs.md:34-41,46-52].

DEV_NOTES is also unusually clear that the FST was never the underlying problem. The trace given there is the regular one: after final-vowel loss and Anglo-Frisian brightening, the stem reaches `*wæbs`; `PGmcBAllophony` turns `*b` into `*β` between vowel and consonant; surface devoicing before voiceless `s` yields `wæfs` [Germanic/docs/DEV_NOTES.md:42201-42221]. DEV_NOTES then ties that directly to handbook phonology: Fulk's discussion of Grimm's-law failure in `*bs/*ps` clusters lists `OE wæfs (also wæsp, wæps) 'wasp'`, with `wæfs` named first [@Fulk2018, §6.5; docs/references/fulk_comparative_grammar_early_germanic.vision.txt:6524-6527]. In other words, the row was fixed by aligning the TSV target with the already-correct derivation, not by adding a new repair rule.

The philological chronology in the sources is the core material that this slice needs to preserve. Bülbring states, “Ebenso entsteht spät-ws. *wasp* aus *wæps* 'Wespe' (<*waefs* Corp.)” [@Bulbring1902, §484 Anm. 3; docs/references/bulbring_altenglisches_elementarbuch.txt:9992-9994]. Brunner §193.3 states that `fs` goes over to `ps` in `wæps`, but that “in den ältesten Denkmälern” one still finds `fs`, specifically `Ep. Corp. waefs` [@SieversBrunner1965, §193.3; docs/references/brunner_1965_altenglische_grammatik.vision.txt:8052-8056]. Brunner §204.3 then treats `wasp` as a later reverse metathesis from `wæps`, and his note stresses that this metathesis is confined to “ein kleines Mundartgebiet” [@SieversBrunner1965, §204.3; docs/references/brunner_1965_altenglische_grammatik.vision.txt:8483-8489]. Campbell confirms the same relative chronology in English: “fs > ps in OE relatively late, for the original sounds are recorded in early texts: weps wasp (Ep., Cp. waefs, but Erf. uaeps)” [@Campbell1959, §418; docs/references/campbell_old_english_grammar.txt:11047-11052].

That chronology is exactly why the live derivation class remains `attested_variant` rather than `regular` or `known_unmodelled`. The project is not claiming that only one OE form existed. It is selecting one attested member of a documented OE variant set and preferring the chronologically earliest, lautgesetzlich form over later dictionary-friendly or West-Saxonized doublets [Germanic/data/germanic-aligned-final.tsv:1331-1331; Germanic/docs/DEV_NOTES.md:42225-42342]. Clark Hall is valuable precisely as a warning here: his headword is `wæps`, while `wæfs` and `wæsp` are cross-references, so lexicographic lemma practice does not identify the earliest or best row target by itself [@ClarkHall1960, s.v. "wæps"; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:46507-46507,46798-46806].

The practical row policy is therefore narrow and conservative. Keep `PROTO *wábsaz`; keep `PROTOFORM *wábsaz`; keep `COUNTERPART wæfs`; keep `DERIVATION_CLASS attested_variant`; and do not try to generalize either `fs > ps` or `ps > sp` into ordinary OE sound rules merely to land on late `wæps` or `wasp` [Germanic/docs/DEV_NOTES.md:42281-42342]. DEV_NOTES is explicit that doing so would have poor cost-benefit and would risk regressions such as `*drīfst`-type forms, exactly because the relevant metatheses are lexically restricted rather than ordinary phonology [Germanic/docs/DEV_NOTES.md:42312-42324; @SieversBrunner1965, §193.3 Anm. 2].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-42191-42221

- Source heading: `§17.47 *wábsaz → wæfs (expected wæsp): TSV target is the late-WS doublet, not the lautgesetzlich form`
- Source line or section hint: `lines 42191-42221`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `fst_trace`; `pgmc_b_allophony`; `surface_devoicing`; `false_mismatch`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This opening fragment is the best current statement that the old mismatch was target-side, not rule-side. DEV_NOTES gives the row-local mismatch table `*wábsaz | wæfs | wæsp`, then walks the trace to `*wæbs`, `*wæβs`, and surface `wæfs`, calling the result “fully lautgesetzlich” [Germanic/docs/DEV_NOTES.md:42195-42221]. The attached Fulk quotation is especially useful because it already bundles the three OE forms in the right order: `wæfs` first, followed by `wæsp` and `wæps` [@Fulk2018, §6.5; docs/references/fulk_comparative_grammar_early_germanic.vision.txt:6524-6527]. For future writing, this fragment should anchor any claim that the cascade itself was correct before the row retargeting.

### DEV_NOTES:line-42223-42270

- Source heading: `Source audit — what is the actual attested OE form?`
- Source line or section hint: `lines 42223-42270`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `philological_chronology`; `earliest_attestation`; `dictionary_lemma_vs_attestation`; `source_audit`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling philological fragment and the strongest candidate for later indexing. DEV_NOTES explicitly stages the evidence as coexistence plus chronology, not as a hunt for one magically “correct” dictionary spelling [Germanic/docs/DEV_NOTES.md:42223-42270]. The fragment preserves the crucial direct quotations from Bülbring and Brunner: late WS `wasp` comes from `wæps`, which in turn goes back to glossary `waefs`; the oldest monuments still show `fs`; and `ps > sp` is a later West Saxon development [@Bulbring1902, §484 Anm. 3; @SieversBrunner1965, §§193.3, 204.3]. It also records Hall's lemma practice (`wæps`, with `wæfs` and `wæsp` redirected) and notes that Fulk lists `wæfs` first [Germanic/docs/DEV_NOTES.md:42260-42269; @ClarkHall1960, s.v. "wæps"; @Fulk2018, §6.5]. That combination makes the fragment much richer than a bare row note.

### DEV_NOTES:line-42272-42342

- Source heading: `Three competing OE forms, three chronological layers`; `Current TSV target`; `Three options`; `Recommendation`
- Source line or section hint: `lines 42272-42342`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `variant_layering`; `target_selection`; `restricted_metathesis`; `policy_decision`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment turns the source audit into policy and should be preserved nearly as-is. DEV_NOTES tabulates `wæfs`, `wæps`, `wasp`, and `wæsp` as distinct chronological layers, then states why the older TSV target `wæsp` was a bad fit: it is not Hall's lemma, it requires both restricted metatheses, and it is not the form produced by the lautgesetzlich cascade [Germanic/docs/DEV_NOTES.md:42272-42295]. The recommendation section then makes the project principle explicit: choose the form that is directly attested, derivable, and chronologically earliest, rather than introducing lexically restricted sound rules for a single row [Germanic/docs/DEV_NOTES.md:42298-42342]. This is the slice's main policy anchor for `attested_variant`.

### DEV_NOTES:line-42344-42350

- Source heading: `Verification plan`
- Source line or section hint: `lines 42344-42350`
- Fragment type: `historical_execution_note`
- Status: `completed_but_still_informative`
- Issue tags: `no_fst_change`; `row_edit_only`; `historical_resolution`
- Recommended next use: `use_as_resolution_provenance`
- Shared with row IDs:

This short fragment is no longer an open to-do list, but it remains useful because it records the scale of the fix. DEV_NOTES says the repair consisted of editing row 2273 to `wæfs`, appending the explanatory note, and making **no FST change** [Germanic/docs/DEV_NOTES.md:42344-42350]. That matters because later readers could otherwise misremember the row as one that required a new metathesis rule. It did not.

### DEV_NOTES:line-9533-9539

- Source heading: `Empirical Validation (Dry Run 2026-03-13)`
- Source line or section hint: `lines 9533-9539`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `old_target`; `regression_snapshot`; `pre_retarget_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This earlier dry-run fragment should be preserved only as labeled history. It records `wabsăz → wafs (should be wæsp) - REGRESSED (was wæfs)` and counts `wasp` among the regressions [Germanic/docs/DEV_NOTES.md:9533-9539]. That is valuable because it shows the row's former state, but it is not current authority: the old “should be `wæsp`” expectation is exactly what §17.47 later overturns.

## Superseded or diagnostic material

- The packet's prompt “Paradigm probe required for this row” is not safe to reuse as current guidance. The research memo correctly explains that this is not a hidden oblique/genitive/plural-cell problem but a citation-form chronology problem among attested lexical variants [Germanic/docs/lexeme_reports/packets/2273-wasp-wæfs.md:226-229; Germanic/docs/lexeme_reports/research_memos/2273-wasp-wæfs.md:65-69].
- The old mismatch state `TSV target = wæsp` is diagnostic history only. It belongs to the period before DEV_NOTES separated the earliest attested form from later West Saxon metathesis outcomes [Germanic/docs/DEV_NOTES.md:42195-42199; Germanic/docs/DEV_NOTES.md:42334-42342].
- Clark Hall's lemma `wæps` and Wiktionary's row-level `wæsp` are both useful background, but neither should overrule the chronological argument from Bülbring, Brunner, Campbell, and Fulk. Lexicographic headwords and inherited TSV source markers are not equivalent to row-policy authority here [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:46798-46806; Germanic/data/germanic-aligned-final.tsv:1331-1331].
- The important live distinction is among attested early `wæfs`, later `wæps`, and late-WS/dialectally restricted `wasp`/`wæsp`. Flattening those into one undifferentiated “OE wasp form” would erase the very evidence that justifies the present `attested_variant` classification [Germanic/docs/DEV_NOTES.md:42272-42342; @Campbell1959, §418; @SieversBrunner1965, §§193.3, 204.3].

## Open questions for later work

- If this row is ever promoted into a final report, decide whether to present the later forms as `wæps` plus late-WS `wasp/wæsp`, or to keep the exact DEV_NOTES table ordering `wæfs > wæps > wasp` with `wæsp` treated separately as a dictionary-style spelling. The current evidence supports the chronology, but the internal status of `wæsp` versus `wasp` is lexicographic rather than fully dossiered [Germanic/docs/DEV_NOTES.md:42272-42279; @ClarkHall1960, s.v. "wæps"].
- If later indexing work wants compact anchors rather than the whole §17.47 block, the strongest candidates are the source audit `DEV_NOTES:line-42223-42270` and the policy/recommendation block `DEV_NOTES:line-42272-42342`. The verification note `DEV_NOTES:line-42344-42350` is useful provenance but weaker as a standalone content anchor.
- If a later report wants a broader comparative paragraph, add the Campbell §418 wording alongside Bülbring and Brunner rather than replacing them; Campbell is a strong corroborating witness for the same chronology, but DEV_NOTES' row-specific argument currently rests most heavily on Bülbring + Brunner + Fulk [@Campbell1959, §418; Germanic/docs/DEV_NOTES.md:42227-42269].
