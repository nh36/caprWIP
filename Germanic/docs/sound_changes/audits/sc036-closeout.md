# SC036 adjudication closeout

Base: `update` at `a36dbcfc2ec8fc4f28bf366a643473227cebb510`.
The publishing commit is the commit containing this report; its exact SHA
is reported in the delivery message. SC035 remains closed. SC037 has not
been adjudicated or begun.

## Decision and historical result

REFORMULATE / confidence C; retain the executable relation, stable identity,
position, `oe` stage and English-specific scope. The
[adjudication](sc036-adjudication.md) supplies the complete reasoning,
H1–H4 comparison and source-access qualifications. Confidence concerns the
composite account's historical generality, independently of stage and scope.

World's weak rounding and soul's nonhigh syncope, final-vowel loss and
epenthesis are not independently demonstrated instances of one raising law.
H2's historical distinction and H3's composite executable-proxy account are
adopted, without manufacturing two new identities. H1 is unestablished.
H4's unrestricted grave-vowel interpretation is refuted for the actual
network: Foma's single comma shares the context between both mappings.
Formal equivalence and negative probes confirm that finding.

The selected world input combines older first-member vocalism with later
ō-stem formation. Orel's actual reconstruction is not already mid-vowelled.
The dialectal initial and medial vowels are separate variables, and not
every written medial `o` proves an earlier `u`. Soul's source-supported
medial vowel disappears; its expanded surface has a secondary vowel.
The retained computation instead preserves and lowers an early raised
medial vowel. Neither successful final output establishes that history.

## Census, controls and effects

| Row | Selected input | Immediately before / after SC036 | Final / target |
| --- | --- | --- | --- |
| 2201 soul | `*sáiwalō` | `*s*ā*w*a*l*u → *s*ā*w*u*l*u` | `sāwol` |
| 2302 world | `*wír-àldu` | `*w*é*r*à*l*d*u → *w*é*r*u*l*d*u` | `weorold` |

These are the complete two firings in selected389 and the same two in the
overlapping migration-aware legacy380, not four independent witnesses.
Both later lose final `u` and undergo SC040; world additionally undergoes
back mutation. The full changing traces are in the experiment receipt.
Right-cluster `j` blocks the real lung derivative. Twenty-one component
probes test stress, length, vowel classes, following vowels, hiatus,
initiality and marker interactions; none is a new attestation.

Seventeen complete-cascade models compare the incumbent, isolated clauses,
equivalent and broader unions, omission and displacements. A-only loses
world's selected output; isolated B-only loses soul's. The equivalent
common-context union changes nothing; broadening its left class is not
formally equivalent despite unchanged live finals. Five later staged-input
comparisons are preserved separately in `sc036-experiments/staged-evidence.json`:
unaccented world still raises, already-rounded world needs no raising,
post-syncope soul gives `sāwl`, and the unshifted i-stem comparison is
explicitly rejected downstream. That rejection is not a linguistic
contradiction or a production failure.

| Relation | Classification and result |
| --- | --- |
| SC004 → SC036 | Model-local vowel-class representation; broadening the class removes the measured break. Completed SC004 judgment preserved. |
| SC019 → SC036 | Independently controlled computational feeding of final `u`, not independent historical dating. |
| SC036 → SC040 | Model-local serialization; current long displacement yields `sāwel/wereald`, not the frozen card's `sāwul/weoruld`. |
| SC036 / SC037 | Synthetic marker consumption can bleed linking syncope; no selected final changes on displacement. Technical, not historical chronology. |
| SC036 / SC038 | No selected boundary; the plain-a mapping substitutes after marker stripping. |
| Old boundary experiments | Frozen, superseded observations in their original coordinate systems; no exact old-runtime replay claimed. |

Production output changes: none, in any selected row. Every executable
definition is unchanged; FST edits are comments only. The selected389 remain
381 matches and eight mismatches, with 167 assembled entries.
No baseline was adopted or refrozen.

| Preserved fingerprint | SHA256 |
| --- | --- |
| Selected389 | `53769ef582dd6d119bacc18f808612980a1f02dfed2f94a6e30645bb9de00a9e` |
| Migration-aware legacy380 | `43de8a47b7aaf17f860c9e3009617002ddb36e4d32a90ede1a99525858a417ce` |
| Lexical projection | `c44d73698e2fa2717366e951a75bbb02d19aa677faf51fc86dfa25187556b6da` |
| Immutable original380 | `fae656520e9ebf446854643907a1ba48a511877fc25b1fae39649d5b97e9a6cf` |

An independent comparison of 225 tracked data, baseline and existing audit
files against the base found only the expected source-hash update in
`oe_equivalence_report.json`. Its output equivalence remains unchanged.
Full-trace changes are provenance only. Frozen cards, migration receipts,
completed adjudications and original scratch files are preserved.

## Validation and publication

Canonical preparation/evidence, a fresh Docker build, isolated compilation
and SC036 finalization were executed. Finalization reports
`CONTROL PLANE CLEAN` and successful propagation.

The requested full command, `cd Germanic/tests && python3 -m pytest -q`,
ran all tests: 1,588 passed and 9,087 subtests passed; one new SC036 assay
test failed because the experimental runner treated a deliberately
alternative input's downstream rejection as fatal. The runner now records
its exact rejected form, component and empty output set, while production
and complete-corpus checks remain strict. All seven SC036 tests then passed,
including fresh Docker execution and equality against the preserved staged
receipt (103.51 seconds). This is a full-run-plus-affected-rerun result,
not a claim of a second uninterrupted green full-suite run.

After the final reader corrections, the strict holding-backed documentary
run, `cd Germanic/tests && python3 -m pytest -q -m 'not runtime'`, passed
1,546 tests and 9,054 subtests, with 43 runtime tests explicitly deselected
(929.28 seconds). The initial full run had already passed the other 42
runtime tests; the corrected SC036 runtime test passed in its affected
rerun. Thus all 1,589 collected tests have passing outcomes across the
full run and these reruns; the documentary rerun is not a substitute for
the recorded Docker execution.

The complete supported command
`bash Germanic/docs/assembly/build_capr_book_draft_docker.sh` succeeded,
building the reader, lexical volume, combined book and introduction.
Exact 97-identity executable/manifest/publication parity, printed definitions,
citations, paragraph glosses, semantic/index policy and unresolved-reference
gates passed. Initial build failures were corrected in the new prose:
SC-plus-executable-name link labels and missing first-occurrence soul glosses.
No unrelated scholarly prose or checker exceptions were changed.
The strict `artifact_graph.py --check` passed after rendering.

| Rendered PDF | Total sheets | Visually inspected sheets |
| --- | --- | --- |
| Combined book | 300 | 68–70 (printed66–68): SC036 history, soul, definition, chronology; 233 (printed231): world; 297/299 (printed295/297): OE and reconstructed-form indexes |
| Standalone reader | 107 | 68: printed SC036 definition, accent explanation and chronology |
| Lexical volume | 158 | 108: world's evidence, corrected derivation and comparison table |

The inspected rule boxes, accents, macrons and reconstructed forms render
without clipping or missing characters. Cross-reference destinations pass
the build's actual-PDF/TeX gate. World index locators resolve to the lexical
discussion, and the mixed transponent retains its distinct label.
New scholarly page images and copyrighted PDFs are not distributed.

## Legitimate residue and next task

Unresolved: the precise rounding path, independently reconstructed weak
prominence and full historical domain; a coordinated, historically faithful
distributed soul implementation; source passages explicitly qualified as
text-only in the source ledger, especially Bülbring's unavailable original;
and exact historical whole-runtime replay. No general historical
`a > u > o` claim or unrestricted secondary-stress reduction is adopted.

The next administrative task is SC037, as confirmed by `--next`, not a
chronological assertion. Its separately authorized investigation should
start from independently reconstructed linking vowels and retained versus
weakened stress, then distinguish actual syncope from marker bookkeeping.
The present synthetic interaction is a diagnostic, not its adjudication.

## Changed-file inventory

All paths below are relative to `Germanic/`. SOURCE changes are the memo,
assay/source ledger, reader, registry/inventory judgments, FST comments,
grouped-dossier authority notice and bounded world-entry corrections.
Other files are generated propagation or supported publication outputs;
the introduction PDF is a rebuild, not an introduction SOURCE change.

```text
docs/assembly/capr_book_draft_alpha_01.md
docs/assembly/capr_book_draft_alpha_01.pdf
docs/assembly/capr_book_intro_alpha_01.pdf
docs/assembly/lexical_source_provenance.json
docs/assembly/lexical_volume_alpha_01.md
docs/assembly/lexical_volume_alpha_01.pdf
docs/assembly/lexical_volume_alpha_01.tex
docs/book/index_verborum_audit.md
docs/book/index_verborum_book_emissions.tsv
docs/book/index_verborum_book_main.tsv
docs/book/index_verborum_book_occurrences.tsv
docs/book/index_verborum_book_print_unique.tsv
docs/book/index_verborum_emission_table.tsv
docs/book/index_verborum_forms.tsv
docs/book/index_verborum_preoe_review.tsv
docs/book/index_verborum_print_audit.md
docs/book/index_verborum_print_excluded.tsv
docs/book/index_verborum_print_main.tsv
docs/book/index_verborum_print_unique.tsv
docs/book/reader_facing_example_forms.tsv
docs/debug_snapshots/oe_full_trace_report.txt
docs/lexeme_reports/model_entries/2302-world-weorold.model.md
docs/lexeme_reports/model_entries/2302-world-weorold.source_ledger.md
docs/sound_changes/audits/sc036-adjudication.md
docs/sound_changes/audits/sc036-closeout.md
docs/sound_changes/audits/sc036-experiments/README.md
docs/sound_changes/audits/sc036-experiments/evidence.json
docs/sound_changes/audits/sc036-experiments/experiment.py
docs/sound_changes/audits/sc036-experiments/source-evidence.tsv
docs/sound_changes/audits/sc036-experiments/staged-evidence.json
docs/sound_changes/book_dossiers/035-037-prefix-and-compound-adjustments.book-dossier.md
docs/sound_changes/cascade_baseline/oe_equivalence_report.json
docs/sound_changes/order_tests/chronology_graph/first_break_edges.dot
docs/sound_changes/order_tests/chronology_graph/first_break_edges.json
docs/sound_changes/order_tests/chronology_graph/first_break_edges.tsv
docs/sound_changes/order_tests/chronology_graph/first_break_graph_summary.md
docs/sound_changes/order_tests/chronology_graph/first_break_nodes.tsv
docs/sound_changes/reader_facing/036-inter-stress-raising.md
docs/sound_changes/reader_facing/reader_facing_chronology_evidence_check_01.md
docs/sound_changes/reader_facing/reader_facing_foma_width_check_01.md
docs/sound_changes/reader_facing/reader_facing_local_section_20.md
docs/sound_changes/reader_facing/reader_facing_local_section_20.pdf
docs/sound_changes/registry/chronology_edges.tsv
docs/sound_changes/registry/current_chronology.tsv
docs/sound_changes/registry/current_sc_state.tsv
docs/sound_changes/registry/sc_inventory_annotations.tsv
docs/sound_changes/registry/sc_inventory_notes.tsv
docs/sound_changes/registry/sc_registry.tsv
docs/sound_changes/registry/settled_verdicts.md
docs/sound_changes/sound_change_historical_staging_map.tsv
docs/sound_changes/sound_change_inventory.tsv
fsts/germanic.txt
tests/test_sc036_adjudication.py
```
