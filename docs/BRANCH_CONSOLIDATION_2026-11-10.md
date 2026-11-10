# Approved branch consolidation and retirement inventory

## Scope and integration identity

This is a Git-history inventory, not a scientific adjudication or a
filesystem-reorganisation authorization. No remote branch is deleted by
this assignment. No experimental implementation is adopted.

The approved integration is the two-parent merge
`dbfa22cb93046e5775bf4f56276aef3ceeb3dac4`:

```text
771692b09f788588eb52570c129a5a07f639f597
|\
| 6b855f3f42525c680f8d209470bad178f06551d4  little scholarly integration
| 2beb1856aeae01e087a4528b2522b6344bbc4749  dependent metadata checks
10e6a2f5234ed5751efa94e1502a1466ec03ed61  navigation
45794ad51eb5df72007addd55c9a97e6c9945efb  private-holdings consolidation record
fa8e6f9ab1cbaf06679dea8b00b2c6e4c4b2510b  worktree/recovery record
|/
dbfa22cb93046e5775bf4f56276aef3ceeb3dac4  ordinary merge
```

`update` first fast-forwarded and was normally pushed to `fa8e6f9a`.
The merge parents are, in order, `fa8e6f9a` and `2beb1856`; all five
original commits retain their identities. The only conflict was adjacent,
independent additions to `docs/references/README_resources.md`. Both
sections were retained verbatim. Relative to the certified little tip,
the merge changes only the six cleanup documentation paths; every other
tracked blob, including scientific inputs, bibliography, source intake,
lexical article/ledger, generated publications and dependent tests, is
identical. The other five cleanup files also match their approved tip.

The administrative commit containing this inventory is a descendant of
that merge. The final tested and published `update` SHA and execution
results are recorded in its closing GitHub commit comment, not inferred
from an older certificate. Resolve the current published ref with
`git rev-parse origin/update`; the integration merge above is immutable.

## Inventory method and categories

All 27 remote branches were fetched and enumerated. The tables below cover
the 26 non-authoritative names; `update` is the authoritative integration
branch described above. Comparisons use `dbfa22cb`, with no intervening
scientific changes in the administrative inventory commit.

For each branch, the unique-commit set is `update..branch`, not its whole
historical log. An ancestral branch's merge base is exactly its listed
tip and its unique-commit set is empty. Non-ancestral branches were also
checked with stable patch IDs, `git cherry`, and file-level comparisons.
The appendix enumerates every non-ancestral unique commit. Shared
experimental commits are not counted as independent discoveries.

Categories:

- A: fully incorporated by ancestry; no outstanding branch contribution.
- B: equivalent but not ancestral; preserve the original identity as well
  as its incorporated replacement.
- C: preserved experimental or historical material; not a production change
  awaiting automatic integration.
- D: potentially useful outstanding development work requiring a separate
  architectural review; not approved for adoption.

Totals excluding `update`: 18 A, 3 B, 4 C, 1 D.

### A — fully incorporated

For every row here, merge base equals the exact tip and unique commits = 0.
Retirement concerns the remote name only. The commit and all its ancestors
remain reachable through `update`; local worktrees and evidence are separate.

| Remote branch | Exact tip (= merge base) | Purpose and disposition |
|---|---|---|
| `family-evidence-audit` | `5bdd732aa400d64483da4b72a990da5c743afb04` | Earlier family-evidence audit; incorporated historical work. |
| `historical-cascade-order` | `d704a94ce8566d988922e461d017aaef6d766579` | Earlier chronology/order work; retain its historical context, not a new order proposal. |
| `integration/earthly-sc040` | `637b30dbfa2455f57f3f467088743d73f8b536b9` | Adopted earthly/SC040 integration and historical evidence closeout. Its evidence commit is not the tested candidate; retain that distinction. |
| `integration/nonhigh-four-cells` | `ee73f189d2c4af2fab6170f7af066d96611ce749` | Completed selected-cell integration. |
| `integration/parser-four-cells` | `c1cfd0a5b2c3dbdefa18da32d05bb229e02543c0` | Completed parser/cell integration; retained checkout and nested dirty source-plan remain protected. |
| `maintenance/pandoc-ci-provisioning` | `23f6234a6074cfb051d6651617229b68cc6b0d2e` | Approved pinned-Pandoc CI repair; portable certification only. |
| `maintenance/repository-consolidation-2026-11-09` | `fa8e6f9ab1cbaf06679dea8b00b2c6e4c4b2510b` | Three approved documentation commits, integrated by fast-forward. |
| `research/christiansen-2018-scytel` | `cdad4dde281fec7d9cbfffb952312fcce4b03293` | Completed source integration; preserve exact certified identity. |
| `research/full-cascade-functionality` | `46956200397c7002bcffb68da6b429b630fcf0a1` | Completed functionality integration; retained checkout and private evidence are not redundant files. |
| `research/high-vowel-deletion-fulk-goering` | `99b1d2e919a191910e8e6df5ef4b138e9bad4de1` | Adopted HVD work and historical certification state, not an outstanding proposal. |
| `research/little-etymology-source-review` | `2beb1856aeae01e087a4528b2522b6344bbc4749` | Both certified scholarly commits incorporated unchanged by merge. |
| `research/soul-fulk-oblique` | `22de1004cea8829c775ea25c21c07db943d4b8e2` | Historical soul investigation; subsequent accepted history is already on `update`. |
| `research/soul-lexical-reassessment` | `52a49a8cd5883d20e72312a40ac068f9cdd499fb` | Completed reassessment incorporated. |
| `research/soul-syncope-resolution` | `1fb0223ba4b308afe4b72a0dc9cad805ca7f786c` | Completed resolution incorporated. |
| `review/sc112-checkpoint` | `5a3fced14d616ccaef5d703278d5cba2ffbca5cb` | Historical SC112 review checkpoint. |
| `review/sc112-lexical-publication` | `4dc907dd69a6090fa11757f3c2207ce5259367a9` | Completed SC112 lexical publication. |
| `sc001-sc020-chronology-audit` | `d084728d7d58a5f9b0311655337803586b84c242` | Completed earlier chronology audit. |
| `wip/syncope-consolidation-review` | `ec6cecdf4a4aa52f35d7a0d4a86608562cf98d9c` | Historical collaborator checkpoint; later adopted consolidation is already incorporated. |

### B — equivalent but not ancestral

Each row has exactly one ancestry-unique commit, its listed original tip.
There is no unmatched substantive patch. Preserve original refs until
archival references/bundles have been approved and verified.

| Remote branch | Original exact tip / unique commit | Exact merge base | Incorporated replacement |
|---|---|---|---|
| `maintenance/post-audit-preservation-controls-review` | `d99ccb404002ad2681059df191a51f926a8da73f` | `23f6234a6074cfb051d6651617229b68cc6b0d2e` | `771692b09f788588eb52570c129a5a07f639f597` |
| `research/compound-secondary-stress` | `29ec734406d2bf1714d37a41980d453c7a4872aa` | `3cb109c981c8868bf383172e2be06cdc88c00fb0` | `164b071c91ca7b3ca7a24734df95e06f97ee292e` |
| `research/earthly-regular-cell` | `7215497ba5cdc2a1b8bef6303cb8c1bf4e9e13f2` | `8f7713c39f26a7f81ef04d29d54070f1b83ab0e0` | `25b48b93f639d556086cb6ac7c8f8d30be5d9210` |

The original documentation commit and its cherry-pick have stable patch ID
`8d72077b77052f1caedca97345824dea66ec253a`.
`REGRESSION_CONTROLS_PILOT_REVIEW.md` remains byte-identical between those
commits; the inventory document subsequently acquired the approved cleanup
additions. No duplicate merge is needed.

The compound-stress pair has stable patch ID
`a9221d70d091d406fb1d89108697db8877ef5c41`; all 11 original packet files
are still byte-identical on `update`. This preserves a distinct experiment
as research, not adoption of its proposed operations. Its original scope,
qualified verdict, source holdings and compressed results remain intact.
The retained research worktree and its ignored files must not be removed.

The earthly pair has stable patch ID
`388b966dc40b880d7731ccaccffeb94b030e8798`; all 18 packet files are
byte-identical on `update`. This is not a missing alternative analysis.
The later, separate adopted weak-neuter cell is recorded by
`1058d9f4256c29b5eea10d26ff840e48392d105e`, followed by publication and
SC040 certification. The earlier packet retains its research-stage gates
and fallback evidence; it does not override the adopted selection.
Its retained checkout and ignored evidence remain protected.

### C/D — non-equivalent historical material and outstanding architecture

All four index branches share exact merge base
`7dad371905f96b87aa67c4c9c0a7e19a0a5581c7`. The appendix's I-numbers
identify their full ancestry-unique commit sets.

| Remote branch | Category | Exact tip | Unique commits | Disposition/preservation |
|---|---|---|---|---|
| `index-iv-anchor-shadow` | C | `480228db93393fb160fbba64b28264f330228065` | I1-I4 (4) | Intermediate anchor migration, including production-mode experimentation despite the name. Preserve original tip; contained in the later index chain. |
| `index-explicit-plan-shadow` | C | `3cd5d7ba0460a52e72e8eecef62599f52d4792eb` | I1-I5 (5) | Intermediate explicit-plan shadow experiment; contained in the later chain. Preserve distinct experimental identity. |
| `index-explicit-plan-production` | C | `b604598ab7642078fad25b2ab2f8be5ae849abf4` | I1-I8 (8) | Later explicit-plan activation/hardening experiment, not current approved production. Preserve its exact tip and checks. |
| `index-broad-prose-placement-shadow` | D | `8c1f2d47d3d045a4c28d74cecc56fe340ec6b337` | I1-I14 (14) | Most complete surviving architecture proposal, including all three earlier tips. Retain pending an actual review; do not merge its stale implementations or publications. |
| `research/hvd-lexical-regression-closeout` | C | `08a3e30663a93d788adfe67254dfef4541468adc` | Its tip alone (1) | Historical exact-state certification evidence. Merge base `1cb8896765fb304fee35139fc9d6b788d04d32ce`. Preserve the evidence with that tested state, not as a current certificate. |

#### Individual index findings

The four branches are a nested experimental chain, not four independent
implementations. Every one of their 14 distinct commits is unmatched by
`git cherry` against current `update`. Their code is not an equivalent
replacement already incorporated under different commit IDs.

Current `index_verborum_README.md` explicitly documents the central Python
occurrence/emission planner plus two emission paths: Lua for visible
explicit spans, Python heading/line injection for non-explicit entries.
It still lists generated anchors, unified final emission, passage-adjacent
placement and TeX occurrence logging as deferred. Therefore it would be
incorrect to declare these experiments wholly superseded by a newer
production implementation merely because their base is old.

The first three experimental stages are superseded within the experimental
chain by `8c1f2d47`, not by an adopted production architecture. Their common
requirements already served by production include central command planning,
book-specific occurrence/emission views, collapse policy and parity checks.
Do not install duplicate owners for those responsibilities.

The unique potentially useful increments, requiring separate review, are:

- `index-iv-anchor-shadow`: generated semantic anchors resolving centrally
  planned commands in Lua, with raw/anchor parity controls.
- `index-explicit-plan-shadow`: a complete per-occurrence emit/suppress plan,
  explicit suppression reasons and shadow semantic checks.
- `index-explicit-plan-production`: fail-closed plan-driven visible-span
  handling and bypass removal; evaluate against today's span semantics and
  historical-stage/variety metadata rather than importing its older versions.
- `index-broad-prose-placement-shadow`: reversible passage-adjacent placement
  using resolved source-block identities, three-pass shadow pagination
  comparisons and exact index-key impact analysis. Its own production
  activation remains review-gated.

These are architectural candidates, not approved improvements or current
validation claims. Old page counts, occurrence counts and line locators are
snapshot observations. The broad branch also changes a historical knob
article and generated volumes; neither those old scholarly bytes nor old
publication outputs should be merged to obtain an infrastructure idea.
TeX-level occurrence/emission logging was still deferred there, not a
finished feature hidden in a branch.

#### HVD historical evidence finding

The unique closeout adds 31 files, all absent at the integration merge,
under `sc063-lexical-coverage-final-certification/`. Its manifest verifies
all 30 listed payloads. All five authentic original A/B/C execution
receipts verify with historical-source checking; their tested HEAD is
`1cb8896765fb304fee35139fc9d6b788d04d32ce`, with successful exit codes
and no source drift. Serial C records 1967 passing tests, 9795 passing
subtests and five intentional historical skips; exclusive C records 26
passing tests. The archive commit itself was never the C-tested candidate.

This is genuinely additive preservation evidence, not a missing scientific
implementation. Its receipt-bound original paths, logs, JUnit, sealed journal
and visual/publication record belong to that historical state. Subsequent
Christiansen/little source integration means it cannot certify today's
publication state.

The narrow discoverability integration is this immutable
[historical evidence link](https://github.com/nh36/caprWIP/tree/08a3e30663a93d788adfe67254dfef4541468adc/Germanic/docs/sound_changes/audits/sc063-lexical-coverage-final-certification),
paired with the
[exact-candidate certificate](https://github.com/nh36/caprWIP/commit/1cb8896765fb304fee35139fc9d6b788d04d32ce#commitcomment-208920923).
Retain the branch until a named archival reference and verified bundle
protect `08a3e306` and identify its relationship to `1cb88967`. A future
decision to import the directory should be a historical-archive operation
retaining those identities, never a current-state validation event. No such
import or merge is performed here.

## Retention and proposed retirement inventory

No remote names, local branches, worktrees or old tags are deleted, renamed
or force-updated. In particular the original local rescue ref
`rescue/source-plan-2026-11-09-03d1e58b` remains at
`03d1e58b67cf76a10955d5a74482ac37c8e5bec4`.

Proposed retirement, after review:

| Group | Specific names | Required preservation before retirement |
|---|---|---|
| 18 incorporated names | Every branch in table A, exactly as individually named there. | Verify each tip is still reachable from retained `update`; preserve scientific/publication checkpoint identities and existing tags. The associated local working directories are not authorized for removal. |
| 3 equivalent originals | `maintenance/post-audit-preservation-controls-review`; `research/compound-secondary-stress`; `research/earthly-regular-cell`. | Annotated archival refs at the three original tips, recording the exact replacement pairs above, plus verified Git-bundle coverage. Keep the two retained research worktrees and their contents. |
| 3 intermediate index labels | `index-iv-anchor-shadow`; `index-explicit-plan-shadow`; `index-explicit-plan-production`. | Preserve annotated experimental-stage refs; verify all three tips are ancestors of retained `index-broad-prose-placement-shadow` and covered by the bundle. This is label consolidation, not adoption. |

Thus 21 names are substantively redundant to `update`, and another three
are intermediate labels recoverable through the retained experimental
chain. This is a proposed 24-name retirement list, not deletion authority.

Keep the following remote names for now:

- `update`: sole authoritative approved integration branch.
- `index-broad-prose-placement-shadow`: parked architectural-review history,
  not a presently authorized production-development task.
- `research/hvd-lexical-regression-closeout`: historical certification evidence
  pending a reviewed archival-reference arrangement.

For a future archival operation, annotated tags should point to original
commits rather than squash summaries. Tag messages should identify purpose,
experimental/adopted status, replacement/equivalence where applicable and
the exact candidate to which receipts apply. A private Git bundle should
contain all proposed archival refs and important certification/publication
refs, pass `git bundle verify`, and be restored into a separate verification
repository with exact-tip and reachability checks. Bundles do not preserve
dirty/untracked/ignored files; those require the existing distinct worktree
preservation process. This report does not initiate a new backup migration.

All six existing worktrees remain in place. The five non-primary checkout
HEADs, index hashes, changed-file content hashes and ignored-file listings
were captured privately before integration. The detached source-plan status
remains 98 modified tracked paths plus three untracked files. A clean branch
tip elsewhere is not permission to remove any of this material.

Existing local archive/publication/rollback tag objects were inventoried
without changing them. The local
`publication/syncope-before-consolidation-2026-11-07` tag is not advertised
by the remote; it must remain locally protected rather than being assumed
to have an independent remote copy. Its annotated object is
`923e919afac3943fc39176d5f78ed80f7bcf6753`, targeting
`b58e7af59d5675fb2c01a2f5acc2b8b15148d2b6`.

## Certification identities and closing validation

| State | Evidence and scope |
|---|---|
| `1cb8896765fb304fee35139fc9d6b788d04d32ce` | Exact HVD scientific/publication candidate; authenticated historical A/B/C receipts and linked certificate above. `08a3e306` preserves evidence, not a second exact-state pass. |
| `cdad4dde281fec7d9cbfffb952312fcce4b03293` | Historical Christiansen scientific/publication certificate: [commit comment](https://github.com/nh36/caprWIP/commit/cdad4dde281fec7d9cbfffb952312fcce4b03293#commitcomment-208953202). |
| `fa8e6f9ab1cbaf06679dea8b00b2c6e4c4b2510b` | Approved documentation-only cleanup; [successful Actions](https://github.com/nh36/caprWIP/actions/runs/42681567758). Not a new scientific certificate. |
| `2beb1856aeae01e087a4528b2522b6344bbc4749` | Little exact-state A/B/C receipts authenticated before switching branches: 1967 tests, 9795 subtests, five historical skips, then 26 exclusive tests. [Successful Actions](https://github.com/nh36/caprWIP/actions/runs/42726814470); strict indexed publication was certified for this state. |
| Final administrative descendant of `dbfa22cb` | New combined-state checks and exact tested SHA belong in its own closing execution record. Earlier certificates are historical evidence, not silently transferred here. |

The final candidate is subject to fresh focused tests/reader semantics,
both canonical Level B commands, the portable runner, full serial and
exclusive Level C, and publication/bibliography/index integrity checks.
Complete command receipts, original exits, source identities, logs and JUnit
remain in the private branch-consolidation validation directory; the closing
commit comment identifies the tested SHA and actual results. Successful
portable Actions for that SHA is recorded separately from strict local C.
The strict lanes run sequentially; no optional xdist experiment is needed.

The combined publication can reuse the already typeset little PDFs only
because all their source, toolchain inputs, Markdown, TeX and PDF bytes are
unchanged. This is publication-artifact identity, not transfer of an
exact-commit scientific certificate or a claim of repeated page-image
inspection. No historical baseline or assertion is relaxed.

The selected little input remains *lūtilō*, with Old English *lȳtelu*;
the distinct root-vowel series and the accounts of Meillet, Krogmann,
Heidermanns, Levitsky, Melazzo and Lühr remain in their certified text.
There is no new Proto-Germanic vowel law, corpus admission, selection change
or sound-law edit. The recorded population remains 394, with 386 matches
and the same eight inherited mismatches.

## Genuinely outstanding work, not branch names

The sole substantive unadopted development candidate discovered here is
the index architecture chain, requiring review and current-state replay
before any future implementation decision. HVD supplementary receipts
need archival-reference policy, not scientific adoption. Original
compound/earthly packets need provenance preservation, not another merge
or reopening of accepted lexical selection.

The source-specific access/interpretive qualifications already stated in
the mature lexical articles remain qualifications, not new branch tasks.
No new sound-law investigation is authorized by this inventory.
The HVD/dart selector, optional regression-control register, filesystem
umbrella move, archive relocation and external-drive migration remain
unimplemented and outside this assignment.

## Appendix: exact index unique commits

| ID | Exact commit | Historical purpose |
|---|---|---|
| I1 | `f03aa5352d41252368fe2f196c4dcf4604b4a2e6` | Introduce anchor shadow infrastructure. |
| I2 | `303c11b10fffb79a468694daeb2ebc875015f837` | Complete initial shadow architecture. |
| I3 | `5caa933883073e2aa5f7e10b95b9e10eba5cafb2` | Strict anchor shadow parity. |
| I4 | `480228db93393fb160fbba64b28264f330228065` | Activate experimental anchor emission. |
| I5 | `3cd5d7ba0460a52e72e8eecef62599f52d4792eb` | Shadow explicit occurrence plan. |
| I6 | `6b4eadc3d572d1acfa2be9a256039a8efd512757` | Activate experimental explicit-plan mode. |
| I7 | `e490bd0b418054330dc716e221eba7768bac3773` | Remove experimental legacy explicit emitter. |
| I8 | `b604598ab7642078fad25b2ab2f8be5ae849abf4` | Close explicit-plan bypasses. |
| I9 | `054d5dc8dda989755f33e5492bd017cd08657a63` | Prototype broad-prose passage placement. |
| I10 | `83e8f75eaf4cf7c3f633d0d3a3e87e45c06a91f1` | Verify exact passage placement. |
| I11 | `28bbe57914ffa6076d073caf86dcf6ed928a3328` | Three-pass full-impact shadow build. |
| I12 | `237a7799390c9749951718c0ae4fbf35a257a01a` | Harden placement identities. |
| I13 | `42f2db31f181cfdae0871c4a73cf2c4f56f9860d` | Validate page impact. |
| I14 | `8c1f2d47d3d045a4c28d74cecc56fe340ec6b337` | Correct exact index-key impact comparison. |
