---
row_id: 2206
concept: spear
counterpart: speoru
proto: *spéru
protoform: *spéru
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2206 spear / speoru

## Current row state

- `Germanic/data/germanic-aligned-final.tsv` line 1070 currently reads row `2206` as `CONCEPT spear`, `COUNTERPART speoru`, `PROTO *spéru`, `PROTOFORM *spéru`, `DERIVATION_CLASS regular`, with a row note explicitly identifying the target as `NApl speoru` and contrasting it with analogical WS `spere`/`speru` [Germanic/data/germanic-aligned-final.tsv:1070].
- The live row uses the same string for `PROTO` and `PROTOFORM`, but the surviving DEV_NOTES argument still needs the distinction kept explicit: the lexeme-level comparative headword is the spear noun, whereas the row's working `PROTOFORM` function is specifically the plural cell selected for OE derivation, not the analogically remodelled singular citation form [Germanic/data/germanic-aligned-final.tsv:1070; DEV_NOTES:line-29747-29771].
- No row-specific packet or research memo stem presently appears to exist for this row under `Germanic/docs/lexeme_reports/`; this slice therefore serves as the replacement working note and uses the canonical row-based filename.

## Detailed development-note summary

The durable project conclusion is that row `2206` should be read as a **paradigm-cell row**, not as a singular headword row. DEV_NOTES began from the old mismatch `*spéru -> speor` against target `spere`, and the first pass explored singular-facing repairs. That earlier work is still useful because it records the negative result cleanly: regular singular-side inputs do **not** yield attested `spere` by pure sound law. DEV_NOTES states that `*speri` / `*speriz` would give `*spire`, not `spere`, because i-mutation applies before final `*-i` lowers; Campbell explicitly says short-stem neuter i-stems have normal developments “except `spere`, which has the vowel of early reformed pl. `*sperō`,” and Brunner likewise treats the singular vocalism as problematic rather than straightforwardly inherited [DEV_NOTES:line-28730-28849; @Campbell1959, §609; @SieversBrunner1965, §262 Anm. 1]. The important practical consequence is that the project did **not** eventually decide that `spere` had become derivable; it decided to stop using the singular as the row's OE target.

The current row policy comes from the later Option-D expansion and the final paradigm dossier. Those notes make the positive case that the OE cell worth targeting is the **N/A plural**. DEV_NOTES preserves the handbook quotations that matter most. Campbell §210.1: “Analogical removal is frequent, e.g. **speru** spear ... after infl. **spere**, n.s.”; Brunner §110.1: “doch ist das `eo` in der Flexion durch Ausgleichung beseitigt in ws. Nom. Akk. Pl. `speru` ... nach dem Sg. `spere` Speer.” Read together, these notes treat `speoru` as the conservative back-umlauted plural and WS `speru` as a later de-back-umlauted levelling under singular pressure [DEV_NOTES:line-28902-28927; DEV_NOTES:line-29252-29280; DEV_NOTES:line-29729-29745; @Campbell1959, §§210.1, 211, 607-608; @SieversBrunner1965, §110.1]. The row's present `COUNTERPART speoru` therefore represents the conservative attested plural cell, not a speculative unattested form.

DEV_NOTES also ties that philological choice to a genuine rule correction rather than a row-local workaround. The old `speor` output turned out to come from a general FST bug: `OEHighVowelApocope` had been treating all diphthongs as heavy, so short diphthongs created by back-umlaut in light stems were losing final `-u` when they should have retained it. The same bad behaviour affected `*teru`, `*smeru`, and `*faru`. The §17.17 diagnosis and implementation result argue that short back-umlauted `*eo` in a single-consonant stem still counts as light for apocope, exactly the condition needed for `*spéru -> speoru` [DEV_NOTES:line-29098-29228; DEV_NOTES:line-29411-29455; @Campbell1959, §345]. This matters because row `2206` is current not by exception-handling, but because the grammar was corrected to let the regular plural derivation surface.

The attestation argument was then rechecked in detail. DEV_NOTES §17.16.19 re-reads the glossary evidence and concludes that `speoru` is **NApl/APl, not NSg**: the gloss line with Latin plural `contos` is plural, Brunner explicitly labels the form as plural, Campbell's paradigm gives NSg `spere` but plural `speru`, and Campbell's back-umlaut discussion treats WS `speru` as a leveled plural after singular `spere` [DEV_NOTES:line-29231-29312; @Campbell1959, §§210.1, 211, 607; @SieversBrunner1965, §110.1]. That recheck is the main reason the slice should keep saying “paradigm-cell target” rather than simply “alternative lexical headword.”

The late coda in §17.16.20 is the most self-contained current authority, but it also preserves one important caution. Its cell-by-cell table argues that the singular paradigm was reshaped early and that the **NApl is the unique cell** where the inherited u-stem/plural vocalism, overt back-umlaut, and secure attestation converge [DEV_NOTES:line-29500-29806]. The same coda also corrects an earlier source shorthand: while earlier notes and the live TSV still say Épinal-Erfurt `Contos, speoru`, the later re-audit says the safest exact witness is **Corpus Glossary #528 `contos : speoru`**, with Cleopatra parallels, and that Brunner's “Ep. Gl.” is a loose citation rather than a precise source label [DEV_NOTES:line-29673-29685]. The row-level philological conclusion stays the same, but later reporting should remember that the attestation locus has been refined.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-28657-28849

- Source heading: `§17.16 spere PROTOFORM research (opening problem and first recommendation)`
- Source line or section hint: `§17.16.1-10, lines 28657-28849`
- Fragment type: `lexeme_specific`
- Status: `superseded`
- Issue tags: `singular_analysis`; `analogical_singular`; `protoform_vs_proto`; `project_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This opening block is superseded as row policy but still essential chronology. It records the negative singular result that later Option D depends on: regular singular-side inputs such as `*speri` do not produce `spere`, and the early recommendation therefore shifted toward correcting the proto and treating singular `spere` as analogical. That recommendation no longer governs the row, but the fragment remains the cleanest statement of **why the project stopped trying to make the singular the FST target at all** [@Campbell1959, §609; @SieversBrunner1965, §262 Anm. 1].

### DEV_NOTES:line-28867-29017

- Source heading: `§17.16.11-15 paradigm-cell approach and lautgesetzlich justification`
- Source line or section hint: `lines 28867-29017`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `paradigm_cell`; `na_pl`; `back_umlaut`; `light_stem_u_retention`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the first core current fragment. It replaces the singular-centred framing with an explicit plural-cell argument, quotes Campbell and Brunner on `speoru ~ speru`, and writes out the derivation `PGmc *sperō -> WGmc *speru -> pre-OE *speru -> OE speoru -> WS speru` [@Campbell1959, §§210.1-211, 608; @SieversBrunner1965, §110.1]. For row `2206`, this is the main authority for the claim that conservative `speoru` is the regular attested outcome and that WS `speru` is the analogical form.

### DEV_NOTES:line-29098-29228

- Source heading: `§17.17 FST bug: apocope treats short diphthongs as heavy`
- Source line or section hint: `lines 29098-29228`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `high_vowel_apocope`; `short_diphthong_weight`; `shared_rule_fix`; `row_enabling_context`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2127; 2206`

This fragment is shared rule context, but it is directly row-enabling rather than incidental background. It documents the specific transducer failure that had been hiding regular `speoru`: short back-umlauted diphthongs in light stems were being treated as heavy and therefore losing final `-u`. The note matters for row `2206` because it shows that `speor` was not the correct inherited plural output after all; it was the product of a general apocope misclassification [@Campbell1959, §345].

### DEV_NOTES:line-29231-29312

- Source heading: `§17.16.19 verification that speoru is NApl (not NSg)`
- Source line or section hint: `lines 29231-29312`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `attestation`; `plural_cell`; `glossary_evidence`; `ws_levelling`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the row's cleanest attestation-control fragment. It explicitly checks the user's earlier worry that `speoru` might be singular and answers no: the glossary evidence, Brunner's plural label, Campbell's paradigm, and Campbell's analogical-removal note all point to N/A plural `speoru/speru`, not singular `speoru` [@Campbell1959, §§210.1, 211, 607; @SieversBrunner1965, §110.1]. Later report prose can rely on this block whenever it needs to justify the cell choice rather than merely repeating the row note.

### DEV_NOTES:line-29411-29455

- Source heading: `§17.17.8 implementation results`
- Source line or section hint: `lines 29411-29455`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `implementation_result`; `row_update`; `probe_result`; `current_policy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment records the transition from proposal to live row state. It states that the short-diphthong weight refactor was implemented, that the mismatch count dropped `31 -> 30`, and that row 1070 was changed from `spere` to `speoru` with the NApl rationale attached [DEV_NOTES:line-29450-29455]. For row-slice purposes, it is the clearest confirmation that the plural-cell policy was not just discussed but actually adopted.

### DEV_NOTES:line-29488-29806

- Source heading: `§17.16.20 coda — cell-by-cell paradigm dossier`
- Source line or section hint: `lines 29488-29806`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `paradigm_dossier`; `protoform_vs_proto`; `dialectology`; `source_locus_correction`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This long coda is the best single replacement note for later report writing. It gives the PGmc cell table, projects each cell to OE, explains why the singular paradigm was remodelled before OE attestation, and argues that the NApl is the one cell where inherited u-stem morphology, visible back-umlaut, and attested early forms all coincide [@Kroonen2013, p. 467; @Orel2003, p. 364; @Campbell1959, §§210-211, 607-608; @SieversBrunner1965, §110.1]. It also preserves the important source correction that exact `contos : speoru` citation is best anchored in Corpus/Cleopatra rather than a strict Épinal citation, even though the core plural analysis is unchanged.

## Superseded or diagnostic material

The main superseded layer is the early singular-facing recommendation in `§17.16.1-10`. That material should remain visible because it captures a real philological result — singular `spere` is analogical and not directly derivable from a clean PGmc input — but later work should not mistake its Option-B-style recommendation for the current row policy [DEV_NOTES:line-28657-28849].

A second diagnostic caution concerns source wording. The live TSV note still uses the shorthand Épinal-Erfurt “Contos, speoru,” and the earlier DEV_NOTES verification block also follows Brunner's loose “Ep. Gl.” language. The later coda, however, says the safest exact locus is Corpus Glossary `contos : speoru` with Cleopatra parallels, while Épinal itself is not the strongest precise witness for the back-umlauted form [DEV_NOTES:line-29240-29258; DEV_NOTES:line-29673-29685]. Later index/report work should preserve the plural-cell conclusion but avoid treating the older source label as fully settled.

The provisional classification caveats inside `§17.17.4` are likewise diagnostic rather than controlling now. Once `§17.17.8` records the implemented short-vs-long diphthong split and the successful probes, later work should cite the implementation block rather than the earlier tentative candidate-fix prose when stating current rule inventory [DEV_NOTES:line-29164-29206; DEV_NOTES:line-29418-29449].

## Open questions for later work

- If the row is ever metadata-cleaned, decide whether `PROTO` should be normalized to an explicit lexeme/headword notation such as `*speru-`, while keeping `PROTOFORM` as the row's selected NApl/APl comparator. The current TSV uses one string for both functions, but the DEV_NOTES argument does not.
- If the row note or any later report is revised, decide whether the attestation citation should be updated from broad Épinal-Erfurt shorthand to the more precise Corpus/Cleopatra formulation preserved in `§17.16.20`.
- If a final lexeme report is written, decide how much of the singular stem-class discussion should be carried forward. The important durable point is that singular `spere` is analogical and therefore not the target cell; the open question is how much of the older `u`-stem versus `s`/`i`-stem explanatory machinery is worth reproducing in full.
- If later indexing wants only compact row-local fragments, decide whether to index the long `§17.16.20` coda as one large attachment or to split out the source-locus correction (`Corpus/Cleopatra` versus loose `Ep. Gl.`) as a separate diagnostic item.
