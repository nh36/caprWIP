---
row_id: 1935
concept: ball
counterpart: -
proto: "*bálluz"
protoform: "*bálluz"
derivation_class:
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
current_status: uncertain
needs_literature_agent: yes
---

# DEV_NOTES material — 1935 ball / - (reconstructed *beall)

## Current row state

- The live Old English row reads `CONCEPT = ball`, `COUNTERPART = -`, `PROTO = *bálluz`, `PROTOFORM = *bálluz`, with blank `DERIVATION_CLASS`. Its row note is explicit: `Unattested OE; reconstructed *beall.` [Germanic/data/germanic-aligned-final.tsv:12-12]
- Repo-local OE source data preserves the same distinction rather than promoting the reconstruction into the OE-form field. `old_english_wiktionary.tsv` gives `ball	-	inh	template:inh (unattested; reconstructed *beall)`, so the reconstruction is real row-local evidence but still sits outside the live `COUNTERPART` column [Germanic/data/old_english_wiktionary.tsv:4-4].
- On that basis, this slice uses the filename stem `beall` while keeping metadata `counterpart: -`. The repo does clearly preserve a specific reconstructed OE proposal, but the live row still distinguishes that proposal from an adopted counterpart field [Germanic/data/germanic-aligned-final.tsv:12-12; Germanic/data/old_english_wiktionary.tsv:4-4].
- No row-specific packet or research memo file for row `1935` is present in the current repo. The only directly attached auxiliary analysis located for this pass is `Germanic/docs/analysis/arestoration_r_l_research.md`, which lists row `1935` as ``*bálluz`` / `-` with the comment `geminate *ll* + breaking; out of scope` [Germanic/docs/analysis/arestoration_r_l_research.md:722-726].
- `oe_known_problems.tsv` has no entry for `*bálluz` or for this row. That absence means only that the item is not presently bucketed there as a tracked exception; it does not itself supply a positive derivational account for `*beall` [Germanic/data/oe_known_problems.tsv:1-8].

## Development-note summary

No lexeme-specific DEV_NOTES dossier for row `1935` survives in `Germanic/docs/DEV_NOTES.md`. The materially relevant DEV_NOTES support is instead shared implementation/debug material about what the grammar was doing with this lexeme class and one later analytical table explicitly marking `*bálluz` as a geminate-`*ll` breaking case outside a different research question. That thinness has to be preserved explicitly: the reconstruction `*beall` is row-local and repeated in repo OE source data, but it is **not** presently backed by a dedicated DEV_NOTES argument explaining why this row's OE side should stay dashed in the table while the note-level reconstruction remains `*beall` [Germanic/data/germanic-aligned-final.tsv:12-12; Germanic/data/old_english_wiktionary.tsv:4-4].

The earliest directly relevant DEV_NOTES material is the December 2025 tail diagnostic. There the project was still fighting stray final high vowels, and `ball` appears as one of the sample bad outputs: “Sample `-i/-u` outputs: `ballu` (ball), `bebru` (beaver), `balgi` (belly), `crafti` (craft), `bugu` (bough)” [Germanic/docs/DEV_NOTES.md:2481-2485]. This matters because it preserves a concrete stage in the row's implementation history: before the heavy-syllable apocope repair, the grammar was not even getting rid of final `-u`, so any later discussion of `*beall` has to remember that the first visible problem was a tail problem (`ballu`), not yet the quality of the root vowel.

The next DEV_NOTES block records the partial repair. In the “High-vowel loss debug” note, the grammar is said to have been nondeterministic, “yielding both apocopated and non-apocopated outputs (e.g., `ballu` + `ball`)”; the fix rewrites final `*i/*u` in heavy contexts and then deletes them, with verification that `balluz/balgiz/bebruz` now yield “a **single** output at each stage, with apocope firing deterministically in heavy contexts” [Germanic/docs/DEV_NOTES.md:2509-2518]. That is important but limited. It explains how the project got from a bad `ballu` tail to deterministic loss of final high vowel, but it does **not** supply a lexeme-specific explanation of the expected OE broken-vowel target `*beall`. In other words, DEV_NOTES here documents cleanup from `ballu` to `ball`-type output, not a completed argument from `*bálluz` to reconstructed `*beall`.

The only later DEV_NOTES passage that names the row more conceptually is the cluster inventory used during the A-restoration research pass. There row `1935` is listed as `*bálluz | — | geminate *ll*, not *Cl*` [Germanic/docs/DEV_NOTES.md:30606-30611]. The paired analysis file restates the point in slightly fuller form: row `1935` is ``*bálluz`` / `-` with comment `geminate *ll* + breaking; out of scope` [Germanic/docs/analysis/arestoration_r_l_research.md:722-726]. That is a real project judgement and should be preserved. It says the row belongs with OE breaking before geminate `ll`, but that the specific research thread in question was not attempting to solve it. So current DEV_NOTES support is enough to say that `ball` is not an arbitrary unattested placeholder and that the row belongs to a breaking environment, but it is still too thin to count as a full row-local defense of reconstructed `*beall`.

For replacement-note purposes, the practical conclusion is conservative. The repo clearly preserves `*beall` as the intended unattested OE proposal, so the filename should reflect it. But the live table still keeps `COUNTERPART = -`, DEV_NOTES only documents shared phonological debugging plus an out-of-scope classification, and no row-specific memo currently bridges those pieces into a settled lexeme report. This slice should therefore preserve the reconstruction, the distinction, and the documentary gap all at once rather than collapsing them into a stronger claim than the repo presently supports [Germanic/data/germanic-aligned-final.tsv:12-12; Germanic/data/old_english_wiktionary.tsv:4-4; Germanic/docs/DEV_NOTES.md:2509-2518,30606-30611].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2481-2485

- Source heading: `Ending diagnostics (old_english.bin)`
- Source line or section hint: `lines 2481-2485`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `final_high_vowel`; `ballu_output`; `shared_tail_diagnostic`
- Recommended next use: `use_to_explain_old_failure_state`
- Shared with row IDs: `1934`; `1943`; `1981`; `2107`

This fragment preserves the first explicit mention of the lexeme in DEV_NOTES. The note says: “Sample `-i/-u` outputs: `ballu` (ball), `bebru` (beaver), `balgi` (belly), `crafti` (craft), `bugu` (bough)” [Germanic/docs/DEV_NOTES.md:2484-2484]. For row `1935`, its value is historical/diagnostic. It shows that the project had a concrete OE-generation problem for this lexeme family, but that the problem being debugged at this stage was stray final `-u`, not yet the full unattested target-selection question around `*beall`.

### DEV_NOTES:line-2509-2518

- Source heading: `High-vowel loss debug (2025-12-21)`
- Source line or section hint: `lines 2509-2518`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `heavy_syllable_apocope`; `nondeterminism_fix`; `ballu_plus_ball`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1934`; `1943`; `1981`; `2107`

This is the most important current DEV_NOTES fragment for row `1935`, even though it is shared rather than lexeme-specific. DEV_NOTES says the weight-marker rule had been “yielding both apocopated and non-apocopated outputs (e.g., `ballu` + `ball`)” and that the repair verified `balluz/balgiz/bebruz` as single-output probes after heavy-context apocope [Germanic/docs/DEV_NOTES.md:2510-2518]. For this row, the fragment establishes one narrow but solid point: final `-u` persistence was recognized as a grammar bug and then repaired. It does **not** by itself explain why the note-level reconstruction is `*beall` rather than simple `ball`, but it is the key surviving DEV_NOTES evidence for the row's implementation history.

### DEV_NOTES:line-30606-30611

- Source heading: `Words in the TSV with proto *-aCl-* or *-aCr-* before a back-vowel tail`
- Source line or section hint: `lines 30606-30611`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `geminate_ll`; `breaking_environment`; `out_of_scope_classification`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1975`; `2002`; `2037`; `2052`

This fragment is brief but materially relevant because it classifies the row structurally rather than just naming a bad output. DEV_NOTES' table lists row `1935` as `*bálluz | — | geminate *ll*, not *Cl*` [Germanic/docs/DEV_NOTES.md:30609-30611]. That means the row was consciously recognized as a breaking/geminate-`ll` case during later analytical work, but also excluded from the narrower A-restoration question then under investigation. For replacement-note purposes, this is the best surviving project-level clue that `*beall` belongs to a real phonological expectation-space rather than being a random unattested guess.

## Superseded or diagnostic material

- Current sandbox diagnostics are useful but should be labeled diagnostic only. `old_english_sandbox_results_current.json` still pairs `ball` with `counterpart: "*beall"` yet reports `outputs: []`, and the stage-trace JSON shows the derivation collapsing to surface `ball` with `first_failing_stage: "ProtoRhoticFronting"` [Germanic/tmp/old_english_sandbox_results_current.json:19-23; Germanic/tmp/old_english_sandbox_results_with_stages.json:289-429]. These files are evidence that the reconstruction is already wired into some repo diagnostics, but they are not DEV_NOTES authority and do not override the live row's dashed counterpart field.
- The absence of a packet, research memo, or `oe_known_problems.tsv` entry is also diagnostic rather than probative. It means the row is underdocumented in current repo infrastructure, not that the derivation to `*beall` has already been settled [Germanic/data/oe_known_problems.tsv:1-8].
- The most important documentary caution is that `*beall` presently comes from row-local source notes (`germanic-aligned-final.tsv` and `old_english_wiktionary.tsv`), not from a dedicated lexeme-specific DEV_NOTES argument. Later writers should not silently upgrade that distinction away [Germanic/data/germanic-aligned-final.tsv:12-12; Germanic/data/old_english_wiktionary.tsv:4-4].

## Open questions for later work

- Write a dedicated memo on whether and how PGmc `*bálluz` should produce reconstructed OE `*beall`, including the exact role of breaking before geminate `ll` and whether any additional rule ordering is needed beyond final high-vowel apocope.
- Decide whether row `1935` should continue to keep `COUNTERPART = -` with note-level `*beall`, or whether the reconstruction is now strong enough to be promoted into the counterpart field as an explicit reconstructed target.
- If this row is ever proposed for indexing, it should probably wait for a row-specific memo or literature-backed derivational note. At present the slice is useful as a replacement working note, but the surviving DEV_NOTES support is still mostly shared/debugging material rather than a full lexeme dossier.
