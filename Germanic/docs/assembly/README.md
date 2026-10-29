# Build the CAPR book

The default publication is the combined sound-change and lexical book:

```sh
bash Germanic/docs/assembly/build_capr_book_draft_docker.sh
```

Run from the repository root with Docker and the locally provisioned scholarly
holdings/runtime. The wrapper performs canonical refresh before checks and
rendering. It fails rather than publishing stale inputs. Outputs are
`capr_book_draft_alpha_01.md` and `.pdf`; `ASSEMBLY_KEEP_DEBUG_TEX=1` retains
the intermediate TeX for diagnosis. Inspect the rendered pages after changes.
For portable versus strict validation, see [CI validation](../../../docs/CI_VALIDATION.md).

## Edit the source, not the assembly

| Material | Editable owner |
| --- | --- |
| Book introduction | `capr_book_intro_alpha_01.md` |
| Sound-change prose | One reader source per published SC, owned by `sound_changes/registry/sc_registry.tsv.source_reader_facing_file`; routed by `adjudicate.py SCNNN --prepare` |
| Sound-change order and chapter divisions | Individual `oe_pipeline` executable sequence; `sound_changes/registry/reader_chapters.tsv` adds SC-anchored chapter boundaries without reordering |
| Elaborated lexical prose | `../lexeme_reports/model_entries/*.model.md` |
| Scoped lexical selection/certification | `../lexeme_reports/pgmc_integration/editorial_cases.tsv` and the existing report manifest |
| Lexical presentation order | `lexical_editorial_order.tsv` (explicit exceptions only; the default editorial policy is derivation class, then alphabetical Modern English headword) |
| Bibliography | `docs/refs.bib` |
| Index decisions | `../book/` SOURCE registries and scoped overrides; never distort prose to appease a checker |

`artifact_graph.py` is the sole generated-output owner. Its `--inventory`
lists node kinds, authorities and outputs. `adjudicate.py --refresh` rebuilds
stale products and checks the fixed points; never maintain another builder list.
Class manifests, compact traces, lexical aggregate, reader aggregate, combined
manuscript and index projections are generated.

The reader manifest has one row per published identity, never a grouped-file
minimum. Filenames and SC numbers are stable identifiers, not sort keys.
The five chapter beginnings are resolved within the already ordered sequence;
moving a rule across a boundary automatically changes its chapter on the next
`adjudicate.py --refresh`. Crossed or missing boundaries fail rather than
rearranging rules. `reader_files.tsv` has been retired with no replacement
membership/order table. Do not reorder the generated manifest or books.

The reader tracks the adopted executable reconstruction, not a claim that
every pairwise historical chronology is independently demonstrated.
Adjudication records preserve that distinction. Existing technical explanations
remain explicitly classified support stages, not new historical sound laws;
SC113 remains unpublished annotation machinery.

One source file is one published SC, including its internal component networks.
Shared thematic background belongs in chapter introductions and cannot force
entries to move together. Chapter breaks remain intentional; a new source file
does not force a new page. Normal reader builds check exact canonical/manifest/
reader/combined SC sequence equality, ownership, headings and anchors.
See [migration evidence](reader_architecture_migration.md) for the original
grouping defect, content-preservation accounting and non-regression record.
Printed Foma bodies are checked against canonical definitions by the shared
parser. Coverage reports classify the current registry population rather than
treating historical report-manifest differences as publication omissions.

Semantic predicted forms use ordinary Markdown content, such as
`[dejæ]{.pred}`, not a raw-LaTeX-only span; the shared filter fails if content
would disappear. Shared rendering keeps short Foma boxes together while long
rules remain breakable. This is independent of source-file boundaries and
does not insert a page break per rule.

The [post-migration consistency record](post_migration_consistency.md) records
chronology reconciliation, rendering causes, runtime-fixture reliability and
the subsequent validation, without rewriting the earlier migration receipt.

Entry position is editorial, never an identifier. Row IDs, filenames and corpus
order do not decide where a lexical entry is published, so adding, renumbering
or re-encoding an entry never needs a manual reorder, and a reorder never touches
reconstructions, selections, sound laws or baselines. To depart from alphabetical
order, add a `row_id`, `sort_as` headword and `reason` row to
`lexical_editorial_order.tsv`, then run `adjudicate.py --refresh`; never
rearrange `manifest_*.tsv`, the lexical volume or the combined draft by hand.
A nonstandard headword (compound, hyphenated, non-`a-z`) or a tie stops the
build until such a row exists.
`tests/test_lexical_editorial_order.py` checks coverage, duplicates, exception
references, the approved sequence and downstream propagation.

## Distinct supported presentations

The default class-manifest book consumes the 168 mature models, including
90 regular entries, preserving their complete arguments and all seven derivation
classes. The complete 389-row compact derivation report has a separate selective
commentary insertion route, currently 22 certified narratives with explicit
outstanding obligations. The current audit covers 395 identities including
six research-only rows; the original reconstruction survey's 393-row scope
remains historical.
See the [generated population summary](../lexeme_reports/pgmc_integration/population_summary.md)
for current counts; these are different populations, not competing corpus owners.

The optional `book_prose` regular-entry presentation is not the default.
Cleanup neither promotes it nor turns every derivation into an extended essay.

Standalone renderers remain supported:

- `build_full_lexical_volume_docker.sh` (or `.sh` with local Pandoc/LaTeX):
  the selective lexical volume.
- `../sound_changes/reader_facing/build_reader_facing_local_section_20_docker.sh`:
  the sound-change reader, with its source-level checks.
- `build_pilot_docker.sh` (or `.sh`): the eight-entry layout/citation fixture,
  not a production population or an unfinished mandatory rollout.

The Python builders implement those presentations; invoke the wrappers for
publication so freshness is enforced.

Both standalone lexical renderers use the same citation and semantic-form
filters. Companion `#rule-...` links without local destinations become readable
non-clickable references only in standalone output. Local links remain active;
the combined book keeps its clickable sound-change references. Both lexical
wrappers and the combined wrapper check actual generated TeX destinations and
PDF-build warnings, failing on unresolved internal references.

The combined wrapper refreshes once. It passes `--check-fresh` to the two
nested Docker renderers, which run the strict graph check and refuse stale
inputs instead of refreshing again. Called without that option, each renderer
still refreshes normally. This is not a validation-bypass option.

## Historical SC034 publication integration receipt

The counts, page locations and validation results below describe the SC034
publication state, not the current populations linked above.

This editorial integration follows scientific release `25d931d5`; it does not
change SC034/SC111, selected inputs, targets or protected scientific baselines.
The standard combined wrapper newly built all four PDFs below. Targeted rendered
pages were inspected, including straw's summary, complete trace and paradigm
table; the three show cells; SC111/SC034; lexical introductions; bibliography
and both relevant index sections.

| PDF | Measured pages | Inspection locations |
| --- | ---: | --- |
| `capr_book_draft_alpha_01.pdf` | 308 | Straw 9.18, printed 266--267; show 6.54, 165--166; imperative 9.28, 278--280; third singular 9.29, 280--281; SC111 30; SC034 72 |
| `lexical_volume_alpha_01.pdf` | 152 | Introduction 1; show 37--38; straw 125--126; imperative 136--137; third singular 137--138 |
| `../sound_changes/reader_facing/reader_facing_local_section_20.pdf` | 123 | SC111 32; SC034 74 |
| `capr_book_intro_alpha_01.pdf` | 4 | Opening page |

Combined-book page numbers above are printed locators; its two front-matter
pages make the corresponding PDF sheet number two greater. Bibliography is
printed 297--299; the Old English and Proto-Germanic straw/show index entries
are on 303 and 305. Standalone locations are PDF page numbers.

Both actual lexical and combined builds pass the unresolved-reference gate.
Independent PDF destination inspection resolves every named internal link;
combined straw/show links reach the actual companion rule sections. Standalone
companion rule references retain their descriptive text without invalid links.
The complete compact report still has 387 identities, with 19 certified
narratives; straw's selection is editorial, not survey-wide certification.

Final strict local validation passed 1,362 tests and 8,507 subtests, including
the provisioned runtime checks. The independent portable runner passed all five
gates: 1,329 tests and 8,482 subtests passed; 33 runtime-dependent tests were
explicitly skipped. Portable validation does not repeat original-image
verification or certify the runtime capabilities exercised by the full run.
Strict scholarly-holding validation and the final strict artifact-graph check
also passed.

An independent byte comparison against `25d931d5` preserves 61 scientific
files, including the FST, corpus, registry TSVs and complete baseline directory.
The selected population remains 387 accepted, 379 matching and eight
mismatching, without ambiguity or rejection; straw still yields `strēa`
against `strēaw`. The new default assembly has 161 models, including 29
late-analogy entries. A shared narrow-panel form-column correction was
re-inspected in both PDFs; it removes the show third-singular trace collision.

The Docker publication wrappers were executed; the equivalent host-local
lexical wrapper was covered by filter/parity regressions but not executed.
Existing source-image certifications were reused, not comprehensively repeated.
The Ringe--Taylor reconstruction-conventions verification gap, show's disputed
prehistoric root history and straw's qualified noun/verb genealogy remain
explicit limits, not newly certified conclusions.

## Historical designs and reports

[archive/](archive/) retains the earlier pilot/alpha navigation and the
[pre-implementation design](archive/full_assembly_design.md) verbatim.
Future-tense instructions there describe the old design stage, not missing
implementation. Layout fixtures and published reports are retained where they
still have a distinct purpose; large generated products are not discarded
merely because they can be rebuilt.
