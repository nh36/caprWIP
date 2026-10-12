# Evidence packet — 2168 sap / sæp

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2168 | sap | sæp | *sapōn | *sápą | early_analogy | OE neut. a-stem (Hall, K-S); Kroonen: n-stem *safō dissolved dialectally | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# sap
PROTO: *sápą
EXPECTED: sæp
OUTPUTS: sæp



### Proto-Germanic consonant inheritance

Proto Input: *sápą

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *sæpą<br>OE Heavy Syllable Nasal Apocope: *sæp |



### Orthography & surface

Outcome: sæp

NOTE: OE neut. a-stem (Hall, K-S); Kroonen: n-stem *safō dissolved dialectally
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:3851 (exact COUNTERPART)

- Nearby heading: ### Case 3: \*flaskō → \*flaskōn (OE flasce 'flask, bottle')

```text
3849: | \*wartōn | wearte | wearte | wearte | unchanged (\*r blocks) |
3850: | \*swalwōn | swealwe | swealwe | swealwe | unchanged (\*l blocks) |
3851: | \*sapōn | sæpe | sape | sæp | bucket change (pre-existing length issue) |
3852: | \*xertōn | heorte | heorte | heorte | unchanged (\*e root) |
3853: | \*laimōn | lāme | lāme | lām | unchanged (\*ai root) |
```

#### Germanic/docs/DEV_NOTES.md:3857 (exact COUNTERPART)

- Nearby heading: ### Case 3: \*flaskō → \*flaskōn (OE flasce 'flask, bottle')

```text
3855: 
3856: \*sapōn moved from `final_vowel_extra` to `fronting_missing__afb` because the root vowel is
3857: now *a* (not *æ*) while the TSV expects *sæp* (with *æ*). However, the expected form "sæp" is
3858: itself problematic: OE *sāpe* has long *ā* and is weak feminine. The proto \*sapōn has short
3859: \*a, so neither the old output (*sæpe*) nor the new (*sape*) matches the correct OE *sāpe*.
```

#### Germanic/docs/DEV_NOTES.md:11910 (exact COUNTERPART)

- Nearby heading: ### The Etymology of OE sæp 'sap'

```text
11908: Currently marked as known issue pending *w-loss rule implementation.
11909: 
11910: ### The Etymology of OE sæp 'sap'
11911: 
11912: **Problem:** FST produces `sape` from `*sapōn` instead of expected `sæp`.
```

#### Germanic/docs/DEV_NOTES.md:11912 (exact COUNTERPART)

- Nearby heading: ### The Etymology of OE sæp 'sap'

```text
11910: ### The Etymology of OE sæp 'sap'
11911: 
11912: **Problem:** FST produces `sape` from `*sapōn` instead of expected `sæp`.
11913: 
11914: **The Issue:**
```

#### Germanic/docs/DEV_NOTES.md:11916 (exact COUNTERPART)

- Nearby heading: ### The Etymology of OE sæp 'sap'

```text
11914: **The Issue:**
11915: 
11916: The current TSV has `*sapōn` (weak feminine ōn-stem), but OE `sæp` is a **neuter**
11917: noun, not a weak feminine. This is a stem-class mismatch between the proto-form
11918: and the OE reflex.
```

#### Germanic/docs/DEV_NOTES.md:11927 (exact COUNTERPART)

- Nearby heading: ### The Etymology of OE sæp 'sap'

```text
11925: 
11926: > "\*saf/ppan- m. 'sap; juice' — ON safi m. 'id.', Far. sjá-savi m. 'smell of the sea',
11927: > OSw. sava f. 'id.', **OE sæp m. 'sap'**, E sap, MDu. sap m. 'sap; juice', Du. sap n.
11928: > 'id' (with secondary neuter gender due to collective semantics), OHG saf,
11929: > sapf m. 'id.', G Saft m. 'id.' > \*sHp-on- (EUR)"
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| sap | sæp | inh | template:inh | sap |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:11926 (concept name)

- Nearby heading: ### The Etymology of OE sæp 'sap'

```text
11924: **1. Kroonen (2013), Etymological Dictionary of Proto-Germanic, s.v. \*saf/ppan-:**
11925: 
11926: > "\*saf/ppan- m. 'sap; juice' — ON safi m. 'id.', Far. sjá-savi m. 'smell of the sea',
11927: > OSw. sava f. 'id.', **OE sæp m. 'sap'**, E sap, MDu. sap m. 'sap; juice', Du. sap n.
11928: > 'id' (with secondary neuter gender due to collective semantics), OHG saf,
```

#### Germanic/docs/DEV_NOTES.md:11941 (concept name)

- Nearby heading: ### The Etymology of OE sæp 'sap'

```text
11939: **2. Kluge-Seebold (2011), Etymologisches Wörterbuch der deutschen Sprache, s.v. Saft:**
11940: 
11941: > "mhd. saft m., älter n., ahd. sa(p)f n., mndd. sap, mndl. sap Stammwort. Aus wg.
11942: > **\*sapi- m.**, auch in **ae. sæp n.**"
11943: 
```

#### Germanic/docs/DEV_NOTES.md:11951 (concept name)

- Nearby heading: ### The Etymology of OE sæp 'sap'

```text
11949: **3. Orel (2003), Handbook of Germanic Etymology, s.v. \*sapōn ~ \*sapan:**
11950: 
11951: > "\*sapōn ~ \*sapan sb.m./n.: ON safi 'sap', OE sæp id., MLG sap id., OHG saf, sapf id."
11952: 
11953: Gives both n-stem (\*sapōn) and an-stem (\*sapan) variants. Labels as masculine/neuter.
```

#### Germanic/docs/DEV_NOTES.md:11957 (concept name)

- Nearby heading: ### The Etymology of OE sæp 'sap'

```text
11955: **4. Hall (1916), A Concise Anglo-Saxon Dictionary:**
11956: 
11957: > "**sæp (e) n. 'sap,' juice**, Or, WW."
11958: 
11959: Confirms OE `sæp` is **neuter** ("n."). The "(e)" indicates variant spelling `sēp`.
```

### Analysis and dossier hits

_None_

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

