# Q2a — Ringe & Taylor source-to-input audit

## Identity and question

Research only, `research/hay-article`, parent `18f64afe`; no production SC verdict or chronology edge is changed. Could a printed diacritic or a stage-local simplification be responsible for an apparent historical diagnostic? The [comparison ledger](source-entry-audit.tsv) separates the printed forms, normalized stages, archived executable inputs, and historical comparators. A mismatch matters historically only where it alters the diagnosis or invalidates identification of the input with the source.

## Current state and literature

The source is the registered Ringe & Taylor (2014) holding (SHA-256 `278f94f6076a31278ecca75d8d0429f0822728e5efe0ec3011186a694cf8d6f2`). Direct images checked here: printed 258–260, 299–301, 317–319 (sheets 273–275, 314–316, 332–334). Q1 already records the [flock](FLOCK_QUANTITY.md) and [three h-loss](H_LOSS_QUANTITY.md) corrections; those receipts remain authoritative. The ledger strips source italics and uses `>` for developments, including those printed in reverse order. Diaereses signal the source's hiatus, not length; superscript *j* on geminates marks palatalization. Source diacritics on cited Old English forms are editorial unless independently verified in the witnesses.

This checkpoint covers the central Ringe–Taylor labial-loss comparisons and the adjacent late-hiatus controls listed in the ledger. It is not the complete inventory audit: independent early back-vowel, h-loss, palatal, stress, dialectal and witness-level comparisons still require their own source checks, including where they have the same headword as an entry here.

## Diagnosis

The targeted comparison is the immutable SC047 frozen cascade and the cycle-three common substrate, each in canonical, A and B2 order. The [replacement receipt](source-entry-traces.json.gz) records pre/post anchors, all changes, complete output and per-build provenance. These are stage entries, not corpus selections or a new general firing census; there is no rule edit or new claim of corpus-wide scope.

- **‘Pillow’:** Ringe & Taylor p. 260 print Latin *pulvīnus* and reconstruct *pulwīn > pylwī > pylī*. The original local `*p*y*l*w*i` is a short-quantity proxy; both frozen and common rules delete *w* from the corrected long-vowel `*p*y*l*w*ī*. The old short probe and the corrected long probe converge at *pyle*, but only the latter separates labial loss, later shortening and lowering. The success is about a postconsonantal position and a fully unstressed high vowel, not hiatus. The separate earlier full-entry admission failure is not reversed by a successful late injection.
- **‘Prepare’:** The publication distinguishes West Saxon *ġierwidǣ* and Mercian *ġerwidǣ* (pp. 258, 260); both corrected entries lose *w*, and produce *ġierede* and *ġerede* respectively. The Mercian local entry has no prefix. The printed infinitive supplies the protected comparison. The valid chronology argument concerns creation of a light syllable before general syncope, not contraction; neither the original split `*i*e` encoding nor pre-lowering the ending is necessary for the stage-local loss.
- **‘Betray’:** The long source tail changes the frozen outcome: the lowered proxy gives *lēide*, whereas *lēwidǣ* gives *lēde* without the common-substrate absorption component. The common substrate gives *lēde* with either input. The output no longer demonstrates a need for that new component. It does not choose between syncope and contraction, as the root was already long (pp. 259, 318).
- **‘Strew’:** Pre-loss *stræwidǣ* produces uncontracted *stræide*; changing just the tail of the old *e*-root proxy does not force contraction. The corrected input retains hiatus but exposes a gap between frozen *w*-loss and the source's *e*-quality at that stage. This is not a new historical raising proposal or a failure of hiatus retention. The written and metrical comparisons retain their earlier lexical and transmission qualifications.
- **‘Higher’:** Both quantities for the final vowel give laryngeal loss. The common substrate absorbs *i* after long *ē* in either test, but with the printed long tail leaves *hērā*, not *hēra*. This is a separate weak-ending realization gap, not evidence for short-root *e.i* before *r*. The strong ‘nearest’ comparison likewise has an independently long root.

## Historical analysis and verdict

**REFORMULATE the research input attributions; RETAIN the recorded experiments; DEFER any new chronology based on these local receipts.** The short-vowel conditioning on p. 258 must be read with the independently identified unstressed long-vowel loan example on p. 260. The novel result here is verifying the long-input behavior of the frozen executable, not discovering the long-vowel historical example. There is no positive evidence for analogy from this replay. The proposal that the inherited short oblique *ehi* underlies the apparently Anglian *ē* ‘of/to a river’ is conditional on ancestry; the source's other derivation from contracted *ēa* remains possible. Neither the printed macron on *ē* nor the archived long *ēhi* sensitivity independently establishes the earlier structure.

## Propagation, validation and residue

Archived table rows, benchmarks and receipts are kept as run. The new ledger and receipt supersede only the source attribution or experimental interpretation specified here. No source used by production regeneration, frozen models, corpus targets or the article changed. The new stage comparisons include both corrected source quantities and archived reduced controls.

```bash
set -o pipefail
c=Germanic/articles/hay/research/hiatus-cycle4
bash "$c/run-container.sh" source_entry_check --stage-cache /tmp/capr-hay-stress.lVemXDSn |
  gzip -n -9 > /tmp/capr-q2-source-entries.json.gz
```

Binary hashes identify the compiled networks actually used. As in Q1b, compare fresh compilations structurally rather than assuming byte-identical Foma exports. Source-backed sets outside this checkpoint remain unaudited; none is silently promoted from “local” to “historical.”
