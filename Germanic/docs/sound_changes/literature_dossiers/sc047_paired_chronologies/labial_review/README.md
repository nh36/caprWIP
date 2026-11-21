# SC047 labial conditioning: evidence for discussion

## Identity and question

SC047 (`OEHeavySyllableNasalApocope`), in relation to SC010
(`PWGmcJGemination`), SC029 (`OEAwwjResolution`) and the SC033/SC110
palatalized-glide stages. Tested on the clean review head
`1468c4ac0a6b4d4ca4997a28f82e88353f33c7a0`, 20 November 2026.

Does the reported 384/394 result show a different chronology, a
geminate that survives apocope, or a retained trigger for a later sound
change? The same right context must be tested at both apocope sites:
if pre-gemination placement never creates a geminate under the same
exception, the late treatment only preserves an existing one. If it
does create one, check whether the exception has also preserved a
singleton environment. Those possibilities have different historical
interpretations even if both endpoints match.

## Current state and comparison

The [reviewed baseline](../README.md) retains weight-independent final
short nasal low-vowel loss in the live serialization. The only approved
lexical delta is row 1988, deer: `*déuzô` → *dēora* for headword *dēor*,
with `*déuzą` an unscored direct-singular diagnostic. There are 394
accepted selections, 386 matches, and the same eight mismatches.
Hay 2061, strew 2227 and hue 2332 retain their existing inputs and
targets. Strew's target is a **reconstruction**, not an attested
West Saxon class-I infinitive.

The [archived plan](../plan.json) has early/FNU, split/FNU and
split/FNS but not early/FNS. The rule changed is **the experimental
post-loss nuclearizer**, not production gemination or labial
resolution. FNU first contracts stranded postconsonantal final `ij` to
`ī`, then vocalizes final `j` after any consonant, then final `w` after
a consonant. FNS retains the first and last clauses but replaces the
middle clause with two separate environments: final `j` after a
non-`w` consonant, and final `j` after `Cw` where `C` is a non-`w`
consonant. Final `wwj` therefore escapes, **but so does `Vwj`**:
the second clause does not contain a vowel. FNS does nothing to a
prevocalic `j`.

The [new plan](plan.json) crosses the exact FNS substitution with
early loss, also tests FNG (which explicitly vocalizes `Vwj` and
preserves `wwj`), and separately tests a narrow early delay. That last
arm holds back only stranded `wj` after a short vowel until SC010;
afterward it applies the same geminate-only treatment. It isolates a
modelling assumption, not a reconstruction directly proposed by Ringe
and Taylor: their pp. 46–47 instead require vocalization of the
stranded singleton before gemination; pp. 53, 173 and 250 support the
need for retained conditioning in **other** cells. The predicted
distribution is limited to early-stranded short-V `wj`; an already
prevocalic cluster should not need the protection, nonlabial `tj`
should vocalize as before, and simple final `rw` should give `ru`.

## Diagnosis: full corpus and controls

The original archived and newly executed row records agree exactly
for identity, early/FNU, split/FNU and split/FNS. The
[per-row TSV](selected-outputs.tsv) gives every arm, and the
[intermediate diff](labial-intermediate-differences.tsv) compares
every selected row at every executable checkpoint between split/FNU
and split/FNS, from the common compiled prefix to surface. The only
differences at **any** of those checkpoints are hay (2061) and hue
(2332); both first diverge at nuclearization. Split/FNS does not add
gemination or change SC010's input. It prevents conversion of its
already geminated cluster's final `j` to `i`, feeding later rules.

| Arm | Matches / 394 | All changed outputs relative to live |
|---|---:|---|
| Live identity | 386 | None |
| Early / FNU | 381 | hay `hēa`; hedge `heġe`; net `nete`; rest `rast`; hue `hii` |
| Early / exact FNS | 383 | hedge `heġe`; net `nete`; rest `rast` |
| Early / FNG | 381 | Same as early / FNU |
| Early / explicit short-V `wj` delay then FNG | 383 | Same as early / exact FNS |
| Split / FNU | 382 | hay `hewe`; hedge `heġe`; rest `rast`; hue `hiewe` |
| Split / exact FNS | 384 | hedge `heġe`; rest `rast` |
| Split / FNG | 384 | Same as split / exact FNS |

All arms accept all 394 selections unambiguously. In the exact
early/FNS arm, hay and hue alone change at nuclearization relative
to early/FNU: FNU gives `*xáwi` and `*xíwi`, so SC010 never sees
their j; FNS leaves `*xáwj` and `*xíwj`, so the unchanged SC010
creates `*wwj` even though the ending is already gone. The explicit
delay reproduces both changes; the strict geminate-only early
treatment changes no nucleus-stage result or endpoint. Consequently
the early rescue cannot be counted for Ringe and Taylor's published
early loss **plus immediate vocalization**.

Control roles: *strew* and the tested *hay* and *hue* genitives retain
prevocalic `j` through gemination in all arms. Direct *searu*
vocalizes stranded `w` (`*sárwą > *sárw > *sáru`) in every
experimental arm and yields `saru` (live `searw`). The unscored
genitive gives *searwes* in every arm, a possible source of the
direct form's attested diphthong. *Nett* stays `nete` in every early arm
and `nett` in every split arm (nonlabial control for nasal order).
*Dor*, *þǣr* and *hwǣr* are invariant. SC112 sees short `*dorą`
in the experimental arms, not `*dor`, and only *there* and *where*
fire, with the original before/after representations. The 40 SC017
firing row IDs also survive. This orders the experimental operations,
not the historical date of SC112.

### Worked traces

The starred forms below simplify the FST serialization. The compressed
archive contains the individual tokens and all intermediate stages.

**Hay.** In both split arms SC010 gives `*xáwwją`, then nasal loss
gives `*xáwwj`. Plain FNU first diverges at `*xáwwi`. That blocks
SC029 and the secondary `au` route: fronting and i-umlaut give
`*çewwi`, later w-loss gives `*çewi`, and the final-vowel stage gives
`*çewe > hewe`. FNS/FNG instead hold `*xáwwj` through SC029
(`*xáuj`), then SC030/SC032 give `*xáeuj > *xēaj`; i-umlaut
gives `*çīej`, and word-final `j` is spelled `ġ`, giving *hīeġ*.
The live stack instead runs SC029 and the long-diphthong steps before
nasal loss (`*xáwwją > *xáują > *xēają > *çēaj`), then gives the
same *hīeġ* without the experimental nuclearizer.
The early immediate direct arm does reach the source's singleton
`*xáwi`, but then CAPR takes its separate singleton-aw diphthong
route, loses `w` before `i`, and gives *hēa*. That result is neither
Ringe and Taylor's `*hæwi` checkpoint nor a new OE attestation.
In contrast the vowel-protected genitive `*xáwjas` geminates under
both chronologies and runs through `*xáwwjas > *xáujas > *xēajæs
> *çīejæs > hīeġes`. The final item is a modelled donor cell,
not a newly verified manuscript genitive. The printed OHG
direct-form contrast is independent evidence that a non-geminating
route and a remodelled route can coexist; it does not decide which
West Saxon cell first had the geminated stem.

**Strew.** Whole-form `*stráwjaną` and Fulk-type `*stráujaną` both
pass the input gate. In the live reference the first forms
`*stráwwjaną` at SC010 and then `*stráujaną` at SC029; the second
undergoes neither operation. Staged probes agree exactly from
SC029 onward. Both give `*stráeujaną > *strēajaną`, with `j` still
before the first syllable of `-aną`. Nasal loss removes the final
vowel only (`*strēajan` on the live path); i-umlaut gives
`*strīejąn`, later `*strīejan`, and intervocalic j after the front
diphthong strengthens in CAPR (`*strīeʒan`) before rendering
reconstructed *strīeġan*. Early versus split loss merely puts
the removal of final `ą` before versus after gemination; neither
changes the root-j environment. This verifies endpoint convergence
under CAPR's rules, not the historical truth of the reversal or
the impossibility of Fulk's alternative w-retaining prediction.
An independent cognate or same-stem cell diagnostic of consonantal
w versus inherited glide, before the routes coalesce, would
distinguish them; the normalized Anglian outcome alone cannot.

**Hue.** Split SC010 and apocope give `*xíwwją > *xíwwj`.
FNU first diverges at `*xíwwi`, which blocks the j-sensitive
labial reanalysis and the long-`īo` stage. CAPR instead gives
short `*çíowwi`, then `*çíewwi > *çíewi > *çíewe > hiewe`.
With FNS/FNG, SC033 gives `*xíuwj`, and SC110 reads the remaining
`wj` to give `*xīowj`; i-umlaut then gives `*çīewj`. Only after it
has carried that conditioning does final heavy-syllable j-loss
give `*çīew > hīew`. The live stack likewise reaches long `*īo`,
but completes SC033/SC110 before apocope. In the early immediate branch
`*xíwją > *xíwj > *xíwi`, no geminate is created. CAPR does the
expected w-loss (`*çíwi > *çíi`), but does not contract the two
adjacent i's to long `ī`, hence literal `hii`, not modelled or
attested *hī*. The protected `*xíwjas` gives *hīewes* regardless
of apocope placement. The long diphthong and w of the edition
forms support a palatalized labial stem; they do not prove its
presence in the original direct cell, its precise phonemic
structure, or that a productive contraction rule is already
implemented in CAPR.

## Literature and evidence limits

- **Hay.** Ringe and Taylor (2014), pp. 46–47, 53, 173, 246,
  distinguish direct `*hawją > *hawi > *hæwi` from protected
  `*hawjwj- > *hauj- > *hēaj-`. The latter yields their normalized
  West Saxon *hīeġ*, beside Mercian and Northumbrian *hēġ*. They
  identify OHG *hewi* as the inherited neuter nominative–accusative
  singular and OHG *houwi* as the same direct form remodelled from
  geminating obliques. That is a historical cell assignment, not a
  claim that a single scribe explicitly labelled or wrote both forms
  in an inflected paradigm. [EWA IV, s.v. *hewi, houwi*](https://ewa.saw-leipzig.de/articles/70680/en)
  records both OHG forms in glosses from the tenth century and later
  texts, including the Alemannic Notker tradition. The article groups
  those sources, so one should not assign every citation of both
  forms to that dialect. Bosworth–Toller Supplement, s.v. *hig*,
  distinguishes edited *heg*, *hig* and *heig* witnesses; the
  macron and dot in CAPR's *hīeġ* are normalization, not diplomatic
  spelling. The inherited/remodelled contrast favours an independent
  oblique route and is not an absolute date for English apocope.
- **Strew.** Campbell (1959), p. 46 §120.2 and p. 167 §407,
  derives the ordinary diphthongal outcome after gemination; Ringe
  and Taylor (2014), pp. 53, 173, 246, explicitly propose reversion
  from palatalized `*strawjwjan` to `*straujan`, comparing OHG
  *gistrouwen*. In Fulk (2018), pp. 71–72 §4.10 and n. 1 **on p. 72**,
  `*straujaną` already has `au`; he objects that a consonantal-w
  route would instead leave w in stages leading to reconstructed
  West Saxon `*strīewan`. Both accepted analyses have root `j`
  before the first suffix vowel `a`, not before the final
  `ą`: nasal loss cannot strand it because `-an-` intervenes.
  The Exeter Book's *Seafarer* 97 is [edited as *stregan*](https://sianechard.ca/web-pages/the-seafarer/);
  *strēġan* is Ringe and Taylor's normalized Anglian reading,
  not a West Saxon manuscript *strīeġan*. Their p. 259 n. 27
  treats the independently well-attested West Saxon class-II
  *streowian* as remodelling. Gothic *straujan* and OHG
  *gistrouwen* motivate the competing accounts; neither spells
  out the prehistoric phonetic sequence in English.
- **Hue.** Ringe and Taylor (2014), pp. 53, 250, propose direct
  `*hiwi` beside `*hiwjwja-`; their direct West Saxon continuation
  is reconstructed `*hī`, whereas the geminated stem passes
  through `*iuw` and `*īow` with a still-palatalizing semivowel,
  then West Saxon *hīew*. Their §6.7.1, pp. 257–261, independently
  situates w-loss before unstressed i (after i-umlaut and before
  syncope); p. 259 includes the relevant *glī* and *nī-* controls.
  Campbell (1959), p. 46 §120.2, likewise distinguishes the *iwj*
  result with w from the *awj* result with j. Bosworth–Toller
  Supplement, s.v. *hiw* 'shape', cites the *Pastoral Care* 133.11
  reading *hiéw* (variant *hîw*) and 87.20 *hiwes* (variant
  *hiéwes*): these are edition readings, not transcriptions newly
  taken from manuscript images. *Hīew* and *hīw* are normalized
  attestations, while `*hī` and CAPR `hii` are not new attestations.
  Orel (2003), pp. 171–172, and Kroonen (2013), p. 224, also give
  substantively different e-reconstructions; the experiment holds
  the adopted i-input fixed. The FST's `ww+j` and `w+j` carry
  conditioning, not a claim about a separately measurable j segment.

## Verdict and propagation

**RETAIN** all production code and lexical selections; **DEFER** the
historical ordering of nasal loss against gemination. No strict
chronology edge follows from a successful rendering of either
reconstruction. The labial traces are evidence about what the
lexemes need in the model. The inherited versus remodelled cell
histories remain philological accounts, not implemented analogy.
No tests, fixtures, recurring compilation, books or frozen baseline
are changed by this follow-up.

Registry-verdict: SC047=REFORMULATE/RETAIN

## Residue and reproducibility

The strongest nasal-order discriminator here remains a **nonlabial**
light nasal direct cell, such as *nett*, not the difference between
382 and 384. Evidence for inherited direct gemination without
plausible donors would favour split loss; securely inherited direct
singleton forms opposite protected geminates favour early loss with
vocalization. To distinguish an independently delayed labial
vocalization from nasal survival, comparative pairs must establish
both the reconstructed ending and whether a stranded singleton
`wj` remained consonantal across gemination; neither endpoint
can establish that independently. The hay singleton-aw and hue
hiatus outputs flag separate downstream issues, not new timing
evidence or corrections adopted here.

[Frozen observations](observations.json.gz) and [provenance](observation-provenance.json)
pin the experiment; the worker is byte-identical to the
[archived snapshot worker](../../sc047_three_decisions/README.md#reproducible-evidence).
The isolated comparison used 451 finite relations in 363.74 s, one
common definition compile plus one batch, peak RSS 2,245,604 KiB.
This is a research-only execution cost, with no addition to default
validation. The dossier prose was drafted while the frozen assay
ran; it does not enter the compiler or publication dependencies.
[Publication receipt projections](publication-receipts.json) identify
the prior approved head and book; they are not validation receipts
for these new discussion files.
