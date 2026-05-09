---
row_id: 2026
concept: folk
counterpart: folc
proto: *fúlką
protoform: *fúlką
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2026 folk / folc

## Current row state

- The live OE row is currently `ID 2026`, `CONCEPT folk`, `COUNTERPART folc`, `PROTO *fúlką`, `PROTOFORM *fúlką`, `DERIVATION_CLASS regular`; there is no separate OE-facing rescue stem in the TSV for this row [Germanic/data/germanic-aligned-final.tsv:370-372].
- The coverage audit still marks row 2026 as having no packet, no research memo, and no prior slice-derived coverage item, so this file is replacing absent row-local DEV_NOTES support rather than condensing an existing packet [Germanic/docs/lexeme_reports/coverage_audit.md:248-248].
- `oe_known_problems.tsv` currently contains no entry for `*fúlką`, `folk`, or `folc`; the known-problems table only lists unrelated exception rows, which is consistent with row 2026 being treated as regular rather than as an accepted mismatch bucket [Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation trace is an exact match: `PROTO: *fúlką`, `EXPECTED: folc`, `OUTPUTS: folc`, with the pathway `NWGmc U Lowering: *fólką` and then `OE Heavy Syllable Nasal Apocope: *fólk`, surfacing as `folc` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1523-1542].
- No row-specific packet, research memo, or surviving DEV_NOTES subsection for row 2026 was found during preparation. The row therefore has to be documented from shared DEV_NOTES material, and that surviving shared material is mainly important because it names `folc` as a **counterexample** to proposed labial-conditioned `u`-preservation, not because row 2026 itself is unstable [Germanic/docs/DEV_NOTES.md:82-86,136-142].

## Development-note summary

No row-specific DEV_NOTES discussion for `folk / folc` appears to survive. What does survive is still useful, but in an inverse way: `folc` is repeatedly cited inside the shared NWGmc `*u > *o` discussion as evidence **against** turning labial adjacency into a categorical blocker. Bülbring's survey, as preserved in DEV_NOTES, says OE `u` may appear “namentlich zwischen Labial und langem oder gedecktem l”, but immediately concedes that “meist steht jedoch der Hauptregel gemäß o”, explicitly citing `folc` among the counterexamples [Germanic/docs/DEV_NOTES.md:82-82]. Luick is then quoted rejecting a categorical phonological explanation and listing `folc` again beside `wolcen`, `folġian`, `folde`, and `bolt` as forms with regular lowering despite similar consonantal surroundings [Germanic/docs/DEV_NOTES.md:84-84].

For row 2026, that means the current exact-match derivation is not a silent accident. The live trace's `*fúlką > *fólką > folc` is exactly the kind of regular lowering outcome that DEV_NOTES uses to keep neighboring `u`-retention rows exceptional [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1530-1542; Germanic/docs/DEV_NOTES.md:136-142]. The distinction among fields should stay explicit: `PROTO`/`PROTOFORM` are both reconstructed `*fúlką`, while `COUNTERPART folc` is the attested OE outcome represented in the TSV; nothing in the surviving notes suggests replacing the proto input, invoking a different paradigm cell, or treating `folc` as philologically dubious within this row's present documentation state [Germanic/data/germanic-aligned-final.tsv:370-372].

The most conservative row-level conclusion is therefore narrow. Row 2026 currently stands as a regular, matched OE reflex and as shared comparative evidence that any proposed “labial environment” preservation tendency was at best statistical and not a usable sound law. DEV_NOTES itself later makes that point explicitly: whatever phonetic clustering might exist, “the counterexamples (`folc`, `bolla`, etc.) preclude formalizing it” [Germanic/docs/DEV_NOTES.md:138-142].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-63-86

- Source label line: `DEV_NOTES shared exception survey`
- Source heading: `NWGmc u-lowering Exceptions Near Labials`
- Source line or section hint: `lines 63-86`
- Fragment type: `shared_comparator_fragment`
- Status: `current`
- Issue tags: `nwgmc_u_lowering`; `counterexample`; `anti_labial_blocking`; `row_2026_as_control_case`
- Recommended next use: `cite_when_explaining_why_folc_is_regular_not_exceptional`
- Shared with row IDs: `1973, 2030, 2162, 2298, 2300`

This is the main surviving DEV_NOTES material that actually mentions row 2026's form. The section begins from the regular law: NWGmc lowering takes stressed `*u` to `*o` before a following non-high vowel, and DEV_NOTES treats that rule as “correct and well-established” even while cataloguing a separate cluster of OE forms that unexpectedly keep `u` [Germanic/docs/DEV_NOTES.md:68-70]. Inside the literature summary, Bülbring is quoted as observing OE `u` “namentlich zwischen Labial und langem oder gedecktem l”, but DEV_NOTES preserves his equally important concession that “meist steht jedoch der Hauptregel gemäß o”, with `folc` named among the counterexamples [Germanic/docs/DEV_NOTES.md:82-82]. For this slice, that quotation is more valuable than a generic statement that `folk` is regular, because it shows that `folc` had already been functioning in the project's working notes as one of the forms that prevents overgeneralization from `full`, `wulf`, `fugol`, and similar items.

The Luick paragraph sharpens the same point. DEV_NOTES says Luick “rejects” Bülbring's phonological proposal and instead argues for paradigmatic levelling, precisely because forms such as `wolcen, folc, folġian, folde, folm, bolla, bolt, bolster, molde, molcen, smolt` still show regular lowering in apparently favorable labial/velar environments [Germanic/docs/DEV_NOTES.md:84-84]. Row 2026 therefore belongs in the documentation not as a problem child but as a control case: it is one of the words that makes a blanket labial-preservation rule philologically unsafe.

### DEV_NOTES:line-136-142

- Source label line: `DEV_NOTES project decision on the exception cluster`
- Source heading: `Decision and implementation`
- Source line or section hint: `lines 136-142`
- Fragment type: `shared_policy_fragment`
- Status: `current`
- Issue tags: `project_policy`; `exceptions_vs_regulars`; `counterexample`; `do_not_formalize_labial_rule`
- Recommended next use: `cite_when_distinguishing_row_2026_from_true_u_retention_exceptions`
- Shared with row IDs: `1973, 2030, 2162, 2298, 2300`

This later part of the same DEV_NOTES block records the project's explicit policy conclusion. It says the FST “correctly models the regular NWGmc u-lowering as a phonological rule” and that the `u`-preserving forms are the exceptional items for which “no phonological conditioning has been established” [Germanic/docs/DEV_NOTES.md:136-136]. Immediately afterward, the note allows only a much weaker claim: there may be a statistical phonetic tendency near labials or gutturals, but “the counterexamples (`folc`, `bolla`, etc.) preclude formalizing it” [Germanic/docs/DEV_NOTES.md:138-142].

For row 2026, this fragment is effectively the surviving replacement note. It explains why the current trace `*fúlką > *fólką > folc` should be read as positive evidence for the regular law, and why later documentation must not accidentally recast `folc` as if it belonged to the same exception bucket as `wulf` or `fugol` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1530-1542]. It also means that if a later packet is written, row 2026 should probably be cross-referenced to those exception rows as a comparator or limiting case, not as another member of the exception cluster.

## Superseded or diagnostic material

The main potentially misleading DEV_NOTES material is not row-specific but widow-specific. In the later `widuwe` investigation, DEV_NOTES briefly proposed that medial unstressed `*u` might be preserved in broadly “labial environments” and even states, for that separate problem, “We will block `OEMedUnstressedULowering` when medial `*u` is immediately preceded or followed by `*w`” [Germanic/docs/DEV_NOTES.md:583-607]. That note should not be imported into row 2026 as if it supplied support for `folk / folc`: it concerns a different change (OE medial unstressed `*u`, not stressed NWGmc `*u`-lowering), and DEV_NOTES elsewhere already uses `folc` as a counterexample to any broad labial-preservation generalization [Germanic/docs/DEV_NOTES.md:82-84,138-142,583-607].

Also diagnostic only is the absence of row-local DEV_NOTES substance. There is no surviving section that walks through OE `folc` attestation, no preserved packet prose, and no row-local known-problem entry. The documentation burden for this slice is therefore conservative by design: it records the exact current row state and the shared comparative notes that mention `folc`, but it does not claim more row-specific philological support than the surviving materials actually provide [Germanic/docs/lexeme_reports/coverage_audit.md:248-248; Germanic/data/oe_known_problems.tsv:1-8].

## Open questions for later work

- If a final lexeme report is later commissioned, add a direct lexicographic citation for OE `folc` itself; the surviving DEV_NOTES material uses `folc` mainly as a comparative counterexample inside a sound-law discussion, not as a stand-alone attestation dossier [Germanic/docs/DEV_NOTES.md:82-84].
- If the exception-cluster rows later get a consolidated index, cross-link row 2026 as a comparator/control case for the labial-near-`l` debate, since DEV_NOTES names `folc` precisely to show that such environments do not categorically preserve `u` [Germanic/docs/DEV_NOTES.md:82-84,138-142].
- If later review revisits the widow-related “labial environment” language, keep the two phenomena separate: row 2026 currently supports regular stressed NWGmc lowering `*u > *o`, whereas the widow note addresses a different OE medial unstressed change and should not silently be generalized back onto `folc` [Germanic/docs/DEV_NOTES.md:583-607].
