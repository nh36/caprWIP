---
row_id: 1954
concept: bone
counterpart: bān
proto: *báiną
protoform: *báiną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/1954-bone-bān.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/1954-bone-bān.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1954 bone / bān

## Current row state

- CONCEPT: `bone`
- COUNTERPART: `bān`
- PROTO: `*báiną`
- PROTOFORM: `*báiną`
- DERIVATION_CLASS: `regular`
- Live TSV note: `Proto: oblique *bainăn→*bainą (n. a-stem nom.sg.; Kroonen)`

## Development-note summary

The live row is regular only if the comparative lemma, the row-specific derivational input, and the superseded project detour stay distinct. Kroonen's comparative entry is stem-level `*baina- n. 'bone, leg'`, with OE `bān` among the reflexes, and Orel likewise gives lemma-style `*bainan` [@Kroonen2013, p. 48; @Orel2003]. The live TSV row, however, does **not** feed either of those dictionary headword spellings or the note's oblique `*bainăn` into the cascade. Its actual row-specific comparator is `PROTO = PROTOFORM = *báiną`, so the regular project expectation is simply `*báiną -> bān`, not `*bainăn -> bānan` and not some separate paradigm-cell workaround.

The attested Old English side is equally straightforward and should not be blurred by the note's stem background. Repo-local lexical sources directly attest citation-form `bān`, and Bright's glossary also keeps the oblique forms visible: `bān, n., bone: ds. bāne ...` [@ClarkHall1960, s.v. "bān"; @BrightCassidyRingler1971, glossary s.v. "bān"]. That matters for this slice because it shows exactly what the current row is and is not claiming. The row target `bān` is the ordinary OE citation / nominative-accusative singular form, while the note's `*bainăn` is useful only as comparative morphology explaining why Kroonen mentions an oblique stem behind the nominative-style input.

The one early DEV_NOTES passage attached directly to this lexeme is now diagnostic history, not current policy. In the mismatch-bucket refinement, the project logged `*bainăn -> bānan` under `inflectional_suffix_extra` and glossed such cases as likely TSV problems caused by selecting the wrong inflectional form [DEV_NOTES:line-1569-1572]. That fragment should be preserved because it records the exact abandoned detour later writers would otherwise have to rediscover: the superseded comparator was an oblique-style input yielding an extra nasal suffix. What it does **not** show is that OE `bānan` is attested, that row 1954 should be retargeted away from `bān`, or that the row's current `regular` classification is in doubt.

Later DEV_NOTES material records the correction that makes the live row stable. The West Germanic monophthongisation note says the sandbox now collapses stressed proto `{*ai}` to `{*ā}` before later OE/English vowel handling, explicitly so intermediate forms such as `{*bān}` can be inspected, and the later verification note confirms that stressed `*ai` forms still derive correctly: `*bainą -> bān` [DEV_NOTES:line-2259-2263; DEV_NOTES:line-14036-14038]. For row 1954, that is the current project decision in practice: regular comparator `*báiną -> *bāną -> bān`, attested OE target `bān`, and superseded project detour `*bainăn -> bānan` retained only as debugging chronology.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1569-1572

- Source heading: `Consonant Mismatch Bucket Refinement (2026-02-07)`
- Source line or section hint: `lines 1569-1572`
- Fragment type: `superseded_analysis`
- Status: `superseded`
- Issue tags: `inflectional_suffix_extra`; `wrong_input_form`; `debug_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This fragment should be kept only as replacement-note chronology. It records that `*bainăn -> bānan` was classified under `inflectional_suffix_extra` and treated as a likely wrong-form selection. Preserve it because it names the abandoned diagnosis precisely: the superseded project problem was an over-inflected comparator with extra `-an`, not the live row's regular comparator `*báiną -> bān`, not evidence for attested OE `bānan`, and not a reason to convert row 1954 into a paradigm-cell or exception case.

### DEV_NOTES:line-2259-2263

- Source heading: `WG monophthongisation stage`
- Source line or section hint: `lines 2259-2263`
- Fragment type: `sound_change_background`
- Status: `current`
- Issue tags: `wg_monophthongisation`; `stressed_ai`; `intermediate_output`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment matters because it explains why the current row can be read as a regular stressed-`*ai` outcome instead of as a residual sandbox artifact. DEV_NOTES states that the project inserted a West Germanic stage where proto `{*ai}` and `{*au}` collapse onto historical `{*ā}` and `{*ō}`, and that spot checks now expose both the WG-monophthongised forms (`bān/stān/fāl/bōl`) and the older `{*bain}` branches. For row 1954, the fragment is current background supporting the regular comparator `*báiną -> *bāną -> bān`; it is not a warning that the row still depends on the discarded `{*bainăn}` route.

### DEV_NOTES:line-14036-14038

- Source heading: `Implementation completed (2026-04-06)`
- Source line or section hint: `lines 14036-14038`
- Fragment type: `verification`
- Status: `current`
- Issue tags: `verification`; `stressed_ai`; `regular_outcome`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the cleanest current-state confirmation for the lexeme inside DEV_NOTES. The note explicitly reports `Stressed *ai forms still work: *bainą -> bān, *dailiz -> dǣl`, so it verifies the live row's actual input-output pair after the monophthongisation and related repairs. Later report prose should prefer this fragment over the older bucket note when stating present row policy, because it confirms the current regular outcome rather than merely preserving a stale bug classification.

## Superseded or diagnostic material

The main warning is narrow but important. Row 1954 does have a preserved project detour, but it is only the stale `*bainăn -> bānan` debugging path from [DEV_NOTES:line-1569-1572]. The current row does **not** depend on reviving that oblique input, and the later monophthongisation / verification notes show that the live nominative-style input `*báiną` already reaches the attested OE target `bān` without extra repair logic.

## Open questions for later work

- If the final lexeme report discusses the TSV note, state explicitly that `*bainăn` is comparative stem/paradigm background and not the row's live derivational input.
- If later writers cite the comparative dictionaries, keep lemma-style `*baina-` / `*bainan` separate from the row-specific FST input `*báiną` rather than silently normalizing them together.
- If the report mentions oblique OE evidence such as `bāne`, use it to clarify the noun's paradigm, not to replace the row target `bān`.
