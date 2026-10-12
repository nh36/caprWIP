# Germanic validation capabilities

The Actions job validates **portable** capabilities explicitly. A green portable
job does not certify full local science validation, availability of original
holdings, repeated page-image inspection, or a fresh Foma execution.

## Commands

From the repository root:

```sh
python3 Germanic/tools/run_portable_checks.py
python3 -m pytest -q --validation-mode=portable Germanic/tests
python3 Germanic/tools/pgmc_reconstruction_survey.py --mode portable
python3 Germanic/tools/artifact_graph.py --check --mode portable
```

The runner preflights the survey once, runs bibliography, regression, artifact
graph and index checks, writes complete logs and JUnit results to `.ci-results/`,
and produces the Actions job summary. Scratch files stay inside that directory.
A missing required tracked basis stops at preflight, rather than producing
hundreds of dependent failures.

Strict local defaults have not changed:

```sh
python3 Germanic/tools/pgmc_reconstruction_survey.py
python3 -m pytest -q Germanic/tests
python3 Germanic/tools/artifact_graph.py --check
```

Full survey validation requires **every declared holding**, including excluded
holdings and PDF-only sources. The command verifies actual available input
hashes against recorded provenance. Provision the declared library first;
the pytest suite performs the same holding/evidence preflight once. Completeness
flags such as `--require-feature-alignment-complete` retain their independent
reading, attribution and analytical gates in either mode.

Full graph validation additionally requires the canonical isolated Foma runner,
compiled stage bins and build manifests. Portable mode never executes the
`runtime_bins`, `full_trace`, `lexical_sources` or `interaction_matrix` nodes,
even if local binaries happen to exist. Synthetic runtime-validator tests and
integrity checks over committed runtime receipts still run; these are not new
runtime evidence.

## Portable evidence and provenance

Portable validation requires bibliography keys, declared library-contained
holding paths, readable tracked non-original verification bases, reciprocal
evidence/review links and the existing analytical identity/attribution checks.
The only absence exemption is an **untracked declared original PDF**. An
original PDF used as a historical evidence basis must belong to that evidence's
declared source. Missing tracked PDFs, text bases, unsafe paths and source/hash
regressions remain failures. Stiles1986a/b need not acquire invented text
derivatives: PDF-only declarations are valid.

Historical `page_image_checked` and other verification records are preserved,
not upgraded or rerun. Portable rendering reports unavailable holding paths
explicitly. Available sources are still hashed. Provenance freshness compares
all available input hashes and population/analysis metadata; only declared
unavailable originals are exempt from an impossible current-byte comparison.

Regenerate through the canonical control plane:

```sh
python3 Germanic/tools/adjudicate.py --refresh
python3 Germanic/tools/adjudicate.py --refresh --mode portable
```

The first command remains strict and includes runtime validation/builds. The
second refreshes portable projections only. Its survey provenance identifies
`validation_mode: portable`, unavailable holdings and the fact that image
verification was not repeated. Previously recorded hashes of missing originals
move unchanged into `historical_unavailable_inputs`; a genuinely unrecorded
original has an explicit `null`, never a fabricated or replacement hash.
Current tracked hashes can therefore refresh without original PDFs. Full
validation, once originals are available, compares their real hashes with
those historical values and fails on a mismatch or absent recorded hash.

## Repaired regression authorities

The 2026-10-11 Actions log (run `38177868157`, commit `7848f762`) contained
2453-versus-2456 production and 2365-versus-2368 printable-count failures.
Comparing generated occurrences against the preceding `5beb487c` state traced
the three removed occurrences to the evolved cud model: the old `*kwedu-2`
span and redundant `cweodu`/`cudu` mentions disappeared. Adder and cud source
line locators also moved. This was not an extractor regression.

Frozen historical count dictionaries and scientific baselines remain intact.
Live expectations now derive from the **complete** canonical production
pipeline (including table and broad-prose decisions), with exact occurrence
multisets, print partitions, book/emission joins and regenerated graph freshness
still enforced. The obsolete cud checker sentinel is no longer required in
publication prose.

The historical cud variety-audit locator can rebase read-only from line 32 to
line 39 only when exactly one surviving current occurrence retains an exact
historical `.iv` tag with the same source path, form sort key and variety.
Missing, changed or ambiguous anchors fail; audit evidence and judgments are
not edited.

The graph inventory test omitted the already-existing reconstruction-survey
and lexical-integration projection nodes. Both are now declared in its expected
inventory, with output ownership and archive exclusion checks retained.
Registry/memo agreement now checks registry and memo verdicts directly, rather
than rerunning the entire binary-dependent graph for every adjudicated SC.
`adjudicate SCNNN --check` still performs the full strict propagation check.

An actual dedicated-branch Actions run also exposed an output-introspection
bug: listing the lexical-integration node's owners invoked its full renderer
and unnecessarily required original PDFs. Its output declaration now uses the
integration module's canonical `OUTPUT_NAMES`, without validation or builds.
The renderer and freshness check retain their explicit capabilities. Hidden
`.ci-results/` log uploads are explicitly enabled, with only log/XML/summary
files selected, not scratch directories.

The provenance refresh also exposed two pre-existing stale tracked
reading-accountability hashes; canonical regeneration updates their hashes,
not the evidence. All declared holdings now participate in provenance, rather
than silently omitting nonconsulted declarations.
