---
row_id: 2302
concept: world
counterpart: weorold
proto: "*wíra-àldiz"
protoform: "*wír-àldu"
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2302-world-weorold.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2302-world-weorold.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md
  - Germanic/docs/dossiers/widuwe-u-preservation.md
current_status: "current row uses *wíra-àldiz / *wír-àldu; older *wer-uldu/*wer-oldu DEV_NOTES states are superseded"
needs_literature_agent: no
---

# DEV_NOTES material — 2302 world / weorold

## Current row state

- The live row is now `2302 | world | weorold | *wíra-àldiz | *wír-àldu | early_analogy`, and its note explicitly claims the present OE-directed derivation `*wir-aldu > weorold` through `(1) NWGmc i-lowering *i>*e, (2) inter-stress raising *a>*u, (3) back mutation *e>*eo, (4) medial *u>*o, (5) final apocope`, while also retaining the older wording `PROTO *weraldiz is etymological headword` [Germanic/data/germanic-aligned-final.tsv:1444-1444]. That last clause is now only a literature-background gloss, not the live `PROTO` cell.
- `coverage_audit.md` marks the row as slice-worthy because both the note and the derivation class need row-local explanation: `| 2302 | world | weorold | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |` [Germanic/docs/lexeme_reports/coverage_audit.md:175-175].
- There is no manifest entry for this row; the packet records `_No manifest entry._`, and the checked `report_manifest.tsv` excerpt contains only earlier pilot rows [Germanic/docs/lexeme_reports/packets/2302-world-weorold.md:11-13; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- `oe_known_problems.tsv` has no matching entry, so the row is not currently being carried as a known unresolved OE exception [Germanic/docs/lexeme_reports/packets/2302-world-weorold.md:44-46].
- The current debug snapshots agree with the live row state. Both publish and compact traces show `PROTO: *wír-àldu`, `EXPECTED: weorold`, `OUTPUTS: weorold`, with the staged path `NWGmc I Lowering: *wéràldu > OE Inter Stress Raising: *wéruldu > OE Med Unstressed U Lowering: *wéroldu > OE Back Mutation: *wéoroldu > OE High Vowel Apocope: *wéorold` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6884-6903; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md:8036-8057].
- Row-local support files do exist and should stay linked: `packets/2302-world-weorold.md` and `research_memos/2302-world-weorold.md`. No row-specific dossier/analysis file was found; the only extra files presently worth carrying are shared-background items about WS/Anglian distribution and back-mutation/rounding behavior after `w-` [Germanic/docs/lexeme_reports/research_memos/2302-world-weorold.md:38-57; Germanic/docs/lexeme_reports/packets/2302-world-weorold.md:154-184].

## Development-note summary

This row does retain substantial DEV_NOTES material, but not as a single unchanged block. The durable core is: `world` is the compound ‘age of men’; the literature discussed in DEV_NOTES treats an early shift from i-stem to ō-stem as crucial; Ringe–Taylor’s row-local quotation gives the comparative chain `*weraldiz > *weraldu > *weruld > WS OE weorold ~ worold`, alongside Mercian `weoruld`, Northumbrian `woruld`, and Kentish `wiarald` [Germanic/docs/DEV_NOTES.md:16931-17018]. That comparative background still matters, but its exact transponent recommendation does not survive unchanged.

The most obviously superseded material is the 2026-04-11 / 2026-04-12 implementation history that temporarily treated `*wer-uldu` and even `*wer-oldu` as the right `PROTOFORM` for row 2302 [Germanic/docs/DEV_NOTES.md:17147-17180]. Later DEV_NOTES work instead implemented `OEInterStressRaising`, showed that `wir-aldu`/`wír-àldu` can be used directly without the older `*wer-uldu` crutch, and then fixed rule ordering so the documented `*u > o` step actually feeds from raising rather than being blocked by earlier ordering [Germanic/docs/DEV_NOTES.md:17819-17929,23451-23472]. So the current slice has to preserve both layers at once: the older `*wer-...` discussion is still useful for explaining why `PROTO` and `PROTOFORM` must be distinguished, but the live row now relies on the later `*wír-àldu` solution.

Support is therefore mixed by type. The compound etymology, variant cluster, and early ō-stem shift are shared-background-plus-row-specific and still usable. The transponent distinction (`PROTO` as comparative headword vs `PROTOFORM` as OE-facing input) survives in principle, but its earlier concrete values `*wer-uldu/*wer-oldu` are superseded. The later inter-stress-raising and rule-ordering notes are the row-specific current implementation support. The accent-migration and regression-scan notes are diagnostic: they illuminate why the present row is spelled `*wíra-àldiz / *wír-àldu` and why it is insulated from unrelated `*wí-... > *wu-...` overgeneration, but they are not the primary etymological argument [Germanic/docs/DEV_NOTES.md:17091-17145,17882-17929,23451-23472,27924-27943,43613-43628].

## Relevant DEV_NOTES fragments

### Fragment 1

- **Source heading:** `### OE weorold 'world': Comprehensive Etymology (2026-04-11)`
- **Source line hint:** `Germanic/docs/DEV_NOTES.md:16913-17018`
- **Fragment type:** `row_specific_etymology_with_shared_comparative_background`
- **Status:** `current for comparative background; not by itself a full description of the live TSV settings`
- **Issue tags:** `compound_structure`; `i_vs_e_first_element`; `o_stem_shift`; `dialect_variants`
- **Recommended next use:** `cite when explaining why the row is early_analogy and why weorold is only one OE member of a larger variant set`
- **Shared-with rows if relevant:** `cognate-set world rows (Dutch/English/German counterparts), not just OE row 2302`

This is the main surviving row-specific DEV_NOTES block. It explicitly frames the lexeme as a compound: `PGmc *weraldiz = *weraz 'man' + *aldiz 'age'` and immediately anchors the comparative discussion in a long Ringe–Taylor quotation: “One word underwent combinative back umlaut (variably) even in WS: ... PNWGmc `*weraldiz` 'world' ... > `*weraldu` > `*weruld` (6.3.3) > WS OE `weorold ~ worold` (also with `u` in the 2nd syll.), Merc. `weoruld`, North. `woruld`, Kent. `wiarald`” [Germanic/docs/DEV_NOTES.md:16922-16941]. That quotation is still central because it preserves the exact comparative chain DEV_NOTES wanted the row to embody, even though the live TSV now writes the cognate-set `PROTO` as `*wíra-àldiz`.

The same block is also where DEV_NOTES most clearly preserves the first-element uncertainty. It says the sources are inconsistent, tabulates Kroonen/Orel/Kluge/Ringe–Taylor against each other, and quotes R/T’s warning that “PIE `*wih₁rés` ... > PGmc `*wiraz` (`*weraz??`)`” and “We cannot be sure that PGmc did not already exhibit `*e` in these words” [Germanic/docs/DEV_NOTES.md:16943-16978]. For the current row, this material is not a license to overwrite the live `PROTO` with `*weraldiz`; rather, it is row-specific background explaining why DEV_NOTES historically oscillated between `*wir-` and `*wer-`, and why the slice must keep `PROTO` (live cognate-set form), literature-stage lowered `*wer-...`, and OE target `weorold` distinct.

### Fragment 2

- **Source heading:** `### OE weorold 'world': Comprehensive Etymology (2026-04-11)`
- **Source line hint:** `Germanic/docs/DEV_NOTES.md:17019-17077`
- **Fragment type:** `shared_background_phonology_for_row`
- **Status:** `current as background; partly generalized beyond row 2302`
- **Issue tags:** `inter_stress_raising`; `regular_vs_analogical`; `medial_a_to_u`; `medial_u_to_o`
- **Recommended next use:** `cite when justifying which part of the derivation is analogical and which later steps the FST treats as regular`
- **Shared-with rows if relevant:** `shared especially with lord / furlong type compound-medial raising cases`

This section preserves the phonological rationale later reused by the live row note. DEV_NOTES quotes R/T §6.3.3 that in certain compounds “the unstressed vowel has not only been retracted but raised all the way to `u`, usually spelled `u ~ o` unless a nasal follows immediately,” and it groups `world` with `hlafurd` and `furlung` as parallel cases [Germanic/docs/DEV_NOTES.md:17021-17040]. The block is explicit that this is *not* the same as the earlier stem-class shift: `*weraldiz` must first be treated as having moved into a ō-stem environment, but the medial `*a > *u` step is then discussed as a regular, limited compound-internal development [Germanic/docs/DEV_NOTES.md:17023-17040,17057-17077].

For row 2302, the durable value is the classification, not the old transponent. DEV_NOTES’s revised chain here is `*weraz + *aldiz -> *weraldiz -> *weraldu -> *weruld -> *weoruld ~ *woruld -> weorold ~ worold`, and it classifies the steps as: stem-class shift `ANALOGICAL`, medial `a > u` `REGULAR`, combinative back umlaut `REGULAR`, medial `u > o` `REGULAR` [Germanic/docs/DEV_NOTES.md:17057-17077]. That classification still aligns well with the live `DERIVATION_CLASS = early_analogy`: the early analogical step is the stem-class reassignment, while the later OE-facing steps are now meant to run in the pipeline.

### Fragment 3

- **Source heading:** `#### 14.6 Implementing Inter-Stress Raising: *a → *u (2026-04-12)`
- **Source line hint:** `Germanic/docs/DEV_NOTES.md:17819-17929`
- **Fragment type:** `row_specific_current_implementation_support`
- **Status:** `current for why the row now uses *wir-aldu/*wír-àldu instead of *wer-uldu`
- **Issue tags:** `protoform_choice`; `oeinterstressraising`; `compound_shape`; `back_mutation_not_breaking`
- **Recommended next use:** `cite when explaining the live PROTOFORM and the absence of an internal linking vowel in the OE row`
- **Shared-with rows if relevant:** `shared as rule background with hlafurd/furlong, but row-local consequences are specific here`

This is the DEV_NOTES block that most directly supports the *current* row shape. It states the goal openly: “Enable using `*wir-aldu` ... as the PROTOFORM for `weorold`,” and then gives the working derivation after the new rule: `1. *wir-aldu ... 2. i-lowering: *w*e*r*a*l*d*u 3. Inter-stress raising: *w*e*r*u*l*d*u 4. ... 6. Back mutation: *w*e*o*r*u*l*d*u 7. Final: weorold ✓” [Germanic/docs/DEV_NOTES.md:17821-17825,17882-17892]. The same passage explicitly says the diphthongization here comes from **back mutation**, “not breaking,” because the relevant context is no longer `r + consonant` once the compound is being handled this way [Germanic/docs/DEV_NOTES.md:17894-17896].

This block is also the best surviving explanation for why the OE row no longer carries the older `*wer-uldu` transponent and no longer carries a linking vowel between first and second elements. DEV_NOTES says the reverted `*ă`-bearing approach blocked the crucial context, but “The form `wir-aldu` (without linking vowel `*ă`) works correctly” [Germanic/docs/DEV_NOTES.md:17864-17880,17882-17892]. The final rule statement then generalizes the pattern, closing with “`*wer-aldu -> *wer-uldu -> weorold` ✓” and “Mismatch count: Unchanged at 40 (no regression)” [Germanic/docs/DEV_NOTES.md:17910-17929]. In present row-local terms, that is the direct ancestor of the live `PROTOFORM *wír-àldu`.

### Fragment 4

- **Source heading:** `#### Probe result`
- **Source line hint:** `Germanic/docs/DEV_NOTES.md:23451-23472`
- **Fragment type:** `row_specific_verification_after_rule_reordering`
- **Status:** `current verification`
- **Issue tags:** `rule_ordering`; `u_lowering_after_raising`; `live_note_matches_fst`; `regression_check`
- **Recommended next use:** `cite when the question is whether the documented live derivation actually matches current bin behaviour`
- **Shared-with rows if relevant:** `shared with sāwol; otherwise row 2302 is one of the explicit beneficiaries`

This later probe is the clearest row-specific confirmation that the live note’s step sequence is no longer merely aspirational. DEV_NOTES reports that reordering the stack produced `baseline (HEAD): 40 mismatches` versus `R3 probe: 38 mismatches`, with the explicit row-local fix `*wír-aldu -> weorold (previously produced weoruld)` and “new regressions: none” [Germanic/docs/DEV_NOTES.md:23457-23466]. It then adds the crucial interpretive sentence: row 1444 already claimed `(4) medial *u > *o`, but under the old ordering that step “could not actually fire”; the new ordering “makes the TSV’s documented derivation match the FST’s actual behaviour” [Germanic/docs/DEV_NOTES.md:23468-23472].

For this slice, that means the current row should be read as a post-reordering row. Earlier DEV_NOTES stages often had the right comparative story but the wrong implemented order. After this probe, the documented chain `i-lowering > inter-stress raising > back mutation > medial u-lowering > apocope` became aligned with the actual derivation snapshots, which is why the compact/publish trace now shows `*wéruldu > *wéroldu > *wéoroldu > *wéorold` for the live `PROTOFORM *wír-àldu` [Germanic/docs/DEV_NOTES.md:23468-23472; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md:8045-8057].

### Fragment 5

- **Source heading:** `#### §17.11.2-b TSV migration` and `#### §17.11.2-d Expected outcome`
- **Source line hint:** `Germanic/docs/DEV_NOTES.md:27924-27943,27983-27993`
- **Fragment type:** `row_specific_notation_and_pipeline_diagnostic`
- **Status:** `current but diagnostic/notation-focused`
- **Issue tags:** `acute_grave_notation`; `proto_vs_protoform`; `linking_vowel_distribution`; `oe_only_syncope`
- **Recommended next use:** `cite when explaining why the live cognate-set PROTO and OE PROTOFORM differ in accenting and in the presence/absence of the linking vowel`
- **Shared-with rows if relevant:** `shared with the non-OE world rows 1442/1443/1445 and with other acute+grave compound migrations`

This material matters because the live row is now prosodically marked. DEV_NOTES records the TSV migration `*wíră-aldiz -> *wíra-àldiz` for the non-OE rows and notes that “under §16.6 we kept the OE-row variants using graves already” [Germanic/docs/DEV_NOTES.md:27924-27943]. It then pauses over the exact world row mechanics: “In our planned OE form `*wír-àldu` (row 2302), there is no linking vowel present — the first element ends in `r` directly abutting the hyphen. Rule doesn’t fire ... For the Du/Ge/En forms `*wíra-àldiz`, the linking `a` sits between `*wír-` and `-àldiz` ... but it isn’t [run] in those pipelines” [Germanic/docs/DEV_NOTES.md:27983-27993].

That is diagnostic rather than foundational, but it is still important row-local guidance. It preserves the exact distinction the slice must keep visible: `PROTO *wíra-àldiz` is the cognate-set form with a linking vowel preserved in the non-OE rows, while `PROTOFORM *wír-àldu` is the OE-specific input after the early analogical ō-stem shift and without the linking vowel that would otherwise disrupt the derivation [Germanic/docs/DEV_NOTES.md:27924-27943,27983-27993].

## Superseded or diagnostic material

- The 2026-04-11 “TSV Changes (Implemented)” block is no longer current as a statement of the row’s actual cells. It first says `Row 2302 (weorold): PROTOFORM *wer-uldu; PROTO *weraldiz`, then later in the same status block reports `Row 2302 now has: PROTOFORM: *wer-oldu; PROTO: *weraldiz` [Germanic/docs/DEV_NOTES.md:17147-17180]. Both states are superseded by the live `*wíra-àldiz / *wír-àldu` row [Germanic/data/germanic-aligned-final.tsv:1444-1444]. What survives from that block is only the *idea* that `PROTO` and `PROTOFORM` may need to differ for this lexeme.
- The `*wir-` vs `*wer-` testing block is partly superseded and partly diagnostic. Its important warning still stands: DEV_NOTES judged direct OE back mutation `*i -> eo` historically suspicious and eventually deleted the explicit `{*i} -> {*e}{*o}` shortcut from `OEBackMutation` as “historically unmotivated” [Germanic/docs/DEV_NOTES.md:17629-17720,17778-17817]. But its interim recommendation to keep `*wer-uldu` is not current after the later inter-stress-raising work and rule reordering [Germanic/docs/DEV_NOTES.md:17819-17929,23451-23472].
- The late-WS `wurold`/`worold` material is shared-background-only, not evidence that the row’s selected OE target should be changed. DEV_NOTES quotes Brunner on “spätws. ... `wurold`” and Kaluza on “`worold` neben `weorold`” as late darkening/rounding phenomena after `w-` [Germanic/docs/DEV_NOTES.md:33304-33318,33421-33435]. Useful for variant ecology; not row-specific authority against `COUNTERPART = weorold`.
- The final regression-scan table entry `| *wír-àldu | w í r à l d u | *r + *à (not *u/*o) | no | weorold |` is diagnostic only [Germanic/docs/DEV_NOTES.md:43613-43628]. Its role is to show that later narrow `*wí-...` scanning rules do **not** fire on this row; it is a safeguard against overgeneration, not the primary derivation story.

## Open questions for later work

- The live row note still says `PROTO *weraldiz is etymological headword`, even though the live `PROTO` cell is `*wíra-àldiz`. If the TSV note is ever revised, it should distinguish current cognate-set `PROTO`, current OE-facing `PROTOFORM`, and literature-stage lowered `*wer-...` forms more cleanly than it does now [Germanic/data/germanic-aligned-final.tsv:1444-1444; Germanic/docs/lexeme_reports/research_memos/2302-world-weorold.md:11-13,117-123].
- DEV_NOTES itself still contains multiple stale “implemented” states (`*wer-uldu`, `*wer-oldu`) before the later `*wír-aldu` success and reordering probe. A future cleanup should mark those older values as historical stages rather than leaving them to look current in isolation [Germanic/docs/DEV_NOTES.md:17147-17180,17819-17929,23451-23472].
- If a later row report needs a fuller variant discussion, it should keep the distinction between selected target `weorold` and the broader OE set `worold / weoruld / woruld / world`, while treating late-WS `wurold` as a secondary rounding/darkening development rather than as the default citation form [Germanic/docs/DEV_NOTES.md:16935-17018,33304-33318,33421-33435].
