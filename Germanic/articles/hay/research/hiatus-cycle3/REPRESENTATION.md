# R2: stress, syllabicity and weight controls

**Question.** Does the matched front-hiatus window recognize
stress after *h*-loss, and is early high-vowel loss a consequence
of the historical analysis or of the selected token class?
Use [the R1 substrate](STACKS.md) and retain the accepted
[S1 diagnosis and failed S2 alignment](../hiatus-cycle2/STRESS.md).
The following are controlled Foma inputs, not new attestations.

| Comparison | Result |
|---|---|
| Plain, head-marked and posttonic *e.i* | Before `OEHLoss` the foot marker locates a prefixed plain root. The component strips it even without a consonant firing, and the same plain root is then missed. Independently accented *é.i* remains eligible; a genuinely posttonic plain input remains unchanged. S1 protects the root at SC083 but does not restore lost accent downstream. |
| Cycle 2 incorporation of *é.i* | `NuDN` emits plain atomic `*ei`, just as for *e.i*. `NaDN` has an acute input clause, but this path never feeds it. |
| Local alternative | `RpNu` emits private atomic `*ėi` or `*éi`, respectively, and `RpMo` lengthens them to `*ē` and `*ḗ` before *d, þ/ð, n*. Inherited `*ei` is not affected by `RpMo`. This narrowly repairs the information loss without applying S2's general tag lift through unrelated components. It does not repair the full-cascade ‘world’ alignment or make unmarked post-*h*-loss heads detectable. |
| Weight | Frozen HVD retains the final high vowel in `*t*e*i*d*i` but deletes it in `*t*ei*d*i`, `*t*e*j*d*i` and `*t*e*ʝ*d*i`. Existing `*ei` is classed long; both palatals count as consonants in this frame. Frozen HVD rejects unknown private tokens, rather than deciding that they are light. With local alphabet admission and no other substantive change to HVD, the short nuclear arm retains final *i* and the long arm deletes it, independent of accent. |
| Serialization | The frozen printer renders syllabic `*e*i` and atomic `*ei` alike; the fricative and the approximant also converge in print after merger. The alternative explicitly serializes both private nuclei as ⟨ei⟩ at the output boundary. Identical spellings do not establish identical syllabicity or quantity. |

**Verdict:** retain S1. Use the private tokens only in comparisons
with explicit alphabet/weight treatment, or when they are contracted
or serialized before exiting the local assay. Do not equate loss of
an unsupported token with historical deletion, or class `*ei` as
long solely because the inherited atomic diphthong is long in CAPR.
This is a diagnostic of model structure, not an order edge or new
production proposal. No full-cascade tests are added to the default
suite; one private compilation and focused component lookups per
replay. Reproduce the [receipt](representation-traces.json.gz) with:

```sh
set -o pipefail
cycle=Germanic/articles/hay/research/hiatus-cycle3
bash "$cycle/run-container.sh" --representation --stage-cache "$cache" |
  gzip -n -9 | cmp "$cycle/representation-traces.json.gz" -
```
