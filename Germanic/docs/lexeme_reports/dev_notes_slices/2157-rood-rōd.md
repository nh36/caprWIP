---
row_id: 2157
concept: rood
counterpart: rōd
proto: *rōdō
protoform: *rōdō
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2157 rood / rōd

## Current row state

- CONCEPT: `rood` [Germanic/data/germanic-aligned-final.tsv:880]
- COUNTERPART: `rōd` [Germanic/data/germanic-aligned-final.tsv:880]
- PROTO: `*rōdō` [Germanic/data/germanic-aligned-final.tsv:880]
- PROTOFORM: `*rōdō` [Germanic/data/germanic-aligned-final.tsv:880]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:880]
- `oe_known_problems.tsv` currently has no row-local entry for `2157`, `*rōdō`, `rood`, or `rōd`; this lexeme is not being tracked as an OE exception or wontfix item there [Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation trace is fully regular and already matches the target: `PROTO: *rōdō`, `EXPECTED: rōd`, `OUTPUTS: rōd`, with the explicit staged path `NWGmc Final Long O Raising: *rōdu` and then `OE High Vowel Apocope: *rōd` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3670-3689].
- Coverage infrastructure still shows no attached packet, research memo, or dossier for this row beyond the slice being created here; the coverage audit lists row `2157` as `regular` with all linked-report fields empty and issue status `none` [Germanic/docs/lexeme_reports/coverage_audit.md:328-328].
- No dedicated row-specific `DEV_NOTES.md` dossier for `rood / rōd / *rōdō` survives. The securely attachable material is shared infrastructure-level discussion of (i) bimoraic word-final `*-ō > *-u` and (ii) later apocope of final high vowels after stressed heavy syllables [Germanic/docs/DEV_NOTES.md:2711-2719,3542-3590,18624-18657].

## Development-note summary

Row `2157` is currently a clean regular-control row, and the current trace already shows the whole derivation that later reviewers are likely to need: `*rōdō > *rōdu > rōd` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3670-3689]. Nothing in the live row suggests a paradigm-cell workaround, analogical retargeting, or exception bucket. `PROTO` and `PROTOFORM` are both `*rōdō`, and the OE target is the ordinary normalized form `rōd` [Germanic/data/germanic-aligned-final.tsv:880].

The relevant DEV_NOTES support is therefore not a row-local controversy file but the shared discussion of **bimoraic final `*-ō`**. DEV_NOTES states in compact rule form that word-final bimoraic non-nasalized long `*-ō` became short `*-u` in PNWGmc/NWGmc and says the project models this with `NWGmcFinalLongORaising: {*ō} -> {*u} || _ .#.` [Germanic/docs/DEV_NOTES.md:2711-2719]. The later cross-source review says the major handbooks agree on the same point: Luick, Bülbring, and Ringe-Taylor all treat bimoraic final `*-ō` as the class that raises to `u`, contrasting it with trimoraic `*-ô`, which stays long longer and has different OE outcomes [Germanic/docs/DEV_NOTES.md:3546-3559]. For row `2157`, that shared distinction matters directly. The row ends in plain `*-ō`, so it belongs to the `*gebō > *gebu` type, not to the trimoraic `*namô > nama` type and not to the `*-ōz` class whose later OE reflexes go through different shortening and fronting histories [Germanic/docs/DEV_NOTES.md:3558-3590].

The second half of the row's regular pathway is equally shared but equally important. DEV_NOTES' apocope research distinguishes an early Germanic apocope from a later pre-OE apocope after stressed heavy syllables; in that later stage, “original i and u were still fully preserved” after stressed syllables in pre-OE and were then “partly apocopated in OE” [Germanic/docs/DEV_NOTES.md:18624-18657]. Elsewhere the same research block states that high-vowel apocope after heavy syllables is a general sound law, not a row-specific patch [Germanic/docs/DEV_NOTES.md:18912-18918]. That is exactly what the current trace shows for `*rōdu > rōd`: once the word-final bimoraic `*-ō` has raised to `*-u`, the heavy monosyllabic stem `rōd-` loses that final high vowel in the ordinary OE apocope stage [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3681-3689].

The most important row-level distinction to preserve is therefore the one between **mora classes and row layers**, not between competing lexical analyses. `PROTO` and `PROTOFORM` are the same here because the row does not need an alternative OE-directed input. But that sameness should not tempt later readers to flatten the phonology: the row depends specifically on plain bimoraic final `*-ō`, which raises, and then on later OE loss of final high vowel after a heavy syllable [Germanic/data/germanic-aligned-final.tsv:880; Germanic/docs/DEV_NOTES.md:2711-2719,3546-3590,18624-18657]. If the ending were misread as trimoraic `*-ô` or as a sheltered `*-ōz` form, the expected OE ending would be different. This slice should therefore be used as a **shared-support/control-case note** for regular `*rōdō > rōd`, not as a mismatch dossier.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2711-2719

- Source heading: `Path A: PNWGmc Raising (bimoric *ō that is word-final in PGmc)`
- Source line or section hint: `lines 2711-2719`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `bimoraic_final_ō`; `NWGmc_final_long_o_raising`; `regular_pathway`; `suffix_quantity`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the clearest compact rule statement currently attachable to row `2157`. DEV_NOTES gives the pathway in exactly the form this row needs: word-final bimoraic `*-ō` raises to `*-u`, and the project models that with `NWGmcFinalLongORaising: {*ō} -> {*u} || _ .#.` [Germanic/docs/DEV_NOTES.md:2711-2719]. The note's examples are other lexemes (`*gebō`, `*grasō`, `*kwemō`), but the rule is the same one the trace now applies to `*rōdō`, producing the intermediate `*rōdu` before OE apocope [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3681-3689].

For this row, the fragment establishes two concrete points. First, the final vowel in `*rōdō` is being treated as the ordinary bimoraic word-final `*-ō` class, not as a special exception. Second, the intermediate `*rōdu` shown in the trace is not an ad hoc project spelling but the expected shared NWGmc stage for this suffix type [Germanic/docs/DEV_NOTES.md:2713-2719; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3683-3683].

### DEV_NOTES:line-3542-3590

- Source heading: `Bimoraic vs. trimoraic *-ō: cross-source analysis and pipeline verification`
- Source line or section hint: `lines 3542-3590`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `bimoraic_vs_trimoraic`; `suffix_quantity`; `protoform_vs_proto`; `shared_row_support`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the best shared literature-and-pipeline fragment for keeping row `2157` from being silently misclassified. DEV_NOTES says all major sources agree on the fundamental distinction between bimoraic and trimoraic final `*-ō`; it then states the point most relevant here in explicit terms: “Bimoraic final `*-ō → u`: All sources agree,” while trimoraic `*-ô` has a different OE outcome [Germanic/docs/DEV_NOTES.md:3546-3560]. The verification table then shows the operational split inside the grammar: `*rastō (nom.sg.)` takes `NWGmcFinalLongORaising` plus heavy apocope, whereas `*namô (n-stem nom.sg.)` does **not** take the raising path and instead yields `nama` through later long-vowel shortening [Germanic/docs/DEV_NOTES.md:3576-3590].

For row `2157`, this fragment establishes what the current row state does **not** spell out on its own. `*rōdō` belongs with the `*rastō`-type pathway, not with trimoraic `*namô` and not with `*-ōz` cases whose later history produces `-e` or `-a` endings [Germanic/docs/DEV_NOTES.md:3564-3590]. That is why the live row can keep `PROTO = PROTOFORM = *rōdō` and remain fully regular: the row is not missing a hidden inflectional cell, but simply instantiates the ordinary bimoraic final-`ō` pathway [Germanic/data/germanic-aligned-final.tsv:880; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3679-3689].

### DEV_NOTES:line-18624-18657

- Source heading: `§15.1: Two Distinct Stages of High Vowel Apocope`
- Source line or section hint: `lines 18624-18657`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `high_vowel_apocope`; `heavy_syllable`; `final_u_loss`; `shared_phonology`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the shared DEV_NOTES fragment that explains the second step of the row's derivation. The table distinguishes a later pre-OE apocope stage “after heavy stressed syllables,” and Brunner is quoted to the effect that after stressed syllables original `i` and `u` were still preserved in pre-OE and were then partly apocopated in OE [Germanic/docs/DEV_NOTES.md:18624-18657]. That is the exact structural environment needed for `*rōdu > rōd`.

The fragment is especially useful because it prevents later reviewers from treating final `-u` loss here as a row-local special fix. DEV_NOTES frames this as a shared chronological stage, not as a `rood/rōd` exception [Germanic/docs/DEV_NOTES.md:18624-18657]. The current trace then supplies the row-specific confirmation that this shared law is what actually happens in the live grammar: `NWGmc Final Long O Raising: *rōdu`, followed by `OE High Vowel Apocope: *rōd` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3683-3689].

## Superseded or diagnostic material

- No securely attachable row-local superseded dossier currently survives for `2157`. The main thing to guard against is not stale row policy but category drift: this row should not be folded into trimoraic `*-ô` material or `*-ōz` material, because the shared DEV_NOTES review gives those classes different outcomes from the one actually shown by `*rōdō > *rōdu > rōd` [Germanic/docs/DEV_NOTES.md:3560-3590; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3681-3689].
- Likewise, the absence of an `oe_known_problems.tsv` entry matters. This row is not a documented mismatch bucket item, so later reporting should not invent an exception dossier merely because the slice is detailed [Germanic/data/oe_known_problems.tsv:1-8; Germanic/data/germanic-aligned-final.tsv:880].
- The surviving DEV_NOTES support is shared/control-case material rather than a bespoke lexeme essay. That is the securely current state of the evidence and should be preserved as such, not rewritten into a false impression that DEV_NOTES contains a dedicated `rōd` problem note [Germanic/docs/DEV_NOTES.md:2711-2719,3542-3590,18624-18657].

## Open questions for later work

- If a packet or memo is eventually created, copy the current trace explicitly as `*rōdō > *rōdu > rōd`, since that now supplies the row-specific derivation that DEV_NOTES only supports through shared phenomenon notes [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3670-3689].
- If `dev_notes_slices/index.tsv` is updated later, index this row as a **current shared-support/control-case note** for bimoraic final `*-ō` plus heavy-syllable high-vowel apocope, not as a row-specific mismatch or exception dossier [Germanic/docs/DEV_NOTES.md:2711-2719,3542-3590,18624-18657].
- If later ō-stem review revisits rows of this shape, keep the mora-class distinction explicit in any final report: row `2157` depends on plain bimoraic final `*-ō`, not on trimoraic `*-ô` and not on the separate `*-ōz` history [Germanic/docs/DEV_NOTES.md:3558-3590].
