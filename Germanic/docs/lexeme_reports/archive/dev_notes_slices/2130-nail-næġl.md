---
row_id: 2130
concept: nail
counterpart: næġl
proto: *náglaz
protoform: *náglaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2130 nail / næġl

## Current row state

- CONCEPT: `nail`
- COUNTERPART: `næġl`
- PROTO: `*náglaz`
- PROTOFORM: `*náglaz`
- DERIVATION_CLASS: `regular`
- Live TSV state: row 2130 currently keeps `*náglaz` as both comparative `PROTO` and row-local `PROTOFORM`, with OE `næġl` as the target and no additional row note beyond inherited-source boilerplate [Germanic/data/germanic-aligned-final.tsv:776-776].
- Lexical-attestation baseline: repo-local dictionary material supports OE `nægl` / `nægel = nægl` as the ordinary lexeme spelling without requiring a different row target; the slice therefore treats project `næġl` as the same OE lexeme written with explicit palatal marking rather than as a different lexical item [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:29212-29216].

## Development-note summary

Secure current DEV_NOTES authority **does survive** for row 2130, but it survives as shared philological reasoning rather than as a dedicated nail-only memorandum. The current project position is explicit that row 2130 is a regular **nominative-singular** `*Cl#` item: `*náglaz` is already the correct comparative lexeme headword (`PROTO`) and also the correct row-local FST input (`PROTOFORM`), while the OE target is the apocopated nominative `næġl`, not a plural such as `næglas` and not a parasite-vowel form such as `nagel/nægel` [Germanic/data/germanic-aligned-final.tsv:776-776; Germanic/docs/DEV_NOTES.md:30609-30627,30641-30647].

That distinction matters because the row is **not** evidence for A-restoration across a consonant-plus-liquid cluster. DEV_NOTES' Campbell-based audit repeatedly separates singular `nægl` from plural `næglas`: the plural is cited as an analogically levelled paradigm form in the larger `Cl/Cr` discussion, whereas singular `nægl` is regular precisely because the word-final `-gl` cluster stands after late apocope with **no surviving back-vowel trigger**. In other words, the row's front vowel belongs to the ordinary Anglo-Frisian fronting outcome that remains unretracted in the nominative singular; the row should therefore be used to block overbroad `Cl`-permission proposals, not to motivate them [Germanic/docs/DEV_NOTES.md:30516-30518,30523-30544,30623-30627,30737-30754; docs/references/campbell_old_english_grammar.txt:4739-4753].

The other live authority is the later palatalization audit. DEV_NOTES revises the project rule so that front-vowel + preconsonantal `*g` must palatalize, and it names `*náglaz → næġl` as one of the minimum regression-watch items. That means the row's explicit OE target is not just `nægl` in unmarked dictionary orthography but project-normalized `næġl`, with dotted `ġ` recording the palatal value before `l`. Ringe-Taylor's handbook forms (`OE negl`) do not contradict that notation because the same volume says it normally omits marks of palatalization; Clark Hall likewise writes `nægl` / `nægel` without dotting the consonant [Germanic/docs/DEV_NOTES.md:43305-43331,43348-43357; docs/references/ringe_taylor_linguistic_history_vol2.txt:955-958,11729-11731,18842-18855; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:29212-29216].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-30492-30544

- Source heading: `Examples involving a cluster vs. a single consonant — empirical inventory` plus `Are there cases where A-restoration fails before *l specifically*?`
- Source line or section hint: `lines 30492-30544`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `a_restoration`; `cl_cluster`; `paradigm_leveling`; `campbell_158`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2050,2133,2164`

This is the main current authority for how `næġl` must be read inside the project's A-restoration work. DEV_NOTES first inventories cluster cases and then isolates the crucial `l`-cluster question. In that audit, plural `næglas` is listed with the forms that are "**NOT restored**," and the note immediately clarifies why: Campbell §158 treats plural `næglas` as analogical `æ` from singular `nægl`, not as proof that the sound change itself failed before `l` [Germanic/docs/DEV_NOTES.md:30516-30518,30523-30529]. DEV_NOTES then generalizes the point: "there is no sound law that says A-restoration fails before *Cl*"; what the lexicon preserves is paradigm levelling, with some forms levelling `a` and others `æ` [Germanic/docs/DEV_NOTES.md:30530-30544]. Campbell's own wording, as preserved in the repo reference extract, says that before most clusters "`a` is not restored except for a few instances before consonant plus liquid," names exceptional `appla / watrode / accras`, then lists "`always ... fedras, nzglas`" before explaining that the earlier restored vowel was later removed by analogy and reflected in doublets such as `hægel, hagol` [docs/references/campbell_old_english_grammar.txt:4742-4753]. For row 2130, the usable conclusion is narrow and current: singular `næġl` stays front because its nominative singular has no back-vowel trigger, while plural `næglas` belongs to the paradigm-levelling dossier rather than to the row's direct derivation [Germanic/docs/DEV_NOTES.md:30523-30529].

### DEV_NOTES:line-30604-30647

- Source heading: `§17.19.4 Other potentially affected words` / `Words in the TSV with proto *-aCl-* or *-aCr-* before a back-vowel tail`
- Source line or section hint: `lines 30604-30647`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `row_inventory`; `proto_vs_protoform`; `nom_sg`; `no_back_vowel_trigger`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2050,2133,2164`

This is the clearest row-local DEV_NOTES statement. In the TSV inventory table, row 2130 is entered explicitly as `*náglaz | næġl | *Cl* word-final NomSg, no back-vowel trigger (cf. *hægl*); regular` [Germanic/docs/DEV_NOTES.md:30621-30627]. The prose directly below makes the same contrast in fuller form: words such as `*naglaz, xáglą, séglą` have `l` as part of a **word-final coda (NomSg)**, so "no back-vowel trigger exists" and their FST outputs are correctly `næġl, hæġl, seġl`, whereas the only actual `a + obstruent + l + back-vowel-tail` row in that audit is the separate `nafola` problem [Germanic/docs/DEV_NOTES.md:30641-30647]. That fragment is the strongest available authority for keeping `PROTO` and `PROTOFORM` identical here: unlike `nafola`, row 2130 does not need a surrogate protoform with an inherited medial vowel, because the target row is already the apocopated nominative shape where the back-vowel-trigger environment no longer exists [Germanic/docs/DEV_NOTES.md:30623-30627,30641-30647].

### DEV_NOTES:line-43305-43357

- Source heading: `§17.50.4.4 Revised proposal` plus `§17.50.4.5 Regression watchlist`
- Source line or section hint: `lines 43305-43357`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `g_palatalization`; `preconsonantal_g`; `orthographic_notation`; `regression_watchlist`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1579,2164`

This later audit governs the consonant notation of the row. DEV_NOTES says the old palatalization rule was too narrow because it missed the **preconsonantal** case, and it names `*náglaz → nail` and `*séglą → sail` as the minimum items that would be broken by that mistake [Germanic/docs/DEV_NOTES.md:43305-43315]. The revised rule is therefore formulated so that after a front vowel, `*g` palatalizes unless followed by a back vowel, and the regression table lists `*náglaz → næġl` under the environment `front-V _ /l/` with required outcome `palatal` [Germanic/docs/DEV_NOTES.md:43319-43331,43348-43357]. The reference framing matches that conclusion: Ringe-Taylor explicitly state that "preconsonantal and word-final `*g` were palatalized by any preceding front vowel," while the same volume also notes that its OE citations normally omit marks of palatalization [docs/references/ringe_taylor_linguistic_history_vol2.txt:11729-11731,955-958]. Their lexical examples accordingly print `OE negl` and `OE segl`, not because the consonant stayed velar, but because the handbook is not using dotted `ġ` notation there [docs/references/ringe_taylor_linguistic_history_vol2.txt:18842-18855]. Clark Hall's `nægel = nægl` / `nægl` headword is compatible with the same interpretation [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:29212-29216].

### DEV_NOTES:line-30731-30754

- Source heading: `§17.19.5 Recommendation` / `Option B — Keep TSV as *nablô*, extend OEARestorationIntervening to allow *l* in cluster position`
- Source line or section hint: `lines 30731-30754`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `overbroad_rule`; `cl_permission`; `project_history`; `row_safeguard`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs: `2050,2133,2164`

This fragment is not current row policy, but it should be preserved because it names row 2130 as a regression risk in a now-rejected repair strategy. DEV_NOTES considers the idea of allowing `*l` inside `OEARestorationIntervening` so that `nafola` could be derived without changing its protoform, then rejects that route as "phonologically wrong" and as a weakening of the rule [Germanic/docs/DEV_NOTES.md:30731-30743]. The decisive row-2130 warning follows immediately: unconditional `*Cl*` permission would "likely break `næġl, hæġl, seġl` NomSg outputs unless very carefully scoped," because those lexemes are precisely the stressed-vowel-plus-`Cl#` environments that should remain fronted [Germanic/docs/DEV_NOTES.md:30744-30754]. For this slice, the fragment matters as superseded project history and as a defensive citation against any later attempt to reuse row 2130 as evidence for widening the restoration rule.

## Superseded or diagnostic material

- The only clearly attachable superseded row history is the rejected idea that a broader `Cl`-permission rule might be an acceptable way to rescue `nafola`. DEV_NOTES itself rejects that option and uses `næġl` as one of the forms that such a rule would endanger, so this material should be cited only as a warning against over-application, not as live support for the row's derivation [Germanic/docs/DEV_NOTES.md:30731-30754].
- Campbell's plural `næglas` evidence is easy to misuse if detached from the singular/plural contrast. In this slice it should remain diagnostic evidence about paradigm levelling and the limits of `Cl`-based restoration generalizations, not a substitute derivation for singular row 2130 [Germanic/docs/DEV_NOTES.md:30516-30529; docs/references/campbell_old_english_grammar.txt:4742-4753].
- Dictionary and handbook spellings without dotted palatal marks (`nægl`, `nægel`, `negl`) are **not** contrary evidence against project `næġl`; they are mostly notation differences. Later reporting should therefore avoid presenting the undotted spellings as though they disproved the current palatalization policy [docs/references/ringe_taylor_linguistic_history_vol2.txt:955-958,18842-18855; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:29212-29216].

## Open questions for later work

- Decide whether the final report wants a one-line paradigm note distinguishing singular `næġl` from diagnostic plural `næglas`, so Campbell §158 cannot be flattened into a false singular derivation [Germanic/docs/DEV_NOTES.md:30523-30529; docs/references/campbell_old_english_grammar.txt:4742-4753].
- If a later packet or memo is created for this row, record explicitly that `PROTO = PROTOFORM = *náglaz` here because the target is the nominative singular coda form, unlike `nafola`-type cases that require a different row-local protoform [Germanic/docs/DEV_NOTES.md:30623-30627,30641-30647].
- If orthographic normalization policy is revisited, keep the notation issue separate from the phonology: handbook/dictionary `nægl` and project `næġl` should be cross-referenced as the same OE lexeme unless new row-specific evidence appears [docs/references/ringe_taylor_linguistic_history_vol2.txt:955-958,11729-11731,18842-18855; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:29212-29216].
