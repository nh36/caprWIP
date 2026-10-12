# Architectural cleanup migration record

Baseline: `c06c896da21f50df756d91c9f5729511b910b8c9`. This records a repository
migration, not a scientific verdict, new editorial policy or current task queue.
Use `../README.md` for current routing.

## Preservation and accounting

The lexical archive mirrors the old lexical-root-relative paths. No migrated
document was shortened, corrected or certified anew. The audit is reproducible:

```sh
python3 Germanic/tools/check_repository_cleanup.py --check
python3 Germanic/tools/artifact_graph.py --inventory
python3 -m pytest -q --validation-mode=portable Germanic/tests/test_repository_cleanup.py
```

The first command emits exact old/new paths and original Git blob IDs, checks
archival bytes, and compares protected cleanup SOURCE against the baseline.
It is a migration check, not a permanent prohibition on separately authorized
future scientific or publication changes. The recurring tests protect archived
history and mechanically validate live models without freezing future prose.

| Collection moved verbatim | Files | Treatment |
| --- | ---: | --- |
| Paired model checklists | 151 | Historical qualifications retained, not active drafting obligations |
| Paired model implementation reports | 151 | Correction and failed-claim history retained |
| Model production/pilot batch reports | 24 | Historical reports, not current instructions |
| Writing-skill rollout/creation records | 2 | Historical workflow |
| Development-note slices and indexes | 390 | Historical arguments, including unresolved and rejected hypotheses |
| Lexeme packet snapshots | 152 | Historical evidence snapshots; fresh packets remain available on demand |
| Research-memo batch summaries | 36 | Historical summaries; individual research memos remain active |
| Lexical-root implementation reports | 2 | Historical workflow |
| Superseded navigation/design originals | 5 | Three lexical and two assembly records |

Thus 908 collection files were moved and five navigation originals were
preserved, for 913 exact old/new archival pairs. The 160 mature models, 156 source
ledgers and 153 individual research memos remain active. Collection-wide heading
inspection found qualifications in 150 checklists and 139 implementation
reports; these mixed documents were not assumed to be disposable. Successive
adder locator corrections illustrate why old claims and their corrections
must survive together.

Active lexical Markdown falls from 1,423 files to 518. Active lexical files of
all types fall from 1,575 to 669. This is a reduction in active paperwork, not
913 deleted scholarly records or a reduction in the size of the evidence base.
Tracked files increase from 3,866 to 3,876: this includes the short replacement
navigation, preserved originals and executable checks, rather than disguising
archival moves as deletion. The command above derives tracked-file counts and
excludes unrelated untracked files; it is not a second editable inventory.

Historical inline references retain their original context. Resolve them
relative to the old location, then apply the mirrored archive mapping; the
complete original context remains available through `git show c06c896d:PATH`.
This does not claim every preserved historical relative link is directly
clickable at its new location. Current navigation links resolve, and the
generated population crosswalk retains stable-ID links to archived packets,
development notes and row-level review records.

No source ledger was retired: diplomatic readings, image-verification records,
printed-page/extraction-sheet distinctions, Toller Supplement attribution,
rejected readings and confidence qualifications remain with their owners.
The survey SOURCE tables and reading receipts are unchanged. Archival process
records no longer influence active drafting diagnostics; archived development
notes and packets remain discoverable supporting evidence, not certification.

The accidentally tracked operating-system file is untracked, not scholarly
content. The tracked session plan is preserved verbatim as
`legacy-mechanistic-buckets-plan.md` in this directory; future session-state
files are ignored. The Celtic backup, old Germanic dataset backup and historical
binary backup are retained: their provenance is historical, and this cleanup
does not assert that they are safely reproducible disposable files.

## Implemented simplifications

Current navigation replaces the accumulated survey checkpoints, obsolete
production backlog, stale resumption plan and future-tense assembly design.
Their original bytes remain archived. SC032 is complete; the registry-derived
next case is SC034, which this task does not investigate.

New lexical drafting uses one shared human checklist plus executable
metadata/bibliography/publication checks. It does not create another completed
checklist and implementation report per word. Unique judgements and limitations
belong in the source ledger or existing research memo; automation cannot
certify image inspection, source attribution or scholarly adequacy.

The default remains `build_capr_book_draft_docker.sh`, with the mature-model
lexical presentation. The complete 387-derivation insertion route, 18 certified
narratives and optional compact-prose presentation retain their distinct
purposes; none replaces the default or promotes further essays.

The default combined Docker path refreshes once instead of three times.
Both nested renderers use `--check-fresh`, which runs the strict graph check
and refuses stale sources. Standalone invocation without the flag still
refreshes. The optional strict-index branch retains its additional strict
operation and subsequent refresh. Supported standalone PDFs are retained:
removing their rendering would change the wrapper's existing output contract,
not merely eliminate duplicate graph regeneration.
Common semantic, bibliography and index checks now run before the child PDF
renders, so a failing shared gate does not waste two standalone renders.

The graph inventory is derived from actual node/output declarations, with no
second builder list. Tests permit additional valid nodes while requiring the
existing capabilities, unique names and output ownership, authority labels,
valid node kinds, declared output coverage and archive exclusion. Fixed-point
logic and portable/full runtime distinctions are unchanged.

Large generated ledgers, comparison maps, traces, manifests, index projections
and rendered products remain tracked where they were tracked before. They have
real validation, review and provenance consumers; size is not proof of
redundancy. The legitimate discovery deltas are the crosswalk's archived paths
and the coverage audit's exclusion of process records, not scientific or
editorial reclassification.

## Release verification

The initial portable baseline passed 1,319 tests and 7,360 subtests with one
runtime-gate skip. Investigation then exposed a capability leak: on a
provisioned machine, older availability-based live tests still executed during
that portable invocation. All live-probe tests now carry the explicit runtime
marker, and portable selection skips the entire category regardless of local
Docker/binary availability. Full mode retains those probes and the strict
runtime gate. Targeted capability checks pass with the runtime actually present.

The complete full-mode cleanup run passed 1,327 tests and 8,437 subtests and
found two navigation assertions: the shortened routing omitted its executable
name, and the survey test pinned a heading moved into history. Both are repaired
without changing scientific evidence. The full-mode follow-up passed all
11 selected repaired/new checks. The complete suite exercised the live evidence
rebuild and strict runtime test, not just persisted receipts.

Strict survey validation passes with actual local holdings and recorded hashes;
the clean checkout's strict command fails at the missing Orel original PDF.
The independent three-source completion limitation remains explicitly
Ringe-Taylor identity/conventions verification, not a suppressed validator
error. No original page images were reinspected.

The standard book build exposed a pre-existing semantic fingerprint residue:
`*kwedu-2` had been removed from the cud model by released `ea5974c1`, but its
removal was absent from the existing semantic-index allowlist. One exact
source/form/role/scope removal now records that released correction. The frozen
snapshot and current model remain unchanged; a negative regression proves that
removing this narrow allowance still triggers the fingerprint error.
The 13-test final publication/migration selection passes with 1,085 subtests.

The next render attempt reached the released SC032 chapter and exposed three
paragraph-gloss false positives. Long *īo* is sound notation, not a lexical
word. The explicitly paired *hēafud* variant shares the preceding *hēafod*
'head' gloss in that paragraph. The validator now recognizes the notation and
has one contextual shared-gloss allowance requiring the already-glossed anchor
in the same paragraph; missing anchors, other contexts, later glosses and
Part II remain failures. ASCII case folding no longer corrupts UTF-8 under a
non-ASCII locale. The reader's bytes are unchanged. All 11 gloss regressions
pass, and the complete assembled manuscript has zero gloss violations.

The clean-worktree portable runner passed every stage: survey, bibliography,
regression, graph freshness and index checks. Its regression stage passed
1,298 tests and 8,412 subtests, with 33 explicitly skipped tests. Subsequent
runtime-marker and publication refinements passed 98 tests and 1,099 subtests
with 28 runtime skips in that same unprovisioned checkout; the final gloss,
publication and migration selection passed 24 tests and 1,112 subtests.
Final clean-checkout survey, graph and index checks also pass without refresh.
These focused selections overlap and must not be added to the full-run totals.

The preservation audit checks 962 protected baseline files and all 913 archival
pairs with zero errors. This includes every model and source ledger, survey
evidence/reading receipt, individual research memo, scientific dossier, corpus/
stage/context owner, verdict, chronology relation and frozen migration record
selected by the documented audit predicate.

The final standard combined build succeeds without bypasses and produces a
305-page PDF. The previous combined artifact was the 302-page October 4 render;
the combined Markdown and lexical aggregate are byte-identical to the cleanup
baseline. The new PDF therefore renders already released SOURCE, including
SC032 and lexical integration, rather than newly adopted science or prose.
Standalone introduction, lexical and sound-change PDFs were also rebuilt;
their layout-text extractions are identical to the baseline, so incidental
PDF metadata and repeated console-log differences are excluded from the commit.

Actual page inspection covers SC032 (printed pp. 69--70), adder (p. 121),
knee's selected dative and trace (p. 252), and the native/reconstruction index
(pp. 298--302). Chapter openings, you/thought/hue and bibliography were also
checked in extracted PDF text. Quantities, diacritics, rule blocks and printed
source locators are readable. All 3,577 internal PDF links target valid pages;
SC032, breaking, glide and medial-lowering links resolve to their actual rule
pages, and sampled index links account for the two preliminary pages.
No replacement character or unresolved `??` occurs in the extracted text.
This is representative inspection, not a new scholarly review of every page.

The build passes semantic, bibliography, locator, occurrence-parity, index,
heading-wrapping and 18 negative-architecture checks. Standalone lexical output
still warns about links to sound-change chapters absent from that standalone
document; those destinations are present in the combined book. Final strict
survey and full graph checks pass. Original holdings were not reinspected,
the independent Ringe-Taylor conventions gap remains, and no new scientific
experiment was run beyond the full suite's existing live evidence checks.

The principal cleanup batches are `9d307fe9` (navigation), `9a16eba4`
(per-model paperwork), `ced81fa1` (historical research), `2595c818`
(ownership/build consolidation), `415f89c6` and `4bea62a9` (portable runtime
boundaries), `698d782e` and `343d0ff7` (routing/provenance checks),
`ba43e145` (exact semantic-index residue and fail-fast rendering), and
`82af7942` (source-preserving gloss validation).

## Decisions deliberately not taken

No FST, input, stage/context, historical verdict, chronology, frozen fingerprint
or approved migration is changed. No model is abridged, report promoted,
scholarly disagreement resolved, original PDF uploaded or historical hash
invented. SC034, further Anglo-Frisian research and broader lexical-catalogue
editorial design require their own scientific/editorial authorization.
