# B3 — Preserve early *iu*, *īo* and *ēo* before a regional merger

## Which histories actually converge?

Ringe & Taylor (2014: 173–175) derive early long *īo* from
*iu*, and *ēo* from *eu*. The sources of the earlier nuclei
are not interchangeable:

| Family | Independent starting point and what the witnesses show |
|---|---|
| ‘Three’ | PGmc neuter *þrijō > þriu > þrīo*; Gothic *þrija*, ON *þrjú*, OS *thriu*, OHG *driu*. Campbell §120.3(c) and Hogg §§3.8, 3.19.3 give an ending-development/hiatus route, not deletion of *w*. The earlier *þri.u* model entry is an analytical hypothesis, not a quotation of the already incorporated *þriu*. Do not use the corpus's different masculine form *þrīe* as the neuter target. |
| ‘Friend’ | PGmc *frijōnd- > friund > frīond*, supported by Gothic *frijonds*, OS *friund*, OHG *friunt*. The realization window receives a nucleus in a closed word, not automatically a productive closed *i.u* rule. Sweet Ct. 40.4 and 40.7 show plural *friond/frionda*; Vespasian Ps 87:19 *freond* is a different witness and cell. Hogg §5.159 reports both spellings in Northumbrian ‘friend’ despite clearer distinction elsewhere. |
| ‘Devil’ | West Germanic loan *diubul*, cf. OS *diuƀal* and OHG *tiubil ~ tiufal*: no necessary English labial-loss or weak-vowel condition supplies *iu*. Sweet 621 lists *dioful* in Vespasian Hymn 13:4 and files Ps 108:6 under *deofol* (text p. 349 prints ⟨deoful⟩), plus compound Corpus 1457 *heldiobul*. Hogg §5.156 independently reports both spellings in the two *Pastoral Care* manuscripts. These are not measurements of individual vowel duration. |
| ‘She’ | Ringe & Taylor 174 posit *hī* plus the feminine ending yielding *hiu* (compare OS/OHG *siu*), then *hīo*. Compare Hogg §5.156's separately counted *hio/heo* in the *Pastoral Care*. This is not a vowel before a consonantal *w*, nor the unrelated *hio* gloss for ‘colour’. |
| ‘Your’ | PGmc *izweraz > iuwar > īower*, independently supported by OS/OHG *iuwar*. Ringe & Taylor 174 expressly distinguish it from *iu* raised from *eu*; the labial remains. Vespasian Ps 30:25 and 68:33 show *eower* in the gloss tradition, not invalidation of the earlier independent reconstruction. |
| ‘Deep’, ‘thief’, ‘tree’ | PGmc *deupaz* and *þeubaz* already contain *eu* (Gothic *diups, þiubs*); ‘tree’ can acquire *eu* from separately motivated labial loss or final vocalization. All give long *ēo* at the early realization stage on this account. ‘Four’ and ‘chew’ likewise give *ēo* with consonantal *w* retained (Ringe & Taylor 173). |

Tensing and second-element realization follow incorporation
where incorporation is needed. Hogg §§5.41–46, 5.155–162
separates second-element lowering (*u > o*) from lowering
of the **first** element at the later phonemic merger. He allows
some earlier southern lowering without dating the full merger
before i-mutation (§5.74 n. 6). In West Saxon, ninth-century
variation leads to broad *ēo* in late texts; Mercian likewise
shows substantial merger, but it is not uniform across the
gloss traditions. Northumbrian largely preserves the contrast
and Kentish has evidence of raising the long series instead
(§§5.159–160). Thus the regular early *īo* and a legitimate
later *ēo* may both be right, but not as interchangeable
historical predictions. Inverted spellings and repeated forms
in one witness are not independent phonemic tests.

## Paired executable diagnosis

The [receipt](early-nuclei-traces.json.gz) replays 14
stage-local inputs across the three unchanged orders. A
word-edge `IuEdge` turns syllabic *i.u* into atomic *iu*;
`IuHigh` then realizes atomic *iu* as *īo*. Both are compared
against the incumbent `OEDiphthongLeveling`, which at this
site maps both atomic *iu/eu* to *ēo*, yet maps plain split
*i.u* to **short** *eo*. A separate, deliberately late `IoLate`
maps *īo* to *ēo* just before rendering. It demonstrates
separability of endpoint from history; rendering position is
not the historical date of merger.

| Input | Incumbent | Incorporation only | Both operations | Both, then merger |
|---|---|---|---|---|
| Split ‘three’ | *þreo*; marked twin *þriu* | *þrēo* in both | *þrīo* | *þrēo* |
| Already incorporated ‘three’ | *þrēo* | *þrēo* | *þrīo* | *þrēo* |
| Atomic ‘friend’, ‘devil’, ‘she’, ‘your’ | *frēond, dēofol, hēo, ēower* | same | *frīond, dīofol, hīo, īower* | same surfaces as incumbent |
| Inherited *eu*, ‘tree’ *eu*, unrelated split *i.o*, split nonfinal *i.u* | Distinct controls | unchanged | unchanged | unchanged |

Realization alone changes the already incorporated forms but
not split ‘three’. The late merger affects independently
pre-existing *īo*, not just tokens made by `IuHigh`. The acute
twin tests decoding and assignment, not a different historical
stress. Early realization currently collapses that marking to
the existing unmarked long-io token. A production proposal
must preserve relevant stress across any intervening consumers.
The [frozen validation panel](../hiatus-cycle4/validation-nuclei-v1.tsv)
already used ‘friend’, ‘your’, ‘devil’ and ‘she’, so this
ablation does **not** count them as unseen holdouts. It uses
the atomic loan at a later anchor; the supplied *b* is a local
consonant projection, not a reconstruction of loan transmission
or the final OE consonant.

**REVISE** the proposed early realization into two reviewable
operations; **DEFER** production until downstream consumers
of *īo* are audited and an independently defined regional
realization is available. Preserve existing late benchmark
targets. Add dated early comparisons rather than changing
those targets, and treat inherited/derived *eu*, already
atomic *iu* and split hiatus as distinct validation strata.
The distinction and direction are published phonology, not a
new CAPR discovery; the matched ablation exposes where the
current shared realization erases the distinction.

```bash
set -o pipefail
bash Germanic/articles/hay/research/hiatus-cycle4/run-container.sh early_nuclei --stage-cache "$cache" |
  gzip -n -9 > /tmp/capr-hay5-early-nuclei.json.gz
```

Use the [pinned cache warm-up](../hiatus-cycle4/PROSPECTIVE_STACK.md#identity-and-question).
Receipt SHA-256:
`1022c51f2b77e86d84c7cf98a3a3b7714ac446447ba527948ba6b472713b8c17`.
One private three-export compilation, no default lane change.
