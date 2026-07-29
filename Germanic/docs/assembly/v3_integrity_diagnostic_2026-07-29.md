# V3 Integrity Diagnostic Report

**Date:** 2026-07-29  
**Branch:** `reader-facing-gloss-audit-v3`  
**Tip SHA (remote):** `918dc2a4aac39effad23c78141f4b8c9fadd53b3`  
**Baseline (v2 checkpoint):** `0ecf63da65d82773e6d4f0bf77461c2d001337a0`

---

## 1. State summary

```
$ git log --oneline 0ecf63da..HEAD
918dc2a4 wip: add integrity layer and regression tests for Part I/II gloss validation v3
```

One commit since v2. Working tree clean.

Gateway results:

| Check | Result |
|---|---|
| `check_reader_facing_semantics.py` (regression suite) | **PASS** |
| `check_predicted_forms.py` | **PASS** |
| `check_index_verborum.py` | **PASS** |
| Part I gloss violations | **1** (see §3) |
| Part II gloss violations | **252** (see §4) |
| Total violations | **253** |

---

## 2. Commits in v3 relative to v2

```
918dc2a4  wip: add integrity layer and regression tests for Part I/II gloss validation v3
```

Files changed: 63 files, +2695 / -2005 lines.  
New files: `Germanic/tools/check_reader_facing_semantics.py`,
`Germanic/docs/book/index_semantic_fingerprint_allowlist.tsv`.

---

## 3. Part I violation — the single new case

**Form:** `*mōna*`  
**File:** `Germanic/docs/sound_changes/reader_facing/025-long-e-nasal-rounding.md`  
**Paragraph 127 of 339 Part I prose paragraphs.**

Context:

```
Before nasals, older long \emph{ē} can round toward the \emph{ō}-vocalism
seen later in *mōnaþ* 'month' and *mōna* / *mōn* 'moon'-type material.
```

Diagnosis: `*mōnaþ*` is followed immediately by `'month'` (compliant). `*mōna*` appears first in the sequence `*mōna* / *mōn* 'moon'-type`, where the gloss `'moon'` immediately follows `*mōn*`, not `*mōna*`. The validator sees `*mōna*` as the first occurrence without its own gloss.

**Genuine or false positive?** Formally genuine: `*mōna*` does lack an immediately-adjacent gloss in standard form. The two forms are listed as alternants (`/`), and `'moon'-type` follows `*mōn*`. Whether alternants sharing one gloss count as a valid convention is an editorial decision, not a validator decision. The detection is correct given the current rules. Do not fix before review.

Part I was previously at zero on the `015f3cc8` clean checkpoint (before v2 breadened the ASCII coverage slightly). The `*mōna*` detection is new in v3 due to the improved recognition of non-ASCII forms in Part I that previously had slightly different thresholds. It is not a Part I regression introduced by prose editing.

---

## 4. Part II: 252 violations

### 4.1 Coverage statistics

The combined-book validator (`capr_book_draft_alpha_01.md`) reported:

```
Part II: 1511 top-level paragraphs visited;
         759  prose paragraphs in ordinary-form scope;
         752  .recon-only paragraphs outside ordinary scope;
         366  .recon, 558 .iv, 551 plain-italic, 0 code occurrences,
         1290 first-occurrence candidates, 252 violation(s)
```

Note on "0 code occurrences": the model-entry source files contain backtick
code spans (e.g., `` `byrd` ``) for OE forms. The `build_capr_book_draft.py`
assembler converts these to italic emphasis (`_byrd_`) when writing the
combined Markdown. Therefore the assembled book sees these as plain italic
(`emph`), not `code` spans. A per-entry run of the validator directly on
source files (with Part II prefix injection) yields 339 violations across
95 entries because: (a) code spans are checked separately, and (b) per-entry
mode lacks cross-entry paragraph deduplication. The **authoritative count is 252**
from the combined book, which is the document actually validated in the build
pipeline.

### 4.2 Violations by subsection (combined book)

| Subsection | Violations |
|---|---|
| Development to Old English | 92 |
| Old English evidence | 73 |
| Reconstruction and comparative evidence | 65 |
| Form note | 9 |
| Dialect note | 7 |
| Paradigm comparison | 3 |
| Lexical note | 1 |
| Source note | 1 |
| Expected and attested forms | 1 |
| **Total** | **252** |

### 4.3 Violations by candidate category

| Category | Count |
|---|---|
| `emph` (plain italic) | 208 |
| `iv` (explicit `.iv` tag) | 44 |
| **Total** | **252** |

No `.recon` violations — the `.recon` spans currently in the corpus all have
glosses or are in non-prose sections.

### 4.4 Full violation list

The violations as reported by the combined-book validator follow. Each is on
the format `[Subsection]: form (category)`. They are identified in "Para 339"
because the validator's global paragraph counter reaches 339 by end of Part I,
and the Part II counter is a different tracked value (1511 paragraphs visited);
the "Para NNN" label in violations is the global counter at the time of the
violation, not the Part II paragraph number. This is a cosmetic reporting quirk
in the validator, not a structural error. Each violation below does correspond
to a distinct first-occurrence candidate in the corpus.

#### Reconstruction and comparative evidence (65)

```
bai* (emph)         bans* (emph)         bezen* (emph)
biegan* (emph)      borian* (emph ×2)    bōns* (emph)
bōz* (emph)         corn* (emph)         dor* (emph)
dæg* (iv)           ekkōn* (emph ×2)     faurhtei* (iv)
fogal* (emph)       foll* (emph)         fundene* (iv)
fōr* (emph)         gang* (emph)         geoguþ* (emph)
gesundrian* (emph)  grafan* (emph)       haldan* (emph)
healdan* (emph)     here* (iv)           herges* (iv)
hladan* (emph)      hīez* (emph)         iuguþ* (emph)
jugunþi* (emph)     juguþ* (emph)        kōz* (emph)
kūaz* (emph)        kūz* (emph)          liehtan* (emph)
lungen* (emph ×2)   mēd* (emph)          nahti* (emph ×2)
nahtiz* (emph)      saf* (emph)          schulder* (emph)
scilling* (emph)    smierwan* (emph)     smirwan* (emph)
sondern* (emph)     spannan* (emph)      sparro* (emph)
still* (emph)       strēzan* (emph)      swalwe* (emph)
swealwe* (emph)     tura* (emph)         vel* (emph)
wadan* (emph)       waefs* (emph)        wald* (emph)
wasp* (emph)        weald* (emph)        weraldu* (emph)
weruld* (emph)      wull* (emph)         wulle* (emph)
wīþja* (emph)
```

#### Old English evidence (73)

```
Macaþ* (emph)       berġes* (iv)         bodan* (emph)
boraþ* (emph ×2)    botm* (emph)         byrd* (emph)
bǣr* (iv)           cnoppa* (emph)       corn* (emph)
cā* (emph ×2)       cūi* (emph)          cūiz* (emph)
cūs* (emph)         cȳ* (emph)           fearn* (emph)
feld* (emph)        fell* (emph)         fern* (emph)
filatum* (emph)     gang* (emph)         gearn* (emph)
habban* (iv)        hameres* (iv)        hefzen* (iv)
helm* (emph)        helma* (emph)        helpan* (emph)
heofon* (iv)        hind* (emph)         hlid* (emph)
hliehhan* (emph)    hlihhan* (emph)      hnecca* (emph)
hwæl* (iv)          liccaþ* (iv)         lind* (emph)
liorna* (iv)        liornes* (iv)        macaþ* (iv)
nasu* (emph)        neaht* (iv)          neahtas* (iv)
neht* (iv)          nett* (emph)         nieht* (iv)
nædre* (iv)         rúst* (emph)         rūst* (emph)
sap* (emph)         slāpan* (emph)       smierwan* (emph)
smirwan* (emph)     stebn* (emph)        strewian* (emph)
strēawian* (emph)   strēgan* (emph)      sumor* (emph)
tó* (emph)          wald* (emph)         windan* (emph)
wold* (emph)        wulfai* (emph)       wulfe* (emph)
wulfi* (emph)       wulle* (emph)        wætera* (emph)
wætere* (emph)      wæteres* (emph)      wæterum* (emph)
ðistel* (iv)        ġeoguþ* (iv)
```

#### Development to Old English (92)

```
Boraþ* (emph)       Mönch* (emph)        ban* (iv)
bere* (iv)          berġes* (iv)         bān* (iv)
bēag* (iv)          būgan* (iv)          cū* (emph)
duguþ* (iv)         duru* (emph)         fearn* (emph)
funden* (iv)        fundene* (iv ×2)     giefan* (emph)
grafan* (emph)      hamer* (iv)          hamor* (iv)
hefen* (iv)         hefzen* (iv)         helpan* (emph)
heofon* (iv)        here* (iv)           herges* (iv)
hwæl* (emph)        iuzuð* (emph)        kȳi* (emph)
liornaþ* (emph)     líorna* (emph)       líornaθ* (emph)
lírnô* (emph)       lírnōθi* (emph)      líznô* (emph)
líznōθi* (emph)     macaþ* (emph)        macian* (emph)
makaθ* (emph)       makōθ* (emph)        menn* (emph)
meoloc* (emph)      meord* (emph)        mizdo* (emph)
mizdu* (emph)       munuc* (iv)          mákōθi* (emph)
méd* (emph)         mēd* (emph)          neaht* (emph)
neaxti* (emph)      niexti* (emph)       nixti* (emph)
náxti* (emph)       næxti* (emph)        rust* (emph ×2)
skáeub* (emph)      skúldramiz* (emph)   skúldrum* (emph)
skúldrumiz* (emph)  skēab* (emph)        skēaβ* (emph)
slæpan* (emph)      slāpan* (emph)       slēpan* (emph)
slǣpan* (emph)      smierwan* (emph)     smirwan* (emph)
spannan* (emph)     stefe* (emph)        streowian* (emph)
strewian* (emph)    strēawian* (emph)    strēgan* (emph)
strīeġan* (emph)    sumer* (emph)        sumor* (emph)
swīn* (emph)        syndrian* (emph)     sċuldrum* (emph)
sċēaf* (emph)       wadan* (emph)        weraldiz* (emph)
weraldu* (emph)     weruld* (emph)       willa* (emph)
wylf* (emph)        wépn* (emph)         wólfa* (emph)
wólfaz* (emph)      wúlfaz* (emph)       ēaw* (emph)
```

#### Form note (9), Dialect note (7), Paradigm comparison (3), other (3)

```
Form note:     gang*, helma*, help*, nett*, spearra*, stille*, sumeres*, sumor*, sundor*
Dialect note:  haldan*, healdan*, liehtan*, lihtan*, lyhtan*, smierwan*, smirwan*
Paradigm:      bēag* (iv), būgan* (iv), heofon* (emph)
Lexical note:  willan* (emph)
Source note:   bǣr* (iv)
Expected:      fúglaz* (emph)
```

### 4.5 Notes on potentially suspect candidates

The following warrant explicit inspection during backlog reduction:

**Development-chain stage forms** (e.g., `*náxti`, `*neaxti`, `*niexti`,
`*nixti`, `*mizdo`, `*mizdu`, `*kȳi`, `*skáeub`, `*skēab`, `*skēaβ`,
`*líznô`, `*lírnô`, `*líornô`, `*líznōθi`, `*lírnoθi`, etc.):
These are intermediate reconstructed stages in "Development to Old English"
sections. Per the established convention, full reconstructed word-forms in
prose are lexical candidates and require `.recon` + gloss. Short
phonological sub-segments (e.g., `*-um`, `*-i`) or explicit notation labels
are not. Each form in these chains must be evaluated individually: is it a
full reconstructed word-form that stands alone as a lexical unit, or is it
notational shorthand for an intermediate phonological state?

**`tó`** (Old English evidence): This was previously identified as a potential
false positive. It is not special-cased at this stage per instructions. It
appears once in the combined-book violations and represents an OE form
`tó` without gloss. Whether this is a lexical item or a directional/
prepositional abbreviation in context requires inspection of the source.

**`cū`, `cȳ`, `*kūaz`, `*kūz`, `cā`, `*cūi`, `*cūiz`, `cūs`**: These are
legitimate cow-paradigm forms. The fact that `cū` and `cȳ` appear as separate
violations demonstrates that the Unicode identity fix is working correctly —
they are NOT collapsed into the same form. Inspection of the source is needed
to confirm glossing intent for each paradigm cell.

**`slāpan`, `slæpan`, `slēpan`, `slǣpan`** in Development to Old English:
The sleep entry has multiple orthographic variants. These need individual
glossing if they are first occurrences in their paragraphs.

**`Mönch`** (German 'monk'), **`sondern`** (German 'but'), **`schulder`**
(German 'shoulder'), **`iuzuð`**, **`foll`** (German 'full'?):
These are Modern German comparative forms. They require glosses, but the
glosses should reflect the German lexical meaning, not the English entry
heading.

**`filatum`** (Latin), **`vel`** (Latin), **`tura`** (Latin): Latin
comparative forms. Require Latin lexical glosses.

**`Boraþ`** and **`Macaþ`** (capitalised): These are sentence-initial
occurrences of forms already in the corpus. They appear as violations
because the capitalised form is treated as a new identity. This is a
known validator behaviour and requires editorial decision about whether
capitalised sentence-initial forms should be exempt or explicitly glossed
the first time they appear capitalised.

---

## 5. ASCII recognition: false-positive/negative analysis

### 5.1 How ASCII forms are recognised

The validator uses `is_ascii_alpha_form(f) and has_language_cue_near(context, i)`
to determine whether a plain-italic ASCII form is a lexical candidate. A
"language cue" is any of the markers `OE`, `OHG`, `OS`, `ON`, `Goth`,
`PGmc`, `NWGmc`, `WGmc`, `PWGmc`, `OFris`, `Gothic` appearing within
approximately 120 characters of the form in the same paragraph block.

### 5.2 `faran` — genuine detection confirmed

The regression test `paragraph_fixture("Old English evidence", "OE *faran* appears without gloss.")`
expects failure (code 2) and **passes**. The form `faran` is detected as a
lexical candidate because `OE` appears immediately before it, satisfying
the language-cue condition. Glossed: `"OE *faran* 'fare' appears"` → pass.

`faran` does not appear in the 252-violation list, which means it is already
glossed everywhere it appears in the assembled corpus. The recognition
mechanism works; the absence from the violation list reflects editorial
completeness, not missed detection.

### 5.3 Ordinary English emphasis — correctly exempt

The regression test `paragraph_fixture("Old English evidence", "This is *important* evidence for chronology.")`
expects pass (code 0) and **passes**. The word `important` is all-ASCII but
has no language cue nearby, so it is not treated as a lexical candidate.

### 5.4 German/Dutch ASCII comparators

The regression test `paragraph_fixture("Reconstruction and comparative evidence", "German *fell* appears without gloss.")`
expects failure (code 2) and **passes**. The word `German` before `*fell*`
satisfies the language-cue requirement (`German` is in the expanded cue list).

This confirms the mechanism is sound. However, inspection of actual
violations like `foll`, `still`, `sondern`, `schulder`, `dor`, `tura`,
`vel`, `lungen`, etc. in "Reconstruction and comparative evidence" is needed
to determine whether each occurrence has a detectable language cue in context
or whether some are detected by the non-ASCII path only.

---

## 6. Regression coverage matrix

For every problem listed in the v3 brief, the protecting test and pass/fail status:

| Problem | Test / check | Status |
|---|---|---|
| **SC057 unmarked counterfactuals** (`bēaġan`, `sōċan`) | `check_predicted_forms.py` corpus scan + `run_known_entry_checks()` fixture | **PASS** |
| **Unmarked counterfactual pattern** `yields *wrong* rather than expected` | `run_predicted_fixtures()` fixture 1 | **PASS** |
| **Glossed counterfactual** `yields *wrong* 'gloss' rather than expected` | `run_predicted_fixtures()` fixture 2 | **PASS** |
| **Marked counterfactual** `[*wrong*]{.pred}` passes | `run_predicted_fixtures()` fixture 3 | **PASS** |
| **`.pred` with gloss fails** `[*wrong*]{.pred} 'gloss'` | `run_predicted_fixtures()` fixture 4 | **PASS** |
| **Ordinary historical input, no `.pred`** passes | `run_predicted_fixtures()` fixture 5 | **PASS** |
| **`+?` uncertainty notation** passes without dagger | `run_predicted_fixtures()` fixture 6 | **PASS** |
| **SC057 `bēaġan` case** specifically | `check_predicted_forms.py` (no unmarked counterfactual in SC057 source) | **PASS** |
| **SC057 `sōċan` case** specifically | `check_predicted_forms.py` (no unmarked counterfactual in SC057 source) | **PASS** |
| **Unicode `cū` vs `cȳ` distinct** | `run_unicode_ascii_fixtures()` fixture 1 (cū then cȳ → fail) | **PASS** |
| **`nǣdl` vs `nædl` distinct** | `run_unicode_ascii_fixtures()` fixture 2 | **PASS** |
| **Exact `cū` twice in paragraph** passes | `run_unicode_ascii_fixtures()` fixture 3 | **PASS** |
| **`cū` in new paragraph** fails | `run_unicode_ascii_fixtures()` fixture 4 | **PASS** |
| **`.recon` repeated in same paragraph** passes | `run_unicode_ascii_fixtures()` fixture 5 | **PASS** |
| **ASCII `faran` without gloss** fails | `run_unicode_ascii_fixtures()` ASCII fixture 1 | **PASS** |
| **ASCII `faran 'fare'`** passes | `run_unicode_ascii_fixtures()` ASCII fixture 2 | **PASS** |
| **German comparator without gloss** fails | `run_unicode_ascii_fixtures()` ASCII fixture 3 | **PASS** |
| **Ordinary English emphasis** not lexical | `run_unicode_ascii_fixtures()` ASCII fixture 4 | **PASS** |
| **Phonological `ēo`, `ēa`, `*ai` notation** — are these tested? | Not explicitly in `run_unicode_ascii_fixtures()`; excluded by `is_notation_only()` function | **covered by corpus behaviour; no dedicated fixture** |
| **Malformed `.recon` `[nasō ... OE nasu]{.recon}`** fails | `run_recon_duplicate_fixtures()` and `run_corpus_lints()` | **PASS** |
| **`.recon` with leading star `[*júką]{.recon}`** fails | `run_recon_duplicate_fixtures()` fixture 2 | **PASS** |
| **`.recon` chain `[náxti > niht]{.recon}`** fails | `run_recon_duplicate_fixtures()` fixture 3 | **PASS** |
| **`.recon` with embedded gloss** fails | `run_recon_duplicate_fixtures()` fixture 4 | **PASS** |
| **Valid `.recon` forms pass** | `run_recon_duplicate_fixtures()` positive fixtures | **PASS** |
| **Duplicate glosses `'night' 'night'`** detected and absent | `run_known_entry_checks()` + `run_corpus_lints()` | **PASS** |
| **Duplicate glosses `'fowl' 'fowl'`** detected and absent | `run_known_entry_checks()` + `run_corpus_lints()` | **PASS** |
| **`nose` overbroad `.recon` span removed** | `run_known_entry_checks()`: `[nasō ... OE nasu]{.recon}` not present | **PASS** |
| **`water` stray `[*` fragment removed** | `run_known_entry_checks()`: `[*` not present in water entry | **PASS** |
| **`stem` semantic relabel** | `run_known_entry_checks()`: `voice, sound` present in stem entry | **PASS** |
| **`.pred` no-gloss corpus policy** (all SC files) | `run_known_entry_checks()` corpus scan of `reader_facing/*.md` | **PASS** |
| **`slǣpan` line-number regression replaced** | `run_index_fingerprint_checks()` semantic invariant (path-based, not line-based) | **PASS** |
| **Index line-number changes do not trigger failure** | `run_index_fingerprint_checks()`: `_semantic_key()` ignores `:NN` suffix | **PASS** |
| **Index stability under gloss-only edits** | `run_index_fingerprint_checks()`: fingerprint delta against `0ecf63da` + allowlist | **PASS** |
| **Adding `.iv` changes semantic index membership** | `run_index_fingerprint_checks()` scope-shift fixture | **PASS** |
| **Part II coverage statistics accurately split** | `run_stats_regression()`: all three sub-counts present in output | **PASS** |
| **`.pred` style-guide prohibition documented** | `Germanic/docs/style_guide.md` updated | confirmed |

**Gap identified:** No dedicated fixture for phonological notation `ēo`, `ēa`, `*ai` being nonlexical. These are excluded by `is_notation_only()` which tests for short forms matching a hardcoded set of phonological patterns. The exclusion works in corpus practice but lacks an explicit regression fixture in `check_reader_facing_semantics.py`. This should be added before backlog reduction.

---

## 7. SC057 counterfactuals: `bēaġan` and `sōċan`

Source: `Germanic/docs/sound_changes/reader_facing/057-j-cluster-coalescence.md`

Current state (lines 29–30):

```markdown
PGmc [báugijaną]{.recon} 'bow' yields [*bēaġan*]{.pred} rather than expected OE *bīeġan*,
and PGmc [sōkijaną]{.recon} 'seek' yields [*sōċan*]{.pred} rather than expected *sēċan*.
```

Both counterfactual outputs carry `.pred`. Neither is glossed. `check_predicted_forms.py`
passes with zero unmarked counterfactuals. The SC057 regression is protected.

---

## 8. `.pred` policy

Firm convention as documented in `Germanic/docs/style_guide.md`:

> A counterfactual predicted output (`.pred`) is daggered in PDF output and
> **must not carry an English lexical gloss**. A `.pred` span with an
> immediately following gloss in single or curly quotes is a policy violation
> and will fail `check_predicted_forms.py`.

The `check_predicted_forms.py` enforcer:
- Detects `yields *X* rather than expected` → FAIL (unmarked counterfactual)
- Detects `yields *X* 'gloss' rather than expected` → FAIL
- Detects `[*X*]{.pred} 'gloss'` → FAIL (`.pred` with gloss)
- Passes `[*X*]{.pred} rather than expected` (correctly marked, no gloss)
- Passes ordinary historical inputs and attested targets

Additional SC fixes in v3: SC055–056 received `.pred` markers for `sǣw`,
`ċȳ`, `lunġen`, `ġieft`, `sċǣþ` in
`Germanic/docs/sound_changes/reader_facing/055-056-i-umlaut-core.md` and
`Germanic/docs/sound_changes/reader_facing/053-054-*.md`.

---

## 9. Unicode-safe paragraph identity

The validator normalises form identity by:

1. Stripping leading reconstruction asterisks (so `*cū` and `cū` collapse
   for repeat-detection but `cū` and `cȳ` remain distinct).
2. NOT stripping diacritics or lowercasing (the old `gsub("[^%w]", "")` approach
   was removed). Non-ASCII distinguishing characters are preserved.

Regression fixture confirms: `cū 'cow'` then `cȳ` in the same paragraph → `cȳ` fails (as expected). `nǣdl` and `nædl` remain distinct.

---

## 10. `stem` entry: disposition of semantic conflict

### What the conflict was

Entry `2216-stem-stefn.model.md` was headed `# stem — OE stefn` with all
internal forms glossed `'stem'`. But Clark Hall, Ringe & Taylor, Orel,
Kroonen, Fulk, Bülbring, and Luick all consistently gloss OE `stefn / stemn`
as 'voice, sound'. The comparative citation label `*stámnaz` belongs to
the 'stem/trunk' semantic family — a different lexical item. The entry had
conflated the comparative metadata label with the lexical analysis of the OE
target form.

### What v3 changed

**This is a scientific/lexical correction, not only a markup repair.**

Specific changes:
- Entry heading changed: `# stem — OE stefn` → `# voice/sound — OE stefn (legacy row label: stem)`
- Metadata field `lexical item` changed: `stem` → `voice, sound (legacy row label: stem)`
- All internal glosses changed from `'stem'` to `'voice, sound'` throughout
  "Reconstruction and comparative evidence", "Old English evidence", and
  "Development to Old English" sections
- `stámnaz` is now explicitly described as "background metadata from the legacy
  row heading" that "should not control the lexical gloss of the OE evidence line"
- `stébnō` and its development stages are consistently glossed `'voice, sound'`
- The note that `stámnaz` belongs to "a different semantic family" is explicit

The claim "scientific baseline unchanged" would be **false**. The v3 change
is deliberate: the lexical analysis of entry `stefn` has been corrected.
The 7-mismatch OE scientific baseline (0 actionable phonology) is not
affected because `stefn` is classified as `early_analogy`, not a phonological
mismatch. The correction is editorial/lexical, not phonological.

### Index fingerprint

`stámnaz` (pgmc, source_protoform, explicit_tag) was removed from the index
fingerprint. This change is in `index_semantic_fingerprint_allowlist.tsv`
with note: "Stem/voice conflation corrected; lexical source_protoform
semantics revised." This is intentional.

---

## 11. Entries 2310–2314 and 2227: rewrite classification

For each entry the question is: **serialization-corruption repair** vs.
**editorial rewriting of reader-facing linguistic content**.

### 2310 — make (3sg) macaþ

**Primary change: serialization-corruption repair.**

The v2 batch edit produced sequences like:
```
Campbell's class-II paradigm makes the ordinary 3sg ending **`-aþ[*, while
his dialect survey allows secondary **]{.recon} 'make (3sg)'-e-[*...
```
— an unclosed backtick, a disconnected `]{.recon}`, and a split form.

v3 rewrote this entry to clean the corruption. Minor prose refinements:
- `makon` gloss changed from `'make (3sg)'` to `'make'` (semantic correction)
- `mákōθi` gloss changed from `'make (3sg)'` to `'makes'` (form-sensitive correction)
- Some forms moved from `.recon` markup to code spans (where appropriate)

**One editorial change with index consequence:** `makon` (OS, comparison_form)
was in the index as an explicit-tag form; after rewrite it is no longer
explicit-tagged. Allowlisted as intentional.

### 2311 — bore (iptv.2sg) bora

**Primary change: serialization-corruption repair.** Broken markup fragments like
`]{.recon} 'bore (iptv.2sg)'borian` removed. Prose structure restored.
No change to linguistic content. Glosses and forms remain the same
(except standardisation of `'bore (iptv.2sg)'` gloss format).

### 2312 — bore (3sg) boraþ

**Primary change: serialization-corruption repair.** Broken inline `.recon`
fragments cleaned. Gloss `'bore (3sg)'` standardised to `'bores'` throughout
(form-sensitive correction: the 3sg present form means 'bores', not 'bore').
No change to linguistic or etymological content.

### 2313 — learn (iptv.2sg) liorna

**Primary change: serialization-corruption repair.** Duplicate gloss
`'learn' 'learn (iptv.2sg)'` → single `'learn (iptv.2sg)'`.
Broken markup in Brunner citation paragraph restored. No change to
linguistic or source-citation content.

### 2314 — learn (3sg) liornaþ

**Primary change: serialization-corruption repair.** Duplicate gloss
`'learns' 'learn (3sg)'` on `líznōθi` → single `'learns'`.
Broken `.recon` fragment in Brunner/Clark Hall paragraph restored.
No change to etymological content.

### 2227 — strew strīeġan

**Mixed: serialization-corruption repair plus one semantic correction.**

Corruption repaired: duplicate glosses `'strew' 'strew'` on `strauwjan`,
`kauwjan`, `striegan`, `straujana` removed.

Semantic correction: `kauwjan` gloss changed from `'strew'` (inherited from
the entry heading via batch edit) to `'chew'`. This is correct: PGmc
`*kawwjaną` is 'chew', not 'strew'. The duplicate-gloss batch had propagated
the wrong meaning from the `strew` entry heading.

One consequence: `strēzan` (OE, comparison_form) was a broad-prose-decision
index candidate. The entry rewrite removed the broad-prose context that had
generated this candidate. Allowlisted as intentional.

---

## 12. `.recon` corpus lint

**Method:** Python regex `\[([^\]]*)\]\{\.recon\}` over all
`*.model.md` files. Note: the Python character class `[^\]]` matches
newlines, so the regex can produce spurious cross-paragraph matches.

**Results:**

| Category | Count |
|---|---|
| Total `.recon` spans found | 544 |
| Spans with structural issues (regex report) | 4 |
| Of those: genuine structural failures | **0** |
| Of those: regex false positives (cross-line match artefacts) | **4** |

### The 4 reported spans

All 4 occur in entries `2252-thousand-þūsend`, `2258-timber-timber`, and
`2268-wake-wacan`. In each case the regex matches a long cross-paragraph
string because a literal `[` in backtick prose (not in a `.recon` span)
precedes an actual empty `[]{.recon}` span later in the same block. The
matched "span content" is prose text starting with `*` (the leading-star
heuristic fires) but the matched region is not actually a `.recon` span
— it is the gap between an opening `[` in inline code and the following
`]{.recon}` tag.

However, these three entries **do contain genuinely malformed markup**
introduced by v2 batch edits, independent of the `.recon` regex results:

- `2252-thousand-þūsend.model.md` lines 40 and 46: empty `[]{.recon}`
  spans followed by `'thousand'*þȳsend` — the OE comparison form `þȳsend`
  was supposed to be inside an `.iv` span but the `.iv` closing bracket
  was broken, leaving an empty `.recon` and a dangling form outside markup.
- Similarly in `2258-timber-timber` and `2268-wake-wacan`.

**These are v2 corruption survivors that were not caught by v3.**
The `check_reader_facing_semantics.py` corpus lint did not detect them because
the `find_recon_span_issues()` function requires spans with `content.startswith('*')`
or `' OE '` inside, and empty spans (`[]`) do not trigger those checks.

**Action required:** Entries 2252, 2258, and 2268 contain residual v2
serialization corruption (empty `.recon` spans with broken `.iv` spans).
These were not fixed in v3. They should be added to the known-entry checks
in `check_reader_facing_semantics.py` and repaired before backlog reduction.

The `run_corpus_lints()` function in the regression suite should add an
explicit check for empty-content `.recon` spans (`[]{.recon}`).

---

## 13. Index fingerprint delta: v2 → v3

The `index_semantic_fingerprint_allowlist.tsv` records 4 intentional changes:

| Language | Form | Role | Change | Source file | Justification |
|---|---|---|---|---|---|
| `oe` | `strēzan` | `comparison_form` | **removed** from broad-prose index | `2227-strew-strīeġan` | Entry rewrite removed broad-prose candidate context |
| `os` | `makon` | `comparison_form` | **removed** from explicit-tag index | `2310-make-(3sg)-macaþ` | Corrupt markup rewritten; `.iv` tag removed with corruption |
| `pgmc` | `skuldr(j)ō` | `source_protoform` | **removed** from explicit-tag index | `2183-shoulder-sċuldrum` | Uncertain parenthesised notation removed from `.iv` span |
| `pgmc` | `stámnaz` | `source_protoform` | **removed** from explicit-tag index | `2216-stem-stefn` | Stem/voice conflation corrected; comparative label relegated to background metadata |

**Net effect:** 4 forms removed from the semantic index (no additions).

All 4 are allowlisted as intentional. `check_index_verborum.py` passes.
The `run_index_fingerprint_checks()` in `check_reader_facing_semantics.py`
confirms no unallowlisted delta.

**Characterisation:**
- `strēzan` removal: acceptable consequence of removing broken prose context
- `makon` removal: acceptable consequence of removing corrupted `.iv` tagging
- `skuldr(j)ō` removal: correct — parenthesised notation `(j)` is not a
  valid lexical form and should not be in the index
- `stámnaz` removal: **this is a semantic change** — the entry now treats
  `stámnaz` as background comparative metadata, not as the primary OE-facing
  selected input. The OE-facing analysis is now `stébnō` (voice/sound), which
  retains its `.iv` tag and index membership. Net: `stámnaz` out, `stébnō`
  continues to be indexed (no new entry, existing one retained).

---

## 14. Validator statistics: accuracy of Part II reporting

The combined-book summary:

```
Part II: 1511 top-level paragraphs visited;
         759  prose paragraphs in ordinary-form scope;
         752  .recon-only paragraphs outside ordinary scope;
```

This correctly separates:
- `1511` = total top-level Para blocks processed in Part II mode
- `759`  = paragraphs inside PROSE_SECTIONS allowlist (where ordinary-form
           checking applies)
- `752`  = paragraphs in Part II but outside PROSE_SECTIONS allowlist
           (where only `.recon` is checked)

Sum: 759 + 752 = 1511. ✓ The three counts are exhaustive and non-overlapping.

The `run_stats_regression()` test confirms all three labels appear in output.

---

## 15. Known residual issues not yet fixed in v3

The following issues were identified during this report and are NOT yet
addressed. They should be fixed before further backlog reduction:

1. **`2252-thousand-þūsend.model.md`** (lines 40, 46): empty `[]{.recon}`
   spans with broken surrounding `.iv` markup. Residual v2 corruption.

2. **`2258-timber-timber.model.md`** and **`2268-wake-wacan.model.md`**:
   similar pattern of broken `.iv` spans adjacent to empty `.recon` spans.

3. **Missing fixture for `ēo`, `ēa`, `*ai` notation exclusion**: the
   `is_notation_only()` function handles these correctly in corpus practice
   but there is no dedicated regression fixture in
   `check_reader_facing_semantics.py` asserting they remain non-lexical.

4. **`run_corpus_lints()` missing empty-span check**: `[]{.recon}` (empty
   content) should be detected as malformed and fail the corpus lint.

5. **Capitalised sentence-initial forms** (`Boraþ`, `Macaþ`) appear as
   violations because the validator treats them as orthographically distinct
   from lower-case forms. This needs an explicit editorial policy: either
   normalise case in paragraph identity, or accept that these require a
   separate gloss.

---

## 16. Final git status

```
$ git status
On branch reader-facing-gloss-audit-v3
nothing to commit, working tree clean
```

```
$ git log --oneline 0ecf63da..origin/reader-facing-gloss-audit-v3
918dc2a4 wip: add integrity layer and regression tests for Part I/II gloss validation v3
```

Remote tip SHA: **`918dc2a4aac39effad23c78141f4b8c9fadd53b3`**

Preserved: `reader-facing-gloss-audit-v2` at `0ecf63da65d82773e6d4f0bf77461c2d001337a0` — unchanged.
