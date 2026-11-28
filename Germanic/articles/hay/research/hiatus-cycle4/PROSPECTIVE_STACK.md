# Prospective cascade: matched builds and independent validation

## Identity and question

Research only (`research/hay-article`, predecessor `f6b8f564`). Hold the
canonical, A and B2 orders fixed and ask which private changes can share a
substrate without losing historically relevant contrasts. Retention, medial
resolution and absolute-edge resolution are separate hypotheses.

The [live receipt](prospective-traces.json.gz), SHA-256
`dd1b903018242f9e26b99c0e6bd88bd83a35c9be89b1acaa2b81f2e0323c1ce1`,
contains compiled-component identities, definitions, actual placements, P0
traces, every changed corpus path, all comparison traces, and timings. The
launcher pins production to `113101ac5f169b589e1a9647cdf24d32cdd4d919`,
first-cycle tools to `f220d31157eaa10fcb9a3785ac349bdfac8d6c22` and
cycles two and three to `5a480e470c19c8877d23b428bad89772f22192d3`.
The source and archived corpus hashes are
`43188e9a8e5bcbd028043675586c6655f81394beba55f0a4bb4044792db4050f` and
`85bc1109b8d53b6049870547f44a82e9ada5beb004047c4d2037ee7efb50bb34`,
respectively. Both new panels were committed before any integrated scoring.

Run in Bash from the repository root with the backend active (Foma
`0.10.0alpha`). The cache path is inside the backend container:

```bash
set -euo pipefail
cache=$(docker compose exec -T backend mktemp -d /tmp/capr-hay-prospective.XXXXXXXX)
bash Germanic/articles/hay/research/hiatus/run-container.sh local --stage-cache "$cache" > /dev/null
bash Germanic/articles/hay/research/hiatus-cycle4/run-container.sh prospective --stage-cache "$cache" |
  gzip -n -9 > /tmp/capr-hay4-prospective.json.gz
```

The recorded run used an already populated cache. Fresh compile times and
binary byte hashes are provenance, not trace-equivalence criteria. This is
a private, opt-in replay, not an added CI lane.

## Current state and design

| Arm | Changes relative to the frozen order |
|---|---|
| P0 | None; compare every output to its immutable archived counterpart. |
| P1 | S1 weak *e.i* repair; split original foot-conditioned singleton loss from marker stripping. Keep the marker through private late operations, then strip before incumbent contraction. |
| P1 + group; P2 without group | Add one to P1 or remove one from P2, independently for each group below. |
| P2 | Early short-back `BkWL` then `BkNu` before `OEAuBrightening`; `HwMed` before `EAFBrighteningUnstressed`; `HLBroken`, `HbFront`, `HbIden` after actual singleton loss and before incumbent `OEContraction`. |
| P3-D/J/N | P2 plus one matched, strictly late nonfinal front mechanism, before marker stripping. |
| Edge D/J/N | P2 plus one absolute-final policy: long contraction, short consonantal outcome, or short nuclear outcome with separate printing. P2 itself tests retention. |
| Fringe sensitivity | P2 plus `HbOU`, kept out of the common group. |

This integrates the existing stage alphabet, not the experimental
[typed nuclear alphabet](NUCLEAR_ALPHABET.md) or an independent general
secondary-stress grammar. Neither private nuclear output nor a printed
digraph should be fed back as a Proto-Germanic reconstruction. The gate
remains order-specific for full inputs; exact local entries are only tests
from their stated anchor. See the [source ledger](SOURCE_ENTRY_AUDIT.md)
and [ordering ledger](ordering-proposal-v1.tsv) for historical authority;
executable placement does not date a change.

## Diagnosis

**Frozen corpus.** All P0 surfaces match: 394 archived and 396 active
records in each order. P1 has four internal-only changes per order,
`1943` and `1944` in both versions (deferred stripping); P2 adds four
internal-only changes, `2019` and `2195` in both versions (`HLBroken`).
P1+back and P1+hw do not add a frozen-corpus firing; P1+h reproduces the P2
counts. P3 and fringe sensitivity add no surface change. Edge D/J each
change only A's two copies of `2061`, *hei* to *hē/heġ*: these are rival
analyses of the same target, not independently preferable corrections.
Edge N changes the representation of the same two paths but not their
printed output. Canonical and B2 have no extra edge firing. No other wide
surface change requires classification. The eight weak-domain firings
were checked in the [separate handoff assay](STRESS_HANDOFF.md); the P1
delta reported here is relative to the frozen staged P0, not a count of
all inherited weak reductions.

**Frozen validation.** There are 42 new rows: two development records,
two explicitly flagged for prior structural use within the 40 reserved
rows, and one non-executable observation. Each order admits 40 of the 41
machine inputs; ‘thief’ loses its path at `SC047ProtoInput`. The exact
first-listed form count is 24 of 40 outputs at P0 and 26 of 40 at P2.
This is not an accuracy measure: exact matches include retentions, and
the reported forms preserve spelling and dialect variation. All gains
are assigned by ablation to the h group, specifically `HLBroken`:
subjunctive ‘flee’ changes *flēoæ* to *flēo* and ‘pupil’ nominative
changes *seoæ* to *sēo*. The latter still shares its stem and mechanism
with the development history of ‘see’. None of P3, the edge policies,
the back group, or the separate fringe arm changes these panel outputs.

The panel separates adjacency after loss from presumed contraction.
‘Catch’ shows the infinitive, plural and participle after singleton
loss against the retained final consonant of the imperative, but P0
already handles these. ‘Trough’ still gives *þrūum*, not the contracted
compound form. ‘Toe’ and ‘hostile’ retain *æ* after loss. The ‘roe’
endpoint is among the recorded variants, though not the first one;
the ‘joy’ correspondence remains disputed. ‘She’, the loan ‘devil’
and the disputed ‘that’ compare *īo* with P0/P2 *ēo*, not three
demonstrations of erroneous quantity. The uncertain ‘lord’ and
‘peacock’ do not become independent tests of a sound law merely because
the model preserves their medial labial. A stage-local *þēo* endpoint
and the observation-only protected *þēow-* are not a full paradigm
replay. Neither protected-labial chronology nor general nuclear
realization is validated.

**Expanded comparisons (310 traces per arm and order).** The following
are comparisons of surface differences, with duplicate controls retained
under distinct trace IDs, not independent families:

| Contrast | Canonical | A | B2 |
|---|---:|---:|---:|
| P2 vs P0 | 36 | 37 | 37 |
| P2 vs P2 without back | 15 | 15 | 15 |
| P2 vs P2 without hw | 3 | 3 | 3 |
| P2 vs P2 without h | 19 | 18 | 18 |
| Each P3 vs P2 | 25 | 33 | 33 |
| Each edge D/J vs P2 | 5 | 8 | 6 |
| Edge N vs P2 | 0 | 0 | 0 |

The back group improves the tested short ‘claw’ full path and short
knee/tree plurals, but its local *au > aeu* path is rejected at
`OEEwLongDiphthong` for ‘claw’, ‘threat’ and ‘few’ probes. Hogg's exact
short local ‘claw’ is one casualty; Ringe and Taylor's long direct
history remains incomplete (*clāw* or *clā* by local entry), not rebutted.
The clean frozen corpus misses both failures.

Removing `HwMed` removes all three copies of the admitted ‘see’
*sēon* endpoint. The rule feeds later breaking and singleton loss,
then `HLBroken` changes *seoan* to *sēon*. It does not by itself
realize ‘lend’ or ‘filter’ (see [the independent hw assay](MEDIAL_HW.md)).
The exact Anglian ‘see’ *æ* tail still gives *seæ*; the lowered probe
*sē* is not a solution to that source input. Removing the h group
also removes motivated southern endpoints for ‘wealth’ and ‘draw’.
The fringe sensitivity removes attested hiatus (*wlōum* becomes
unattested *wlōm*); it is excluded from the common recommendation.

The matched late D/J/N families have identical surfaces on this panel.
A and B2 recover *ġecēþ/ġecēd* where P2 exposes the prefixed hiatus;
the source-backed short ‘strike’ local entry and the reduced ‘flock’
probe contract too. But the same arms erase *streide* in the lowered
and directly comparable retention probes; the exact published *æ*
entry remains *stræide*, not independently explained by their behavior.
No surface improvement on ‘call’ or ‘strike’ licenses a general rule
that also collapses a supported retention. Moved applications and
synthetic controls are not countable dating evidence.

At the edge, *cǣġ/cǣġe* survive every comparison. The short ‘river’
probe gives *ei/ē/eġ/ei* under retention/D/J/N; J is adverse if the
attested mid-vowel oblique is inherited from short *ehi*. None of those
outputs alone explains the whole paradigm. In particular the long
stage-local ‘river’ entries here can still print *ēi/īei*: an earlier
successful absorption in a different arm must not be imported into P2.
N is demonstrably distinct internally from retention; the shared printer
does not identify their histories.

## Literature, scope and verdict

The relevant loci and statuses are recorded in the source audit, the
[river collation](RIVER_OBLIQUES.md), and the [priority register](SCHOLARLY_PRIORITY.md).
In particular, Ringe & Taylor (2014: 49, 179) support medial labiovelar
reduction; their pp. 314–318 support actual intervocalic loss feeding
contraction but also show uncontracted outcomes. Hogg's and Ringe &
Taylor's disagreeing ‘claw’ quantities must be run independently.
SC085/086 are the frozen controls, not replacement templates.
Loss before loss-induced contraction is entailed by the adjacency and
independently supported by the uncontracted spellings. Earlier labial
hiatus formation is distinguishable from its later realization; these
runs do not independently date the latter against HVD. The experiment
does not establish that the loss and contraction domains are identical
across Old English varieties. Front hiatus resolution does not establish
an analogical source or select a unique historical mechanism.

**RETAIN** production and all frozen captures. **RESTRICT** the
prospective core to the diagnosed S1/handoff repair and independently
supported narrow medial *hw* and post-loss environments for separate
formal review (`P2-without-back` is the tested starting point, not a
production proposal). **DEFER** the back group as integrated here, broad
SC086 replacement, the universal late front and absolute-edge arms,
and any migration. Before adoption, resolve the exact admitted-stage
failures, validate the post-loss quality/quantity scope with independent
contrasting cells, and run any approved, bounded changes through the
formal production gates. No registry verdict or certification changes.

## Propagation and residue

No source registry, prose, production code, generated projection or target
needs propagation from this experimental verdict. The earlier receipts
remain in place; the corrected quantities and exact input statuses in
the source ledger govern interpretation. The replay itself checks all
frozen outputs, frozen panel identities, and isolated component exports.
Its fresh-run trace comparison does not certify fresh production builds.
