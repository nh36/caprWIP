# Evidence packet — 2041 give / ġiefan

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2041 | give | ġiefan | *gébaną | *gébaną | regular | WS palatalized initial (R/T §6.4.1 rule 1: g before front vowel) | TSV: giefan → ġiefan; |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# give
PROTO: *gébaną
EXPECTED: ġiefan
OUTPUTS: ġiefan



### Proto-Germanic consonant inheritance

Proto Input: *gébaną

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>OE Heavy Syllable Nasal Apocope: *géban<br>OE Secondary Nasalization: *gébąn<br>PGmc B Allophony: *géβąn<br>OE Velar Palatalization: *ʤéβąn<br>OE Ws Palatal Diphthongization: *ʤíeβąn<br>OE Weak Tail Reduction: *ʤíeβan |



### Orthography & surface

Old English Orthography: ġ*íeβan
Outcome: ġiefan

NOTE: WS palatalized initial (R/T §6.4.1 rule 1: g before front vowel)
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

_None_

### Analysis and dossier hits

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:440 (exact COUNTERPART)

- Nearby heading: ### Campbell §170 ff., §253

```text
439: 
440: Campbell §253 examples (ll. 7621–7623, and §170 ff.): WS `ġiefan, ġiest,
441: ġearu, sceal, sceaft, scieran, sċieppan` from earlier `*gefan, *gæst,
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:455 (exact COUNTERPART)

- Nearby heading: ### Ringe & Taylor §6.5.1 (repo ll. 12450–12541)

```text
454: |---|---|---|
455: | `*geban-` | `ġiefan` | Merc. `for-ġeofan` (with BM); North. `ġeafa` |
456: | `*geldan-` | `ġieldan` | Merc. `geldan`; North. `gelda` |
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:626 (exact COUNTERPART)

- Nearby heading: ## 8. The WS digraph `ie` (later WS `y, i`) ~ Anglian `e`

```text
625: This is essentially a corollary of §§5 and 7: WS `ie/íe` arises both from
626: PD (`ġiefan, sceaft`) and from i-umlaut of `ea, éa, io, ío` and of the
627: diphthong from PD (`ċiese`). Anglian lacks PD altogether and has plain
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| give | giefan | der | template:der | give |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:314 (concept name)

- Nearby heading: # Block if stressed syllable (first syllable) contains *u

```text
312: - `*xéβun` (accented `*e`): `*u → *o` → `heofon` ✓
313: - `*wúduwōn` (accented `*u`): `*u` preserved → `wuduwe` ✓
314: - `*wíduwōn` (accented `*i`): should give `*u → *o`? But OE has `widuwe`...
315: 
316: **Comprehensive research on OE widow forms (2026-03-21):**
```

#### Germanic/docs/DEV_NOTES.md:966 (concept name)

- Nearby heading: ### Why u-lowering doesn't apply

```text
964: 
965: - `*durą` (a-stem) → regular u-lowering → *dor* ✓ (correctly modeled)
966: - `*durō` (ō-stem) → would give *doru* (u-lowering applies)
967: - `*duruz` (u-stem) → no u-lowering → *duru* ✓
968: 
```

#### Germanic/docs/DEV_NOTES.md:1234 (concept name)

- Nearby heading: ### What other sources say (for completeness)

```text
1232: **Campbell (1959), §§419-420:** Discusses WS `*p > t` before nasals vs. Anglian preservation of `*p` — this is a separate, later sound change, not the PGmc paradigmatic alternation.
1233: 
1234: **Fulk (2018), Ringe/Taylor (2014):** Give basic etymology without the paradigmatic analysis.
1235: 
1236: ### FST implementation
```

#### Germanic/docs/DEV_NOTES.md:2308 (concept name)

- Nearby heading: ### KIT sweep (status: reverted to baseline)

```text
2306: ### KIT sweep (status: reverted to baseline)
2307: 
2308: - Replayed the dockered `flookup` harness (`python3 - <<'PY' …`) to isolate the true KIT cases (filtering out `aɪ/eɪ/ɔɪ`). We still have 35 `{ɪ}` forms headed by `fish/give/six/will` plus the `{ɪə}`+`r` items (`beard/bier/deer/spear/year`).
2309: - Restored the brace-aware helper sets (`EnglishSandboxPlainVocalic/Liquid/Nasal`), the `{*u}` contexts, and `EnglishSandboxPostVocalicRLoss` after rolling back an experimental smoothing stage that tanked the harness. `english_brace_sandbox.bin` is back to the 179/376 success baseline.
2310: - `python3 server/tools/api_regression.py` remains green, so the sandbox is stable again for the next round of KIT work (detailed smoothing + consonant-cluster contexts).
```

#### Germanic/docs/DEV_NOTES.md:2322 (concept name)

- Nearby heading: ### KIT sweep (WIP)

```text
2320: ### KIT sweep (WIP)
2321: 
2322: - Fed the KIT bucket through the same dockered `flookup` harness (`python3 - <<'PY' …`) after filtering out diphthongs (`aɪ/eɪ/ɔɪ`). The remaining 35 entries are the genuine `{ɪ}` cases headed by `fish/give/six/will` alongside the `{ɪə}` + post-vocalic /r/ cohort (`beard/bier/deer/spear/ year`, etc.).
2323: - Updated `EnglishSandboxCoreVowelRules` so short `{*i}` finally drops its star and enters the plain alphabet, and extended `EnglishSandboxShortVowelSplit` with `{i}`→`{ɪ}` rewrites in closed syllables / word-final contexts. This keeps the KIT conditioning in the same stage as the `{*e}`/{`*u`} splits instead of leaving `{*i}` untouched.
2324: - The attested-form harness still lands at 179/376 successes (KIT bucket = 35) because the stubborn cases need post-vocalic /r/ smoothing (`{ɪ}`→`{ɪə}` before the new `EnglishSandboxPostVocalicRLoss`) or suffixal analogies (`sieve/singe/timber`). Logged them here so the next pass can target `{ɪə}` outputs without sacrificing the `{bəʊn}/{fʊt}` improvements we just landed.
```

#### Germanic/docs/DEV_NOTES.md:2979 (concept name)

- Nearby heading: #### B. Stressed vowel ie vs eo (*liznô → lierna vs leorna)

```text
2977: **Affected:** *liznô → lierna (expected leorna), *liznōjăną → lierneian (expected leornian)
2978: 
2979: **Issue:** The root *lizn- should give OE leorn- (with eo from breaking of e before rn). Our FST produces ie instead of eo. This is a stressed vowel quality issue in the `vowel_quality__stressed_vowel` bucket. Needs investigation: the *i → *e lowering and then breaking to *eo should give eo, not ie.
2980: 
2981: #### C. Spurious palatalization of geminate *kk (*likkô → liċca vs licca)
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:234 (concept name)

- Nearby heading: ### 2.7 Kaluza, *Historische Grammatik des Englischen* — file `kaluza_historische_grammatik_englisch.txt`

```text
233: 
234: Kaluza confirms the standard "open syllable, dark vowel in the next syllable" formulation; the local file does not give an *r*/*l*-specific carve-out.
235: 
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:691 (concept name)

- Nearby heading: ### 10.4 Predicted effects of the recommended change (option B) on the six probed inputs

```text
690: 
691: All six probes give the desired output under the recommended change. (Verification by manual trace; not yet compiled because the task brief explicitly forbids modifying `germanic.txt`.)
692: 
```

#### Germanic/docs/analysis/dill_stem_class_investigation.md:25 (concept name)

- Nearby heading: ## The linguistic problem

```text
24: |----------|------|-----------|----------|
25: | OE | dile | i-stem *deliz | No gemination (WGmc *j-gemination would give **dille*) |
26: | OS | dilli | ja-stem *deljaz | Gemination before *j |
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:35 (concept name)

- Nearby heading: ### OE target assessment

```text
34: 
35: The TSV has `hlæhhan`. R/T give the WS form as **hliehhan** (lines 3674, 10264,
36: 13896, 19594) and the Anglian poetic form as **hlehhan** (line 13897). The form
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:51 (concept name)

- Nearby heading: ### OE target assessment

```text
50: "R/T: PGmc *hlahjanan > OE hlæhhan/hliehhan" — this appears to be inaccurate;
51: R/T do NOT give hlæhhan as a standard form.
52: 
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:105 (concept name)

- Nearby heading: ### Proto-form assessment

```text
104: The proto `*skellinăz` does not match Kroonen's reconstruction. The \*e in
105: \*skellinăz would give OE \*sċiellen (via i-umlaut and palatalization), but the
106: attested form is sċilling with *i.
```

#### Germanic/docs/analysis/fryhtu_investigation.md:27 (concept name)

- Nearby heading: ### R/T's analysis

```text
26: R/T (line 21553) treat OE fyrhtu as an **ī-stem abstract noun**. The i-umlaut
27: (\*u → y) proves an \*i-containing source, since the ō-stem \*furhtō- would give
28: OE \*forhte without umlaut.
```

#### Germanic/docs/analysis/fryhtu_investigation.md:169 (concept name)

- Nearby heading: ### The standard accounts

```text
168: 
169: R/T give extensive examples. Crucially, they note a complication with
170: CR-clusters (p.269): "if a CR-cluster in a weak class I verb is preceded by a
```

#### Germanic/docs/analysis/fryhtu_investigation.md:177 (concept name)

- Nearby heading: ### The standard accounts

```text
176: 
177: R/T also give the \*-iþu- abstract derivation explicitly (p.56, discussing
178: PWGmc survival of final vowels): "\*strangiþu > \*strængiþu > \*strengþu >
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:541 (concept name)

- Nearby heading: ### 2.17 Kilday, "Crist's Law, Smith's Law, and English *wizen*" (2024 draft)

```text
540: 
541: This is also the first source in the chronological survey to give
542: weight to the **WS/Mercian vs. Northumbrian** distribution: he reports
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:943 (concept name)

- Nearby heading: ## 7. Sources I wished I had

```text
942: 
943: 6. **DOE (Toronto Dictionary of Old English)**. The DOE would give
944:    the canonical and complete attestation count for *meord*/*meorde*
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:402 (concept name)

- Nearby heading: ### H1: Target switch to Anglian/Northumbrian form

```text
401: - FST output: `meord` (with breaking diphthong *eo)
402: - Anglian smoothing (Campbell §§255–256) would give: `*merd` (short *e)
403: - Attested Anglian: **no simplex attestation found**
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:486 (concept name)

- Nearby heading: ### H6: Genuine analogical exception

```text
485: **Test**: What could be the source of analogy?
486: - **Oblique stem generalization**: If oblique forms (gen./dat. *mēde*) were regularized early (by analogy with other ō-stems), and then the nom.sg. was remade from the oblique stem, this could give *mēd* without breaking
487: - **Noun-class shift**: If *mēd* was reanalyzed as belonging to a different stem class (e.g., from ō-stem to i-stem), this could have triggered paradigm leveling
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:643 (concept name)

- Nearby heading: ### Option 5: Proto-form switch to hypothetical `*mezdō` (e-grade)

```text
642: - **Change PROTOFORM** from `*mízdō` to `*mézdō` (hypothetical e-grade)
643: - This would give: `*mezdō` → `*merdō` → `*meordō` → `meord` (same FST output)
644: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:292 (concept name)

- Nearby heading: #### Page 285 (in section on *z-loss and compensatory lengthening):

```text
291: 
292: **Possible interpretation**: R/T may be hinting that *\*mizd- → *\*mīd- (with z-loss and compensatory lengthening, **bypassing rhotacism**) → *mēd- (with i-lowering to e). This would give *méd* directly, without breaking.
293: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:596 (concept name)

- Nearby heading: ### 6.1 Original dossier hypotheses revisited

```text
595:    - **Kroonen**: Lists both *meord* and *méd* but doesn't explain the alternation. His footnote (per web search) suggests breaking "does not take place" because *i precedes a single dental—this **contradicts** Campbell and implies *méd* is regular, *meord* is not.
596:    - **R/T**: List both forms with tilde but don't explain. Their discussion of z-loss + compensatory lengthening (p. 285) hints at an alternative pathway (*zd → *d with lengthening) that would give *mēd* directly.
597: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:764 (concept name)

- Nearby heading: ### 7.3 Recommended TSV/FST action

```text
763: - Followed by: `{*ī}{*d} → {*ē}{*d}` (i-lowering after lengthening)
764: - This would give: `*mizdō` → `*mīdō` → `*mēdō` → `mēd` ✓
765: 
```

#### Germanic/docs/analysis/notable_findings.md:84 (concept name)

- Nearby heading: ## 1. Medial high-vowel syncope: dental-obstruent conditioning

```text
83: - **R/T (vol.2 §6.7.3, pp.264-270):** "High *i and *u were lost only if the
84:   preceding syllable was both heavy and stressed." Give the most detailed
85:   treatment. Note a complication with CR-clusters (p.269): "if a CR-cluster
```

#### Germanic/docs/analysis/notable_findings.md:112 (concept name)

- Nearby heading: ## 1. Medial high-vowel syncope: dental-obstruent conditioning

```text
111: The scholarly treatments of medial syncope differ in how much attention
112: they give to the consonantal environment of the syncopated vowel. The
113: older scholarship (Kaluza, Luick) formulates the rule almost entirely in
```

#### Germanic/docs/analysis/notable_findings.md:606 (concept name)

- Nearby heading: ## 3. PWGmc \*j-related sound changes: formalization of under-specified rules

```text
605: affected after short syllables." His examples: "many weak verbs of Class I,
606: as sellan give, fremman do, þennan stretch, clyppan embrace, settan set,
607: cnyssan knock, wecċan awake; nouns and adjs. of the ja-, jō-, and jan-/jōn-
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:292 (concept name)

- Nearby heading: ### 2.8 Sources NOT consulted in detail (named but not used as authority here)

```text
291:   did not have a verifiable copy and so I have **deliberately not cited
292:   her**, despite earlier search results that purported to give her wording
293:   (those were LLM confabulations).
```

#### Germanic/docs/dossiers/un-to-on-chronology.md:371 (concept name)

- Nearby heading: ## Verdict

```text
370:   final syllables (`-un#`), is a WS Lautgesetz operative from the
371:   early 9th century. Brunner §44 Anm. 7 and Luick §326.2 give the
372:   rule: lowering applies in inlaut before any single C except `m`,
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Campbell1959 | single available key for Campbell |

### Low-confidence candidates

_None_

