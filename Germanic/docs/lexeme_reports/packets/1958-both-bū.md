# Evidence packet — 1958 both / bū

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1958 | both | bū | *bō | *bō | regular | OE neut. dual 'both' (paradigm bēġen m. / bā f. / bū ~ bā n.; Brunner §324 Anm.2, Campbell §683, Fulk §10.1). PROTOFORM is un-extended PGmc neut. dual *bō (Kroonen 4678-4694 s.v. *ba-). Modern E `both` does NOT continue this OE form: it descends from ON báðir (PGmc *bai-þ- extended stem, cogn. with G beide, NL beide); see §17.30. Earlier target `bā]] [[þā` was Wiktionary template:inh extraction garbage. Lemma `bū` chosen over `bēġen` because the latter is at least partly analogical (Kroonen 2013: 47, -en from twēġen) and over `bā` because the FST currently mishandles *bai → bē instead of bā (separate issue, parked). Mismatch persists pending §17.31: FST currently shortens *bō → bu via weak-tail reduction; correct behaviour is no shortening of a monosyllable's only vowel (Campbell §122: cū, hū, tū, bū). Fix should be a guard on the apocope/weak-tail rule, not new stressed-long-vowel inventory. | Source: Wiktionary etymology (template:inh) \| Source: Wiktionary etymology (template:inh) |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# both
PROTO: *bō
EXPECTED: bū
OUTPUTS: bū



### Proto-Germanic consonant inheritance

Proto Input: *bō

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>NWGmc Stressed Monosyllable O Raising: *bū | **Old English**<br>[no change] |



### Orthography & surface

Outcome: bū

NOTE: OE neut. dual 'both' (paradigm bēġen m. / bā f. / bū ~ bā n.; Brunner §324 Anm.2, Campbell §683, Fulk §10.1). PROTOFORM is un-extended PGmc neut. dual *bō (Kroonen 4678-4694 s.v. *ba-). Modern E `both` does NOT continue this OE form: it descends from ON báðir (PGmc *bai-þ- extended stem, cogn. with G beide, NL beide); see §17.30. Earlier target `bā]] [[þā` was Wiktionary template:inh extraction garbage. Lemma `bū` chosen over `bēġen` because the latter is at least partly analogical (Kroonen 2013: 47, -en from twēġen) and over `bā` because the FST currently mishandles *bai → bē instead of bā (separate issue, parked). Mismatch persists pending §17.31: FST currently shortens *bō → bu via weak-tail reduction; correct behaviour is no shortening of a monosyllable's only vowel (Campbell §122: cū, hū, tū, bū). Fix should be a guard on the apocope/weak-tail rule, not new stressed-long-vowel inventory.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:37295 (exact pair)

- Nearby heading: #### .1.d Modern English `both`

```text
37293:   cognate with G `beide` *via* PGmc `*bai-þ-`.
37294: - OE `bēġen` died out without survival in ModE.
37295: - The cogset header `*bō` is awkward: it fits OE `bū`/`bā` (un-extended
37296:   stem) but not the German/Dutch/MnE forms (which need *bai-þ-).
37297: 
```

#### Germanic/docs/DEV_NOTES.md:37303 (exact pair)

- Nearby heading: #### .1.e FST gap assessment

```text
37301: - `*bṓjenō` → `+?` (rejected; pgrmWord shape coverage gap)
37302: - `*bōjenaz` (no stress) → `bēien` — short /e/, no length, j retained as i
37303: - `*bō` → `bu` (stressed monosyllable; SHOULD be long `bū` per Campbell
37304:   §122 "final accented ō → ū … OE cū, hū, **tū**, **bū** both")
37305: - `*kō` → `cu` (same bug; should be `cū`)
```

#### Germanic/docs/DEV_NOTES.md:37347 (row ID)

- Nearby heading: ### .3 TSV change (this loop only — no FST changes yet)

```text
37345: ### .3 TSV change (this loop only — no FST changes yet)
37346: 
37347: Row 1958, OE row in cogset "both":
37348: 
37349: | field | before | after |
```

#### Germanic/docs/DEV_NOTES.md:37362 (row ID)

- Nearby heading: ### .4 Predicted side-effects

```text
37360: ### .4 Predicted side-effects
37361: 
37362: - Row 1958 still mismatches (FST gives short `bu` ≠ target `bū`) until
37363:   the §17.31 monosyllable-guard fix lands.
37364: - Mismatch count unchanged at 24; tractable list moves this row to a
```

#### Germanic/docs/DEV_NOTES.md:37373 (row ID)

- Nearby heading: ### .5 Verification plan (this loop)

```text
37371: ### .5 Verification plan (this loop)
37372: 
37373: 1. Edit row 1958 (ALIGNMENT, COUNTERPART, NOTE; PROTOFORM unchanged).
37374: 2. Run reports; expect mismatch count unchanged at 24.
37375: 3. Commit DEV_NOTES + TSV.
```

#### Germanic/docs/DEV_NOTES.md:37649 (exact pair)

- Nearby heading: ### .9 Regression risk

```text
37647: - `*sōkjan → sēċan`, `*dōmjan → dēman`: not affected (internal ō)
37648: - `*xūs → hūs`, `*bū → bū`: already pass, must still pass
37649: - `*kō → cū`, `*twō → tū`, `*hwō → hū`, `*bō → bū`: must now pass (new outcome)
37650: 
37651: ### .10 Open questions
```

#### Germanic/docs/DEV_NOTES.md:37751 (row ID)

- Nearby heading: ### §17.31.11 — Implementation outcome (2026-…)

```text
37749: **Mismatch count**: 24 → 23. Tractable 16 → 15.
37750: 
37751: **Status**: row 1958 (*bō → bū) now passes. The *kō row, if present
37752: in the corpus, is also now correct. The fix is general — any future
37753: stressed-monosyllabic *-ō entry will derive *-ū automatically.
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:37233 (exact COUNTERPART)

- Nearby heading: #### .1.a Attestation (Brunner §324 Anm.2 = `brunner_1965_altenglische_grammatik.vision.txt:13207-13217`; Campbell §683 = `campbell_old_english_grammar.txt:18919-18953`; Fulk §10.1 = `fulk_comparative_grammar_early_germanic.txt:15632-15638)

```text
37231: | | masc. | fem. | neut. |
37232: |---|---|---|---|
37233: | N/A | **bēġen** | **bā** | **bā, bū** |
37234: | Gen. | bēġra, bēġ(e)a | bēġra, bēġ(e)a | bēġra, bēġ(e)a |
37235: | Dat. | bǣm | bǣm | bǣm |
```

#### Germanic/docs/DEV_NOTES.md:37237 (exact COUNTERPART)

- Nearby heading: #### .1.a Attestation (Brunner §324 Anm.2 = `brunner_1965_altenglische_grammatik.vision.txt:13207-13217`; Campbell §683 = `campbell_old_english_grammar.txt:18919-18953`; Fulk §10.1 = `fulk_comparative_grammar_early_germanic.txt:15632-15638)

```text
37235: | Dat. | bǣm | bǣm | bǣm |
37236: 
37237: Compound dual-numeral construction `bā twā` (m./f.), `bū tū` (n.),
37238: `bām twām` (dat.), often written together (`bū-twū`, `bū-tā`).
37239: 
```

#### Germanic/docs/DEV_NOTES.md:37238 (exact COUNTERPART)

- Nearby heading: #### .1.a Attestation (Brunner §324 Anm.2 = `brunner_1965_altenglische_grammatik.vision.txt:13207-13217`; Campbell §683 = `campbell_old_english_grammar.txt:18919-18953`; Fulk §10.1 = `fulk_comparative_grammar_early_germanic.txt:15632-15638)

```text
37236: 
37237: Compound dual-numeral construction `bā twā` (m./f.), `bū tū` (n.),
37238: `bām twām` (dat.), often written together (`bū-twū`, `bū-tā`).
37239: 
37240: Dialectal:
```

#### Germanic/docs/DEV_NOTES.md:37244 (exact COUNTERPART)

- Nearby heading: #### .1.a Attestation (Brunner §324 Anm.2 = `brunner_1965_altenglische_grammatik.vision.txt:13207-13217`; Campbell §683 = `campbell_old_english_grammar.txt:18919-18953`; Fulk §10.1 = `fulk_comparative_grammar_early_germanic.txt:15632-15638)

```text
37242:   bōezo` (L); gen. `bōēġera` (Rit.). The `oe` digraph = unrounded ø̄
37243:   (i-umlaut of ō).
37244: - Mercian R¹: `bēġen, bū` (WS-like ē).
37245: - Vesp.Ps.: lemma unattested.
37246: - Kentish (9th-c.): gen. `bēġa` ~ `bōēġa`; dat. `bǣm` ~ `bōēm`.
```

#### Germanic/docs/DEV_NOTES.md:37256 (exact PROTOFORM)

- Nearby heading: #### .1.b Reconstruction state of the art

```text
37254: | Source | OE bēġen ← |
37255: |---|---|
37256: | Sievers Beitr. 18, 407 → Holthausen → **Brunner §324 Anm.2** → **Orel** (`orel:6294-6295`) | **\*bōjenō** (compound `*bō- + jenō`); sound-law derivation |
37257: | **Fulk** §10.1 (`fulk:15584-15596, 15662-15667`) | accepts `*bō-jen-` cautiously; flags Seebold's objection |
37258: | **Seebold 1968: 418-21** (cited in Fulk 15662-7) | rejects `*bō-jen-`; favours `*bō-þ-` (article-stem), parallel to ON báðir, OHG bēde |
```

#### Germanic/docs/DEV_NOTES.md:37257 (exact PROTOFORM)

- Nearby heading: #### .1.b Reconstruction state of the art

```text
37255: |---|---|
37256: | Sievers Beitr. 18, 407 → Holthausen → **Brunner §324 Anm.2** → **Orel** (`orel:6294-6295`) | **\*bōjenō** (compound `*bō- + jenō`); sound-law derivation |
37257: | **Fulk** §10.1 (`fulk:15584-15596, 15662-15667`) | accepts `*bō-jen-` cautiously; flags Seebold's objection |
37258: | **Seebold 1968: 418-21** (cited in Fulk 15662-7) | rejects `*bō-jen-`; favours `*bō-þ-` (article-stem), parallel to ON báðir, OHG bēde |
37259: | **Kroonen 2013** s.v. *ba- (`kroonen:4678-4694`, esp. 4681) | OE bēġen = **analogical** (`-en` from `twēġen`, lit. 'both two'); inherited PGmc paradigm is bare `*bai, *bōz, *bō`; no `*bōjenō` |
```

#### Germanic/docs/DEV_NOTES.md:37258 (exact PROTOFORM)

- Nearby heading: #### .1.b Reconstruction state of the art

```text
37256: | Sievers Beitr. 18, 407 → Holthausen → **Brunner §324 Anm.2** → **Orel** (`orel:6294-6295`) | **\*bōjenō** (compound `*bō- + jenō`); sound-law derivation |
37257: | **Fulk** §10.1 (`fulk:15584-15596, 15662-15667`) | accepts `*bō-jen-` cautiously; flags Seebold's objection |
37258: | **Seebold 1968: 418-21** (cited in Fulk 15662-7) | rejects `*bō-jen-`; favours `*bō-þ-` (article-stem), parallel to ON báðir, OHG bēde |
37259: | **Kroonen 2013** s.v. *ba- (`kroonen:4678-4694`, esp. 4681) | OE bēġen = **analogical** (`-en` from `twēġen`, lit. 'both two'); inherited PGmc paradigm is bare `*bai, *bōz, *bō`; no `*bōjenō` |
37260: | **Ringe-Taylor vol. 2** | silent on this lemma |
```

#### Germanic/docs/DEV_NOTES.md:37259 (exact PROTOFORM)

- Nearby heading: #### .1.b Reconstruction state of the art

```text
37257: | **Fulk** §10.1 (`fulk:15584-15596, 15662-15667`) | accepts `*bō-jen-` cautiously; flags Seebold's objection |
37258: | **Seebold 1968: 418-21** (cited in Fulk 15662-7) | rejects `*bō-jen-`; favours `*bō-þ-` (article-stem), parallel to ON báðir, OHG bēde |
37259: | **Kroonen 2013** s.v. *ba- (`kroonen:4678-4694`, esp. 4681) | OE bēġen = **analogical** (`-en` from `twēġen`, lit. 'both two'); inherited PGmc paradigm is bare `*bai, *bōz, *bō`; no `*bōjenō` |
37260: | **Ringe-Taylor vol. 2** | silent on this lemma |
37261: 
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| both | bā]] [[þā | inh | template:inh | both |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:82 (concept name)

- Nearby heading: ### Summary of the scholarly literature

```text
80: ### Summary of the scholarly literature
81: 
82: **Bülbring (EB §116, pp.45-46)** provides the original hypothesis that both Luick and R/T engage with. He observes that OE u appears instead of expected o (from WGmc a-Umlaut, his §81d) "namentlich zwischen Labial und langem oder gedecktem l" — i.e. between a labial and ll or l+consonant: *full* 'full', *wulle* 'wool', *wulf* 'wolf'; also *fugol* 'bird', *bucca* 'buck', *múrnan* 'mourn'. He concedes that "meist steht jedoch der Hauptregel gemäß o" — usually the regular rule gives o — citing *wolcen, folgian, bolt, folc* as counterexamples. In his Anmerkung, Bülbring notes the agreement with OFris. and OS (afries. *ful, wulla, wulf*; as. *full, wulla, wulf, fugal*), which shows the phenomenon is "sehr alt" (very old). He remains agnostic on mechanism: "Ob wir darin Erhaltung des wg. u oder Wiederaufhebung der durch a-Umlaut herbeigeführten Veränderung erblicken müssen, läßt sich nicht mit Sicherheit entscheiden" — whether this reflects preservation of the original WGmc *u or reversal of a-Umlaut cannot be determined with certainty. He speculates that *u was lowered only partway ("etwa zu [ou] oder zu engem [o]") and then, under influence of its labial/velar environment, reverted to u, while in other words it continued to open [ɔ]. This "incomplete lowering + reversion" model is phonetically interesting but not formalizable as a categorical rule, since the same environments also show regular lowering.
83: 
84: **Luick (§78, Anm. 3)** engages directly with Bülbring's proposal and rejects it. He argues for paradigmatic leveling instead: doublet forms arose because paradigms had both u-preserving (high-vowel suffix) and u-lowering (non-high suffix) forms; near labials and gutturals, the u-forms were preferred. He explicitly cites the counterexamples that make Bülbring's phonological conditioning untenable: *wolcen, folc, folġian, folde, folm, bolla, bolt, bolster, molde, molcen, smolt* — all have labial or velar environments but regular lowering.
```

#### Germanic/docs/DEV_NOTES.md:84 (concept name)

- Nearby heading: ### Summary of the scholarly literature

```text
82: **Bülbring (EB §116, pp.45-46)** provides the original hypothesis that both Luick and R/T engage with. He observes that OE u appears instead of expected o (from WGmc a-Umlaut, his §81d) "namentlich zwischen Labial und langem oder gedecktem l" — i.e. between a labial and ll or l+consonant: *full* 'full', *wulle* 'wool', *wulf* 'wolf'; also *fugol* 'bird', *bucca* 'buck', *múrnan* 'mourn'. He concedes that "meist steht jedoch der Hauptregel gemäß o" — usually the regular rule gives o — citing *wolcen, folgian, bolt, folc* as counterexamples. In his Anmerkung, Bülbring notes the agreement with OFris. and OS (afries. *ful, wulla, wulf*; as. *full, wulla, wulf, fugal*), which shows the phenomenon is "sehr alt" (very old). He remains agnostic on mechanism: "Ob wir darin Erhaltung des wg. u oder Wiederaufhebung der durch a-Umlaut herbeigeführten Veränderung erblicken müssen, läßt sich nicht mit Sicherheit entscheiden" — whether this reflects preservation of the original WGmc *u or reversal of a-Umlaut cannot be determined with certainty. He speculates that *u was lowered only partway ("etwa zu [ou] oder zu engem [o]") and then, under influence of its labial/velar environment, reverted to u, while in other words it continued to open [ɔ]. This "incomplete lowering + reversion" model is phonetically interesting but not formalizable as a categorical rule, since the same environments also show regular lowering.
83: 
84: **Luick (§78, Anm. 3)** engages directly with Bülbring's proposal and rejects it. He argues for paradigmatic leveling instead: doublet forms arose because paradigms had both u-preserving (high-vowel suffix) and u-lowering (non-high suffix) forms; near labials and gutturals, the u-forms were preferred. He explicitly cites the counterexamples that make Bülbring's phonological conditioning untenable: *wolcen, folc, folġian, folde, folm, bolla, bolt, bolster, molde, molcen, smolt* — all have labial or velar environments but regular lowering.
85: 
86: **R/T (§2.3.1, pp.32-33 / our OCR pp.47-48)** agree these are genuine exceptions but reach a different conclusion about paradigmatic leveling. They find it "implausible" for a-stem nouns, arguing that the only case-forms with high-vowel suffixes are functionally marginal: inst.sg. *-u, dat.pl. *-umaz, inst.pl. *-umiz. They conclude: "We do not really know why *u failed to lower in these forms."
```

#### Germanic/docs/DEV_NOTES.md:132 (concept name)

- Nearby heading: ### Areal variation

```text
130: ### Areal variation
131: 
132: Luick (Anm. 1) and R/T both note that OE, OFris., and OS share the u-preserving forms, while OHG has regular lowered forms: OE/OS wulf vs. OHG wolf, OE/OS full vs. OHG fol. This is a NWGmc areal feature, not specifically OE. R/T goes further: for *wulfaz, even OF (!) shows wolf with lowering, which is unexpected if the u-preservation were a shared northern WGmc innovation.
133: 
134: ### Decision and implementation
```

#### Germanic/docs/DEV_NOTES.md:142 (concept name)

- Nearby heading: ### Decision and implementation

```text
140: **Additional citation (Brunner §68):** Brunner echoes Bülbring: "In einigen Wörtern steht, zumal in der Nachbarschaft von Labialen, statt des zu erwartenden o ein u, z. B. full voll, wulf Wolf, wulle Wolle, fugol Vogel, bucca Bock, cnucian stoßen, ufan oben..." ("In some words, especially in the neighborhood of labials, instead of the expected o, a u appears..."). His examples align with the pattern but provide no formal conditioning.
141: 
142: **Phonetic note:** Labial consonants share the [+round] feature with /u/. This articulatory compatibility may have created a phonetically favorable context for preserving the high back rounded vowel. However, as Bülbring and Luick both concede, this cannot be formalized as a categorical rule given the counterexamples.
143: 
144: ### Expert consultation: Stefan Schuhmacher (Vienna, 2026-03-20)
```

#### Germanic/docs/DEV_NOTES.md:160 (concept name)

- Nearby heading: ### Expert consultation: Stefan Schuhmacher (Vienna, 2026-03-20)

```text
158: inflected as an n-stem, viz. \*bukō, gen. \*bukkaz < \*bhug-ōn, \*bhug-n-ós."
159: The gemination reflects Kluge's Law in the n-stem genitive. Kluge-Seebold
160: confirms OE had both bucca (n-stem) and bucc (a-stem). Whether there was ever
161: a u-stem variant remains unverified. See notable_findings.md §2 for details.
162: 
```

#### Germanic/docs/DEV_NOTES.md:236 (concept name)

- Nearby heading: ### OE Medial unstressed `*u → *o`: Conditioning environment (2026-03-20)

```text
234: 
235: 2. **Words where medial `*u` should remain:**
236:    - `*widuwōn` → `widuwe` (R/T, Campbell §218-219: both `widuwe` and `wuduwe` attested)
237: 
238: **Extensive research (2026-03-20):**
```

#### Germanic/docs/DEV_NOTES.md:1578 (exact PROTOFORM)

- Nearby heading: ## Consonant Mismatch Bucket Refinement (2026-02-07)

```text
1576:    - Examples: `*bebruz → beber` (expected `befer`), `*drībăną → drīban` (expected `drīfan`)
1577: 4. **prefix_morphology_issue: 1** - Missing derivational prefix
1578:    - Example: `*bō → bō` (expected `bā]] [[þā`)
1579: 5. **consonant_mismatch_other: 27** - Remaining genuine consonant substitutions needing investigation
1580: 
```

#### Germanic/docs/DEV_NOTES.md:37222 (row ID)

- Nearby heading: ## §17.30 — *bō ('both') row 1958: target was Wiktionary garbage; OE has no clean reflex

```text
37220: 5. Commit + push.
37221: 
37222: ## §17.30 — *bō ('both') row 1958: target was Wiktionary garbage; OE has no clean reflex
37223: 
37224: ### .1 Research dossier (OE 'both': `bēġen / bā / bū`)
```

#### Germanic/docs/DEV_NOTES.md:37224 (exact COUNTERPART)

- Nearby heading: ### .1 Research dossier (OE 'both': `bēġen / bā / bū`)

```text
37222: ## §17.30 — *bō ('both') row 1958: target was Wiktionary garbage; OE has no clean reflex
37223: 
37224: ### .1 Research dossier (OE 'both': `bēġen / bā / bū`)
37225: 
37226: Compiled with Opus subagent across `docs/references/` (line numbers are
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:20 (concept name)

- Nearby heading: ## 1. Executive summary

```text
19: 
20:    i.e. the set of consonants admitted between the fronted *æ* and a triggering back vowel **excludes both *r* and *l*** (`germanic.txt` lines 1806–1808). A Kleene star (`[OEARestorationIntervening]*`) wraps this set in the actual replacement rule (line 1817).
21: 
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:54 (concept name)

- Nearby heading: ## 1. Executive summary

```text
53: 
54:    together with a one-line change to the rule body so the cluster description is matched exactly once (no Kleene star), or — equivalently — by adding a hard upper bound. Either of two minimal edits achieves the same surface result; both are detailed in §10.
55: 
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:95 (concept name)

- Nearby heading: ### 2.1 Campbell, *Old English Grammar* (1959) — file `campbell_old_english_grammar.txt`

```text
94: 
95: §764 (lines 23258–23262) — `sparian` in fact attested with both class II and class III variants, and the front-vowel `spær-` forms are precisely the ones expected when no back vowel follows:
96: 
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:122 (concept name)

- Nearby heading: ### Case 4: *tángō (tongs) — tang (lautgesetzlich Anglian) vs. tange (analogical late)

```text
121: | **Implementation** | TSV now targets `tang` (nom.sg., early Anglian). The FST output matches. |
122: | **Note** | This case is the **mirror image** of §17.16: in §17.16 (*spere*), the simplex nominative is lautgesetzlich and the plural/compound show back umlaut; in §17.20 (*tang*), the simplex nominative is lautgesetzlich and later forms show analogical restoration. Both demonstrate that paradigm-cell targeting (choosing oblique/plural/early forms) is methodologically sound. |
123: 
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:135 (concept name)

- Nearby heading: ### Case 5: *nábulō (navel) — nafola / nafela

```text
134: | **Lautgesetzlich output** | `nafola` (preserves the medial *u → *o stage; nom.sg. of strong n-stem shows medial-vowel preservation per §17.19) |
135: | **Attested simplex** | `nafela` (late WS majority, showing both vowel-harmony stages: *u → *o → *e*); `nafola` (early/rare, preserves intermediate stage) |
136: | **DEV_NOTES reference** | §17.19 (PROTOFORM choice *nablô* vs *nabulō*); lines c. 10800–11700 |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:137 (concept name)

- Nearby heading: ### Case 5: *nábulō (navel) — nafola / nafela

```text
136: | **DEV_NOTES reference** | §17.19 (PROTOFORM choice *nablô* vs *nabulō*); lines c. 10800–11700 |
137: | **Attestation status** | **Both forms attested in OE: `nafola` earlier/rarer, `nafela` later/majority in WS.** The choice represents two stages of vowel harmony, not two different proto-forms. |
138: | **Classification** | Unlike *meord*, *spere*, *tangle*, this case involves **oblique paradigm cells**: the oblique forms of the n-stem all show *a (e.g., *nafolan*), which preserves the *u of the root indirectly. The nominative singular `nafola` vs. `nafela` represents two diachronic stages of vowel harmony within OE, not a pre-OE phenomenon. |
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:19 (concept name)

- Nearby heading: ## Kroonen's reconstruction (*kō- ~ *ku-)

```text
18: >
19: > A root noun continuing the common IE word for 'cow'. Germanic has two different root variants, i.e. *kō- and *kū-, both of which belonged to an originally ablauting paradigm **nom. *kōz, obl. *kū-**, continuing a PIE u-stem *gʷéh₃-u-s, obl. *gʷh₃-u-.
20: 
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:24 (concept name)

- Nearby heading: ## Kroonen's reconstruction (*kō- ~ *ku-)

```text
23: - Zero-grade stem: *kū- (oblique cases)
24: - Both are PIE-inherited ablaut grades, not analogical innovations
25: 
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:111 (concept name)

- Nearby heading: ### Option B: PGmc dat.sg. *kūi → OE cȳ

```text
110: - **Pipeline**: `kūi → cȳe` ✗ (has extra -e)
111: - **Pro**: Clearly lautgesetzlich per R/T §6.6.1. Both proto and OE are oblique forms. Satisfies the user's requirement of "oblique PGmc form + oblique OE form."
112: - **Con**: Pipeline produces wrong output (cȳe not cȳ). Would need a pipeline fix for vowel-hiatus contraction, OR we accept the mismatch.
```

#### Germanic/docs/analysis/dill_stem_class_investigation.md:17 (concept name)

- Nearby heading: ## Kroonen's reconstruction (*deli- ~ *delja-)

```text
16: >
17: > The material offers evidence for both an i-stem (OE dile) and a ja-stem (OS dilli, OHG tilli). Perhaps the forms with rounded vowels (OE dyle, MHG tülle) can be adduced to reconstruct an additional ablauting pair *duli- ~ *dulja-. If so, the original paradigm probably had ablaut of the root, viz. nom. *deliz, gen. *duljaz < *dhél-i-s, *dhl̥-i-ós.
18: 
```

#### Germanic/docs/analysis/final_vowel_missing_analysis.md:93 (concept name)

- Nearby heading: ### Option 3: Update TSV to Use Consistent Citation Forms

```text
92: ### Option 3: Update TSV to Use Consistent Citation Forms
93: Ensure both proto and OE forms use same morphological base (e.g., both nom.sg., or both stems):
94: - If proto is nom.sg inflected, OE should be nom.sg
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:6 (concept name)

- Nearby heading: ## Overview

```text
5: Four TSV items remain in the "complex TSV fix" category. Each has problems with
6: the proto-form, the OE target, or both, and each would require pipeline changes
7: to resolve fully. This document analyzes each item in detail.
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:196 (concept name)

- Nearby heading: ### Verdict: PARTIALLY FIXABLE

```text
195: Fixing the proto to `*furxtiz` would be correct. The target `fyrhtu`/`fryhtu`
196: requires both r-metathesis (a real sound change we don't model) and analogical
197: -u (morphological, not phonological). The closest the pipeline can get is `fyrht`.
```

#### Germanic/docs/analysis/fryhtu_investigation.md:48 (concept name)

- Nearby heading: ### The \*iþō-abstract analysis

```text
47: 3. **Unstressed ō-shortening**: \*fyrhþō → \*fyrhþu (\*ō → u in final unstressed)
48: 4. **Cluster simplification**: \*fyrhþu → fyrhtu (or fyrhþu — both spellings attested)
49: 
```

#### Germanic/docs/analysis/fryhtu_investigation.md:50 (concept name)

- Nearby heading: ### The \*iþō-abstract analysis

```text
49: 
50: Under this analysis, **both the umlaut and the -u ending are lautgesetzlich**:
51: - Umlaut comes from the derivational \*-i- in \*-iþō-
```

#### Germanic/docs/analysis/fryhtu_investigation.md:66 (concept name)

- Nearby heading: ### Verdict

```text
65: Proto should be **\*furhtiþō** (PGmc \*iþō-abstract nom.sg.). This is the form
66: that regularly produces OE fyrhtu with both umlaut and the -u ending.
67: 
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:91 (concept name)

- Nearby heading: ### 2.1 Streitberg, *Urgermanische Grammatik* (1896)

```text
90: 
91: **Position.** Streitberg already in 1896 has **both pathways on the
92: table**. The ē of *mēd* is from compensatory lengthening following loss
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:159 (concept name)

- Nearby heading: ### 2.5 Luick, *Historische Grammatik der englischen Sprache* (1914–1940)

```text
158: 
159: **Position.** Luick has **both forms but two distinct accounts**:
160: *mēd* = ē² (the narrow ē whose PGmc source he treats elsewhere as
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:175 (concept name)

- Nearby heading: ### 2.6 Hirt, *Urgermanisch* I (1931–1934), p. 33

```text
174: This is the **PGmc-level doublet hypothesis**: \*mizdō and \*mēdō are
175: both inherited from Proto-Germanic, the latter with compensatory
176: lengthening of \*ē² already in PGmc, before the WGmc/dialectal
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:228 (concept name)

- Nearby heading: ### 3.4 The vowel alternation problem: *i vs. *e in the root

```text
227: 
228: Campbell's footnote for *leornian* notes that OHG has both *lernen* (e-grade) and *lirnen* (i-grade), and OFris. has *lernia* ~ *lirnia*. This **e/i variation** is present in the Germanic languages.
229: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:51 (concept name)

- Nearby heading: ## 1. Charge of this supplement

```text
50: 
51: 3. **Parallel with \*rēc** (notable_findings.md #10): OE *rēc* 'smoke' shows universal long ē across all dialects where we expect WS diphthong *īe (from *au + i-umlaut). Both *rēc* and *mēd* avoid expected diphthongs. Is there a systematic development *VzC → VːC* that yields ē regularly, making *meord* the marked form rather than *mēd*?
52: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:158 (concept name)

- Nearby heading: ### 3.1 Orel (2003), *A Handbook of Germanic Etymology*

```text
157: The entry appears on p. 272 under Germanic cognates. Orel lists:
158: - **OE forms**: both **meord** and **méd**
159: - **Meaning**: 'reward, pay'
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:162 (concept name)

- Nearby heading: ### 3.1 Orel (2003), *A Handbook of Germanic Etymology*

```text
161: 
162: **Orel's treatment**: He **lists meord as an OE form** alongside méd, implying both existed. However, Orel does **not provide textual citations** or discuss the relationship between the two forms (i.e., whether *meord* is attested, dialectal, or reconstructed).
163: 
```

#### Germanic/docs/analysis/notable_findings.md:84 (concept name)

- Nearby heading: ## 1. Medial high-vowel syncope: dental-obstruent conditioning

```text
83: - **R/T (vol.2 §6.7.3, pp.264-270):** "High *i and *u were lost only if the
84:   preceding syllable was both heavy and stressed." Give the most detailed
85:   treatment. Note a complication with CR-clusters (p.269): "if a CR-cluster
```

#### Germanic/docs/analysis/notable_findings.md:157 (concept name)

- Nearby heading: ## 1. Medial high-vowel syncope: dental-obstruent conditioning

```text
156: exemplification. Their main rule: "high *i and *u were lost only if the
157: preceding syllable was both heavy and stressed." They then note a
158: significant complication with CR-clusters (p.269): "if a CR-cluster in a
```

#### Germanic/docs/analysis/notable_findings.md:215 (concept name)

- Nearby heading: ## 1. Medial high-vowel syncope: dental-obstruent conditioning

```text
214: 
215: Both analyses predict our observed pattern but also predict cases where
216: our rule is too restrictive (blocking syncope before, say, *s* in *hīehsta*)
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:64 (concept name)

- Nearby heading: ### For \*sumaraz and \*xamaras

```text
63:    root (sum-, ham-) could cause partial velarization of the medial vowel
64: 3. Both `sumer` and `sumor` are **attested** (Kroonen: "OE sumer, sumor m.")
65: 4. Both `hamor` and `hamer` are **attested** (Wiktionary: "OE hamor, hamer, homer")
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:65 (concept name)

- Nearby heading: ### For \*sumaraz and \*xamaras

```text
64: 3. Both `sumer` and `sumor` are **attested** (Kroonen: "OE sumer, sumor m.")
65: 4. Both `hamor` and `hamer` are **attested** (Wiktionary: "OE hamor, hamer, homer")
66: 5. Hall's dictionary gives gen.sg. **sumeres** (with -e-), confirming -e- in oblique forms
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:149 (concept name)

- Nearby heading: ### 1. \*sumerăz/sumor → fix proto AND target

```text
148: **Target correction**: sumor → sumer. The regular neogrammarian outcome is
149: "sumer" (via \*a → \*æ by a-fronting → e by unstressed æ/i merger). Both forms
150: are attested (Kroonen: "OE sumer, sumor m."; Hall's: gen.sg. "sumeres").
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:367 (concept name)

- Nearby heading: ### Campbell §210 — concrete dialect contrast

```text
366: consonants; a-umlaut is mostly absent (`fela, helan, beran, nefa, sefa,
367: weras, wela`). In Anglian (l. 6337): "both u- and a-umlaut of e are general
368: before all consonants except c and g."
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:522 (concept name)

- Nearby heading: ### Campbell §164–169

```text
521: 
522: So: VP shows both halves (`æ > e` and `a > æ`); Ep./Cp./RG/St. Chad show
523: only the first half robustly; Ru.¹ shows neither.
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:558 (concept name)

- Nearby heading: ### Texts showing second fronting

```text
557: 
558: - **Vespasian Psalter (VP)** — both halves, robustly
559: - **Royal Glosses (RG)** and **St. Chad** — first half (æ > e) frequent
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:13 (concept name)

- Nearby heading: ## §1. Question

```text
12: 
13: Both rows were retargeted from the infinitive (`*beuganą / būgan`,
14: `*skeubaną / sċūfan`) to the 3 pl. pret. in the same session that
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:35 (concept name)

- Nearby heading: ## §1. Question

```text
34: to target**, and whether some other cell of the same paradigm would
35: be both Lautgesetzlich and attested for *būgan* and *sċūfan*
36: respectively. The question was prompted by the user's request:
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:104 (concept name)

- Nearby heading: ## §2. Reconstruction of the original choice (checkpoints 064–065)

```text
103: 
104: 1. **Both the past pl. (`-un`) and the past ptcp. (`-anaz`) cells
105:    were already known to map regularly to attested OE forms in
```

#### Germanic/docs/dossiers/bugun-scufun-attestation.md:222 (concept name)

- Nearby heading: ## Synthesis

```text
221: 
222: Both `bugun` and `sċufun` are **structurally well-formed**: they are
223: the forms one would expect a Class-II strong verb pret. pl. to take
```

#### Germanic/docs/dossiers/bugun-scufun-attestation.md:229 (concept name)

- Nearby heading: ## Synthesis

```text
228: etc.). They are *not*, however, **directly attested as such in the
229: surviving corpus**. Both verbs appear in 3 pl. pret. only in late-WS
230: or West-Saxon-leaning manuscripts (Chronicle 10–11c. annals, Ælfric,
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:325 (concept name)

- Nearby heading: ## 3. The conditioning, abstracted

```text
324: #" + "front V _ frontV") is rows 7 and 9 together (preconsonantal AND final
325: both palatalise) — actually it's **row 7** specifically: their proposal
326: captures rows 4 and 9 but loses row 7 (*nægl, segl, regn, wegn, sægde, bregdan*).
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:365 (concept name)

- Nearby heading: ## 5. The single-ġ / geminate-ċġ split, and dialect notes

```text
364:   *singe*. Campbell §430 quoted above is explicit on this.
365: - The current foma rule conflates both as `{*ʤ}`. Inspection of the TSV (e.g.
366:   `*wégaz → ʋeɪ`) shows that downstream rules (`SilentCleanup`, `Surface`,
```

#### Germanic/docs/dossiers/un-to-on-chronology.md:180 (concept name)

- Nearby heading: ### Luick §326

```text
179: 
180: 1. Luick lists `ridon`, `wǣron` — both pret.pl. forms — as exemplars
181:    of the WS inlaut `*u > o` lowering. So the lowering of `*-un >
```

#### Germanic/docs/dossiers/un-to-on-chronology.md:433 (concept name)

- Nearby heading: ## Implications for FST design

```text
432:   handbooks; or (b) drop the stem-`u` harmony block and re-break
433:   `wuduwe`, `munuc`, `duguð`. Both options are wrong.
434: 
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:96 (concept name)

- Nearby heading: #### §365 — parasite vowel `-uw-` lowers

```text
95: sequence undergoes the very `*u → *o` lowering of §373, with the
96: canonical examples `beadowe`, `swalewan` — both with `*w` as the
97: right-context consonant.
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:187 (concept name)

- Nearby heading: #### p. 270 — `widuwe` listed under "i, u, y not syncopated"

```text
186: medial `*u` is preserved by Lautgesetz or by analogy; they simply
187: list both outcomes.
188: 
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:306 (concept name)

- Nearby heading: ### 3.2. The analogical / paradigm-uniformity hypothesis

```text
305: * WS inherits the unsyncopated form `wuduwe`.
306: * Late WS, in contact with both forms, produces a hybrid: the root
307:   `i` of `widwe` is restored alongside the `-uwe` of `wuduwe`,
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | author + year mention (Kroonen 2013) |
| Campbell1959 | single available key for Campbell |
| SieversBrunner1965 | single available key for Sievers |
| Fulk2018 | single available key for Fulk |
| Orel2003 | single available key for Orel |
| Seebold1970 | single available key for Seebold |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Ringe2006 | surname mention only: Ringe |
| Ringe2017 | surname mention only: Ringe |
| RingeTaylor2014 | surname mention only: Ringe |
| Ringe1984 | surname mention only: Ringe |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |

