# Proto-Germanic reconstruction survey

Start here for source verification and reconstruction research. The completed
49-tranche programme aligned all 393 survey identities, including the six
research-only rows without runnable targets. The live sound-change corpus has
387 runnable rows. Neither completed alignment nor `bounded_limit` establishes
a settled history, an important scholarly disagreement, or permission to
change the selected reconstruction.

## Editable authorities

| SOURCE | Owns |
| --- | --- |
| `sources.tsv` | Bibliography/holding identities, conventions, consultation mode and limits |
| `forms.tsv` | Diplomatic forms and process evidence, printed pages, source arguments, verification and independent confidence |
| `coverage.tsv` | Actual consultations, evidence links, search basis and assessments |
| `review_targets.tsv`, `reading_scopes.tsv` | Finite commitments and screened/read passages; a schedule is not a consultation |
| `reading_accountability/` | Applicability manifests, original-page checks, exact occurrence spans and reversible amendment receipts |
| `analyses.tsv` | Evidence-linked row/cell identity, attribution, stage interpretation and supported features |
| `comparisons.tsv` | Scoped comparisons, alignment, comparability, explanations and missing premises |
| `rationales.tsv` | Cited position support, descriptive bridges and explanations of divergence, kept distinct |
| `commentary.md` | Scientific synthesis and open questions |

Live `PROTO`, `PROTOFORM`, stage/context and derivation class come from
`Germanic/data/`, not these research tables. Shared source evidence may support
several rows without making their cells interchangeable. Dictionary notation,
source dating, analytical interpretation, confidence and page-image verification
are separate axes. A quoted or rejected theory is not an author's endorsement.
Never assemble an ending onto a stem and attribute the whole word to its author.

The authorized wether adoption selects row 2283's masculine nominative singular
`*wéθruz` in both live reconstructed fields (Orel 2003, pp. 459–460;
Kroonen 2013, p. 584). Orel's `*weþraz` remains an alternative. Current
assessments and commentary reflect the adoption; the tranche-44 receipts
and earlier SC015 experimental report retain their historical inputs.
See the lexical source ledger and supplementary `sc015-adjudication.md`;
no SC015 sound-law verdict or rule change is implied.

The generated inventory, ledger, comparison map, coverage, priorities,
reading progress and provenance are views, not editable authorities.
The exact output declaration comes from
`python3 Germanic/tools/artifact_graph.py --inventory`; regenerate only with
`python3 Germanic/tools/adjudicate.py --refresh`.

## Validate and query

Run from the repository root:

```sh
# Portable integrity: absent untracked original PDFs are explicitly unverified.
python3 Germanic/tools/pgmc_reconstruction_survey.py --mode portable

# Strict local integrity and recorded holding hashes.
python3 Germanic/tools/pgmc_reconstruction_survey.py

# Completed bounded alignment, not resolution of every historical question.
python3 Germanic/tools/pgmc_reconstruction_survey.py --require-feature-alignment-complete

# Validated, read-only in-memory SQLite; no second editable database.
python3 Germanic/tools/pgmc_reconstruction_survey.py --mode portable --query \
  "SELECT alignment_status, count(*) FROM comparisons WHERE scope='core_triage' GROUP BY alignment_status"
python3 Germanic/tools/pgmc_reconstruction_survey.py --mode portable --query \
  "SELECT a.row_id,f.source_key,f.printed_pages,a.analytical_form FROM analyses a JOIN forms f USING(evidence_id) WHERE a.row_id='2085' ORDER BY a.analysis_id"
```

`--require-core-complete` checks dictionary dispositions;
`--require-analysis-complete` adds core triage;
`--require-three-source-complete` checks the distinct reading programme.
The latter still refuses the declared Ringe-Taylor identity/conventions gap.
`--require-complete` is the composite gate. Do not remove that gap or lower a
gate to label the survey wholly verified. Portable validation preserves previous
image-check records; it does not repeat those checks. PDF-only holdings are valid.
See [validation capabilities](../../../../docs/CI_VALIDATION.md).

Use actual printed folios, not extraction-sheet numbers or a global offset.
No source record means no recorded consultation, not author silence. Failed
text searches do not prove absence. Further reading must address a named
missing premise; the old bibliography-by-row Cartesian workload is obsolete.

## Publication and history

The [editorial integration](../pgmc_integration/README.md) assesses significance
independently of derivation success. Its `editorial_cases.tsv` owns scoped
publication decisions; the [report schema](../report_schema.md) owns selection
policy. Model prose and source ledgers remain separate from this survey's
evidence. Scientific adoption requires the existing adjudication protocol.

The [verbatim pre-cleanup README](../archive/pgmc_reconstructions/README.md)
preserves all tranche narratives, historical measurements and earlier commands
from `c06c896d`, including their then-current/uncommitted claims. They are history,
not current instructions. Exact receipts remain in `reading_accountability/`,
and the [survey audit](../../sound_changes/audits/pgmc-reconstruction-survey.md)
retains the scientific work record. Never rerun a persisted one-use alignment
candidate or recreate its immutable preparation.
