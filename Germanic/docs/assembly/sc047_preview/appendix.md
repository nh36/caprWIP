\appendix

# CAPR Models A and B2: Technical Appendix {#sc047-technical-appendix}

## Active model outputs

Both models use the same 396 selected inputs and targets. They derive
all six common selections for net, hue, bed, kin, hedge and rest.
A derives 387 of 396 active targets; B2 derives 388. Hay remains a direct
comparison in both models, unmatched in A. The full stage orders,
unmatched forms and unscored probes are published in the model
companions; the 394-input benchmark remains separate from the active
catalogue. Ordinary Old English derivation can use either model; A is
the application default. The compatibility cascade is retained for
replay and is not a third historical hypothesis.

The figures and traces in the following sections are historical
experiment results, not the results of the active catalogue.

## Archived matched comparison: scope and reproduction

The original configurations were `SC047-A-early-v1` and
`SC047-B-split-v1`. Neither archived snapshot has been revised in
place. The initial B has been retired from the active implementation.
The original arms shared reconstructed inputs and differed in the order
of nasal loss, vocalization of the resulting stranded glide, and gemination.
The identity arm was the canonical cascade, not a historical alternative.
Both proposed chronologies lose oral \emph{*a} before gemination; the
identity arm does not. There is no analogical operation in any arm.

The executable source revision is `60d6e3f0f3631fbdb63588830650b57a413af1e3`. The accompanying research supplement, *SC047: matched historical models*, specifies the container command and input manifest. Its `observations.json.gz` preserves the exact input digests, the complete orders, every selected endpoint and all checkpoints following the common prefix for the probes and traced controls; `matched-cells.tsv` and `changed-outputs.tsv` are tabular views. The comparison uses the frozen 394-row corpus, not a separately optimized corpus for each chronology. Five of the 52 unscored inputs, including the conditional nominative and dative of *hyse*, are rejected by the shared input gate; they supply no negative phonological evidence.

## Relative order and additional assumptions

In both arms the common prefix includes the inherited input checks, early consonant adjustments and contraction of \emph{*ij} in the environments already defined for that contraction. The experimental u-lowering is placed before losses that would remove its triggers. The special final-\emph{*r} lengthening rule immediately follows lowering and still sees *dor* ‘door’ with \emph{*ą} intact; the short vowel survives, and the adverbial controls ‘there’ and ‘where’ are unchanged. These are constraints on the serialized assay, not historical dating evidence for lengthening. Final \emph{*z} deletion then exposes short oral \emph{*a}, which falls. A shared vocalization treats newly final consonant-following \emph{*ij}, \emph{*j} and \emph{*w} as \emph{*ī}, \emph{*i} and \emph{*u} respectively.

| Order from the shared oral checkpoint | Model A | Model B |
|---|---|---|
| First | Loss of short final nasal \emph{*ą} | Gemination before surviving \emph{*j} |
| Second | Vocalization after nasal loss | Loss of short final nasal \emph{*ą} |
| Third | Gemination before surviving \emph{*j} | Vocalization after nasal loss |

The ordinary syllabic-glide treatment follows this block. A shared expansion of endingless \emph{*aw} treatment recovers newly exposed final \emph{*aw} without changing the historical hypothesis being compared. Later loss of newly exposed final \emph{*z} precedes rhotacism. For ‘deer’, direct \emph{*déuzą} gives reconstructed \emph{*dēo}, whereas the selected genitive plural \emph{*déuzô} protects internal \emph{*z}, giving *dēora* ‘of deer’, attested in Ohthere’s account, *Orosius* I.1 §15 [@Bosworth1859, p. 20, lines 25–27]. The direct singular is not scored. The same labial rules, fronting, mutation, high-vowel loss and final consonant simplification follow both trial blocks.

Immediate vocalization removes \emph{*j} from a newly endingless doubled labial before rules that otherwise consume the doubled cluster. The B2 prototype uses the geminate-only nuclearizer: it leaves \emph{*wwj} available to those rules, but still vocalizes singleton \emph{*Vwj} and stranded nonlabial glides. The retained \emph{*j} marks conditioning; the assay does not decide whether it was a separate segment or a property of the labial. Other tests separately delay vocalization of singleton \emph{*wj}, contract short stressed and unstressed \emph{*ii}, or narrow a singleton-\emph{*aw} diphthong proxy. Those tests did not alter the archived A or B snapshots.

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

There were 386 canonical matches, 381 in A and 382 in B, with the same original 394 inputs in each. The proposed feminine hedge and accusative rest inputs are not substituted here. The hedge discrepancy compares different formations; rest reflects the selected genitive and a separate interaction of final consonant loss and long-vowel raising. Neither is a vote on the order of short nasal loss. The full traces preserve the unchanged controls, including ‘strew’, the selected deer cell, and the door and adverb controls. No model counts an analogically supplied result as a regular phonological match.

## Prospective comparison with corrected cells

The separate corrected-selection replay substitutes only the feminine nominative \emph{*xágjō} and the long-nasal accusative \emph{*rástǭ}. The two re-executed cells give *heġġ* ‘hedge’ and *ræste* ‘rest’ in all arms. The other 392 inputs, contexts and endpoints come from the frozen runs. With the corrected selection the canonical cascade gives 386/394, A gives 383/394, B gives 384/394, and B2 gives 386/394. Each retains the same eight inherited mismatches. The following are all additional differences:

| Item | Canonical | A | B | B2 |
|---|---|---|---|---|
| ‘hay’ | *hīeġ* | \emph{*hēa} | \emph{*hewe} | *hīeġ* |
| ‘net’ | *nett* | \emph{*nete} | *nett* | *nett* |
| ‘hue’ | *hīew* | \emph{*hii} | \emph{*hiewe} | *hīew* |

In B2, \emph{*xáwwj} passes through \emph{*xáuj} on the way to *hīeġ*; \emph{*xíwwj} passes through \emph{*xíuwj} and \emph{*xīowj} on the way to *hīew*. In B, immediate vocalization gives \emph{*xáwwi} and \emph{*xíwwi} instead. The unscored direct ‘glee’ probe shows the same sensitivity as ‘hue’. Protected inflected cells and ‘sew’ and ‘strew’ retain a prevocalic trigger; ‘new’ still vocalizes its singleton in the oral direct singular. ‘Believe’, ‘straw’ and ‘show’ do not change, and ‘net’ keeps its nonlabial contrast. This isolates a shared representational dependency, not a new chronology or a proof of inherited direct gemination.

## Inherited cells outside the score

The accompanying research supplement, *Inherited and protected cells in the SC047 comparison*, records the inputs, outputs, witnessed cells, donor status and confidence together. The supplementary finite assay uses the same orders and does not amend the original 52 probes.

| Comparison | Shared A/B result or separate limitation |
|---|---|
| Masculine ‘hedge’, \emph{*xagjaz} versus feminine \emph{*xagjō} | The former strands the glide and gives *hege*; the latter retains a vowel through gemination and gives *heċġ*. Feminine \emph{*xagjǭ} gives oblique *heċġe*. This is a stem-class distinction, not a short nasal contrast. |
| ‘Rest’, \emph{*rastō}, \emph{*rastōz}, \emph{*rastōi}, \emph{*rastǭ} | Nominative and genitive give \emph{*rast}; the genitive enters final-\emph{*ō} raising after earlier \emph{*z}-loss. The long nasal accusative gives *ræste*. The PGmc dative spelling is rejected; the published West Germanic stage \emph{*rastē} motivates the expected *ræste*, not a successful lookup of the PGmc input. |
| ‘Hay’, genitive and direct plural | Both give \emph{*hīeġes} and \emph{*hīeġ}, potential donors, not verified tokens of those cells. For A’s singleton route the narrower labial experiment gives \emph{*hei}, not \emph{*hīeġ}. B’s direct cell geminates but loses the conditioning glide early. |
| ‘Hue’, genitive and direct plural | Both give *hīewes* and predicted \emph{*hīew}; the Cotton genitive verifies the former stem. Short-\emph{*i.i} fusion under A is independent of preserving the geminated cluster under B; neither is incorporated in the matched models. |

The original rejections of ‘army’, ‘yellow’ and the conditional *hyse* forms are not findings about their historical reflexes. A component assay on specified post-admission strings can test whether the remaining rules behave as expected, but it is not admission of a Proto-Germanic form and cannot independently establish the class of *hyse*. The production gate and its scope are unchanged.

Separate canonical checks reject the inherited dative \emph{*-ōi} inputs for ‘rest’, ‘gift’ and ‘soul’. Later \emph{*-ē} inputs for ‘rest’ and ‘gift’ give *ræste* and *ġiefe*; the later ‘soul’ input is still rejected. These checks identify a limit of the implemented derivation, not a result about the historical reflex of the diphthong.
