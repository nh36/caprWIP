# SC017–SC019 and Old English *wull*: completed investigation

Start with [the nine-heading scientific report](REPORT.md). Its Verdict
answers the eight research questions and recommends a decision; its Literature
section provides printed-page locators and the actual verification limits.
This is a completed research package, **not an adopted adjudication**.

The investigated baseline is `586ec5f370e58d9038142d330121acf58b085a18`
on `update`, including the completed SC034 adjudication and rust input
migration. The report and original preservation receipts are frozen at
investigation closeout, before the user's subsequent authorization to commit
and push this evidence. Their statements that no release was authorized or
performed describe that closeout, not the later research-only publication.
No production rule, chronology decision, selected input, target, or protected
baseline is changed by publishing this directory.

## Review map

| File | Contents |
| --- | --- |
| [REPORT.md](REPORT.md) | Scientific argument, source comparison, alternatives, recommendation and affected-owner map |
| [measured-summary.json](measured-summary.json) | Compact measured variant results |
| [all_387_rows_all_variants.tsv](all_387_rows_all_variants.tsv) | All 1,935 row/variant comparisons, including unchanged rows |
| [all_changed_intermediates.tsv](all_changed_intermediates.tsv) | Every changed aligned checkpoint |
| [all_paradigm_cells.tsv](all_paradigm_cells.tsv) | All 80 cell/variant results, with source, stage and assembly status |
| [paradigm_all_intermediate_states.tsv](paradigm_all_intermediate_states.tsv) | Complete paradigm checkpoint states |
| [complete_sc017_sc018_sc019_firing_census.tsv](complete_sc017_sc018_sc019_firing_census.tsv) | Complete baseline firing census |
| [composition_and_historical_metadata.tsv](composition_and_historical_metadata.tsv) | All 107 executable positions and distinct historical metadata |
| [pathway.json](pathway.json) | Actual parser and vowel-class diagnostics |
| [independent-equivalence.json](independent-equivalence.json) | Independent prefix, complete-suffix and nested-event comparisons |
| [source-readings-final.json](source-readings-final.json) | Reading and original-image accountability; explicit text-only limits |
| [production-preservation-final.json](production-preservation-final.json) | Investigation-closeout preservation of all 163 protected files |

The six large JSON receipts are stored with deterministic, lossless gzip
compression: `identity.json.gz` and the five `*-replay.json.gz` files. They
retain the complete original JSON bytes, not reduced summaries. For example:

```sh
gzip -dc identity.json.gz | python3 -m json.tool | head -n 40
```

`recipes.json`, `predictions.json`, `stage_map.json` and `wull_fixtures.tsv`
are the original predeclared experimental inputs. `recipes-context-v2.json`
and `context-identity-repair.json` record the private context-wrapper repair
without replacing the original recipes or changing the scientific hypotheses.

The copied preparation packets are `wull-sc017-prepare.txt` and
`wull-sc019-prepare.txt` **in this directory**; the report's `../` references
describe their original session layout. `wull-production-protection-before.json`
retains the original production hash set. No source PDFs, page images, or
full-book extracts are distributed in this package.

## Integrity and execution provenance

`artifact-sha256.tsv` is the unchanged investigation-closeout index of
uncompressed original artifacts. From this directory, verify it without
extracting the large receipts:

```sh
python3 - <<'PY'
import csv
import gzip
import hashlib
from pathlib import Path

with Path("artifact-sha256.tsv").open() as handle:
    for row in csv.DictReader(handle, delimiter="\t"):
        path = Path(row["file"])
        data = (path.read_bytes() if path.exists()
                else gzip.decompress(Path(str(path) + ".gz").read_bytes()))
        assert hashlib.sha256(data).hexdigest() == row["sha256"], path
print("All original artifact hashes match.")
PY
```

`publication-sha256.tsv` additionally hashes every published file in this
directory except itself, including compressed storage bytes, this README and
the supplementary preparation receipts.

The Python scripts are preserved execution provenance, not a newly installed
production runner. Container scripts used `/research` for these artifacts and
`/usr/app` for the private baseline, with the existing repository tools.
`closeout.py` records the original host checkout path. Preparation, repair,
annex and closeout scripts are one-use and deliberately refuse existing
destinations: **do not rerun them over these frozen receipts**. Reproduction
requires a separate private worktree at the pinned baseline, private runtime
copies and a fresh output directory under the established experimental
protocol. The owned research container was stopped at closeout.

The report recommends a separately approved recognition/domain repair and
qualified provisional retention of the executable order. Neither that repair
nor any alternative chronology is adopted by this publication.
