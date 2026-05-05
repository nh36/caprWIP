# Evidence packet — 2004 fast / festan

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2004 | fast | festan | *fastēną | *fástijaną | early_analogy | R/T: "festan 'to fix, to fasten' < *fæstjan" (Class I weak); "acquired stative meaning ['to fast'] by lexical confusion" with *fastēn-. OE fæstan has æ from analogy with adj. fæst. | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# fast
PROTO: *fástijaną
EXPECTED: festan
OUTPUTS: festan



### Proto-Germanic consonant inheritance

Proto Input: *fástijaną

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *fæstijaną<br>OE Heavy Syllable Nasal Apocope: *fæstijan<br>OE Secondary Nasalization: *fæstijąn<br>Sievers Law Syncope: *fæstjąn<br>OE I Umlaut: *festjąn<br>OE Weak Tail Reduction: *festjan<br>OE J Loss After Heavy: *festan |



### Orthography & surface

Outcome: festan

NOTE: R/T: "festan 'to fix, to fasten' < *fæstjan" (Class I weak); "acquired stative meaning ['to fast'] by lexical confusion" with *fastēn-. OE fæstan has æ from analogy with adj. fæst.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:3870 (row ID)

- Nearby heading: ### The problem

```text
3868: | ID | Proto | Pipeline output | Expected | OE class |
3869: |----|-------|----------------|----------|----------|
3870: | 2004 | \*fastēną | faston | fastian | II (-ian) |
3871: | 2027 | \*fulgēną | folgon | folgian | II (-ian) |
3872: | 2107 | \*libēną | leofon | lifian | II (-ian) |
```

#### Germanic/docs/DEV_NOTES.md:3968 (row ID)

- Nearby heading: ### The individual verbs

```text
3966: The TSV proto \*wakēną was wrong — corrected to \*wakaną. Now matches. (See mismatch trajectory.)
3967: 
3968: **fastian (ID 2004)**: Denominal from \*fastu- 'firm'. Kroonen \*fastēn- → OE fastian.
3969: 
3970: *Research findings (2026-03-09):*
```

#### Germanic/docs/DEV_NOTES.md:4474 (row ID)

- Nearby heading: ### Part 2: fastian (Row 2004)

```text
4472: ---
4473: 
4474: ### Part 2: fastian (Row 2004)
4475: 
4476: #### Step 1: Proto-Germanic infinitive in the literature
```

#### Germanic/docs/DEV_NOTES.md:4587 (row ID)

- Nearby heading: #### Step 5: Summary and recommendations

```text
4585: 4. Update TSV with corrected PROTOFORM and COUNTERPART
4586: 
4587: **For now, leaving row 2004 as a documented mismatch** pending:
4588: - Confirmation of correct OE counterpart
4589: - Fix for i-umlaut \*a → æ bug
```

#### Germanic/docs/DEV_NOTES.md:4611 (row ID)

- Nearby heading: ### Implementation (2026-03-09f continued)

```text
4609: - Current: 291 matches / 88 mismatches (75.4% match rate)
4610: 
4611: **Remaining: fastian (row 2004)**
4612: 
4613: Need to investigate the i-umlaut issue with `*fastjăną → festan` (should be fæstan).
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:3974 (exact COUNTERPART)

- Nearby heading: ### The individual verbs

```text
3972:   festia, OHG festen, all 'make firm') that has acquired the stative meaning by lexical confusion"
3973: - This suggests the actual OE verb 'to fast' is **fǣstan** < **\*fastjăną** (Class I), not fastian
3974: - Pipeline test: \*fastjăną → festan (close to fǣstan), \*fastēną → faston (not attested)
3975: - Pipeline test: \*fastēþi → fæsteþ (3sg present) — but no evidence this is an archaic relic
3976: - **Issue:** TSV target "fastian" may be incorrect; standard OE is "fǣstan" from Class I \*fastjăną
```

#### Germanic/docs/DEV_NOTES.md:4525 (exact COUNTERPART)

- Nearby heading: #### Step 3: Reassessing the OE attestations

```text
4523: **Test: \*fastjăną → ?**
4524: 
4525: Pipeline result: `fastjăną → festan`
4526: 
4527: Expected: **fæstan** or **fǣstan**
```

#### Germanic/docs/DEV_NOTES.md:4529 (exact COUNTERPART)

- Nearby heading: #### Step 3: Reassessing the OE attestations

```text
4527: Expected: **fæstan** or **fǣstan**
4528: 
4529: **Analysis:** The pipeline produces festan (with <e>), not fæstan (with <æ>). This is wrong.
4530: 
4531: Wait — \*a before \*j should become æ through i-umlaut? Let me trace:
```

#### Germanic/docs/DEV_NOTES.md:4536 (exact COUNTERPART)

- Nearby heading: #### Step 3: Reassessing the OE attestations

```text
4534: - Result should be fæstan
4535: 
4536: But pipeline gives festan. This suggests the i-umlaut of \*a → æ is not being applied, or is being overwritten.
4537: 
4538: **Further testing needed:** Check whether \*a → æ i-umlaut is working correctly.
```

#### Germanic/docs/DEV_NOTES.md:4544 (exact COUNTERPART)

- Nearby heading: #### Step 3: Reassessing the OE attestations

```text
4542: Pipeline result: `satjăną → settan` ✓
4543: 
4544: This is correct! \*a → e before \*j (gemination context). So why is \*fastjăną → festan wrong?
4545: 
4546: **Reanalysis:** The issue is that \*satjăną has \*a → e because of the following geminate. In \*fastjăną, the cluster \*stj may behave differently. Let me check:
```

#### Germanic/docs/DEV_NOTES.md:4553 (exact COUNTERPART)

- Nearby heading: #### Step 3: Reassessing the OE attestations

```text
4551: - \*fæstăną → fæstan (apocope)
4552: 
4553: Expected: **fæstan**. Pipeline gives: **festan**.
4554: 
4555: **Bug identified:** I-umlaut of \*a → æ is not applying in \*fastjăną.
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| fast | fæst | inh | template:inh | fast |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:2345 (concept name)

- Nearby heading: ### English gold IPA normalized to RP / non-rhotic baseline

```text
2343: 
2344: - Cleaned every English row in `server/data/germanic-aligned-final.tsv` whose counterpart contains an orthographic `r` but whose surface tokens still ended in a vowel + `r`. Each of the 40 affected entries now drops the trailing `r` (e.g. `adder ædər→ædə`, `fire faɪər→faɪə`, `door dɔːr→dɔː`). Mirrored the same edits into the staged snapshot (`server/pipeline/output/germanic/stage3/germanic-aligned-final.tsv`) so downstream docs stay in sync.
2345: - Added `server/tools/validate_english_rhoticity.py` to guard the policy going forward. The helper scans any TSV for English rows where the tokens end in `…V r` and fails fast; CI/local runs should call `python3 server/tools/validate_english_rhoticity.py` (optionally pointing it at the stage3 export) whenever the gold data changes.
2346: - Reran the validator on both the canonical and stage3 TSVs — both now report “No rhotic entries detected.” Next time the gold file is touched, run the validator before committing so we don’t regress toward GA-style outputs again. Once the analyzer tweaks land, rerun `python3 server/tools/english_apply_down_stats.py` to confirm the RP-aware surfaces align with the updated targets.
2347: 
```

#### Germanic/docs/DEV_NOTES.md:2695 (concept name)

- Nearby heading: ### OE sound-change reference index (2026-02-02)

```text
2693: - **New index file:** `docs/references/oe_sound_change_index.md`
2694:   - Collects frequently reused citations and exact `rg`/`sed` commands for Hogg and Ringe/Taylor.
2695: - **Why:** we keep re-checking the same passages during OE chronology work; this keeps lookups fast and consistent.
2696: 
2697: ## Bimoric vs. Trimoric *ō: Comprehensive Analysis (Session 028)
```

#### Germanic/docs/DEV_NOTES.md:3884 (concept name)

- Nearby heading: ### What Kroonen reconstructs

```text
3882: 
3883: - **\*fastēn-** wv. (under \*fastu- entry, p.131): "Go. fastan, ON fasta, OE fastian, OFri. festia,
3884:   OHG fastēn ww. 'to fast' < \*fastēn-." Denominal from \*fastu- 'firm'.
3885: - **\*fulgēn-** wv. (p.158): "OE fylgan, folgian ww. 'id.', E to follow, OS folgon wv., OHG
3886:   folgēn ww." He also notes: "ON fylgja and OE fylg(e)an continue a formation \*fulgjan-"
```

#### Germanic/docs/DEV_NOTES.md:3971 (concept name)

- Nearby heading: ### The individual verbs

```text
3969: 
3970: *Research findings (2026-03-09):*
3971: - R/T §3.3.2 say OE **fǣstan** 'to fast' is "an originally Class I weak verb (cf. ON festa, OS 
3972:   festia, OHG festen, all 'make firm') that has acquired the stative meaning by lexical confusion"
3973: - This suggests the actual OE verb 'to fast' is **fǣstan** < **\*fastjăną** (Class I), not fastian
```

#### Germanic/docs/DEV_NOTES.md:3973 (concept name)

- Nearby heading: ### The individual verbs

```text
3971: - R/T §3.3.2 say OE **fǣstan** 'to fast' is "an originally Class I weak verb (cf. ON festa, OS 
3972:   festia, OHG festen, all 'make firm') that has acquired the stative meaning by lexical confusion"
3973: - This suggests the actual OE verb 'to fast' is **fǣstan** < **\*fastjăną** (Class I), not fastian
3974: - Pipeline test: \*fastjăną → festan (close to fǣstan), \*fastēną → faston (not attested)
3975: - Pipeline test: \*fastēþi → fæsteþ (3sg present) — but no evidence this is an archaic relic
```

#### Germanic/docs/DEV_NOTES.md:4479 (concept name)

- Nearby heading: #### Step 1: Proto-Germanic infinitive in the literature

```text
4477: 
4478: **Kroonen (EDPG s.v. \*fastēn-):**
4479: - Class III weak \*fastēn- 'to fast, abstain from food'
4480: - OE fæstan, fǣstan
4481: - Derived from adj. \*fastu- 'firm, fast'
```

#### Germanic/docs/DEV_NOTES.md:4625 (row ID)

- Nearby heading: ### fastian resolution (2026-03-09f continued)

```text
4623: 4. OE fæstan has æ from **analogy** with adj. fæst, not from sound change
4624: 
4625: **Row 2004 update:**
4626: - Changed PROTOFORM: `*fastēną` → `*fastjăną`
4627: - Changed COUNTERPART: `fastian` → `festan`
```

### Analysis and dossier hits

#### Germanic/docs/dossiers/un-to-on-chronology.md:164 (concept name)

- Nearby heading: ### Luick §326

```text
163: > ein u der Tonsilbe ist es überhaupt bewahrt worden**: die Schreibung
164: > weist in solchen Fällen fast ständiges u auf. So: me(o)du, sunu,
165: > wudu …
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:1742 (concept name)

- Nearby heading: ### D.1 Open vs. closed syllable conditioning

```text
1741: > ein u der Tonsilbe ist es überhaupt bewahrt worden**: die Schreibung
1742: > weist in solchen Fällen fast ständiges u auf. So: me(o)du, sunu,
1743: > wudu …
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |

