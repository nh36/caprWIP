# SC047: matched historical models

## Identity and question

SC047 (`OEHeavySyllableNasalApocope`), compared with SC041 and SC010;
branch `research/sc047-labial-discussion`, research baseline
`b5fc278fe2e7884afbbaaf3eacf6c456a91736f0`. Does inherited short nasal
`*-ą` still protect `*j` when gemination applies? A securely inherited,
early nonlabial singleton-plus-high-vowel nasal direct cell would
favour A, especially if it coexisted with a protected double. An
inherited English nasal direct geminate demonstrably predating stem
replacement would favour B. The observed final double alone does not
establish that premise.

## Current state

The live SC047 fragment deletes the short final nasal vowel in its
licensed context. Production puts SC010 before both SC041 and SC047;
it is not the published split order. The canonical controls and
unchanged selected rows are the same as in the [prior adjudication](../../../../audits/sc047-adjudication.md).
Its 158 live SC047 applications are an executable census, not dating
evidence. The selected deer input is `*déuzô` → *dēora*; `*déuzą` is
unscored. No source, corpus, registry or generated book is replaced.

## Diagnosis and reproducibility

**SC047-A-early-v1** and **SC047-B-split-v1** are labels `A` and `B`
in the [runner](../run_parallel.py), at revision
`60d6e3f0f3631fbdb63588830650b57a413af1e3`. Their exact operations
and definitions are the `early` and `split` entries and `FW`, `FON`
and `FNU` in the [archived plan](../../labial_review/plan.json);
the runner is also the supplemental input manifest. It inherits the
same compiler and final canonical reference bins; the capture records
input digests, complete orders, all 394 rows, and full checkpoint traces
after the common prefix. The corpus and contextual metadata are not
modified by probe construction.

Use the pinned execution revision or this report's checkout, which
retains the same runner and model inputs. Start a healthy Germanic
backend with fresh canonical bins (the assay refuses a stale build
manifest). Run from the repository root:

```sh
mkdir -p .capr-work/sc047-parallel
docker compose exec -T backend python3 /usr/app/docs/sound_changes/literature_dossiers/sc047_paired_chronologies/comparative_followup/run_parallel.py > .capr-work/sc047-parallel/observed.json
```

In this report's checkout, regenerate the tables without running Foma:

```sh
python3 Germanic/docs/sound_changes/literature_dossiers/sc047_paired_chronologies/comparative_followup/summarize_parallel.py .capr-work/sc047-parallel/observed.json .capr-work/sc047-parallel
```

The runner compiles one isolated image shared across both arms and the
identity control. It creates no registry inputs or canonical outputs.
The identity control must agree row-for-row with the existing final
bin. [Matched cells](matched-cells.tsv) show the shared oral checkpoint,
the first divergent step in the three-operation block, the actual
post-nasal and post-gemination checkpoints, and final outputs.
[Changed outputs](changed-outputs.tsv) are exhaustive for the two
arms. The raw [capture](observations.json.gz) includes feeding,
bleeding and unchanged control paths, with multiplicity or rejection
preserved rather than repaired.

The run contains 52 unscored probes and traces for 15 scored controls.
All 394 outputs in each of identity, A and B agree row-for-row with
both authenticated earlier captures; the A/B orders are identical
as well. The raw JSON SHA-256 is
`bffedc5f370422522927578171fc6db9e3b8e89b796875bec2299a3e2f2dab8e`;
the archived gzip SHA-256 is
`f2962dde3a9f0e1771c6de1bab6cbd2b18f0f844bbddfcb6807b7dab81e43060`.
`∅` denotes no transducer output, not a zero ending.

### Relative chronology and dependencies

| Phase | Shared or model-specific operations |
|---|---|
| Shared prefix and preparation | Same input gate, earlier consonant adjustments, and `PWGmcIjContraction`. Move u-lowering immediately thereafter so its low-vowel triggers are still present. Keep `PNWGmcMonosyllabicFinalRLengthening` (SC112) next: it sees `*dórą`, not a newly exposed final `*r`, and short *dor* survives. *There/where* and all 40 lowering firing identities are preserved in the authenticated [census](../source_integration/README.md). |
| Ending exposure and oral loss | Move `EAFFinalZDeletion` before SC041; an oral `*-az` can become bare `*-a`. SC041 deletes that vowel and `FON` immediately vocalizes stranded consonant-following `*ij/j/w` as `*ī/i/u`. No gemination on this oral path in either model. |
| Nasal loss and gemination | **A:** SC047 → `FNU` → SC010. **B:** SC010 → SC047 → `FNU`. `FON` is an alias of `FNU`; the same operation is applied to newly stranded glides. Protected `*CjV` remains eligible for gemination in both. |
| Subsequent consonants and vowels | Both retain the ordinary `PWGmcSyllabicJ` and subsequent u-independent developments. `FW` extends `PWGmcEndinglessAw` to also handle newly exposed word-final `*aw/*áw`. The later `MonosyllabicFinalZLoss` still precedes `EAFRhotacism`: newly exposed final `*z` of direct ‘deer’ can disappear; the selected genitive keeps it internal. Other consonant treatments, including `PNWGmcPreconsonantalXLoss`, `NWGmcInStemNLoss` and the late treatment of final nasals, are not moved. |
| Labials, final vowels and simplification | The same existing labial consumers (including `OEAwwjResolution`, `OEEwLongDiphthong`, `OEJWWSimplification` and `OEJGlideIO`) follow the intervention. Neither arm delays vocalization specifically for `*wwj`. After mutation and weight marking, `OEHighVowelApocope` deletes eligible high vowels after heavy syllables; subsequent lowering accounts for light-stem *-e*. `OEFinalGeminateSimplification` and the surface rules are identical in both arms. |

Final-*z* loss feeding oral apocope and surviving *j* feeding gemination
are supported historical relations in A and B; phonological
vocalization removes that conditioning. The SC112 placement,
u-lowering trigger visibility and `FW` recovery are implementation
constraints, not independent demonstrations of absolute historical
stage, geographical scope or adjacency. Protected cases are positive
controls; *ende* and the oral masculine nominatives are shared bleeding
controls. Direct ‘deer’ is a useful final-consonant diagnostic, not
evidence for labial or nominal levelling chronology.

Labial preservation is a **separate sensitivity**, not included in
either primary ID. The [labial trials](../../labial_review/) and
[matched archive](../source_integration/README.md) distinguish
`FNS` (defer singleton `*Vwj` and doubled `*wwj`) from `FNG`
(defer doubled `*wwj` only); `FII` (short stressed + unstressed
*ii* contraction) and `FWA` (narrow high-front exclusion on
the SC034 proxy) are downstream hypotheses. The base arms have the
same immediate-vocalization treatment. The archived geminate-only
preservation with the matched downstream options recovers hay and hue
in B; it does not recover attested hay from A's singleton. Moving
the labial consumers earlier disturbed unrelated believe/straw.
This locates a real additional dependency rather than establishing
that hay and hue are two independent chronology witnesses.

## Literature and comparative register

| Witness | Evidence and scope |
|---|---|
| Ringe–Taylor pp. 44–47, 173–174; Campbell §576 (pp. 229–230) | A: oral and nasal losses precede gemination; direct singleton with vocalized *i*, doubled before a protected syllable. Both need neuter replacement if English direct geminates are remodelled. |
| Dahl pp. 81–86; Hogg (1979) pp. 68–73; Hogg–Fulk §2.23 (pp. 19–22) | B: oral nominative gives singleton; nasal accusative and neuter direct cells give inherited doubles. The proposal for *hyll* assumes the accusative outcome, it does not attest it; *hyle* is reconstructed. |
| Boutkan pp. 209–213, 435–436; Versloot pp. 79, 86–87 | Gemination-first needs an independent account of southern singleton-plus-*i*. The northern executable ordering in the archive does not test that. Continental vowel retention after z-loss and Frisian regional reduction do not date nasal loss relative to gemination in English. |
| OHG *peti/bedi* | [Primary collation](../morphology/peti.md): Clm 18550a 154v.22 `p&i` (Bavarian, second quarter ninth century), acc. *stratum*; Frankish *bedi*, acc. *culcitram*. Doubled *betti/bette* in Tatian. Two manuscript witnesses, one lexeme; vernacular case inferred, singleton inheritance not directly witnessed. A gives the singleton mechanism; B needs separate change, transfer, or a regional chronology. No OHG output is inferred from the OE FST. |
| OHG *hewi* type | [AWb IV col. 1043](https://awb.saw-leipzig.de/?sigle=AWB&lemid=H02092) indexes nom. *heuui* (Gl. III 16.34); Notker's Psalter has nom. *houue* (36.2, variant *houui*), acc. *houue* (146.8), gen. *heuues* (105.20). The normalized singleton type is labial, not a second nonlabial ‘bed’ witness; neither the manuscript spellings nor the paradigm guarantee the direction of levelling. These are not OE outputs. |
| *mene*, *dili* | Corpus Glossary C887 *maenoe* glosses *crepundia*, but the inherited gender and vernacular cell are not secure; Old Saxon *(hals-)meni* is a compound, not equivalent independent evidence. *Dili* is genuinely singleton with a high vowel, but a class-ambiguous isolated gloss, not an inherited nasal neuter direct cell. Their proposed OE inputs in the trace register are conditional. |

## Historical analysis: forms versus interpretation

The inherited reconstruction for *nett, bedd, wedd, cynn* is supported
independently of English doubling (Kroonen, respective entries; compare
Gothic *nati, badi, wadi, kuni*). Nasal versus oral is a phonological
condition, not a case selector in the transducer. The truth of the
nasal-loss edge for Old English and the geographical extent of either
schedule remain unproved. Consult the [attestation register](../morphology/english-cells.md),
[paradigms](../morphology/paradigms.md), [early witnesses](../morphology/early-oe-witnesses.md)
and [original-source assessment](../morphology/early-oe-levelling.md).

| Cell(s) | Attestation and morphological interpretation, not FST rules |
|---|---|
| *nett* nom./acc.; gen., dat. and plural | Luke 5:6 subject *net* and John 21:6 object *nett* do not attest *nete*. Dative *nette* (Paris Psalter 89.10), plural *nett* (Matt. 4:22) and *nettum* (*Colloquy* 21.21–22.11) are usable donors for A; *nettes* is predicted only. B needs no direct replacement. |
| *bedd* nom./acc.; gen. and dat. | Épinal–Erfurt 243 *bedd* is isolated; the accusative *bedd* (Paris Psalter 40.3) has oblique *bedde* in the same passage. Gen. *beddes* (*Beowulf* 1791), dat. *bedde* are real donors. A requires replacement of its singular direct stem, B does not. |
| *wedd* nom./acc.; gen. and dat. | Ælfric, Thorpe II 272.6–8 has subject *wedd*, object *wed*. Gen. *weddes* (Gen. 9:12), dat. *wedde* (Gen. 17:13) supply donors. Single final spelling is not *wede*. |
| *cynn* direct; gen. and dat. | Attested *cynn*, *cynnes*, *cynne* (BT, s.v. *cynn*; Hogg–Fulk §2.20). Final-n simplification makes the direct output less transparent than the intervocalic donors. |
| *seċġ*, *hyll* nom., acc. and protected dat. | Both predict the ungeminated inherited nom.; A also predicts an ungeminated acc., so relies on doubled obliques or a doubled plural. B predicts a geminated acc., allowing direct-case syncretism. Attested obliques and the resulting direct forms are not attestation of the starting opposition or its direction. *Hyle* in Hogg's table (23) is hypothetical; alternate stem analyses of *hyll* remain possible. |
| *hyse* ja-stem probes | *Maldon* tradition: nom. *hyse*, gen. *hysses*, pl. *hyssas* and *hysas*. Lost original; inherited class unproved. The conditional nasal *xúsją* gives *hyse* in A and *hyss* in B. The proposed oral *xúsjaz* and protected *xúsjai* are rejected at the shared `EnglishProtoInput` gate; this neither adjudicates the historical class nor refutes a protected donor. Their lack of output is left explicit. |
| *mete* i-stem | Vespasian Psalter, Hymn 6.37, has acc. pl. *mettas* and prepositional singular *from mete* (Sweet p. 409). Acc. sg. *in mete minne*, p. 282; gen. pl. *metta*, p. 247. Neither chronology regularly generates an analogical plural by selecting this i-stem; the i-stem probes are controls, not substitutes for the attested plural. |
| *hay, hue, strew; rīċe; searu* | The direct labials diverge early, but later labial consumption/hiatus controls their endpoints. Protected forms are possible donor material, not evidence of transfer. Heavy `*rīkij` yields `*rīkī` in either arm. Both direct wa-stem probes give *saru* after restoration; *searwes* is the attested broken oblique supporting extension of its diphthong to *searu*. The regular direct output and the analogical account belong to separate layers. |

Adamczyk (2018: 150) finds doubled stems in **86% of eligible plurals,
4% of eligible singulars** in the relevant **light i-stem** subgroup.
This supports productivity of restructuring and the coexistence of
different stems, not a general tendency toward oblique-to-singular spread
in neuter ja-stems. A can posit one pattern of stem extension to the
neuter direct cases, with a doubled bare stem copied from a plural where
available, or an oblique stem extended before high-vowel loss. Which,
when and how generally are unproved. B's available masculine direct
accusative gives a more specific structural motivation, but syncretism
and direction must still be distinguished.

## Verdict and propagation

Retain the executable setting; defer the historical relation of nasal
loss to gemination. Continental singleton evidence gives A a specific
comparative advantage, whereas B directly accounts for English nasal
neuter geminates and offers a direct-cell donor for masculine
syncretism. Neither advantage resolves the inheritance/levelling
premises. Regulation by scope is possible but not independently shown.

`Registry-verdict: SC047=REFORMULATE/RETAIN`

Production propagation: none. Frozen reference: 394 accepted, 386
matches, eight inherited mismatches, fingerprint
`8405a0661e893ba512b032dcd427c7f812c5688fa09cba1b271fe42afdd1c900`.
Base-arm diagnostics are 381 A and 382 B (five and four changed rows
respectively); neither score has historical-probability meaning.
Validation cost: one isolated definition compile shared between two
arms and the identity control, opt-in only; no CI fixture, rebuild,
worker concurrency, validation lane, or production certificate added.
The backend image used locally was
`sha256:91065f6b1fe4c180737956d44b5ce0158787d396cb9c1557a5f4d86023b12b13`.

## Residue and bounded source follow-up

- **Dill:** Corpus Glossary A571, fol. 8v left, *dili* for *anetum*
  does not secure the vernacular case. Hatton 20 *Pastoral Care*,
  Sweet 439.28, is an accusative according to Dahl p. 84. The
  dictionary's examples *diles blōstman* and *diles sædes* supply
  singleton protected genitives, not doubled donors (Cockayne,
  *Leechdoms* II 20.7, 190.9, 192.14, cited in
  [BT *dile*](https://bosworthtoller.com/7702)). These are edition
  reports, not new checks of the medical manuscript's spelling.
  Kroonen p. 93 distinguishes the English i-stem analysis from
  Continental ja-stems; the English form cannot adjudicate its own
  inheritance by agreement with a hypothetical ja-stem output. No
  securely inherited English doubled protected form was established.
- **Continental *weti*:** Kroonen p. 564 and Boutkan p. 201 are
  leads. The [DWDS etymology](https://www.dwds.de/wb/etymwb/Wette)
  gives doubled *wetti* from the eighth century.
  [Köbler 2014, s.v. *wetti*](https://www.koeblergerhard.de/ahd/ahd_w.html)
  lists a normalized ja-stem headword, gloss collections and several
  Latin equivalents; the third-quarter eighth-century Winithar
  Paulus glosses (St Gall 70) are among the indexed sources. Its
  apparatus does not identify a diplomatic singleton token. No
  independently identified singleton manuscript, case, date and
  spelling was secured; do not count it as a second independent
  “bed”-type lexeme.
- **Dal:** The [DNB catalogue entry](https://www.deutsche-digitale-bibliothek.de/item/KJAF6XDEY3LZB4UXJA7JMASXBZPP7TCV)
  identifies the 1971 volume and [HathiTrust](https://catalog.hathitrust.org/Record/000008483)
  lists search-only access. The article (1934: 243–252; reprint
  pp. 65–73) was not obtained; earlier citations remain mediated.

Prioritize Dal when obtainable and an independently traceable
singleton *weti* locus if one is identified. A further undirected
English dictionary or glossary sweep is unlikely to settle the
order; a genuinely inherited nonlabial direct/oblique contrast
would justify reopening the philological search.
