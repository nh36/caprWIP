---
row_id: 2052
concept: hall
counterpart: heall
proto: *xállō
protoform: *xállō
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: null
linked_research_memo_file: null
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2052 hall / heall

## Current row state

- CONCEPT: `hall`
- COUNTERPART: `heall`
- PROTO: `*xállō`
- PROTOFORM: `*xállō`
- DERIVATION_CLASS: `regular`
- Live TSV row `2052` is stable and already matches: `hall` / `heall`, with both `PROTO` and `PROTOFORM` carried as `*xállō`. For this row the two proto columns presently coincide; there is no live evidence here for the kind of `PROTO` vs `PROTOFORM` split seen in analogy-driven rows [Germanic/data/germanic-aligned-final.tsv:472-474].
- Current derivation snapshot is fully successful: `PROTO: *xállō`, `EXPECTED: heall`, `OUTPUTS: heall`, with the compact stage chain `NWGmc Final Long O Raising: *xállu`, `Anglo Frisian Brightening: *xællu`, `OE Breaking: *xeallu`, `OE Velar Fricative Palatalization: *çeallu`, `OE High Vowel Apocope: *çeall`, then orthographic `h*eall` and surface `heall` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md:2177-2197].
- `oe_known_problems.tsv` has no entry for row `2052`, `*xállō`, or `heall`; the file's current problem list is limited to unrelated known exceptions such as `*búkkaz`, `*fūri`, and `*táppô` [Germanic/data/oe_known_problems.tsv:1-8].
- `coverage_audit.md` classifies row `2052` as `regular` with `no` outstanding coverage issue and `none` under notes, which is consistent with the successful live trace and with the absence of any row-local rescue memo [Germanic/docs/lexeme_reports/coverage_audit.md:262-264].
- `report_manifest.tsv` still contains only the earlier pilot subset and has no row `2052` entry, so this slice has to carry the detailed replacement note itself rather than pointing to a completed packet/report workflow [Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- The only row-adjacent non-DEV_NOTES background found in the checked analysis layer is the A-restoration inventory line `| 2052 | *xállō | heall | geminate *ll* + breaking |`; this is useful as class-level phonological grouping, not as an independent row-specific argument [Germanic/docs/analysis/arestoration_r_l_research.md:722-734].

## Development-note summary

No dedicated row-specific DEV_NOTES block survives for `2052 hall / heall`. That needs to be stated plainly. The attachable DEV_NOTES material consists only of shared implementation and audit mentions where `*xállō → heall` is used as an exact positive example inside broader discussions of short-diphthong weight, high-vowel apocope, and later A-restoration scoping [Germanic/docs/DEV_NOTES.md:29428-29435; Germanic/docs/DEV_NOTES.md:29457-29475; Germanic/docs/DEV_NOTES.md:30610-30623].

Those shared fragments are nevertheless enough to reconstruct the working note conservatively because the live derivation trace still matches them step for step. The row is not being preserved as an exception, analogical repair, or unresolved mismatch. The current implementation story is: PGmc `*xállō` raises final long `ō` to `u` in NWGmc, undergoes Anglo-Frisian brightening, then OE breaking before geminate `ll`, and finally loses the final high vowel because the broken form counts as a heavy `ShortDiphthong + C + C+` shape [Germanic/docs/DEV_NOTES.md:29431-29435; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md:2184-2197].

The main caution for later use is evidential, not phonological. Because DEV_NOTES does not preserve a hall-specific discussion block, later writing should label the surviving evidence correctly: current support is mostly **shared-background-only** rather than row-specific. The one row-numbered DEV_NOTES mention (`2052 | *xállō | heall | geminate *ll* |`) is still only an audit-table line, not a standalone lexeme dossier [Germanic/docs/DEV_NOTES.md:30622-30622]. No primary-source quotation embedded in DEV_NOTES survives specifically for this row, so the replacement slice should not pretend otherwise.

## Relevant DEV_NOTES fragments

### DEV_NOTES:29428-29435

- Source heading: `OEHighVowelApocope diphthong clauses refactored along weight lines`
- Source line hint: `Germanic/docs/DEV_NOTES.md:29428-29435`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `breaking`; `high_vowel_apocope`; `short_diphthong_weight`; `geminate_ll`
- Recommended next use: `cite as the controlling implementation rule for why heall is consonant-final`
- Shared-with rows if relevant: `2057`; `2068`; `2120`; also other breaking rows with heavy post-diphthong codas

This is the most important surviving DEV_NOTES material for the row, even though it is not a dedicated hall note. DEV_NOTES states the rule in exactly the form later writers need: `ShortDiphthong + C + C+ (2+ C) -> heavy -> apocopate`, with the explicit example string `*xérdō → heord, *márkō → mearc, *xállō → heall` [Germanic/docs/DEV_NOTES.md:29431-29435]. For row `2052`, the substance is that the relevant apocope decision is made **after** breaking has created a short diphthong: the live trace's `*xeallu` / `*çeallu` stage is not light, because geminate `ll` supplies the `C + C+` environment that puts the form on the heavy side of the split [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md:2190-2197].

This should therefore be treated as current implementation authority, but not as row-specific philological argument. It explains the mechanics of the successful surface form `heall`; it does **not** independently establish the lexical reconstruction or provide any special exception-handling rationale. Its evidential status is shared-background-only, strengthened by the fact that the current audit trace still lands exactly on `heall` under the same rule ordering [Germanic/docs/DEV_NOTES.md:29431-29435; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md:2177-2197].

### DEV_NOTES:29457-29475

- Source heading: `Verification probes; regressions that self-resolved`
- Source line hint: `Germanic/docs/DEV_NOTES.md:29457-29475`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `verification`; `regression_history`; `geminate_ll`; `apocope_fix`
- Recommended next use: `cite when documenting that heall is a checked success case, not merely an inferred consequence`
- Shared-with rows if relevant: `2057`; `2068`; `2120`; `2006`

This fragment preserves the row as an explicit verification target. DEV_NOTES' probe table includes the exact line `| *xállō | heall | heall | HEAVY (ll geminate) |`, and the follow-up note says that `heall` was among the `Regressions that self-resolved` once the short-diphthong-plus-cluster and `-u-after-h` clauses were in place [Germanic/docs/DEV_NOTES.md:29459-29475]. The value of that wording is practical: it records that `heall` was not only predicted by the rule schema above but also actively checked during the refactor.

For later workflow, this is the best surviving statement about row status inside DEV_NOTES itself. It shows a small but important chronology: older apocope work had exposed `heall` as a failure case, but by the time of this DEV_NOTES section it had been promoted into the verified-success column. That history matches the older diagnostic notes that once had `*xallō → heallō` and the current live audit trace that now has `Outcome: heall` [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:23-30; Germanic/docs/germanic_notes/heavy_syllable_apocope_experiment_results.md:49-55; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md:2194-2197].

### DEV_NOTES:30622

- Source heading: `later audit table for A-restoration scope / row grouping`
- Source line hint: `Germanic/docs/DEV_NOTES.md:30622`
- Fragment type: `diagnostic_background`
- Status: `current_background`
- Issue tags: `a_restoration_scope`; `geminate_ll`; `negative_evidence`; `row_grouping`
- Recommended next use: `keep only as scoping evidence; do not elevate into a standalone hall dossier`
- Shared-with rows if relevant: `1935`; `2002`; `2037`; `2077`

The row-numbered DEV_NOTES mention is useful, but only narrowly. The table line `| 2052 | *xállō | heall | geminate *ll* |` shows that later audit work continued to classify the row under the geminate-`ll` / breaking umbrella rather than reopening it as an A-restoration problem [Germanic/docs/DEV_NOTES.md:30622-30622]. Read together with the parallel analysis table line `| 2052 | *xállō | heall | geminate *ll* + breaking |`, the point is negative but still valuable: this row is part of the class inventory that helps define what the later audit was **not** trying to fix [Germanic/docs/analysis/arestoration_r_l_research.md:722-734].

Because the fragment is only a one-line table entry, its status should remain diagnostic/background rather than row-specific authority. It can help later writers explain why hall is grouped with other broken `a + l/r` rows, but it does not add new derivational substance beyond what the shared apocope/verification section already says.

## Superseded or diagnostic material

No superseded hall-specific DEV_NOTES block has been found. The older material that actually preserves a row-shaped failure history for this lexeme sits outside DEV_NOTES in pre-refactor diagnostic notes, and it should be labelled exactly that way.

- `final_vowel_apocope_investigation.md` preserves the earlier failure state twice: once in the general pattern sketch `*xallō -> heallō (expected heall)` and again in the proto `*-ō` case list [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:23-30; Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:304-314].
- `heavy_syllable_apocope_experiment_results.md` repeats the same pre-fix diagnosis under `Remaining final_vowel_extra (19 cases)`, again listing `*xallō -> heallō (expected heall)` [Germanic/docs/germanic_notes/heavy_syllable_apocope_experiment_results.md:49-55].

These notes are useful only as superseded diagnostics showing what the later DEV_NOTES refactor repaired. They should not be treated as current row authority, because current DEV_NOTES and the live derivation snapshot both supersede them with successful `heall` output [Germanic/docs/DEV_NOTES.md:29457-29475; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md:2177-2197].

## Open questions for later work

- If a full packet/research-memo workflow is later created for row `2052`, preserve the evidential label explicitly: current support is mostly shared implementation material plus the live derivation trace, not a dedicated hall-specific DEV_NOTES dossier.
- Decide whether a later row packet should cite the broader geminate-`ll` comparison set (`beall`, `feallan`, `ġealla`) as shared background, while keeping clear that row `2052` itself is presently `regular` and not an analogy case [Germanic/docs/analysis/arestoration_r_l_research.md:726-733].
- If future literature pass-through is desired, add external lexicographic support for the OE noun class and meaning; no literature-agent escalation is needed now because the row already matches and no surviving DEV_NOTES dispute attaches specifically to `heall` [Germanic/docs/lexeme_reports/coverage_audit.md:263-263; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md:2177-2197].
