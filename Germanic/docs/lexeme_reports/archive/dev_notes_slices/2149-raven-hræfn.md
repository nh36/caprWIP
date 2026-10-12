---
row_id: 2149
concept: raven
counterpart: hræfn
proto: *xrábnaz
protoform: *xrábnaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2149 raven / hræfn

## Current row state

- The live OE row currently reads `CONCEPT = raven`, `COUNTERPART = hræfn`, `PROTO = *xrábnaz`, `PROTOFORM = *xrábnaz`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:851-851].
- `PROTO` and `PROTOFORM` are still identical here. This row is therefore **not** using a special OE-facing paradigm-cell protoform or a workaround input; the same `*xrábnaz` serves both as comparative label and as derivational input for the OE target [Germanic/data/germanic-aligned-final.tsv:851-851].
- The TSV row's embedded sourcing is still only duplicated Wiktionary-etymology boilerplate rather than a row-local project note or packet reference, so the slice needs to preserve the relevant DEV_NOTES authority explicitly [Germanic/data/germanic-aligned-final.tsv:851-851].
- `oe_known_problems.tsv` currently has no entry for row `2149`, for `*xrábnaz`, for `raven`, or for `hræfn`; the present contents are limited to unrelated `u`-lowering and analogy items [Germanic/data/oe_known_problems.tsv:1-8].
- The main current DEV_NOTES audit already treats the row as matching cleanly: in the `-Cl/-Cn/-Cm#` table, `*xrábnaz | hræfn | hræfn | ✓` appears as a full target/output match, and the following attestation table records both unbroken `hræfn` and broken `hræfen`, with `hræfn` as the lemma-form entry for the word [Germanic/docs/DEV_NOTES.md:29887-29917].

## Development-note summary

No securely attachable row-numbered dossier for `2149 raven / hræfn` survives in `DEV_NOTES.md`. The usable authority is instead the shared `-Cl/-Cn/-Cm#` note at §17.18, plus one direct regression log entry and one comparative-scholarship aside that happens to mention raven explicitly [Germanic/docs/DEV_NOTES.md:3351-3357,9528-9539,29853-30083]. That shared material is nevertheless strong enough to replace casual consultation of `DEV_NOTES.md`, because it does three things the live TSV does not do on its own: it explains why `hræfn` is a deliberate target rather than an accidental output, it records the attested coexistence of `hræfn` and `hræfen`, and it preserves the one important historical bug state (`hrafn`) that should **not** be mistaken for a legitimate current rival [Germanic/data/germanic-aligned-final.tsv:851-851; Germanic/docs/DEV_NOTES.md:9528-9539,29853-30083].

The core philological point is the same one DEV_NOTES makes for the whole class of OE words ending in word-final obstruent + sonorant clusters. After WGmc/OE syncope, forms like `*hræfn-` can show a late-OE parasite vowel in the nominative singular, yielding `hræfen`, while oblique forms such as `hræfnes` remain unbroken because the cluster is medial there [Germanic/docs/DEV_NOTES.md:29855-29868,29943-29946,30036-30039]. DEV_NOTES is concrete about the raven row itself: it lists `hræfn` among the unbroken forms preserved “metri causa” in poetry, then records in the attestation table that `hræfn` is directly attested in *Beowulf* (lines 1801, 2448, 3024), while broken `hræfen` is also attested in Cynewulf's *Elene* 52 [Germanic/docs/DEV_NOTES.md:29870-29879,29909-29917]. The row therefore sits in a **real variation set**, not a mistake-vs-correction pair: `hræfn` is an attested unbroken nominative singular, and `hræfen` is an attested broken nominative singular.

Current project policy resolves that variation in favor of the unbroken form. After weighing three possible strategies for the whole `-Cl/-Cn/-Cm#` group, DEV_NOTES records the user's ruling: “If unbroken versions are attested in Beowulf/poetic and early/Anglian, let's stick with them,” and then explicitly names `hræfn` among the ten unbroken nominative targets retained unchanged [Germanic/docs/DEV_NOTES.md:30015-30033,30067-30083]. For this row, that matters more than the general phonological background. The dataset is **not** claiming that `hræfen` is unattested or “wrong”; it is claiming that, given attested unbroken evidence and the project's register choice, `hræfn` is the preferred OE target for TSV/FST alignment [Germanic/docs/DEV_NOTES.md:29917-29917,30071-30083]. Because `PROTO` and `PROTOFORM` remain the same `*xrábnaz`, the row's design stays simple: no special protoform replacement, no paradigm-cell retargeting, just a deliberately selected unbroken OE nominative singular [Germanic/data/germanic-aligned-final.tsv:851-851].

The only caution to preserve beyond that row-policy result is comparative rather than target-setting. Elsewhere in DEV_NOTES, while discussing the history of scholarship on another `-bn-/-fn-/-mn-` lexeme, Ringe/Taylor are quoted as placing raven in the chain `*hrabnaz → hrefn → hræfn → hremn`, but Fulk is then quoted warning that “the etymologies of OE stefn, stemn 'voice' (Go. stibna), hrafn, hramn 'raven', and efn, emn 'even' (Go. ibns) are rather insecure” [Germanic/docs/DEV_NOTES.md:3351-3357]. For row `2149`, this does **not** unsettle the current OE target `hræfn`; the attestation and row-policy evidence for the target are still solid. What it does mean is that later writeups should avoid turning the deeper comparative `*bn > fn > mn` story into an overconfident row-level claim. In this slice, `hræfn` is secure as the selected OE target; the full comparative pathway to later `hremn/hramn` belongs to background scholarship, not to active row policy [Germanic/docs/DEV_NOTES.md:3351-3357,29887-29917,30067-30083].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-29853-29917

- Source heading: `§17.18.1 The lautgesetzlich background` through `§17.18.3 Attestation findings`
- Source line or section hint: `lines 29853-29917`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `cluster_parasiting`; `hræfn_vs_hræfen`; `attestation`; `nom_sg_selection`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the main current philological fragment for the row. DEV_NOTES first sets out the rule environment: word-final obstruent + sonorant clusters may take a late-OE parasite vowel in nominative singular forms, and Campbell's canonical illustration explicitly includes `hræfen / hræfnes` [Germanic/docs/DEV_NOTES.md:29855-29868]. The note then sharpens the register distribution: poetry preserves unbroken forms such as `hræfn`, whereas late WS prose regularizes the broken type more often [Germanic/docs/DEV_NOTES.md:29870-29879]. Finally, the row appears by name in both tables: the current FST/TSV check gives `*xrábnaz | hræfn | hræfn | ✓`, and the attestation table states that `hræfn` is attested in *Beowulf* 1801, 2448, 3024 while `hræfen` is also attested in *Elene* 52, with `hræfn` listed as the lemma form [Germanic/docs/DEV_NOTES.md:29887-29917].

For row `2149`, this fragment establishes two concrete things that later summaries must keep distinct. First, the **current row target** `hræfn` is derivationally aligned and directly attested. Second, the row belongs to a documented alternation class where broken `hræfen` also exists, so a later reviewer should not treat the absence of `-e-` here as ignorance of manuscript variation [Germanic/docs/DEV_NOTES.md:29887-29917]. It also provides the key oblique-form anchor: `hræfnes` belongs to the uniformly unbroken oblique stem pattern, which is why the row does not need a special workaround protoform to keep the cluster intact in non-nominative contexts [Germanic/docs/DEV_NOTES.md:29863-29868,29943-29946].

### DEV_NOTES:line-30067-30083

- Source heading: `§17.18.7.1 Resolved policy`
- Source line or section hint: `lines 30067-30083`
- Fragment type: `row_policy`
- Status: `current`
- Issue tags: `resolved_policy`; `dataset_register`; `unbroken_nom_sg`; `retained_target`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the governing present-tense policy fragment for the row. DEV_NOTES quotes the user decision, “If unbroken versions are attested in Beowulf/poetic and early/Anglian, let's stick with them,” and then names `hræfn` among the ten unbroken nominative targets that are “all directly attested manuscript spellings” and are therefore “retained unchanged” [Germanic/docs/DEV_NOTES.md:30071-30080]. The same passage adds that the FST's current no-parasiting behavior for `-Cl/Cn/Cm#` is correct for those lemmas because it matches the early / poetic / Anglian register chosen by the dataset [Germanic/docs/DEV_NOTES.md:30080-30083].

For `2149`, this fragment answers the only practical row-policy question that the attestation fragment alone leaves open: why keep `hræfn` when DEV_NOTES itself acknowledges `hræfen`? The answer is not that `hræfen` lacks evidence, but that the project explicitly chose the attested unbroken register-form where such a form exists [Germanic/docs/DEV_NOTES.md:29917-29917,30071-30083]. This also keeps the three row levels clean: `PROTO *xrábnaz`, `PROTOFORM *xrábnaz`, and selected OE `COUNTERPART hræfn` remain aligned without inventing a special OE-facing input or re-lemma strategy [Germanic/data/germanic-aligned-final.tsv:851-851].

### DEV_NOTES:line-3351-3357

- Source heading: `History of scholarship`
- Source line or section hint: `lines 3351-3357`
- Fragment type: `comparative_background`
- Status: `background`
- Issue tags: `bn_fn_mn_chain`; `comparative_caution`; `hrefn_hremn`; `etymology_insecure`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This fragment is not current row policy, but it is worth preserving because it mentions raven explicitly and tempers how strongly later reports should narrate the deeper comparative history. Ringe/Taylor are quoted as grouping raven with forms that show a `*bn → fn → mn` trajectory, specifically `*hrabnaz → hrefn → hræfn → hremn` [Germanic/docs/DEV_NOTES.md:3351-3351]. Immediately after that, Fulk is quoted cautioning that “the etymologies of OE stefn, stemn 'voice' (Go. stibna), hrafn, hramn 'raven', and efn, emn 'even' (Go. ibns) are rather insecure” [Germanic/docs/DEV_NOTES.md:3357-3357].

For row `2149`, this background fragment should be used carefully. It does **not** undermine the selected OE target `hræfn`, which is secured elsewhere by attestation and explicit row policy [Germanic/docs/DEV_NOTES.md:29887-29917,30067-30083]. Its value is narrower: if later work tries to build a research memo about the full PGmc/OE consonant history behind raven and its later `hramn/hremn` variants, DEV_NOTES already preserves both an affirmative derivational chain and a warning that the chain is not beyond dispute [Germanic/docs/DEV_NOTES.md:3351-3357].

## Superseded or diagnostic material

### DEV_NOTES:line-9528-9539

- Source heading: regression log under `BUT: SIGNIFICANT REGRESSIONS OBSERVED!`
- Source line or section hint: `lines 9528-9539`
- Fragment type: `project_history`
- Status: `diagnostic_only`
- Issue tags: `a_restoration_regression`; `hrafn_bad_state`; `fronting_loss`; `do_not_retarget`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This is the one direct row-specific bug-history fragment that needs to survive in the slice. DEV_NOTES records that broadening the A-restoration trigger caused `xrabnăz → hrafn (should be hræfn) - REGRESSED`, and lists raven among the nine forms made worse by that overgeneralization [Germanic/docs/DEV_NOTES.md:9520-9539]. For this row, the diagnostic value is exact: it names the historical bad output `hrafn`, shows that the problem was front-vowel restoration/fronting failure caused by a too-broad suffix trigger, and makes clear that `hrafn` belongs to regression history, not to the row's accepted OE variation set [Germanic/docs/DEV_NOTES.md:9528-9539].

Two cautions follow from that. First, `hrafn` should never be presented as though it were a coequal live target beside `hræfn` and `hræfen`; within current DEV_NOTES it is only a regressed model output [Germanic/docs/DEV_NOTES.md:9528-9539,29887-29917]. Second, this regression history is independent of the separate `hræfn ~ hræfen` manuscript variation discussed in §17.18. The former is an FST bug, the latter is real OE variation within the attested word class [Germanic/docs/DEV_NOTES.md:29853-29917,9528-9539].

## Open questions for later work

- If a later packet or memo is created for this lexeme, keep three layers separate near the top: current row policy (`hræfn` retained as the attested unbroken target), real OE nominative variation (`hræfn` and `hræfen`), and deeper comparative background (`*hrabnaz → hrefn → hræfn → hremn`, with Fulk's caution that the etymology is insecure) [Germanic/docs/DEV_NOTES.md:29887-29917,30067-30083,3351-3357].
- If index entries are later added, the strongest current anchors are the attestation/background cluster note and the resolved-policy note, not the regression log. `9528-9539` is useful project history but should index as diagnostic history only if indexed at all [Germanic/docs/DEV_NOTES.md:9528-9539,29853-30083].
- A future source audit could expand the manuscript-side documentation beyond the line-level summaries already preserved in DEV_NOTES, but the present slice should not claim more than DEV_NOTES securely states: unbroken `hræfn` is directly attested, broken `hræfen` is also attested, and the dataset intentionally keeps the unbroken form [Germanic/docs/DEV_NOTES.md:29917-29917,30071-30083].
