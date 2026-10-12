---
row_id: 2035
concept: frost
counterpart: forst
proto: *frústą
protoform: *frústą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2035 frost / forst

## Current row state

- Live row `2035` currently keeps `CONCEPT = frost`, `COUNTERPART = forst`, `PROTO = *frústą`, `PROTOFORM = *frústą`, and `DERIVATION_CLASS = regular`. The row has no row-local note text in the TSV; its history field is only duplicated imported provenance (`Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh)`) [Germanic/data/germanic-aligned-final.tsv:407-407].
- `old_english_wiktionary.tsv` agrees with the live OE target and likewise records inherited-source provenance only: `frost	forst	inh	template:inh	frost` [Germanic/data/old_english_wiktionary.tsv:99-99].
- `oe_known_problems.tsv` has no surviving entry for row `2035`, `frost`, `forst`, or `*frústą`, so the row is not currently being tracked as a live OE exception or unresolved repair item there [Germanic/data/oe_known_problems.tsv:1-8].
- The coverage audit still treats this row as uncovered infrastructure-wise: `| 2035 | frost | forst | regular | no | - | - | - | none |`. That means there is no manifest-backed packet, research memo, or existing report stem to reuse, so the canonical row-based filename is appropriate here [Germanic/docs/lexeme_reports/coverage_audit.md:253-253; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- The current published OE derivation trace is an exact match. It shows `PROTO: *frústą`, `EXPECTED: forst`, `OUTPUTS: forst`, with the OE-side chain `NWGmc U Lowering: *fróstą` → `OE Heavy Syllable Nasal Apocope: *fróst` → `OE R Metathesis: *fórst` → `Outcome: forst` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1643-1662].

## Development-note summary

No frost-specific lexeme dossier presently survives in `DEV_NOTES.md`; the usable material is instead a cluster of shared `r`-metathesis notes plus one later diagnostic bug memo that explicitly keeps `*frústą → forst` as a regression check [Germanic/docs/DEV_NOTES.md:4839-4853,4979-5068,39972-40033]. This matters because the slice should not pretend there was ever a long row-local argument unique to `frost`. The support is real, but it is mostly **shared sound-change and implementation support**, not a dedicated row packet.

The most important philological point preserved in DEV_NOTES is that `forst` is not being treated as an arbitrary pipeline artifact. Campbell's quotation, as copied into DEV_NOTES, lists `*forst* 'frost'` among classic OE `r`-metathesis forms, but it immediately adds that many such words also occur "without metathesis," including `*frost*` [Germanic/docs/DEV_NOTES.md:4842-4853]. For this row, that means the project currently targets metathesized OE `forst`, yet the note history itself preserves awareness that non-metathesized `frost` also existed in the historical record. The slice therefore needs to keep a conservative distinction between the live project `COUNTERPART` and broader attestation variation.

The implementation-side summary is also specific enough to be worth preserving. DEV_NOTES identifies the productive environment as `r + short vowel + s`, gives `frost ← **frust*, *forst*` as an example in its conditioning summary, and then implements a deliberately restricted `OERMetathesis` rule for `*rVst` clusters with a worked table entry `*frustą | → | *forst | 'frost' ✓` [Germanic/docs/DEV_NOTES.md:4979-5023]. The same section closes by saying, "The gains are modest but correct: we now derive *berstan* and *forst* without regressions" [Germanic/docs/DEV_NOTES.md:5062-5068]. In other words, the row's present `regular` status depends on the current shared metathesis policy already doing exactly what it is meant to do.

The later `rust` bug memo sharpens that point rather than replacing it. When DEV_NOTES diagnosed erroneous word-initial metathesis in `*rústō → orst`, it explicitly named `*frústą → forst` as a TSV consumer that must continue to work because the form has "a consonant before the *r" and therefore still belongs in the real Campbell-style `CrVst` environment [Germanic/docs/DEV_NOTES.md:39993-40033]. That note is diagnostic rather than lexeme-specific, but it confirms that row `2035` is not merely tolerated by the grammar; it is one of the intended positive controls after the metathesis rule was narrowed.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-4839-4853

- Source label line: `DEV_NOTES:line-4839-4853`
- Source heading: `Primary sources` / `Campbell, Old English Grammar §459`
- Source line or section hint: `Campbell quotation on OE r-metathesis`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `r_metathesis`; `attestation_variation`; `forst_vs_frost`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1974`

This is the main inherited philological fragment for row `2035`, even though it is not a frost-only note. DEV_NOTES copies Campbell's statement that "The most frequent metathesis in OE is that of r from before to behind a short vowel followed by s or n," then gives `*forst* 'frost'` among the worked examples [Germanic/docs/DEV_NOTES.md:4842-4848]. For the live row, that directly supports why `COUNTERPART = forst` is a serious OE target and not a made-up normalization.

Just as important, the quotation preserves the caution that many such words also occur "without metathesis," and the list specifically includes `frost` [Germanic/docs/DEV_NOTES.md:4848-4850]. That prevents the replacement note from overstating certainty. The project's row now points to `forst`, but DEV_NOTES itself preserves evidence that the historical lexeme family is not reducible to a single invariant spelling tradition.

### DEV_NOTES:line-4979-5068

- Source label line: `DEV_NOTES:line-4979-5068`
- Source heading: `Phonological conditioning` / `FST implementation` / `Evaluation impact`
- Source line or section hint: `shared summary of productive r-metathesis and implemented rule`
- Fragment type: `shared_implementation_fragment`
- Status: `current`
- Issue tags: `shared_sound_change`; `fst_policy`; `positive_control`; `regular_output`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1974`

This fragment is the controlling project-policy note for the row. DEV_NOTES first summarizes the productive environment as `r + short V + s`, giving the frost example in schematic form: `frost ← **frust*, *forst*` [Germanic/docs/DEV_NOTES.md:4979-4985]. It then says the grammar implements a restricted rule targeting `*r + V + st` clusters, with the explicit positive table row `*frustą | → | *forst | 'frost' ✓` [Germanic/docs/DEV_NOTES.md:4999-5023]. The row is therefore supported twice inside the same note block: once as a historical conditioning example and once as a concrete FST acceptance case.

The tail of the fragment is equally useful because it records the project's own evaluation claim: after adding the restricted `OERMetathesis`, "we now derive *berstan* and *forst* without regressions" [Germanic/docs/DEV_NOTES.md:5062-5068]. For row `2035`, that is the nearest thing to a row-specific status statement that still survives in DEV_NOTES. It does not discuss manuscripts or paradigm cells, but it does explicitly say that `forst` is one of the intended successful outputs of the current shared rule.

### DEV_NOTES:line-39972-40033

- Source label line: `DEV_NOTES:line-39972-40033`
- Source heading: `§17.42 *rústō → orst (expected rust): word-initial *r escapes OERMetathesis`
- Source line or section hint: `bug memo restricting OERMetathesis to true CrVst environments`
- Fragment type: `diagnostic_regression_fragment`
- Status: `diagnostic_only`
- Issue tags: `metathesis_bugfix`; `left_context_restriction`; `regression_check`; `old_tsv_line_reference`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `1974`; `2162`

This later memo is not a frost dossier, but it materially helps explain the row's current stability. DEV_NOTES diagnosed a false metathesis in `*rústō → orst`, then re-read Campbell and emphasized that the real environment is `CrVsC → CVrsC`, i.e. the metathesizing `r` must have a consonant to its left in the same syllable [Germanic/docs/DEV_NOTES.md:39972-40012]. That clarification is directly relevant to `*frústą`, whose initial cluster `fr-` satisfies the intended environment.

The memo then lists the surviving TSV consumers of the corrected rule and explicitly includes `row 407 / 125: *frústą → forst   (f is consonant — still fires ✓)` [Germanic/docs/DEV_NOTES.md:40014-40023]. The `407 / 125` notation is diagnostic bookkeeping from an older grep-based TSV view rather than the current live row ID `2035`, but the linguistic point remains current: `forst` was deliberately preserved when word-initial false positives were removed. The probe list repeats the same expectation in imperative form: `*frústą → forst       (regression check, must still fire)` [Germanic/docs/DEV_NOTES.md:40025-40033].

## Superseded or diagnostic material

- No dedicated frost packet, research memo, or row-local DEV_NOTES rescue section was located for this pass. The row's support is mostly shared `r`-metathesis material plus the exact-match derivation trace, not a lexeme-specific dossier [Germanic/docs/lexeme_reports/coverage_audit.md:253-253; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1643-1662].
- The preserved contrast `forst` / `frost` in Campbell's quotation should be treated as attestation/variation context, not as evidence that the live row is presently mislabelled. DEV_NOTES uses the metathesized form as a positive example while also acknowledging non-metathesized comparators [Germanic/docs/DEV_NOTES.md:4842-4853].
- The `rust` note is diagnostic only. Its value for row `2035` is not that `frost` itself was broken, but that `*frústą → forst` was one of the regression probes used to keep the restricted metathesis rule honest [Germanic/docs/DEV_NOTES.md:39972-40033].
- Coverage infrastructure still marks the row as having no prior report coverage, which is workflow information rather than linguistic authority: `| 2035 | frost | forst | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:253-253].

## Open questions for later work

- If this row ever receives a full lexeme report, decide how explicitly to present the distinction between the live project target `forst` and DEV_NOTES' preserved evidence that `frost` also occurs without metathesis. The current slice should not collapse those into a false either/or [Germanic/docs/DEV_NOTES.md:4842-4853].
- If later OE reporting becomes dialect- or attestation-sensitive, check whether the row should remain centered on metathesized `forst` alone or whether the non-metathesized comparator deserves formal metadata somewhere else. Nothing in the current shared notes requires changing the live row now.
- If indexability is reviewed later, this row has genuine DEV_NOTES substance, but it is mainly shared-rule and regression-history material rather than a standalone frost dossier. Any later index entry should say that plainly.
