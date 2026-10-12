---
row_id: 1994
concept: dove
counterpart: -
proto: "*dūbōn"
protoform: "*dūbōn"
derivation_class:
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/final_vowel_missing_analysis.md
current_status: uncertain
needs_literature_agent: yes
---

# DEV_NOTES material — 1994 dove / - (reconstructed *dūfe)

## Current row state

- The live OE row currently reads `ID 1994 | CONCEPT dove | COUNTERPART - | PROTO *dūbōn | PROTOFORM *dūbōn`, with blank `DERIVATION_CLASS`. Its note is explicit on both the reconstruction and the lexical warning: `Unattested OE; reconstructed *dūfe. | Attested OE culfre is not cognate with ModE dove; reconstructed *dūfe unattested.` [Germanic/data/germanic-aligned-final.tsv:246-246]
- Row-local repo sources preserve a specific reconstructed OE form even though the live counterpart field stays dashed. In `germanic-aligned-final.tsv`, the OE `TOKENS` field is `* d ū f e`, and `old_english_wiktionary.tsv` likewise gives `dove	-	inh	template:inh (unattested; reconstructed *dūfe) (attested OE culfre not cognate; reconstructed *dūfe unattested)` [Germanic/data/germanic-aligned-final.tsv:246-246; Germanic/data/old_english_wiktionary.tsv:60-60]. On that basis, this slice uses the filename stem `dūfe` while keeping metadata `counterpart: -`.
- No row-specific packet or research memo file was located for row `1994` in the current repo pass. The closest directly relevant shared analysis is `final_vowel_missing_analysis.md`, which identifies `*-ōn` forms as a recurrent source of missing-final-vowel problems and states that the current FST does not yet convert `*-ōn` weak nouns to OE `-e/-a` outcomes [Germanic/docs/analysis/final_vowel_missing_analysis.md:16-24,41-60].
- `oe_known_problems.tsv` currently has no entry for `*dūbōn`, `dove`, or row `1994`, so the lexeme is not presently being tracked there as a named OE exception bucket [Germanic/data/oe_known_problems.tsv:1-8].
- Current sandbox diagnostics are worth recording, but only as diagnostics. The OE sandbox JSON already pairs `concept: "dove"` / `proto: "*dūbōn"` with `counterpart: "*dūfe"`, yet reports `outputs: []`; the stage-trace file shows the derivation surviving all the way to surface `dūbōn` and flags `first_failing_stage: "ProtoRhoticFronting"` [Germanic/tmp/old_english_sandbox_results_current.json:592-596; Germanic/tmp/old_english_sandbox_results_with_stages.json:8827-8966].

## Development-note summary

Direct review finds no lexeme-specific DEV_NOTES section for row `1994`, no heading for `dove`, `*dūbōn`, `*dūfe`, or `culfre`, and no surviving DEV_NOTES passage that explicitly audits the row note's non-cognacy claim. That negative result is itself important: the live row does preserve a specific unattested OE proposal, but the repo does not currently preserve a dedicated DEV_NOTES argument explaining why `*dūfe` should be the right reconstruction or why `culfre` should be excluded.

The materially relevant DEV_NOTES support is therefore indirect and shared. First, DEV_NOTES' mismatch-bucket cleanup explicitly says OE diagnostics need a bucket for “intervocalic stops (VbV) that should be fricatives (VfV),” illustrated by forms such as `*bebruz → beber` where the expected OE output is `befer` [Germanic/docs/DEV_NOTES.md:1564-1576]. That is not a dove note, but it is directly relevant to the consonant side of the reconstruction: any path from `*dūbōn` to `*dūfe` depends on the same general expectation that medial `*b` in vowel environment should continue as OE fricative `f`, not remain stop `b`.

Second, DEV_NOTES' older apocope investigation explicitly warns that some collateral failures may be cases of “weak nouns being treated as strong” [Germanic/docs/DEV_NOTES.md:1639-1641]. That brief remark becomes materially relevant here because row `1994` is a `*-ōn` item, and the shared analysis file linked above treats `*-ōn` weak nouns as exactly the sort of forms where the present FST can miss the expected OE final vowel [Germanic/docs/analysis/final_vowel_missing_analysis.md:22-24,41-60]. In other words, even without a row-specific dove section, DEV_NOTES does preserve a project-level warning that weak-noun morphology is one place where OE outputs can go wrong.

The strongest shared DEV_NOTES passage is the later note on word-final long `*ō`. DEV_NOTES distinguishes the ordinary PNWGmc raising of word-final `*ō > u` from a different path where bimoric `*ō` is not yet word-final because an ending still follows it; once that ending is lost, DEV_NOTES says the surviving long vowel yields PWGmc `*a` and then OE `-e` by unstressed fronting. The worked example is exactly fem. n-stem nom.sg. `*tungōn → *tungō̃ → PWGmc *tunga → OE tunge`, followed by the explicit statement: “For fem. n-stems, modelled by `NWGmcNStemNLoss` ... This covers the n-stem case” [Germanic/docs/DEV_NOTES.md:2722-2739]. For row `1994`, that is the clearest current in-repo DEV_NOTES support for taking a `*-ōn` feminine toward an OE `-e` outcome rather than leaving the form at unreduced `-ōn`.

Taken together, the surviving DEV_NOTES material supports only a cautious working conclusion. The repo does preserve `*dūfe` as the intended unattested OE form, and shared DEV_NOTES discussions make that shape phonologically plausible at the level of `*-ōn > -e` and intervocalic `*b > f`. But the lexeme still lacks a row-specific DEV_NOTES dossier, lacks a packet or memo, and lacks a dedicated in-repo literature audit of the claim that attested OE `culfre` is non-cognate. The slice therefore needs to preserve the reconstruction and its plausibility without overstating the current documentary support.

## Relevant DEV_NOTES fragments

### DEV_NOTES:no-exact-hit-for-1994-dove-dūfe

- Source heading: no exact row `1994` / `dove` / `*dūbōn` / `*dūfe` / `culfre` heading survives in `Germanic/docs/DEV_NOTES.md`
- Source line or section hint: direct review found no securely attachable row-specific note
- Fragment type: `unclear_needs_human_review`
- Status: `uncertain`
- Issue tags: `missing_row_specific_authority`; `unattested_target`; `negative_result`; `needs_source_audit`
- Recommended next use: `check_against_literature`
- Shared with row IDs:

This negative result is the first fact that later work needs to preserve. The live row contains a fairly strong claim — unattested reconstructed `*dūfe`, with attested `culfre` excluded as non-cognate — but no surviving DEV_NOTES section currently explains where that claim came from or what primary/secondary literature was used to reach it [Germanic/data/germanic-aligned-final.tsv:246-246]. Any later reporting should therefore avoid implying that the current repo already contains a row-specific DEV_NOTES defense of the reconstruction.

### DEV_NOTES:line-1564-1576

- Source heading: `Consonant Mismatch Bucket Refinement (2026-02-07)`
- Source line or section hint: `lines 1564-1576`
- Fragment type: `shared_rule_discussion`
- Status: `current_but_indirect`
- Issue tags: `intervocalic_b_to_f`; `shared_consonant_logic`; `mismatch_bucketing`
- Recommended next use: `cite_with_scope_caution`
- Shared with row IDs: `1936`; `2027`; other `VbV > VfV` OE rows

This fragment is shared rather than dove-specific, but it does preserve the exact consonant expectation that the reconstruction `*dūfe` would need. DEV_NOTES says the tooling now detects “intervocalic stops (VbV) that should be fricatives (VfV)” and illustrates the problem with `*bebruz → beber` where the expected OE result is `befer` [Germanic/docs/DEV_NOTES.md:1566-1576]. For row `1994`, the relevance is structural: `*dūbōn` likewise places `*b` between vowels before the weak ending is reduced, so any serious defense of `*dūfe` would lean on this same general OE fricativization expectation. What the fragment does **not** do is show that DEV_NOTES ever applied that logic specifically to `dove`.

### DEV_NOTES:line-1639-1641

- Source heading: `Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY`
- Source line or section hint: `lines 1639-1641`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded_but_relevant`
- Issue tags: `weak_noun_morphology`; `collateral_damage`; `final_vowel_history`
- Recommended next use: `use_as_diagnostic_background_only`
- Shared with row IDs: broad `final_vowel_missing` cohort, especially weak nouns

This fragment is brief, but it is one of the only DEV_NOTES lines that directly points toward the kind of morphological failure row `1994` appears to involve. DEV_NOTES says the collateral damage from the old apocope experiment needed case-by-case review to see whether some items were “weak nouns being treated as strong” [Germanic/docs/DEV_NOTES.md:1639-1641]. For the dove row, that is a meaningful diagnostic because the shared `final_vowel_missing_analysis.md` later identifies `*-ōn` weak nouns as a class where the present FST still lacks the reduction to OE `-e/-a` [Germanic/docs/analysis/final_vowel_missing_analysis.md:22-24,41-60]. The fragment should therefore be kept, but clearly marked as diagnostic history rather than as a settled row-specific explanation.

### DEV_NOTES:line-2722-2739

- Source heading: `Path B: PWGmc Unrounding (bimoric *ō that becomes word-final LATER)`
- Source line or section hint: `lines 2722-2739`
- Fragment type: `shared_rule_background`
- Status: `current`
- Issue tags: `feminine_n_stem`; `*-ōn_to_-e`; `surviving_bimoric_ō`; `unstressed_fronting`
- Recommended next use: `cite_if_explaining_why_*dūfe_is_phonologically_plausible`
- Shared with row IDs: weak feminine `*-ōn` rows

This is the strongest shared DEV_NOTES passage for the row's final vowel. DEV_NOTES says that when bimoric `*ō` only becomes word-final after loss of `*-z`, `*-n`, or similar endings, the result is PWGmc `*a` and then OE `-e`, and it gives the explicit weak-feminine example `*tungōn ... → PWGmc *tunga → OE tunge` [Germanic/docs/DEV_NOTES.md:2722-2737]. It then states that the current FST already models this path for fem. n-stems: “This covers the n-stem case” [Germanic/docs/DEV_NOTES.md:2736-2739]. For row `1994`, this is not yet a proof that `*dūfe` is the correct lexeme-level reconstruction, but it is the clearest surviving DEV_NOTES support for the row note's final `-e`.

## Superseded or diagnostic material

- The row's claim that attested OE `culfre` is not cognate with ModE `dove` currently lives in row-local source notes, not in an identified DEV_NOTES source audit. That claim should therefore be repeated only with explicit source caution until a packet, memo, or literature review pins it down more securely [Germanic/data/germanic-aligned-final.tsv:246-246; Germanic/data/old_english_wiktionary.tsv:60-60].
- Current sandbox JSON should be treated as diagnostic only. It already wires the lexeme to `counterpart: "*dūfe"`, but it simultaneously reports `outputs: []`, leaves the unreduced shape visible through most stages, and ends with surface `dūbōn`; this is evidence of present implementation trouble, not of settled row policy [Germanic/tmp/old_english_sandbox_results_current.json:592-596; Germanic/tmp/old_english_sandbox_results_with_stages.json:8827-8966].
- `Germanic/docs/analysis/final_vowel_missing_analysis.md` is useful shared analysis, not a row-specific dossier. It makes the `*-ōn` weak-noun problem legible and probably explains why a form like `*dūfe` would still be undergenerated, but it does not independently establish that `*dūfe` is the right lexeme-level reconstruction for OE `dove` [Germanic/docs/analysis/final_vowel_missing_analysis.md:22-24,41-60].

## Open questions for later work

- Find the literature behind the live row note: specifically, what source supports reconstructed OE `*dūfe`, and what source supports the claim that attested OE `culfre` is not cognate with this Germanic set?
- Decide whether the live row should continue to keep `COUNTERPART = -` with note-level `*dūfe`, or whether the reconstruction is strong enough to be promoted into the counterpart field as an explicitly reconstructed target.
- If the OE grammar is revisited, check whether row `1994` belongs concretely in the weak-`*-ōn` / final-vowel-missing repair set and whether the empty-output sandbox state can be resolved without special-casing the lexeme.
- Unless a row-specific memo or literature-backed audit is added, this slice should probably remain **no-index** or diagnostic-only. The repo preserves a plausible reconstruction, but current DEV_NOTES support is still shared and indirect rather than a proper lexeme dossier.
