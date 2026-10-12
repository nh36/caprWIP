# Evidence packet — 2300 wool / wull

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2300 | wool | wull | *wúllō | *wúllō | unexplained_unmodelled | DOCUMENTED EXCEPTION (per §17.10.34): regular sound change from *wúllō gives **woll (Stiles 2012 §4.1.1.2 env. (b): low *ō triggers a-umlaut). Campbell §115 explicitly lists 'full' as an exact morphological parallel exception, with OHG 'foll' as the regular outcome. Unlike wulf/fugol/bucc/rust, wull is a fem. ō-stem with no paradigm cell containing high *i/*ī/*j to escape via env. (a) — every cell has a back-vowel ending. The FST output 'woll' is the correct regular result; attested 'wull' is non-derivable in this FST. | See DEV_NOTES §17.10.34. |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# wool
PROTO: *wúllō
EXPECTED: wull
OUTPUTS: woll



### Proto-Germanic consonant inheritance

Proto Input: *wúllō

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>NWGmc U Lowering: *wóllō<br>NWGmc Final Long O Raising: *wóllu | **Old English**<br>OE High Vowel Apocope: *wóll |



### Orthography & surface

Outcome: woll

NOTE: DOCUMENTED EXCEPTION (per §17.10.34): regular sound change from *wúllō gives *woll (Stiles 2012 §4.1.1.2 env. (b): low *ō triggers a-umlaut). Campbell §115 explicitly lists 'full' as an exact morphological parallel exception, with OHG 'foll' as the regular outcome. Unlike wulf/fugol/bucc/rust, wull is a fem. ō-stem with no paradigm cell containing high *i/ī/j to escape via env. (a) — every cell has a back-vowel ending. The FST output 'woll' is the correct regular result; attested 'wull' is non-derivable in this FST.
```

### Matching oe_known_problems.tsv entries

| proto | status | category | reason | refs | added |
| :--- | :--- | :--- | :--- | :--- | :--- |
| *wúllō | wontfix | u_lowering_near_labial | Same u-lowering near labials issue | notable_findings#2 | 2026-04-25 |

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:24583 (exact COUNTERPART)

- Nearby heading: #### 1. Re-classification of *rústō and *wúllō

```text
24581:    — the report tool uses the `_U_LOWERING_ROOTS` set in
24582:    `oe_mismatch_report.py` (which already contains "rust"/"rost" and
24583:    "wull"/"woll") to separate documented lexical exceptions from
24584:    genuine model errors.
24585: 
```

#### Germanic/docs/DEV_NOTES.md:24586 (row ID)

- Nearby heading: #### 1. Re-classification of *rústō and *wúllō

```text
24584:    genuine model errors.
24585: 
24586: 2. The TSV row for `*wúllō` (row 2300) carries the explicit note
24587:    `EXCEPTION: u-lowering blocked near labials (Luick §78, R/T
24588:    §2.3.1, Brunner §68). FST outputs regular woll; attested wull is
```

#### Germanic/docs/DEV_NOTES.md:24588 (exact COUNTERPART)

- Nearby heading: #### 1. Re-classification of *rústō and *wúllō

```text
24586: 2. The TSV row for `*wúllō` (row 2300) carries the explicit note
24587:    `EXCEPTION: u-lowering blocked near labials (Luick §78, R/T
24588:    §2.3.1, Brunner §68). FST outputs regular woll; attested wull is
24589:    genuine lexical exception.` Row 2162 for `*rústō` similarly
24590:    notes `OE rust retains u; cf. R/T §2.3.1 for general u-lowering
```

#### Germanic/docs/DEV_NOTES.md:25953 (exact pair)

- Nearby heading: ### §17.10.34 Cluster: u-lowering "exceptions" (wulf, fugol, bucc, rust, wull) — paradigm-cell switch for 4/5

```text
25951: | `*rústō` | `orst` | `rust` |
25952: | `*wúlfaz` | `wolf` | `wulf` |
25953: | `*wúllō` | `woll` | `wull` |
25954: 
25955: #### Source audit — is there a lautgesetzlich rule that gives these?
```

#### Germanic/docs/DEV_NOTES.md:26069 (row ID)

- Nearby heading: #### Why row 2300 (wull) is left alone

```text
26067: cell whose OE outcome the row attests.
26068: 
26069: #### Why row 2300 (wull) is left alone
26070: 
26071: OE `wull` is a feminine ō-stem; the entire ō-stem paradigm has back
```

#### Germanic/docs/DEV_NOTES.md:26079 (exact pair)

- Nearby heading: #### Why row 2300 (wull) is left alone

```text
26077: 
26078: Per `skills/be-lautgesetzlich.md` "Documenting genuine exceptions",
26079: the row is left as `*wúllō → wull`, with the NOTE field expanded to
26080: record that:
26081: 
```

#### Germanic/docs/DEV_NOTES.md:26114 (row ID)

- Nearby heading: #### Implementation order

```text
26112: 2. Edit `Germanic/data/germanic-aligned-final.tsv` rows
26113:    1973/2030/2162/2298 (TOKENS, PROTOFORM, IPA, COUNTERPART, NOTE);
26114:    row 2300 (NOTE expansion only). Per `skills/be-lautgesetzlich.md`
26115:    convention: PROTOFORM = cell-specific FST input; PROTO = cognate
26116:    headword (preserved as `*wúlfaz`/`*fúglaz`/`*búkkaz`; corrected to
```

#### Germanic/docs/DEV_NOTES.md:26183 (row ID)

- Nearby heading: ### §17.10.34a Revision: paradigm-cell switch does NOT work — all 5 are documented exceptions

```text
26181: (PROTOFORM/TOKENS/COUNTERPART restored to committed values); rewrote
26182: each NOTE to cite §17.10.34 and Campbell §115 as documented
26183: exceptions. Row 2300 (wull) kept its §17.10.34 note. All five now
26184: surface in the mismatch report bucket
26185: `vowel_quality__u_lowering_exception`, properly categorised.
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:82 (note keyword: a-umlaut)

- Nearby heading: ### Summary of the scholarly literature

```text
80: ### Summary of the scholarly literature
81: 
82: **Bülbring (EB §116, pp.45-46)** provides the original hypothesis that both Luick and R/T engage with. He observes that OE u appears instead of expected o (from WGmc a-Umlaut, his §81d) "namentlich zwischen Labial und langem oder gedecktem l" — i.e. between a labial and ll or l+consonant: *full* 'full', *wulle* 'wool', *wulf* 'wolf'; also *fugol* 'bird', *bucca* 'buck', *múrnan* 'mourn'. He concedes that "meist steht jedoch der Hauptregel gemäß o" — usually the regular rule gives o — citing *wolcen, folgian, bolt, folc* as counterexamples. In his Anmerkung, Bülbring notes the agreement with OFris. and OS (afries. *ful, wulla, wulf*; as. *full, wulla, wulf, fugal*), which shows the phenomenon is "sehr alt" (very old). He remains agnostic on mechanism: "Ob wir darin Erhaltung des wg. u oder Wiederaufhebung der durch a-Umlaut herbeigeführten Veränderung erblicken müssen, läßt sich nicht mit Sicherheit entscheiden" — whether this reflects preservation of the original WGmc *u or reversal of a-Umlaut cannot be determined with certainty. He speculates that *u was lowered only partway ("etwa zu [ou] oder zu engem [o]") and then, under influence of its labial/velar environment, reverted to u, while in other words it continued to open [ɔ]. This "incomplete lowering + reversion" model is phonetically interesting but not formalizable as a categorical rule, since the same environments also show regular lowering.
83: 
84: **Luick (§78, Anm. 3)** engages directly with Bülbring's proposal and rejects it. He argues for paradigmatic leveling instead: doublet forms arose because paradigms had both u-preserving (high-vowel suffix) and u-lowering (non-high suffix) forms; near labials and gutturals, the u-forms were preferred. He explicitly cites the counterexamples that make Bülbring's phonological conditioning untenable: *wolcen, folc, folġian, folde, folm, bolla, bolt, bolster, molde, molcen, smolt* — all have labial or velar environments but regular lowering.
```

#### Germanic/docs/DEV_NOTES.md:148 (note keyword: a-umlaut)

- Nearby heading: ### Expert consultation: Stefan Schuhmacher (Vienna, 2026-03-20)

```text
146: Prof. Schuhmacher confirmed the scholarly consensus and provided additional clarifications:
147: 
148: **Terminology:** He prefers "Lowering of \*u" over "A-Umlaut" as more transparent.
149: 
150: **Scope:** "Such lowering affects **only stressed vowels**... I do not see that the lowering affects unstressed vowels such as the middle vowel in the word for 'widow'." This validates our implementation restricting lowering to stressed syllables.
```

#### Germanic/docs/DEV_NOTES.md:217 (note keyword: a-umlaut)

- Nearby heading: ### Related: effects of initial labials on vowels (Bülbring §§260-274)

```text
215: 
216: Note that Bülbring's "Dreizehntes Kapitel" (§§260-274) discusses a *separate* set of phenomena — the effects of initial labials (especially w) on following vowels and diphthongs. These include:
217: - **w + iu → wu** (§264): *widu → wudu 'wood' (via u/a-Umlaut *wiudu → wudu under w-influence)
218: - **weo → wo → wu** (§§265-268): late WS weorpan → wurpan, sweord → swurd
219: - **w + i → y** (§261): ni + witan → nytan (contraction contexts)
```

#### Germanic/docs/DEV_NOTES.md:620 (note keyword: a-umlaut)

- Nearby heading: #### 1. NWGmc U-Lowering ("A-Umlaut" / Lowering of *u)

```text
618: distinguish them clearly because they have different conditioning:
619: 
620: #### 1. NWGmc U-Lowering ("A-Umlaut" / Lowering of *u)
621: 
622: **Rule:** Stressed `*u → *o` before a non-high vowel (*a, *o, *ē) in the following syllable.
```

#### Germanic/docs/DEV_NOTES.md:5137 (note keyword: a-umlaut)

- Nearby heading: #### View 2: Lowering occurred in West Germanic (Bülbring's position)

```text
5135: > "\*nëstoz 'Nest' aus älterem \*nistoz, \*wëroz 'Mann' aus \*wiroz"
5136: 
5137: Bülbring calls this "a-Umlaut" — lowering of *i, u* before non-high vowels in the
5138: following syllable. He treats this as a WGmc phenomenon that took an earlier
5139: \*nistoz and produced \*nestoz.
```

#### Germanic/docs/DEV_NOTES.md:5243 (note keyword: a-umlaut)

- Nearby heading: #### Lloyd (1966): "Is There an a-Umlaut of i in Germanic?"

```text
5241: explanation that is both Neogrammarian and predictive.
5242: 
5243: #### Lloyd (1966): "Is There an a-Umlaut of i in Germanic?"
5244: 
5245: Albert L. Lloyd (University of Pennsylvania) argued that **no regular a-umlaut of
```

#### Germanic/docs/DEV_NOTES.md:13791 (exact COUNTERPART)

- Nearby heading: # MUST use *a (not *ă) to undergo unstressed fronting: *a → *æ → *e

```text
13789: | 2119 | man | `*mannăz` | man | mann | word-final degemination |
13790: | 2203 | span | `*spannō` | span | spann | word-final degemination |
13791: | 2300 | wool | `*wullo` | wollo | wull | degemination + vowel |
13792: 
13793: **Neuter a-stems:** Gen.sg. uses the same `-es` ending as masculines (Brunner §237).
```

#### Germanic/docs/DEV_NOTES.md:24450 (exact PROTOFORM)

- Nearby heading: #### 1. Probe outcome (vs. post-§17.10.23 baseline of 38)

```text
24448:   again). `*skúldrō` and `*mízdō` shift back to their pre-§17.10.23
24449:   forms (`sċoldor`, `meord`).
24450: - `*rústō`, `*wúllō` — **re-regress** (lose their §17.10.23 fix).
24451: - Eight **new** mismatches, all sharing the shape *CVCuz:
24452: 
```

#### Germanic/docs/DEV_NOTES.md:25940 (exact COUNTERPART)

- Nearby heading: ### §17.10.34 Cluster: u-lowering "exceptions" (wulf, fugol, bucc, rust, wull) — paradigm-cell switch for 4/5

```text
25938: 
25939: 
25940: ### §17.10.34 Cluster: u-lowering "exceptions" (wulf, fugol, bucc, rust, wull) — paradigm-cell switch for 4/5
25941: 
25942: **Mismatch bucket.** `vowel_quality__u_lowering_exception` — five OE
```

### Analysis and dossier hits

#### Germanic/docs/analysis/notable_findings.md:418 (note keyword: a-umlaut)

- Nearby heading: ### Expert consultation (Stefan Schuhmacher, Vienna, 2026-03-20)

```text
417: **On terminology:** Schuhmacher prefers "Lowering of high vowels" or "Lowering
418: of \*u" over the traditional "a-Umlaut" (German *a-Umlaut*).
419: 
```

#### Germanic/docs/analysis/notable_findings.md:1057 (note keyword: a-umlaut)

- Nearby heading: ## 7. NWGmc *i > *e lowering: consonant-conditioned blocking and rule ordering

```text
1056: **Background:** NWGmc \*i lowered to \*e before non-high vowels in the following
1057: syllable, parallel to the well-established \*u > \*o lowering (a-umlaut).
1058: However, the \*i lowering is notoriously sporadic — Campbell (OEG §114) notes
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:366 (note keyword: a-umlaut)

- Nearby heading: ### Campbell §210 — concrete dialect contrast

```text
365: and liquids (`heofon, eofor, beofor, heorot`) but not generally before other
366: consonants; a-umlaut is mostly absent (`fela, helan, beran, nefa, sefa,
367: weras, wela`). In Anglian (l. 6337): "both u- and a-umlaut of e are general
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:367 (note keyword: a-umlaut)

- Nearby heading: ### Campbell §210 — concrete dialect contrast

```text
366: consonants; a-umlaut is mostly absent (`fela, helan, beran, nefa, sefa,
367: weras, wela`). In Anglian (l. 6337): "both u- and a-umlaut of e are general
368: before all consonants except c and g."
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:655 (note keyword: a-umlaut)

- Nearby heading: ## 9. u-mutation vs. back mutation; dialect distribution

```text
654: - **WS**: u-umlaut general before single labial/liquid (`heofon, eofor,
655:   beofor, heorot`); a-umlaut "generally absent" (`fela, helan, beran, nefa,
656:   weras, wela`; Campbell §210.1, l. 6332). Combinative back umlaut after
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:402 (note keyword: a-umlaut)

- Nearby heading: ### What NOT to do

```text
401:   middle vowel in the word for 'widow'") to argue against the rule
402:   itself. Schuhmacher there is talking about *A-Umlaut / stressed-
403:   `*u`-lowering*, not about Campbell §373; the latter is securely
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:505 (note keyword: a-umlaut)

- Nearby heading: ### Cited only via secondary / not directly opened in this round

```text
504:   The quote is informative but not load-bearing for this dossier:
505:   Schuhmacher is discussing A-Umlaut / stressed-`*u`-lowering, not
506:   Campbell §373 medial-unstressed lowering.
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:525 (note keyword: a-umlaut)

- Nearby heading: ### Not consulted in this round (and not needed)

```text
524:   *widuwō(n)- not in dispute.
525: * Stiles 2012, Howell & Salmons 1988, Cercignani — concern A-Umlaut
526:   / stressed lowering, not the medial-unstressed rule.
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| wool | wull | inh | template:inh | wool |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1433 (exact pair)

- Nearby heading: ## Project Status (as of 2026-04-30) — research phase complete

```text
1431: * `*táppô → tappa` (expected `tæppa`) — `exception: analogical_n_stem_levelling`
1432: * `*wúlfaz → wolf` (expected `wulf`) — `wontfix: u_lowering_near_labial`
1433: * `*wúllō → woll` (expected `wull`) — `wontfix: u_lowering_near_labial`
1434: 
1435: (Previously listed `*ráukaz → rēac` mismatched against attested Anglian
```

#### Germanic/docs/DEV_NOTES.md:2315 (concept name)

- Nearby heading: ### Short-vowel fixes + /r/-loss scaffold

```text
2313: 
2314: - Added plain helper sets (`EnglishSandboxPlainVocalic/Liquid/Nasal`) so late-stage rules can reason about the brace-free vowels while still matching against the starred consonants passed along from the proto inventory.
2315: - Reworked `EnglishSandboxShortVowelSplit` to cover the documented FOOT/STRUT environments: `{*u}` now targets `{ʊ}` before velars, `{*z/m/n}` plus weak-tail templates, dark `{*l}`, `{*r}`, and the `{*f}/{*s}/{*θ}` codas (`wolf/wool`), while KIT contexts keep `{*e}`→`{ɪ}` before nasals/liquids. Everything else still falls through to `{ʌ}`/`{ɛ}`.
2316: - Inserted `EnglishSandboxPostVocalicRLoss` (after the vowel stack but before weak-tail reductions) so `{*r}` drops after any plain vowel plus a consonant/word boundary, giving us a chronological hook for the upcoming smoothing work.
2317: - Reran the attested-form sweep (same `python3 - <<'PY' …` harness as above): 179/376 English entries now reconstruct (up from 119), with the failure buckets collapsing to KIT = 61, FOOT = 3, weak-tail schwa = 51, /r/-bearing = 54, and `{ɔ/əʊ}` = 18. Spot checks show `bəʊn/bəʊθ` retrieving `{*bōr}` bundles prior to loss, while known outliers like `bʊzəm` and the irregular `ʋʊl/ʋʊlf` remain on the TODO list.
```

#### Germanic/docs/DEV_NOTES.md:13801 (concept name)

- Nearby heading: # MUST use *a (not *ă) to undergo unstressed fronting: *a → *æ → *e

```text
13799: 2. ✓ Updated row 1936 (ban): proto `*bannas`, target `bannes` 
13800: 3. For span (fem. ō-stem), different paradigm — investigate separately
13801: 4. For wool, different issue (vowel) — investigate separately
13802: 
13803: **Results:** Mismatch count improved from 64 → 62 (2 fixes).
```

#### Germanic/docs/DEV_NOTES.md:14044 (concept name)

- Nearby heading: ### Implementation completed (2026-04-06)

```text
14042: The 62 count came from testing with a stale `backend/old_english.bin` that hadn't
14043: been updated from previous commits. The actual change from this commit is 56 → 55.
14044: The wool and lungen changes visible in the diff are from TSV updates in earlier
14045: commits that only became visible when the backend bin was refreshed.
14046: 
```

#### Germanic/docs/DEV_NOTES.md:24252 (exact PROTOFORM)

- Nearby heading: #### 1. Probe result

```text
24250: - Case 3 target **passes**: `*rástōz → ræste` ✓ (no longer in the
24251:   mismatch list).
24252: - Two incidental **fixes**: `*rústō` and `*wúllō` no longer mismatch.
24253: - Net mismatch total: 37 → 38 (+1).
24254: 
```

#### Germanic/docs/DEV_NOTES.md:24412 (exact PROTOFORM)

- Nearby heading: #### 6. Expected outcome

```text
24410:   derivation pattern.
24411: 
24412: - Pre-existing fixes `*rústō`, `*wúllō` **retained** (they were fixed
24413:   by §17.10.23's main innovation — the surviving-bimoric unrounding
24414:   + long-final AFB path — which is untouched by this reorder).
```

#### Germanic/docs/DEV_NOTES.md:24548 (exact PROTOFORM)

- Nearby heading: #### 6. Expected outcome

```text
24546: - All eight *-uz regressions dissolve (z stripped before OEMedUnstressedULowering
24547:   ever sees them, exactly as in pre-§17.10.24 behaviour).
24548: - `*rústō`, `*wúllō` re-acquire their §17.10.23 fix (the surviving-
24549:   bimoric + long-final-AFB path is untouched and composes
24550:   downstream).
```

#### Germanic/docs/DEV_NOTES.md:24572 (exact PROTOFORM)

- Nearby heading: #### 1. Re-classification of *rústō and *wúllō

```text
24570: attack Case 4 (`*fúnðanaz → funden`).
24571: 
24572: #### 1. Re-classification of *rústō and *wúllō
24573: 
24574: `*rústō → orst (expected rust)` and `*wúllō → woll (expected wull)`
```

#### Germanic/docs/DEV_NOTES.md:24574 (exact pair)

- Nearby heading: #### 1. Re-classification of *rústō and *wúllō

```text
24572: #### 1. Re-classification of *rústō and *wúllō
24573: 
24574: `*rústō → orst (expected rust)` and `*wúllō → woll (expected wull)`
24575: were reported as "new regressions" after §17.10.24/25 landed. They
24576: are **not actually regressions of our chronology work**. Three
```

#### Germanic/docs/DEV_NOTES.md:39770 (concept name)

- Nearby heading: ### Dossier inventory

```text
39768:   rule-ordering conflicts, a morphological/analogical change,
39769:   or an unformalized regular rule (e.g. Luick §247 /uRCr/
39770:   Dehnung)? Belongs in the wool/wolf/fugol wontfix bin?
39771: 
39772: ### Q3 finding — cell choice (target nom.sg., not plural)
```

### Analysis and dossier hits

#### Germanic/docs/analysis/notable_findings.md:341 (concept name)

- Nearby heading: ## 2. NWGmc u-lowering exceptions near labials: a non-Neogrammarian pattern

```text
340: can be explained by paradigmatic levelling. For instance, OE lufian 'love'
341: could owe its u to nom.sg. lufu with *-ō > *-u; OE wulle 'wool' could have
342: levelled from *wullō; OE spurnan 'kick' from 3sg. *spurniþi where *u was
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Lloyd1966 | author + year mention (Lloyd 1966) |
| HowellSalmons1988 | author + year mention (Salmons 1988) |
| Stiles2012 | author + year mention (Stiles 2012) |
| Campbell1959 | single available key for Campbell |
| Luick1914 | single available key for Luick |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| LloydSpringer1988 | explicit year mention (1988) |
| Cercignani1979 | surname mention only: Cercignani |
| Cercignani1980 | surname mention only: Cercignani |
| Stiles2017 | surname mention only: Stiles |
| Stiles1985 | surname mention only: Stiles |
| Stiles1986a | surname mention only: Stiles |
| Stiles1986b | surname mention only: Stiles |

## Paradigm probe

Paradigm probe required for this row, but no built-in `oe_paradigm_probe.py` specification exists yet. This packet should be used to draft the probe configuration before prose drafting.

