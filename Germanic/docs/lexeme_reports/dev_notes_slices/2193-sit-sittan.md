---
row_id: 2193
concept: sit
counterpart: sittan
proto: *sétjaną
protoform: *sétjaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2193 sit / sittan

## Current row state

- The live OE row is `2193 | sit | sittan | *sétjaną | *sétjaną | regular`. `PROTO` and `PROTOFORM` are identical, so the aligned TSV is not currently using a substitute stage-form, a paradigm-cell retarget, or a separate reconstruction for the OE slot; the stored derivational input and the listed protoform are both `*sétjaną`, and the attested OE target is the infinitive `sittan` [Germanic/data/germanic-aligned-final.tsv:1019-1019].
- The row has no local OE problem flag. `oe_known_problems.tsv` contains no entry for row `2193`, `*sétjaną`, or `sittan`, so this lexeme is not currently tracked as an exception, broken derivation, or unresolved analogical replacement [Germanic/data/oe_known_problems.tsv:1-8].
- The row also remains uncovered in the audit infrastructure: `coverage_audit.md` lists `| 2193 | sit | sittan | regular | no | - | - | - | none |`, which means there is not yet a packet, research memo, or indexed DEV_NOTES fragment attached to it [Germanic/docs/lexeme_reports/coverage_audit.md:355-355].
- Repo-local lexical support agrees with the live row. `old_english_wiktionary.tsv` gives `sit    sittan`, with no rival OE lemma in that local source layer [Germanic/data/old_english_wiktionary.tsv:254-254]. Clark Hall likewise has `sit` as the present 3sg. of `sittan` and defines `sittan³` as “to ‘sit,’ sit down, recline ... remain, continue, be situated” [@ClarkHall1960]. [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:36583-36587]. Bright’s verb list gives `sittan, sæt sæton seten (5), sit` [@BrightCassidyRingler1971]. [docs/references/bright_anglo_saxon_reader.vision.txt:25021-25022].
- Comparative reference files support the same OE target but show different reconstruction layers. Kroonen’s headword is `*set(j)an- ... OE sittan` [@Kroonen2013, p. 434]. [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:22504-22519]. Campbell gives the explicit developmental chain `OE sittan < West Gmce. *sittjan < Prim. Gme. *sitjan- < *setjan-` [@Campbell1959, §112 n. 4]. [docs/references/campbell_old_english_grammar.txt:3741-3742]. Ringe–Taylor write `PGmc *sitjang ... > PWGmc */sitjan/ > OE sittan` [@RingeTaylor2014, p. 51]. [docs/references/ringe_taylor_linguistic_history_vol2.txt:3638-3642]. Fulk’s comparative grammar groups the same verb among inherited `*-io-` formations: `PIE *sed-io- > OIcel. sitja, OE sittan, OS sittian, OHG sitzen` [@Fulk2018, §4.4; §12.19]. [docs/references/fulk_comparative_grammar_early_germanic.vision.txt:3811-3812,16592-16593].
- The published live derivation already matches exactly. The compact trace report shows `PROTO: *sétjaną`, `EXPECTED: sittan`, `OUTPUTS: sittan`, with the rule sequence `PWGmc J Gemination` > `OE I Umlaut` > `OE Weak Tail Reduction` > `OE J Loss After Heavy` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4286-4305]. The full trace spells the same path out line by line: `PWGmcJGemination: *séttjaną`, then `OEHeavySyllableNasalApocope`, `OESecondaryNasalization`, `OEIUmlaut: *sittjąn`, `OEWeakTailReduction: *sittjan`, `OEJLossAfterHeavy: *sittan`, and finally `OldEnglishRemoveStars: sittan` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:29120-29233].

## Development-note summary

No dedicated row-`2193` narrative survives in `DEV_NOTES.md`. What survives is narrower and more indirect: a pair of current shared tables from the `*-ij-aną` / light-stem review, plus a general chronology note on short-stem `*-j-` verbs. Those fragments are still genuinely useful for this row, but they do **not** amount to a bespoke lexeme memo. The slice therefore has to do more explanatory work than a row whose DEV_NOTES already contain a focused block on the lexeme [Germanic/docs/DEV_NOTES.md:1750-1753,8940-8945,9020-9027].

The most row-relevant surviving DEV_NOTES evidence is the normalization audit that explicitly keeps `*setjăną` in the light-stem bucket. One table says `*setjăną` is a form “NOT Updated” because it is a light stem `(CVC)`; the later status table repeats that `*setjăną | set- (CVC) | light | ✓ correct` [Germanic/docs/DEV_NOTES.md:8940-8945,9022-9027]. For row `2193`, the practical force of those entries is clear: DEV_NOTES was not trying to replace the row’s input with a heavier `*-ij-` form, diagnose it as analogical, or move it into an exception bucket. The lexeme was treated as an ordinary short/light `*-j-` verb whose inherited shape was already suitable for the regular OE pathway.

The notation requires careful separation because the live row and the comparative references do **not** all write the same stage-form. The aligned row stores `PROTO = PROTOFORM = *sétjaną` [Germanic/data/germanic-aligned-final.tsv:1019-1019]. DEV_NOTES’ audit tables write `*setjăną`, which is best read as the same lexical item in older/internal working notation: no acute on the stressed vowel, breve on `ă`, and `-jăną` formatting used throughout that audit table [Germanic/docs/DEV_NOTES.md:8942-8944,9024-9026]. Campbell explicitly distinguishes chronological stages, giving `*setjan-` as the older form, `*sitjan-` as a later Primitive Germanic stage, and `*sittjan` as West Germanic [@Campbell1959, §112 n. 4]. [docs/references/campbell_old_english_grammar.txt:3741-3742]. Ringe–Taylor prefer the raised stage `*sitjang > */sitjan/ > OE sittan` [@RingeTaylor2014, p. 51]. [docs/references/ringe_taylor_linguistic_history_vol2.txt:3638-3642], while Kroonen keeps the broader dictionary headword `*set(j)an-` [@Kroonen2013, p. 434]. [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:22504-22519]. These are not competing OE targets and not evidence for a live `PROTO`/`PROTOFORM` split. They are notation layers and chronology layers for the same lexeme.

The live project behavior should therefore be stated in its own terms. In the current trace, the row begins from `*sétjaną`; `PWGmcJGemination` yields `*séttjaną`; OE-side nasal-apocope and secondary nasalization prepare the weak tail; `OEIUmlaut` raises `é`-written input to `i` in `*sittjąn`; `OEWeakTailReduction` gives `*sittjan`; and `OEJLossAfterHeavy` gives `*sittan`, which surfaces as `sittan` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:29139-29233]. That is a regular exact-match derivation in the live system, not a patched output. The row’s current target is therefore supported both by the implementation trace and by the comparative grammar tradition that expects a geminated `tt` present stem and OE `i`-vocalism for this verb [@Campbell1959, §112 n. 4; @RingeTaylor2014, p. 51; @Kroonen2013, p. 434]. [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4286-4305; docs/references/campbell_old_english_grammar.txt:3741-3742; docs/references/ringe_taylor_linguistic_history_vol2.txt:3638-3642; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:22504-22519].

The surviving shared chronology note in DEV_NOTES also matches the live trace well enough to matter here, even though its explicit example is `*satjan > ... > OE settan` rather than `sit`. DEV_NOTES says that standard descriptions place West Germanic consonant gemination before `*j` ahead of later i-mutation, and the current implementation was adjusted to respect that ordering [@Campbell1959, §§190 ff.; @Fulk2018, §6.15; @SieversBrunner1965, §§95, 227]. [Germanic/docs/DEV_NOTES.md:1750-1753]. Row `2193` now shows exactly that shape of derivation: gemination first (`*séttjaną`), then OE umlaut (`*sittjąn`), then later `j`-loss after the heavy syllable (`*sittan`) [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:29139,29190,29213-29214]. The vowel history differs from `settan` because the lexeme and reconstruction layer differ, not because the rule family differs.

What does **not** survive is equally important. No current DEV_NOTES passage says that OE should be anything other than `sittan`; no row-local memo preserves a superseded alternative like `*sitan`, `*sitan`, or a paradigmatically retargeted form; and no row-local problem report survives in `oe_known_problems.tsv` [Germanic/data/oe_known_problems.tsv:1-8]. The surviving evidence is therefore current but mostly indirect: enough for a detailed row dossier, probably not enough for confident index integration without overclaiming that DEV_NOTES contains a fuller lexeme-specific discussion than it actually does.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-8940-8945

- Source heading: `Forms NOT Updated (light stems or special cases)`
- Source line or section hint: `lines 8940-8945`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `light_stem`; `j_stem`; `notation_variant`; `regular_derivation`
- Recommended next use: `keep_as_shared_background`
- Shared with row IDs:

This fragment is the first surviving place where the row’s lexeme appears directly inside current DEV_NOTES. The table lists `*setjăną` among forms intentionally left alone, with the reason `Light stem (CVC)` [Germanic/docs/DEV_NOTES.md:8940-8945]. That wording matters for row `2193` because it says what the audit was **not** doing: it was not normalizing this lexeme to a heavier `*-ij-` stem, not marking it as analogical, and not flagging it as an exception. The fragment is still indirect, because it is part of a wider stem-weight audit rather than a row-specific philological note, but it is current and row-applicable.

### DEV_NOTES:line-9022-9027

- Source heading: `Light-stem verbs (keep -jăną)`
- Source line or section hint: `lines 9022-9027`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `light_stem`; `stem_weight`; `j_stem`; `current_validation`
- Recommended next use: `cite_in_final_report_if_needed`
- Shared with row IDs:

This is the strongest current DEV_NOTES fragment for the row, even though it is still a table rather than a prose memo. It names the same working-form directly: `*setjăną | set- (CVC) | light | ✓ correct` [Germanic/docs/DEV_NOTES.md:9022-9027]. The fragment is valuable because it turns the earlier “not updated” logic into a positive validation statement. For row `2193`, that means the surviving DEV_NOTES record does affirm that the short/light `*setj-` analysis is the intended one and that, within that audit, the form was judged correct rather than problematic.

### DEV_NOTES:line-1750-1753

- Source heading: `OE *-gj- chronology check (2026-01-22)`
- Source line or section hint: `lines 1750-1753`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `chronology`; `j_gemination`; `i_umlaut`; `short_stem_j_verbs`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs: `2173,2191`

This fragment is not lexeme-specific to `sit`, but it is still the clearest surviving DEV_NOTES statement of the ordered mechanism that the live `sittan` trace now shows. DEV_NOTES says that standard descriptions place West Germanic gemination before `*j` ahead of i-mutation, and that implementation was updated to respect that chronology [@Campbell1959, §§190 ff.; @Fulk2018, §6.15; @SieversBrunner1965, §§95, 227]. [Germanic/docs/DEV_NOTES.md:1750-1753]. The explicit example there is `*satjan > ... > settan`, not `sit`; however, the same rule ordering is visible in row `2193`’s exact-match trace, where gemination precedes `OEIUmlaut` and later `j`-loss [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:29139,29190,29213-29214]. This fragment is therefore suitable as background, but not as sole authority for indexing the row.

## Superseded or diagnostic material

- No dedicated superseded row-`2193` analysis was found. There is no surviving DEV_NOTES passage that records an abandoned OE target, an older wrong row counterpart, or a hidden exception classification for `sittan` [Germanic/docs/DEV_NOTES.md:8940-8945,9022-9027; Germanic/data/oe_known_problems.tsv:1-8].
- The main diagnostic caution is notation drift, not lexical disagreement. Live TSV `*sétjaną`, DEV_NOTES `*setjăną`, Campbell’s older `*setjan-` and later `*sitjan-`, Campbell’s West Germanic `*sittjan`, Kroonen’s headword `*set(j)an-`, and Ringe–Taylor’s `*sitjang > */sitjan/` are best treated as chronological or editorial layers for one lexeme, not as evidence for multiple row policies [@Campbell1959, §112 n. 4; @Kroonen2013, p. 434; @RingeTaylor2014, p. 51]. [Germanic/data/germanic-aligned-final.tsv:1019-1019; Germanic/docs/DEV_NOTES.md:8942-8944,9024-9026; docs/references/campbell_old_english_grammar.txt:3741-3742; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:22504-22519; docs/references/ringe_taylor_linguistic_history_vol2.txt:3638-3642].
- Because the surviving DEV_NOTES material is mainly shared audit-table evidence rather than a focused lexeme memo, this row is better read as a well-behaved regular derivation with sparse project notes than as a row whose documentation history has already been fully consolidated. The slice is therefore useful as a dossier, but the evidence base remains thinner than for rows with direct quotation-rich DEV_NOTES blocks.

## Open questions for later work

- If later packet work is undertaken, capture direct quotation-rich literature extracts for the `*setjan- / *sitjan- / *sittjan > sittan` sequence so the row no longer depends primarily on shared audit tables and live trace output.
- If project-wide reconstruction policy is normalized later, decide whether rows like `2193` should continue to display the earlier-style input `*sétjaną` or be harmonized to a later stage-form such as `*sitjaną`; current evidence suggests that such a change would be a notation-policy decision, not a different OE target.
- If `dev_notes_slices/index.tsv` is revised later, re-evaluate only after there is a denser row-local DEV_NOTES or packet citation. The present fragment set is usable for a slice but still comparatively thin for index integration.
