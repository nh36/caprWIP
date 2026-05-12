# Book architecture 02 report

## Summary

- Seven TSV derivation classes now used as canonical architecture sections: **yes**
- Class manifests regenerated: **yes**
- Total model entries found: **147**
- Counts by class:
  - `regular`: **70**
  - `attested_variant`: **4**
  - `early_analogy`: **35**
  - `late_analogy`: **28**
  - `reconstructed_oe`: **3**
  - `known_unmodelled`: **2**
  - `unexplained_unmodelled`: **5**
- Unknown class labels remaining: **0**
- Full assembly attempted: **no**

The regenerated seven-class counts match the expected live corpus split exactly,
so no corpus-drift explanation is needed in this pass.

## Class architecture

The lexical volume architecture now treats these seven TSV `DERIVATION_CLASS`
values as first-class sections in this order:

1. `regular` -> **Regular derivations**
2. `attested_variant` -> **Attested variants and selected comparison forms**
3. `early_analogy` -> **Early analogy and pre-Old-English input selection**
4. `late_analogy` -> **Late analogy and paradigm-cell selection**
5. `reconstructed_oe` -> **Reconstructed Old English comparators**
6. `known_unmodelled` -> **Known but unmodelled remodellings**
7. `unexplained_unmodelled` -> **Unexplained or deliberately unmodelled exceptions**

Unknown future labels still fall back to a review bucket with warnings, but the
currently attested seven labels are now all canonical assembly sections.

## Manifest changes

New manifest files created:

- `manifest_attested_variant.tsv`
- `manifest_reconstructed_oe.tsv`
- `manifest_known_unmodelled.tsv`

The previous review-bucket treatment for `attested_variant`,
`reconstructed_oe`, and `known_unmodelled` has been removed.

Current manifest counts:

- `manifest_regular.tsv`: 70
- `manifest_attested_variant.tsv`: 4
- `manifest_early_analogy.tsv`: 35
- `manifest_late_analogy.tsv`: 28
- `manifest_reconstructed_oe.tsv`: 3
- `manifest_known_unmodelled.tsv`: 2
- `manifest_unexplained.tsv`: 5
- `manifest_all_by_class.tsv`: 147

All **147** current model entries are now assigned to canonical assembly
sections, and `manifest_summary.md` reports:

- zero unknown class labels
- zero incomplete metadata rows
- zero filename row-ID parse problems
- zero non-confident trace matches

## Documentation changes

Updated:

- `book_architecture.md`
  - now presents a seven-part main lexical catalogue
  - removes language describing `attested_variant`, `reconstructed_oe`, and
    `known_unmodelled` as anomalous or review-bucket categories

- `full_assembly_design.md`
  - now specifies seven-class ordering for future full assembly
  - makes clear that the current known labels are canonical
  - retains a fallback warning/review path only for unknown future labels

- `section_introductions_draft.md`
  - now includes mechanical placeholder introductions for all seven sections
  - removes the earlier “review bucket” framing

- `README.md`
  - now lists the seven class manifests
  - states that the assembly architecture follows all seven TSV derivation
    classes

## Remaining issues

- No unknown derivation-class labels remain in the current corpus.
- No trace-match problems remain in the current corpus.
- `1959 bottom / botm` remains the reviewed-but-unchanged separator note from
  assembly pilot 08, but that is not an architecture blocker.
- No new architecture-level blocker appeared in this pass.

## Recommendation

**Decision: A. Seven-class architecture is ready; proceed to full lexical assembly alpha.**

## Scope confirmation

- No model-entry prose or metadata was edited.
- No TSV source data, FST files, `report_manifest.tsv`, compact trace files,
  packets, dev-note slices, research memos, bibliography files,
  OCR/reference files, or citation-locator reports were edited.
- No full-corpus PDF, TeX, or assembled Markdown volume was generated.
