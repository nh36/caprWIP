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
| Sound-change prose and chapter membership | Reader sources and `sound_changes/registry/reader_files.tsv`, routed by `adjudicate.py SCNNN --prepare` |
| Elaborated lexical prose | `../lexeme_reports/model_entries/*.model.md` |
| Scoped lexical selection/certification | `../lexeme_reports/pgmc_integration/editorial_cases.tsv` and the existing report manifest |
| Bibliography | `docs/refs.bib` |
| Index decisions | `../book/` SOURCE registries and scoped overrides; never distort prose to appease a checker |

`artifact_graph.py` is the sole generated-output owner. Its `--inventory`
lists node kinds, authorities and outputs. `adjudicate.py --refresh` rebuilds
stale products and checks the fixed points; never maintain another builder list.
Class manifests, compact traces, lexical aggregate, reader aggregate, combined
manuscript and index projections are generated.

## Distinct supported presentations

The default class-manifest book consumes the 160 mature models, preserving
their complete arguments and all seven derivation classes. The complete
387-row compact derivation report has a separate selective commentary insertion
route, currently 18 certified narratives with explicit outstanding obligations.
The reconstruction survey covers 393 identities including six research-only rows.
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

## Historical designs and reports

[archive/](archive/) retains the earlier pilot/alpha navigation and the
[pre-implementation design](archive/full_assembly_design.md) verbatim.
Future-tense instructions there describe the old design stage, not missing
implementation. Layout fixtures and published reports are retained where they
still have a distinct purpose; large generated products are not discarded
merely because they can be rebuilt.
