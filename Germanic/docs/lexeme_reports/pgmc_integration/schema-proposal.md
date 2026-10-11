# Proposed lexical-report selection and coverage change

Status: proposal for author review. `report_schema.md`, the current coverage
helper, model entries and both publication manifests remain unchanged.

## Two independent dimensions

The derivation dimension keeps the existing classifications and their meanings.
`regular` says the selected path is modelled, not that its reconstruction is
uncontroversial. `early_analogy` concerns pre-encoded/remodelled input;
`late_analogy` can concern paradigm selection or later levelling, even when a
chosen oblique is phonologically regular. `known_unmodelled` identifies a
known explanatory gap, while `unexplained_unmodelled` retains an unresolved
one. `attested_variant` and `reconstructed_oe` preserve comparator status.
None of these labels assigns philological significance.

The reconstruction dimension records scoped editorial categories from
`editorial_cases.tsv`, linked to protected audit evidence. A reviewed scope,
category, precise reason and missing premise replace automatic inference from
the number of comparisons or their type tags. Different questions for one row
may receive different categories. "Not editorially reviewed" is an independent
workflow state, never an automatic negative judgement.

## Minimal proposed replacement for the selective-policy paragraph

Retain the three existing triggers (NOTE, nonregular class, manually certified
production report). Add:

> An extended lexeme report is also required when a source-checked editorial
> assessment identifies a substantive reconstruction disagreement concerning
> the selected formation or its historical input. A qualified alternative
> requires an explicit editorial decision that the unresolved premise is
> consequential for that formation. Differences of notation, cell, endpoint
> or unrelated etymological family alone do not activate the requirement.
> Regular derivation and absence of a TSV note do not exempt an entry from
> this philological requirement.

A source-backed substantive controversy should automatically require an
extended report *after* identity, comparability and relevance are manually
established. A machine-generated candidate is not that establishment.
Qualified alternatives are not all mandatory essays: scope their payoff
explicitly. Ordinary entries continue with concise input/cell, source,
derivation and result treatment. Non-substantive differences may need a
sentence, not a history of the entire scholarship.

Do not put an extra trigger into NOTE or alter DERIVATION_CLASS to achieve
selection. Those would conflate the axes and corrupt existing scientific
classifications. The judgement relation is the single editorial SOURCE;
the inventory, coverage reason and selection status are projections.
The next policy adoption should add one small explicit
`requires_extended_discussion` decision for qualified cases to that relation,
not infer it from a category's wording. It is intentionally not implemented
here because all present examples are provisional and unpromoted.

## Entry structure and citations

Preserve the current schema's useful evidence and derivation sections. Add a
short, optional "Reconstruction and competing interpretations" section,
before the sound-change argument. It must identify the compared object and
explain the consequential difference rather than reproduce evidence lists.
Its conclusion distinguishes input legitimacy, sound-change validity and
computed target correspondence.

Always identify PROTO and PROTOFORM separately when they differ. The former
remains the PGmc citation; the latter is the actual selected cell/input with
its independently established stage and context. If a complete cell is
assembled from a scholarly stem and ending, state that CAPR made the assembly.
Equal values and the code's equality-stage convention do not independently
prove that an author reconstructed the exact complete input.

Cite bibliographic keys and printed pages for substantive assertions.
Preserve original signs and author commitment: a reported/rejected theory
is not the author's preference. Keep detailed evidence IDs in the traceability
companion, not the reader-facing argument. Unsettled premises should be
named precisely; they need not be resolved to make a useful lexical report.

## Minimal future coverage logic

Proposed predicate:

```
old_requirement = has_note or class_is_nonregular or certified_production_report
philological_requirement = reviewed_relevant_substantive_case
                           or explicitly_selected_qualified_case
requires_extended_report = old_requirement or philological_requirement
```

Expose both reasons independently alongside material availability, draft
presence, review status and actual book inclusion. Use stable-ID joins, exact
selected forms and declared evidence links; exclude `format_test` from
certified production. Provisional integration examples remain neither
production nor a manual-trigger workaround.

The first adoption task must reconcile the legacy pilot/full manifest and
the model-entry assembly. Prefer one certification mechanism for publishable
model prose; preserve pilot/format-test distinctions without pretending the
11 pilots equal the 160 assembled entries. Make its exact ownership choice
with the author before changing validators or manifests.

Tests for that later adoption should cover regular-but-substantive selection,
qualified-case decisions, no selection from bounded limits/type tags, mixed
scopes, no conflation of cell and reconstruction, ordinary concise entries,
prototype exclusion, stable homonym/cell IDs and independent derivation status.
This assignment provides the research projection and safeguards, not the
new production predicate.
