# Evidence packet — 2278 weapon / wǣpn

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2278 | weapon | wǣpn | *wḗpną | *wḗpną | regular | Proto: oblique *wēpnăn→*wēpną (n. a-stem nom.sg.; Kroonen) | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# weapon
PROTO: *wḗpną
EXPECTED: wǣpn
OUTPUTS: wǣpn



### Proto-Germanic consonant inheritance

Proto Input: *wḗpną

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>NWGmc Long E Lowering: *wǣpną | **Old English**<br>OE Heavy Syllable Nasal Apocope: *wǣpn |



### Orthography & surface

Outcome: wǣpn

NOTE: Proto: oblique *wēpnăn→wēpną (n. a-stem nom.sg.; Kroonen)
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:29856 (exact COUNTERPART)

- Nearby heading: #### §17.18.1  The lautgesetzlich background (Campbell §§360–363; Hogg §§6.30–6.36; SB §§145–146)

```text
29854: 
29855: OE inherits, after WGmc/OE syncope, stem-final clusters of the type
29856: obstruent + sonorant (e.g. \*þistl-, \*tācn-, \*wǣpn-, \*hræfn-,
29857: \*wuldr-, \*fugl-). In the **NomSg/AccSg** of masc/neut a-stems (zero
29858: ending) the cluster falls **word-finally**, where late OE develops a
```

#### Germanic/docs/DEV_NOTES.md:29872 (exact COUNTERPART)

- Nearby heading: #### §17.18.1  The lautgesetzlich background (Campbell §§360–363; Hogg §§6.30–6.36; SB §§145–146)

```text
29870: Parasiting is dialectally and chronologically variable:
29871:    - **Late WS prose (Ælfric, Wulfstan, laws)**: the rule is regular.
29872:    - **Beowulf and other poetry**: unbroken forms (*hræfn, wǣpn, tācn*)
29873:      preserved metri causa.
29874:    - **Anglian (Mercian, early Northumbrian)**: less prominent (Campbell §363).
```

#### Germanic/docs/DEV_NOTES.md:29899 (exact COUNTERPART)

- Nearby heading: #### §17.18.2  Current TSV state (11 candidate words)

```text
29897: | 9 | \*stébnō | stefn | stefn | ✓ |
29898: | 10 | \*táikną | tācn | tācn | ✓ |
29899: | 11 | \*wēpną | wǣpn | wǣpn | ✓ |
29900: 
29901: So the FST currently does **no** parasiting for `-Cl/Cn/Cm#` (except a
```

#### Germanic/docs/DEV_NOTES.md:29921 (exact COUNTERPART)

- Nearby heading: #### §17.18.3  Attestation findings (per agent research, sources cited at end)

```text
29919: | 9 | stefn | ✅ standard | rare | **stefn** |
29920: | 10 | tācn | ✅ (Beowulf 141) | ✅✅ (LWS prose dominant; Beo 833) | **tācn** (DOE) |
29921: | 11 | wǣpn | ✅ (mainly compounds, poetic simplex) | ✅✅ standard simplex | **wǣpen** (BT/DOE) |
29922: 
29923: **Critical findings:**
```

#### Germanic/docs/DEV_NOTES.md:29933 (exact COUNTERPART)

- Nearby heading: #### §17.18.3  Attestation findings (per agent research, sources cited at end)

```text
29931:    (Lchdm. ii.312.20); Ælfric glossaries.
29932: 
29933: 2. **\*wǣpn is similarly marginal as a simplex NomSg.** BT and DOE both
29934:    lemmatize **wǣpen** (broken) as the headword. *wǣpn* survives mainly
29935:    in compounds (*hildewǣpn-*) and poetic simplex.
```

#### Germanic/docs/DEV_NOTES.md:29934 (exact COUNTERPART)

- Nearby heading: #### §17.18.3  Attestation findings (per agent research, sources cited at end)

```text
29932: 
29933: 2. **\*wǣpn is similarly marginal as a simplex NomSg.** BT and DOE both
29934:    lemmatize **wǣpen** (broken) as the headword. *wǣpn* survives mainly
29935:    in compounds (*hildewǣpn-*) and poetic simplex.
29936: 
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| weapon | wǣpn | inh | template:inh | weapon |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:2249 (concept name)

- Nearby heading: ### Sandbox vowel expansion

```text
2247:   - `{*ai}` now yields `{əʊ}` before nasals, velars, labials, and the `gw/kn/xw` clusters that cover the attested `bəʊn/fəʊl/snow/stone/soul/token` cases.
2248:   - `{*au}` exposes an `{əʊ}` branch in addition to `{aʊ}/{oː}`, `{*ō}` can realise `{ɔː}` or `{ʊ}` in the usual `r/l/#` and velar-k environments, and `{*a}` picks up `{ɔː}` before `l/r/w`.
2249:   - Added a dedicated schwa cleanup for the weak-tail templates (`-az/-an/-nē/-gą/-lō/-raz`) so `hammer`, `bottom`, `weapon`, etc. stop stalling solely because the tail vowel stayed as `{a}`.
2250: - `docker compose exec backend sh -lc 'cd /usr/app && foma -f fsts/english_brace_sandbox.txt'` recompiles the sandbox to a 21.7 kB automaton (201 states / 23 M paths). Quick probes such as `printf 'bɔːl\nkɔːn\nfəʊl\nbəʊn\nbʊk\n' | flookup english_brace_sandbox.bin` now return full proto bundles instead of `+?`.
2251: - `python3 server/tools/api_regression.py` still PASS for both Burmish and Germanic datasets, so the extra branches did not perturb the production analyzer.
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |
| Campbell1959 | single available key for Campbell |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |

## Paradigm probe

Philological note; no paradigm probe required for this row under the current classification. The note mentions paradigm forms, but it does not yet depend on a paradigm-cell solution.

