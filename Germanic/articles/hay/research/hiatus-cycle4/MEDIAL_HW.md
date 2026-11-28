# A3a — Independent labiovelar controls

## Question and source entry

Is the narrowly intervocalic reduction used for ‘see’ supported beyond that verb? The [earlier assay](../hiatus-cycle2/STACKS.md) found the candidate useful on one full entry and exercised initial controls, but that cannot establish the positive domain of a general development. Ringe & Taylor (2014: 48–50) distinguish Proto-Germanic unit labiovelars from West Germanic dorsal-plus-labial sequences. The printed p. 179, checked against the page image, supplies **long** *ī* for two new families: PGmc *līhʷaną* and *sīhʷaną*, PWGmc *līhwan* and *sīhwan*. The FST only encodes the labiovelar as `xw` at full admission. Those full inputs cannot themselves test the earlier historical split of a unit consonant.

| Family and cell | Independent source | Role and limits |
|---|---|---|
| ‘See’, infinitive | Ringe & Taylor 178, 315, 317: PGmc *sehʷaną* > PWGmc *sehwan* > pre-loss *seohan*; West Saxon *sēon*, Mercian *ge-sian/ge-sean* | Established positive. The Anglian smoothing comparison is separate; the absence of *w* and absence of *h* are not one operation. |
| ‘Lend’, infinitive | Ringe & Taylor 179, 344–345: PGmc *līhʷaną* > PWGmc *līhwan* > pre-loss *līohan* > *līon* > *lēon*. Past singular *lah/on-lēah* and participle *on-ligen* are different paradigm members | Newly tested positive. The participial velar reflects levelling on their analysis, so it is not a negative built from an inherited intervocalic *hw* input. |
| ‘Filter’, infinitive and participle | Ringe & Taylor 179, §6.2.4, 344–345; [Bosworth–Toller, *seón*](https://bosworthtoller.com/27502), inflected citations including *bi-seón* and *ā-seowen/ā-siwen* | The infinitive is another positive (*sīhwan* > *sīohan* > *sīon* > *sēon*). The participle continues a voiced Verner alternant with *w*, not another input to fricative-cluster reduction. The local participle probe omits the prefix. |
| ‘Sieve’, direct singular | Ringe & Taylor 49, 178: *sihhwā* > *siohhæ* > *seohhe*; [Wright’s glossary attestation via Bosworth–Toller](https://bosworthtoller.com/27470), Wrt. Voc. I.24.52 ⟨Seohhe⟩ | An inherited geminate environment in the ‘filter’ family. It supplies evidence for the distinction between singleton loss and geminate retention; its own *w* is also lost in the published history. It is not a claim that the geminate must forever keep its labial, and not an independent fourth root. |
| ‘Horse’, direct singular; ‘white’, direct singular; ‘turn’, infinitive | Ringe & Taylor 49, 178: *ehu* and protected *ehw-* beside *eoh*; *hwīt* > *hwīt*; *hwerban* > *hweorfan* | Initial negatives and a final cluster **sensitivity**. The local final *ehw* is not equated with the published direct *ehu*. The full ‘turn’ approximation is rejected upstream; the local negative and admitted full ‘white’ are the pertinent comparisons. |

## Executable diagnosis

The [isolated replay](medial-hw-traces.json.gz) applies narrow `HwMed` and the earlier broader `HwRed` to the same structural cases. Narrow `HwMed` changes the three independent medial singleton entries and no initial, final, voiced or geminate control. `HwRed` also acts on initial ‘white’ and geminate ‘sieve’. The initial effect is unwanted; the latter could produce a historically valuable intermediate but folds a separate quantity context into an otherwise over-broad rule. Correctly retaining geminate *h* does not by itself explain how or when the geminate cluster lost *w*.

In all three full orders, the new long-vowel infinitives actually fire before breaking. They acquire `*īo`, after which singleton h-loss leaves `*īo*a`; the present isolated comparison ends in *līoan/sīoan*, not the attested normalized *lēon/sēon*. ‘See’ likewise reaches *seoan* without the independently tested back-tail contraction. These are endpoint gaps after successful cluster reduction and singleton loss, not counterexamples to either in isolation. The frozen ‘sieve’ probe ends in *siohhwe*; its missing geminate de-labialization and subsequent realization remain separate. The full early probe for ‘turn’ has an admission gap, so its empty trace cannot count as a successful negative.

**RETAIN** narrow `HwMed` as a candidate component. **DEFER** the exact historical placement of de-labialization relative to breaking and the generalization about other singleton environments. The sources give *h* without *w* in the pre-loss stage; the frozen implementation shows it feeding singleton h-loss, but inserting the operation before breaking establishes no independent historical ordering between those two. The conclusion is not calibrated to the successful spelling of ‘see’. These audited cases are **development** evidence and must not be relabelled as withheld validation. The production rules, historical metadata and targets are unchanged.

```bash
set -o pipefail
c=Germanic/articles/hay/research/hiatus-cycle4
bash "$c/run-container.sh" medial_hw_check --stage-cache /tmp/capr-hay-stress.lVemXDSn |
  gzip -n -9 > /tmp/capr-hay4-hw-replay.json.gz
```

Validation cost: one private isolated two-export build and 13 full or local traces per arm and order; no new default-suite execution or wide-corpus sweep.
