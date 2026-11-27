# Integrated hiatus experiments

## T1: comparison inventory and common substrate

[`panel.tsv`](panel.tsv) extends the pinned first-cycle
[`historical.tsv`](../hiatus/historical.tsv) by key; the receipt
materializes both inventories without overwriting conflicting early
claims. For ‘couch’, the C1–C3 records supersede the alleged bare
token and separate the accusative, conditional genitive and
unattested nominative. The Kentish *hei weg* row records the future
editorial correction **859**, not OCR **839**, without editing the
article. The *cǣġ/cǣġe* pair remains an independent retention check;
‘rainbow’ is related to ‘rain’, not a separate root, and *sēl* is
not counted as attested.

The original 49 rows had 29 admissions, eight rejections and 12
without a submission. In the latest inherited 54, the same 37
submissions split **29 admitted / 8 rejected** in each model;
17 have no submitted full form. The supplement adds eight
admitted full submissions, including two using the same fixed
active-corpus identities as the joint assay. These are counts of
submissions, not of independent witnesses or matching outputs.
Each substrate run now includes 65 traced inputs; the three
explicitly marked compound probes await boundary-aware replay
and the observed Kentish spelling has no submitted input.

All eight older rejections remain visible. For ‘couch’ the gap
is a later final *-u*, not the cluster or encoding (C3).
For ‘call’, ‘strew’, ‘betray’ and ‘prepare’ the earlier long
preterite ending is not accepted in the submitted forms; their
separately justified stage inputs carry a reduced ending and do
not prove its exact earlier quantity. The exact weak tail in
‘flock’ remains disputed; shortening or dropping the vowel to
pass the gateway would pre-judge HVD. ‘Pillow’ is a loan with a
source-supported later state. ‘Brandish’ has a grade/segmental
problem and the retained-vs.-lost palatal comparison is local,
not an amendment to the accepted early lexeme. Stage entries
record the preceding derivation and use the exact before-stage
anchor; an encoded synthetic state is not a historical input.

| Executable site (A/B2, relative to its neighbours) | Historical purpose and constraint |
|---|---|
| `OEIUmlaut` > `OEWLossBeforeI` > `SC047FinalIi` | Mutate the root before losing noninitial *w* before fully weak *i/ī*, leaving *e.i* where both vowels survive. In A/B2 the following experimental baseline already contracts final stressed *i.i*; that component is not a law for unlike nuclei or every medial identical pair. See Ringe–Taylor pp. 258–261, 317–318. |
| `OEBackMutation` > `OEMedLongShort` > `OEHighVowelApocope` > `OEMedialSyncope` | Distinguish mutation, shortening and weight-sensitive deletion. The following medial-syncope anchor is an identity; the quantitative component itself can delete medial high vowels. Contraction/gliding before it can change eligible weight; late placement cannot undo apocope. |
| `OEMedUnstressedILowering1`/`OEMedUnstressedILowering` before `OEJLossAfterHeavy` | Lower weak *i* in the implemented environments, not a nuclear offglide. Heavy-context *j*-loss is not general loss of final *j* after a long nucleus. |
| `OEJStrengtheningAfterFrontDiphthong` > `OEIntervocalicJVocalization` > `OEUnstressedEIContraction` | Separate consonantal strengthening/vocalization from SC083's unstressed initial/member deletion. The common substrate changes only the last operation, to the S1 foot guard. A physical order is not a dated series of independent sound laws. |
| `OEHLoss` > `OEContraction` > `OEPalatalFricativeMerger` > `OldEnglishOrthography` | Intervocalic velar loss provides another source of adjacent nuclei, after ordinary syncope in the historical chronology (Ringe–Taylor pp. 260–261). The separate general contraction component has its own matching domains; the later merger/serialization cannot tell us whether two identical spellings arose via a glide, fricative or nucleus. |

[`panel-traces.json.gz`](panel-traces.json.gz) has all stage
inputs/outputs and the S0/S1 differences. S1 changes only the
root-stress controls: local past of ‘call’ in all orders and
full present and participle in A/B2. The inherited frozen
traces were replayed before applying S1. To reproduce, run
`bash Germanic/articles/hay/research/hiatus-cycle2/run-container.sh --panel --stage-cache "$cache"`
from the repository root with the private cache described in
[STRESS.md](STRESS.md).
