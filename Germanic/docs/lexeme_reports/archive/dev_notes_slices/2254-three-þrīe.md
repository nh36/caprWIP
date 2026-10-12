---
row_id: 2254
concept: three
counterpart: þrīe
proto: *θréjez
protoform: *θréjez
derivation_class: attested_variant
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2254-three-þrīe.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2254-three-þrīe.md
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2254 three / þrīe

## Current row state

- CONCEPT: `three`
- COUNTERPART: `þrīe`
- PROTO: `*θréjez`
- PROTOFORM: `*θréjez`
- DERIVATION_CLASS: `attested_variant`
- Live TSV note: `Target retargeted from þrī (late-WS reduction) to þrīe (regular early-WS m.nom/acc., Campbell §683); see DEV_NOTES §17.43.` [Germanic/data/germanic-aligned-final.tsv:1257-1257]
- Existing row infrastructure: the packet and research memo already use the stem `2254-three-þrīe`, so the slice reuses that row-local filename rather than inventing a new stem [Germanic/docs/lexeme_reports/packets/2254-three-þrīe.md:1-9; Germanic/docs/lexeme_reports/research_memos/2254-three-þrīe.md:1-11].
- Known-problems status: no row-local `oe_known_problems.tsv` entry was found for `2254`, `*θréjez`, `þrīe`, or `þrī`.

## Detailed development-note summary

The live row is a targeted attested-variant decision, not a phonological repair. `PROTO` and `PROTOFORM` happen to be identical in the TSV, but they still need to be kept conceptually distinct: `PROTO` is the row's comparative/cognate-set label as stored in the table, whereas `PROTOFORM` is the actual derivational input the OE cascade applies to this row. `COUNTERPART` is then not a generic OE headword for “three” but the specific attested early West Saxon masculine nominative/accusative cell `þrīe`. The row therefore stands for `*θréjez -> þrīe`, not for an undifferentiated lexeme-level equation in which any handbook headword spelling for the numeral would do [Germanic/data/germanic-aligned-final.tsv:1257-1257; DEV_NOTES:line-40094-40113].

The core DEV_NOTES argument is that the old target `þrī` made a regular derivation look like an error. Section 17.43 records the observed output `*θréjez -> þrīe`, then immediately corrects the mismatch script's framing: “this is not a breaking-extra problem — `*éje` contracts regularly to `*īe`” [DEV_NOTES:line-40045-40046]. The trace excerpt is explicit that the OE cascade already gives `ProtoToOE: *θ*r*ī*e` and `Surface: þrīe`, so the `īe` sequence is not an aberrant extra diphthong but the expected outcome of the inherited sequence [DEV_NOTES:line-40051-40056; @Campbell1959, §120].

Campbell's paradigm, preserved directly in DEV_NOTES, is the decisive philological anchor and should stay quoted rather than paraphrased away: “Masc. nom/acc. **þrīe**, fem. and neut. nom/acc. **þrēo**, gen. **þrēora**, dat. **þrim** ... ‘eW-S has frequently -io- for -éo-; **lW-S has þry, þri for þrīe**.’” [DEV_NOTES:line-40066-40072; @Campbell1959, §683]. That quotation does two jobs at once. First, it confirms that `þrīe` is the regular early-WS masculine nominative/accusative form and not a fabricated convenience spelling. Second, it explains exactly why `þrī` kept showing up in lexical tables and headword-style sources: `þrī` is a later West Saxon reduced reflex of `þrīe`, not the conservative cell the current cascade is meant to model [DEV_NOTES:line-40074-40077; @Campbell1959, §683].

That contrast between row target and later reduction has to stay explicit. The row does **not** say that all OE evidence should be normalized to `þrīe`, and it does **not** deny that `þrī` is attested. The narrower claim is that for this row's selected paradigm cell, `þrīe` is the regular inherited early-WS outcome, while `þrī` belongs to a later apocopated/reduced stage that the current OE cascade “does not — and should not — model” [DEV_NOTES:line-40097-40101]. This is why `DERIVATION_CLASS = attested_variant` still makes sense: the target is attested, but it is an intentionally chosen conservative paradigm cell rather than the later reduced headword that a dictionary or Swadesh list may foreground [Germanic/data/germanic-aligned-final.tsv:1257-1257; DEV_NOTES:line-40084-40090,40094-40113].

The project decision in DEV_NOTES is correspondingly narrow and stable: change the TSV target only, leave the FST alone. Section 17.43 says “The FST is correct,” retargets the row from `þrī` to `þrīe`, adds the explanatory note, and records that no other Germanic rows for the cognate set are affected [DEV_NOTES:line-40094-40113]. The later verification note is equally important because it fixes the scope of the correction: the mismatch bucket should disappear, and the trace should still surface `þrīe` “since no FST change” was required [DEV_NOTES:line-40124-40132]. For later report work, the essential lesson is therefore not “the rule was repaired,” but “target selection was corrected so the already-regular derivation could be read correctly.”

Comparative-source hygiene remains worth flagging, even though DEV_NOTES itself settles the row-level decision. Comparative dictionaries often cite the numeral under a stem-like headword rather than under the inflected masculine cell used here; Kroonen, for example, gives Proto-Germanic `*þri-` with the wider numeral paradigm, not an OE-ready masculine nominative/accusative citation [@Kroonen2013]. That broader comparative practice is compatible with the row, but it should not be confused with the row's `PROTOFORM`. For row 2254, `PROTOFORM = *θréjez` is the derivational input chosen to land on the specific OE cell `þrīe`, while `COUNTERPART = þrīe` must remain distinct from the later/headword reduction `þrī` [@Kroonen2013; @Fulk2018, §10.1; @Campbell1959, §683].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-40045-40056

- Source heading: `§17.43 *θréjez → þrīe`
- Source line or section hint: `lines 40045-40056`
- Fragment type: `row_local_trace_and_correction`
- Status: `current`
- Issue tags: `trace`; `contraction`; `false_mismatch`; `attested_variant`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment preserves the first crucial correction: the mismatch script's label was wrong. DEV_NOTES says the apparent problem is “not a breaking-extra problem” because `*éje` contracts regularly to `*īe`, then shows the live trace landing on `Surface: þrīe` [DEV_NOTES:line-40045-40056; @Campbell1959, §120]. For this row, that means the `īe` outcome is evidence of a regular inherited development, not a cue to rewrite the OE sound changes.

### DEV_NOTES:line-40066-40090

- Source heading: `§17.43 source audit`
- Source line or section hint: `lines 40066-40090`
- Fragment type: `row_local_philology_and_method`
- Status: `current`
- Issue tags: `campbell_quote`; `paradigm_cell`; `late_ws_reduction`; `headword_vs_target`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the philological heart of the slice. DEV_NOTES preserves Campbell's paradigm quotation for `three`, including both the target cell `þrīe` and the explicit note that late West Saxon has `þry, þri for þrīe` [DEV_NOTES:line-40066-40072; @Campbell1959, §683]. The accompanying prose then states the current project reading plainly: inherited early-WS masculine nom./acc. `þrīe` versus later reduced `þrī/þrȳ`, plus the warning that Wiktionary-style lemma practice can collapse those distinct things if treated incautiously [DEV_NOTES:line-40074-40090].

### DEV_NOTES:line-40094-40113

- Source heading: `§17.43 diagnosis and plan`
- Source line or section hint: `lines 40094-40113`
- Fragment type: `row_local_decision_record`
- Status: `current`
- Issue tags: `target_selection`; `no_fst_change`; `attested_variant`; `protoform_vs_counterpart`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment records the decision that now governs the live TSV row. DEV_NOTES states, “The FST is correct,” identifies `þrī` as the late-WS reduction variant, and prescribes a TSV-only retarget from `COUNTERPART = þrī` to `COUNTERPART = þrīe` with no cascade edit [DEV_NOTES:line-40094-40113]. If later report prose needs one compact statement of present row policy, this is the fragment to cite.

### DEV_NOTES:line-40117-40132

- Source heading: `§17.43 risk assessment and verification`
- Source line or section hint: `lines 40117-40132`
- Fragment type: `row_local_verification_note`
- Status: `current`
- Issue tags: `verification`; `attestation`; `mismatch_bucket`; `no_rebuild`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This fragment is still worth preserving because it records the exact post-retarget expectations. DEV_NOTES says the retargeted `þrīe` is “well attested,” that the mismatch risk is zero, and that the trace should still surface `þrīe` without an FST rebuild [DEV_NOTES:line-40117-40132]. It is not the main philological argument, but it is useful project chronology showing that the fix was supposed to be table-local and immediately verifiable.

## Superseded or diagnostic material

The superseded material is the old mismatch framing itself: `*θréjez -> þrīe (expected þrī)` plus the script comment “ie-diphthong instead of expected high vowel” [DEV_NOTES:line-40041-40042]. That wording should be retained only as diagnosis history. DEV_NOTES immediately overturns it by saying the `*īe` output is regular and by relocating the problem to target choice rather than sound change [DEV_NOTES:line-40045-40056,40094-40113].

The late progress-log entry is likewise diagnostic chronology rather than independent argument. It records the row as “þrīe: TSV retarget þrī → þrīe early-WS (§17.43),” which is useful confirmation that the project treated this as a closed row-local retarget and not as a broader cascade rewrite [DEV_NOTES:line-10429-10431]. That fragment can support indexing or change history, but the substantive working note should still rely on the fuller section 17.43 material.

Lexical-table headwords such as `þrī` also belong here when they are used as evidence against the row. They explain why the row was easy to mistarget, but by themselves they do not outweigh Campbell's paradigm or the DEV_NOTES diagnosis. In other words: `þrī` is diagnostically relevant as the later/headword form that caused confusion, not as the present row target.

## Open questions for later work

- If a final lexeme report is drafted, decide whether to quote Campbell's full paradigm block or just the decisive contrast `þrīe` versus late-WS `þry, þri`; the shorter quote may be enough if space is tight, but the fuller block preserves the paradigm-cell logic best.
- Add a dedicated numeral-cell probe if future OE probe infrastructure expands beyond its current pilot set; the obvious cells are masc. nom./acc. `þrīe`, fem./neut. nom./acc. `þrēo`, gen. `þrēora`, and dat. `þrim`.
- If later comparative prose is added, decide how explicitly to gloss the difference between comparative stem-style citations such as `*þri-` and the row-level derivational input `*θréjez`, so that `PROTO`/`PROTOFORM`/`COUNTERPART` are not flattened back together.
