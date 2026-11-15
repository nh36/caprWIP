# Integration of mære and the Flask nominative plural

## Scope and references

This integration starts at `8204ed8264b44d8931a6e506b68549f30b9fbe53`,
which includes the certified Flask adoption `2254faea` and findings §12.
PR9 is already merged into `update`. Only the two later fixes and their
regressions from PR10 commit
`26a425a667153a9119fdcad7e60b67e1872406e2` are imported.
SC044 is a separate assignment and is not begun here.

The existing [final-nasal analysis](sc042-final-nasal-candidate.md),
[pretonic implementation review](sc085-pretonic-context-review.md),
[SC069 decision](sc069-adjudication.md) and
[Flask certification](flask-production-certification.md) retain their
historical evidence, decisions and exact before-references.

## Reconciliation

SC076 retains the existing positive pretonic annotation. SC085's foot
guard consumes that information before annotation cleanup. No intervening
rule, historical stage, chronology edge, lexical selection or SC051
semantics is changed. The source and regression justification remains
the bounded pretonic review, not a new historical adjudication.

The migration validator rejects a change in output count at each link,
before folding a chain. A singleton-to-ambiguous-to-singleton chain
cannot hide its transient multiplicity. Valid migrations, their order,
every approval and every frozen baseline remain unchanged.

The overlapping historical source guard verifies all five exact Flask
definition changes and both exact annotation-lifetime changes against
the immutable pre-adoption source before projecting those later changes
out for older historical assertions. This preserves the archived
three-definition final-nasal comparison instead of widening it or
rewriting its receipts.

## Publication and follow-up

Findings §12 and its contents link are retained. The selected Flask
cell is nominative plural flascan; its separately attested dative
singular shares the late-final-n route, while flasce remains the
singular comparison. SC023 precedes the apocope exposing secondary
final n; SC069 leaves final -ōn to SC071/SC100. Chapter 3 retains the
same explanation and Hill's historical alternative.

The Boutkan1995 §3.2.14 and early English/Frisian newly-final-n
follow-up remains in the Anglo-Frisian literature backlog. No new
source consultation or historical conclusion is claimed.

## Validation and landing

Canonical `adjudicate.py --refresh` and `--status` both passed. The
refresh rebuilt production bins, canonical traces, registry views and
reader/book projections through the artifact graph, resolving the stale
products reported by PR10's failed portable run. All graph nodes are fresh.
The combined Foma source SHA256 is
`56369de5575623beb4b36473dae214a158a5748353039f0623161831b08e08de`.

The fresh normal-entry comparison reused the unchanged worker in
`flask-production-evidence/verify.py`, without calling its file-writing
main or overwriting its historical observations. All 394 records and the
complete computed summary agree exactly with the certified `2254faea`
baseline: 386 matches, the same eight mismatches, no rejections, no
final ambiguities and no intermediate ambiguities. There are zero
row-by-row differences. The output digest remains
`1bef3798e864ce1277511f9d9f6bf5c461dcbfa4608173849f4b467225e89727`.
All 15 Flask/class controls agree with the certified candidate, including
the disclosed pre-existing accusative and pre-m residues.

| Witness | Entry | Combined result |
|---|---|---|
| mære | normal raw `márōn` | mære |
| Flask nominative plural | normal raw `fláskōniz` | flascan |
| Flask dative singular | normal raw `fláskōni` | flascan |
| Flask singular comparison | normal raw `fláskōn` | flæsċe, not the selected cell |
| toe | selected normal input | `*t*ā*ç*e` → `*t*ā*e` → tā |
| clay | explicitly post-tokenization stage entry | front ending with fricative → hiatus → þō |
| fringe | stage entry `*w*l*ō*x*u*m` | `*w*l*ō*u*m`, retaining all of -um |
| pretonic retention | stage entry `*ᶠ*b*i*x*í*n*d*a*n` | marker retained through SC076; h retained and marker removed at SC085; final behindan |

Clay still rejects at the ordinary gateway; its external control is not
a newly admitted corpus row. Fringe and the pretonic control are also
explicitly stage-entry assays. The seven intervening operations preserve
the same segmental development with or without the pretonic annotation.
The deliberate reversed-order and front-only h-loss perturbations still
fail their intended assertions. Protected canonical runtime and baselines
were unchanged by those isolated assays.

The reconciled static guards and migration tests passed 26 tests and
409 subtests, including the transient-cardinality regression. The focused
runtime controls passed all 25 tests. Authentic receipts, full 394-row
observations, stage traces and unfiltered logs are retained under
`.capr-work/maere-flask-integration/`, notably:

| Check | Receipt |
|---|---|
| Static/migration guards | `integration-initial-guards-46d4c65f2cc740619c5f3a490f2eac89.receipt.json` |
| Fresh 394 rows and 15 controls | `integration-production-394-b3dc17ddc4af4e519634692764da5865.receipt.json` |
| Runtime controls | `integration-runtime-controls-8ed136d13afd45b4bd561fbbda389a3a.receipt.json` |
| Strict publication | `integration-strict-publication-788412f4b0c54a638d99df1e47d54bf6.receipt.json` |

The strict publication wrapper passed with retained TeX, zero unresolved
internal references and zero paragraph-gloss violations. The rebuilt
350-sheet PDF was inspected: Flask printed pp.150–154 (PDF sheets152–156)
selects the nominative plural, separately identifies the dative singular,
and preserves the singular problem. SC023 (sheets18–19), Chapter 3
(41–42) and SC069 (112–113) retain the adopted secondary-n/late-shortening
account. These pages and the Flask article are text/layout-identical to
the previously inspected certified publication.

The actual printed index on sheet344 includes flascan at pp.150–151 and
flasce at p.151. Generated index roles distinguish the selected target
from the singular comparison. The table, index, weak-paradigm and SC069
pages were also inspected as images. The updated SC076 and SC085 rule
boxes were visually checked on sheets119 and123, with cleanup only after
the guarded h-loss relation. No clipping or missing glyphs was found on
the inspected pages. Existing width advisories and nonfatal Pandoc ticker
warnings do not represent failed publication gates.

Findings §12, its contents anchor and all four destination files/anchors
were checked directly. The live status now describes the integrated
production state and explicitly leaves SC044 unstarted. No frozen
baseline, prior approval, migration row or historical production-evidence
file was rewritten; only the generated equivalence report changed in
the baseline directory.

Portable CI passed locally (1969 tests, 98 explicitly skipped,
9781 passing subtests) and on integration PR11. The first complete strict
serial run passed 2035 tests and 9821 subtests, with five prescribed skips,
but failed the older SC035 generality assay's live SC076 expectations.
The exclusive suite was not started after that failure.

The assay's six annotated i-lowering controls still expected cleanup at
SC076. Its live mode now retains the marker; its default historical cases,
frozen observation and original holdings remain unchanged. The current
comparison permits only that exact annotation-lifetime difference, not
segmental drift. No production rule, baseline or publication change
accompanies this test-harness reconciliation. All 11 generality tests,
including the fresh runtime assay and checks against the unchanged
345-control historical observation, passed after this repair
(`integration-generality-repair-e4fe66d68d13491f99d119b9fcd78193.receipt.json`).
Complete strict
serial/exclusive certification of the repaired candidate and PR landing
remain to be recorded after execution.
