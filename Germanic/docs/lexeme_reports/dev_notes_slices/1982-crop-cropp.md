---
row_id: 1982
concept: crop
counterpart: cropp
proto: *krúppaz
protoform: *krúppaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1982 crop / cropp

## Current row state

- The live OE row is `CONCEPT = crop`, `COUNTERPART = cropp`, `PROTO = *krúppaz`, `PROTOFORM = *krúppaz`, `DERIVATION_CLASS = regular`; the source field is only the inherited-etymology placeholder, not a row-local explanatory note [Germanic/data/germanic-aligned-final.tsv:199-199].
- The published derivation trace is currently exact and explicitly regular: `Proto Input: *krúppaz`, then `NWGmc U Lowering: *króppaz`, then `PGmc Final Z Deletion: *króppa`, then `PWGmc Final Bare A Loss: *krópp`, with surface `Outcome: cropp` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:773-792].
- `coverage_audit.md` still treats row 1982 as a plain regular row with `NOTE? no`, empty report slots, and `Requirement basis = none`, so there is no pre-existing packet/memo chain to inherit here [Germanic/docs/lexeme_reports/coverage_audit.md:218-218].

## Development-note summary

`DEV_NOTES.md` does not preserve a dedicated `crop / cropp` dossier. The materially relevant support is shared rule discussion about Northwest Germanic `u`-lowering near labials. That discussion states the project's baseline rule in unambiguous terms: “Our NWGmcULowering rule lowers stressed *u → *o before non-high vowels in a following syllable ... This is correct and well-established.” It then isolates only a limited set of lexemes as true holdouts, e.g. `*fullăz → full`, `*wulfăz → wulf`, `*fuglăz → fugol`, `*bukkăz → bucc`, `*wullō → wulle`, `*lubō → lufu`, `*rustō → rust` [Germanic/docs/DEV_NOTES.md:70-78].

For row 1982, that shared note matters because the live derivation is exactly the ordinary path that the note says should remain ordinary: `*krúppaz -> *króppaz -> cropp` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:782-792]. The row sits in a labial environment and ends in geminate `-pp-`, but DEV_NOTES explicitly refuses to treat labial adjacency as a categorical blocker. Bülbring's older account is preserved with the concession that “meist steht jedoch der Hauptregel gemäß o” (“usually the regular rule gives o”), and Luick's counterargument is copied even more sharply: forms such as `wolcen, folc, folġian, folde, folm, bolla, bolt, bolster, molde, molcen, smolt` show that similar labial/velar environments still undergo regular lowering [Germanic/docs/DEV_NOTES.md:82-84].

The practical project conclusion is also directly relevant. DEV_NOTES decides: “Accept the mismatches. The FST correctly models the regular NWGmc u-lowering as a phonological rule. The u-preserving forms are genuine lexical exceptions for which no phonological conditioning has been established” [Germanic/docs/DEV_NOTES.md:136-138]. Row 1982 therefore does **not** need an exception story, analogical substitute, or OE-known-problem diagnosis. Its usefulness as a replacement note is narrower: it is a regular control row whose current `cropp` outcome is fully compatible with the live implementation and with DEV_NOTES' refusal to generalize a labial-blocking rule.

Because the DEV_NOTES support is shared rather than row-explicit, this slice should stay conservative. It preserves the substance of the project's discussion about why some labial-context words keep `u`, but it should not pretend that DEV_NOTES singled out `crop / cropp` itself for special treatment. The durable point is simply that row 1982 follows the regular lowering path, and the project's own note says that this regular path remains the default even in many labial contexts [Germanic/docs/DEV_NOTES.md:70-86,136-140].

## Relevant DEV_NOTES fragments

### `Germanic/docs/DEV_NOTES.md:70-86`

- Source heading: `NWGmc u-lowering Exceptions Near Labials`
- Fragment type: `shared_rule_discussion`
- Status: `current`
- Issue tags: `u_lowering`; `labial_environment`; `exception_scope`; `regular_control_case`
- Recommended next use: `cite_if_explaining_why_cropp_needs_no_exception`
- Shared with row IDs: not row-specific; applies to the broader `u`-lowering / labial cluster discussion.

This is the main fragment that bears on row 1982. It opens with the project-wide rule statement that stressed `*u` lowers to `*o` before a following non-high vowel and says that this rule is “correct and well-established” [Germanic/docs/DEV_NOTES.md:70-70]. It then lists the genuine holdouts and preserves two important quotations from the literature review: Bülbring's concession that “meist steht jedoch der Hauptregel gemäß o” and Luick's rejection of categorical labial conditioning via counterexamples such as `folc`, `bolla`, `bolt`, and `molcen` [Germanic/docs/DEV_NOTES.md:82-84]. For `*krúppaz > cropp`, the fragment is relevant precisely because it does **not** create a blanket labial exception. The row's `NWGmc U Lowering: *króppaz` trace is therefore consistent with the surviving DEV_NOTES policy [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:786-786].

### `Germanic/docs/DEV_NOTES.md:136-140`

- Source heading: `Decision and implementation`
- Fragment type: `project_policy`
- Status: `current`
- Issue tags: `exception_policy`; `u_lowering`; `wontfix_scope`; `lexical_exception_only`
- Recommended next use: `quote_when_distinguishing_regular_rows_from_exception_rows`
- Shared with row IDs: all rows potentially affected by NWGmc `u`-lowering near labials.

This short decision passage is the clearest current policy statement to carry over. DEV_NOTES says: “Accept the mismatches. The FST correctly models the regular NWGmc u-lowering as a phonological rule. The u-preserving forms are genuine lexical exceptions for which no phonological conditioning has been established” [Germanic/docs/DEV_NOTES.md:136-136]. It then keeps only a speculative future-discussion note about possible phonetic clustering near labials/gutturals, immediately adding that the counterexamples “preclude formalizing it” [Germanic/docs/DEV_NOTES.md:138-140]. For row 1982, this is the reason to stay neutral and non-diagnostic: `cropp` is not one of the retained exception rows, and DEV_NOTES does not authorize promoting `-pp-` to a rule blocker.

## Superseded or diagnostic material

- Bülbring's labial-environment idea is worth preserving only as diagnostic/superseded background. DEV_NOTES itself records both his own concession that regular `o` is still the usual outcome and Luick's explicit rejection of categorical phonological conditioning, so this material should not be reused as if it licensed a special `*krúppaz > cropp` rescue rule [Germanic/docs/DEV_NOTES.md:82-84].
- No row-specific packet, research memo, dossier, or analysis file was found for row 1982, and `coverage_audit.md` still marks it as a regular no-note row with no report requirement; the blank metadata links above are therefore an accurate evidence-state report, not an omission in this slice [Germanic/docs/lexeme_reports/coverage_audit.md:218-218].
- There is likewise no surviving row-specific DEV_NOTES passage for `crop / cropp`. The note material here is intentionally thin and shared; later reporting should not overstate it as if DEV_NOTES had preserved a dedicated lexical argument for this row [Germanic/docs/DEV_NOTES.md:70-86,136-140].

## Open questions for later work

- If a later packet or research memo is created, add direct handbook or dictionary evidence for OE `cropp` / PGmc `*krúppaz`; the current replacement slice is strong on project rule policy but thin on row-specific philology.
- If later work revisits labial-context `u`-lowering, keep row 1982 on the regular side unless a source specifically names `cropp` as exceptional. The existing DEV_NOTES material argues against promoting a statistical labial tendency into a categorical rule [Germanic/docs/DEV_NOTES.md:82-84,138-140].
- If `index.tsv` is reconsidered later, this slice probably belongs in the conservative/no-index tier unless more row-explicit evidence is added. The present note is useful replacement documentation, but its DEV_NOTES basis is shared policy discussion rather than a dedicated row-local dossier [Germanic/docs/DEV_NOTES.md:70-86,136-140; Germanic/docs/lexeme_reports/coverage_audit.md:218-218].
