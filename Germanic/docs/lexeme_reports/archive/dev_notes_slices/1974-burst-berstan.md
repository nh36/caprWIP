---
row_id: 1974
concept: burst
counterpart: berstan
proto: *bréstaną
protoform: *bréstaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1974 burst / berstan

## Current row state

- CONCEPT: `burst`
- COUNTERPART: `berstan`
- PROTO: `*bréstaną`
- PROTOFORM: `*bréstaną`
- DERIVATION_CLASS: `regular`
- Live TSV row `1974` keeps a fully regular setup: `PROTOFORM = *bréstaną`, `COUNTERPART = berstan`, `DERIVATION_CLASS = regular`; the `NOTE` column is blank, and `HISTORY` contains only duplicated Wiktionary etymology placeholders rather than a row-local explanation [Germanic/data/germanic-aligned-final.tsv:167-167].
- Coverage audit still lists row `1974` as uncovered, with no packet, no research memo, no attached fragment, and status `none` [Germanic/docs/lexeme_reports/coverage_audit.md:214-214].
- A matching shared-analysis file does exist: the West Saxon vs. Anglian dialect note quotes Campbell §155 with `berstan` among the forms where metathesis was too late to trigger breaking, i.e. the row belongs to the late-metathesis/no-breaking set rather than the Anglian `beornan/eornan` type [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:272-284].
- The current published derivation trace is exact-match regular. It shows `PROTO: *bréstaną`, `EXPECTED: berstan`, `OUTPUTS: berstan`, and the OE-side path includes `OE R Metathesis: *bérstan` before final `Outcome: berstan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:631-650].

## Development-note summary

DEV_NOTES support for row `1974` is real but mostly **shared-rule** support rather than a dedicated lexeme dossier. The important thing to preserve is that `berstan` is not an incidental example mentioned once in passing: the row sits inside the project's main discussion of OE `r`-metathesis chronology, and it is also reused later as an implementation checkpoint when the metathesis rule is restricted and debugged [Germanic/docs/DEV_NOTES.md:4839-4853,4880-5068,39993-40033].

The philological substance is consistent across the note cluster. Campbell's material, as copied into DEV_NOTES, first places `berstan` among the classic short-vowel-plus-`r` words affected by metathesis, but it also preserves lexical variation: “there are scattered forms of *beornan, berstan, perscan* without metathesis” [Germanic/docs/DEV_NOTES.md:4842-4853]. That matters because the replacement note should not oversimplify the lexeme into a claim that OE had only one invariant surface tradition. DEV_NOTES is preserving the existence of non-metathesized comparators, not asking the live row to adopt them.

The chronology discussion is the controlling current interpretation. DEV_NOTES quotes Campbell §155 that metathesis of `r` “usually took place too late for secondary r-groups to cause breaking, e.g. *gers* 'grass', *berst* 'he burst', *berstan* 'burst'” [Germanic/docs/DEV_NOTES.md:4880-4886]. Ringe-Taylor and Luick are then used to sharpen the dialect point: Anglian `burn/run` forms could metathesize early enough for breaking, but West Saxon forms like `berstan` belong to the opposite side of the chronology, where metathesis is late and breaking therefore does **not** arise [Germanic/docs/DEV_NOTES.md:4900-4958]. DEV_NOTES makes this explicit in its own summary sentence: “Metathesis in *grass, burst, thresh, fresh* was universally late (post-breaking)” [Germanic/docs/DEV_NOTES.md:4967-4975]. For row `1974`, that is the core explanatory content: `PROTO` and `PROTOFORM` remain `*bréstaną`; the OE target is regular late-WS-style `berstan`; and no broken `**beorstan` outcome is expected under the current project model.

The implementation side of DEV_NOTES is also materially relevant and should be kept. The note says the live grammar deliberately implements a restricted `OERMetathesis` rule for `*r + V + st` clusters, gives `*brestanan -> berstan` as the worked positive case, and reports that “we now derive *berstan* and *forst* without regressions” [Germanic/docs/DEV_NOTES.md:4999-5068]. A later diagnostic note, written while fixing erroneous word-initial metathesis in `rust`, keeps `*brestaną -> berstan` as a regression probe and explains why it must continue to work: unlike `rust`, it has the required consonant before the metathesizing `r` [Germanic/docs/DEV_NOTES.md:39993-40033]. So even though row `1974` is not a current mismatch, it is still a live control item in the project's metathesis chronology and implementation history.

## Relevant DEV_NOTES fragments

### `Germanic/docs/DEV_NOTES.md:4839-4853`

- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `r_metathesis`; `lexical_variation`; `attestation_context`
- Recommended next use: `cite_in_final_report`

This is the earliest materially relevant fragment because it names `berstan` directly inside the main Campbell quotation on OE `r`-metathesis. DEV_NOTES copies the rule scope—metathesis of `r` from before to behind a short vowel followed by `s` or `n`—and then preserves the caution that “there are scattered forms of *beornan, berstan, perscan* without metathesis” [Germanic/docs/DEV_NOTES.md:4842-4853]. For row `1974`, the value of the fragment is twofold: it supports metathesis as the ordinary pathway to `berstan`, and it also preserves non-metathesized comparators as documentary background rather than as grounds for rewriting the live row.

### `Germanic/docs/DEV_NOTES.md:4880-4975`

- Fragment type: `shared_chronology_fragment`
- Status: `current`
- Issue tags: `r_metathesis`; `breaking`; `dialect_variation`; `late_ws_output`
- Recommended next use: `cite_in_final_report`

This is the controlling shared chronology fragment. DEV_NOTES quotes Campbell that metathesis was “too late for secondary r-groups to cause breaking” in forms such as `*berst*` and `*berstan*` [Germanic/docs/DEV_NOTES.md:4880-4886]. It then quotes Ringe-Taylor on the contrasting `burn/run` evidence and Luick on the same chronology in German, ending with the project's own distilled conclusion that metathesis in “*grass, burst, thresh, fresh* was universally late (post-breaking)” [Germanic/docs/DEV_NOTES.md:4900-4958,4967-4975]. For this row, the fragment explains exactly why `berstan` is compatible with regular OE development while a broken outcome is not part of current row policy.

### `Germanic/docs/DEV_NOTES.md:4999-5068`

- Fragment type: `shared_implementation_fragment`
- Status: `current`
- Issue tags: `fst_policy`; `metathesis_rule`; `positive_control`; `regular_output`
- Recommended next use: `cite_in_final_report`

This fragment turns the historical discussion into live grammar policy. DEV_NOTES says the implemented `OERMetathesis` rule is intentionally restricted to `*rVst` clusters and illustrates the intended behavior with the table row `*brestanan -> berstan` [Germanic/docs/DEV_NOTES.md:4999-5029]. It then states the scope limits—single standard late-WS output, no generalized dialect modeling—and closes the section with the evaluation result that “we now derive *berstan* and *forst* without regressions” [Germanic/docs/DEV_NOTES.md:5031-5068]. For row `1974`, this is the direct project-level reason the live row can remain an unremarkable `regular` item.

### `Germanic/docs/DEV_NOTES.md:39993-40033`

- Fragment type: `diagnostic_regression_fragment`
- Status: `diagnostic_only`
- Issue tags: `metathesis_bugfix`; `rule_restriction`; `regression_check`
- Recommended next use: `use_as_project_history_only`

This later note is not a row-specific explanation of `berstan`, but it is still worth preserving because it shows that row `1974` functioned as a regression sentinel during a real bugfix. DEV_NOTES restates Campbell's metathesis environment, emphasizes that the worked examples `*brestaną -> berstan` and `*frustą -> forst` both have “a **consonant before the metathesizing *r**,” and therefore says row `1974` will keep firing when the rule is restricted away from bad word-initial cases like `rust` [Germanic/docs/DEV_NOTES.md:39993-40033]. This is diagnostic history only, but it confirms that the current exact-match row is an intentionally preserved consumer of the restricted metathesis rule.

## Superseded or diagnostic material

- No dedicated row-local rescue note, packet, or research memo was located for `1974`; the row's evidentiary base is the shared DEV_NOTES metathesis dossier plus exact-match trace support, not a mismatch-specific investigation [Germanic/docs/lexeme_reports/coverage_audit.md:214-214; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:631-650].
- The clause about “scattered forms of *... berstan ...* without metathesis” should be treated as preserved lexical/dialectal variation, not as a superseding instruction to replace live `berstan` with an un-metathesized form [Germanic/docs/DEV_NOTES.md:4849-4853].
- The late `rust` bug note is diagnostic only. Its relevance here is not that `berstan` was ever problematic, but that `berstan` remained one of the forms that **should still** be generated after `OERMetathesis` was narrowed to true `CrVst` environments [Germanic/docs/DEV_NOTES.md:39993-40033].

## Open questions for later work

- If later reporting wants to discuss attested variation around this lexeme, decide whether the row should stay centered on regular late-WS `berstan` alone or whether the non-metathesized comparators preserved in DEV_NOTES deserve a separate source-audit note [Germanic/docs/DEV_NOTES.md:4842-4853].
- If the project ever introduces dialect-specific OE outputs, keep `berstan` separate from the Anglian early-metathesis/breaking cases: DEV_NOTES treats `burst` with `grass/thresh/fresh` as a late-metathesis set, not as part of the `beornan/eornan` pattern [Germanic/docs/DEV_NOTES.md:4880-4975].
- If `Germanic/docs/lexeme_reports/dev_notes_slices/index.tsv` is reviewed later, this row now has enough explicit DEV_NOTES substance to be arguable for indexing, but the material is still mostly shared-rule and regression-history evidence rather than a standalone lexeme dossier.
