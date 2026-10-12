---
row_id: 2164
concept: sail
counterpart: seġl
proto: *séglą
protoform: *séglą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2164 sail / seġl

## Current row state

- CONCEPT: `sail` [Germanic/data/germanic-aligned-final.tsv:907-907]
- COUNTERPART: `seġl` [Germanic/data/germanic-aligned-final.tsv:907-907]
- PROTO: `*séglą` [Germanic/data/germanic-aligned-final.tsv:907-907]
- PROTOFORM: `*séglą` [Germanic/data/germanic-aligned-final.tsv:907-907]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:907-907]
- The live TSV row already keeps the row-level distinction clean: comparative `PROTO` and row-local `PROTOFORM` are both `*séglą`, while the selected OE target is `seġl`; there is no row-local warning note in the TSV beyond the regular classification [Germanic/data/germanic-aligned-final.tsv:907-907].
- `oe_known_problems.tsv` currently has no row-local entry for row `2164`, concept `sail`, lexeme `seġl`, or proto/protoform `*séglą`; nothing there presently treats the row as an OE exception, wontfix item, or unresolved mismatch [Germanic/data/oe_known_problems.tsv:1-8].

## Development-note summary

No securely attachable dedicated `sail / seġl / *séglą` memorandum survives in `Germanic/docs/DEV_NOTES.md`. What does survive is still strong enough to replace a DEV_NOTES lookup, because the row is named explicitly in two current cross-lexeme audits and one superseded caution. The live row is regular, with `PROTO = PROTOFORM = *séglą` and OE target `seġl` [Germanic/data/germanic-aligned-final.tsv:907-907]. DEV_NOTES' current use of the row is not to diagnose a lingering mismatch, but to mark two things that later reporting must keep separate and explicit: first, row 2164 is **not** an `*aCl` A-restoration problem; second, it **is** a positive control for palatalization of preconsonantal `*g` after a front vowel [Germanic/docs/DEV_NOTES.md:30620-30647,43305-43357].

The A-restoration material is unusually clear about the negative claim. In the inventory table the row is entered as `*séglą | seġl | *Cl*, not *aCl*; *e*-grade`, and the prose directly below says that words like `*naglaz, xáglą, séglą` have `l` "as part of a word-final coda (NomSg) where no back-vowel trigger exists" and that their FST output is correctly `næġl, hæġl, seġl` [Germanic/docs/DEV_NOTES.md:30630-30646]. That means row 2164 should not be cited as evidence that restoration can reach across a consonant-plus-`l` cluster or that the row needs a special OE-directed protoform with a surviving medial back vowel. The current project position is the opposite: the row is regular precisely because its vowel is inherited `*e`, not `*a`, and because the relevant `-gl` cluster belongs to the word-final coda environment that lacks the back-vowel trigger discussed for `nafola`-type cases [Germanic/docs/DEV_NOTES.md:30630-30647].

The palatalization material supplies the positive claim. DEV_NOTES later says an earlier rule proposal was "too narrow" because it captured only word-final and intervocalic palatalization and "loses the preconsonantal case"; `*séglą → sail` is named as one of the minimum rows that would break if that environment were omitted [Germanic/docs/DEV_NOTES.md:43305-43315]. The revised rule is then stated so that after a front vowel, `*g` palatalizes unless followed by a back vowel, and the regression watchlist includes `*séglą -> seġl` under the environment `front-V _ /l/` with required outcome `palatal` [Germanic/docs/DEV_NOTES.md:43319-43331,43346-43357]. For row 2164, this is the concrete reason the OE target should remain `seġl` with dotted `ġ`: the row is a control case for the project's preconsonantal palatal-`g` policy, not a place where undotted `segl` should be allowed to drift back in as if nothing phonological were at stake [Germanic/data/germanic-aligned-final.tsv:907-907; Germanic/docs/DEV_NOTES.md:43305-43357].

The only attachable superseded material is likewise useful because it shows how the row can be misused. When DEV_NOTES rejects an overbroad repair that would allow unconditional `*Cl` permission in the restoration rule, it warns that such a move would likely break `næġl, hæġl, seġl` nominative-singular outputs unless scoped with great care [Germanic/docs/DEV_NOTES.md:30744-30754]. That warning does not create a row-specific problem history for `seġl`; it preserves a boundary condition. Later writers should use row 2164 as a safeguard against overgeneralized `Cl` restoration, while continuing to use it positively as a preconsonantal-`g` palatalization check [Germanic/docs/DEV_NOTES.md:30744-30754,43305-43357].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-30620-30647

- Source heading: `§17.19.4 Other potentially affected words` / `Words in the TSV with proto *-aCl-* or *-aCr-* before a back-vowel tail`
- Source line or section hint: `lines 30620-30647`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `a_restoration`; `e_grade`; `cl_cluster`; `protoform_vs_proto`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2050,2130`

This is the main current authority for row 2164. DEV_NOTES names the row directly in the table as `*séglą | seġl | *Cl*, not *aCl*; *e*-grade` [Germanic/docs/DEV_NOTES.md:30630-30630]. The prose immediately below then explains why that label matters: `*naglaz, xáglą, séglą` have the `l` "as part of a word-final coda (NomSg) where no back-vowel trigger exists," so the FST outputs `næġl, hæġl, seġl` are already correct [Germanic/docs/DEV_NOTES.md:30641-30646].

For this row, the fragment establishes three concrete points that should be carried forward unchanged. First, row 2164 is not part of the `*a + obstruent + l + back-vowel-tail` problem that DEV_NOTES is solving in the surrounding section. Second, the row does not need a special surrogate `PROTOFORM`; the live `*séglą` is already the correct row-local input because there is no missing medial back-vowel trigger to encode [Germanic/data/germanic-aligned-final.tsv:907-907; Germanic/docs/DEV_NOTES.md:30630-30646]. Third, `seġl` is not merely tolerated but explicitly affirmed as the correct OE output in this shared comparison set [Germanic/docs/DEV_NOTES.md:30644-30646].

### DEV_NOTES:line-43305-43357

- Source heading: `§17.50.4.4 Revised proposal` plus `§17.50.4.5 Regression watchlist`
- Source line or section hint: `lines 43305-43357`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `g_palatalization`; `preconsonantal_g`; `orthographic_notation`; `regression_watchlist`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2130`

This fragment governs the consonant analysis of the row. DEV_NOTES says the earlier formulation was "too narrow" because it missed the **preconsonantal** palatalization environment, and it lists ``*séglą  → sail`` among the minimum lexemes that would be broken by that omission [Germanic/docs/DEV_NOTES.md:43305-43315]. The revised rule is then given as `{*g} -> {*ʤ} || EnglishStarFrontVowel _ \EnglishStarBackVowel`, glossed as "after a front V, palatalise *g unless followed by a back V" [Germanic/docs/DEV_NOTES.md:43319-43331].

The regression watchlist makes the row-local implication fully explicit: `*séglą` must yield `seġl`, its environment is `front-V _ /l/`, and the required outcome is `palatal` [Germanic/docs/DEV_NOTES.md:43346-43357]. That is the securely attachable reason the slice keeps OE `seġl` with dotted `ġ`. For later reporting, this fragment should be used not as generic background but as a direct control citation: row 2164 is one of the named tests that the project itself uses to prove that front-vowel + preconsonantal `*g` is still being palatalized correctly [Germanic/docs/DEV_NOTES.md:43308-43315,43346-43357].

### DEV_NOTES:line-30742-30754

- Source heading: `§17.19.5 Recommendation` / `Option B — Keep TSV as *nablô*, extend OEARestorationIntervening to allow *l* in cluster position`
- Source line or section hint: `lines 30742-30754`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `overbroad_rule`; `cl_permission`; `project_history`; `row_safeguard`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs: `2050,2130`

This is not current row policy, but it is the most useful diagnostic warning preserved in DEV_NOTES. While rejecting a broader `*Cl`-permission repair, DEV_NOTES says such a rule "would over-apply" and would likely break `næġl, hæġl, seġl` nominative-singular outputs unless very carefully scoped, because those lexemes are stressed-vowel-plus-`Cl#` environments [Germanic/docs/DEV_NOTES.md:30744-30750]. The point is not that `seġl` itself is unstable; it is that the row is one of the cases that expose why the proposed repair was phonologically wrong [Germanic/docs/DEV_NOTES.md:30738-30754].

Later use should therefore stay narrow. This fragment is valuable as project history and as a caution against reusing row 2164 as evidence for a generalized restoration rule across `Cl` clusters. It should not be cited as though the row had an unresolved derivational defect or needed a non-regular workaround [Germanic/docs/DEV_NOTES.md:30744-30754; Germanic/data/germanic-aligned-final.tsv:907-907].

## Superseded or diagnostic material

- No securely attachable dedicated superseded `sail` dossier survives beyond the rejected broad-`Cl` repair warning. The important historical fact is therefore negative: row 2164 was used to block a bad generalization, not to justify one [Germanic/docs/DEV_NOTES.md:30744-30754].
- The row should not be absorbed into the neighboring `nafola` discussion merely because both sections mention `l`-clusters. DEV_NOTES is explicit that `séglą` belongs with the word-final-coda forms where "no back-vowel trigger exists," not with the actual `*aCl* + tail` problem case [Germanic/docs/DEV_NOTES.md:30641-30646].
- Conversely, the row should not be flattened into a purely orthographic note. DEV_NOTES' later palatalization audit treats `*séglą -> seġl` as one of the named regression checks for the phonological rule itself, so undotted spellings are at best notation drift and not evidence that the consonant analysis is optional [Germanic/docs/DEV_NOTES.md:43305-43315,43346-43357].

## Open questions for later work

- If a packet or memo is later created for row 2164, make the row's dual role explicit: it is negative evidence against overbroad `*Cl` A-restoration and positive evidence for front-vowel + preconsonantal-`*g` palatalization [Germanic/docs/DEV_NOTES.md:30630-30646,30744-30754,43305-43357].
- If `dev_notes_slices/index.tsv` is updated later, the securely attachable current anchors are `DEV_NOTES:line-30620-30647` and `DEV_NOTES:line-43305-43357`; `DEV_NOTES:line-30742-30754` is useful only as a superseded warning block [Germanic/docs/DEV_NOTES.md:30620-30647,30742-30754,43305-43357].
- If orthographic normalization is revisited elsewhere, keep the row-level distinction sharp: `PROTO = PROTOFORM = *séglą`, OE target `seġl`, and dotted `ġ` justified by the current palatalization rule rather than by ad hoc spelling preference [Germanic/data/germanic-aligned-final.tsv:907-907; Germanic/docs/DEV_NOTES.md:43319-43331,43346-43357].
