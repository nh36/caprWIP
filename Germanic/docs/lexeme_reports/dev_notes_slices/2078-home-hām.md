---
row_id: 2078
concept: home
counterpart: hām
proto: "*xáimaz"
protoform: "*xáimaz"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt
current_status: "current; no row-specific DEV_NOTES block survives"
needs_literature_agent: no
---

# DEV_NOTES material — 2078 home / hām

## Current row state

- The live TSV row is `2078 | home | hām | *xáimaz | *xáimaz | regular` (with `PROTO = *xáimaz`, `PROTOFORM = *xáimaz`, and OE target `COUNTERPART = hām`) [Germanic/data/germanic-aligned-final.tsv:574-574].
- `oe_known_problems.tsv` has no entry for `*xáimaz`, `home`, or `hām`; the current tracked OE problems are other lexemes only, so this row is not presently treated as a known exception or unresolved mismatch [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure likewise treats the row as uncovered but not problematic: `| 2078 | home | hām | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:279-279]. `report_manifest.tsv` still contains only pilot reports and has no row-2078 entry to reuse [Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- The current derivation snapshot is fully regular and very short. The published trace gives `PROTO: *xáimaz`, `EXPECTED: hām`, `OUTPUTS: hām`, then spells out the chain `PWGmc Ai Monophthongization: *xāmaz`, `PGmc Final Z Deletion: *xāma`, `PWGmc Final Bare A Loss: *xām`, `Old English Orthography: h*ām`, `Outcome: hām` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2453-2473]. The fuller text trace confirms that every later OE rule is `[no-change]`; after `PWGmcAiMonophthongization`, `PGmcFinalZDeletion`, and `PWGmcFinalBareALoss`, the form simply remains `*xām` until orthography/surface conversion to `hām` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:13956-14070].
- For this row, the distinction among levels matters even though `PROTO` and `PROTOFORM` happen to be identical: both are the inherited Germanic input `*xáimaz`, while `COUNTERPART` is the attested OE outcome `hām` reached by the current cascade, not another proto-level representation [Germanic/data/germanic-aligned-final.tsv:574-574; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2453-2473].

## Development-note summary

No row-specific mismatch dossier or implementation block for row 2078 survives in `DEV_NOTES.md`. The only explicit surviving mention of `hām` there occurs in a shared discussion of endingless dative forms, not in a dedicated `*xáimaz → hām` case study [Germanic/docs/DEV_NOTES.md:6211-6223]. This slice therefore has to be reconstructed conservatively from (a) the live row and live derivation trace, and (b) shared-background DEV_NOTES material on the two changes the trace actually uses: stressed `*ai > *ā` and WGmc/NWGmc loss of word-final `*-z` before any rhotacism issue could arise [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:13964-14070; Germanic/docs/DEV_NOTES.md:3459-3494,13874-13919].

On the current evidence, the row is straightforwardly regular. The trace does not show any row-specific repair, exception rule, or analogical override in the derivation proper: `*xáimaz` first undergoes stressed-root `*ai > *ā`, then loses final `*-z`, then loses final bare `*-a`, and only after that is mapped orthographically to `hām` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2460-2473; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:13968-14070]. The absence of an `oe_known_problems.tsv` entry and the `regular` derivation class in the live TSV both match that trace state [Germanic/data/germanic-aligned-final.tsv:574-574; Germanic/data/oe_known_problems.tsv:1-8].

The surviving DEV_NOTES reference to `hām` should not be overread. It is useful because it shows that the notes explicitly recognize OE `hām` as a real form, but the context is endingless dative analogy: the notes say that the endingless dat.sg. pattern spread to nouns like `dæg`, `morgen`, `ǣfen`, and `hām`, and that this was “a **later analogical development** after the regular sound change had deleted the ending” [Germanic/docs/DEV_NOTES.md:6220-6223]. That belongs in this slice as row-adjacent evidence about the OE form, but it is not the main derivational story of row 2078, whose current pipeline already reaches `hām` without any special-case intervention [Germanic/docs/DEV_NOTES.md:6215-6223; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2453-2473].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-13874-13919

- Source heading: `Research: Stressed vs. Unstressed *ai Monophthongization`
- Source line hint: `lines 13874-13919`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `stressed_ai`; `pwgmc_monophthongization`; `root_vowel_history`
- Recommended next use: `use_to_explain_why_row_2078_starts_with_*xā-`
- Shared-with rows if relevant: `all OE rows whose PGmc root contains stressed *ai`

DEV_NOTES preserves the core generalization that underwrites the first step of the current trace. It says the unconditional `PWGmcAiMonophthongization` diagnosis was wrong for unstressed syllables because “`*ai` should become `*ē`, not `*ā`” there, then quotes the literature: “unstressed `*ai` was usually monophthongized to `*é` throughout the NWGmc” and “the NWGmc merger of unstressed `*ai` with `*é`” [Germanic/docs/DEV_NOTES.md:13874-13896]. The same block then states the contrast explicitly: “**Stressed `*ai → *ā`** ... **Unstressed `*ai → *ē`**” [Germanic/docs/DEV_NOTES.md:13887-13889].

For row 2078 this is shared background, not a row dossier, but it is directly applicable. `*xáimaz` has root-initial stressed `*ái`, not an unstressed endingal `*ai`, so this fragment supports exactly the first current trace step `*xáimaz → *xāmaz` and warns against importing the `*-ai > *ē > -e` logic from inflectional endings into this lexeme [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:13964-13970; Germanic/docs/DEV_NOTES.md:13887-13919].

### DEV_NOTES:line-28065-28117

- Source heading: `§17.12.2 Phonetic equivalence of stress and position` / `§17.12.3 Implementation`
- Source line hint: `lines 28065-28117`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `root_vs_ending_ai`; `positional_stress`; `corpus_scope`
- Recommended next use: `use_as_guardrail_against_misclassifying_row_2078_as_unstressed_*ai`
- Shared-with rows if relevant: `all rows contrasting root *ai with endingal *-ai`

This later DEV_NOTES cleanup restates the same distinction in corpus-management terms. It says the surviving breve marker had distinguished unstressed endingal `*-ăi` from stressed root `*ai`, then adds: “**Stressed `*ai`** occurs exclusively in **root syllables** ... Any root-internal `*ai` bears primary stress by default,” whereas “**Unstressed `*ai`** occurs exclusively in **inflectional endings**” [Germanic/docs/DEV_NOTES.md:28065-28095]. The implementation note then keeps the split as word-final `*ai -> *ē` versus stressed `*ai -> *ā` [Germanic/docs/DEV_NOTES.md:28097-28117].

This still is not row-specific evidence, but for row 2078 it sharpens the classification: nothing about `*xáimaz` puts its `*ai` in the endingal, word-final, weak-tail environment. The row belongs unambiguously to the stressed-root branch, so this fragment is useful as a conservative anti-overreading note when later work compares `home / hām` with rows whose `-e` outcomes come from endingal `*-ai` [Germanic/docs/DEV_NOTES.md:28078-28117; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:13964-13970].

### DEV_NOTES:line-3459-3494

- Source heading: `Historical phonology of final *-z loss and its interaction with rhotacism`
- Source line hint: `lines 3459-3494`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `final_z_loss`; `ordering`; `no_final_rhotacism`
- Recommended next use: `use_to_explain_*xāmaz_>_*xāma`
- Shared-with rows if relevant: `all OE rows descending from PGmc forms in final *-z`

This fragment supplies the second indispensable change in the row’s current derivation. DEV_NOTES quotes Ringe & Taylor: “On the WGmc side, the loss of word-final `*z` in unstressed syllables ... must likewise have preceded the merger of `*z` with `*r`,” and Hogg: “Gmc /z/ yielded /r/ in intervocalic position in Old English (rhotacism), but in final position it is generally lost” [Germanic/docs/DEV_NOTES.md:3463-3470]. The notes then spell out the consequence: “Final `*-z` was **never rhotacized**. It was already gone by the time rhotacism occurred” and the pipeline therefore models `PGmcFinalZLoss` before rhotacism [Germanic/docs/DEV_NOTES.md:3471-3494].

For row 2078, this shared background matches the live trace exactly: after monophthongization to `*xāmaz`, the next material change is `PGmcFinalZDeletion: *xāma`, not any `*-r` stage [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:13968-13990]. The fragment is not specific to `home`, but it is the clearest surviving DEV_NOTES authority for why the row should be read as `*xāmaz > *xāma`, not as passing through a rhotacized final consonant.

### DEV_NOTES:line-6211-6223

- Source heading: `R/T vol.2 pp.379-380 (§7.2.2): Endingless datives`
- Source line hint: `lines 6211-6223`
- Fragment type: `diagnostic_with_explicit_form_mention`
- Status: `diagnostic_only`
- Issue tags: `endingless_dative`; `later_analogy`; `explicit_hām_mention`
- Recommended next use: `retain_only_for_case-form_context_not_for_core_derivation`
- Shared-with rows if relevant: `rows involving dæg/morgen/ǣfen/hām-type endingless datives`

This is the only surviving DEV_NOTES block that explicitly names `hām`, so it should be preserved even though it is not a home-row derivation note. The block quotes R/T on “endingless dat. sg. forms where an overt ending `-e` would be expected,” then adds that the pattern spread from `niht` to other nouns “like `dæg`, `morgen`, `ǣfen`, `hām`, and place-name compounds” and that this “was a **later analogical development** after the regular sound change had deleted the ending” [Germanic/docs/DEV_NOTES.md:6215-6223].

For row 2078, the value of the fragment is narrow but real. It confirms that DEV_NOTES treats OE `hām` as an attested/recognized form in a historically meaningful context, yet the discussion is about an endingless dative pattern, not about the core phonological path from `PROTO/PROTOFORM = *xáimaz` to the lexical counterpart `hām`. This fragment should therefore be used only as row-adjacent diagnostic support for the OE form and for the possibility of later analogical case-level behavior; it should not be made to carry the burden of the main derivation, which the current trace already handles without special pleading [Germanic/docs/DEV_NOTES.md:6211-6223; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2453-2473].

## Superseded or diagnostic material

- No dedicated row-specific DEV_NOTES case block survives for `*xáimaz → hām`. That absence itself matters: unlike rows with residual-mismatch dossiers or implementation proposals, row 2078 currently has to be documented from shared historical notes plus the live derivation trace [Germanic/docs/DEV_NOTES.md:3459-3494,6211-6223,13874-13919; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:13956-14070].
- The endingless-dative passage is diagnostic rather than controlling for the row. It explicitly includes `hām`, but only as part of a later analogical case-form spread after ending deletion; it is not evidence that the lexeme needs to be reclassified as analogical or exceptional in the live TSV [Germanic/docs/DEV_NOTES.md:6211-6223; Germanic/data/germanic-aligned-final.tsv:574-574].
- The stressed/unstressed `*ai` discussions are shared background, not row-specific notes. Their role here is to prevent a wrong derivation story — i.e. treating root `*xái-` as if it behaved like endingal `*-ai` — rather than to memorialize any row-2078 bug history [Germanic/docs/DEV_NOTES.md:13874-13919,28065-28117].
- Current trace evidence makes any more elaborate diagnostic narrative unnecessary unless later corpus work uncovers contrary data. In the present state, the row is simply `*xáimaz → *xāmaz → *xāma → *xām → hām`, with all later OE rules inert for this input [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2460-2473; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:13968-14070].

## Open questions for later work

- If this row eventually receives a full report, decide whether the report should explicitly distinguish lexical `hām` from the endingless dat.sg. `hām` discussion preserved in DEV_NOTES. The current slice keeps them distinct, but the surviving DEV_NOTES citation is case-form-specific while the TSV row itself is just `home / hām` [Germanic/docs/DEV_NOTES.md:6211-6223; Germanic/data/germanic-aligned-final.tsv:574-574].
- If later documentation wants a literature-facing note rather than a trace-facing note, it may be worth extracting direct external citations for the full `*xáimaz > hām` chain, because DEV_NOTES currently preserves only shared rule discussions plus the one dative-analogy mention, not a dedicated lexeme dossier [Germanic/docs/DEV_NOTES.md:3459-3494,6211-6223,13874-13919].
- The current trace leaves initial `*x-` to the orthography/surface stage (`h*ām` → `hām`) rather than to a separately narrated sound-change paragraph. If future row documentation standardizes explicit discussion of inherited initial `x/h`, row 2078 may need a short added note on that representational step even though no mismatch is involved now [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2470-2473; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:14065-14070].
