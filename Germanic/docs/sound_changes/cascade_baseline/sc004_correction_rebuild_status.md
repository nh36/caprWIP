# SC004/SC014 correction — rebuild status (§6)

Scientific closure reached: all 134 tests pass, chronology cards regenerated,
frozen `outputs_sha256` `aaf19ba919cafbe86ea59d482ce74d0944f541336e246da481a3f37b20da480e`
preserved, and the mismatch report is byte-identical after regeneration.

## Regenerated (direct artefacts of the corrected FST)

- **Full stage-by-stage trace** `debug_snapshots/oe_full_trace_report.txt`
  (regenerated from the recompiled sandbox checkpoints, corrected SC014/SC004
  rule bodies).
- **Mismatch report** `debug_snapshots/oe_mismatch_report.txt` (regenerated;
  byte-identical — the split/correction is output-neutral).
- **Interaction matrix** `cascade_baseline/cascade_interaction_matrix.tsv` and
  the SC004/SC014 crossing analysis.
- **First-break summaries** `order_tests/summaries/sc004corr_first_break_*`
  (SC014, SC004, SC036).
- **Component application report** (PROTOFORM) and **component behaviors** probes.
- **PROTOFORM-frozen baseline**
  `cascade_baseline/post_sc004_split_semantic_baseline.tsv`.

## Downstream reassembly (coupled Docker book/index pipeline)

The compact/derivation-class trace (`oe_derivation_class_trace_report.compact.md`),
the assembled book (`assembly/capr_book_draft_alpha_01.md/.pdf`), the lexical
volumes (`assembly/lexical_volume_*`), the reader-facing local sections
(`reader_facing/reader_facing_local_section_*.md`), and the index-verborum
products (`docs/book/index_verborum_*`) are assembled from the corrected reader
sources and the FST by the reader-facing / book / index Docker build pipeline
(`build_index_verborum.py` writes both the compact trace and the index). They are
regenerated wholesale by that pipeline, which consumes the updated
`reader_facing/004-pwgmc-ai-monophthongization.md`,
`reader_facing/014-015-opening-vowel-prelude.md`, and
`reader_facing/chap3-pwgmc-to-af-intro.md`. The `post_sc004_split_semantic_baseline`
hashes these products so that a mismatch after the downstream rebuild is
detectable; the book-headings/index rows in the baseline should be re-frozen once
that rebuild runs.

The authoritative inputs (FST, registries, dossiers, reader sources, chronology
cards) are all corrected; the downstream products carry only the mechanical
regeneration of that corrected content.
