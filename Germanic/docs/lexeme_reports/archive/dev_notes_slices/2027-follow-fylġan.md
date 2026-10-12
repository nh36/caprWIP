---
row_id: 2027
concept: follow
counterpart: fylġan
proto: *fulgēną
protoform: *fúlgijaną
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2027-follow-fylġan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2027-follow-fylġan.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2027 follow / fylġan

## Current row state

- CONCEPT: `follow`
- COUNTERPART: `fylġan`
- PROTO: `*fulgēną`
- PROTOFORM: `*fúlgijaną`
- DERIVATION_CLASS: `early_analogy`
- Live TSV row: the row now explicitly keeps the comparative cognate-set headword separate from the OE-directed derivational input. `PROTO` remains `*fulgēną`, while `PROTOFORM` is the class-I form `*fúlgijaną`, and the target is normalized OE `fylġan` [Germanic/data/germanic-aligned-final.tsv:line-376].
- Live TSV note: `Kroonen s.v. *fulgēn-: "OE fylg(e)an continue *fulgjan-"; R/T §2.3.1: "class I weak OE fylgan". WS folgian is Class II from *fulgēn-.` That note already captures the core row split that the slice needs to preserve [Germanic/data/germanic-aligned-final.tsv:line-376].
- `oe_known_problems.tsv`: no row-local entry for `2027`, `*fulgēną`, `*fúlgijaną`, `fylġan`, or `folgian`; this row is not currently tracked as a known unresolved system exception [Germanic/data/oe_known_problems.tsv:line-1-8].
- `report_manifest.tsv`: no manifest entry for this lexeme [Germanic/docs/lexeme_reports/report_manifest.tsv:line-1-14].
- Packet and memo status: both supporting files exist and already agree that the live row should preserve the `PROTO` / `PROTOFORM` split rather than collapsing everything to the class-I form; they are useful corroboration, but the controlling row-local authority still lives in `DEV_NOTES.md` plus the live TSV row [Germanic/docs/lexeme_reports/packets/2027-follow-fylġan.md:line-1-47; Germanic/docs/lexeme_reports/research_memos/2027-follow-fylġan.md:line-1-23].

## Development-note summary

This row has securely attachable row-specific DEV_NOTES authority, and it is strong enough to replace repeated return visits to `DEV_NOTES.md` in normal workflow. The decisive material is the 2026-03-09 row analysis at `DEV_NOTES:line-4402-4470`, read together with the live TSV row and the short implementation log at `DEV_NOTES:line-4596-4601`. That cluster establishes that the inherited comparative lexeme is still `*fulgēną`, but the OE row should be derived through a separate class-I formation, now represented in the TSV as `*fúlgijaną`, yielding normalized `fylġan` rather than `folgian` [DEV_NOTES:line-4402-4470; DEV_NOTES:line-4596-4601; Germanic/data/germanic-aligned-final.tsv:line-376].

The central philological point is not that OE had only one verb here. DEV_NOTES explicitly preserves Ringe and Taylor's dual-formation account: `PNWGmc *fulgija- ~ *fulgai-`, giving OE `fylgan` beside `folgian`, and adds the key quotation that the dual formation "probably reflects an original alternation between j-present and ē-stative" [DEV_NOTES:line-4411-4415; @RingeTaylor2014, pp. 293-294]. Kroonen is handled compatibly: the comparative headword remains the `*fulgēn-` family, but OE `fylg(e)an` is treated as continuing `*fulgjan-`, so the row is not a claim that `fylġan` is the direct unmodified infinitive reflex of bare `*fulgēną` [Germanic/data/germanic-aligned-final.tsv:line-376; DEV_NOTES:line-4406-4410; @Kroonen2013].

DEV_NOTES also makes the regular-vs-attested contrast explicit and should continue to do so in later work. When the project tested bare class-III/class-II `*fulgēną`, the cascade returned `folgon`, not `folgian`; DEV_NOTES states plainly that `*fulgēną → folgian` is **not** a regular phonological infinitive pathway because the `-ian` infinitive is a later class-II morphological reanalysis, not a straight sound-law outcome [DEV_NOTES:line-4416-4426]. By contrast, once the NWGmc u-lowering conditioning was repaired so that intervening `*j` blocks the lowering environment, the class-I input `*fulgjăną` produced `fylġan`, matching the attested class-I OE form [DEV_NOTES:line-4430-4438]. For row work, that means the decisive problem was stem/formation choice, not an unfinished sound law.

The most reusable current-policy wording is the step-4 solution note. DEV_NOTES says the class-I infinitive regularly yields OE `fylġan` because `*u` does **not** lower to `*o` when `*j` intervenes, then does undergo i-umlaut to `y`; it also preserves the short but useful quotation from R/T §2.1.1 that lowering fails where "`*j` intervened" [DEV_NOTES:line-4452-4456; @RingeTaylor2014]. The same fragment then states the complementary claim that class-II `folgian` belongs to the analogically remodeled `*-ē-` stem branch, where lowering to `o` is possible and the infinitive was later reshaped to productive `-ian` [DEV_NOTES:line-4458-4460]. Later report prose should therefore keep the contrast explicit: regular project comparator `*fulgēną -> folgon` for the abandoned direct class-II path, current row-target derivation `*fúlgijaną -> fylġan`, and parallel OE `folgian` as the remodeled class-II/literary branch rather than as the form this row itself must target [DEV_NOTES:line-4462-4470].

One project-history correction must stay visible so later writers do not silently reintroduce an obsolete metadata collapse. The implementation note records that row 2027 was temporarily edited so that `PROTO`, `PROTOFORM`, and target all shifted together to the class-I solution [DEV_NOTES:line-4596-4601]. That is no longer the best reading of the row. The live TSV and the research memo both restore the better distinction: `PROTO = *fulgēną` as comparative headword, `PROTOFORM = *fúlgijaną` as OE-directed input, and `COUNTERPART = fylġan` as the selected OE class-I outcome [Germanic/data/germanic-aligned-final.tsv:line-376; Germanic/docs/lexeme_reports/research_memos/2027-follow-fylġan.md:line-13-23,49-60]. The row should therefore be treated as an **early-formation-selection case**, not as a reason to rewrite the cognate-set proto itself.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-3980-3992

- Source heading: `The individual verbs` / `folgian (ID 2027)`
- Source line or section hint: `lines 3980-3992`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `initial_probe`; `i_umlaut_bug_suspicion`; `class_i_vs_class_ii`; `project_chronology`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This early probe is worth keeping only as row history. It already identified the real comparative problem correctly — Kroonen's `*fulgēn-` material coexists with an OE/ON class-I `*fulgjan-` branch, and direct `*fulgēną` testing yields `folgon` rather than the desired infinitive — but it still misread the class-I output as `felġan` and therefore treated the row as an i-umlaut bug candidate [DEV_NOTES:line-3980-3992]. Later work should preserve this fragment so the chronology is recoverable, but should not cite it as if the bug diagnosis survived. The later row note explicitly replaces that reading once the u-lowering conditioning was fixed.

### DEV_NOTES:line-4402-4415

- Source heading: `Part 1: folgian (Row 2027)` / `Step 1: Proto-Germanic infinitive in the literature`
- Source line or section hint: `lines 4402-4415`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `dual_formation`; `proto_vs_protoform`; `comparative_headword`; `literature_basis`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment is the main comparative anchor for the row. It preserves the split between Kroonen's class-III/headword zone and Ringe-Taylor's dual formation, including the quotation that the OE alternation "probably reflects an original alternation between j-present and ē-stative" [DEV_NOTES:line-4406-4415; @RingeTaylor2014, pp. 293-294; @Kroonen2013]. If later report prose needs to explain why the row keeps `PROTO = *fulgēną` while deriving the OE form from `*fúlgijaną`, this is the fragment that makes that structure philologically defensible.

### DEV_NOTES:line-4416-4448

- Source heading: `Part 1: folgian (Row 2027)` / `Step 2: Can PGmc infinitive regularly yield OE infinitive?` through `Step 3: Other paradigm cells`
- Source line or section hint: `lines 4416-4448`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `regular_comparator`; `mismatch_exposure`; `formation_selection`; `finite_cell_probe`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the best replacement-note record of the row diagnosis itself. DEV_NOTES first demonstrates that `*fulgēną` gives `folgon`, not `folgian`, and explains why: the `-ian` infinitive of class-II OE verbs is not the direct phonological continuation of PGmc class-III `*-ēną` [DEV_NOTES:line-4418-4426]. It then records the corrected class-I test, `*fulgjăną -> fylġan`, and notes that finite cells like `*fulgēþi -> folġeþ` were examined but lacked evidence as surviving archaic relics [DEV_NOTES:line-4430-4448]. For later work this fragment matters because it rules out two tempting shortcuts at once: keeping `folgian` as if it were the regular direct reflex, or switching the row to an unattested finite-cell workaround.

### DEV_NOTES:line-4450-4470

- Source heading: `Part 1: folgian (Row 2027)` / `Step 4: Solution`
- Source line or section hint: `lines 4450-4470`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `target_correction`; `class_i_derivation`; `u_lowering_blocked_by_j`; `analogy_background`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling current-policy fragment. It states in compact, reusable form that class-I `*fulgjăną` regularly yields OE `fylġan`, because `*j` blocks `u`-lowering and then triggers i-umlaut to `y`, while class-II `folgian` belongs to the analogically remodeled `*-ē-` branch [DEV_NOTES:line-4452-4460]. The option table then makes the working decision explicit: reject `*fulgēną -> folgian` as a mismatch, accept `*fulgjăną -> fylġan` as the regular and attested solution, and reject finite-cell `folġeþ` as lacking evidence [DEV_NOTES:line-4462-4470]. If a later lexeme report cites only one DEV_NOTES fragment for row 2027, it should be this one.

### DEV_NOTES:line-4596-4601

- Source heading: `Implementation (2026-03-09f continued)` / `Row 2027 (folgian → fylġan)`
- Source line or section hint: `lines 4596-4601`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `implemented_change`; `stale_proto_change`; `row_edit_history`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This short implementation log is still useful, but only as chronology. It preserves the exact edit bundle made when the row was first converted to the class-I solution, including the now-superseded claim that `PROTO` itself should change to the class-I form [DEV_NOTES:line-4596-4600]. The live TSV no longer follows that last step. Keep this fragment to document how the project got from `folgian` to `fylġan`, but do not cite it as present metadata authority without also stating that the comparative `PROTO` / OE-facing `PROTOFORM` distinction has since been restored.

## Superseded or diagnostic material

The superseded material here is not the class-I analysis itself. What has been superseded is first the early suspicion that the row still reflected an i-umlaut bug (`felġan` instead of `fylġan`), and second the temporary implementation-era collapse that rewrote `PROTO` as if the comparative headword and the OE-directed derivational input were identical [DEV_NOTES:line-3980-3992; DEV_NOTES:line-4596-4601]. The current row keeps the better three-part distinction: comparative `*fulgēną`, OE-facing `*fúlgijaną`, and normalized OE target `fylġan` [Germanic/data/germanic-aligned-final.tsv:line-376].

Diagnostic but still useful background also survives around `folgian`. DEV_NOTES does **not** say that `folgian` is unreal or should be erased from OE discussion. It says that `folgian` belongs to the parallel analogically remodeled class-II branch and therefore should not be forced into this row as the directly regular reflex of bare `*fulgēną` [DEV_NOTES:line-4458-4470]. Later work should preserve that narrower claim, especially because lightweight dictionary material in the packet still surfaces `follow -> folgian` and could otherwise tempt a false either/or framing [Germanic/docs/lexeme_reports/packets/2027-follow-fylġan.md:line-171-178].

## Open questions for later work

- Decide whether the final lexeme report should quote Ringe and Taylor's dual-formation line directly, since it is the cleanest single explanation for why OE preserves both `fylgan` and `folgian` [DEV_NOTES:line-4411-4415].
- If the final report discusses orthography, keep the statement modest: the row target is normalized `fylġan`, while DEV_NOTES and the dictionaries also cite `fylgan` / `fylgean`; the important issue is the class-I versus class-II formation split, not a manuscript-spelling argument [DEV_NOTES:line-4436-4438,4452-4456; Germanic/docs/lexeme_reports/research_memos/2027-follow-fylġan.md:line-61-71].
- If the TSV note is ever tightened, preserve the distinction between `PROTO` and `PROTOFORM`; row 2027 is a good example of why the project needs both fields.
- If later report work wants a compact diagnostic comparison table, the most useful three lines are `*fulgēną -> folgon`, `*fúlgijaną -> fylġan`, and the rejected finite-cell probe `*fulgēþi -> folġeþ`.
