# Repository inventory: preservation before consolidation

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

## Boundaries, not approved restructuring

Pandoc-only maintenance fast-forwarded `update` from scientifically
certified `1cb88967` to infrastructure commit `23f6234a`.
Its successful portable CI is distinct from full local certification.
Christiansen source integration and the
[control-pilot review](REGRESSION_CONTROLS_PILOT_REVIEW.md) remain separate
workstreams, not authorization to change selected cells or consolidate.

No worktree, branch, experimental directory, archive or bundle is approved
for deletion. No pruning, archive-tag fetch, history rewrite or alteration
of independent historical repositories belongs to this assignment.
Future cleanup needs a separately reviewed retention plan accounting for
unique commits, dirty state, ignored evidence, restricted holdings and
independently verified backups.
