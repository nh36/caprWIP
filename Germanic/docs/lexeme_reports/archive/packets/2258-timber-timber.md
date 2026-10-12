# Evidence packet — 2258 timber / timber

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2258 | timber | timber | *tímrą | *tímbrą | early_analogy | Kroonen *timbra- with *b; OE timber. | Source: Wiktionary etymology (template:der) \| Source: Wiktionary etymology (template:der) \| TSV fix: proto *timrą → *timbrą. |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# timber
PROTO: *tímbrą
EXPECTED: timber
OUTPUTS: timber



### Proto-Germanic consonant inheritance

Proto Input: *tímbrą

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>OE Heavy Syllable Nasal Apocope: *tímbr<br>OE Epenthetic Vowel: *tímber |



### Orthography & surface

Outcome: timber

NOTE: Kroonen *timbra- with *b; OE timber.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:2324 (exact COUNTERPART)

- Nearby heading: ### KIT sweep (WIP)

```text
2322: - Fed the KIT bucket through the same dockered `flookup` harness (`python3 - <<'PY' …`) after filtering out diphthongs (`aɪ/eɪ/ɔɪ`). The remaining 35 entries are the genuine `{ɪ}` cases headed by `fish/give/six/will` alongside the `{ɪə}` + post-vocalic /r/ cohort (`beard/bier/deer/spear/ year`, etc.).
2323: - Updated `EnglishSandboxCoreVowelRules` so short `{*i}` finally drops its star and enters the plain alphabet, and extended `EnglishSandboxShortVowelSplit` with `{i}`→`{ɪ}` rewrites in closed syllables / word-final contexts. This keeps the KIT conditioning in the same stage as the `{*e}`/{`*u`} splits instead of leaving `{*i}` untouched.
2324: - The attested-form harness still lands at 179/376 successes (KIT bucket = 35) because the stubborn cases need post-vocalic /r/ smoothing (`{ɪ}`→`{ɪə}` before the new `EnglishSandboxPostVocalicRLoss`) or suffixal analogies (`sieve/singe/timber`). Logged them here so the next pass can target `{ɪə}` outputs without sacrificing the `{bəʊn}/{fʊt}` improvements we just landed.
2325: 
2326: ## 2025-12-04
```

#### Germanic/docs/DEV_NOTES.md:16673 (exact COUNTERPART)

- Nearby heading: ### OEEpentheticInsertion: Parasitic Vowel in Final Consonant Clusters (2026-04-10)

```text
16671: **Examples:**
16672: - PGmc `*fingrăz` → OE `finger` (via `*fingr → *fingEr → *finger`)
16673: - PGmc `*timbrą` → OE `timber` (via `*timbr → *timbEr → *timber`)
16674: - PGmc `*wintruz` → OE `winter` (via `*wintr → *wintrEr → *winter`)
16675: - PGmc `*hungruz` → OE `hungor` (via `*hungr → *hungrEr → *hungEr → *hungor`)
```

#### Germanic/docs/DEV_NOTES.md:16689 (exact COUNTERPART)

- Nearby heading: ### OEEpentheticInsertion: Parasitic Vowel in Final Consonant Clusters (2026-04-10)

```text
16687: The quality of the epenthetic vowel depends on the preceding vowel:
16688: - After back vowels: `*E → *o` (e.g., `hungor`, `fugol`)
16689: - After front vowels: `*E → *e` (e.g., `finger`, `timber`)
16690: 
16691: This is handled by `OEEpentheticBackShift` (→ *o) and `OEEpentheticFront` (→ *e).
```

#### Germanic/docs/DEV_NOTES.md:16709 (exact COUNTERPART)

- Nearby heading: ### OEEpentheticInsertion: Parasitic Vowel in Final Consonant Clusters (2026-04-10)

```text
16707: 
16708: **Conclusion:**
16709: - `OEEpentheticInsertion` is a real phonological rule needed for words like `finger`, `timber`, `winter`
16710: - It is NOT a hack for `water` — water works via a different rule (`PWGmcFinalOrLowering`)
16711: - Both rules are necessary and do different things in the phonological pipeline
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| timber | timber | der | template:der | timber |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

_None_

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

