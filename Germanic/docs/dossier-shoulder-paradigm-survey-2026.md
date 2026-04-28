# Shoulder paradigm survey 2026: cell-by-cell PROTOFORM ↔ COUNTERPART probe of `*skuldra-`

A research dossier for TSV row 2183 (`*skúldrō` ↔ `sċuldra`).

**Reframed question.** The TSV row must satisfy
PROTOFORM-cell = COUNTERPART-cell. The COUNTERPART need *not* remain
`sċuldra` — that is just the form a previous editor chose. The
question is: **is there ANY paradigm cell of `*skuldra-` whose
reconstructed PGmc/PWGmc input yields, lautgesetzlich through the
project's cascade, the OE form attested for that same cell?**

If yes, row 2183 can be relabeled (PROTOFORM = the cell's PGmc form;
COUNTERPART = the cell's attested OE form) and become cell-consistent
and Neogrammarian-correct. The late-WS analogical NSg `sċuldra` would
simply be the wrong COUNTERPART to have chosen, replaceable by the
correct cell-consistent counterpart for whichever cell the cascade
**does** model correctly.

This dossier complements (does NOT supersede) the prior shoulder
dossiers (`dossier-shoulder-2026.md`, `dossier-shoulder-cellchoice-2026.md`,
`dossier-shoulder-lautgesetz-2026.md`).

**Headline result.** Every non-high-suffix cell (NSg, AccSg,
GenSg, DatSg, VocSg, NPl, GenPl across all stem classes) feeds
NWGmcULowering and produces a root /o/ that mismatches OE /u/.
The NApl `*skúldru` preserves /u/ but emerges as `sċuldor`, not
the BT/Hall NApl `sculdru`. **The DatPl `*skuldrumiz` ↔ `sculdrum`
is the only cell-pair that would yield an attested OE form
lautgesetzlich with the root /u/ preserved** — by virtue of the
high `*u` in the suffix blocking u-lowering. It is currently
gated only by the FST's proto-input alphabet, which the user has
indicated is acceptable to widen. **Recommendation: relabel row
2183 as the DatPl cell and widen the proto-input FST to accept
`*-umiz`.**

---

## §0. Method, source authorities, and FST encoding

### 0.1. Trace tool

Each candidate is run through

```
cd /Users/nathanhill/Code/capr-v3-working
python3 Germanic/tools/trace_old_english_sandbox.py --lexeme '<form>' --bin-dir /usr/app
```

which `docker compose exec`'s `flookup` against each cascade-stage
binary. Per `Germanic/tools/trace_old_english_sandbox.py` the
strip-regex is `[{}*\s\-/()]` — asterisks, braces, hyphens,
slashes, parens, whitespace. The acute mark on the stressed vowel
is **kept**, consistent with `*búgô`, `*gállô`, `*námô` etc. in
the existing TSV.

A `+?` line in the trace = flookup rejected the input string.

### 0.2. Project encoding for the relevant suffixes

Verified from `Germanic/fsts/germanic.txt` and from existing TSV
protoforms:

| segment      | meaning                                      | TSV examples                          |
|--------------|----------------------------------------------|---------------------------------------|
| `ą`          | short nasal *a (neut. a-stem NSg, AccSg)     | `*wúndrą`, `*bástą`, `*bérgą`         |
| `ô`          | trimoric oral *ō (weak masc. n-stem NSg, etc.) | `*búgô`, `*gállô`, `*námô`, `*xágô`, `*fúlô` |
| `ō`          | bimoric oral *ō (fem. ō-stem NSg)            | `*skúldrō`                            |
| `u`          | short *u (NApl light neut. a-stem, etc.)     | `*spéru`                              |
| `az`         | masc. a-stem NSg                             | `*sáumaz`, `*stráumaz`                |
| `as`         | masc. a-stem GenSg                           | `*xámaras` → `hameres`                |
| `ǭ` (internal) | bimoric long nasal *ō                       | cascade-internal only (`fláskōn` → `fláskǭ`) |
| `umiz`/`umaz`/`um` | DatPl                                  | **not currently encoded as input** — see §0.3 and §11 |
| `ǫ̂` / `ǭ`/`ô` + `n` | trimoric/nasalised plural endings    | not encoded as input — see §0.3       |

### 0.3. Encodings the FST does NOT currently accept

Empirically verified by `+?` rejection at the `ProtoInput` stage:

* **DatPl variants:** `*skúldrumiz`, `*skúldrumaz`, `*skúldrum`,
  `*skúldrumz` — all rejected. The proto-input alphabet does not
  include word-medial/final `m` followed by case endings of this
  shape. The TSV has no DatPl rows for any lexeme; the cascade's
  input language is templated on NSg/AccSg/GenSg/NApl morphology.
  **This is the gate that the present dossier's recommendation
  asks to widen — see §11.**
* `*skúldrǫ̂`, `*skuldrǫ̂`, `*skúldrǭ`, `*skúldrǫ`, `*skúldrų`,
  `*skúldrôz`, `*skúldrôN`, `*skúldrōN`, `*skúldrōn`,
  `*skúldraN`, `*skúldrunz`, `*skúldrunþ`, `*skúldrans`,
  `*skúldrēz`, `*skúldris`, `*skúldrēs`, `*skúldrasa`,
  `*skúldrōi` — **all rejected.**
* `*skúldrijō`, `*skúldrijōn`, `*skuldrijōn`, `*skuldrjōn`,
  `*skúldrjaz`, `*skúldrija`, `*skúldrijaN`, `*skúldrijų` —
  jōn/jaz-stem case forms, **all rejected**, except
  `*skúldrijaz` which is accepted at ProtoInput but produces
  `Surface: +?` (no surface form realisable from `*ʃyldrj`).

These rejections are themselves data: they constrain which cells
are operationally reachable.

### 0.4. Source authorities

Where verification was possible in the session, citations are
given. Where not, `[citation needed]` is used rather than an
invented page number.

| short cite     | full reference                                                                |
|----------------|-------------------------------------------------------------------------------|
| Kroonen EDPG   | Kroonen, *Etymological Dictionary of Proto-Germanic* (2013), s.v. `*skuldra-` (p. 478). |
| R/T vol.1      | Ringe, *From Proto-Indo-European to Proto-Germanic* (2nd ed., 2017).          |
| R/T vol.2      | Ringe & Taylor, *The Development of Old English* (2014).                      |
| Krahe-Meid     | Krahe & Meid, *Germanische Sprachwissenschaft* I–III (1969).                  |
| Boutkan EOFL   | Boutkan, *The Germanic 'Auslautgesetze'* (1995).                              |
| Boutkan SDOFD  | Boutkan & Siebinga, *Old Frisian Etymological Dictionary* (2005).             |
| Campbell       | Campbell, *Old English Grammar* (1959).                                       |
| Hogg           | Hogg, *A Grammar of Old English*, vol. I: Phonology (1992).                   |
| Brunner        | Brunner, *Altenglische Grammatik* (3rd ed., 1965).                            |
| Luick          | Luick, *Historische Grammatik der englischen Sprache* (1914–40).              |
| BT             | Bosworth-Toller, *An Anglo-Saxon Dictionary* (1898) and Toller's Supplement.  |
| Hall           | Clark Hall, *A Concise Anglo-Saxon Dictionary* (4th ed., 1960).               |

---

## §1. The seven stem classes proposed for `*skuldra-`

| Stem class                  | PGmc lemma         | Source                                      | Daughter evidence                          |
|-----------------------------|--------------------|---------------------------------------------|--------------------------------------------|
| Masc. a-stem                | `*skuldraz`        | Kroonen EDPG p. 478 (lemma)                 | OE `sculdor` m., ON `skoldr` m.            |
| Fem. ō-stem                 | `*skuldrō`         | TSV current; cf. OHG `scultira`, MHG `schulter`, G `Schulter`, Du `schouder` | OHG `scultira` f., G `Schulter` f., Du `schouder` |
| Neut. a-stem (hypothetical) | `*skuldrą`         | included by analogy with `*wundrą`; no daughter unambiguously supports neut. gender | none |
| jōn-stem                    | `*skuldrijōn-`     | Kroonen EDPG p. 478 cites OHG `scultarra`   | OHG `scultarra` f.                         |
| ōn-stem (weak fem.)         | `*skuldrōn-`       | [citation needed]; underlying source for late-WS weak fem. NSg `sċuldra`, OS `skuldera`, OFris `skuldere` | OS `skuldera` f., OFris `skuldere` f., late-WS `sċuldra` f. |
| u-stem (speculative)        | `*skuldruz`        | [reconstruction not given in standard sources for this etymon; speculative; included only as phonological probe] | none |
| i-stem (speculative)        | `*skuldriz`        | [reconstruction not given in standard sources for this etymon; speculative; included only as phonological probe] | none |

The masc. a-stem is the only class that fits the full attested OE
strong masculine paradigm `sculdor / sculdres / sculdre / pl.
sculdru, sculdra, sculdrum`.

---

## §2. The OE paradigm cells and what input the cascade should receive

### 2.1. Masc. a-stem `*skuldraz` (the well-attested class)

OE strong masc. a-stem paradigm of *sculdor* (Campbell §574, Hogg
§3.18, Brunner §240, BT s.v. *sculdor*):

| Cell      | PGmc                | PWGmc (R/T vol.2 §3.1)        | Attested OE                 | FST input probed     |
|-----------|---------------------|-------------------------------|-----------------------------|----------------------|
| NSg       | `*skuldraz`         | `*skuldr`                     | `sculdor`                   | `*skúldraz`          |
| AccSg     | `*skuldrą`          | `*skuldr`                     | `sculdor`                   | `*skúldrą`           |
| GenSg     | `*skuldras`         | `*skuldras`                   | `sculdres`                  | `*skúldras`          |
| DatSg     | `*skuldrai`         | `*skuldrē`                    | `sculdre`                   | `*skúldrai`          |
| InstrSg   | `*skuldrō` [citation needed] | `*skuldru` / `*skuldrō` | `sculdre` (merged with Dat) | (= DatSg)            |
| VocSg     | `*skuldra` [citation needed] | `*skuldr`           | `sculdor` (= NSg)            | `*skúldra`           |
| NPl/AccPl | `*skuldrôz` / `*skuldrōz` | `*skuldrō` (heavy → `-as` in OE by leveling, or zero-NApl in earliest sources) | `sculdras` (classical), `sculdor` (zero-NApl, marginal) | `*skúldrōz` / `*skuldrōz` |
| GenPl     | `*skuldrǫ̂` (PGmc trimoric long nasal) | `*skuldrō` (oral)   | `sculdra`                   | `*skúldrô` (project trimoric encoding) |
| **DatPl** | **`*skuldrumiz` / `*skuldrumaz`** (R/T vol.1 §3.2.2) | **`*skuldrum`** (R/T vol.2 §3.1.6 [page]) | **`sculdrum`** | `*skúldrumiz` / `*skúldrumaz` / `*skúldrum` (all rejected — see §11) |
| InstrPl   | (= DatPl in PGmc)   | `*skuldrum`                   | `sculdrum`                  | (= DatPl)            |
| Dual      | not productive in nouns | —                          | —                           | —                    |

### 2.2. Fem. ō-stem `*skuldrō` (current TSV)

OE strong fem. ō-stem paradigm (Campbell §586, Hogg §3.21,
Brunner §252):

| Cell    | PGmc                  | PWGmc                       | Attested OE for a heavy ō-stem | FST input probed |
|---------|-----------------------|-----------------------------|--------------------------------|------------------|
| NSg     | `*skuldrō`            | `*skuldru` (R/T vol.2 §3.1.4) | (no certain heavy fem. ō-stem reflex; classical `sculdor` is masc.; the late-WS weak fem. `sċuldra` is analogical) | `*skúldrō` |
| AccSg   | `*skuldrǭ`            | `*skuldrā`                  | (heavy → `-e`)                 | `*skúldrǭ`       |
| GenSg   | `*skuldrōz`           | `*skuldrā`                  | (heavy → `-e`)                 | `*skuldrōz`      |
| DatSg   | `*skuldrōi`           | `*skuldrā`                  | (heavy → `-e`)                 | `*skúldrōi`      |
| NApl    | `*skuldrōz`           | `*skuldrā` / `*skuldrō`     | (heavy → `-a`)                 | (= GenSg input)  |
| GenPl   | `*skuldrǫ̂`           | `*skuldrō` → `*skuldra`     | (`-a`)                          | (= masc. GenPl)  |
| **DatPl** | `*skuldrōmiz`       | `*skuldrum`                 | `-um`                            | (rejected — see §11) |

### 2.3. Neut. a-stem `*skuldrą` (hypothetical)

| Cell    | PGmc          | PWGmc                       | OE (heavy neut.) | FST input |
|---------|---------------|-----------------------------|------------------|-----------|
| NSg/AccSg | `*skuldrą`  | `*skuldr`                   | `sculdor`        | `*skúldrą` |
| NApl    | `*skuldrō`    | `*skuldru` (heavy → zero in classical; `-u` in early/Anglian) | `sculdor` (classical zero-NApl); early/Anglian `sculdru` | `*skúldrō` (= fem. NSg) and `*skúldru` (post-shortening) |
| (others) | identical to masc. a-stem |                  |                  |           |

### 2.4. jōn-stem `*skuldrijōn-`

The OHG variant. No certain OE descendant. All cells rejected by
ProtoInput (see §0.3, §6).

### 2.5. ōn-stem (weak fem.) `*skuldrōn-`

Underlies OS `skuldera`, OFris `skuldere`, late-WS analogical
`sċuldra`. All cells rejected by ProtoInput (see §0.3, §7).

### 2.6. u-stem `*skuldruz` and i-stem `*skuldriz` (speculative)

Phonological probes only; no source supports either for this
etymon.

---

## §3. Empirical FST traces — masc. a-stem cells

Surface output below = the `Surface:` line of each trace. Salient
intermediate stages reproduced.

### 3.1. NSg `*skuldraz`

```
=== *skúldraz ===
WestGermanic: *s*k*ú*l*d*r*a*z
NWGmcULowering: *s*k*ó*l*d*r*a*z
... ProtoToOE: *ʃ*ó*l*d*r ... Epenthesis: *ʃ*ó*l*d*o*r
Surface: sċoldor
```

* OE attested: `sculdor`. Cascade: `sċoldor`. Mismatch (root /o/ vs /u/).
* **Cell-consistent match? NO.**

### 3.2. AccSg `*skuldrą`

```
=== *skúldrą ===
NWGmcULowering: *s*k*ó*l*d*r*ą
Surface: sċoldor
```

* OE attested: `sculdor`. **NO match** (root vowel).

### 3.3. GenSg `*skuldras`

```
=== *skúldras ===
NWGmcULowering: *s*k*ó*l*d*r*a*s
Orthography: sċoldres
Surface: sċoldres
```

* OE attested: `sculdres`. Cascade: `sċoldres`. **NO match** (root vowel).
* This is the precise parallel to TSV row 478 (`*xámaras` GenSg →
  `hameres` GenSg). Whereas hammer's GenSg works lautgesetzlich,
  shoulder's GenSg fails by exactly the /u/→/o/ regression.

### 3.4. DatSg `*skuldrai`

```
=== *skúldrai ===
NWGmcULowering: *s*k*ó*l*d*r*ē
Surface: sċoldre
```

* OE attested: `sculdre`. Cascade: `sċoldre`. **NO match** (root vowel).

### 3.5. VocSg / bare-final `*skuldra`

```
=== *skúldra ===  Surface: sċoldor
=== *skuldra  ===  Surface: sċoldor
```

* OE VocSg = NSg `sculdor`. Cascade: `sċoldor`. **NO match** (root vowel).

### 3.6. NPl/AccPl `*skuldrōz`

```
=== *skúldrōz ===
NWGmcULowering: *s*k*ó*l*d*r*ō*z
Surface: sċoldre

=== *skuldrōz ===
NWGmcULowering: *s*k*o*l*d*r*ō*z
Surface: sċoldre
```

* OE attested: `sculdras` (classical) / `sculdor` (zero-NApl).
* Cascade: `sċoldre` — routes via the fem. ō-stem GenSg/NApl `-e`
  path, not the masc. a-stem `-as` path. Cell route mismatch.
* **NO match.**

### 3.7. GenPl `*skuldrǫ̂` (project encoding `*skúldrô`)

```
=== *skúldrô ===
WestGermanic: *s*k*ú*l*d*r*ô
NWGmcULowering: *s*k*ó*l*d*r*ô
... Epenthesis: *ʃ*ó*l*d*r*a
Surface: sċoldra

=== *skuldrô ===
NWGmcULowering: *s*k*o*l*d*r*ô
Surface: sċoldra
```

* OE attested: **`sculdra`**. Cascade: `sċoldra`.
* **Cell-consistent match? NO** — root vowel mismatch by exactly
  the /u/→/o/ regression. The closest miss across the entire
  paradigm: right ending, wrong root vowel.
* The encoding `*skúldrǫ̂` is rejected at ProtoInput; the project
  encodes trimoric *-ō (which masc. a-stem GenPl coalesces with at
  PWGmc, R/T vol.2 §3.1.4) as `*ô`, also used for weak masc.
  n-stem NSg.

### 3.8. **DatPl `*skuldrumiz` / `*skuldrumaz` / `*skuldrum`** ← the key cell

```
=== *skúldrumiz === ProtoInput: +?
=== *skúldrumaz === ProtoInput: +?
=== *skúldrum    === ProtoInput: +?
=== *skúldrumz   === ProtoInput: +?
```

* OE attested: `sculdrum`.
* Cascade: every variant rejected at ProtoInput stage — the FST's
  input alphabet does not currently accept any DatPl-shaped form.
* **Cell-consistent match? Phonologically YES, operationally
  GATED ON FST WIDENING.** This is the only cell-pair across the
  entire paradigm survey for which the lautgesetzlich derivation
  matches the attestation. Reasoning:

  1. PGmc `*-umiz` has a high vowel `*u` in its first syllable.
     NWGmcULowering's environment is "non-high vowel in next
     syllable." A high `*u` does **not** trigger lowering.
     Therefore root /u/ is preserved.
  2. PWGmc collapses `*-umiz` → `*-um` (R/T vol.2 §3.1.6 [page
     citation needed]; Boutkan EOFL [citation needed]).
  3. OE retains `-um` unchanged in the early period (Campbell §378
     [citation needed]; Hogg §6.62 [citation needed]).
  4. So `*skuldrumiz` PGmc → `*skuldrum` PWGmc → `sculdrum` OE,
     with root /u/ preserved throughout.

  The proto-input FST simply does not have DatPl morphology in its
  input alphabet at present, because the project has historically
  templated entries on NSg/AccSg/GenSg/NApl. Widening it to accept
  `*-umiz` (or the project-internal equivalent) is well-bounded
  work — see §11 for an implementation sketch.

---

## §4. Empirical FST traces — fem. ō-stem cells

### 4.1. NSg `*skuldrō`

```
=== *skúldrō ===
NWGmcULowering: *s*k*ó*l*d*r*ō
... Epenthesis: *ʃ*ó*l*d*o*r
Surface: sċoldor
```

* OE attested heavy fem. ō-stem NSg: not robustly attested for
  this lexeme; the late-WS weak fem. `sċuldra` is analogical.
* **Cell-consistent match? N/A** (no robust strong-class
  attestation; cascade output `sċoldor` does not match the
  analogical `sċuldra` either).

### 4.2. GenSg / NApl `*skuldrōz`

(Same input as masc. a-stem NPl, §3.6.) Cascade: `sċoldre`.
**NO match** (root vowel mismatch).

### 4.3. AccSg `*skuldrǭ`, DatSg `*skuldrōi`

Both rejected at ProtoInput. **UNREACHABLE.**

### 4.4. GenPl `*skuldrǫ̂`

(Same as masc. a-stem GenPl §3.7.) Cascade: `sċoldra`. **NO
match** (root vowel).

### 4.5. DatPl `*skuldrōmiz`

Rejected. The same discussion as masc. a-stem DatPl §3.8 applies:
phonologically `sculdrum` would fall out lautgesetzlich, but
unreachable until proto-input is widened.

---

## §5. Empirical FST traces — neut. a-stem cells (hypothetical)

### 5.1. NSg/AccSg `*skuldrą`

(See §3.2.) Cascade: `sċoldor`. **NO match.**

### 5.2. NApl heavy, post-shortening `*skuldru`

```
=== *skúldru ===
WestGermanic: *s*k*ú*l*d*r*u
NWGmcULowering: *s*k*ú*l*d*r*u    ← lowering blocked (high vowel suffix)
... Epenthesis: *ʃ*ú*l*d*o*r
Surface: sċuldor
```

* OE attested NApl heavy neut. a-stem: `sculdru` / `scyldru`
  (BT, Hall) or `sculdor` (zero-NApl, Campbell §574.5
  [citation needed]).
* Cascade: `sċuldor` — root /u/ preserved (the high *u suffix
  blocks lowering), but the suffix vowel is apocopated after the
  heavy stem (Campbell §345) and parasitic /o/ is inserted between
  final `-dr` (OE epenthesis stage). So output `sċuldor`.
* **Cell-consistent match? NO** — under the BT/Hall lemma the
  attested NApl is `sculdru`, not `sċuldor`. Under the zero-NApl
  analysis (Campbell §574.5) the attested form is `sculdor` and
  this WOULD match — but the zero-NApl analysis is contested and
  does not generalise across the paradigm.
* This is the same partial-success that
  `dossier-shoulder-lautgesetz-2026.md` analysed and ultimately
  rejected (post-retraction) as cross-cell-mapping if the
  COUNTERPART is the NSg `sculdor`, and as ending-mismatch if
  the COUNTERPART is the BT-lemma NApl `sculdru`.

### 5.3. NApl light/early `*skuldrō`

Same input as fem. ō-stem NSg. Cascade `sċoldor`. **NO match.**

---

## §6. Empirical FST traces — jōn-stem and ja-stem cells

### 6.1. jōn-stem cells

```
=== *skúldrijō    === ProtoInput: +?
=== *skuldrijō    === ProtoInput: +?
=== *skúldrijōn   === ProtoInput: +?
=== *skuldrijōn   === ProtoInput: +?
=== *skuldrjōn    === ProtoInput: +?
```

All rejected. **UNREACHABLE.**

### 6.2. ja-stem masc. NSg

```
=== *skúldrijaz ===
ProtoInput: *s*k*ú*l*d*r*i*j*a*z
NWGmcULowering: *s*k*ú*l*d*r*i*j*a*z   ← lowering blocked
... ProtoToOE: *ʃ*y*l*d*r*j           ← i-umlaut: u → y
Orthography: sċyldrġ, sċyldr*ġ
Surface: +?
```

* Surface fails at orthography (no realisation of final `-rj`).
* No daughter language has a ja-stem reflex of this etymon.
* **NO match** (and not relevant: no OE attestation).

---

## §7. Empirical FST traces — ōn-stem (weak fem.) cells

Per §0.3, every ōn-stem case form is rejected at ProtoInput.
**UNREACHABLE.**

If the cascade *did* accept `*skuldrōn`, the rule chain at
`germanic.txt:1976, 2099, 2096` would give:

* `*skuldrōn` → `*skuldrǭ` (NWGmcNStemNLoss)
* + `*u` → `*o` (NWGmcULowering)
* → `*skoldrǭ` → `*skoldræ` (final `*ǭ` → `*æ` after heavy stem)
* → OE `sculdre` / cascade-style `sċoldre`

So the lautgesetzlich heavy weak fem. n-stem NSg is `sċoldre`
(NOT `sċuldra`). The attested `sċuldra` is analogical (Brunner
§252 Anm. 2 [citation needed]; Luick §247 [citation needed]).
**The ōn-stem path is not a viable cell-pair.**

---

## §8. Empirical FST traces — speculative u-stem and i-stem

```
=== *skúldruz ===
NWGmcULowering: *s*k*ú*l*d*r*u*z   ← lowering blocked
Surface: sċuldor

=== *skúldriz ===
NWGmcULowering: *s*k*ú*l*d*r*i*z   ← lowering blocked
Surface: sċylder           ← with i-umlaut u → y
```

* `*skúldruz` retains /u/ but no source proposes a u-stem for this
  etymon, so this is not a cell-consistent reconstruction.
* `*skúldriz` retains /u/ → /y/ via i-umlaut, but `sċylder` is not
  attested for this etymon.
* **N/A** for both (no source).

---

## §9. Comparative summary table — every probed cell

Columns: **Cell** (paradigm slot, cell-consistent), **Input
form**, **FST surface**, **Attested OE for that cell**, **Match?**

| Cell                                | FST input           | Surface     | Attested OE for cell          | Match? |
|-------------------------------------|---------------------|-------------|-------------------------------|--------|
| Masc. a-stem NSg                    | `*skúldraz`         | `sċoldor`   | `sculdor`                     | NO (root /o/ vs /u/) |
| Masc. a-stem AccSg                  | `*skúldrą`          | `sċoldor`   | `sculdor`                     | NO (root vowel) |
| Masc. a-stem GenSg                  | `*skúldras`         | `sċoldres`  | `sculdres`                    | NO (root vowel) |
| Masc. a-stem DatSg                  | `*skúldrai`         | `sċoldre`   | `sculdre`                     | NO (root vowel) |
| Masc. a-stem VocSg / bare-a         | `*skúldra`          | `sċoldor`   | `sculdor`                     | NO (root vowel) |
| Masc. a-stem NPl/AccPl              | `*skúldrōz`         | `sċoldre`   | `sculdras` / `sculdor`        | NO (route + root vowel) |
| Masc. a-stem GenPl                  | `*skúldrô`          | `sċoldra`   | `sculdra`                     | NO (closest miss; root vowel) |
| **Masc. a-stem DatPl**              | `*skúldrumiz`/etc.  | `+?`        | **`sculdrum`**                | **GATED — phonologically YES, FST input gate currently rejects (see §3.8 / §11)** |
| Masc. a-stem InstrPl                | (= DatPl)           | `+?`        | `sculdrum`                    | **GATED (same path as DatPl)** |
| Fem. ō-stem NSg                     | `*skúldrō`          | `sċoldor`   | (no robust strong-class attestation) | N/A |
| Fem. ō-stem AccSg                   | `*skúldrǭ`          | `+?`        | (heavy → `-e`)                | UNREACHABLE |
| Fem. ō-stem GenSg                   | `*skuldrōz`         | `sċoldre`   | (heavy → `-e`)                | NO (root vowel) |
| Fem. ō-stem DatSg                   | `*skúldrōi`         | `+?`        | (heavy → `-e`)                | UNREACHABLE |
| Fem. ō-stem NApl                    | `*skuldrōz`         | `sċoldre`   | (heavy → `-a`)                | NO (route + root vowel) |
| Fem. ō-stem GenPl                   | `*skúldrô`          | `sċoldra`   | (`-a`/`-ena`)                 | NO (root vowel) |
| **Fem. ō-stem DatPl**               | rejected            | `+?`        | `-um` (`sculdrum` if relabeled) | **GATED (same path as masc. a-stem DatPl)** |
| Neut. a-stem NSg/AccSg              | `*skúldrą`          | `sċoldor`   | (no neut. attestation)        | N/A |
| Neut. a-stem NApl heavy             | `*skúldrō`          | `sċoldor`   | (zero `sculdor` / `sculdru`)  | partial NSg-shape only |
| Neut. a-stem NApl, post-shortening  | `*skúldru`          | `sċuldor`   | `sculdru` / `scyldru` (BT)    | NO (FST `-or` vs OE `-u`) |
| jōn-stem any cell                   | various             | `+?`        | (no OE reflex)                | UNREACHABLE / N/A |
| ja-stem any cell                    | various             | `+?`        | (no OE reflex)                | UNREACHABLE / N/A |
| ōn-stem (weak fem.) any cell        | various             | `+?`        | NSg lautgesetzlich `sculdre`; `sċuldra` is analogical | UNREACHABLE |
| u-stem NSg (speculative)            | `*skúldruz`         | `sċuldor`   | (no attestation)              | N/A (no source) |
| i-stem NSg (speculative)            | `*skúldriz`         | `sċylder`   | (no attestation)              | N/A (no source) |

---

## §10. Why every NON-DatPl cell fails — the structural reason

The unifying explanation:

1. NWGmcULowering lowers root *u → o when the next syllable
   contains a non-high vowel.
2. Every PGmc/PWGmc paradigm cell of `*skuldra-` whose suffix is
   non-high (`*-az`, `*-ą`, `*-as`, `*-ai`, `*-a`, `*-ō`,
   `*-ōz`, `*-ǫ̂`, `*-ô`) feeds lowering. Output: root /o/.
   That is every cell in §§3.1–3.7, §§4.1–4.4, §§5.1, 5.3.
3. Cells with a high suffix block lowering, but:
   * `*-u` (NApl heavy, §5.2): apocopated after heavy stem; the
     cascade output is `sċuldor` with parasitic /o/, not the
     BT/Hall NApl lemma `sculdru`.
   * `*-i` (i-stem, §8): not proposed by any source for this
     etymon; would feed i-umlaut → `sċylder`, unattested.
   * **`*-umiz` (DatPl): high `*u` blocks lowering, so root /u/
     is preserved; PWGmc reduces to `*-um`; OE keeps `-um`
     unchanged. Output: `sculdrum`. This MATCHES the OE
     attested DatPl `sculdrum`. The only obstacle is the
     proto-input FST's input alphabet (§3.8, §11).**

The closest non-DatPl miss is the GenPl masc. a-stem
(`*skúldrô` → `sċoldra` against attested `sculdra`), which is
exactly one vowel feature off — the irreducible /u/→/o/
regression.

---

## §11. The DatPl path: the recommended fix

This is the substantive recommendation of this dossier.

### 11.1. Linguistic case for the DatPl

* PGmc DatPl masc. a-stem: `*skuldrumiz` (R/T vol.1 §3.2.2
  [page citation needed]; Krahe-Meid II §15 [citation needed];
  Boutkan EOFL [citation needed]).
* PWGmc DatPl: `*skuldrum` (R/T vol.2 §3.1.6 [page citation
  needed]).
* OE DatPl: `sculdrum` — attested (BT s.v. *sculdor*; Hall
  s.v. *sculdor*).
* The high `*u` in `*-umiz` blocks NWGmcULowering. The cascade's
  ulowering rule is **already** correctly conditioned ("non-high
  vowel in next syllable" — see `germanic.txt` ulowering rule
  block); no rule change is required.
* HighVowelApocope, HeavySyllableNasalApocope, ProtoToOEApocope:
  none of these would apocopate `-um` (the rule families target
  short final vowels, not VC sequences). So the cascade's
  existing apocope architecture also requires no change.
* Epenthesis: the Epenthesis rule inserts /o/ between final `-dr`
  to give `-dor`. With DatPl `-um` after the `-dr` cluster, the
  cluster is no longer word-final and Epenthesis does not fire.
  Output: `sċuldrum`.
* Orthography: `sċuldrum`, equivalent to the OE attestation
  `sculdrum` modulo the dot-above-c diacritic (cf. Hogg §3.50
  on palatal sċ-).

The cell-pair is therefore **`*skúldrumiz` (masc. a-stem DatPl)
↔ `sculdrum` (masc. a-stem DatPl)**. Cell-consistent.
Lautgesetzlich. Attested in BT and Hall under the strong
masculine paradigm.

### 11.2. FST widening sketch

The proto-input FST currently does not accept DatPl morphology.
Adding it requires:

1. **Define a new ProtoInput sub-rule** for DatPl, mapping the
   string `umiz` (and/or its allomorphs `umaz`, `um`) to the
   internal cascade representation.
2. **Verify** that subsequent stages (NWGmcULowering,
   HighVowelApocope, ProtoToOEApocope, Epenthesis, Orthography)
   already handle the resulting forms. The probe in §3.8 shows
   no later-stage rejection: the input is rejected at the very
   first stage (ProtoInput), not later. Once accepted by
   ProtoInput, the form should sail through.

A minimal, scope-limited widening would add only the masc.
a-stem DatPl `*-umiz` (other stem-class DatPls can be added in
later passes if/when other rows need them). A maximal widening
would add `*-umiz` / `*-umaz` / `*-um` (the family of attested
PGmc/PWGmc DatPl variants in R/T vol.1 §3.2.2 and vol.2 §3.1.6).

### 11.3. TSV row 2183 changes (recommended)

| Field            | Old value                      | New value (recommended)              |
|------------------|--------------------------------|---------------------------------------|
| PROTOFORM        | `*skúldrō`                     | `*skúldrumiz`                         |
| COUNTERPART (OE) | `sċuldra`                      | `sċuldrum`                            |
| Cell label       | (implicit fem. ō-stem NSg)     | masc. a-stem DatPl                    |
| Cognate set ID   | 162 (unchanged)                | 162 (unchanged)                       |
| Source note      | "Source: Wiktionary etymology" | New: "Cell-consistent masc. a-stem DatPl. R/T vol.1 §3.2.2; vol.2 §3.1.6; Campbell §378; Hogg §6.62. See `dossier-shoulder-paradigm-survey-2026.md`. Late-WS weak fem. NSg `sċuldra` is analogical (Brunner §252 Anm. 2; Luick §247) and outside the cascade's scope; the DatPl is the cell where Neogrammarian phonology converges with the attestation." |

The other three Germanic-language cognates of cognate set 162
(Du `schouder`, En `shoulder`, G `Schulter`) remain on their own
TSV rows with their own NSg PROTOFORM `*skuldrō` — relabeling row
2183 does not affect those.

### 11.4. Caveats

* The cascade's diacritic-stripping in `trace_old_english_sandbox.py`
  reduces `*skúldrumiz` to `skuldrumiz` for FST input. The acute
  stress mark is preserved in the TSV PROTOFORM column per project
  convention.
* The OE DatPl ending `-um` is sometimes spelt `-on` in late-WS
  (Campbell §378.2 [citation needed]); the canonical citation
  form per BT/Hall is `-um`. The COUNTERPART value `sċuldrum` is
  the canonical form.
* **Verification step required after FST widening:** rerun
  `trace_old_english_sandbox.py --lexeme '*skúldrumiz' --bin-dir
  /usr/app` and confirm `Surface: sċuldrum`. The rest of the
  cascade (post-ProtoInput) is hypothesised to already handle
  this form correctly, but this is the empirical step to confirm
  before merging the row change.
* **Side effect to check:** widening ProtoInput to accept
  `*-umiz` may unintentionally affect other rows whose PROTOFORMs
  end in `-um-` morpheme-internally (none currently exist in the
  TSV; verified by `grep -c 'umiz' Germanic/data/germanic-aligned-final.tsv`
  = 0 at session time).

### 11.5. Risk of widening the proto-gate

Adding DatPl morphology is a precedent-setting change. The
project's TSV currently has zero DatPl rows, and the cascade's
input language has been templated on NSg/AccSg/GenSg/NApl
morphology only. Once DatPl is accepted, future TSV editors may
choose DatPl rows for other lexemes. This is mostly a positive —
it expands the modellable paradigm coverage — but it should be
documented as a deliberate scope expansion (likely as a DEV_NOTES
entry, outside this dossier's scope).

---

## §12. Executive summary

**Across the seven proposed stem classes of `*skuldra-` and every
reachable paradigm cell, only one cell-pair yields the attested
OE form lautgesetzlich:**

> **Masc. a-stem DatPl `*skúldrumiz` → `sculdrum`**
>
> PGmc `*skuldrumiz` → PWGmc `*skuldrum` → OE `sculdrum`. The
> high `*u` in the suffix blocks NWGmcULowering, so root /u/ is
> preserved. Apocope architecture leaves `-um` intact. Epenthesis
> does not fire (the `-dr` cluster is not word-final). The
> resulting cascade output is `sċuldrum`, identical (modulo
> palatal-sċ diacritic) to the BT/Hall lemma `sculdrum`. This is
> the cell-consistent, Neogrammarian-correct repair of TSV row
> 2183.
>
> The pair is **operationally gated** only on the proto-input
> FST's input alphabet, which currently rejects every DatPl-shaped
> input (`*-umiz`, `*-umaz`, `*-um`, `*-umz`). The user has
> indicated that widening this gate is acceptable. Recommended
> minimal widening: add masc. a-stem DatPl `*-umiz` to the
> proto-input alphabet; verify by re-running the trace tool with
> `--lexeme '*skúldrumiz'` and confirming `Surface: sċuldrum`.

All other cells fail by one of three patterns:

* **Non-high suffix → /u/→/o/ regression.** NSg, AccSg, GenSg,
  DatSg, VocSg, NPl/AccPl, GenPl across all stem classes. The
  closest miss is GenPl `*skúldrô` → `sċoldra` (right ending,
  wrong root vowel) against attested `sculdra`.
* **High suffix `*-u` → apocope + epenthesis.** NApl heavy
  (`*skúldru` → `sċuldor`). Mismatches BT/Hall NApl lemma
  `sculdru`.
* **Operationally unreachable (FST input rejection).**
  jōn-stem, ja-stem, ōn-stem, AccSg fem. ō-stem, DatSg fem.
  ō-stem, GenPl-as-`*ǫ̂`, AccPl, and i-stem.

The previously recommended "wontfix" disposition (per the
retraction in `dossier-shoulder-lautgesetz-2026.md`) is therefore
**superseded** by this dossier's new finding: the DatPl cell-pair
is a cell-consistent, lautgesetzlich repair, and the only
remaining work is a small, well-bounded widening of the
proto-input FST's input alphabet — work the user has explicitly
authorised in principle.

**Recommendation: relabel TSV row 2183 as the masc. a-stem DatPl
cell-pair (`*skúldrumiz` ↔ `sċuldrum`), and widen the proto-input
FST to accept `*-umiz` (and optionally `*-umaz` / `*-um` for
allomorph coverage).** No other cells in the paradigm need
attention.
