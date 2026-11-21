\appendix

# Testing the Chronologies of Final Low-Vowel Loss {#sc047-technical-appendix}

## Scope and reproduction

The two configurations are **SC047-A-early-v1** and **SC047-B-split-v1**. They share reconstructed inputs and differ in the order of nasal loss, vocalization of the resulting stranded glide, and gemination. The identity arm is the canonical cascade, not a third historical hypothesis. Both proposed chronologies lose oral \emph{*a} before gemination; the identity arm does not. There is no analogical operation in any arm.

The executable source revision is `60d6e3f0f3631fbdb63588830650b57a413af1e3`. The accompanying research supplement, *SC047: matched historical models*, specifies the container command and input manifest. Its `observations.json.gz` preserves the exact input digests, the complete orders, every selected endpoint and all checkpoints following the common prefix for the probes and traced controls; `matched-cells.tsv` and `changed-outputs.tsv` are tabular views. The comparison uses the frozen 394-row corpus, not a separately optimized corpus for each chronology. Five of the 52 unscored inputs, including the conditional nominative and dative of *hyse*, are rejected by the shared input gate; they supply no negative phonological evidence.

## Relative order and additional assumptions

In both arms the common prefix includes the inherited input checks, early consonant adjustments and contraction of \emph{*ij} in the environments already defined for that contraction. The experimental u-lowering is placed before losses that would remove its triggers. The special final-\emph{*r} lengthening rule immediately follows lowering and still sees *dor* ‘door’ with \emph{*ą} intact; the short vowel survives, and the adverbial controls ‘there’ and ‘where’ are unchanged. These are constraints on the serialized assay, not historical dating evidence for lengthening. Final \emph{*z} deletion then exposes short oral \emph{*a}, which falls. A shared vocalization treats newly final consonant-following \emph{*ij}, \emph{*j} and \emph{*w} as \emph{*ī}, \emph{*i} and \emph{*u} respectively.

| Order from the shared oral checkpoint | Model A | Model B |
|---|---|---|
| First | Loss of short final nasal \emph{*ą} | Gemination before surviving \emph{*j} |
| Second | Vocalization after nasal loss | Loss of short final nasal \emph{*ą} |
| Third | Gemination before surviving \emph{*j} | Vocalization after nasal loss |

The ordinary syllabic-glide treatment follows this block. A shared expansion of endingless \emph{*aw} treatment recovers newly exposed final \emph{*aw} without changing the historical hypothesis being compared. Later loss of newly exposed final \emph{*z} precedes rhotacism. For ‘deer’, direct \emph{*déuzą} gives reconstructed \emph{*dēo}, whereas the selected genitive plural \emph{*déuzô} protects internal \emph{*z}, giving *dēora* ‘of deer’, attested in Ohthere’s account, *Orosius* I.1 §15 [@Bosworth1859, p. 20, lines 25–27]. The direct singular is not scored. The same labial rules, fronting, mutation, high-vowel loss and final consonant simplification follow both trial blocks.

Immediate vocalization removes \emph{*j} from a newly endingless doubled labial before rules that otherwise consume the doubled cluster. Preservation of \emph{*wwj} through those rules is a separate phonological hypothesis. Other tests separately delay vocalization of singleton \emph{*wj}, contract short stressed and unstressed \emph{*ii}, or narrow a singleton-\emph{*aw} diphthong proxy. These tests distinguish the initial chronological fork from later dependencies; none is used to give one principal model a different set of downstream rules.

## Matched derivations and witness status

The illustrative derivations below omit unrelated intervening rules. The archived checkpoints give the actual executable strings and rule order. For a nasal direct form, the first divergence in the central block is the immediate removal of the nasal vowel in A versus doubling with the vowel still present in B. An oral nominative joins the shared vocalization path before the block. A protected form can already geminate at the first step of B, but A catches up at its third step: this difference in timing does not make the protected endpoint a historical discriminator.

| Cell | Input | Early loss | Split loss | Evidence and interpretation |
|---|---|---|---|---|
| *nett*, direct sg. | \emph{*natją} | \emph{*natj} → \emph{*nati} → \emph{*nete} | \emph{*nattją} → \emph{*natti} → *nett* | Luke 5:6 nom. *net*, John 21:6 acc. *nett*; either inheritance in B or replacement in A. |
| *nett*, dat. sg. | \emph{*natjai} | *nette* | *nette* | Paris Psalter 89.10; attested donor in A, not evidence of spread. Genitive \emph{*nettes} is predicted. |
| *bedd*, direct sg. and protected dat. | \emph{*badją}, \emph{*badjai} | \emph{*bede}; *bedde* | *bedd*; *bedde* | Paris Psalter 40.3 (accusative and oblique); *beddes* at *Beowulf* 1791 adds a genitive donor. |
| *wedd*, direct sg. and protected dat. | \emph{*wadją}, \emph{*wadjai} | \emph{*wede}; *wedde* | *wedd*; *wedde* | Ælfric, Thorpe II 272.6–8, nom. *wedd* and acc. *wed*; Gen. 17:13 dat. *wedde*. Letter count in the direct form does not attest \emph{*wede}. |
| *cynn*, direct sg. and protected dat. | \emph{*kunją}, \emph{*kunjai} | \emph{*cyne}; *cynne* | \emph{*kynn} then *cyn* by final simplification; *cynne* | Obliques *cynnes*, *cynne* supply actual donors; final double spelling is not the model's consonant-length analysis. |
| *seċġ*, nom. sg. | \emph{*sagjaz} | \emph{*sagi} → \emph{*seġe} | same | Attested nominative *seċġ* requires remodelling in either model. |
| *seċġ*, acc. sg. and protected gen. | \emph{*sagją}, \emph{*sagjas} | \emph{*sagi}; doubled oblique | \emph{*saggją}; doubled oblique | A has an oblique donor; B additionally has a predicted inherited accusative donor, not independently attested before syncretism. |
| *ende*, oral nom. sg. | \emph{*andijaz} | \emph{*andī} → *ende* | same | Published heavy-stem oral control; distinguishes neither A nor B [@HoggFulk2011, pp. 19–22]. |

Three comparison types must be kept apart. First, Continental *peti/bedi* belongs to one independently supported nonlabial neuter lexeme, with two manuscript witnesses. It supports early loss if inherited, not an Old English output. Contemporaneous scope, transfer and the southern developments postulated by Boutkan remain questions. *Hewi* has additional labial complications; the reported *weti* lacks an independently verified singleton locus. Second, a reconstructed *hyle* and an inferred accusative *hyll* are not attested early nominative and accusative forms. The *Maldon* spellings *hyse*, *hysses*, *hyssas* and *hysas* are evidence of alternation, but do not secure inheritance or direction. The declension of *mene* is uncertain, and the Corpus Glossary *dili* is not a parsed, independently classified nasal neuter direct cell. Third, the paired *mettas* and *from mete* in the Vespasian Psalter are independently an i-stem comparison, not an estimate of how often a light neuter ja-stem adopts a new direct stem [@Hogg1979Analogy, pp. 68–73; @Adamczyk2018, pp. 148–151; @Lindsay1921, A571; @Sweet1885, p. 409].

## Complete changes in the selected corpus

| Selected item | Canonical | A | B |
|---|---|---|---|
| hay | *hīeġ* | \emph{*hēa} | \emph{*hewe} |
| hedge | *heġġ* | \emph{*heġe} | \emph{*heġe} |
| net | *nett* | \emph{*nete} | *nett* |
| rest | *ræste* | \emph{*rast} | \emph{*rast} |
| hue | *hīew* | \emph{*hii} | \emph{*hiewe} |

There were 386 canonical matches, 381 in A and 382 in B. The shared change for ‘hedge’ reflects the early oral path; ‘rest’ has an exposed stressed-vowel development, not a diagnostic ja-stem direct opposition. The experiments classify the two labial departures separately rather than treating them as independent votes for an order. The full traces also preserve the unchanged controls, including strew, the selected deer cell, and the door and adverb controls. Other grammatical cells are unscored; they do not affect either count. No model is entitled to count an analogically supplied result as a regular phonological match.
