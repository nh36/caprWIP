---
row_id: 1996
concept: drench
counterpart: drenċ
proto: *dránkiz
protoform: *dránkiz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: "Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md; Germanic/docs/debug_snapshots/oe_full_trace_report.txt"
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1996 drench / drenċ

## Current row state

- The live OE row is `ID 1996`, `CONCEPT drench`, `COUNTERPART drenċ`, `PROTO *dránkiz`, `PROTOFORM *dránkiz`, `DERIVATION_CLASS regular` [Germanic/data/germanic-aligned-final.tsv:254-254].
- `PROTO` and `PROTOFORM` are identical in the live TSV. The row is not presently using an alternate OE-facing proxy form, an oblique paradigm cell, or a separate repair-stage input; the stored comparative input is `*dránkiz`, and the OE target is `drenċ` [Germanic/data/germanic-aligned-final.tsv:254-254].
- `oe_known_problems.tsv` has no surviving entry for row `1996`, for `drench`, for `drenċ`, or for `*dránkiz`, so the row is not currently being tracked as a live OE exception [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage and manifest infrastructure still treat the row as uncovered background documentation rather than as a packet-backed case: `coverage_audit.md` lists `| 1996 | drench | drenċ | regular | no | - | - | - | none |`, and `report_manifest.tsv` contains only the small pilot set, with no row `1996` entry [Germanic/docs/lexeme_reports/coverage_audit.md:227-227; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- The current published derivation is already an exact match. The compact report gives `PROTO: *dránkiz`, `EXPECTED: drenċ`, `OUTPUTS: drenċ`, with the visible chain `PGmc Final Z Deletion: *dránki`, `OE Velar Palatalization: *dránʧi`, `OE I Umlaut: *drenʧi`, `OE High Vowel Apocope: *drenʧ`, then orthographic `*drenċ` and surface `drenċ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:996-1016]. The full trace confirms the same ordering and also shows the orthographic branch cleanup `OldEnglishOrthography: *d*r*e*n*ċ, *d*r*e*nċ`, `OldEnglishRemoveStars: drenċ, dren*ċ`, `OldEnglishSurface: drenċ` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:6798-6845].

## Development-note summary

No securely row-specific DEV_NOTES dossier survives for the current row header `1996 drench / drenċ / *dránkiz`. That needs to be stated plainly. The attachable DEV_NOTES material is shared and partly historical: one older debugging cluster that mentions `*dranką` with expected `drenċ`, and one later handbook-digest passage that quotes Campbell on palatal consonants after umlaut, using the derivative verb `drenċan` as an example [Germanic/docs/DEV_NOTES.md:2588-2606,43224-43243]. Neither fragment is a row-local memo keyed to the live stored protoform `*dránkiz`, so this slice has to work conservatively as a replacement note rather than pretending that a dedicated `drench` section survives.

The live row itself is now simple and exact. In current traces the grammar derives `*dránkiz > *dránki > *dránʧi > *drenʧi > *drenʧ > drenċ`, with the crucial visible steps being final `*-z` loss, palatalization of `*k` before `*i`, i-umlaut of `a > e`, and high-vowel apocope [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1003-1016; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:6764-6810]. That matters because the surviving older DEV_NOTES diagnostic does **not** describe the row in this current form. It preserves a superseded debugging state in which `*dranką` was grouped with fronting/palatalization failures and yielded bad `drænca` instead of expected `drenċ` [Germanic/docs/DEV_NOTES.md:2593-2606]. Without a row-local memo bridging those stages, the safest reading is that DEV_NOTES is preserving project history about a nearby earlier analysis state, not authoritative live row metadata.

The most reusable shared philological substance is the Campbell quotation preserved in DEV_NOTES: “an umlauted vowel is followed by a palatal consonant, even if a back vowel followed, e.g. *fēġan, drenċan, streċċan, liċġan*” [Germanic/docs/DEV_NOTES.md:43241-43243]. That quotation remains useful, but only with care. It names `drenċan`, not this row's bare `drenċ`, so it should not be promoted into direct lexical proof for row `1996`. What it does support is the broader phonological class: DEV_NOTES explicitly records handbook support for palatal consonant outcomes in umlauted environments even when a back-vowel context might otherwise look hostile. For the present row, that is background support for the sound-change environment, not a substitute for a dedicated row memo.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2588-2606

- Source heading: `### OE palatalization vs fronting/umlaut split (2025-12-23)` and `### OE i-umlaut/fronting bucket diagnostics (2026-01-01)`
- Source line or section hint: `lines 2588-2606`
- Fragment type: `shared_diagnostic_fragment`
- Status: `diagnostic_only`
- Issue tags: `fronting_context`; `palatalization_bucket`; `nasal_block`; `protoform_drift`
- Recommended next use: `use only as project-history support, paired with the live exact-match trace`
- Shared with row IDs: `2244`

This is the only surviving DEV_NOTES material that explicitly names expected OE `drenċ` itself. The wording is revealing and needs to be preserved almost verbatim. First DEV_NOTES says the apparent “palatalization missing” bucket was really upstream-context trouble: “the 7 ‘palatalization missing’ cases are **not** palatalization-rule failures; palatalization never triggers because the **front-vowel context is missing**” [Germanic/docs/DEV_NOTES.md:2590-2593]. It then names `*dranką` among the forms to revisit:

> “prioritize fronting/breaking changes that create front‑vowel contexts (esp. for *bōkō, *θankăz, *dranką, *fleugăną, *xunăgą), then re‑check palatalization buckets.” [Germanic/docs/DEV_NOTES.md:2593-2593]

The next dated diagnostic keeps the same older shape and gives the most concrete bad-output record:

> “nasal‑block examples: *dranką → drænca (expected drenċ), *tangō → tængō (expected tange)” [Germanic/docs/DEV_NOTES.md:2606-2606]

For row `1996`, this fragment is important but not straightforwardly current. The live row does **not** store `*dranką`; it stores `*dránkiz` and currently derives `drenċ` exactly [Germanic/data/germanic-aligned-final.tsv:254-254; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:996-1016]. So the fragment should be used as evidence that the lexeme once sat inside a fronting/umlaut/palatalization diagnostic bucket, not as proof that `*dranką` remains the row's intended protoform. The conservative conclusion is that DEV_NOTES here preserves older debugging history for the same lexical area, while the live row has since moved to a different stored protoform and a resolved derivation.

### DEV_NOTES:line-43224-43243

- Source heading: `#### §17.50.4.1 The handbook consensus`
- Source line or section hint: `lines 43224-43243`
- Fragment type: `shared_handbook_context_for_lexeme`
- Status: `current`
- Issue tags: `campbell_palatalization`; `i_umlaut_override`; `shared_phonology`; `derivative_example`
- Recommended next use: `cite as shared sound-change background only`
- Shared with row IDs: `2226`

This later DEV_NOTES digest does not discuss row `1996` directly, but it preserves the best current handbook quotation relevant to the row's palatalized OE output. DEV_NOTES summarizes Campbell's discussion of medial palatalization and then preserves the line:

> “an umlauted vowel is followed by a palatal consonant, even if a back vowel followed, e.g. *fēġan, drenċan, streċċan, liċġan*.” [Germanic/docs/DEV_NOTES.md:43241-43243]

That quotation is worth keeping because it is more specific than a bare paraphrase: DEV_NOTES is not merely saying “Campbell allows palatalization here,” but preserving Campbell's own contrastive formulation and example list [Germanic/docs/DEV_NOTES.md:43229-43243]. For the present row, however, the example has to be handled cautiously. The cited form is `drenċan`, not `drenċ`, so the fragment does not by itself identify the row's exact counterpart or current stored protoform. Its real value is phonological and classificatory: it shows that the kind of OE palatal outcome seen in the live `drenċ` trace is not aberrant in handbook terms, even where a following back-vowel environment might otherwise tempt an over-narrow conditioning rule.

## Superseded or diagnostic material

- The older March 2026 full trace already produced the correct surface outcome, but under pre-stress-tier notation: `PROTO: *drankiz`, `EXPECTED: drenċ`, `OUTPUTS: drenċ` [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:2973-2976]. The derivational logic there is already essentially the same as now — palatalization, then umlaut, then apocope — so this older trace is useful as notation history, not as evidence for a different current lexical target [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:2978-3026; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:6798-6845].
- The more troubling older DEV_NOTES form is `*dranką`, not older plain `*drankiz`. Because no row-local memo survives to explain why DEV_NOTES once used `*dranką` while the live row now uses `*dránkiz`, that older string should be treated as diagnostic project history only. It is too risky to collapse `*dranką`, pre-stress-tier `*drankiz`, and live `*dránkiz` into one undifferentiated “same thing” label without a surviving row-specific argument [Germanic/docs/DEV_NOTES.md:2593-2606; Germanic/data/germanic-aligned-final.tsv:254-254; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:2973-2979].
- The row is currently exact and absent from the live OE problem register. That makes the older `drænca` diagnostic meaningful as superseded history rather than as an unresolved current failure [Germanic/docs/DEV_NOTES.md:2606-2606; Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:996-1016].

## Open questions for later work

- If a later packet or research memo is created, the first thing to resolve is the relation among three distinct strings now visible in the repo: live `*dránkiz`, older full-trace `*drankiz`, and older DEV_NOTES diagnostic `*dranką`. At present the safest documentation practice is to keep them distinct and to avoid claiming a single neat equivalence that the surviving notes do not actually prove [Germanic/data/germanic-aligned-final.tsv:254-254; Germanic/docs/DEV_NOTES.md:2593-2606; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:2973-2979].
- If later work wants stronger philological support, it should gather direct lexicographic evidence for bare OE `drenċ` rather than relying mainly on the DEV_NOTES-preserved Campbell quotation for `drenċan`. The present slice can document sound-change background and project history, but it cannot honestly convert the derivative example into row-specific lexical proof [Germanic/docs/DEV_NOTES.md:43241-43243].
- If an index proposal is made later, the row should probably stay conservative unless new row-local material appears. The present evidence is good enough for a replacement working note, but most of the surviving DEV_NOTES attachment is shared-policy or superseded diagnostic material rather than a dedicated `1996` analysis.
