# SC017–SC019 chronology and Old English *wull*

Investigation-only scientific report. No production verdict, scientific SOURCE edit, baseline transition, commit or push is authorized or performed. The nine headings follow the adjudication template, but this report deliberately contains no adopted registry-verdict line.

## Identity

SC017 `PNWGmcULowering`, SC018 `PNWGmcStressedMonosyllableORaising`, and SC019 `PNWGmcFinalLongORaising`; production branch `update`, base and remote-tracking HEAD `586ec5f370e58d9038142d330121acf58b085a18`. The base includes completed SC034 and the subsequent rust2162 selection of *rústaz*. SC034's straw input remains *stráwą*, target *strēaw*, regular model output *strēa*: an expressly retained mismatch, not an unfinished adoption.

All experiments use the detached session worktree `sc017-wull-worktree` and the owned, network-disabled `capr-wull-fce1` container. Its scientific mounts are private copies or read-only private-worktree mounts, never production mounts. The original preparation packets are `../wull-sc017-prepare.txt` and `../wull-sc019-prepare.txt`. Existing protected archives and source pins remain unchanged.

## Question

Can final unstressed oral bimoric *ō > u* precede stressed *u > o* and thereby give an inherited nominative *wullu*, while a nasalized accusative *wullǭ* regularly gives a lowered *woll-* stem? If so, does that establish Ringe and Taylor's subsequent nominative-vowel generalization, or merely make it possible?

Two distinct possible defects must not be conflated: an insufficiently demonstrated chronology claim, and failure to recognize a real nasalized vowel in the input and conditioning domains. A third issue is whether early phonetic lowering, phonemicization, and analogy are being dated as a single event. Neither a match for *wull* nor failure to match *nosu* independently settles these questions.

## Current state (before any edits)

The released baseline has 387 selected runnable rows: 379 matches, eight mismatches, and no rejection or ambiguity. Mismatch IDs are **1973, 2013, 2030, 2162, 2224, 2240, 2298, 2300**. Wool2300 supplies *wúllō*, expects *wull*, and obtains *woll*. Nose2143 supplies *núsō*, although its citation PROTO is *nasō*: these are not interchangeable inputs.

The selected digest is `1ef9f5df8f90c7b1e37ce438b3b0ecdbb313deeecf42ec1eb0f1d070027ea3ec`; active original380 digest `953de7b8646fbfe8e0dcce7ed398f182ac45a4ca04af2802dde549f623f654d2`; immutable original380 digest `fae656520e9ebf446854643907a1ba48a511877fc25b1fae39649d5b97e9a6cf`. These are preservation observations, not scores used to select a history.

SC017 is currently adjudicated RETAIN, `pnwgmc/pan_pnwgmc`, confidence A. SC018 has the same historical stage/scope, confidence B, and remains unadjudicated. SC019 has that stage/scope, confidence A, and remains unadjudicated. Source comments and the SC017 memo overstate agreement on lowering before final raising; Stiles explicitly gives the other order (2012, p.45), and Ringe and Taylor's wool proposal requires it (2014, p.32).

The following numbers are derived executable coordinates, not dates. `composition_and_historical_metadata.tsv` supplies all 107 positions, origin blocks, kinds, and registry assignments.

| Executable index / cascade position | Identity | Current historical interpretation |
|---|---|---|
| 19 / 17 | SC015, i-lowering | Earlier operational anchor only |
| 20 / 18 | SC017, u-lowering | Northwest Germanic; not a proved date for phonemicization |
| 21 / 19 | SC018, stressed monosyllabic ō-raising | Distinct stressed-long-vowel treatment |
| 22 / 20 | SC019, final unstressed oral ō-raising | Northwest Germanic |
| 23 / 21 | SC020, unstressed final-z deletion | West Germanic; makes secondary final vowels |
| 24 / 22 | SC098, early prosodic high-vowel loss | Separate from ordinary OE apocope |
| 25 / 23; 26 / 24 | SC097; EAFRhotacism | Distinct monosyllabic z-loss; remaining rhotacism |
| 28 / 26 | SC023, final-n-loss proxy | Historically PGmc despite later executable site |
| 48 / 46; 49 / 47 | SC041; SC042 | Bare-a loss; surviving oral bimoric ō unrounding, PWGmc |
| 50 / 48; 51 / 49; 52 / 50 | Unstressed, stressed, long-final brightening | Distinct components, not one chronology inference |
| 56 / 54 | SC047 | Neuter nasal-a-ending loss, not wool's accusative ǭ |
| 72 / 70 | SC063 | OE prosodic high-vowel apocope |
| 74 / 72 | Medial syncope | Existing serialization, not independently established by these assays |
| 78–82 / 76–80 | Early/late o-shortening, unstressed fronting/raising/lowering | Later ending-processing interfaces |
| 83 / 81; 84 / 82 | SC072; SC073 | OE long-ending shortening and æ-merger |
| 89 / 87; 91 / 89 | Weak-tail reduction; final geminate simplification | Later output realization |

Actual SC017 matches first-nucleus *u/ú*, before a consonantal string whose first consonant is neither nasal nor *j*, with no intervening *j*, followed by `EnglishStarNonHighVowel`. It does **not** simply prohibit every nasal anywhere in that string. Acute and unaccented *u* are both handled; context prefixes are lifted by `Ctx`. A source description of nasal conditioning must not silently be replaced by this narrower structural test.

Its literal nonhigh class is `{*a}|{*ā}|{*ą}|{*e}|{*ē}|{*ḗ}|{*o}|{*ō}|{*ɔ̆}|{*ô}|{*à}|{*è}|{*ò}`. The literal right context is `[EnglishStarConsonantNoJ - EnglishStarNasal] EnglishStarConsonantNoJ* EnglishStarNonHighVowel`, after the initial `.#. EnglishStarConsonant*` anchor. B adds only `{*ǭ}` to the final trigger term. This is not a change to stress, nasals, j-blocking, consonant classes or vowel quantity.

Source anchors in the unchanged `Germanic/fsts/germanic.txt` are parser weak tails/simple words at lines 301–521, `PGmcStarVowel` at 527–573, alphabet/context wrapper at 1066–1080, SC020 at 1249–1254, SC017/class at 2350–2383, SC018/019 at 2481–2502, high-vowel apocope at 3410–3500, and the raw input adapter at 3906–3908. The worktree's pinned full source, not an independently maintained copied cascade, is the exact definition authority.

SC018 maps absolute-final monosyllabic *ō > ū* after a consonantal onset. SC019 maps oral *ō > u* at absolute word end after a preceding vocalic nucleus and at least one consonant. It excludes nasal *ǭ* and trimoric *ô*. Both rules retain their definitions in order experiments; the sole live SC018 witness, both1958, remains protected.

SC019 precedes SC020, so inherited final *-ō* raises, whereas *-ōz* is still protected by *z*. After z-loss, the newly exposed *ō* takes the SC042/long-final-brightening/SC072/SC073 path rather than SC019. This counterfeeding distinction agrees with Ringe and Taylor's ending account (2014, pp.58–60, 298–300); it does not settle SC017 versus SC019.

## Diagnosis

### Measured vowel and parser pathways

`pathway.json` contains actual component lookups, including acute/unaccented wool, all seven paradigm stems, and both context prefixes.

| Surface | Oral *ō* | Nasal *ǭ* | Trimoric *ô* |
|---|---|---|---|
| `PGmcStarVowel` / `PGmcStarVocalic` | Recognized | **Not recognized** | **Not recognized** |
| `EnglishStarAlphabet` / early `Ctx` segment admission | Recognized | Recognized | Recognized |
| `EnglishStarNonHighVowel` | Lowering conditioner | **Missing conditioner** | Lowering conditioner |
| Bare weak-tail input | `ō` accepted | **`ǭ` rejected** | `ô` accepted |
| Genitive weak-tail input | `ōz` accepted | Not tested as a genitive | **`ôz` rejected** |

Thus alphabet admission does not establish vowel-class membership or parser admission. `EnglishStarVocalic` inherits the problematic underlying class. Raw `wúllō` yields `*w*ú*l*l*ō`; raw `wúllǭ` has no output. Accepted `wúllanǭ` and `wúllōn` are different morphological/phonological inputs, not substitutes for the accusative cell. SC023's later *ōn > ǭ* proxy can conceal the missing inherited-ǭ conditioner because lowering already saw *ō*.

A generic private adapter admits bare final *ǭ* after the existing heavy/plain and nasal root parser alternatives; it is not wool-specific. It accepts `wúllǭ` as exactly `*w*ú*l*l*ǭ` and preserves **all 387 existing selected tokenizations**. This proves an available pathway, not completeness of a future production parser repair. No global inventory edit was smuggled into B or C.

Trimoric *wúllôz* is separately rejected by the raw parser. When entered already tokenized, its *ô* also fails the vocalic-nucleus test of SC020; the final *z* survives that rule. Its complete staged cascade ultimately rejects. All five paradigm assays report this rejection, with no ambiguity. That is an implementation coverage limitation, **not a falsification of Fulk's morphology**, and is never silently replaced by bimoric *ōz*.

SC042 directly transforms surviving oral *ō* into the carried *ā* tier. The inherited nasal *ǭ* instead survives symbolically until SC072's nasal-long branch gives *æ*, followed by SC073 *e*; bare *ô* has a different final-shortening branch. These are distinct encoding paths, not faithful dates for persistence of nasalization. Ringe and Taylor reconstruct earlier loss of nasality and PWGmc *ā* for accusatives (2014, pp.58–60); their historical quantities must be distinguished from this telescoped serialization.

### Complete baseline firing census

`complete_sc017_sc018_sc019_firing_census.tsv` gives every stable ID, selected input, and actual pre/post state.

SC017 fires on **39 rows**: 1953 board, 1956 bore, 1959 bottom, 1963 bow, 1973 buck, 1979 corn, 1982 crop, 1992 door, 2023 foal, 2026 folk, 2030 fowl, 2031 fox, 2035 frost, 2042 god, 2043 gold, 2076 hoard, 2082 horn, 2087 knob, 2111/2112 lock, 2143 nose, 2145 oven, 2146 ox, 2155 coat, 2162 rust, 2185 shovel, 2200 sorrow, 2211 spur, 2219 stock, 2222 stork, 2223 storm, 2251 thorn, 2265 trough, 2298 wolf, 2300 wool, 2301 word, 2307 yoke, 2311/2312 bore finite cells. These are applications, not 39 independent chronology proofs. Buck, fowl, rust, wolf, and wool retain unresolved selected histories.

SC018 fires on **both1958** alone. SC019 fires on **28 rows**: 1942, 1949, 1989, 2052, 2072, 2073, 2075, 2104, 2108, 2114, 2116, 2120, 2132, 2136, 2143, 2154, 2157, 2165, 2167, 2176, 2185, 2187, 2200, 2201, 2208, 2261, 2285, 2300. Every one is separately listed in the census.

### Executed counterfactuals

Predictions were declared in `predictions.json` before execution. All variants compile the entire cascade, retain all selected inputs/contexts, and compare all 387 finals. The original independent identity compiled all 107 full prefixes. Stage replay is additionally checked against that identity at **41,409 row/checkpoint pairs**, against four independently compiled full prefixes per variant, and against each variant's independently compiled full wrapper. All 16 declared paradigm cells per variant are independently checked through a complete derived suffix restricted only by a finite input acceptor; no sound law is restricted to those cells.

| Variant | Scientific intervention | Changed finals | Changed aligned intermediate rows | Matches / mismatches | Live-row rejection / ambiguity |
|---|---|---|---|---|---|
| Identity | Released cascade | None | None | 379 / 8 | 0 / 0 |
| A, order-only | Unchanged SC018 then SC019 before unchanged SC017 | 2143, 2185, 2200, 2300 | 29 | 377 / 10 | 0 / 0 |
| B, conditioning-only | Existing order; add *ǭ* only to SC017's nonhigh trigger | None | None | 379 / 8 | 0 / 0 |
| C, combined | A plus B | 2143, 2185, 2200, 2300 | 29 | 377 / 10 | 0 / 0 |
| D, continued allophony | B's early lowering; after SC019, revalue initial *o/ó* before final *u* to *u/ú* | 2143, 2185, 2200, 2300 | 4 | 377 / 10 | 0 / 0 |

D is a test of a specified hypothesis, not a newly established historical law. Reversibility is possible but not inevitable in Stiles's account (2012, pp.54–60); early analogical extensions outside the conditioning context are already present (pp.47–48). No lexical analogy is implemented by D.

The exact 29 intermediate-changed IDs in A/C are **1942, 1949, 1958, 1989, 2052, 2072, 2073, 2075, 2104, 2108, 2114, 2116, 2120, 2132, 2136, 2143, 2154, 2157, 2165, 2167, 2176, 2185, 2187, 2200, 2201, 2208, 2261, 2285, 2300**. Most reflect earlier final raising and converge later. D's changed aligned rows are the four final-changed rows. Inserted-event states are separately retained; original-slot diagnostics must not be mistaken for the new historical event site. `independent-equivalence.json` expands A/C's early nested SC018/SC019 operations for all 387 rows.

| Row | Released final | A/C/D final | Target | Interpretation |
|---|---|---|---|---|
| 2143 nose | nosu | nusu | nosu | Earlier raising removes nominative lowering conditioner |
| 2185 shovel | sċofl | sċufl | sċofl | Same; heavy-syllable apocope then removes final u |
| 2200 sorrow | sorg | surg | sorg | Same |
| 2300 wool | woll | wull | wull | Same; a match is compatibility, not chronology proof |

The A/C/D mismatch set is **1973, 2013, 2030, 2143, 2162, 2185, 2200, 2224, 2240, 2298**. Wool leaves the old mismatch set; nose/shovel/sorrow enter it. No mismatch is omitted or exempted.

Folk2026, god2042, gold2043, lock2111/2112 and buck1973, fowl2030, rust2162, wolf2298 preserve **every aligned intermediate and final** in all four variants. The latter four are not repaired by this chronology. Rust retains selected *rústaz*, output *rost*; its former *rústō* is not resurrected.

A helper-only technical defect was repaired transparently: private segment-only identity placeholders initially rejected the word-unstressed prefix on you2326 (`ᵘízwiz`). The revised placeholders use the existing `Ctx` mechanism. Original recipes are preserved; `recipes-context-v2.json` and `context-identity-repair.json` record the exact change. Definitions of SC017/018/019, scientific order hypotheses, original predictions and source pins were not altered. Cancelled expensive diagnostic compilations provide no scientific results.

## Literature

### Original-source passages and what they actually establish

| Source and printed pages | Express statement / evidence | Limit or inference |
|---|---|---|
| Ringe–Taylor 2014, pp.15–16 | Absolute-final unstressed bimoric oral *ō > u*; preference for raising to *ū* and subsequent shortening | This is not a rule for nasal *ǭ*, trimoric vowels, or stressed monosyllables |
| Ringe–Taylor 2014, pp.27–34, especially p.32 | Conditional lowering; *lufu* can supply u to *lufe/lufian*, and *wullu* can supply u to wool's paradigm | Wool may instead be a genuine unexplained exception. Their analogy is proposed, not established |
| Ringe–Taylor 2014, pp.33–34 | Gallehus *Holtijaz*, daughter and ox illustrate o-generalization beyond the original conditioner | Demonstrates the reality of analogy, not a specific attested wool alternation |
| Ringe–Taylor 2014, pp.57–60, 284–289, 298–300, 377–379 | Distinguishes early prosodic loss, ordinary OE apocope, long-ending shortening and inflectional generalization | Weight-conditioned u/zero nominative endings do not prohibit independent root-vowel levelling; shortening counterfeeds apocope and can overlap it |
| Fulk 2018, pp.55–57, especially p.56 | *skulō > scolu* and OS *skola* support lowering before final *ō > u*; *horna* ca.400 shows lowering, and raising is assigned to the fifth century | *scolu* argument assumes inherited nominative root vocalism has not been remodelled |
| Fulk 2018, p.57 n.1 | Explicitly cites Ringe–Taylor pp.27–34 and reports their argument about lowering and final *-az* loss; discusses *Hludana* ca.200 | Not an explicit named rejection of the p.32 wool hypothesis |
| Fulk 2018, pp.82–86, especially p.82 | Järsberg *waritu* ca.450, from *wrītō*, witnesses final oral raising; chapter 5 distinguishes historical quantities/endings | An attestation supplies an upper bound, not by itself a lower bound for onset or a strict English chronology |
| Fulk 2018, pp.154–156, especially p.155 | Feminine ō-stem nominative *ō > u* versus accusative nasal ending; OS/OHG accusative -a generalizes to nominative | Continental nominatives are not untouched controls; root and ending can be generalized separately. Fulk's trimoric genitive differs from RT's bimoric account |
| Ringe 2017, pp.171–173, 241–244, especially pp.242–243 | Explicit wool nom. *wullō > wullu*; acc. *wullǭ > wullā > wulle* as ending examples | The displayed root u is not independent evidence that no earlier conditioned root lowering occurred |
| Stiles 2012, pp.44–48, especially p.45 | Expressly places final bimoric *ō > u* before a-umlaut; separates conditioned phones and phonemes; Runic analogical extensions | Predates RT2014, so is not a response to it. Its order statement is not a new independently dated wool paradigm |
| Stiles 2012, pp.49–60 | Critiques automatic conditioner-loss accounts of phonemicization; discusses levelling and possible reversion | Does not authorize a general obligatory reversion rule like D |
| Campbell 1959, p.43, §115 and note | Lowering and northern exceptions; *nosu* from *nusō* | Text-only holding in this investigation; no original page image certified |
| Bülbring 1902, pp.45–46, §116 | Retention versus reversal remains uncertain; tentative intermediate vocalism; exceptions alongside regularly lowered words | Text-only holding; tentative accounts are not established new sound laws |
| Luick, printed pp.105–106, §§77–79, especially §78 | Paradigm alternation/generalization, contrasts near labials/liquids, inferred *scufel* beside *scofel* | The repeatedly cited “§§105–106” is a locator error: actual §§105–106 are on pp.120–121 and address different material |
| Orel 2003, p.474 | Feminine *wullō* and comparative wool etymology | No explicit proof of the proposed u/o levelling |
| Kroonen 2013, pp.598–599 | Feminine *wullō-*; older mobile/consonantal or alternative neuter formation; OFri *wolle*, OHG *wolla* beside high-vowel reflexes | Older ancestry does not exclude a later PGmc ō-stem. Low-root comparanda support a possible wool o-history, not the exact unattested early English oblique |

Comparison stems are supported by Orel 2003 pp.118 (*palm*), 249 (*love*), 347 (*shovel*), Kroonen 2013 pp.383 (*nose*), 493 (*sorrow*), and Ringe–Taylor 2014 pp.32–33, 299. Except for Ringe's explicit wool cells and RT's explicit sorrow accusative, tested complete cells assembled from these stems and generic endings are marked **CAPR assemblies**, not attributed whole-word quotations. The comparison set does not add corpus rows.

Bounded external searches for explicit criticism of the wool account or this order found no additionally verified passage that directly rejects it. Fulk's actual p.57 n.1 citation is verified and reported above; it must not be replaced by the erroneous claim that he never discusses RT. General reviews are not counted as criticism of this analysis. An unexamined Brill lead, “Levelling and Rule Restructuring in Old English Adjectives,” DOI `10.1163/22125892-00301001`, is not evidence here; access was refused and no wool-specific passage was verified. This search result is bounded, not proof that no published response exists.

### Page locators and verification accountability

The supplied RT original has 629 sheets and SHA256 `278f94f6076a31278ecca75d8d0429f0822728e5efe0ec3011186a694cf8d6f2`; the existing and supplied copies are byte-identical. Original-PDF extraction readings include the complete relevant arguments and notes at pp.15–16, 27–34, 57–60, 267, 284–289, 298–300, 377–379; p.267 is syncope, not the primary apocope discussion. Visual inspection of its pp.15 and 32 verifies the load-bearing quantities and conditional wool proposal.

| Holding | Printed page → PDF sheet | Original-image checks actually performed |
|---|---|---|
| RT2014 | 15→30; 32→47; 33–34→48–49; 57–60→72–75; 267→282; 284–289→299–304; 298–300→313–315; 377–379→392–394 | 15, 32 |
| Fulk2018 | 55–57→72–74; 82→99; 154–156→171–173 | 56, 57, 82, 155 |
| Ringe2017 | 172→183; 242–243→253–254 | 172, 242, 243 |
| Orel2003 | 474→513 | 474 |
| Kroonen2013 | 598–599→638–639 | 598, 599 |
| Luick Part I | 105–106→121–122; actual §§105–106 at 120–121→136–137 | 105, 106 |
| Stiles2012 | Printed p.45 lies on chapter sheet 3; embedded page markers locate the rest | 45; complete chapter argument and notes read |

Saved crops reside in `pages/` and the two RT images alongside the investigation directory. Page extraction from an original PDF is distinguished from a visual check; Campbell and Bülbring remain text-only verification limits. No full copyrighted pages are reproduced in this report.

## Historical analysis

### Source-supported case reconstruction and executed finals

All fixtures enter **PGmc**, already tokenized, immediately after `EnglishProtoInput`. This bypass is explicit because bare nasal accusatives currently fail that adapter; it does not assign them a later historical stage. Acute stress is CAPR encoding. The complete original quantity is preserved.

| Cell | Released | A: early raising only | B: corrected conditioner | C: both | D: revaluation |
|---|---|---|---|---|---|
| wool nom. *wúllō* | woll | wull | woll | wull | wull |
| wool acc. *wúllǭ* | wulle | wulle | wolle | wolle | wolle |
| love nom. *lúbō* | lofu | lufu | lofu | lufu | lufu |
| love acc. *lúbǭ* | lufe | lufe | lofe | lofe | lofe |
| shoal nom. *skúlō* | sċolu | sċulu | sċolu | sċulu | sċulu |
| shoal acc. *skúlǭ* | sċule | sċule | sċole | sċole | sċole |
| nose nom. *núsō* | nosu | nusu | nosu | nusu | nusu |
| nose acc. *núsǭ* | nuse | nuse | nose | nose | nose |
| shovel nom. *skúflō* | sċofl | sċufl | sċofl | sċufl | sċufl |
| shovel acc. *skúflǭ* | sċufle | sċufle | sċofle | sċofle | sċofle |
| sorrow nom. *súrgō* | sorg | surg | sorg | surg | surg |
| sorrow acc. *súrgǭ* | surge | surge | sorge | sorge | sorge |
| palm nom. *fúlmō* | folm | fulm | folm | fulm | fulm |
| palm acc. *fúlmǭ* | fulme | fulme | folme | folme | folme |
| wool gen., RT bimoric assembly *wúllōz* | wolle | wolle | wolle | wolle | wolle |
| wool gen., Fulk trimoric assembly *wúllôz* | rejected | rejected | rejected | rejected | rejected |

Unattested comparison accusatives have **no invented attested target** in the receipts. CAPR's *sċolu* and Fulk's plain *scolu* differ in explicit palatal orthographic marking, not in the root-vowel chronology under investigation.

C genuinely produces this regular contrast:

* Nom.: *wúllō → wúllu* by final oral raising, no lowering before high *u*, then heavy-syllable high-vowel loss gives *wull*. The intermediate *wullu* is present before ordinary OE apocope, not an asserted attested word.
* Acc.: *wúllǭ → wóllǭ* under nasal-vowel-aware lowering; SC019 does not raise *ǭ*. The implemented ending suffix produces *wolle*. Historically the intervening denasalization/unrounding is earlier than its telescoped code representation (RT2014, pp.58–60; Ringe2017, pp.242–243).
* Attested oblique *wulle* still requires separately argued replacement of the oblique root *o* by nominative *u*. This operation is not in the sound laws.

A's apparent regular *wull/wulle* is not a completed historical solution: the accusative retains u only because the nasal conditioner is missing. Once that omission is repaired, the regular oblique is *wolle*. The released *wulle* staged output is likewise a misleading match for this cell.

Under corrected lowering-before-raising B, wool's nominal and accusative roots are both o; generalizing a nominative u cannot explain them because that nominative was never regularly high. Love likewise has *lofu/lofe*. This sequence therefore leaves the high-root histories unexplained rather than disproving an earlier-raising alternative. The other corrected B paradigms have consistent lowered roots and require no root-vowel levelling for the compared low-root forms.

Under C, *lufu/lofe* can yield attested *lufu/lufe* by nominative-root generalization, just as RT proposes (2014, p.32). Shoal *sċulu/sċole* can yield *scolu* by oblique-root generalization without changing nominative -u; nose, shovel, sorrow, and palm have the corresponding possible o-generalizations. These are real, independently supported inflectional environments, not invented high/low endings. However, the particular direction of levelling for each lexeme is inferred, not directly witnessed in the tested early paradigms.

The legitimacy of such analogy is independently supported by early *Holtijaz* and the daughter/ox paradigms (RT2014, pp.33–34; Stiles2012, pp.47–48), and by continental ō-stem accusative-to-nominative generalization (Fulk2018, pp.154–156). It does **not** prove the specific OE *scolu* or *wull* reconstruction. OFri *wolle* and OHG *wolla* supply independent wool low-root comparanda (Kroonen2013, pp.598–599), but not a dated unattested English *woll-* case.

### Chronology and Runic constraints

Fulk's argument is coherent **if** *scolu* preserves its regular inherited nominative root: lowering must then have seen the old final low vowel before raising removed it (2018, p.56). It is not a refutation once independently possible oblique-root remodelling is admitted. OS *skola* is especially not an untouched nominative control, because Fulk himself describes generalization of accusative -a into the nominative (pp.154–156).

*Horna* ca.400 independently witnesses conditioned lowering in the Runic language; *waritu* ca.450 independently witnesses final oral raising (Fulk2018, pp.56, 82). They do **not** by themselves establish a strict order: a form with raising attested around 450 does not prove raising began after 400. Inscription date, linguistic affiliation, vowel quantity, and onset versus completion remain separate. Retained written o in a different ending is not proof that oral bimoric final *ō* had not raised; trimoric and consonant-protected endings must first be distinguished (Fulk2018, pp.82–86).

The Gallehus *Holtijaz* and Tune *dohtriR* forms also show analogical o outside its original conditioning while low-vowel conditioners survive (Stiles2012, pp.47–48). Thus *horna* does not date the entire phonemicization bundle, and loss of final a is not its automatically sufficient explanation. RT's lowering-before-final-a-loss argument (2014, p.29) is likewise distributional and premise-dependent; it does not independently force lowering before final-ō raising.

The canonical reciprocal records at `chronology_edges.tsv` lines 18 and 21 are displacement relations, **not two strict before-edges forming a historical cycle**. Their “independently_demonstrated” force depends on selected nominatives *núsō/skúflō/súrgō* and absence of later root levelling. These are conditional computational preservation dependencies, not an independent exclusion of RT/Stiles. The SC019–SC020 relation has a separate quantity/final-consonant basis; SC018's search boundaries establish no relative-history law.

No checked evidence requires shifting all three events to a different genealogical stage. Northwest Germanic lowering onset remains a defensible characterization; the onset, retention of its conditioned realization, and eventual phonemic contrast must be narrated separately. D usefully exposes the difference but adds an unsupported general revaluation operation; it should not be adopted to get the same finals as C.

## Verdict

### Explicit answers

1. **Does a defensible sound-law sequence produce nominative *wullu* regularly?** Yes. C's oral final raising before correctly conditioned lowering does so, retaining stressed-monosyllable SC018 separately. This order is expressly stated by Stiles (2012, p.45), and underlies RT's conditional wool/love account (2014, p.32).
2. **Does the same sequence produce an independently supported *woll-* oblique?** It regularly predicts *wóllǭ → wolle* from the independently reconstructed nasal accusative (Ringe2017, pp.242–243). The inflection and lowered-root comparanda are independent support; the exact early English oblique itself is reconstructed, not attested or expressly quoted by Ringe as *woll-*.
3. **Does Fulk's *scolu* establish the reverse order?** Only under the unremodelled-nominative premise. Oblique-root generalization is plausible and has independent typological/comparative support within these authors' actual paradigms (RT2014, pp.33–34; Fulk2018, pp.154–156). It is not directly proved for *scolu*.
4. **Does Runic dating independently constrain both changes?** It supplies separate positive attestations and upper bounds, not a strict pairwise order or dates for every phonetic/phonemic component (Fulk2018, pp.56, 82; Stiles2012, pp.47–48).
5. **Which source supplies the best relative-chronology argument?** Fulk supplies the most direct positive lexical order argument, *scolu* (2018, p.56), but it is explicitly conditional once its unlevelled-root premise is exposed. RT's detailed paradigm account and Stiles's analysis of early analogy show why it is not decisive (2014, pp.27–34; 2012, pp.45–60). No checked source supplies a premise-free demonstration; Stiles's opposite-order statement is not itself a stronger dated witness.
6. **Is RT's *wull* account established, plausible but unproved, or contradicted?** **Plausible but unproved.** Corrected complete-cascade assays show its genuine regular nominal/oblique contrast and the needed separate levelling; neither they nor the comparative low-root forms establish the particular early English paradigm or levelling direction (RT2014, p.32; Kroonen2013, pp.598–599).
7. **Reorder, reformulate, restage, split, or retain?** **Recommend reformulating the vowel/domain/input recognition and the strength of the historical chronology claim; retain the present executable order provisionally, not as a proved history.** Do not adopt a global reorder merely to solve wool, and do not add D's revaluation rule. No wholesale restaging or new historical split is justified by this evidence. C is the correct executable representative of the RT/Stiles alternative for a subsequent explicit choice, not a broken or refuted account.
8. **What owners and lexical entries would change if C were chosen?** The live final changes are exactly nose2143, shovel2185, sorrow2200, wool2300. Their inputs/targets would not automatically change; the first three would need honest regular-versus-levelled histories rather than score-restoring input substitutions. Published love, shoal, and palm comparisons would also need the alternate paradigms. SC017/018/019 readers, their grouped corridor dossier, SC017's prior memo and SC017–SC019 chronology records, input/inventory documentation, and the relevant chapter/lexical SOURCE owners would need coordinated updating.

### Recommended adoption decision

The certain defect is **not** proof that the existing historical order is false: it is the omission of inherited nasal *ǭ* from the relevant conditioner and raw input pathway, together with broader vowel-class and trimoric-genitive coverage gaps. Recommend a separately approved, general quantity-preserving recognition repair, with all consumers tested; B establishes its local conditioning consequence without changing any of the 387 selected finals. It deliberately removes the misleading “regular *wulle*” staged match.

For chronology, retain current serialization as a **provisional Fulk-compatible working model**, withdraw claims that nose/shovel/sorrow independently prove it against levelling alternatives, and publish RT's account as a tested, plausible competing explanation of wool. Fulk's direct nominative argument is a reasonable default, not a refutation. Selecting C later is scientifically defensible if its analogical premise is accepted; it must be selected as a historical account with openly recorded case remodelling, not because it improves wool's score.

This is a positive bounded decision, not a proposal for another unrestricted investigation: repair the demonstrated recognition defect; qualify the chronology; reject an invented general reversion law; do not adopt a global reorder on the present evidence.

## Propagation (only after verdict)

**None adopted.** The following is the owner map for a future explicit decision, not authorization to edit it:

* `Germanic/fsts/germanic.txt`: bare-final nasal admission; underlying vocalic/back-vowel classification; SC017 conditioner; quantity-sensitive consumers including SC020. A trimoric genitive must not be “fixed” by changing it to bimoric *ōz*.
* `Germanic/docs/sound_changes/registry/{sc_registry,chronology_edges,sc_inventory_notes}.tsv`: only evidence-supported chronology characterization and any expressly approved metadata. Generated positions/annotations are not hand-edited.
* `Germanic/docs/sound_changes/audits/sc016-017-adjudication.md`; `book_dossiers/016-020-early-vocalic-final-corridor.book-dossier.md`; `literature_dossiers/019-nwgmc-final-long-o-raising.dossier.md`: replace apparent unanimity with page-backed premise-level comparisons.
* `reader_facing/017-nwgmc-u-lowering.md`, `018-stressed-monosyllable-o-raising.md`, `019-nwgmc-final-long-o-raising.md`, `042-surviving-bimoric-o-unrounding.md`, `063-high-vowel-apocope.md`, `072-073-unstressed-long-vowel-shortening-and-ae-merger-core.md`, and the chapter introductions: explain oral/nasal/trimoric distinctions, keep SC018 separate, and distinguish onset from phonemicization.
* Current `model_entries/{2300-wool-wull,2143-nose-nosu}.{model,source_ledger}.md` and `research_memos/{2300-wool-wull,2143-nose-nosu}.md`, plus the structured PGmc comparison SOURCE: exact regular outputs versus attested forms and separate analogy. Shovel2185 and sorrow2200 currently have archival DEV_NOTES slices rather than these live authored model entries; any new account belongs in live SOURCE, **not** by rewriting those archives. Buck1973, fowl2030, rust2162 and wolf2298 remain unresolved controls, not additional consequences of this reorder.

If C were adopted without new selected inputs, the accepted population remains 387; final-output fingerprints change for exactly four rows, while target mismatch membership changes as reported. A new approved transition would be needed; all older protected archives stay byte-identical. No such transition is performed here.

Research receipts are `identity.json`, the five `*-replay.json` files, `pathway.json`, `independent-equivalence.json`, `context-identity-repair.json`, original/revised recipes and predeclared predictions. The six TSV annexes give the complete 387-row comparisons, every changed intermediate, all paradigms and all positions/census entries. `production-preservation-final.json` records the final production closeout; `artifact-sha256.tsv` supplies deliverable hashes.

## Residue

The smallest remaining historical premise is whether the **root o of the inherited ō-stem nominatives, above all *scolu*, is regular nominative inheritance or oblique-root generalization**. Existing cases prove that generalization can happen and supply the right oblique conditioners; they do not directly identify this particular early paradigm. This one premise determines whether Fulk's best order argument excludes C.

Separately, the exact early English *woll-* oblique and nominative-to-oblique u-generalization are not directly attested; RT's own reservation must remain visible (2014, p.32). The different genitive quantities in RT (2014, pp.59, 299) and Fulk (2018, pp.85, 155) remain distinct, and the current trimoric pathway is not fully modelled. Campbell/Bülbring originals remain unverified image holdings, and the external-response search is bounded. None of these limitations is concealed by a successful nominative *wull*.

The requested scientific comparison and declared experiments are complete. Production adoption is the explicit stopping boundary.
