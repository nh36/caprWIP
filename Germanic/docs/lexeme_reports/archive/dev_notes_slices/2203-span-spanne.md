---
row_id: 2203
concept: span
counterpart: spanne
proto: *spannō
protoform: *spánnai
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2203-span-spanne.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2203-span-spanne.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2203 span / spanne

## Current row state

- CONCEPT: `span`
- COUNTERPART: `spanne`
- PROTO: `*spannō`
- PROTOFORM: `*spánnai`
- DERIVATION_CLASS: `late_analogy`
- Live TSV note: `Dat.sg. paradigm-cell (Brunner §252). Fem. ō-stem dat.sg. *-ai preserves medial geminate; unstressed word-final *ai→*ē (R/T §6.1.5; §17.12).` [Germanic/data/germanic-aligned-final.tsv:1057]
- `oe_known_problems.tsv`: no entry for row 2203, `spanne`, `*spánnai`, or `*spannō` turned up in the required check, so the row is not currently being tracked as an unresolved exception [Germanic/data/oe_known_problems.tsv:1-9].
- Existing packet / memo stem already matches the row and should govern slice naming: `2203-span-spanne.md` [Germanic/docs/lexeme_reports/packets/2203-span-spanne.md:1; Germanic/docs/lexeme_reports/research_memos/2203-span-spanne.md:1].
- Current row policy must keep the three-way distinction explicit: lexeme-level `PROTO` `*spannō`, row-specific `PROTOFORM` `*spánnai`, and OE target `spanne`. The selected `PROTOFORM` is a paradigm-cell input, not a replacement lexeme headword [Germanic/data/germanic-aligned-final.tsv:1057; Germanic/docs/lexeme_reports/research_memos/2203-span-spanne.md:42-48].

## Detailed development-note summary

The live row is a deliberate **paradigm-cell** solution for a feminine ō-stem noun. DEV_NOTES first records the underlying problem in plain terms: lexeme-level `*spannō` gives OE `span`, but the row targets `spanne`, so the noun has to be modeled through an oblique singular cell instead of the citation-form nominative [DEV_NOTES:line-13811-13818; Germanic/data/germanic-aligned-final.tsv:1057]. That is the essential current claim. `PROTO` remains the cognate-set headword `*spannō`; `PROTOFORM` is the chosen dative singular `*spánnai`; `COUNTERPART` is the selected OE oblique form `spanne` [Germanic/data/germanic-aligned-final.tsv:1057; @SieversBrunner1965, §252].

DEV_NOTES preserves an important failed detour before reaching that solution. The first attempt tried to parallel the masc. a-stem fixes (`mannes`, `bannes`) by using a fem. ō-stem gen.sg. in `*-āz`. That route failed because final `*z` deletes too early, leaving word-final `*-ā > *-a`; the relevant unstressed-a fronting rule then cannot apply, because the ending no longer has a following consonant. DEV_NOTES therefore records the bad outputs explicitly: `*spannāz -> spanna` and `*spannās -> spannes`, neither of which yields the row target `spanne` [DEV_NOTES:line-13819-13848]. This material is no longer current row policy, but it is worth keeping because it explains why the project did **not** stay with a genitive-singular analysis.

The durable solution is the switch to the dative singular ending `*-ai`. DEV_NOTES states that for feminine ō-stems the dat.sg. gives the same OE surface ending `-e` needed here, but through a different phonological history from the failed gen.sg. path [DEV_NOTES:line-13850-13867; @SieversBrunner1965, §252]. The key source support, quoted directly in DEV_NOTES from Ringe-Taylor, is that "unstressed *ai was usually monophthongized to *é throughout the NWGmc" and that there was a "NWGmc merger of unstressed *ai with *é" [DEV_NOTES:line-13880-13896; @RingeTaylor2014, §6.1.5]. Once that applies, the row's selected derivation is straightforward: `*spánnai -> *spannē -> *spanne`, with the medial geminate preserved and the final unstressed vowel shortened to `-e` [DEV_NOTES:line-13915-13919,28120-28124; @RingeTaylor2014, §§6.1.5, 17.12].

Project chronology still matters because DEV_NOTES preserves two different notational stages. The April 2026 note first proposed marking the weak-tail diphthong as `*spannăi`, treating unstressed `*ăi` as a separate engineering symbol from stressed `*ai` [DEV_NOTES:line-13921-14039]. That is now superseded. The current account is §17.12, which explicitly eliminates the breve and argues that for this corpus **word-final position already captures the relevant unstressed environment**. DEV_NOTES says that word-final `*ai` is "a fully equivalent phonetic condition" for the distinction the breve had been marking, rewrites the row to `*spánnai`, and verifies the exact desired outcome `*spánnai -> spanne` with no stressed-`*ai` regressions [DEV_NOTES:line-28076-28124; @RingeTaylor2014, §§6.1.5, 17.12]. For any replacement working note, `*spánnai` is therefore the only current `PROTOFORM`; `*spannăi` / `*spánnăi` survives only as project history.

The support is adequate for row policy but still somewhat thin for broader lexicographical claims. The packet and memo both agree that the current repo solution is the **post-§17.12** state and that the row is best treated as a dative-singular paradigm-cell noun entry, not a simple citation-form equation [Germanic/docs/lexeme_reports/packets/2203-span-spanne.md:17-44; Germanic/docs/lexeme_reports/research_memos/2203-span-spanne.md:33-49,56-60]. At the same time, the memo also warns that the local lexical-table check it performed found citation-form `spann`, not an independently documented dictionary headword `spanne`, so later report work should avoid overclaiming direct lemma status for `spanne` until a stronger textual or lexicographical witness is added [Germanic/docs/lexeme_reports/research_memos/2203-span-spanne.md:35-38,52-55].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-13807-13848

- Source heading: `Fem. ō-stem gen.sg. paradigm-cell for span (2026-04-06)` / `Problem` / `Attempted solutions`
- Source line or section hint: `lines 13807-13848`
- Fragment type: `lexeme_specific`
- Status: `superseded`
- Issue tags: `genitive_singular`; `failed_route`; `chronology`; `paradigm_cell`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This opening span note should be preserved because it records the exact dead end that later summaries otherwise flatten away. DEV_NOTES explains why the apparently obvious fem. ō-stem gen.sg. route fails in the cascade: final `*z` deletes too early, word-final `*a` does not front, and the outputs stay `spanna` or `spannes` instead of `spanne` [DEV_NOTES:line-13819-13848]. The fragment is superseded as a proposed solution, but it remains diagnostic evidence for why the row moved away from `*-āz` and toward the dative singular.

### DEV_NOTES:line-13850-13920

- Source heading: `Solution: Use dat.sg. instead of gen.sg.` / `Testing dat.sg. *-ai approach (2026-04-06)` / `Research: Stressed vs. Unstressed *ai Monophthongization`
- Source line or section hint: `lines 13850-13920`
- Fragment type: `lexeme_specific`
- Status: `current_with_stale_notation`
- Issue tags: `dative_singular`; `unstressed_ai`; `geminate_preservation`; `source_quote`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the core explanatory fragment. It states the row decision explicitly: use the fem. ō-stem dat.sg. rather than the gen.sg., because both give OE `-e` but only the dat.sg. path avoids the word-final fronting problem [DEV_NOTES:line-13850-13867; @SieversBrunner1965, §252]. It also preserves the most useful direct quotations from Ringe-Taylor: "unstressed *ai was usually monophthongized to *é throughout the NWGmc" and "the NWGmc merger of unstressed *ai with *é" [DEV_NOTES:line-13880-13886; @RingeTaylor2014, §6.1.5]. The final worked chain `*spannai -> *spannē -> *spanne` is still correct in substance even though the notation and implementation details were later cleaned up [DEV_NOTES:line-13915-13919].

### DEV_NOTES:line-13921-14039

- Source heading: Input Notation / Revised analysis: Two separate changes for *ai / Implementation completed (2026-04-06)
- Source line or section hint: `lines 13921-14039`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `breve_notation`; `engineering_diacritic`; `old_protoform`; `project_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This fragment preserves the obsolete `*spannăi` / `*spánnăi` stage. DEV_NOTES here treats unstressed `*ăi` as a separate symbol, rewrites the row with the breve-marked ending, and records a successful test under that older implementation [DEV_NOTES:line-13921-14039]. It is still useful chronology, but it is no longer current row policy because §17.12 later removes the breve and returns the row to plain `*spánnai`.

### DEV_NOTES:line-28061-28135

- Source heading: `§17.12 — Eliminating the unstressed-diphthong breve {*ăi} (2026-04-24)`
- Source line or section hint: `lines 28061-28135`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `current_protoform`; `word_final_ai`; `notation_cleanup`; `verification`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the present controlling fragment. DEV_NOTES says the row's old breve marker survived only in the fem. ō-stem dat.sg. ending, then argues that word-final `*ai` is "a fully equivalent phonetic condition" for the stressed/unstressed distinction because root-syllable `*ai` is never word-final while inflectional `*-ai` is [DEV_NOTES:line-28065-28095]. The section then rewrites the row from `*spánnăi` to `*spánnai`, updates the grammar to treat word-final `*ai` as the `*ē` outcome, and verifies `*spánnai -> spanne` without regressions elsewhere [DEV_NOTES:line-28097-28124; @RingeTaylor2014, §§6.1.5, 17.12]. This is the fragment that should govern any future report or index entry.

### DEV_NOTES:line-25306-25308

- Source heading: `Path α — paradigm-cell PROTOFORM (Lautgesetzlich via Campbell's own account)`
- Source line or section hint: `lines 25306-25308`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `diagnostic_only`
- Issue tags: `project_precedent`; `stale_row_number`; `old_protoform`; `shared_methodology`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs: `2011; 2119; 2152`

This later methodology summary is useful only with a warning label. It correctly treats `spanne` as a precedent for encoding the relevant paradigm cell rather than forcing the nominative, but it still mislabels the row as `2140` and still cites the obsolete breve-marked form `*spannăi` [DEV_NOTES:line-25306-25308]. Keep it only as evidence that row 2203 became part of the project's broader paradigm-cell method; do not reuse it as clean current row metadata.

## Superseded or diagnostic material

The main superseded material is the abandoned **gen.sg.** route at `DEV_NOTES:line-13807-13848`. It is valuable because it shows that the project did not jump directly to the final dat.sg. solution; the genitive failed for specific chronological reasons in the cascade.

The second major superseded layer is the old **breve-marked unstressed diphthong** stage. `DEV_NOTES:line-13921-14039` records a real successful implementation for `*spannăi`, but §17.12 later decides that the engineering diacritic is unnecessary and rewrites the row as plain `*spánnai` [DEV_NOTES:line-28061-28135]. Any prose that still cites `*spannăi` / `*spánnăi` should now be read as project history, not current analysis.

The shared precedent line at `DEV_NOTES:line-25306-25308` is also diagnostic only. Its methodological point is still sound, but the row number and protoform spelling are stale, so it should never be quoted without correction.

## Open questions for later work

- Add a stronger textual or lexicographical citation for OE `spanne` if the row is ever turned into a fully indexable lexeme note. Current repo-local support is good for the paradigm-cell analysis but thinner for independent lemma-style attestation [Germanic/docs/lexeme_reports/research_memos/2203-span-spanne.md:52-55].
- If a final report is drafted, keep the distinction explicit between lexeme-level `PROTO` `*spannō` and row-level `PROTOFORM` `*spánnai`; do not let the successful oblique input collapse into a false claim that `*spánnai` is the noun's lexeme headword.
- If cross-row methodology summaries continue using `spanne` as a precedent, update stale inherited references so they cite row `2203` and the current post-§17.12 spelling `*spánnai`, not `2140` / `*spannăi`.
