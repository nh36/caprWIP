# SC063 lexical coverage: validation evidence

This is an evidence archive, not a successful certification. The research
candidate is commit `e16ac243382280b0c7ffc50335d6cc1f28051b3e`, with tree
`87944bf326c46bf8090fb547c48ed3445d6dec04`. The approved `update` reference
remains `99b1d2e919a191910e8e6df5ef4b138e9bad4de1`.

## Completed strict serial run

- [Full stdout log](final-strict-serial-652657e3f3094274a51097225b039bd2.stdout.log)
- [Full stderr log](final-strict-serial-652657e3f3094274a51097225b039bd2.stderr.log)
- [Original execution receipt](final-strict-serial-652657e3f3094274a51097225b039bd2.receipt.json)
- [Receipt alias](final-strict-serial.json)
- [JUnit report](final-strict-serial-652657e3f3094274a51097225b039bd2.junit.xml)

The command was the full strict serial lane, excluding the separately
exclusive evidence suite. It returned exit code 1: 26 failed, 1,934 passed,
five intentional historical-replay skips, and 9,781 passing subtests.
Pytest reported 3,906.58 seconds. JUnit's test count includes subtests;
it is not the count of top-level test methods.

The failures concern population/publication/census expectations, the
`PGCellEnd` change whitelist, fingerprint/current-state consistency and
index-approval scopes. They are not 26 new lexical mismatches. No exclusive
lane pass or completed A/B/C certification is claimed.

The run began with HEAD at the approved before-reference. Commit
`e16ac243` was created and pushed while it was running, at the user's
request. The receipt records `source_changed: true`. Although the candidate
tree was unchanged, this is not a final source-bound certification of the
commit.

## Supporting evidence and integrity

[runs.tsv](runs.tsv) inventories every completed logged command from this
closeout, including unsuccessful intermediate attempts. Each row links its
receipt alias, original receipt, full stdout/stderr and JUnit report when
one exists. Successful publication, focused controls, protected adoption
and integrated checks are preserved alongside failures, not substituted
for the failed strict lane.

The receipts and logs are byte-for-byte copies of the original artifacts.
Their absolute execution and artifact paths are historical provenance,
not paths expected to exist in a fresh checkout. The corresponding copied
artifacts are identified by basename in `runs.tsv`; the original recorded
stdout, stderr and JUnit hashes are unchanged.

[final-population-protection.json](final-population-protection.json) records
392 accepted selections, 384 matches and eight inherited mismatches,
preservation of all 391 prior complete records, and the unchanged protected
380 projection. [publication-visual-final.json](publication-visual-final.json)
records inspected pages and PDF/image hashes. Its private page-image paths
are historical locators; the rendered PDFs are published in the repository.

[SHA256SUMS](SHA256SUMS) covers all other files in this directory, including
this explanation. Verify from this directory with:

```sh
shasum -a 256 -c SHA256SUMS
```
