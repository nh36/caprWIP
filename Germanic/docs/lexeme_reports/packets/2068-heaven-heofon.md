# Evidence packet — 2068 heaven / heofon

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2068 | heaven | heofon | *xémenaz | *xémonų | late_analogy | PGmc mn-stem acc.sg. *xemonų (Kroonen p.220, Fulk §6.14). Derives via: o-raising (*o→*u before *ų), mn-dissimilation (*m→*β), back umlaut (*e→*eo), trisyllabic apocope (*ų→Ø). | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# heaven
PROTO: *xémonų
EXPECTED: heofon
OUTPUTS: heofon



### Proto-Germanic consonant inheritance

Proto Input: *xémonų

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>NWGmc Unstressed O Raising: *xémunų<br>NWGmc Mn Dissimilation: *xéβunų | **Old English**<br>OE Med Unstressed U Lowering: *xéβonų<br>OE Velar Fricative Palatalization: *çéβonų<br>OE Back Mutation: *çéoβonų<br>OE High Vowel Apocope: *çéoβon |



### Orthography & surface

Old English Orthography: h*éoβon
Outcome: heofon

NOTE: PGmc mn-stem acc.sg. *xemonų (Kroonen p.220, Fulk §6.14). Derives via: o-raising (*o→u before *ų), mn-dissimilation (*m→β), back umlaut (*e→eo), trisyllabic apocope (*ų→Ø).
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:12826 (row ID)

- Nearby heading: ### The Mismatch

```text
12824: ### The Mismatch
12825: 
12826: TSV row 2068:
12827: - PROTOFORM: `*xemenăz`
12828: - COUNTERPART: `heofon`
```

#### Germanic/docs/DEV_NOTES.md:12981 (row ID)

- Nearby heading: ### TSV Fix Proposed

```text
12979: 
12980: **Current state:**
12981: Row 2068 has PROTOFORM `*xemenăz` (with `-en-` suffix)
12982: - This yields `hefen` (dissimilation fires, but no back umlaut — wrong final vowel)
12983: - The `-en-` suffix doesn't trigger back umlaut (not a back vowel)
```

#### Germanic/docs/DEV_NOTES.md:29439 (exact pair)

- Nearby heading: ### §17.17.8 Implementation results (short-diphthong weight refactor)

```text
29437:      ShortDiphthong first-syllables: trisyllabic apocope fires
29438:      regardless of stress-syllable weight (Campbell §345),
29439:      so *xémonų → *xéomonų → heofon works after the split.
29440: 
29441: 3. Added Campbell §§238/346 rule: final high vowels lost after
```

#### Germanic/docs/DEV_NOTES.md:29468 (exact pair)

- Nearby heading: ### §17.17.8 Implementation results (short-diphthong weight refactor)

```text
29466: | *márkō    | mearc   | mearc    | HEAVY (rk cluster)    |
29467: | *xállō    | heall   | heall    | HEAVY (ll geminate)   |
29468: | *xémonų   | heofon  | heofon   | trisyllabic (light 1) |
29469: | *féxu     | feoh    | feoh     | §238 -u after h loss  |
29470: | *skipu    | sċipu   | sċipu    | LIGHT, no diphthong   |
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:22 (exact COUNTERPART)

- Nearby heading: ### Mismatch fixes (Mar 2026)

```text
20: - [OE huniġ 'honey': The -ag > -ig Sound Change](#oe-huniġ-honey-the--ag---ig-sound-change-2026-03-19)
21: - [OE wīþiġ 'withy': ja-stem vs Sievers' Law](#oe-wīþiġ-withy-ja-stem-adjective-vs-sievers-law-syncope-2026-03-19)
22: - [OE heofon 'heaven': Back Umlaut and Nasal Dissimilation](#oe-heofon-heaven-back-umlaut-and-medial-syncope-2026-03-20)
23: - [OE lungen 'lung': The *-anjō Suffix Problem](#oe-lungen-lung-the--anjō-suffix-problem-2026-03-21)
24: 
```

#### Germanic/docs/DEV_NOTES.md:232 (exact COUNTERPART)

- Nearby heading: ### OE Medial unstressed `*u → *o`: Conditioning environment (2026-03-20)

```text
230: 
231: 1. **Words where medial `*u → *o` is correct:**
232:    - `*xeβun` (< `*xemonų`) → `heofon` (Campbell §293)
233:    - `*sebun` → `seofon` (Campbell §293, §331 fn.3)
234: 
```

#### Germanic/docs/DEV_NOTES.md:252 (exact COUNTERPART)

- Nearby heading: ### OE Medial unstressed `*u → *o`: Conditioning environment (2026-03-20)

```text
250: 
251: The key is the **dialectal difference**:
252: - **WS/Northumbrian**: medial `*u → *o` → `seofon`, `heofon`
253: - **Mercian**: medial `*u → *e` (vowel harmony per Campbell §385) → `seofen`, `heofen`
254: 
```

#### Germanic/docs/DEV_NOTES.md:274 (exact COUNTERPART)

- Nearby heading: ### OE Medial unstressed `*u → *o`: Conditioning environment (2026-03-20)

```text
272: > texts... In Ep., however, **protected u > o very often**, e.g. uuiloc-, helostr,
273: > déatlicostan, suornodun... Ordinary OE forms are, however, e.g. héafod head,
274: > **heofon** heaven, tungol star, past indic. pl. -on..."
275: 
276: And critically, the exception:
```

#### Germanic/docs/DEV_NOTES.md:290 (exact COUNTERPART)

- Nearby heading: ### OE Medial unstressed `*u → *o`: Conditioning environment (2026-03-20)

```text
288: 
289: - `*sebun` → `seofon` ✓: accented `*e`, so medial `*u` → `*o`
290: - `*xeβun` → `heofon` ✓: accented `*e`, so medial `*u` → `*o`
291: - `*widuwōn` → `widuwe` ✓: accented `*i` (but followed by `u`!), and more importantly
292:   the second `*u` follows after root `*widu-` which has `u` — Campbell says `u` is
```

#### Germanic/docs/DEV_NOTES.md:312 (exact COUNTERPART)

- Nearby heading: # Block if stressed syllable (first syllable) contains *u

```text
310: **Predictions:**
311: - `*sébun` (accented `*e`): `*u → *o` → `seofon` ✓
312: - `*xéβun` (accented `*e`): `*u → *o` → `heofon` ✓
313: - `*wúduwōn` (accented `*u`): `*u` preserved → `wuduwe` ✓
314: - `*wíduwōn` (accented `*i`): should give `*u → *o`? But OE has `widuwe`...
```

### Analysis and dossier hits

#### Germanic/docs/analysis/compound_archaism_inventory.md:200 (exact COUNTERPART)

- Nearby heading: ### Case 9: *héfanaz (heaven) — heofon (lautgesetzlich WS) vs. hefēn/hefen (Anglian)

```text
199: 
200: ### Case 9: *héfanaz (heaven) — heofon (lautgesetzlich WS) vs. hefēn/hefen (Anglian)
201: 
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:205 (exact COUNTERPART)

- Nearby heading: ### Case 9: *héfanaz (heaven) — heofon (lautgesetzlich WS) vs. hefēn/hefen (Anglian)

```text
204: | **PROTO** | `*héβan` / `*hemĭn` (m., stem class varies by source; root *hem-*, suffix *-an* or *-in*) |
205: | **OE WS** | `heofon` (nom.sg., showing back umlaut *e → eo* before labial+back vowel in suffix *-on*) |
206: | **OE ANGLIAN** | `hefen` (showing front vowel in suffix *-en*, no back umlaut trigger) |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:208 (exact COUNTERPART)

- Nearby heading: ### Case 9: *héfanaz (heaven) — heofon (lautgesetzlich WS) vs. hefēn/hefen (Anglian)

```text
207: | **Sound changes** | Back umlaut (*e → eo* before labial+back vowel) in WS; no umlaut in Anglian (suffix has front vowel) |
208: | **Lautgesetzlich output** | `heofon` (WS, from back umlaut); `hefen` (Anglian, from front suffix *-en* = no umlaut) (FST WS path: ✓ correct) |
209: | **Attested simplex** | Both `heofon` (WS) and `hefen` (Anglian); forms represent **different suffix vowels in the paradigm**. Per Campbell §210.1, WS generalized the oblique *-un-* to the nom.sg., giving `heofon` with back umlaut. |
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:334 (exact COUNTERPART)

- Nearby heading: ### Hogg vol. 1 (repo ll. 5678–5694) — WS restriction explicit

```text
333: > occurred only if the preceding vowel was /i/ ... Typical examples are:
334: > *sifon > siofon 'seven', *hefon > heofon 'heaven', *lifað > leofað 'he
335: > lives', but a word such as fela 'many', since it had /e/ before /a/ rather
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:365 (exact COUNTERPART)

- Nearby heading: ### Campbell §210 — concrete dialect contrast

```text
364: Campbell §210 (repo ll. 6319–6336): in WS u-umlaut occurs before labials
365: and liquids (`heofon, eofor, beofor, heorot`) but not generally before other
366: consonants; a-umlaut is mostly absent (`fela, helan, beran, nefa, sefa,
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:654 (exact COUNTERPART)

- Nearby heading: ## 9. u-mutation vs. back mutation; dialect distribution

```text
653: 
654: - **WS**: u-umlaut general before single labial/liquid (`heofon, eofor,
655:   beofor, heorot`); a-umlaut "generally absent" (`fela, helan, beran, nefa,
```

#### Germanic/docs/dossiers/un-to-on-chronology.md:44 (exact COUNTERPART)

- Nearby heading: ### Campbell §49, §373, §735(e)

```text
43: > lNorth. and Ru.1. Ordinary OE forms are, however, e.g. heafod head,
44: > heofon heaven, tungol star, **past indic. pl. -on**, weak past of
45: > Class II -ode, superl. -ost, but n.s. of wa-, o- and u-stems -u,
```

#### Germanic/docs/dossiers/un-to-on-chronology.md:169 (exact COUNTERPART)

- Nearby heading: ### Luick §326

```text
168: > zu sein; **doch wirkt auch hier ein u der Stammsilbe (vor einfachen
169: > Konsonanten) bewahrend**. So: (urg. u) nacod, hēafod, heofon, hamor,
170: > **ridon, wǣron**, h(e)afoc, nafola, afora; (u nach §317) sāwol,
```

#### Germanic/docs/dossiers/un-to-on-chronology.md:231 (exact COUNTERPART)

- Nearby heading: ### Hogg vol.1 §3.3.1.3 + §3.3.3.2

```text
230: > "/u/ had a strong tendency to lower, **especially when a consonant
231: > followed**, so we find, for example, **heofon 'heaven' in Early West
232: > Saxon rather than heofun**, although **if /u/ is in absolute
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:405 (exact COUNTERPART)

- Nearby heading: ### What NOT to do

```text
404:   attested for unstressed `*u` in the relevant environment (cf.
405:   `heofon`, `tungol`, past-pl. `-on`, `beadowe`, `swalewan`).
406: 
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:1746 (exact COUNTERPART)

- Nearby heading: ### D.1 Open vs. closed syllable conditioning

```text
1745: > zu sein; **doch wirkt auch hier ein u der Stammsilbe (vor einfachen
1746: > Konsonanten) bewahrend**. So: … nacod, hēafod, heofon, hamor, ridon,
1747: > wǣron, hafoc, nafola, afora; sāwol, wundor, tungol; huntoð, geogoð,
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| heaven | heofon | inh | template:inh | heaven |

#### old_english_swadesh.tsv

| NUMBER | ENGLISH | OLD_ENGLISH | IPA_RAW |
| :--- | :--- | :--- | :--- |
| 162 | sky | heofon | /ˈheo̯von/ |

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:644 (concept name)

- Nearby heading: #### 2. OE Medial Unstressed *u → *o (Campbell §373)

```text
642: **Examples where the change applies:**
643: - `*sebun → seofon` 'seven' (accented vowel is `*e`, not `*u`)
644: - `*xeβun → heofon` 'heaven' (accented vowel is `*e`, not `*u`)
645: - Past plural `-un → -on` (accented vowel is in the root, not `*u`)
646: 
```

#### Germanic/docs/DEV_NOTES.md:12822 (concept name)

- Nearby heading: ## OE heofon 'heaven': Back Umlaut and Medial Syncope (2026-03-20)

```text
12820: ---
12821: 
12822: ## OE heofon 'heaven': Back Umlaut and Medial Syncope (2026-03-20)
12823: 
12824: ### The Mismatch
```

#### Germanic/docs/DEV_NOTES.md:12838 (concept name)

- Nearby heading: ### Source Research

```text
12836: 
12837: **Kroonen (2013) p.220:**
12838: > `*hemina-` ~ `*hemna-` m. 'heaven' — Go. himins m. 'id.', ON himinn m. 'id.', 
12839: > Far. himin m. 'id.', OE heofon m. 'id.', E heaven, OFri. himel m. 'id.', OS himil, 
12840: > heban m. 'id.', ODu. himil m. 'id.', Du. hemel c. 'id.', OHG himil m. 'id.', G 
```

#### Germanic/docs/DEV_NOTES.md:12839 (concept name)

- Nearby heading: ### Source Research

```text
12837: **Kroonen (2013) p.220:**
12838: > `*hemina-` ~ `*hemna-` m. 'heaven' — Go. himins m. 'id.', ON himinn m. 'id.', 
12839: > Far. himin m. 'id.', OE heofon m. 'id.', E heaven, OFri. himel m. 'id.', OS himil, 
12840: > heban m. 'id.', ODu. himil m. 'id.', Du. hemel c. 'id.', OHG himil m. 'id.', G 
12841: > Himmel m. 'id.'
```

#### Germanic/docs/DEV_NOTES.md:19148 (exact pair)

- Nearby heading: ### Attempted Fix (2026-04-14)

```text
19146: **Result:** Fixed `*júgunθ → ġeoguþ` but caused regressions:
19147: - `*búgun → bugun` (expected `bugon`) — harmony over-applied
19148: - `*xémonų → heofun` (expected `heofon`) — harmony over-applied
19149: - `*skúbun → sċufun` (expected `sċufon`) — harmony over-applied
19150: 
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |
| Campbell1959 | single available key for Campbell |
| SieversBrunner1965 | single available key for Sievers |
| Fulk2018 | single available key for Fulk |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |

## Paradigm probe

Paradigm probe required for this row, but no built-in `oe_paradigm_probe.py` specification exists yet. This packet should be used to draft the probe configuration before prose drafting.

