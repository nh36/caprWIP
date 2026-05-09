---
row_id: 1933
concept: adder
counterpart: nǣdre
proto: *nḗdrōn
protoform: *nḗdrōn
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/lexeme_reports/pilot/adder.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1933 adder / nǣdre

## Current row state

- The live OE row reads `ID = 1933`, `CONCEPT = adder`, `COUNTERPART = nǣdre`, `PROTO = *nḗdrōn`, `PROTOFORM = *nḗdrōn`, and `DERIVATION_CLASS = regular`; the `NOTE` field is empty, while the history field preserves duplicated Wiktionary-etymology provenance text [Germanic/data/germanic-aligned-final.tsv:4-4].
- `PROTO` and `PROTOFORM` are currently identical. The live row has already absorbed the DEV_NOTES correction away from older `*nadrō`; no alternate OE-facing rescue form is now encoded in the TSV [Germanic/data/germanic-aligned-final.tsv:4-4; Germanic/docs/DEV_NOTES.md:6095-6158].
- `oe_known_problems.tsv` has no row-local entry for `1933`, `adder`, `nǣdre`, or `*nḗdrōn`; the current ledger lists unrelated exception and wontfix items only [Germanic/data/oe_known_problems.tsv:1-8].
- Row-local support infrastructure is thin but not absent. No matching packet or research memo file was found for row `1933`, but `coverage_audit.md` and `report_manifest.tsv` both point to `pilot/adder.md`, and that pilot note treats the row as a regular control case [Germanic/docs/lexeme_reports/coverage_audit.md:425-435; Germanic/docs/lexeme_reports/report_manifest.tsv:1-2; Germanic/docs/lexeme_reports/pilot/adder.md:1-19].
- The published derivation traces are exact matches. The compact report gives `PROTO: *nḗdrōn`, `EXPECTED: nǣdre`, `OUTPUTS: nǣdre`, with the named path `NWGmc N Stem N Loss: *nḗdrǭ`, `NWGmc Long E Lowering: *nǣdrǭ`, `OE Unstressed Long Vowel Shortening: *nǣdræ`, `OE Unstressed AE Merger: *nǣdre` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1-24]. The full trace writes the proto string as `*nēdrōn` rather than acute-accented `*nḗdrōn`, but the derivation is the same and ends in orthographic/surface `nǣdre` [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:1-56].

## Development-note summary

The surviving row-specific DEV_NOTES discussion is clear about what had gone wrong and what had to be preserved. The older TSV had `*nadrō` as the proto-form, and under that setup the transducer produced `næder`, i.e. the wrong vowel quantity and the wrong ending for the OE target `nǣdre` [Germanic/docs/DEV_NOTES.md:6093-6097]. DEV_NOTES does not treat that as a minor orthographic cleanup. It argues that the old proto-form represented the wrong member of an ablauting lexical pair.

The note's central philological claim is that Kroonen distinguishes two related Germanic snake words, not one. DEV_NOTES quotes first `"*nadra- m. 'adder, snake' — Go. nadrs m. 'id.', ON nadr m. 'id.'"`, then separately `"*nédron- f. 'viper' — OE nǣdre, nǣddre f. 'id.' ..."`, followed by the explicit sentence `"A formation ablauting with *nadra- (q.v.)."` [Germanic/docs/DEV_NOTES.md:6103-6114]. The note then states the row-level consequence in plain terms: `OE nǣdre comes from the e-grade feminine *nēdrōn, NOT the zero-grade masculine *nadra-.` [Germanic/docs/DEV_NOTES.md:6116-6117]. For this row, that is the decisive reason the protoform was changed.

DEV_NOTES reinforces the same distinction with Orel. The quoted passage under `*naþraz` ends `"See also *nēþrōn ~ *naþrōn."` and the note glosses that as explicit support for a feminine long-vowel form behind the West Germanic reflexes [Germanic/docs/DEV_NOTES.md:6121-6127]. Campbell is then used to anchor the OE side: DEV_NOTES quotes `"næddre adder, ǣttres g.s. poison"` and explains that the doubled `-dd-` is secondary from `-ðr-`, while the long `ǣ` is the regular continuation of PGmc `*ē` [Germanic/docs/DEV_NOTES.md:6129-6135]. In other words, the note preserves both parts of the OE form that the older `*nadrō` input mishandled: the long vowel and the weak feminine ending.

The ablaut argument is written out explicitly and should be kept explicit in any later report. DEV_NOTES derives the masculine form from PIE zero-grade `*n̥h₂tr-o- → PGmc *nadra-` and the feminine from e-grade `*neh₂tr-éh₂- → PGmc *nēdrōn-`, then states that West Germanic generally continues the feminine e-grade form (`OE nǣdre`, `OHG nāt(a)ra`, `OS nādra`), while Gothic and Norse continue the masculine zero-grade (`Go. nadrs`, `ON naðr`) [Germanic/docs/DEV_NOTES.md:6137-6150]. That is more than background etymology: it explains why the OE row should not be normalized back toward the Gothic/Norse-looking masculine stem.

For the live row, the important follow-through is that the DEV_NOTES fix is already incorporated. The note says the project changed `PROTOFORM` from `*nadrō` to `*nēdrōn`, with the derivational expectations `*nē- → OE nǣ-` and `-drōn → OE -dre`, and concludes `FST now correctly produces nǣdre` [Germanic/docs/DEV_NOTES.md:6152-6158]. The current row and both current published traces confirm that this is now the live state, though current row-level notation prefers acute-accented `*nḗdrōn` where DEV_NOTES and the full trace use `*nēdrōn` [Germanic/data/germanic-aligned-final.tsv:4-4; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5-24; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:3-56]. Nothing in the surviving notes suggests that this accent difference encodes a different reconstruction; it is best treated conservatively as notation-layer variation.

A second strand of DEV_NOTES is directly relevant but no longer current as the row's main explanation. Before the protoform was corrected, `adder` was repeatedly used as a diagnostic example in the OE A-restoration investigation. One status note says: `Fronting undone by A-restoration: *nadrō (adder) fronting yields *æ, but OldEnglishARestoration flips it back due to a back vowel in the next syllable; output nadrō vs expected nǣdre.` Another records `*nadrō -> nǣdre` among the A-restoration false positives with intervening `dr` [Germanic/docs/DEV_NOTES.md:1715-1723]. A later literature-grounded repair note keeps the lexeme in play but changes the diagnosis: `*nadrō` should be blocked because `*dr` is a cluster, not because liquids are globally excluded, and the old FST got `*nadrō → nædre` right only `incidentally` [Germanic/docs/DEV_NOTES.md:36517-36546]. Those passages remain worth preserving because they explain why `adder` shows up in the shared rule history, but they belong to the superseded `*nadrō` analysis rather than to the current row state built on `*nḗdrōn`.

## Relevant DEV_NOTES fragments

### `Germanic/docs/DEV_NOTES.md:6091-6158`

- Source heading: `OE nǣdre 'adder': Fix proto-form *nēdrōn (2026-03-10)`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `protoform_correction`; `ablaut`; `feminine_ōn_stem`; `source_audit`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling row-specific fragment. It preserves both the mistaken older state and the durable correction. DEV_NOTES says the older TSV had `*nadrō`, that the FST therefore produced `næder`, and that the expected form is `nǣdre` with long vowel and weak feminine ending [Germanic/docs/DEV_NOTES.md:6093-6097]. The note then quotes Kroonen's two-way lexical split, including `"*nadra- m. 'adder, snake' ..."` versus `"*nédron- f. 'viper' — OE nǣdre, nǣddre f. 'id.' ..."` and `"A formation ablauting with *nadra- (q.v.)."` [Germanic/docs/DEV_NOTES.md:6103-6114].

The fragment's row-level conclusion is explicit and should be quoted almost as-is when needed: `OE nǣdre comes from the e-grade feminine *nēdrōn, NOT the zero-grade masculine *nadra-.` [Germanic/docs/DEV_NOTES.md:6116-6117]. Orel's `"See also *nēþrōn ~ *naþrōn"` and Campbell's `"næddre adder, ǣttres g.s. poison"` are used inside the same note to support, respectively, the long-vowel feminine comparator and the secondary nature of `-dd-` [Germanic/docs/DEV_NOTES.md:6121-6135]. The note closes with the direct implementation claim that `PROTOFORM` was changed to `*nēdrōn` and that the FST now outputs `nǣdre` [Germanic/docs/DEV_NOTES.md:6154-6158].

### `Germanic/docs/DEV_NOTES.md:1715-1723`

- Source heading: `Concrete “rule not firing” evidence` / `Measured ARestoration intervening segments`
- Fragment type: `shared_rule_discussion_directly_bearing_on_row`
- Status: `diagnostic_only`
- Issue tags: `a_restoration`; `fronting_missing_no_trigger`; `older_protoform`; `false_positive_bucket`
- Recommended next use: `background_only`
- Shared with row IDs: `1934`; `1942`; `1943`; `1968`; other A-restoration dossiers

This fragment is directly row-relevant only as preserved project history for the older `*nadrō` state. DEV_NOTES writes: `Fronting undone by A-restoration: *nadrō (adder) fronting yields *æ, but OldEnglishARestoration flips it back due to a back vowel in the next syllable; output nadrō vs expected nǣdre.` It then lists `*nadrō -> nǣdre, inter=dr` among the false positives measured for A-restoration [Germanic/docs/DEV_NOTES.md:1716-1723]. The lasting value is diagnostic: before the lexeme-specific protoform correction and before the later rule cleanup, `adder` was one of the examples exposing that the then-current A-restoration implementation was misclassifying forms with back-vowel tails.

For a final row report, this fragment should not be allowed to outrank the dedicated lexeme note at `6091-6158`. It is about a transducer failure on the obsolete proto input `*nadrō`, not about the live row's successful `*nḗdrōn → nǣdre` path [Germanic/data/germanic-aligned-final.tsv:4-4; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5-24].

### `Germanic/docs/DEV_NOTES.md:36517-36546`

- Source heading: `§17.25.2 The canonical conditioning of A-restoration (literature consensus)`
- Fragment type: `shared_rule_discussion_directly_bearing_on_row`
- Status: `diagnostic_only`
- Issue tags: `a_restoration`; `cluster_conditioning`; `liquid_veto_overcorrection`; `older_protoform`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs: multiple A-restoration rows

This is the best shared-rule explanation of why `adder` appeared in the A-restoration dossier at all. DEV_NOTES says the old exclusion of `*r` and `*l` from the restoration environment was an `over-correction`, added partly to defeat `false positives like *nadrō → *nadre`, but that these forms are really blocked by consonant-cluster effects, `not by liquids per se` [Germanic/docs/DEV_NOTES.md:36517-36522]. It then states the row-specific lesson in one sentence: `The current FST handles *nadrō → nædre correctly only incidentally: *r is excluded → restoration cannot fire. Under the literature-grounded rule ({single C | geminate | sC | fC}), *nadrō is blocked by the *dr cluster — same surface result, correct cause.` [Germanic/docs/DEV_NOTES.md:36543-36546].

That diagnosis still matters if later work revisits the older `*nadrō` comparator, because it separates the row's accidental old success from the linguistically correct conditioning story. But it is still diagnostic material around the superseded masculine-looking protoform, not the main evidence for the current row.

### `Germanic/docs/DEV_NOTES.md:36649-36768`

- Source heading: `§17.25.7 Regression after first build` / `§17.25.8 Post-fix verification`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `probe_history`; `regression_check`; `older_protoform`; `no_regression`
- Recommended next use: `background_only`
- Shared with row IDs: multiple A-restoration rows

This fragment is useful only because it records the old probe discipline around `adder`. During the A-restoration repair cycle, DEV_NOTES repeatedly used `echo 'nadrō' | flookup ...` as a no-regression probe, first with expected `nædre/næder`, then with the post-fix confirmations `*nadrō → næder` and `*nadrō → næder ✓ (no regression — *dr cluster correctly blocks)` [Germanic/docs/DEV_NOTES.md:36649-36656; Germanic/docs/DEV_NOTES.md:36742-36768].

For row `1933`, this should be kept only as diagnostic chronology. It documents how the old comparator behaved while shared rule work was being repaired, but it predates the dedicated `*nēdrōn` correction note and therefore should not be mistaken for the present row policy.

## Superseded or diagnostic material

The main superseded material is the entire `*nadrō` storyline. In surviving DEV_NOTES, that older protoform shows up in two ways: first as the lexeme-specific mistake later corrected by the March 2026 `nǣdre` note, and second as a recurring probe form in the shared A-restoration investigations [Germanic/docs/DEV_NOTES.md:6095-6097; Germanic/docs/DEV_NOTES.md:1716-1723; Germanic/docs/DEV_NOTES.md:36543-36546; Germanic/docs/DEV_NOTES.md:36654-36768]. Later reporting should preserve this history, but label it clearly as old project state, not current row design.

The durable part of that old material is methodological rather than lexical. It shows that `adder` was once used to test whether the A-restoration rule was mis-specified, and that later notes concluded the old success on `*nadrō` came from the wrong mechanism: a liquid veto instead of proper cluster conditioning [Germanic/docs/DEV_NOTES.md:36517-36546]. That remains worth retaining as transducer-history context, especially because other row packets cite `adder` as a diagnostic example.

A smaller diagnostic caution is notational. The live TSV and compact published trace use acute-accented `*nḗdrōn`, whereas the row-specific DEV_NOTES note and the full trace write `*nēdrōn` [Germanic/data/germanic-aligned-final.tsv:4-4; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5-18; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:3-16; Germanic/docs/DEV_NOTES.md:6116-6158]. Nothing in the surviving material turns that into a substantive reconstruction dispute, so it should be treated conservatively as editorial notation variation unless a later memo shows otherwise.

## Open questions for later work

- If this row eventually gets a packet or research memo, it should keep the lexeme-specific correction front and center: OE `nǣdre` is tied in DEV_NOTES to the feminine e-grade `*nēdrōn/*nḗdrōn`, not to masculine `*nadra-` [Germanic/docs/DEV_NOTES.md:6103-6158].
- If later reporting wants to discuss the older `*nadrō` probe history, it should label that material explicitly as superseded or diagnostic. The A-restoration notes are genuinely relevant project history, but they are not the authority for the live row after the protoform correction [Germanic/docs/DEV_NOTES.md:1715-1723; Germanic/docs/DEV_NOTES.md:36517-36768].
- If the report stack is cleaned up, decide whether the current pilot file `Germanic/docs/lexeme_reports/pilot/adder.md` should be replaced by a fuller packet/memo workflow or simply left as a light regular-control note. At present there is enough row-specific DEV_NOTES material to justify a substantial slice, but not yet a dedicated packet or research memo [Germanic/docs/lexeme_reports/report_manifest.tsv:1-2; Germanic/docs/lexeme_reports/pilot/adder.md:1-19].
- If a future indexing pass wants one fragment only, `Germanic/docs/DEV_NOTES.md:6091-6158` is the obvious candidate. It is lexeme-specific, source-based, and still current; the A-restoration fragments are secondary and mostly diagnostic.
