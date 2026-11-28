# Q1b: ‘Receive’, ‘cover’, and ‘rug’ are not short-root controls

## Identity and question

Research-only test of the R8 entries against printed Ringe & Taylor (2014: 317, held PDF sheet 332). The question is whether each entry actually demonstrates new length from short input. The [R8 inventory](../hiatus-cycle3/holdouts-v1.tsv) and [R9 receipt](../hiatus-cycle3/revised-traces.json.gz) remain immutable. The new [quantity ledger](quantity-corrections.tsv) describes the source-aligned inputs and distinguishes the original probes from genuinely different phonological comparisons.

## Source and input correction

| Witness | Page-image finding | Consequence |
|---|---|---|
| ‘Receive’ | The authors print *fanhidi*, then a long nasal vowel, then *fœ̄hiþi* and Mercian *on-fœ̄ð*. The rounded vowel already bears a macron when intervocalic loss applies. | Withdraw the claimed positive short *æ.i* comparison. Preserve earlier nasalization and rounding as separate historical premises, not additional properties of the late local input. |
| ‘Cover’ | Both PWGmc *wrīhidi* and Anglian *wrīhiþi* have long *ī*; the Mercian normalization is *ofer-wrīð*. Compare the uncontracted West Saxon alternative. | Withdraw the identification as short *i.i*. The historic test is loss of a short high vowel next to an independently long vowel of the same quality. |
| ‘Rug’ | The authors print pre-OE *rūhjǣ*, oblique *rūhjan*, early Mercian *rȳhǣ > rȳe* and reconstructed oblique *rȳhan > rȳan > rīan > rīon > rēon*. | Both corridors start with long *ȳ* after mutation. The macron represents the authors’ reconstruction, not a glossary notation. The back-vowel history proposes a change in vowel quality after loss, not the creation of length from short *y*. |

The local executable uses `*ç` for the supplied front-history fricative and `*x` for the back-history comparison; the book writes *h* and does not directly attest those realizations. `*θ` is the established dental input convention. The paired full-ending and tail-less injections in the receipt deliberately do not infer the order of syncope or final loss from the normalized output. The forms start late and do not test early admission or generate the older umlaut history.

## Diagnosis

- **Receive:** The exact rounded long input is rejected at the frozen foot-scoped `OEHLoss`; injection after loss still fails `OldEnglishSurface`. These are representation gaps, not evidence that long *œ̄.i* resists absorption. The separately marked long unrounded proxy shows that the shared `AbsHigh` can give *fēþ* without adding length, but it does not derive Mercian rounded vocalism or the attested prefixed form.
- **Cover:** The original short injection reached *wrīþ* through `OEContraction`; the corrected long-plus-short injection gives frozen *wrīiþ* and shared *wrīþ* through `AbsHigh`. The apparent old success diagnosed the wrong operation. The final-*i* injection remains *wrīþi* in the shared run: that late input cannot test earlier tail loss.
- **Rug:** The corrected front input reaches *rȳǣ* from the source’s *rȳhǣ*, or *rȳe* if the lower weak vowel is supplied at entry. Neither trace establishes a new short-vowel contraction. The corrected back input reaches *rȳan*, not *rēon*. This is a genuine remaining realization gap, but it lies after the observed loss; the old short *ryan* was not a correct diagnosis.

**REFORMULATE** the historical classification of these witnesses; **DEFER** a new contraction or rounding rule. They are late Anglian comparisons, not failures of the frozen West Saxon target convention. Cover motivates testing absorption after independently long nuclei; rug tests both loss and the subsequent properties of unlike nuclei; receive first requires a supported rounded-long representation. No new chronology edge, production verdict, target change or independent demonstration of short *e.i* before another consonant follows.

## Receipt and replay

The replacement receipt applies only to these corrected comparisons. Two substrates (frozen and third-cycle common), 12 stage inputs and all three frozen orders are recorded with verified component hashes. The source-to-input correction does not require rerunning the earlier full corpus or changing saved R8/R9 outputs. Fresh compilation reproduced every trace and the build identity; freshly compiled raw Foma binary hashes differed. Those hashes bind each receipt to the actual binaries used, not to an assumption of byte-identical recompilation.

```sh
cycle=Germanic/articles/hay/research/hiatus-cycle4
bash "$cycle/run-container.sh" quantity_check --stage-cache /tmp/capr-hay-stress.lVemXDSn |
  gzip -n -9 > /tmp/capr-hay4-quantity-replay.json.gz
# Compare the decoded receipt, excluding only the freshly built export SHA-256 values.
```
