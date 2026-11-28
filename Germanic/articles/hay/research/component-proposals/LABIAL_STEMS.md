# B2 — Early labial loss, root quantity, and protected stems

## What distinguishes the ‘claw’ histories

Hogg (2011 reprint: §§3.19.1, 5.10) gives short *klawɔ > klawu >
kla.u > klau > klæu > clēa* in the direct singular, and short
*clawe > clæwe > clawe* in the protected accusative. Ringe &
Taylor (2014: 150, 173) explicitly print long *klāwu > klāu >
clēa*, with *klāwā > clāwe* in the accusative. In their account
English long *ā* remains before *w* plus the nonhigh vowel,
while the Old Frisian cognate *klēwe ~ klē* shows fronting.
Their direct *āu* and short *au* derived by loss converge at
*ēa*. **The English direct outcome cannot choose between them.**

There are positive but competing comparative grounds. Long
OHG *klāwa* and the Frisian front outcome motivate Ringe &
Taylor's quantity; their p. 150 cites ON *kló* alongside the
long-root comparison. But the ON vowel does not directly
measure West Germanic *a*: Kroonen (2013: 292, *klawō-*)
separates ON *kló* (with Faroese *klógv*, Elfdalian *kluo* and
OHG *klō(a)*) as a long rounded ablaut form *klōwō-*. He allows
OHG *klāwa* to continue short *klawō-*. Orel (2003, s.v.
*klōwō / klēwō*) instead lemmatizes two long grades; his
comparison shows disagreement, not consensus for either
quantity in the English accusative. The [EWA entry
*klâwa*](https://ewa.saw-leipzig.de/lemmas/kl%C3%A2wa/) also
distinguishes rounded *klōwō(n)-*, continental long *ā*
forms, and a proposed *klawō(n)-* group. The indexed account
was available; the revised direct article endpoint did not load.
Do not silently treat ⟨ā⟩ in one normalized OHG token as a
measurement in early English, or derive all forms from one
grade without explaining the ablaut evidence.

On the English side, Luick (§100 and the note on intervocalic
*w* after §257) posits short *a* for the original loss, and
uses the metrical short first syllable of accusative *clawe* as
independent support for syllable-initial *w* and a short vowel
in the attested inflected form. Brunner (1965: §§50.2, 128.1,
173) favours short *klawu*, treats isolated Paris ⟨clao⟩ as
inadequate to establish a long ancestor, and questions the rare
*clām* reading as evidence for regular dative loss. Campbell
§§120.3, 598.2 and Hogg & Fulk (2011: 118–119 §3.94)
distinguish the inherited direct and protected cells and
replacement in both directions. A later short inflected form
does not strictly rule out an earlier long grade, but provides
positive evidence for the short English account without adding
a shortening or renewed stem. **Prefer short for that restricted
English explanation; retain long as an independently motivated
comparative alternative.** This ranking is not based on Foma.

## Cell and environment audit

| Family | What must be kept separate |
|---|---|
| ‘Claw’ | The ancestral direct-singular *clēa* is a **reconstruction** (Hogg & Fulk §3.94 n. 2), not the word directly verified in the nominative of an early text. Sweet 463, Ps 68:32, ⟨clea⟩ : *ungulas*, is accusative plural. Ælfric, *Grammar* 55.11 ⟨clawu⟩ is a renewed nominative, with protected *w* available. Épinal/Erfurt 29, Corpus 211 ⟨clauuo⟩ gloss *arpago* ‘hook’, not unequivocally anatomical ‘claw’. Distinguish the transferred dative singular (*Charm* 12.7), later nominative plural and dative plural (*Alexander* 468, 473), protected *clawe* and *clawum*, and the uncertain isolated *clām* in *Phoenix*. The actual direct plurals need not all be levelled: Ringe & Taylor allow regular loss before *ō*, by comparison with ‘lord’ and ‘peacock’, while *clāwa* can be renewed. |
| ‘Knee’, ‘tree’ | PGmc *knewą, trewą* lose an ending, exposing final *w* to vocalization; the neuter direct plurals can reach the same nucleus by loss before raised *u*, not automatically the same event. Compare protected Northumbrian *cnewa* (acc.pl.) and *trewum* (dat.pl.) in Ringe & Taylor 174 and Hogg & Fulk §§3.45–46. Their *w*-bearing shapes do not attest short breaking (*cneowum* can contain a remodelled long diphthong). Distinguish ‘tree’ from the unrelated ‘trough’ and compare the earlier *treu/treo* glossary material in Sweet 621. |
| ‘Threat’, ‘few’ | ‘Threat’ pairs reconstructed *þrawu > þrau > þrēa* with protected *þrawā > þrawe*. Épinal 53 ⟨thrauu⟩ and Corpus 200 ⟨thrauuo⟩ support renewal in the direct cell, not a directly attested protected accusative. ‘Few’ direct neuter plural *fawu > fau > fēa* strengthens the short comparison. Luick §100 and Ringe & Taylor 173 also assign *fēam* to closed loss, with *fēawe* remodelled. The common open-final rule did not test that closed scope. |
| ‘Straw’, ‘servant’ | *strawą > strau > strēa* and *þewaz > þeu > þēo* supply a coda-vocalization route, not deletion of intervocalic *w* before syllabic *u*. Compare *strēaberiġe* and Gothic plural *þiwos*; protected *straw-*, *þew-* supply material for renewed *w*, which need not automatically be a newly inserted consonant. Distinguish ‘servant’ from weak gender-specific derivatives with different source morphology. |

## Reproducible ablations and disposition

The [receipt](labial-stems-traces.json.gz) replays 23 local inputs
on each of canonical/A/B2. The old short loss and incorporation,
the exact addition of long *ā* to the loss context, and forced
convergence of the results are separate controls. For the long
arm, `LongWL` deletes *w* after *ā* before final *u* and `LongAu`
maps *ā.u* to the same executable *au* as the short history.
That last operation is **a deliberately merged projection** of
the authors' common endpoint, not independently demonstrated
early shortening. Donor and renewed forms are explicitly
stage-local; injecting late *clawu* is not a full derivation of
morphological renewal.

| Contrast | Result in all orders except where specified |
|---|---|
| Short ‘claw’ | Frozen *clēaw*; open short loss plus incorporation gives *clēa*. Atomic *au* by itself fails later in the frozen domain; the short comparison includes the established bridge. |
| Long ‘claw’ | Frozen and short arm *clāw*; long loss fires and gives *clā*, just like direct injection of post-loss *klā.u*. Only adding the separately tested merger gives *clēa*. The two required operations are not interchangeable. |
| Protected cells | Long *klāwā* gives *clāwe* and never fires; short *klawa* gives *clēaw* in canonical, *clēawa* in A/B2 (incumbent early *aw* proxy). Short ‘threat’ *þrawā* likewise gives *þrēawe*, not reconstructed *þrawe*. This is not a phonological argument for preferring long. |
| Other direct comparisons | ‘Knee’, ‘tree’, ‘threat’, ‘few’, ‘straw’ and ‘servant’ give the expected nuclei when supplied the separately justified short inputs. Protected controls retain *w* but the later fronting, breaking and weak endings need not match exact protected spellings. ‘Few’ closed-tail sensitivity stays *fēawum*; do not broaden the open loss window just to recover the target. |

**RETAIN** short open loss, coda vocalization and nuclear
incorporation as separately supported historical mechanisms.
**DEFER** a general adoption proposal for long loss and the
representation of its nucleus, and retain the long comparison
as experimental. The exact length of early *clāwe*, and the
earliest distribution of the alleged closed-context loss, would
materially affect the scope. None of the observed convergence
is evidence for the much later *wi* sequence.

```bash
set -o pipefail
bash Germanic/articles/hay/research/hiatus-cycle4/run-container.sh labial_stems --stage-cache "$cache" |
  gzip -n -9 > /tmp/capr-hay5-labial-stems.json.gz
```

Use the [pinned cache warm-up](../hiatus-cycle4/PROSPECTIVE_STACK.md#identity-and-question).
Receipt SHA-256:
`f28f179787a40a27f724824d31783816320a18afdd8239b5f61871cf667debd1`.
One private five-export compilation and focused lookups; no
change to a default validation lane or to any protected target.
