# Evidence packet — 2090 lap / lappa

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2090 | lap | lappa | *lábbaz | *láppô | early_analogy | - | Source: Wiktionary etymology (template:inh) \| Source: Wiktionary etymology (template:inh) |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# lap
PROTO: *láppô
EXPECTED: lappa
OUTPUTS: lappa



### Proto-Germanic consonant inheritance

Proto Input: *láppô

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *læppô<br>OE A Restoration: *lappô<br>OE Unstressed Long Vowel Shortening: *lappa |



### Orthography & surface

Outcome: lappa
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:14200 (row ID)

- Nearby heading: ### Options

```text
14198: **Option A (recommended): Change proto to weak n-stem `*lappō`**
14199: 
14200: Change row 2090 from `*labbăz` to `*lappō` (fem. n-stem nom.sg.).
14201: 
14202: Test: Need to verify FST supports this input.
```

#### Germanic/docs/DEV_NOTES.md:36671 (exact pair)

- Nearby heading: ### §17.25.7 Regression after first build — diagnosis and follow-up fix

```text
36669: | `*fáraną`  | `færan`   | `faran`  | `færan`  | now mismatch (etymologically correct); user deferred to a separate loop |
36670: | `*táppô`   | `tappa`   | `tæppa`  | `tæppa`  | **now matching** (−1 mismatch, but see below — this is wrong-side-of-correct) |
36671: | `*láppô`   | `lappa`   | `læppa`  | `lappa`  | **NEW mismatch** |
36672: | `*márōn`   | `mære`    | `mare`   | `mære`   | **NEW mismatch** |
36673: 
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:10395 (exact COUNTERPART)

- Nearby heading: ## Mismatch Progress Log (2026-03-14)

```text
10393: | 2026-03-19 | 57 | -8 | — | Multiple TSV/FST fixes (huniġ, thistle, etc.) |
10394: | 2026-04-05 | 55 | -2 | — | span fix (feminine ō-stem dat.sg.) |
10395: | 2026-04-06 | 52 | -3 | — | TSV fixes: dile, lappa, cnobba |
10396: | 2026-04-07 | 49 | -3 | 0a649b3 | būgan/sċūfan past 3pl paradigm cells |
10397: | 2026-04-07 | 48 | -1 | b1cc80e | heord fix: was 'hierd' (herdsman ≠ herd) |
```

#### Germanic/docs/DEV_NOTES.md:14165 (exact COUNTERPART)

- Nearby heading: ### Research

```text
14163: 
14164: **Brunner §190, §258:**
14165: Lists `lappa` (with variants `laeppa`, plural `leappan`) as **swm** (schwaches Maskulinum = 
14166: weak masculine n-stem). Notes it alongside other weak nouns like `budda, ebba, frogga`.
14167: 
```

#### Germanic/docs/DEV_NOTES.md:14169 (exact COUNTERPART)

- Nearby heading: ### Research

```text
14167: 
14168: **Campbell §158:**
14169: Cites `lappa` as example of a-restoration before geminate: "lappa skirt" (not `*læppa`).
14170: The base vowel is `a` with i-umlaut giving `æ` in some forms.
14171: 
```

#### Germanic/docs/DEV_NOTES.md:14173 (exact COUNTERPART)

- Nearby heading: ### Research

```text
14171: 
14172: **Kluge-Seebold (s.v. *Lappen*):**
14173: > "Das -pp- erscheint auch außerdeutsch: as. lappa, afr. lappa, ae. lappa (vereinzelt); 
14174: > mit anderem Vokal ae. læppa, anord. leppr."
14175: 
```

#### Germanic/docs/DEV_NOTES.md:14176 (exact COUNTERPART)

- Nearby heading: ### Research

```text
14174: > mit anderem Vokal ae. læppa, anord. leppr."
14175: 
14176: Notes both `lappa` and `læppa` in OE, and `pp` across West Germanic (not `bb`).
14177: 
14178: **Kroonen (s.v. *lofan- ~ *lappan-*):**
```

#### Germanic/docs/DEV_NOTES.md:14193 (exact COUNTERPART)

- Nearby heading: ### Analysis

```text
14191: 2. **Kroonen's reconstruction gives `*lappan-` (n-stem)** as the PGmc form.
14192: 
14193: 3. **For OE, the nom.sg. should be `*lappō` → `lappa`** (with a-restoration), or 
14194:    with umlaut `læppa`.
14195: 
```

#### Germanic/docs/DEV_NOTES.md:36704 (exact PROTOFORM)

- Nearby heading: ### §17.25.7 Regression after first build — diagnosis and follow-up fix

```text
36702: **Bug B — `*ô` is not in `OEARestorationStrongOTail`.**
36703: 
36704: `*ô` (trimoric *ō, n-stem masc nom.sg., e.g. *táppô, *láppô) is
36705: explicitly designed in this grammar to *trigger* A-restoration: see
36706: the comment at germanic.txt:1809 and its inclusion in
```

#### Germanic/docs/DEV_NOTES.md:36720 (exact PROTOFORM)

- Nearby heading: ### §17.25.7 Regression after first build — diagnosis and follow-up fix

```text
36718: 
36719: Under the previous (Kleene-star, *r/*l-excluded) rule this didn't
36720: surface for `*táppô / *láppô` because the rule was looser overall.
36721: With the literature-grounded version, `*ô` now needs to be
36722: explicitly marked as "strong" so the subtraction does not bleed
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:81 (exact COUNTERPART)

- Nearby heading: ### 2.1 Campbell, *Old English Grammar* (1959) — file `campbell_old_english_grammar.txt`

```text
80: 
81: > § 158. The restoration of *a* is common before all single consonants and geminates, e.g. *faran* go, *calan* be cold, *bacan* bake, *gnagan* gnaw, *grafan* dig, *stapol* pillar, *sadol* saddle, *latost* latest, *lapode* he invited, *cassoc* rough grass, *hassuc* the same, *mattoc* mattock, *hnappian* fall asleep, *racca* cord, *lappa* skirt.
82: >
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:192 (exact COUNTERPART)

- Nearby heading: ### 2.4 Brunner, *Altenglische Grammatik* (1965) — file `brunner_1965_altenglische_grammatik.txt`

```text
191: 
192: > vor einem *a*, *o*, *u* der Folgesilbe (auch wenn diese wegen späteren Lautwandels nicht mehr erhalten sind), z. B. *habban* haben, *crabba* Krabbe, *lappa* Lappen (neben *læppa*), *appla* G. Pl. zu *æppel* Apfel, *mattuc* Hacke, *assa* Esel … Pl. *dagas* zu *dæg* Tag, *atol* schrecklich, *nacod* nackt, Pl. *fatu, fata, fatum* zu *fæt* Faß, *sadol* Sattel, *stadelian* befestigen, *nafela* (neben *nabula* Corp.) Nabel, *macedon* (neben *macodon*) machten, **ebenso vor dem aus -ōj- entstandenen -i- der schw. Vb. II. Kl. (§ 411, 1) macian machen, gladian sich freuen, daccian streicheln usw.** und bei Ausfall des ursprünglichen Mittelvokals *gedaf(e)nian* geziemen (neben *gedafonian*), *war(e)nian* sich hüten, *gad(e)rian* sammeln …
193: 
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:212 (exact COUNTERPART)

- Nearby heading: ### 2.5 Luick, *Historische Grammatik der englischen Sprache* — file `luick_historische_grammatik.txt`

```text
211: >
212: > 2. sehr deutlich auch vor langen Konsonanten (außer *hh, rr, ll*, die Brechung bewirkt hatten): *hnappian* einschlafen, *lappa* Lappen, *mattuc* Hacke, … *crabba* Krabbe, *gabbian* spotten, … *cassuc, hassuc* Binse …;
213: >
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:542 (exact COUNTERPART)

- Nearby heading: ### Ringe & Taylor §6.5.2 (repo ll. 12601–12674)

```text
541: dagas, magan` ← → Merc. `cwecian, wræcu, dægas, mægan`. With back umlaut
542: (ll. 12654–12668): WS `lappa, fatu, gatu, gladian, hafoc, swaþu, sparian`
543: ← → Merc. **`leappa, featu, geatu, gleadian, heafuc, sweaþu, spearian`**.
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| lap | læppa | inh | template:inh | lap |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:9539 (concept name)

- Nearby heading: ### Empirical Validation (Dry Run 2026-03-13)

```text
9537: 
9538: - **Fixed: 6** (bake, grave, wade, wake, wash, will)
9539: - **Regressed: 9** (craft, day, mast, raven, staff, tap, wain, lap, wasp)
9540: 
9541: ### Analysis: Why the Fix Fails
```

#### Germanic/docs/DEV_NOTES.md:14150 (concept name)

- Nearby heading: ## OE læppa 'lap, skirt': n-stem with voiceless *pp (2026-04-06)

```text
14148: 
14149: 
14150: ## OE læppa 'lap, skirt': n-stem with voiceless *pp (2026-04-06)
14151: 
14152: ### The problem
```

#### Germanic/docs/DEV_NOTES.md:14154 (row ID)

- Nearby heading: ### The problem

```text
14152: ### The problem
14153: 
14154: **TSV row 2090:** `*labbăz → læppa` (Old English)
14155: **FST output:** `*labbăz → læbb`
14156: **Expected:** `læppa`
```

#### Germanic/docs/DEV_NOTES.md:14338 (row ID)

- Nearby heading: ### Implementation (2026-04-06)

```text
14336: ### Implementation (2026-04-06)
14337: 
14338: Row 2090 changed:
14339: - Proto: `*labbăz` → `*lappô`
14340: - Target: `læppa` → `lappa`
```

#### Germanic/docs/DEV_NOTES.md:36687 (exact pair)

- Nearby heading: ### §17.25.7 Regression after first build — diagnosis and follow-up fix

```text
36685: of the two consonants but not the cluster span as a whole) — meaning
36686: the rule now denies restoration to all geminate-medial forms,
36687: incorrectly bleeding it for `*láppô → læppa` (target `lappa`) and
36688: spuriously satisfying it for `*táppô → tæppa` (target `tæppa`).
36689: 
```

#### Germanic/docs/DEV_NOTES.md:36744 (exact pair)

- Nearby heading: ### §17.25.7 Regression after first build — diagnosis and follow-up fix

```text
36742: **Net outcome after Bugs A + B fixes (predicted):**
36743: 
36744: - `*láppô` → `lappa` (matches target — restored from regression).
36745: - `*táppô` → `tappa` (mismatch vs target `tæppa` — now correctly
36746:   diagnosed as a TSV-target issue, parallel to *márōn and *fáraną).
```

#### Germanic/docs/DEV_NOTES.md:36770 (exact pair)

- Nearby heading: ### §17.25.8 Post-fix verification

```text
36768: - `*nadrō → næder` ✓ (no regression — *dr cluster correctly blocks)
36769: - `*bastą → bæst` ✓ (no regression — weak-tail *ą correctly blocks)
36770: - `*láppô → lappa` ✓ (Bug A fixed: geminate now matches as two segments)
36771: - `*táppô → tappa` (lautgesetzlich-correct; TSV target `tæppa` is the question)
36772: - `*márōn → mare` (lautgesetzlich-correct; TSV target `mære` is the question)
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |
| Campbell1959 | single available key for Campbell |
| Seebold1970 | single available key for Seebold |
| KlugeSeebold2011 | single available key for Kluge |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |

