# R4: What the surviving ‘flock’ ending dates

## Identity and question

**Branch:** `research/hay-article`; experimental base `113101ac5f169b589e1a9647cdf24d32cdd4d919`; immediate predecessor `0362b998`. **Incumbent:** SC063 `OEHighVowelApocope`, recorded as Old English and English-specific in the registry. The D, J and N operations have no registry identities. Would the direct singular in [FLOCK.md](FLOCK.md) have lost its independently reconstructed final short *i* if unlike hiatus had already ceased to be syllabic?

## Current state

The frozen quantitative deletion uses the first foot and treats long vowels/diphthongs or a short vowel followed by at least two consonants as heavy in the relevant context. It has no second post-*h*-loss pass. The local ‘flock’ input starts immediately before *w*-loss at `*e*w*i*d*i` and does not claim that the full PGmc parser derives this form. Short *i* is the Ringe–Taylor reconstruction, not inferred from the output. The long, lowered and absent tails are sensitivity probes. The genitive and dative plural inputs are projected protected shapes, not attested w-less tokens; their *e.i* is injected by the inherited stage context here, not a reconstruction of how those cells acquired it.

## Diagnosis

The receipt records 36 arms in each of canonical, A and B2, against the same 17 stage-local entries. It brackets *w*-loss, HVD, weak-*i* lowering, *h*-loss and the palatal merger. The “after weak *i*” placement follows the entire weak-vowel group through `OEWeakTailReduction`. The stage orders and the FST hash are checked against the frozen baseline. All three orders agree on these local surface results; that agreement does not extend to independently submitted full histories. A wider corpus census belongs to R9, not this local placement assay.

| ‘Flock’ direct singular | Input at HVD | HVD result and consequence |
|---|---|---|
| Before HVD: D, J or N complete | *ēdi* | *ēdi > ēd*, no ending to lower |
| Before HVD: J first step only | *ejdi* | *ejdi > ejd > ēd*; delaying assimilation does not preserve the ending |
| Before HVD: N first step only, frozen atomic token | heavy *ei̯di* (atomic `*ei`) | short *i* deleted; later monophthongization still gives *ēd* |
| After HVD: D, J or N | syllabic *e.idi* | HVD leaves *i*; subsequent resolution and lowering give *ēde* |
| Before HVD: N first step only, private light token | light *ei̯di* (private `*ėi` or accented `*éi`) | short *i* survives, unlike the corresponding private heavy test; subsequent *ēdi* is compatible with later lowering |

With the initial short *i* absent the unchanged or resolved stem has no final reflex to compare. Long *ī* and already lowered *e* let even early heavy resolution give *ēde*. The protected projections do not test direct-cell HVD. The short direct form is a **counterfeeding negative** for early heavy resolution under the short-ending hypothesis; the controls test whether deleting that ending follows from weight rather than from late endpoint matching.

Post-*h*-loss placement can reach the plain and accented stage-local ‘strike’ *e.i*, whereas a wholly pre-*h*-loss matched pair cannot. The *e.e* comparison contracts on the common substrate. Conversely, after *h*-loss the unaccented prefixed ‘call’ probe loses the foot marker and is missed; a split J arm can leave *ġeceġþ* when downstream strengthening changes the intermediate before assimilation. This is a representational limitation, not a source-supported ordering. Before the palatal merger late J assimilation reaches injected inherited *j* but not *ʝ*; after the merger it reaches both. Late N assimilation reaches an injected old atomic *ei* (origin collision). The independent long-vowel ‘key’ control remains *cǣġ* in every arm.

## Literature

[FLOCK.md](FLOCK.md) records the source evidence, including Ringe & Taylor (2014: 259, 318) on short-final *awidi* and contraction, and Skeat (1874: 133) on the neuter direct cell. Fulk (2010: 129–134) and Goering (2016: 186–188; 2023: 67–68), as collated in the SC063 adjudication, motivate quantitative deletion and the independent final/medial distinction. The stage-local timing grid and light/heavy private token assignments are CAPR comparisons, not historical claims from those sources.

## Historical analysis

The geographical claim concerns the w-less English evidence, not all Anglian, West Saxon or Germanic usage. Conditioning is phonological: stressed short unlike hiatus before a single dental plus a final short high vowel; the inherited grammatical cell supplies the relevant input, but is not a condition on contraction. The attested w-bearing English forms motivate separate evaluation of renewal or preserved allomorphy; they do not positively identify a proportional restoration of final *i* in the w-less direct form. Early light incorporation followed by later lengthening is not excluded by the ending. Nor does a synthetic *j* or *ʝ* probe establish independently that assimilation postdates or predates the merger.

**Chronology:** Under short-final *awidi* and regular retention rather than renewal, the ‘flock’ direct cell gives independent evidence, unrelated to ‘hay’, for **HVD before the onset of heavy resolution**. The pre-HVD heavy alternatives feed deletion, contrary to the attested ending. It places no requirement on the timing of an independently light first step. No additional edge is independently demonstrated against weak-vowel lowering, *h*-loss or the merger by this witness; the evidence therefore favours a post-HVD heavy change without identifying one shared calendar window for *w*- and *h*-loss outputs.

## Verdict

**DEFER** choice of nonfinal mechanism and any production chronology edge. Retain the incumbent SC063 implementation and verdict; the attested cell gives a conditional historical preference, not a corpus adoption.

`Registry-verdict: SC063=REFORMULATE`

## Propagation and residue

Only the private launcher, assay, record and compressed receipt change. No baseline, registry, corpus or publication fingerprint changes. The executable controls cover early/late loss, early serial weight, the long and lowered tail sensitivity, both private nuclear weights and ‘key’. The short-final reconstruction, historical weight of a possible nucleus, renewability of the ending and stress representation after *h*-loss remain separate questions. The early ‘strew’ projection continues to be collapsed by every nonfinal arm from the *w*-loss input; its evidential status is the next independent inquiry.

**Replay:** Two small private component compilations and 108 × 17 local traces on the frozen cache; no default-suite expansion or production rebuild.

```sh
set -o pipefail
cycle=Germanic/articles/hay/research/hiatus-cycle3
bash "$cycle/run-container.sh" --chronology --stage-cache /tmp/capr-hay-stress.lVemXDSn |
  gzip -n -9 | cmp "$cycle/chronology-traces.json.gz" -
```
