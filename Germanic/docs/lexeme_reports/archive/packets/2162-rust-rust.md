# Evidence packet — 2162 rust / rust

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2162 | rust | rust | *rústō | *rústō | unexplained_unmodelled | DOCUMENTED EXCEPTION (per §17.10.34): regular sound change gives **rost (Stiles 2012 §4.1.1.2 env. b: low *ō triggers a-umlaut). Campbell §115 groups with the u-preservation exceptions. No lautgesetzlich paradigm cell available: i-stem/gen.sg. cells with high *i would instead trigger i-umlaut (→ **ryst). | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# rust
PROTO: *rústō
EXPECTED: rust
OUTPUTS: rost



### Proto-Germanic consonant inheritance

Proto Input: *rústō

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>NWGmc U Lowering: *róstō<br>NWGmc Final Long O Raising: *róstu | **Old English**<br>OE High Vowel Apocope: *róst |



### Orthography & surface

Outcome: rost

NOTE: DOCUMENTED EXCEPTION (per §17.10.34): regular sound change gives *rost (Stiles 2012 §4.1.1.2 env. b: low *ō triggers a-umlaut). Campbell §115 groups with the u-preservation exceptions. No lautgesetzlich paradigm cell available: i-stem/gen.sg. cells with high *i would instead trigger i-umlaut (→ *ryst).
```

### Matching oe_known_problems.tsv entries

| proto | status | category | reason | refs | added |
| :--- | :--- | :--- | :--- | :--- | :--- |
| *rústō | wontfix | u_lowering_near_labial | u retention before /st/; also separate metathesis bug (orst output) | notable_findings#2 | 2026-04-25 |

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:24461 (exact pair)

- Nearby heading: #### 1. Probe outcome (vs. post-§17.10.23 baseline of 38)

```text
24459: | \*grúnduz  | grundo  | grund    |
24460: | \*kwíθuz   | cwiþo   | cwedu    |
24461: | \*rústō    | orst    | rust     |
24462: | \*spēnuz   | spōno   | spōn     |
24463: 
```

#### Germanic/docs/DEV_NOTES.md:24582 (exact COUNTERPART)

- Nearby heading: #### 1. Re-classification of *rústō and *wúllō

```text
24580:    `vowel_quality__u_lowering_exception`, not `vowel_quality__u_o_alternation`
24581:    — the report tool uses the `_U_LOWERING_ROOTS` set in
24582:    `oe_mismatch_report.py` (which already contains "rust"/"rost" and
24583:    "wull"/"woll") to separate documented lexical exceptions from
24584:    genuine model errors.
```

#### Germanic/docs/DEV_NOTES.md:24589 (row ID)

- Nearby heading: #### 1. Re-classification of *rústō and *wúllō

```text
24587:    `EXCEPTION: u-lowering blocked near labials (Luick §78, R/T
24588:    §2.3.1, Brunner §68). FST outputs regular woll; attested wull is
24589:    genuine lexical exception.` Row 2162 for `*rústō` similarly
24590:    notes `OE rust retains u; cf. R/T §2.3.1 for general u-lowering
24591:    exceptions.`
```

#### Germanic/docs/DEV_NOTES.md:25951 (exact pair)

- Nearby heading: ### §17.10.34 Cluster: u-lowering "exceptions" (wulf, fugol, bucc, rust, wull) — paradigm-cell switch for 4/5

```text
25949: | `*búkkaz` | `bocc` | `bucc` |
25950: | `*fúglaz` | `fogol` | `fugol` |
25951: | `*rústō` | `orst` | `rust` |
25952: | `*wúlfaz` | `wolf` | `wulf` |
25953: | `*wúllō` | `woll` | `wull` |
```

#### Germanic/docs/DEV_NOTES.md:26055 (exact pair)

- Nearby heading: #### Chosen approach: paradigm-cell switch for 4/5 (per §17.10.32)

```text
26053: | 2030 | `*fúglaz → fugol` (analogical, parasite vowel) | `*fúglis → fugles` (gen.sg., regular) | Stiles env. (a); also avoids parasite-vowel cell |
26054: | 1973 | `*búkkaz → bucc` (analogical) | `*búkkis → bucces` (gen.sg., regular) | Stiles env. (a) |
26055: | 2162 | `*rústō → rust` (wrong stem class — OE rust is masc. a-stem per BT) | `*rústis → rustes` (gen.sg. of *rústaz, regular) | Stiles env. (a); also corrects stem class |
26056: 
26057: For row 2162 (`rust`), the existing PROTOFORM `*rústō` (ō-stem,
```

#### Germanic/docs/DEV_NOTES.md:26057 (row ID)

- Nearby heading: #### Chosen approach: paradigm-cell switch for 4/5 (per §17.10.32)

```text
26055: | 2162 | `*rústō → rust` (wrong stem class — OE rust is masc. a-stem per BT) | `*rústis → rustes` (gen.sg. of *rústaz, regular) | Stiles env. (a); also corrects stem class |
26056: 
26057: For row 2162 (`rust`), the existing PROTOFORM `*rústō` (ō-stem,
26058: fem.) is also incorrect: BT s.v. *rust* gives "m. (-es; pl. -as)
26059: RUST". The cognate-set headword in the PROTO column is
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:19 (note keyword: i-umlaut)

- Nearby heading: ### Mismatch fixes (Mar 2026)

```text
17: - [Preconsonantal *x Loss: *xs > *s](#preconsonantal-x-loss-xs--s-before-consonant-clusters)
18: - [PGmc *d/*ð Representation Decision](#decision-2026-03-11-option-2a-confirmed)
19: - [OE þistel 'thistle': Scholarly Controversy](#oe-þistel-thistle-i-umlaut-not-preserved-2026-03-18)
20: - [OE huniġ 'honey': The -ag > -ig Sound Change](#oe-huniġ-honey-the--ag---ig-sound-change-2026-03-19)
21: - [OE wīþiġ 'withy': ja-stem vs Sievers' Law](#oe-wīþiġ-withy-ja-stem-adjective-vs-sievers-law-syncope-2026-03-19)
```

#### Germanic/docs/DEV_NOTES.md:78 (exact COUNTERPART)

- Nearby heading: ### The problem

```text
76: - *wullō → wulle (not ×wolle; OHG wolla)
77: - *lubō → lufu (not ×lofu)
78: - *rustō → rust (not ×rost)
79: 
80: ### Summary of the scholarly literature
```

#### Germanic/docs/DEV_NOTES.md:82 (note keyword: a-umlaut)

- Nearby heading: ### Summary of the scholarly literature

```text
80: ### Summary of the scholarly literature
81: 
82: **Bülbring (EB §116, pp.45-46)** provides the original hypothesis that both Luick and R/T engage with. He observes that OE u appears instead of expected o (from WGmc a-Umlaut, his §81d) "namentlich zwischen Labial und langem oder gedecktem l" — i.e. between a labial and ll or l+consonant: *full* 'full', *wulle* 'wool', *wulf* 'wolf'; also *fugol* 'bird', *bucca* 'buck', *múrnan* 'mourn'. He concedes that "meist steht jedoch der Hauptregel gemäß o" — usually the regular rule gives o — citing *wolcen, folgian, bolt, folc* as counterexamples. In his Anmerkung, Bülbring notes the agreement with OFris. and OS (afries. *ful, wulla, wulf*; as. *full, wulla, wulf, fugal*), which shows the phenomenon is "sehr alt" (very old). He remains agnostic on mechanism: "Ob wir darin Erhaltung des wg. u oder Wiederaufhebung der durch a-Umlaut herbeigeführten Veränderung erblicken müssen, läßt sich nicht mit Sicherheit entscheiden" — whether this reflects preservation of the original WGmc *u or reversal of a-Umlaut cannot be determined with certainty. He speculates that *u was lowered only partway ("etwa zu [ou] oder zu engem [o]") and then, under influence of its labial/velar environment, reverted to u, while in other words it continued to open [ɔ]. This "incomplete lowering + reversion" model is phonetically interesting but not formalizable as a categorical rule, since the same environments also show regular lowering.
83: 
84: **Luick (§78, Anm. 3)** engages directly with Bülbring's proposal and rejects it. He argues for paradigmatic leveling instead: doublet forms arose because paradigms had both u-preserving (high-vowel suffix) and u-lowering (non-high suffix) forms; near labials and gutturals, the u-forms were preferred. He explicitly cites the counterexamples that make Bülbring's phonological conditioning untenable: *wolcen, folc, folġian, folde, folm, bolla, bolt, bolster, molde, molcen, smolt* — all have labial or velar environments but regular lowering.
```

#### Germanic/docs/DEV_NOTES.md:93 (note keyword: gen.sg.)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
91: 
92: **Approach A: Use a u-stem or root-noun form.**
93: R/T notes that u-stems and root nouns regularly preserve *u because their paradigms have predominantly high-vowel suffixes (nom.sg. *-uz, acc.sg. *-ŷ, gen.sg. *-iz, dat.sg. *-i, nom.pl. *-iz, etc.). For example, *lustuz (u-stem nom.sg.) → OE lust with preserved u (R/T p.45). If *wulf-, *fugl-, or *bukk- were u-stems, we could use the nom.sg. in *-uz.
94: 
95: **What weighs against Approach A:**
```

#### Germanic/docs/DEV_NOTES.md:116 (note keyword: i-umlaut)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
114: - Root nouns are a small, archaic class (burg, brust, furh, hnut-); extending the analysis to common nouns like 'wolf' and 'fowl' would be speculative.
115: 
116: **Approach D: Use a derivational form with i-umlaut trigger.**
117: For some of the items, there are derivational forms with *j or *i that block lowering: *wulfi- (hypothetical i-stem variant?), or the derived verb *fullijaną 'to fill' → OE fyllan (where *-ij- blocks lowering of root *u).
118: 
```

#### Germanic/docs/DEV_NOTES.md:120 (note keyword: i-umlaut)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
118: 
119: **What weighs against Approach D:**
120: - These derived forms already show i-umlaut (*fullijaną → fyllan, not full). We can't simultaneously have the u preserved (from the high-vowel context) AND escape i-umlaut. The derivational base is a different word, not a paradigm form of the simplex noun.
121: 
122: ### Luick's doublets evidence
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

#### Germanic/docs/DEV_NOTES.md:709 (note keyword: i-umlaut)

- Nearby heading: ### Summary of OE syncope rules (scholarly consensus)

```text
707: 1. **Non-high vowel syncope** (`*a/*e → ∅`): Applies **regardless of preceding 
708:    syllable weight**, as long as the syllable is stressed. This affects PWGmc `*a` 
709:    and its i-umlaut product `*e`.
710:    
711:    Examples:
```

#### Germanic/docs/DEV_NOTES.md:742 (note keyword: i-umlaut)

- Nearby heading: ### The milk problem: `*melukz` → `meoloc` (expected `meolc`)

```text
740: with paradigm variation:
741: - Nom.sg.: `*melukz` → `meoloc` (with breaking `e → eo`, no syncope)
742: - Gen./dat.sg.: `*milukiz/*miluki` → Anglian `milc` (with i-umlaut and syncope)
743: 
744: R/T §6.6.4 (p.253): "The usual WS form of 'milk' is `meolc < meoluc < *meluk`... 
```

#### Germanic/docs/DEV_NOTES.md:749 (note keyword: i-umlaut)

- Nearby heading: ### The milk problem: `*melukz` → `meoloc` (expected `meolc`)

```text
747: 
748: **Key point:** The syncopated form `milc` shows **early syncope** that occurred even
749: before i-umlaut — R/T (p.257) notes this as a "possible early instance of syncope."
750: The WS form `meoloc ~ meolc` shows **variable syncope after a light syllable**.
751: 
```

#### Germanic/docs/DEV_NOTES.md:1379 (note keyword: gen.sg.)

- Nearby heading: ### 1. PWGmcSyllabicJ: *ja/*ją → *i (after light syllable, word-finally)

```text
1377: **Conditioning:** After a light syllable (short vowel + single consonant), word-finally.
1378: **Examples in our data:**
1379: - *bazją → *bazi → berġes ('berry', gen.sg.)
1380: - *harjaz → *hari → here ('army')
1381: - *natją → *nati → net ('net')
```

#### Germanic/docs/DEV_NOTES.md:2733 (note keyword: gen.sg.)

- Nearby heading: ### The Three Fates of Word-Final *ō

```text
2731: - Examples: ō-stem acc.sg. *gebō(n?) → *gebō (after ending loss) → PWGmc
2732:     *geba → OE giefe
2733:   ō-stem gen.sg. *gebōz → *gebō (after z-loss) → PWGmc *geba → OE giefe
2734:   fem. n-stem nom.sg. *tungōn → *tungō̃ (after n-loss, nasalized) →
2735:     PWGmc *tunga → OE tunge
```

#### Germanic/docs/DEV_NOTES.md:2738 (note keyword: gen.sg.)

- Nearby heading: ### The Three Fates of Word-Final *ō

```text
2736: - **Our FST**: For fem. n-stems, modelled by NWGmcNStemNLoss: {*ō}{*n} →
2737:   {*ǭ} word-finally, then {*ǭ} → {*æ} → OE -e. This covers the n-stem case.
2738:   For other "surviving bimoric" cases (acc.sg., gen.sg. of ō-stems), we DON'T
2739:   have a rule — but these paradigm cells aren't in our TSV data.
2740: 
```

#### Germanic/docs/DEV_NOTES.md:3131 (note keyword: gen.sg.)

- Nearby heading: ### Root cause: {*æ} should NOT trigger A-restoration

```text
3129: ### Root cause: {*æ} should NOT trigger A-restoration
3130: 
3131: The `{*æ}` symbol was added to the A-restoration trigger set based on an incorrect analysis that suffix *a (like gen.sg. *-as), after being fronted to *æ by AFB, still triggers restoration as an "underlyingly back" vowel.
3132: 
3133: **R/T's paradigm disproves this (§6.3.2, p. 199):**
```

#### Germanic/docs/DEV_NOTES.md:3134 (note keyword: gen.sg.)

- Nearby heading: ### Root cause: {*æ} should NOT trigger A-restoration

```text
3132: 
3133: **R/T's paradigm disproves this (§6.3.2, p. 199):**
3134: - gen.sg. *dagas → *dæges → OE **dæges** (NOT *dages) — A-restoration does NOT fire
3135: - nom.pl. *dagos → OE **dagas** — A-restoration DOES fire (suffix *-os has genuine back *o)
3136: - dat.pl. *dagum → OE **dagum** — A-restoration DOES fire (suffix *-um has genuine back *u)
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

#### Germanic/docs/DEV_NOTES.md:10430 (exact COUNTERPART)

- Nearby heading: ## Mismatch Progress Log (2026-03-14)

```text
10428: | 2026-04-28 | 16 | -1 | 7f8a289b | westene: target alignment with *wéstanē (§17.38) |
10429: | 2026-04-28 | 15 | -1 | 14565e33 | sċuldrum: DatPl *-amiz cascade (§17.41) |
10430: | 2026-04-28 | 15 | 0 | 97aab23e | OERMetathesis word-initial guard (rust → ledger; §17.42) |
10431: | 2026-04-28 | 14 | -1 | 400e41c8 | þrīe: TSV retarget þrī → þrīe early-WS (§17.43) |
10432: | 2026-04-29 | 13 | -1 | (pending) | *tíkkô: TSV retarget gloss ticia → ticca per Kroonen 2013 (§17.44) |
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

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:456 (note keyword: i-umlaut)

- Nearby heading: ## 7. R/T relative chronology of A-fronting, A-restoration, breaking, and i-umlaut

```text
455: 
456: ## 7. R/T relative chronology of A-fronting, A-restoration, breaking, and i-umlaut
457: 
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:472 (note keyword: i-umlaut)

- Nearby heading: ## 7. R/T relative chronology of A-fronting, A-restoration, breaking, and i-umlaut

```text
471: (3) *a before single C / geminate / sC + back vowel
472:  ↓ I-umlaut (R/T §6.6)
473: (4) modifies remaining *æ but cannot un-restore *a
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:735 (note keyword: i-umlaut)

- Nearby heading: ## 11. Affected TSV rows

```text
734: | 2056 | `*xármaz` | `hearm` | breaking |
735: | 2057 | `*xárbistuz` | `hierfest` | breaking + i-umlaut |
736: | 2077 | `*xáldaną` | `healdan` | breaking |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:154 (note keyword: i-umlaut)

- Nearby heading: ### Case 6: *líznōn- (learn) — leornian

```text
153: | **Lautgesetzlich output** | `leornian` (from *e-grade root `*leznōn-`) (FST: ✓ correct with corrected proto) |
154: | **Previous FST output** | `liernian` (from incorrect *i-grade root `*liznōn-` + i-umlaut *eo → ie*) |
155: | **DEV_NOTES reference** | §14.518–14.760 (OE leornian 'to learn' — ie vs eo diphthong problem); major cross-reference in mismatch_dossier_mizdo.md (Campbell §123 fn.2 citation) |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:168 (note keyword: i-umlaut)

- Nearby heading: ### Case 7: *fúwerō / *fūri (fire) — fȳre (dat.sg.) vs. fȳr (nom.sg.)

```text
167: | **PROTO** | `*fūri` (dat.sg., locative singular; singular = u-stem or ī-stem, feminine) |
168: | **OE SIMPLEX (NOM.SG.)** | `fȳr` (nom.sg., attested, showing i-umlaut of *ū → *ȳ*) |
169: | **OE SIMPLEX (DAT.SG.)** | `fȳre` (dat.sg., showing i-umlaut plus **analogically restored** final *-e*) |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:169 (note keyword: i-umlaut)

- Nearby heading: ### Case 7: *fúwerō / *fūri (fire) — fȳre (dat.sg.) vs. fȳr (nom.sg.)

```text
168: | **OE SIMPLEX (NOM.SG.)** | `fȳr` (nom.sg., attested, showing i-umlaut of *ū → *ȳ*) |
169: | **OE SIMPLEX (DAT.SG.)** | `fȳre` (dat.sg., showing i-umlaut plus **analogically restored** final *-e*) |
170: | **Sound changes** | I-umlaut (*ū → ȳ* before *i) + Apocope (final *-i → Ø* after heavy syllable) + Analogical restoration (*-e added*) |
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:48 (note keyword: i-umlaut)

- Nearby heading: ### OE paradigm of cū (§6.6.1, line 18238)

```text
47: - **nom.sg.** cū (< leveled *kū, analogical from oblique)
48: - **dat.sg.** cȳ (< *kūi, regular i-umlaut: ū → ȳ)
49: - **nom.-acc.pl.** cȳ (< *kūiz, same i-umlaut)
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:49 (note keyword: i-umlaut)

- Nearby heading: ### OE paradigm of cū (§6.6.1, line 18238)

```text
48: - **dat.sg.** cȳ (< *kūi, regular i-umlaut: ū → ȳ)
49: - **nom.-acc.pl.** cȳ (< *kūiz, same i-umlaut)
50: - **gen.sg.** cā (< *kūiz? — form uncertain, R/T say "apparently")
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:61 (note keyword: i-umlaut)

- Nearby heading: ### Hall's Concise Anglo-Saxon Dictionary

```text
60: 
61: This matches R/T's §7 observation (line 21452): "The ō-stem gen. sg. ending -e has spread to fem. root-nouns, where it is in competition with the inherited endingless form with i-umlaut."
62: 
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:46 (note keyword: i-umlaut)

- Nearby heading: ### OE target assessment

```text
45: 3. **Breaking**: \*æhh → \*eahh
46: 4. **i-Umlaut**: \*eahh → \*ieahh → hiehh (WS palatal diphthong umlaut)
47: 
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:105 (note keyword: i-umlaut)

- Nearby heading: ### Proto-form assessment

```text
104: The proto `*skellinăz` does not match Kroonen's reconstruction. The \*e in
105: \*skellinăz would give OE \*sċiellen (via i-umlaut and palatalization), but the
106: attested form is sċilling with *i.
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:114 (note keyword: i-umlaut)

- Nearby heading: ### Pipeline issues

```text
113: 
114: 2. **With current proto** `skellinăz`: the pipeline produces `sċiellen` (with i-umlaut
115:    of *e → *ie, but no mechanism to produce *i in the root).
```

#### Germanic/docs/analysis/fryhtu_investigation.md:26 (note keyword: i-umlaut)

- Nearby heading: ### R/T's analysis

```text
25: 
26: R/T (line 21553) treat OE fyrhtu as an **ī-stem abstract noun**. The i-umlaut
27: (\*u → y) proves an \*i-containing source, since the ō-stem \*furhtō- would give
```

#### Germanic/docs/analysis/fryhtu_investigation.md:34 (note keyword: i-umlaut)

- Nearby heading: ### The \*iþō-abstract analysis

```text
33: with the suffix PGmc \*-iþō-. These are inflectionally ō-stems but contain the
34: derivational element \*-iþ- which triggers i-umlaut. Well-known examples:
35: 
```

#### Germanic/docs/analysis/fryhtu_investigation.md:45 (note keyword: i-umlaut)

- Nearby heading: ### The \*iþō-abstract analysis

```text
44: 
45: 1. **i-umlaut**: \*furhtiþō → \*fyrhtiþō (\*u → \*y, triggered by \*i in suffix)
46: 2. **Medial vowel syncope**: \*fyrhtiþō → \*fyrhþō (unstressed medial \*i lost)
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:809 (note keyword: gen.sg.)

- Nearby heading: ## 5. FST-probe relevance

```text
808: 4. The FST output of `meorde` from BOTH `mizdai` (dat.sg.) and
809:    `mizdōz` (gen.sg.) is striking: it means the **paradigm-cell
810:    targeting** approach (the user's preferred framing under
```

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

#### Germanic/docs/analysis/notable_findings.md:1095 (note keyword: a-umlaut)

- Nearby heading: ## 7. NWGmc *i > *e lowering: consonant-conditioned blocking and rule ordering

```text
1094: 
1095: - **Lloyd (1966):** Argues that "the so-called a-umlaut of i in Proto-Germanic
1096:   did not exist" and that sporadic \*e forms result from "systemic analogy"
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:66 (note keyword: gen.sg.)

- Nearby heading: ### For \*sumaraz and \*xamaras

```text
65: 4. Both `hamor` and `hamer` are **attested** (Wiktionary: "OE hamor, hamer, homer")
66: 5. Hall's dictionary gives gen.sg. **sumeres** (with -e-), confirming -e- in oblique forms
67: 
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:150 (note keyword: gen.sg.)

- Nearby heading: ### 1. \*sumerăz/sumor → fix proto AND target

```text
149: "sumer" (via \*a → \*æ by a-fronting → e by unstressed æ/i merger). Both forms
150: are attested (Kroonen: "OE sumer, sumor m."; Hall's: gen.sg. "sumeres").
151: 
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

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:239 (note keyword: i-umlaut)

- Nearby heading: ### §4.2 Phonological assessment

```text
238: * **`bȳhþ` / `bȳhst`** (3/2 sg. pres. ind.): would require
239:   i-umlaut of the *u* (or of the inherited *iu* > *í*-stage)
240:   followed by spirantisation/devoicing of the stem-final consonant
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:326 (note keyword: i-umlaut)

- Nearby heading: ### §5.2 Phonological assessment

```text
325:   a-mutation, then *-anaz > -en. Universal attestation.
326: * **`sċȳfþ`** (3 sg. pres. ind.): would require i-umlaut + cluster
327:   realisation parallel to `bȳhþ`; possible but more cascade-
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:32 (note keyword: i-umlaut)

- Nearby heading: ## 1. TL;DR

```text
31: > **Inherited West-Gmc /ɣ/ palatalises to OE [ʝ] > [j] (spelt ġ) when it is
32: > adjacent to a front vowel (i, ī, e, ē, æ, ǣ, y, ȳ from i-umlaut, ie/ī from
33: > i-umlaut, and the front diphthongs io/eo/ea, ie/ȳ) AND a following back
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:33 (note keyword: i-umlaut)

- Nearby heading: ## 1. TL;DR

```text
32: > adjacent to a front vowel (i, ī, e, ē, æ, ǣ, y, ȳ from i-umlaut, ie/ī from
33: > i-umlaut, and the front diphthongs io/eo/ea, ie/ȳ) AND a following back
34: > vowel does not "rescue" it.**
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:79 (note keyword: i-umlaut)

- Nearby heading: ### 2.1 Campbell, *Old English Grammar* (1959), §§ 426–430

```text
78: > i.e. by æ, e, i, by ǣ, ē, ī, by the diphthongs ǣa, ēa, eo, io, by æ̆ and
79: > ē̆ where these are due to i-umlaut, but not by y, ȳ, œ, ø̄ from i-umlaut of
80: > u, ū, o, ō (cf. § 190)."
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
| rust | rust | inh | template:inh | rust |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1430 (exact pair)

- Nearby heading: ## Project Status (as of 2026-04-30) — research phase complete

```text
1428: * `*fūri → fȳr` (expected `fȳre`) — `exception: analogical_dat_e`
1429: * `*fúglaz → fogol` (expected `fugol`) — `wontfix: u_lowering_near_labial`
1430: * `*rústō → rost` (expected `rust`) — `wontfix: u_lowering_near_labial`
1431: * `*táppô → tappa` (expected `tæppa`) — `exception: analogical_n_stem_levelling`
1432: * `*wúlfaz → wolf` (expected `wulf`) — `wontfix: u_lowering_near_labial`
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

#### Germanic/docs/DEV_NOTES.md:24574 (exact pair)

- Nearby heading: #### 1. Re-classification of *rústō and *wúllō

```text
24572: #### 1. Re-classification of *rústō and *wúllō
24573: 
24574: `*rústō → orst (expected rust)` and `*wúllō → woll (expected wull)`
24575: were reported as "new regressions" after §17.10.24/25 landed. They
24576: are **not actually regressions of our chronology work**. Three
```

#### Germanic/docs/DEV_NOTES.md:26117 (row ID)

- Nearby heading: #### Implementation order

```text
26115:    convention: PROTOFORM = cell-specific FST input; PROTO = cognate
26116:    headword (preserved as `*wúlfaz`/`*fúglaz`/`*búkkaz`; corrected to
26117:    `*rústaz` for row 2162).
26118: 3. Re-run `python3 tools/oe_mismatch_report.py`; verify count is 32
26119:    and only the four target rows changed.
```

### Analysis and dossier hits

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:61 (note keyword: gen.sg.)

- Nearby heading: ### 2.1 Standard dictionary lemmata

```text
60: - Etymology: "from PGmc. *mizdō"
61: - Inflection: strong fem. ō-stem (nom.sg. mēd, acc.sg. mēd/mēde, gen.sg. mēde, dat.sg. mēde)
62: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:292 (note keyword: i-umlaut)

- Nearby heading: ### 4.1 Primary handbooks

```text
291:   - Standard breaking rule: *e → *eo / __ {r, x}C
292: - **§202** (pp. 80–82): Describes i-umlaut of breaking diphthongs
293:   - "A small group of words (§124) suggest that the mutation of eo was io"
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:518 (note keyword: i-umlaut)

- Nearby heading: ### 6.2 Other *i + rd clusters (rhotacized)

```text
517: 1. `*búrdiz` 'birth' (row 1951) → FST: `byrd` ✓
518:    - Expected: `*búrdiz` → u-lowering → `*bordiz` → breaking (blocked, because *o not *e/*i) → i-umlaut `*byrd` ✓
519: 2. `*xérdō` 'herd' (row 2073) → FST: `heord` ✓
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:51 (note keyword: i-umlaut)

- Nearby heading: ## 1. Charge of this supplement

```text
50: 
51: 3. **Parallel with \*rēc** (notable_findings.md #10): OE *rēc* 'smoke' shows universal long ē across all dialects where we expect WS diphthong *īe (from *au + i-umlaut). Both *rēc* and *mēd* avoid expected diphthongs. Is there a systematic development *VzC → VːC* that yields ē regularly, making *meord* the marked form rather than *mēd*?
52: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:522 (note keyword: i-umlaut)

- Nearby heading: ### 5.1 The *rēc case (notable_findings.md #10)

```text
521: **OE rēc** 'smoke' < PGmc *\*raukiz (m. i-stem):
522: - **Expected WS outcome**: *\*rīec (from *au + i-umlaut → *īe)
523: - **Attested outcome**: **rēc** (long ē monophthong, **no diphthong**)
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:556 (note keyword: i-umlaut)

- Nearby heading: ### 5.3 Testing the VzC → VːC hypothesis

```text
555: Other *i + rd clusters (after rhotacism):
556: 1. *\*búrdiz* 'birth' → OE *byrd* (no issue; *u lowers, then i-umlaut)
557: 2. *\*xérdō* 'herd' → OE *heord* ✓ (regular breaking of *e → *eo)
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | author + year mention (Kroonen 2013) |
| Lloyd1966 | author + year mention (Lloyd 1966) |
| HowellSalmons1988 | author + year mention (Salmons 1988) |
| Stiles2012 | author + year mention (Stiles 2012) |
| Campbell1959 | single available key for Campbell |
| SieversBrunner1965 | single available key for Sievers |
| Luick1914 | single available key for Luick |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |
| LloydSpringer1988 | explicit year mention (1988) |
| Cercignani1979 | surname mention only: Cercignani |
| Cercignani1980 | surname mention only: Cercignani |
| Stiles2017 | surname mention only: Stiles |
| Stiles1985 | surname mention only: Stiles |
| Stiles1986a | surname mention only: Stiles |
| Stiles1986b | surname mention only: Stiles |

## Paradigm probe

Paradigm probe required for this row, but no built-in `oe_paradigm_probe.py` specification exists yet. This packet should be used to draft the probe configuration before prose drafting.

