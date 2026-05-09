---
row_id: 2031
concept: fox
counterpart: fox
proto: *fúxsaz
protoform: *fúxsaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md]
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2031 fox / fox

## Current row state

- The live OE row is currently an exact regular match: `CONCEPT = fox`, `COUNTERPART = fox`, `PROTO = *fúxsaz`, `PROTOFORM = *fúxsaz`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:392-392].
- `PROTO` and `PROTOFORM` are identical in the TSV, so the row is **not** presently using a substitute OE-directed stem, an analogical repair input, or a separate paradigm-cell workaround; the project is deriving OE `fox` directly from the same project-normalized protoform it cites comparatively [Germanic/data/germanic-aligned-final.tsv:392-392].
- The current published derivation trace already reaches the target exactly and without exception handling: `PROTO: *fúxsaz`, `EXPECTED: fox`, `OUTPUTS: fox`, with the explicit stages `NWGmc U Lowering: *fóxsaz`, `PGmc Final Z Deletion: *fóxsa`, `PWGmc Final Bare A Loss: *fóxs`, `OE Xs Merge: *fóXS`, and surface `Outcome: fox` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1583-1602].
- `oe_known_problems.tsv` has no row-specific entry for row `2031`, for `fox`, or for `*fúxsaz`; the current tracked exception/wontfix list covers other lexemes only [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage/report infrastructure is likewise sparse for this row. `coverage_audit.md` marks row `2031` as `regular` with `NOTE? no`, no packet, no research memo, no dossier, and requirement basis `none`, while `report_manifest.tsv` currently lists only pilot rows and contains no entry for `2031` [Germanic/docs/lexeme_reports/coverage_audit.md:250-250; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- The TSV note/source field for the OE row preserves only duplicated inherited-source placeholders (`Source: Wiktionary etymology (template:inh)` twice), not a row-local derivational explanation. The replacement slice therefore has to lean on shared DEV_NOTES material plus the current trace, and should say that plainly rather than pretending a dedicated fox dossier survives [Germanic/data/germanic-aligned-final.tsv:392-392].

## Development-note summary

No dedicated row-specific DEV_NOTES dossier for `fox / fox` survives. The secure current DEV_NOTES material is instead a **shared guardrail** from the later `*x`-loss audit: row `2031 *fúxsaz → fox` is listed under the medial `*xs` cohort, and that cohort is described as “mostly preserved as `x` orthographically, no loss” [Germanic/docs/DEV_NOTES.md:39265-39270]. DEV_NOTES then states the project policy in the sentence that matters most for this row: “These do not require the loss rule. Per Campbell §416, `*xs` survives as `x` (= ks) when no further consonant follows; the loss rule should not fire here” [Germanic/docs/DEV_NOTES.md:39273-39276].

That means the surviving DEV_NOTES support for row `2031` is mainly **negative but still substantial**. The row is not being defended as a special exception; rather, it is being protected from over-application of a different sound change. The relevant comparison is with `*xs + C` material such as `wæstm`, `sesta 'sixth'`, and `niuhsjan`-type forms, because the long shared dossier in §17.40 repeatedly defines the deletion environment with those preconsonantal examples and explicitly warns that the literature does **not** justify treating the rule as “any `*x` before any CC” [Germanic/docs/DEV_NOTES.md:39027-39043,39096-39102]. For `fox`, whose relevant cluster is plain medial `*xs` with no further consonant after it by the time the crucial conditioning is assessed, that shared background supports preservation rather than deletion [Germanic/docs/DEV_NOTES.md:39273-39276].

The current derivation trace fits that interpretation closely. The row does undergo NWGmc `u`-lowering (`*fúxsaz > *fóxsaz`) and later final-vowel reductions, but nothing in the current trace or surviving DEV_NOTES suggests a row-local repair, exception tag, or alternate protoform [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1592-1602; Germanic/data/germanic-aligned-final.tsv:392-392]. The consonant side is the more important note-prep issue: the row's `x` is the expected orthographic continuation of `*xs`, not something awaiting deletion by the preconsonantal `*x`-loss rule [Germanic/docs/DEV_NOTES.md:39265-39276].

The conservative working conclusion is therefore narrow. Row `2031` is presently a stable regular row, but the support preserved in DEV_NOTES is mostly **shared phenomenon-level support** rather than a fox-specific research memo. The slice should preserve that limitation explicitly: current evidence says that `*fúxsaz > fox` is treated as a regular `*xs` survivor in the project, and it does **not** preserve a separate row-history narrative of mismatch, repair, or philological controversy [Germanic/docs/DEV_NOTES.md:39260-39276; Germanic/docs/lexeme_reports/coverage_audit.md:250-250].

## Relevant DEV_NOTES fragments

No securely attachable dedicated fox-only DEV_NOTES packet survives. The fragments below are the best replacement material because they either name the row directly or preserve the shared conditioning that explains why row `2031` stays regular.

### DEV_NOTES:line-39260-39276

- Source label line: `DEV_NOTES.md lines 39260-39276`
- Source heading: `#### 6. Corpus rows that depend on the current loss rule`
- Source line or section hint: `lines 39260-39276`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `xs_preservation`; `no_x_loss`; `regular_row`; `guardrail`
- Recommended next use: `cite_if_explaining_why_fox_is_not_an_x_loss_case`
- Shared with row IDs: `2017`; `2146`; `2194`; `2275`; `2276`

This is the strongest surviving row-explicit DEV_NOTES fragment. DEV_NOTES names row `2031` directly in the `*xs` bucket: `- 2031 *fúxsaz → fox` [Germanic/docs/DEV_NOTES.md:39265-39268]. It immediately glosses the whole subgroup as “mostly preserved as `x` orthographically, no loss” [Germanic/docs/DEV_NOTES.md:39265-39270]. The follow-up sentence is the operative row policy and should be preserved verbatim because it is more specific than a casual paraphrase: “These do not require the loss rule. Per Campbell §416, `*xs` survives as `x` (= ks) when no further consonant follows; the loss rule should not fire here” [Germanic/docs/DEV_NOTES.md:39273-39276].

For row `2031`, this fragment does nearly all of the surviving DEV_NOTES explanatory work. It does **not** give a full fox dossier, but it does make clear that the row belongs with ordinary `*xs` survivors rather than with `*xs + C` loss cases. That is exactly the distinction a later report will need if someone asks why the row keeps `x` while nearby literature examples talk about `xs > s` [Germanic/docs/DEV_NOTES.md:39265-39276].

### DEV_NOTES:line-39023-39102

- Source label line: `DEV_NOTES.md lines 39023-39102`
- Source heading: `### §17.40 research dossier — *x preconsonantal loss vs. j-gemination`
- Source line or section hint: `lines 39023-39102`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `xs_plus_c`; `conditioning`; `shared_background`; `do_not_overgeneralize`
- Recommended next use: `cite_as_shared_philological_background_only`
- Shared with row IDs: `2010`; `2086`; `2092`; `2102`; `2140`; `2194`; `2242`; `2291`

This longer dossier is not fox-specific, but it preserves the philological boundary conditions that make the row-explicit fragment intelligible. DEV_NOTES opens the section by insisting that the handbooks describe the rule narrowly: “The conditioning is **not** ‘any `*x` before any CC’”; instead the canonical cases are the sibilant cluster environment where `*x` is followed by `*s` and then by another consonant [Germanic/docs/DEV_NOTES.md:39027-39031]. It then quotes Campbell §417: “When a consonant follows, `xs > s` in OE, e.g. `wæstm` fruit ... North. `sesta` sixth ... `þixl` axle beside `þisl` ...” [Germanic/docs/DEV_NOTES.md:39033-39043]. Brunner §221 is quoted in similar terms: “Wenn auf `hs` andere Konsonanten (auch `j`) folgen, ist `h` ausgefallen ... nordh. `sesta`, `seista` ...” [Germanic/docs/DEV_NOTES.md:39058-39070].

The most useful sentence for row `2031` is the dossier synopsis: “all four primary handbooks describe the change with examples drawn exclusively from clusters whose first member is `*x` and whose second member is `*s` (i.e. `*xs + C`, including `*xsj` in `*niuhsjan`)” [Germanic/docs/DEV_NOTES.md:39096-39102]. For `fox`, the value of this fragment is negative delimitation. It shows that the big shared `*x`-loss discussion is about **preconsonantal** `*xsC` environments, not about ordinary medial `*xs` items like `*fúxsaz` that end up simply preserving `x` in the orthography [Germanic/docs/DEV_NOTES.md:39096-39102; Germanic/docs/DEV_NOTES.md:39273-39276].

### DEV_NOTES:line-39202-39221

- Source label line: `DEV_NOTES.md lines 39202-39221`
- Source heading: `##### Option (a) — restrict the loss rule to *xs (or, more generally, to non-*x first member)`
- Source line or section hint: `lines 39202-39221`
- Fragment type: `implementation_guardrail`
- Status: `current`
- Issue tags: `rule_scope`; `safe_for_current_corpus`; `xs_only`; `future_regression_guard`
- Recommended next use: `cite_if_rule_scope_is_reopened`
- Shared with row IDs: `2017`; `2031`; `2146`; `2194`; `2275`; `2276`

This fragment is broader than row `2031`, but it is worth preserving because it records the current implementation judgment in corpus-aware form. DEV_NOTES proposes tightening the loss rule to canonical `*xs` contexts and then states, crucially, that “None of the current TSV rows require non-`*xs` `*x`-loss, so both narrowings are safe for the current corpus” [Germanic/docs/DEV_NOTES.md:39202-39221]. In context, row `2031` is one of the rows named immediately afterward in the preserved `*xs` bucket [Germanic/docs/DEV_NOTES.md:39260-39276].

For this slice, the value is not that `fox` itself triggered the proposal; it did not. The value is that the proposal's safety statement helps explain why `fox` can be treated conservatively as an unaffected control row when the `*x`-loss rule is revised. If later work reopens rule scoping, this fragment should be cited alongside the row-explicit inventory so that `fox` is not accidentally swept into a broader deletion environment than the current DEV_NOTES actually supports [Germanic/docs/DEV_NOTES.md:39202-39221,39260-39276].

## Superseded or diagnostic material

There is no securely recoverable fox-specific superseded mismatch dossier in current DEV_NOTES. Unlike rows such as `fire`, `fowl`, or `tap`, row `2031` does not preserve a current exception note, a repaired alternative `PROTOFORM`, or a long problem narrative in either `oe_known_problems.tsv` or coverage/report infrastructure [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/coverage_audit.md:250-250; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].

The main diagnostic risk is therefore interpretive rather than textual. Because `fox` is named inside the corpus audit for the `*x`-loss discussion, a later reader could mistake it for a row that once wanted `x` deleted. The surviving DEV_NOTES evidence says the opposite: row `2031` is included in that audit specifically as a form where `*xs` is preserved and where “the loss rule should not fire” [Germanic/docs/DEV_NOTES.md:39265-39276].

The duplicated inherited-source placeholders in the TSV row are likewise diagnostic only. They record intake provenance, not a row-level philological argument, and they should not be treated as a substitute for the shared but real DEV_NOTES substance collected here [Germanic/data/germanic-aligned-final.tsv:392-392].

## Open questions for later work

- If a later packet is written for this row, add direct lexicographic/literature support for attested OE `fox`; the present slice is strong on current project rule scope, but it is still mainly a replacement for missing row-specific DEV_NOTES rather than a full literature dossier [Germanic/docs/lexeme_reports/coverage_audit.md:250-250; Germanic/docs/DEV_NOTES.md:39260-39276].
- If `NWGmcPreconsonantalXLoss` or related `*x`-loss logic is revised again, re-check that row `2031` remains in the preserved `*xs` bucket and still derives by ordinary `*xs > x` orthographic continuation rather than by deletion [Germanic/docs/DEV_NOTES.md:39202-39221,39260-39276; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1592-1602].
- If future reporting wants a fuller historical note on the vowel side, confirm whether the current trace's `NWGmc U Lowering: *fóxsaz` needs any lexeme-specific comment or can remain implicit as an unproblematic regular step; current DEV_NOTES material does not single out `fox` as a u-lowering problem row [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1592-1597; Germanic/data/oe_known_problems.tsv:1-8].
