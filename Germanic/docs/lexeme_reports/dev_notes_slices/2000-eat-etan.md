---
row_id: 2000
concept: eat
counterpart: etan
proto: *étaną
protoform: *étaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/debug_snapshots/oe_full_trace_report.txt
  - Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2000 eat / etan

## Current row state

- The live row currently reads `ID = 2000`, `CONCEPT = eat`, `COUNTERPART = etan`, `PROTO = *étaną`, `PROTOFORM = *étaną`, and `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:270-270].
- `PROTO` and `PROTOFORM` are identical here. The row is therefore not currently using a special OE-facing repair input, an oblique substitute, or a paradigm-cell workaround; the same Proto-Germanic form serves as both comparative label and derivational input in the live TSV [Germanic/data/germanic-aligned-final.tsv:270-270].
- `oe_known_problems.tsv` has no surviving entry for row `2000`, for `eat`, for `etan`, or for `*étaną`, and the coverage audit still lists the row as `regular` with all report-link fields empty and issue status `none` [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/coverage_audit.md:231-231].
- The current published derivation trace is an exact match: `PROTO: *étaną`, `EXPECTED: etan`, `OUTPUTS: etan`, with the decisive OE-side sequence `OE Heavy Syllable Nasal Apocope: *étan`, `OE Secondary Nasalization: *étąn`, `OE Weak Tail Reduction: *étan`, and final surface `etan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1078-1097].
- A fuller trace records the same successful derivation in more detail. It writes the input once as accentless/breve-marked `*etăną`, but it still ends at `Orthography: etan` and `Surface: etan`; for present purposes that difference is internal notation across debug artifacts, not evidence for a rival stored protoform or a rival OE target [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:7195-7309; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:3193-3246].
- The only clearly row-local DEV_NOTES mention now recoverable is not a lexeme dossier but an older diagnostics example: a closeness scan once listed `*etăną → ētan` vs expected `etan` among normalized-distance-zero near-misses, and the next line classed such cases as “orthography/diacritic alignment issues rather than phonology failures” [Germanic/docs/DEV_NOTES.md:2614-2621]. The live row and current traces now both target and produce `etan`, so that older `ētan` example should be retained as diagnostic history only, not as present row policy [Germanic/data/germanic-aligned-final.tsv:270-270; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1078-1097].

## Development-note summary

No dedicated row-specific DEV_NOTES dossier for `eat / etan` survives in the live notes file. That needs to be said plainly. The only direct row-local DEV_NOTES material now visible is the 2026-01-02 diagnostics example `*etăną → ētan` vs `etan`, and DEV_NOTES itself immediately frames that cluster as a matter of “orthography/diacritic alignment issues rather than phonology failures” rather than as evidence for a different lexical target or a failed derivation [Germanic/docs/DEV_NOTES.md:2614-2621].

The substantive support for row `2000` therefore comes from shared DEV_NOTES material about the regular Old English infinitive pathway in `*-aną`. DEV_NOTES argues that infinitives keep `-an` because heavy-syllable loss of final `*ą` is followed by coda-conditioned secondary nasalization before final `n`, and that this nasalization blocks the unstressed fronting that would otherwise push the weak vowel toward `-en` [Germanic/docs/DEV_NOTES.md:9592-9625,10818-10902,21000-21018]. That shared class analysis is directly borne out by the current row trace: `*étaną/*etăną > *étan > *étąn > *étan > etan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1091-1097; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:7258-7309].

The key distinction to preserve is therefore not between two competing OE counterparts, but between different kinds of evidence. `PROTO` and `PROTOFORM` remain the live comparative/derivational input `*étaną`; intermediate forms like `*étan`, `*étąn`, or the accentless/breve-marked debug spelling `*etăną` are stage forms inside the derivation; and `COUNTERPART = etan` is the attested OE target currently selected by the TSV [Germanic/data/germanic-aligned-final.tsv:270-270; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:7195-7309]. The old diagnostic output `ētan` should be treated conservatively as a former notation/length mismatch inside a near-miss report, not as a second stored row target [Germanic/docs/DEV_NOTES.md:2620-2621].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-9592-9625

- Source heading: `Primary vs Secondary Nasalization: The Correct Solution`
- Source line or section hint: `lines 9592-9625`
- Fragment type: `shared_phenomenon_context`
- Status: `current_with_notational_caution`
- Issue tags: `secondary_nasalization`; `infinitive_-an`; `fronting_block`; `shared_rule`
- Recommended next use: `cite_for_class_background`
- Shared with row IDs:

This fragment is not lexeme-specific, but it is the clearest surviving DEV_NOTES explanation for why a regular OE infinitive such as row `2000` should end in `-an` rather than drift toward `-en`. DEV_NOTES distinguishes “Primary Nasalization” from “Secondary Nasalization,” preserving the Ringe/Taylor quotation that “Stressed low vowels were nasalized when immediately followed by a nasal in the northern WGmc dialects; unstressed *a was apparently nasalized when immediately followed by a nasal in the syllable coda, but not when immediately followed by an intervocalic nasal” [Germanic/docs/DEV_NOTES.md:9597-9615]. It then states the operational consequence in project language: “The nasalization blocks fronting,” so “Nasalized `-a-` → stays `-a-` → OE `-an` (infinitive)” while “Non-nasalized `-a-` → fronts to `-æ-` → `-e-` → OE `-en` (participle)” [Germanic/docs/DEV_NOTES.md:9623-9625].

For row `2000`, this is the main philological substance that survives. The subsection still uses provisional symbol-design discussion, so its exact notation history should not be over-read; but the phonological distinction itself matches the current row trace, which explicitly includes an `OE Secondary Nasalization` stage between apocope and weak-tail reduction [Germanic/docs/DEV_NOTES.md:9627-9645; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1091-1097]. In other words, the symbol proposal is historical baggage, but the core claim about infinitive `-an` remains live and directly relevant.

### DEV_NOTES:line-10816-10902

- Source heading: `The Fix`; `Implementation Results (2026-03-15)`
- Source line or section hint: `lines 10816-10902`
- Fragment type: `shared_implementation_fragment`
- Status: `current`
- Issue tags: `heavy_syllable_nasal_apocope`; `secondary_nasalization`; `infinitive_class`; `pipeline_order`
- Recommended next use: `cite_for_current_rule_order`
- Shared with row IDs:

This fragment matters because it records the current implementation-facing chronology for the whole infinitive class. DEV_NOTES says: “We already have `OEHeavySyllableNasalApocope` ... We just need to run it BEFORE `OESecondaryNasalization`, not after,” and then simplifies the nasalization rule to true coda conditioning `_ {*n} .#.` [Germanic/docs/DEV_NOTES.md:10818-10839]. The preserved expected-derivations table is especially relevant: `*bakaną` becomes `bacan` and `*bindaną` becomes `bindan` because nasalization blocks fronting in infinitives, whereas participles such as `*fundanăz` continue to yield `funden` [Germanic/docs/DEV_NOTES.md:10841-10849].

The implementation-result block then states that the change was actually made and preserves the direct test outputs: “`bakaną   → bacan    ✓ (infinitive: nasalization blocks fronting)`” and “`bindaną  → bindan   ✓ (infinitive: nasalization blocks fronting)`” [Germanic/docs/DEV_NOTES.md:10882-10902]. Row `2000` is best understood as another member of that same regular class. The current trace for `*étaną` shows exactly the ordering this fragment defends: heavy-syllable apocope first, secondary nasalization second, then later denasalized/normalized `-an` at the surface [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:7258-7309].

### DEV_NOTES:line-20998-21018

- Source heading: `Why the baseline rule is already correct`
- Source line or section hint: `lines 20998-21018`
- Fragment type: `shared_derivational_summary`
- Status: `current`
- Issue tags: `infinitive_derivation`; `fronting_exception`; `shared_rule_order`; `denasalization`
- Recommended next use: `cite_for_explicit_class_derivation`
- Shared with row IDs:

This fragment is useful because it compresses the class behavior into a compact derivational recipe rather than a long debugging narrative. DEV_NOTES says the §333 infinitive exception is enforced “NOT by the fronting rule but by an earlier stage that *nasalises* the stem vowel so the fronting rule no longer sees it,” and then lays out the operative sequence: `OEHeavySyllableNasalApocope`, `OESecondaryNasalization`, `OEFinalSchwaApocope` [Germanic/docs/DEV_NOTES.md:21000-21009]. The worked example for `*hólpaną` is explicit: HeavyNasalApocope drops the final `*ą`, SecondaryNasalization produces `*hólpąn`, fronting does not fire, and later `OEWeakTailReduction1b` denasalises back to a form yielding `helpan` [Germanic/docs/DEV_NOTES.md:21011-21018].

For row `2000`, this fragment does not mention `etan`, but it is close to a direct prose gloss on the current trace. The same structural logic explains why `*étaną` remains in the infinitival `-an` class: after final `*ą` is removed in the heavy-syllable environment, the remaining final `-n` conditions nasalization, fronting is blocked, and later reduction/denasalization returns the written sequence `-an` rather than `-en` [Germanic/docs/DEV_NOTES.md:21000-21018; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1091-1097].

### DEV_NOTES:line-2614-2621

- Source heading: `OE diagnostics: mismatch closeness + diacritics (2026-01-02)`
- Source line or section hint: `lines 2614-2621`
- Fragment type: `lexeme_specific_diagnostic`
- Status: `superseded_but_row_specific`
- Issue tags: `diacritic_alignment`; `former_ētan_output`; `near_miss`; `row_local_example`
- Recommended next use: `retain_as_history_only`
- Shared with row IDs:

This is the only surviving fragment that names the row's derivation closely enough to count as row-local DEV_NOTES material. DEV_NOTES says that the normalized-distance-zero scan included “`*etăną → ētan` vs expected `etan`,” and the next bullet says the relevant traces “confirm these are orthography/diacritic alignment issues rather than phonology failures” [Germanic/docs/DEV_NOTES.md:2618-2621]. That wording is important: the note does not argue that `etan` is philologically wrong, nor does it promote `ētan` to a replacement target. It documents an earlier near-match whose remaining error was interpreted as surface/diacritic alignment.

For this slice, the fragment should therefore be preserved but carefully fenced. It is valuable because it is the one row-local breadcrumb in DEV_NOTES; it is not valuable as current derivational authority. The live TSV, the published derivation trace, and the fuller trace all now converge on plain `etan` [Germanic/data/germanic-aligned-final.tsv:270-270; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1078-1097; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:3193-3246]. The older `ētan` should thus stay in the dossier only as superseded diagnostic history.

## Superseded or diagnostic material

- The row does **not** have a surviving lexeme-specific DEV_NOTES mini-dossier comparable to the more heavily discussed problem rows. The only row-local DEV_NOTES material now recoverable is the old 2026-01-02 closeness-scan example `*etăną → ētan` vs `etan`, and DEV_NOTES itself already categorizes that cluster as orthography/diacritic noise rather than a phonological failure [Germanic/docs/DEV_NOTES.md:2614-2621].
- The older diagnostic `ētan` should not be promoted to current row status. In present project artifacts, `COUNTERPART` remains `etan`, the published derivation-class trace outputs `etan`, and the fuller trace also ends at `etan`; the long-vowel spelling survives only as a past near-miss example inside diagnostics [Germanic/data/germanic-aligned-final.tsv:270-270; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1078-1097; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:3193-3246].
- The older “Archived: Heavy Syllable Nasal Apocope” discovery note remains useful as project history for when the rule first entered the pipeline, but later DEV_NOTES sections give the cleaner and more current account for this row class because they incorporate the reordered relationship between heavy-syllable apocope and secondary nasalization [Germanic/docs/DEV_NOTES.md:1591-1620,10818-10902].
- The accent/breve differences among `*étaną`, `*etăną`, and intermediate trace forms such as `*étąn` should be treated conservatively as artifact-specific notation and chronology markers, not as proof of multiple rival stored protoforms for row `2000` [Germanic/data/germanic-aligned-final.tsv:270-270; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:7195-7309].
- No packet, research memo, or row-specific dossier file was located for this row, and the coverage audit still records `none` rather than an already-linked report infrastructure [Germanic/docs/lexeme_reports/coverage_audit.md:231-231].

## Open questions for later work

- If a packet or final lexeme report is written later, keep saying plainly that row `2000` is supported mainly by shared infinitive-class DEV_NOTES material plus exact modern traces, not by a rich row-local DEV_NOTES section [Germanic/docs/DEV_NOTES.md:9592-9625,10818-10902,21000-21018; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1078-1097].
- If future indexing work wants a row anchor, the safest current anchors are the shared class fragments at `10816-10902` and `20998-21018`; the row-local `2614-2621` fragment should be indexed, if at all, only as superseded diagnostic history [Germanic/docs/DEV_NOTES.md:10816-10902,20998-21018,2614-2621].
- If later philological cleanup revisits the old diagnostic `ētan`, verify first whether it was only a transient length/diacritic normalization artifact inside debug output. Nothing in the live TSV or current traces presently requires changing `COUNTERPART = etan` [Germanic/data/germanic-aligned-final.tsv:270-270; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1078-1097].
