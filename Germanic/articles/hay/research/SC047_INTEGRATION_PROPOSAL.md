# SC047 — integration decision for the project owner

**Recommend approval of exact-head promotion of PR #21.** The candidate has
passed the required scientific and publication checks at `113101ac`. Approval
would integrate two selectable historical orders and one shared selected corpus;
it would not select the historically preferable SC047 order or settle ‘hay’.
Nothing in this review modifies or merges the PR.

## Verified position

| Ref | Observed state |
|---|---|
| Remote `update` | `545ba40ab3fa363249562bc032f7df1c3923dc47`; ancestor and merge base of both research and candidate |
| Local `update` | `3f2bbd90`, nine commits behind `origin/update`; not checked out. Use the verified remote ref, not this stale local branch. |
| [PR #21](https://github.com/nh36/caprWIP/pull/21) | Open draft, clean merge state, base `update`, head `integration/sc047-model-adoption` at `113101ac5f169b589e1a9647cdf24d32cdd4d919`; exact-head portable check passed; no recorded approval in PR review state |
| Candidate worktree | Clean, same exact head and tracking ref |
| `research/hay-article` | `418ff25f8dc2539b4273bae0900cdf904f1b1127` locally and remotely; no tracked work in progress. Three pre-existing unrelated untracked paths left alone. Its merge base with #21 is `545ba40a`, not the candidate. |

## What promotion would integrate

The [adoption memorandum](https://github.com/nh36/caprWIP/blob/113101ac5f169b589e1a9647cdf24d32cdd4d919/Germanic/docs/models/sc047/adoption.md),
[model documentation](https://github.com/nh36/caprWIP/blob/113101ac5f169b589e1a9647cdf24d32cdd4d919/Germanic/docs/models/sc047/README.md)
and [SC047 audit](https://github.com/nh36/caprWIP/blob/113101ac5f169b589e1a9647cdf24d32cdd4d919/Germanic/docs/sound_changes/audits/sc047-adjudication.md)
remain authoritative for the evidence and scientific decisions.

- A (Ringe–Taylor) and B2 (Dahl–Hogg–Fulk) are separately composed from
  shared source, selectable in Flask and the UI, with A the single-model
  interface default and both in the main book. Provision separately
  hash-bound model binaries with the candidate's backend
  `python3 tools/build_germanic_models.py`. Internal board operations check
  selected inputs forward; custom transducers retain their comparison path.
  Stale/missing binaries fail rather than falling back.
- The compatibility cascade remains an explicit historical replay, with
  compatibility ordering also retained in legacy diagnostics, standalone
  lexical reference and rule inventory. It is not the default application
  model. Modern doculect networks are not being replaced.
- The shared 396-row catalogue includes the documented migrations: deer
  1988 genitive plural, hedge 2069 feminine nominative singular, net 2138
  dative singular, rest 2152 accusative singular and hue 2332 genitive
  singular; admissions are bed 2340 dative singular and kin 2341 genitive
  singular. Hay 2061 retains the comparison; A's mismatch is not repaired
  by selecting an unsupported protected donor. The hedge/rest candidate
  contributed lexical SOURCE only; #20's deer is already incorporated.
  [PR #20](https://github.com/nh36/caprWIP/pull/20) remains open, not an
  additional merge prerequisite; retain its independent research evidence.
  Approval of #21 covers the reviewed bundle, not other migrations or
  wholesale adoption of the earlier proposal branches.
- The original 394-row model captures remain immutable (A 382/B2 385
  matches). The active capture is separate (A 387/B2 388 of 396; compatibility
  388/396) and preserves the eight shared inherited mismatches. Six common
  selected cells and both new admissions match in both models. Pledge, fen
  and wicg are still unscored. Different counts and the interface default
  do not adjudicate historical order. The book, indexes and A/B2 companion
  traces are separate projections of this shared architecture.

## Certification and promotion gates

The PR **description** cites `ddd7f92a` and must not be used as evidence
for `113101ac`. The subsequent exact-head PR comment is supported by
saved receipts in the candidate worktree's
`.capr-work/sc047-hay-final-receipts/`. The ordinary receipt verifier checked
their exact current source identity, persisted records, log/JUnit digests
and test counts. Identity:
`954ee49d1e1deb9d47e391fafe522fc5f91b13c1f4293af9593e5edcc9488136`.

| Exact-head lane | Result | Receipt SHA-256 | JUnit SHA-256 |
|---|---|---|---|
| Serial | 2,146 tests + 9,800 subtests passed; five prescribed historical skips | `d0453279ef061e7399e2b987adf1cdc8ccc17a012050963d43452a39af81b4aa` | `6d2a603c73e63591024ebb436a8319be0c33f4b82ff65cc80c854ffb28e762cd` |
| Exclusive | 26 passed | `b0744c05555d0a9de794fbd674b9d3247bfc4da555a49f73a851481eb0b3f5e1` | `97898d13fc5948979f3c4031ebe0a8bcb3624eded7fd4c12b847c52297daa65d` |

The exact-head focused lane passed 17 tests; saved `--status` reported
fresh graph nodes and consistent scientific/publication axes. Its five
standing unassembled lexical items are explicit editorial policy, not new
SC047 obligations. The exact-head publication record reports the strict
344-page build, 1,377 audited index links and 117 stages in each model
companion; the checked-in main PDF, A/B2 PDFs, capture and shared corpus
hashes match the adoption memorandum. The body reports a successful
frontend build and pre-existing Svelte typing issues; a clean typecheck
is not claimed. Neither portable CI nor this read-only audit is a fresh
strict run.

**Proposed execution only after approval:**

1. Recheck both remote refs, clean candidate source, approval and the
   exact-head receipts. Update the PR's certification summary without
   changing its head. If administrative policy permits, fast-forward
   `update` to certified `113101ac` without rewriting history or changing
   the source identity; candidate tree:
   `8f1d86f3455fbf6a69b718da55d386d7668802e0`. Reconcile the PR's closure
   with the actual promotion. Do not separately merge #20.
2. If the required merge path creates a different commit, or the base
   moves, stage the intended integrated commit and obtain its own
   applicable exact-source certificate and publication record before
   promoting. An identical tree may establish content parity but does not
   transfer an exact-commit certificate. Re-run the affected canonical
   regeneration, strict serial then exclusive validation and rendered
   inspection where the certified state changes.
3. Verify the resulting remote `update` and provision current A+B2 app
   binaries on that deployment; smoke-check both selectors and explicit
   compatibility, and record the actual live commit. Preserve both the old
   captures and receipt sets. Begin SC083 only after this baseline and the
   scoped next-work authority are confirmed.

No identified scientific or publication blocker remains for the exact
candidate as reviewed. Owner approval, the promotion route/PR record,
durable retention of the local receipt bundle, and deployment verification
are still outstanding; any different final commit has a separate
certification gate.
