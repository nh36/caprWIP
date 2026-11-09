# Repository inventory: preservation and consolidation

This is a non-sensitive overview of the November 2026 inventory and
preservation. Detailed inventories, branch graphs, restricted-holding
manifests and restoration evidence remain in private local audit/backup
storage. This overview does not replace them.

## Verified structure and preservation

The original inventory identified sixteen development checkouts sharing
one Git object database, not sixteen independent backups. It also
identified a separate historical archive clone and non-Git research/archive
collections. Independent historical repositories were not modified.

Eight of the twenty-three remote branches observed in that inventory had
commits outside the then-certified `update`; their histories overlap.
These are dated observations, not current branch counts or redundancy
judgments. Two remote archive-tag objects were unavailable locally;
neither was fetched, and tag-history coverage is not exhaustive.

The nested `source-plan` checkout was reverified at detached
`03d1e58b67cf76a10955d5a74482ac37c8e5bec4`, with 98 modified tracked paths
and three untracked files. Local-only rescue reference
`rescue/source-plan-2026-11-09-03d1e58b` now protects the commit.
Its HEAD, index, working contents and location were not changed.

A separate private backup contains the rescue-bearing bundle, complete
working contents including ignored/untracked material, staged/unstaged
patches, index/status metadata, hash/mode manifest and detailed prior audit.
Isolated restoration reproduced all 4582 files, index entries, dirty status,
hashes and modes. The backup is outside the source worktree but on the
same APFS volume: protection from checkout loss is verified; independent
disaster recovery is not. Restricted holdings and full local metadata
must not be uploaded with repository documentation.

## Prior assignment boundary (historical)

Pandoc-only maintenance fast-forwarded `update` from scientifically
certified `1cb88967` to infrastructure commit `23f6234a`.
Its successful portable CI is distinct from full local certification.
Christiansen source integration and the
[control-pilot review](REGRESSION_CONTROLS_PILOT_REVIEW.md) remain separate
workstreams, not authorization to change selected cells or consolidate.

The preceding preservation assignment approved no worktree, branch,
experimental directory, archive or bundle for deletion, and no pruning,
archive-tag fetch, history rewrite or alteration of independent historical
repositories. The subsequent execution below was separately authorized and
accounts for
unique commits, dirty state, ignored evidence, restricted holdings and
independently verified backups.

## Authorized consolidation executed, 9 November 2026

`update` incorporated the exact certified scholarly commit
`cdad4dde281fec7d9cbfffb952312fcce4b03293` by fast-forward, followed by
documentation-only cherry-pick `771692b09f788588eb52570c129a5a07f639f597`.
The original documentation identity `d99ccb40` remains retained separately.
All other tree entries in the successor are byte-identical to `cdad4dde`.
Its full scientific/publication certificate was verified, not transferred
to the new documentation identity. The successor passed portable validation
and a non-mutating full artifact-graph check.

The registered development worktree count fell from sixteen to six.
Every removed checkout was clean, inactive, unlocked, free of nested Git
repositories and unresolved operations, and at a commit already reachable
from the retained public history. Ignored files were not assumed disposable:
all non-deduplicated local material, including failed receipts, old binaries,
research and scratch results, was privately archived and hash-verified.
Each target and its contents were checked again immediately before ordinary,
non-forced `git worktree remove`. Canonical HEAD, references and shared
object storage were checked after every removal.

| Removed checkout label | Retained exact HEAD | Completed purpose |
| --- | --- | --- |
| sc017-wull-worktree | `586ec5f370e58d9038142d330121acf58b085a18` | Incorporated wool/rust-era research |
| capr-ci-workstream | `fc6ded21a48800b717971355004a20137f8c9774` | Completed CI work; failed and successful logs preserved |
| capr-cleanup-worktree | `abbf68d78f24eda520ab751b704b8d221c2ef6fc` | Earlier integrated architectural cleanup |
| capr-lexical-workstream | `674a76b9785fbf612914757b79779f7da61d03c2` | Integrated lexical graph/publication work |
| capr-sc032-workstream | `68b84e93c3e9c76757b2cd86db9f1b5d0a8db16f` | Completed SC032 integration and errata |
| earthly-sc040 | `637b30dbfa2455f57f3f467088743d73f8b536b9` | Certified, integrated SC040/earthly work |
| nonhigh-four-cells | `ee73f189d2c4af2fab6170f7af066d96611ce749` | Closed blocked-gate investigation, subsequently superseded |
| soul-fulk-oblique | `22de1004cea8829c775ea25c21c07db943d4b8e2` | Archived exact-commit soul research |
| soul-lexical-reassessment | `52a49a8cd5883d20e72312a40ac068f9cdd499fb` | Archived exact-commit lexical research |
| soul-syncope-resolution | `1fb0223ba4b308afe4b72a0dc9cad805ca7f786c` | Archived strict research certification |

The canonical checkout remains active. Compound-secondary-stress and
earthly-regular-cell retain unintegrated experimental commits and their
checkouts. Full-cascade-functionality retains substantial unique formal
and experimental material with path-bound proof inputs. Parser-four-cells
remains because it contains the explicitly protected dirty source-plan.
Neither it nor source-plan was moved, cleaned, reset or removed.

The independent historical checkout is unchanged. One isolated bare
verification repository successfully restored all advertised references of
the four distinct historical bundles and passed full `git fsck`; it is not
a replacement development worktree. All four historical bundles and both
existing rescue/completion bundles were retained. No exact redundant bundle
was established, so none was retired.

The two formerly unavailable archive tags were narrowly fetched after
matching the original and live remote identities:

| Tag | Acquired commit object |
| --- | --- |
| archive/pred-form-annotations-wip-2026-07-31 | `1f027a7393671ee71cf4dbcb6d710f1e67c4b0d2` |
| archive/reader-facing-gloss-audit-wip-2026-07-29 | `e92a7e5fdac53bb53eb18cbf86c40f42d1b54c06` |

Eight unattached, fully integrated local branches were deleted with ordinary
`git branch -d`: maintenance/pandoc-ci-provisioning,
integration/earthly-sc040, integration/nonhigh-four-cells,
review/sc112-checkpoint, review/sc112-final-integration,
review/sc112-lexical-publication, sc001-sc020-chronology-audit and
wip/syncope-consolidation-review. Their commits remain reachable.

No remote branch was deleted. After review, the same integrated remote
branches except local-only review/sc112-final-integration are candidates
for retirement; preserve their historical identities first. The four index
experiment branches, compound-secondary-stress, earthly-regular-cell and
the supplementary HVD closeout still carry distinct histories. Keep those,
the exact scholarly/certification references and the source-plan rescue.
The original documentation branch is cherry-pick-equivalent, not an ancestor,
and is deliberately retained for provenance.

The source library lost 1039 exact duplicate worktree paths, not distinct
originals or derivatives; see [holding policy](references/README_resources.md).
The main library and frozen recovery copies remain verified and unchanged.
Detailed original audit, before/after inventories, manifests, removal records
and private receipts remain locally available. No existing scientific tools,
historical tests, protected baselines or evidence were deleted or rewritten.

No mounted independent backup destination was available. The configured
TimeMachine destination could not mount; local snapshots and additional
directories on this APFS volume do not provide independent disaster recovery.
That limitation remains explicit for every new private recovery package.
The provisional controls and lazy dart selector remain deferred.
