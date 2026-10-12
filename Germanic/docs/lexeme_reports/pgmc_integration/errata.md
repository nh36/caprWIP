# Verified reporting errata — 2026-10-12

## Identity and question

Stream 1, branch `update`, base `7848f76223099402cf3863aa8016cd9fe40f949a`.
This is a bounded factual/bibliographic/navigation correction, not a new
research survey or SC adjudication. Question: do the held running heads and
current generated population owners support the existing attribution,
locators and current-status claims?

## Current state, diagnosis and literature

Current authority: `../../CURRENT_STATE.md`, `../../README.md`, the generated
population crosswalk/summary, report and class manifests, and the named
model/ledger/pilot documents. Scholarly pages below are printed pages,
not extraction-sheet markers. Page-marked held texts were reopened; no
new original-image verification or unavailable-main-dictionary check is claimed.

| Original claim / owner | Proof and source | Corrected claim / action |
| --- | --- | --- |
| Fire model/ledger: `BosworthToller1898, 288` supports noun `fyr` and oblique `fyre`; reviewer/implementation records say that locator was localized. | `docs/refs.bib` separately catalogues the main dictionary without a local file and `Toller1921` Supplement with the held PDF. Its Vision title sheets005/007 say Supplement; sheet288 bears printed276, FYLSTA / FYR-HÚS, and `fyr. Add` (lines45373–45406). Noun attestations include `fŷr bið þeóf`; obliques separately include `of fŷre`, `in fŷre`, and hearth `Fŷre`. Sheet300 bears printed288, GEARD / GEARO. | Model/ledger cite `Toller1921, 276`, separately identifying noun and oblique evidence. Historical review/implementation assertions carry supersession notices. No locally verified main-dictionary page is asserted or disproved. Dictionary forms do not demonstrate analogical restoration. |
| Fire ledger's second receipt, lines5388–5394, is attached to the noun entry. | Same held Supplement: this passage is in `āhreddan`, with `of þam fyre`, not the noun entry. | Replace the misleading receipt with the verified printed276 entry; retain the independently attested oblique evidence there. Fire pilot has no erroneous dictionary locator and remains unchanged. |
| You ledger: Fulk §8.3 pp204–205 corroborates `*-zw- > *-ww-`. Integration source-checks/resumption imply a stale unsupported claim distinct from the origin passage. | Fulk Vision sheets204–205 bear printed187–188 (lines11372–11432). Printed187 gives the reported Krahe/Meid origin and explicitly no consensus, then separately offers `*-zw- > *-ww-` as one route to WGmc `*iuwiz`, alongside another route. Actual printed204–205, sheets221–222, discusses relative/indefinite pronouns. | Correct ledger to printed187–188, preserving qualified consonantal corroboration. Repair the active integration criticism: this was a sheet/folio error, not invalid evidence. Model and integration origin citation187–188 remain valid and unchanged. |
| Adder model: Fulk149 supports secondary `næddre`; earlier review/ledger/implementation records repeat149. | Fulk sheet149 bears printed132 (lines7895–7928); it discusses `næddre` beside `nædre`, probable shortening, obscure motivation and possible analogical alternation. | Correct model to132 and add ledger/review/implementation supersession receipts. The model claim and survey citation132 concern the same valid passage, not competing claims. Clark Hall was not reverified or changed. |
| Adder pilot: straightforward inherited control with no early-reconstruction disagreement. | `report_manifest.tsv` marks this as `format_test`. Current model and scoped integration preserve Orel's two feminine alternatives; held Orel sheet325, printed286 (Vision lines32159–32170), gives long-*ē* and short-*a* feminine forms. Existing original-page receipt in the adder ledger verifies barred *đ*. | Add a concise historical-format-test supersession/navigation notice; leave the historical body, selected long-*ē* input, classifications and regular output unchanged. No etymological consensus claim is added. |
| Root/Germanic README: research complete, current write-up-only phase,386 rows in root, canonical-state current authority. | Living CURRENT_STATE owns sequential per-SC adjudication and selected387; docs README defines SOURCE/GENERATED/ARCHIVE. | Route current phase/commands to those owners; root denominator becomes387. Preserve the 2026-04-30 completion claim as historical, not current; distinguish active versus immutable original380 fingerprints. |
| Assembly README:147 current model entries; production backlog: current380/148 and11 reports leave136 missing. | GENERATED integration summary/crosswalk: selected387, audit393, assembled160, required157, original380 currently required150; five required unassembled2055/2120/2327/2328/2329, eight optional assembled, hence152 required assembled. Report manifest separately has11 pilots and1 format test. | Update explicitly current assembly/navigation claims; banner the detailed old backlog/counts as a retained checkpoint. Distinguish387 runnable derivation write-ups,393 audit records and160 elaborated models. Assembly gaps are not absent derivation write-ups. |

Holding limit: the checked dictionary PDF/text holdings are the Supplement,
despite the filename. No separate main-dictionary holding was found in the
local reference collection; its noun/oblique assertions cannot be independently
certified here. This is not a claim that the main work lacks those forms.

## Historical analysis and verdict

History/stage/scope, rule census, counterfactuals and chronology-witness
classification: n/a; no scientific decision is reopened. Reporting verdict:
correct proven work/folio/navigation errors; retain distinct valid source
claims and mark holding uncertainty. No registry verdict or editorial
classification changes. Fire's selected quantity/cell and restoration analysis
remain outside this erratum.

## Propagation and validation

Only the listed SOURCE prose and legitimate downstream assembly/index
projections may change. Regeneration uses only
`python3 Germanic/tools/adjudicate.py --refresh`; no PDF rebuild is required
for these annotations. Citation, index, freshness and regression guard
results follow. Corpus/FST/registries/edges, reconstruction
audit SOURCE evidence, baselines and scientific outputs remain protected.

- Canonical refresh and `artifact_graph.py --check`: **CONTROL PLANE CLEAN**.
  `pgmc_lexical_integration.py --check` validates all three projections.
- Chapter citation ranges, bibliography sanity and source section-locator
  guards pass; index architecture negative fixtures pass (18 checks).
- Targeted integration, publication freshness, citation, stage-index,
  variety-index and cascade-baseline tests: **152 passed, 48 subtests passed,
  5 failed**. The five variety-index failures predate this erratum:
  expected2456 versus actual2453 occurrences, expected2368 versus actual2365
  print-main entries, and cud annotation receipts at source line32 versus39.
  Re-running those five assertions against CSVs read directly from committed
  base `7848f762` reproduces all five failures. The standalone index guard's
  broad-prose assertion also fails against those committed base tables.
  No unrelated index assertions or baselines were rewritten to hide them.
- Exact diff inspection: generated changes are only the fire/adder prose in
  lexical/book assembly, lexical provenance hashes, and two additional
  non-indexed quotation candidates in the index audit. Production index
  tables and variety-attestation audit remain byte-identical to the base.
  No corpus, FST, registry, edge, protected audit-evidence, baseline or
  scientific-output file changed; `.DS_Store` and `fsts/tmp_probe.foma`
  remain outside the release.

## Residue

Main-dictionary verification remains unavailable. No SC032 work, new survey,
publication promotion, morphology/input/output change or consensus assessment
is authorized by these errata.
