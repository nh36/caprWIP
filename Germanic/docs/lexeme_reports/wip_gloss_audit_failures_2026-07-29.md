# WIP: Paragraph-gloss validator failure report — 2026-07-29

> **TEMPORARY DIAGNOSTIC — WIP BRANCH ONLY**
>
> This file must be **removed** before any merge to `update` or `reader-facing-conventions-audit`.
> It records the current failure state for independent inspection on `reader-facing-gloss-audit-wip`.

## Context

- Branch: `reader-facing-gloss-audit-wip`
- Based on: `reader-facing-conventions-audit` @ `015f3cc8`
- Starting failures: Part I 3, Part II 123 (126 total, first build of this session)
- Failures fixed in this session: Part I 3 (all resolved), Part II 14 (via source edits and one narrow validator exclusion)
- **Current state before this commit**: Part I 0 / Part II 109 (index-verborum check also failing; see below)
- Full build **does not pass** in this commit — this is a WIP checkpoint

---

## Current paragraph-gloss validator results

**Build that last reported clean Part I + 109 Part II violations:**
(from the build prior to the `slǣpan` markup edit — see index failure section below)

```
Paragraph gloss validator:
  Part I:  339 prose paragraphs, 415 Emph/iv/recon occurrences, 375 first-occurrence candidates, 0 violation(s)
  Part II: 1514 prose paragraphs in scope, 298 .recon, 598 .iv, 374 plain-italic, 0 code occurrences, 995 first-occurrence candidates, 109 violation(s)
  Total violations: 109
```

### Part I violations: 0 (resolved in this session)

The three Part I violations that appeared were:

- Para 21: `*OEIUmlaut*` — validator rule-label exclusion narrowed (was non-ASCII mixed-case catching rule names)
- Para 242: `` *báugijaną* `` — migrated from Code span to `.recon` in `057-j-cluster-coalescence.md`
- Para 242: `` *sōkijaną* `` — same migration

### Part II violations: 109 remaining

Full list as reported (Part II paragraph numbers are within the assembled book's Part II section):

```
Para 177 [Form note]: missing gloss for *forlēosan* (emph)
Para 221 [Old English evidence]: missing gloss for *ġiest* (emph)
Para 324 [Form note]: missing gloss for **xlídą* (emph)
Para 349 [Old English evidence]: missing gloss for **meluk* (emph)
Para 358 [Old English evidence]: missing gloss for *mōdor* (emph)
Para 393 [Reconstruction and comparative evidence]: missing gloss for **skap* (emph)
Para 393 [Reconstruction and comparative evidence]: missing gloss for *scéap* (emph)
Para 421 [Old English evidence]: missing gloss for *slēp* (emph)
Para 421 [Old English evidence]: missing gloss for *slēap* (emph)
Para 421 [Old English evidence]: missing gloss for *slēpon* (emph)
Para 421 [Old English evidence]: missing gloss for *slēpen* (emph)
Para 423 [Form note]: missing gloss for *slēap* (emph)
Para 474 [Reconstruction and comparative evidence]: missing gloss for **sunþraz* (emph)
Para 474 [Reconstruction and comparative evidence]: missing gloss for **sunþrjanan* (emph)
Para 501 [Old English evidence]: missing gloss for *þencan* (emph)
Para 501 [Old English evidence]: missing gloss for *geþencan* (emph)
Para 510 [Old English evidence]: missing gloss for *þorn* (emph)
Para 548 [Development note]: missing gloss for *wæden* (emph)
Para 575 [Lexical note]: missing gloss for *wēox* (emph)
Para 626 [Reconstruction and comparative evidence]: missing gloss for **garna* (emph)
Para 626 [Reconstruction and comparative evidence]: missing gloss for **geern* (emph)
Para 626 [Reconstruction and comparative evidence]: missing gloss for **gearn* (emph)
Para 644 [Reconstruction and comparative evidence]: missing gloss for *tȳn* (emph)
Para 649 [Development to Old English]: missing gloss for *tīen* (emph)
Para 658 [Old English evidence]: missing gloss for *þry* (emph)
Para 706 [Development to Old English]: missing gloss for *ēo* (emph)
Para 709 [Formation comparison]: missing gloss for *brēost* (iv)
Para 730 [Formation comparison]: missing gloss for *dile* (iv)
Para 743 [Class comparison]: missing gloss for *festan* (iv)
Para 756 [Formation comparison]: missing gloss for *flasce* (iv)
Para 769 [Class comparison]: missing gloss for *fylġan* (iv)
Para 769 [Class comparison]: missing gloss for *folgian* (iv)
Para 782 [Stem comparison]: missing gloss for *ġealla* (emph)
Para 854 [Reconstruction and comparative evidence]: missing gloss for **nabulō* (emph)
Para 854 [Reconstruction and comparative evidence]: missing gloss for **næbula* (emph)
Para 858 [Development to Old English]: missing gloss for **nabulō* (emph)
Para 858 [Development to Old English]: missing gloss for **næbula* (emph)
Para 878 [Reconstruction and comparative evidence]: missing gloss for **nēþlō* (emph)
Para 878 [Reconstruction and comparative evidence]: missing gloss for *nédl* (emph)
Para 882 [Development to Old English]: missing gloss for **nēþlō* (emph)
Para 882 [Development to Old English]: missing gloss for *nédl* (emph)
Para 890 [Reconstruction and comparative evidence]: missing gloss for **nusō* (emph)
Para 894 [Development to Old English]: missing gloss for **nósu* (emph)
Para 902 [Reconstruction and comparative evidence]: missing gloss for **saf* (emph)
Para 902 [Reconstruction and comparative evidence]: missing gloss for *sæp* (emph)
Para 913 [Reconstruction and comparative evidence]: missing gloss for **sawi* (emph)
Para 913 [Reconstruction and comparative evidence]: missing gloss for **sei* (emph)
Para 914 [Old English evidence]: missing gloss for **sǣi* (emph)
Para 915 [Development to Old English]: missing gloss for **sáiwiz* (emph)
Para 915 [Development to Old English]: missing gloss for **sāwiz* (emph)
Para 915 [Development to Old English]: missing gloss for **sāwi* (emph)
Para 915 [Development to Old English]: missing gloss for **sāi* (emph)
Para 915 [Development to Old English]: missing gloss for *sǣ* (emph)
Para 925 [Development to Old English]: missing gloss for **síβi* (emph)
Para 925 [Development to Old English]: missing gloss for **síβe* (emph)
Para 943 [Development to Old English]: missing gloss for **stábaz* (emph)
Para 943 [Development to Old English]: missing gloss for **stába* (emph)
Para 943 [Development to Old English]: missing gloss for **stáb* (emph)
Para 943 [Development to Old English]: missing gloss for *stæf* (emph)
Para 1038 [Reconstruction and comparative evidence]: missing gloss for **wīþja* (emph)
Para 1050 [Reconstruction and comparative evidence]: missing gloss for **weraldu* (emph)
Para 1050 [Reconstruction and comparative evidence]: missing gloss for **weruld* (emph)
Para 1055 [Development to Old English]: missing gloss for **weraldiz* (emph)
Para 1055 [Development to Old English]: missing gloss for **weraldu* (emph)
Para 1055 [Development to Old English]: missing gloss for **weruld* (emph)
Para 1063 [Reconstruction and comparative evidence]: missing gloss for **jugunþi* (emph)
Para 1063 [Reconstruction and comparative evidence]: missing gloss for **juguþ* (emph)
Para 1063 [Reconstruction and comparative evidence]: missing gloss for *geoguþ* (emph)
Para 1063 [Reconstruction and comparative evidence]: missing gloss for *iuguþ* (emph)
Para 1096 [Reconstruction and comparative evidence]: missing gloss for *ēa* (emph)
Para 1102 [Paradigm comparison]: missing gloss for *bēag* (iv)
Para 1102 [Paradigm comparison]: missing gloss for *būgan* (iv)
Para 1108 [Reconstruction and comparative evidence]: missing gloss for **kōz* (emph)
Para 1109 [Reconstruction and comparative evidence]: missing gloss for **kūaz* (emph)
Para 1109 [Reconstruction and comparative evidence]: missing gloss for **kūz* (emph)
Para 1110 [Old English evidence]: missing gloss for *cūs* (emph)
Para 1110 [Old English evidence]: missing gloss for **cūi* (emph)
Para 1110 [Old English evidence]: missing gloss for **cūiz* (emph)
Para 1115 [Paradigm comparison]: missing gloss for *cȳ* (emph)
Para 1140 [Paradigm comparison]: missing gloss for *fyrhte* (iv)
Para 1208 [Development to Old English]: missing gloss for **mizdo* (emph)
Para 1208 [Development to Old English]: missing gloss for **mizdu* (emph)
Para 1208 [Development to Old English]: missing gloss for *méd* (emph)
Para 1217 [Reconstruction and comparative evidence]: missing gloss for **nahti* (emph)
Para 1221 [Development to Old English]: missing gloss for **náxti* (emph)
Para 1221 [Development to Old English]: missing gloss for **neaxti* (emph)
Para 1221 [Development to Old English]: missing gloss for **niexti* (emph)
Para 1221 [Development to Old English]: missing gloss for **nixti* (emph)
Para 1230 [Old English evidence]: missing gloss for *tó* (emph)
Para 1247 [Development to Old English]: missing gloss for **skúldramiz* (emph)
Para 1247 [Development to Old English]: missing gloss for **skúldrumiz* (emph)
Para 1247 [Development to Old English]: missing gloss for **skúldrum* (emph)
Para 1247 [Development to Old English]: missing gloss for *sċuldrum* (emph)
Para 1249 [Paradigm comparison]: missing gloss for *sculdrum* (iv)
Para 1257 [Development to Old English]: missing gloss for **skáeub* (emph)
Para 1257 [Development to Old English]: missing gloss for **skēab* (emph)
Para 1257 [Development to Old English]: missing gloss for **skēaβ* (emph)
Para 1257 [Development to Old English]: missing gloss for *sċēaf* (emph)
Para 1258 [Paradigm comparison]: missing gloss for *sċēaf* (emph)
Para 1334 [Development to Old English]: missing gloss for **líznô* (emph)
Para 1334 [Development to Old English]: missing gloss for **lírnô* (emph)
Para 1346 [Development to Old English]: missing gloss for **líznōθi* (emph)
Para 1346 [Development to Old English]: missing gloss for **lírnōθi* (emph)
Para 1422 [Reconstruction and comparative evidence]: missing gloss for *hīez* (emph)
Para 1434 [Reconstruction and comparative evidence]: missing gloss for **fōr* (emph)
Para 1475 [Expected and attested forms]: missing gloss for **fúglaz* (emph)
Para 1484 [Old English evidence]: missing gloss for *rūst* (emph)
Para 1499 [Development to Old English]: missing gloss for **wúlfaz* (emph)
Para 1499 [Development to Old English]: missing gloss for **wólfa* (emph)
```

---

## Index-verborum failure (current blocker)

The most recent build attempt failed in `check_index_verborum.py` before reaching the paragraph-gloss validator:

```
Traceback (most recent call last):
  File "Germanic/tools/check_index_verborum.py", line 1097, in <module>
    main()
  File "Germanic/tools/check_index_verborum.py", line 1087, in main
    assert_broad_prose_buckets()
  File "Germanic/tools/check_index_verborum.py", line 694, in assert_broad_prose_buckets
    assert ("slǣpan", "Germanic/docs/lexeme_reports/model_entries/2196-sleep-slǣpan.model.md:25") in same_entry_pairs
AssertionError
```

### Cause

The `2196-sleep-slǣpan.model.md` Old English evidence prose was edited to wrap
preterite forms (`slēp`, `slēap`, `slēpon`, `slēpen`) and the infinitive target
(`slǣpan`) in explicit `.iv` markup in order to satisfy the paragraph-gloss validator.

The index-verborum auditor contains a regression assertion that the plain-text
(non-indexed) form `slǣpan` appears at **source line 25** of that file, where
the audit expects it in the "Already indexed in same entry" bucket.

### Questions for inspection

1. Does the same-entry witness still exist in the file at a different line?
   (It does — `slǣpan` appears multiple times; the assertion uses a specific
   line number `25` which may have shifted or the form may now be marked `.iv`
   rather than plain text.)

2. Should the regression assertion be made line-number-agnostic while still
   testing the semantic invariant (that `slǣpan` appears at least once in plain
   prose within the same entry)?

3. Is the audit's "Already indexed in same entry" bucket even the right bucket
   if the form is now explicitly marked `.iv`? The edit may have made the form
   the preferred indexed form rather than a broad prose suggestion.

4. Would regenerating the index-verborum audit tables resolve the assertion
   (because the generated `index_verborum_broad_prose_suggestions.tsv` would
   no longer contain `slǣpan` at line 25)?

### Do not change source or test to resolve this until inspected

Per instructions: do not restore raw markup or rearrange prose solely to
recreate line 25. Preserve the semantically correct state and resolve the
regression fixture question first.

---

## Session summary: changes made in this pass

### Validator changes (`Germanic/tools/paragraph_gloss_validator.lua`)

- Added `has_non_ascii()` and `looks_like_linguistic_form()` helpers moved to
  module scope (were accidentally nested inside `utf8_len()`)
- Part I: Code spans checked only if non-ASCII (excludes rule labels like
  `*ijo`, `*iu` which are pure-ASCII phonological notation)
- Part I/II: Plain italic `Emph` filtered through `looks_like_linguistic_form()`
  so that English-word emphasis (e.g. *shoulder*, *four*, *you*) is not counted
  as a lexical candidate
- Added exclusion: bare forms matching `^[A-Z][A-Za-z]+$` (rule labels, PGmc
  abbreviations) are treated as notation-only
- Added exclusion for short diacritic-only sequences (`*ēo`, `*ēa`) as 2-codepoint
  notation

### Part I source changes

- `Germanic/docs/sound_changes/reader_facing/057-j-cluster-coalescence.md`:
  Migrated `` `*báugijaną` `` and `` `*sōkijaną` `` from Code spans to `.recon`
  spans (eliminates Part I validator false positives for Para 242)

### Part II source changes (canonical model entries)

- `1958-both-bū.model.md`: Added glosses to `bām` / `bēġra` in Old English
  evidence paragraph (paradigm list now has inline glosses)
- `1961-bow-bīeġan.model.md`: Wrapped `biegan`/`bigan`/`bīeġan` in `.iv` spans
  with explicit glosses in all three prose sections
- `1969-breeches-brēċ.model.md`: Wrapped `brōc`/`brēc`/`brōkiz`/`breeci`/`bréc`
  in `.iv`/`.recon` spans; retained PNWGmc stage phrase required by lexical-volume
  regression assertion
- `2022-fly-flēogan.model.md`: Wrapped all fly-family forms in `.iv` spans with
  explicit per-form glosses
- `2028-forlorn-lēosan.model.md`: Wrapped OE forms in `.iv` spans with glosses;
  removed unsupported `lang=got` Gothic annotation
- `2049-guest-ġiest.model.md`: Wrapped all guest-family OE forms in `.iv` spans
  with glosses
- `2057-harvest-hierfest.model.md`: Wrapped harvest forms in `.iv` spans with
  per-form glosses
- `2196-sleep-slǣpan.model.md`: Wrapped preterite and infinitive forms in `.iv`
  spans — **this edit triggered the index-verborum regression**

---

## Remaining 109 Part II failures — preliminary classification

Many are in development-chain paragraphs where intermediate stage forms are
listed in prose without glosses. Classification by entry:

| Entry | Forms | Classification |
|-------|-------|----------------|
| lid (2100) | `*xlídą` | Form note — reconstructed lexical form, needs `.recon` |
| milk (2126) | `*meluk` | Reconstruction evidence — reconstructed lexical form |
| mother (2129) | `mōdor` | OE evidence — ordinary attested OE form |
| sheep (2179) | `*skap`, `scéap` | Reconstruction evidence — lexical forms |
| sleep (2196) | `slēp`, `slēap`, `slēpon`, `slēpen` | OE evidence — preterite paradigm forms |
| sunder (2232) | `*sunþraz`, `*sunþrjanan` | Reconstruction evidence — reconstructed lexical forms |
| think (2248) | `þencan`, `geþencan` | OE evidence — ordinary OE forms |
| thorn (2251) | `þorn` | OE evidence — ordinary OE form |
| wade (2266) | `wæden` | Development note — intermediate form |
| wax (2276) | `wēox` | Lexical note — OE preterite |
| yarn (2305) | `*garna`, `*geern`, `*gearn` | Reconstruction evidence |
| ten (2242) | `tȳn`, `tīen` | Reconstruction/Development — OE forms |
| three (2254) | `þry` | OE evidence — ordinary OE form |
| breast (1968) | `ēo` | Development — **vowel sequence, likely false positive** |
| breast (1968) | `brēost` | Formation comparison — `.iv` form |
| dill (1990) | `dile` | Formation comparison — `.iv` form |
| fast (2004) | `festan` | Class comparison — `.iv` form |
| flask (2016) | `flasce` | Formation comparison — `.iv` form |
| follow (2027) | `fylġan`, `folgian` | Class comparison — `.iv` forms |
| gall (2037) | `ġealla` | Stem comparison — ordinary OE form |
| navel (2133) | `*nabulō`, `*næbula` | Reconstruction and Development — reconstructed forms |
| needle (2136) | `*nēþlō`, `nédl` | Reconstruction and Development |
| nose (2143) | `*nusō`, `*nósu` | Reconstruction and Development |
| sap (2168) | `*saf`, `sæp` | Reconstruction evidence |
| sea (2169) | `*sawi`, `*sei`, `*sǣi`, `*sáiwiz`, `*sāwiz`, `*sāwi`, `*sāi`, `sǣ` | Development chain — stage forms |
| sieve (2189) | `*síβi`, `*síβe` | Development — reconstructed stage forms |
| staff (2212) | `*stábaz`, `*stába`, `*stáb`, `stæf` | Development chain |
| withy (2296) | `*wīþja` | Reconstruction evidence |
| world (2302) | `*weraldu`, `*weruld`, `*weraldiz` | Development chain — stage forms |
| youth (2308) | `*jugunþi`, `*juguþ`, `geoguþ`, `iuguþ` | Reconstruction evidence |
| bow/bēag (1962) | `ēa` | Reconstruction — **vowel sequence, likely false positive** |
| bow/bēag (1962) | `bēag`, `būgan` | Paradigm comparison — `.iv` forms |
| cow (1980) | `*kōz`, `*kūaz`, `*kūz`, `cūs`, `*cūi`, `*cūiz`, `cȳ` | Reconstruction/OE evidence |
| fright (2034) | `fyrhte` | Paradigm comparison — `.iv` form |
| meed (2124) | `*mizdo`, `*mizdu`, `méd` | Development chain |
| night (2140) | `*nahti`, `*náxti`, `*neaxti`, `*niexti`, `*nixti` | Development chain |
| rest (2152) | `tó` | OE evidence — **preposition, likely false positive** |
| shoulder (2183) | `*skúldramiz`, `*skúldrumiz`, `*skúldrum`, `sċuldrum` | Development chain |
| shoulder (2183) | `sculdrum` | Paradigm comparison — `.iv` form |
| shove (2184) | `*skáeub`, `*skēab`, `*skēaβ`, `sċēaf` | Development chain |
| shove (2184) | `sċēaf` | Paradigm comparison |
| learn-liorna (2313) | `*líznô`, `*lírnô` | Development chain |
| learn-liornaþ (2314) | `*líznōθi`, `*lírnōθi` | Development chain |
| strew (2227) | `hīez` | Reconstruction evidence |
| fire (2013) | `*fōr` | Reconstruction evidence |
| fowl (2030) | `*fúglaz` | Expected/attested table |
| rust (2162) | `rūst` | OE evidence — ordinary OE form |
| wolf (2298) | `*wúlfaz`, `*wólfa` | Development chain |

**Probable false positives requiring narrow validator exclusions:**
- `ēo` (Para 706, breast/Development): single diphthong sequence, not a lexical word
- `ēa` (Para 1096, bow/Reconstruction): single diphthong sequence
- `tó` (Para 1230, rest/OE evidence): preposition `tó` used as part of a prepositional phrase, not a lexical headword

**Development-chain stage forms** (e.g. `*náxti > *neaxti > *niexti > *nixti > niht`):
These need inspection — some may be genuine intermediate lexical forms that require
either `.recon` migration + gloss, or a narrow development-chain exclusion in the validator.
