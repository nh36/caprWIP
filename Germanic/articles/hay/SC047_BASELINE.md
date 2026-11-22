# SC047 and hay baseline

## Branch boundary

- Article branch: `research/hay-article`
- Hay/article baseline commit in this handoff: `8048652604b1925ea815265a66bffa12a55017cc`
- PR #21 branch: `integration/sc047-model-adoption`
- PR/authoritative model commit: `113101ac5f169b589e1a9647cdf24d32cdd4d919`
- Common ancestor: `545ba40ab3fa363249562bc032f7df1c3923dc47`
- PR worktree: `.capr-work/worktrees/sc047-model-adoption`
- PR remains open and draft; it is not merged.

The branches are intentionally not merged or rebased.

## Read-only access

Use the PR worktree as read-only source and evidence:

```sh
cd .capr-work/worktrees/sc047-model-adoption
git status --short --branch
git rev-parse HEAD
```

Do not run a model by using files from the article branch that lack the
adoption commit. The PR worktree supplies the authoritative A/B2 captures,
traces and hay lexeme ledgers listed below.

## Authoritative PR files

| Repository path | Authority |
|---|---|
| `Germanic/docs/models/sc047/adoption.md` | PR adoption scope, frozen results and execution boundary |
| `Germanic/docs/models/sc047/README.md` | A/B2 model architecture and scientific scope |
| `Germanic/docs/models/sc047/results.md` | measured results and capture inventory |
| `Germanic/docs/models/sc047/cells.tsv` | selected model cells |
| `Germanic/docs/models/sc047/expansions.tsv` | expansion proposals and non-adoption controls |
| `Germanic/docs/models/sc047/captures/sc047-production-v1.json.gz` | frozen production capture |
| `Germanic/docs/models/sc047/captures/sc047-active-v1.json.gz` | active capture |
| `Germanic/docs/models/sc047/captures/sc047-active-v2.json.gz` | active capture revision |
| `Germanic/docs/models/sc047/captures/sc047-adoption-v1.json.gz` | adoption capture |
| `Germanic/docs/models/sc047/captures/sc047-lexical-expansion-v1.json.gz` | lexical expansion capture |
| `Germanic/docs/lexeme_reports/model_entries/2061-hay-hīeġ.model.md` | authoritative hay model entry |
| `Germanic/docs/lexeme_reports/model_entries/2061-hay-hīeġ.source_ledger.md` | authoritative hay source ledger |
| `Germanic/tools/sc047_models.py` | A/B2 runner |
| `Germanic/tests/test_sc047_adjudication.py` | adjudication tests |
| `Germanic/tests/test_sc047_followup.py` | follow-up tests |
| `Germanic/tests/test_sc047_models.py` | model tests |

## Frozen versus editable

The adoption capture, corpus fingerprint, 394-row compatibility denominator,
active 396-row catalogue and A/B2 outputs are frozen scientific evidence.
Do not edit or normalize them as part of source transcription.

The following article branch legacy path remains useful historical context,
not PR-adoption authority:

- `Germanic/docs/lexeme_reports/archive/dev_notes_slices/2061-hay-hīeġ.md`

The PR worktree's hay model and source-ledger files supersede branch-specific
older summaries for the A/B2 handoff.

## Safe future integration

The safest future integration is a new authorized branch created from
`update` plus an explicit merge/three-way review of the article metadata.
It should use the PR commit as a source, not cherry-pick or rebase the
article branch silently. No such integration is performed here.
