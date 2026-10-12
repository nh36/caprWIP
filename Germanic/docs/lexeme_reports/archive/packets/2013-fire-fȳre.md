# Evidence packet — 2013 fire / fȳre

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2013 | fire | fȳre | *fūri | *fūri | known_unmodelled | ANALOGICAL: Proto dat.sg. *fūri triggers i-umlaut; final *-i apocopated after heavy syllable → fȳr. Attested fȳre has -e analogically restored by proportion with regular a-stems (word:worde::fȳr:fȳre). FST correctly produces endingless fȳr. | See DEV_NOTES.md. |

## Manifest status

| REPORT_PATH | STATUS |
| :--- | :--- |
| pilot/fire.md | pilot |

## High-confidence evidence

### Compact derivation trace entry

```md
# fire
PROTO: *fūri
EXPECTED: fȳre
OUTPUTS: fȳr



### Proto-Germanic consonant inheritance

Proto Input: *fūri

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>OE I Umlaut: *fȳri<br>OE High Vowel Apocope: *fȳr |



### Orthography & surface

Outcome: fȳr

NOTE: ANALOGICAL: Proto dat.sg. *fūri triggers i-umlaut; final *-i apocopated after heavy syllable → fȳr. Attested fȳre has -e analogically restored by proportion with regular a-stems (word:worde::fȳr:fȳre). FST correctly produces endingless fȳr.
```

### Matching oe_known_problems.tsv entries

| proto | status | category | reason | refs | added |
| :--- | :--- | :--- | :--- | :--- | :--- |
| *fūri | exception | analogical_dat_e | FST correctly produces fȳr (regular nom./acc.sg. outcome of *fūri after i-umlaut + high-vowel apocope); target fȳre has analogically restored dat.sg. -e (four-part analogy with word:worde) — morphological process the FST cannot model | DEV_NOTES.md §6084-6268 (esp. 6189, 6262-6268) | 2026-04-25 |

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:6173 (exact pair)

- Nearby heading: ### The problem

```text
6171: ### The problem
6172: 
6173: The TSV uses proto `*fūri` (dative/locative singular) with target `fȳre`.
6174: The FST produces `fȳr` (without the `-e` ending).
6175: 
```

#### Germanic/docs/DEV_NOTES.md:30617 (exact pair)

- Nearby heading: ##### Words in the TSV with proto *-aCl-* or *-aCr-* before a back-vowel tail

```text
30615: | 2002 | *fállaną | feallan | geminate *ll* |
30616: | 2008 | *fárnaz | fearn | breaking |
30617: | 2013 | *fūri | fȳre | irrelevant |
30618: | 2025 | *fálθaną | fealdan | breaking |
30619: | 2030 | *fúglaz | fugol | *u*-vowel, not A-restoration; handled by `OEGLInsertion` (germanic.txt) |
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:19 (note keyword: i-umlaut)

- Nearby heading: ### Mismatch fixes (Mar 2026)

```text
17: - [Preconsonantal *x Loss: *xs > *s](#preconsonantal-x-loss-xs--s-before-consonant-clusters)
18: - [PGmc *d/*ð Representation Decision](#decision-2026-03-11-option-2a-confirmed)
19: - [OE þistel 'thistle': Scholarly Controversy](#oe-þistel-thistle-i-umlaut-not-preserved-2026-03-18)
20: - [OE huniġ 'honey': The -ag > -ig Sound Change](#oe-huniġ-honey-the--ag---ig-sound-change-2026-03-19)
21: - [OE wīþiġ 'withy': ja-stem vs Sievers' Law](#oe-wīþiġ-withy-ja-stem-adjective-vs-sievers-law-syncope-2026-03-19)
```

#### Germanic/docs/DEV_NOTES.md:93 (note keyword: dat.sg.)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
91: 
92: **Approach A: Use a u-stem or root-noun form.**
93: R/T notes that u-stems and root nouns regularly preserve *u because their paradigms have predominantly high-vowel suffixes (nom.sg. *-uz, acc.sg. *-ŷ, gen.sg. *-iz, dat.sg. *-i, nom.pl. *-iz, etc.). For example, *lustuz (u-stem nom.sg.) → OE lust with preserved u (R/T p.45). If *wulf-, *fugl-, or *bukk- were u-stems, we could use the nom.sg. in *-uz.
94: 
95: **What weighs against Approach A:**
```

#### Germanic/docs/DEV_NOTES.md:116 (note keyword: i-umlaut)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
114: - Root nouns are a small, archaic class (burg, brust, furh, hnut-); extending the analysis to common nouns like 'wolf' and 'fowl' would be speculative.
115: 
116: **Approach D: Use a derivational form with i-umlaut trigger.**
117: For some of the items, there are derivational forms with *j or *i that block lowering: *wulfi- (hypothetical i-stem variant?), or the derived verb *fullijaną 'to fill' → OE fyllan (where *-ij- blocks lowering of root *u).
118: 
```

#### Germanic/docs/DEV_NOTES.md:120 (note keyword: i-umlaut)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
118: 
119: **What weighs against Approach D:**
120: - These derived forms already show i-umlaut (*fullijaną → fyllan, not full). We can't simultaneously have the u preserved (from the high-vowel context) AND escape i-umlaut. The derivational base is a different word, not a paradigm form of the simplex noun.
121: 
122: ### Luick's doublets evidence
```

#### Germanic/docs/DEV_NOTES.md:709 (note keyword: i-umlaut)

- Nearby heading: ### Summary of OE syncope rules (scholarly consensus)

```text
707: 1. **Non-high vowel syncope** (`*a/*e → ∅`): Applies **regardless of preceding 
708:    syllable weight**, as long as the syllable is stressed. This affects PWGmc `*a` 
709:    and its i-umlaut product `*e`.
710:    
711:    Examples:
```

#### Germanic/docs/DEV_NOTES.md:742 (note keyword: i-umlaut)

- Nearby heading: ### The milk problem: `*melukz` → `meoloc` (expected `meolc`)

```text
740: with paradigm variation:
741: - Nom.sg.: `*melukz` → `meoloc` (with breaking `e → eo`, no syncope)
742: - Gen./dat.sg.: `*milukiz/*miluki` → Anglian `milc` (with i-umlaut and syncope)
743: 
744: R/T §6.6.4 (p.253): "The usual WS form of 'milk' is `meolc < meoluc < *meluk`... 
```

#### Germanic/docs/DEV_NOTES.md:749 (note keyword: i-umlaut)

- Nearby heading: ### The milk problem: `*melukz` → `meoloc` (expected `meolc`)

```text
747: 
748: **Key point:** The syncopated form `milc` shows **early syncope** that occurred even
749: before i-umlaut — R/T (p.257) notes this as a "possible early instance of syncope."
750: The WS form `meoloc ~ meolc` shows **variable syncope after a light syllable**.
751: 
```

#### Germanic/docs/DEV_NOTES.md:763 (note keyword: dat.sg.)

- Nearby heading: ### The milk problem: `*melukz` → `meoloc` (expected `meolc`)

```text
761: **Possible explanations:**
762: 
763: 1. **Paradigmatic leveling:** The syncopated form `milc` (< gen./dat.sg. `*milyci` 
764:    with heavy syllable from consonant cluster) was generalized to nom./acc.
765:    
```

#### Germanic/docs/DEV_NOTES.md:3195 (note keyword: dat.sg.)

- Nearby heading: ### Case 1: *rastō → rast (expected ræst) — ō-stem feminine

```text
3193: - Acc.sg. *rastō̃ → PWGmc *rasta → AFB *ræstæ → ræste (front suffix, no restoration)
3194: - Gen.sg. *rastōz → PWGmc *rasta → AFB *ræstæ → ræste (front suffix, no restoration)
3195: - Dat.sg. *rastōi → PWGmc *rastē → AFB (no *a in suffix to front) → ræste (no restoration)
3196: 
3197: Only the nom.sg. has the back suffix *-u that triggers A-restoration. All oblique cases (acc., gen., dat.) have front suffix vowels → no restoration → ræst- throughout. The majority oblique pattern was generalized to the nom.sg.: ræst.
```

#### Germanic/docs/DEV_NOTES.md:3202 (note keyword: dat.sg.)

- Nearby heading: ### Case 1: *rastō → rast (expected ræst) — ō-stem feminine

```text
3200: 
3201: **Sources:**
3202: - BT: headword "ræst" f. 'rest, repose, bed, grave'. Oblique forms: ræste (gen./dat.sg.).
3203: - Kroonen (p.420): *rasto- f. 'interval' — Go. rasta, ON rost, OE rest, OS rasta, OHG rasta. (Kroonen gives OE "rest", i.e. ræst with late OE æ→e.)
3204: - R/T §6.3.1–6.3.2: paradigmatic alternation between a and æ due to A-restoration is explicitly discussed for a-stems (dæg/dagas); same logic applies to ō-stems.
```

#### Germanic/docs/DEV_NOTES.md:6169 (exact COUNTERPART)

- Nearby heading: ## OE fȳr/fȳre 'fire': Paradigm and umlaut problem (2026-03-10)

```text
6167: ---
6168: 
6169: ## OE fȳr/fȳre 'fire': Paradigm and umlaut problem (2026-03-10)
6170: 
6171: ### The problem
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:456 (note keyword: i-umlaut)

- Nearby heading: ## 7. R/T relative chronology of A-fronting, A-restoration, breaking, and i-umlaut

```text
455: 
456: ## 7. R/T relative chronology of A-fronting, A-restoration, breaking, and i-umlaut
457: 
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:46 (note keyword: i-umlaut)

- Nearby heading: ### OE target assessment

```text
45: 3. **Breaking**: \*æhh → \*eahh
46: 4. **i-Umlaut**: \*eahh → \*ieahh → hiehh (WS palatal diphthong umlaut)
47: 
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:105 (note keyword: i-umlaut)

- Nearby heading: ### Proto-form assessment

```text
104: The proto `*skellinăz` does not match Kroonen's reconstruction. The \*e in
105: \*skellinăz would give OE \*sċiellen (via i-umlaut and palatalization), but the
106: attested form is sċilling with *i.
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:114 (note keyword: i-umlaut)

- Nearby heading: ### Pipeline issues

```text
113: 
114: 2. **With current proto** `skellinăz`: the pipeline produces `sċiellen` (with i-umlaut
115:    of *e → *ie, but no mechanism to produce *i in the root).
```

#### Germanic/docs/analysis/fryhtu_investigation.md:26 (note keyword: i-umlaut)

- Nearby heading: ### R/T's analysis

```text
25: 
26: R/T (line 21553) treat OE fyrhtu as an **ī-stem abstract noun**. The i-umlaut
27: (\*u → y) proves an \*i-containing source, since the ō-stem \*furhtō- would give
```

#### Germanic/docs/analysis/fryhtu_investigation.md:34 (note keyword: i-umlaut)

- Nearby heading: ### The \*iþō-abstract analysis

```text
33: with the suffix PGmc \*-iþō-. These are inflectionally ō-stems but contain the
34: derivational element \*-iþ- which triggers i-umlaut. Well-known examples:
35: 
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:627 (note keyword: dat.sg.)

- Nearby heading: ### 2.21 Lexicographical witnesses (Bosworth–Toller, Bright, Hall)

```text
626: in §1 — all three list *meord* as a real lemma cross-referenced to
627: *mēd*, with *meorde* (dat.sg.) the actual attested form. No source
628: in the local repo cites a bare nom.sg. attestation of *meord* — it is
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:629 (note keyword: dat.sg.)

- Nearby heading: ### 2.21 Lexicographical witnesses (Bosworth–Toller, Bright, Hall)

```text
628: in the local repo cites a bare nom.sg. attestation of *meord* — it is
629: universally a lexicographer's reconstruction from the dat.sg. obliques.
630: 
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:692 (note keyword: dat.sg.)

- Nearby heading: ## 3. Synthesis: which authors support which hypothesis?

```text
691:    §2.10/§2.11 above). No author proposes that, e.g., *mizdai*
692:    (dat.sg.) gives *meorde* lautgesetzlich while *mizdō* (nom.sg.)
693:    gives *mēd* lautgesetzlich, with later levelling.
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:75 (note keyword: dat.sg.)

- Nearby heading: ### For \*mōdēr

```text
74:   later reflex" (i.e. leveled from paradigm forms with back vowels)
75: - The regular outcome is -er (cf. dat.sg. mēder, brēder from \*-ri)
76: - The -or/-ur forms have the back vowel **leveled in** from other case forms
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:173 (note keyword: dat.sg.)

- Nearby heading: ### 3. \*mōdēr/mōdor → fix target

```text
172: The regular neogrammarian nom.sg. outcome is "mōder" (via \*ē → \*ǣ → e).
173: R/T: early WS "modor ~ -ur" alongside dat.sg. "mēder" (regular, from \*-ri).
174: 
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:176 (note keyword: dat.sg.)

- Nearby heading: ### 3. \*mōdēr/mōdor → fix target

```text
175: Note for TSV: "R/T §7.2.1: 'modor ~ -ur' has suffixal vowel leveled from
176: oblique cases (analogical). Regular nom.sg. reflex is mōder (cf. dat.sg. mēder
177: < \*mōdri). The regular form mōder matches OE fæder < \*fader."
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:145 (note keyword: i-umlaut)

- Nearby heading: ### Ringe & Taylor §6.9.2 (repo ll. 17663–17760)

```text
144: R/T note an asymmetry (ll. 17769–17772): the raising `æ > é` operated only
145: on `æ < éa` (smoothing-output), **not** on `æ < *a` (i-umlaut output). Hence
146: WS, Merc., North. all keep `ǽht` 'possession', `tǽcnan`, `fǽcne` etc.
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:156 (note keyword: i-umlaut)

- Nearby heading: ### Brunner §119 "Ebnung" (repo ll. 4745–4811)

```text
155: > für ea und eo jeder Herkunft (für ea in ganz alten Texten aber æ ...),
156: > i für io, æ für ea (bei i-Umlaut aber e ...), e für eo, i für io. Solche
157: > anglische Formen sind demnach: ... becen Zeichen, ec auch, leg Seil, ege
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:569 (note keyword: i-umlaut)

- Nearby heading: ## 7. i-mutation outcomes

```text
568: 
569: For most front vowels, i-umlaut outcomes are uniform across dialects.
570: Differences emerge mainly with the diphthongs `ea, eo, io` and with `ǽ`:
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:239 (note keyword: i-umlaut)

- Nearby heading: ### §4.2 Phonological assessment

```text
238: * **`bȳhþ` / `bȳhst`** (3/2 sg. pres. ind.): would require
239:   i-umlaut of the *u* (or of the inherited *iu* > *í*-stage)
240:   followed by spirantisation/devoicing of the stem-final consonant
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:326 (note keyword: i-umlaut)

- Nearby heading: ### §5.2 Phonological assessment

```text
325:   a-mutation, then *-anaz > -en. Universal attestation.
326: * **`sċȳfþ`** (3 sg. pres. ind.): would require i-umlaut + cluster
327:   realisation parallel to `bȳhþ`; possible but more cascade-
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:32 (note keyword: i-umlaut)

- Nearby heading: ## 1. TL;DR

```text
31: > **Inherited West-Gmc /ɣ/ palatalises to OE [ʝ] > [j] (spelt ġ) when it is
32: > adjacent to a front vowel (i, ī, e, ē, æ, ǣ, y, ȳ from i-umlaut, ie/ī from
33: > i-umlaut, and the front diphthongs io/eo/ea, ie/ȳ) AND a following back
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:33 (note keyword: i-umlaut)

- Nearby heading: ## 1. TL;DR

```text
32: > adjacent to a front vowel (i, ī, e, ē, æ, ǣ, y, ȳ from i-umlaut, ie/ī from
33: > i-umlaut, and the front diphthongs io/eo/ea, ie/ȳ) AND a following back
34: > vowel does not "rescue" it.**
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:79 (note keyword: i-umlaut)

- Nearby heading: ### 2.1 Campbell, *Old English Grammar* (1959), §§ 426–430

```text
78: > i.e. by æ, e, i, by ǣ, ē, ī, by the diphthongs ǣa, ēa, eo, io, by æ̆ and
79: > ē̆ where these are due to i-umlaut, but not by y, ȳ, œ, ø̄ from i-umlaut of
80: > u, ū, o, ō (cf. § 190)."
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:380 (exact PROTOFORM)

- Nearby heading: ### Option B: Add to `oe_known_problems.tsv`

```text
379: This category aligns with existing `oe_known_problems.tsv` entries
380: (`*fūri` → `analogical_dat_e`; `*táppô` → `analogical_n_stem_levelling`).
381: 
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| fire | fȳr | inh | template:inh | fire |

#### old_english_swadesh.tsv

| NUMBER | ENGLISH | OLD_ENGLISH | IPA_RAW |
| :--- | :--- | :--- | :--- |
| 167 | fire | fȳr | /fyːr/ |

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:90 (concept name)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
88: ### Could we use paradigm forms? (Why we decided not to)
89: 
90: For other problematic items (fire, brand, berry, thorn), we successfully resolved mismatches by adopting a paradigm form in which the phonological development is lautgesetzlich. The question is whether the same approach works for the u-lowering exceptions.
91: 
92: **Approach A: Use a u-stem or root-noun form.**
```

#### Germanic/docs/DEV_NOTES.md:1428 (exact pair)

- Nearby heading: ## Project Status (as of 2026-04-30) — research phase complete

```text
1426: The 7 remaining are all documented exceptions:
1427: * `*búkkaz → bocc` (expected `bucc`) — `wontfix: u_lowering_near_labial`
1428: * `*fūri → fȳr` (expected `fȳre`) — `exception: analogical_dat_e`
1429: * `*fúglaz → fogol` (expected `fugol`) — `wontfix: u_lowering_near_labial`
1430: * `*rústō → rost` (expected `rust`) — `wontfix: u_lowering_near_labial`
```

#### Germanic/docs/DEV_NOTES.md:1738 (concept name)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1736:   - **Observation:** `OldEnglishWeakTailReduction` appears inert in current builds; `*u` in weak tails (e.g., *tehun, *sebun, *newun) stays `{*u}` at `EnglishAfterProtoToOEWeakTail`, so the new `{*u}->{*o}` line does **not** affect `*-un`.
1737:   - **Implication:** a targeted `*-un -> -on` rewrite may need to be its own rule/stage, or the existing weak‑tail reduction block needs fixing so any reductions actually apply.
1738:   - **Next checks:** run `flookup` against `old_english_sandbox_after_proto_to_oe_weak_tail.bin` for `texun/tehun/sebun/newun` and probe `OldEnglishWeakTailReduction` in isolation to confirm whether **any** `{*ă}/{*ą}/{*i}/{*u}` reductions fire.
1739:   - **Decision point:** if `OldEnglishWeakTailReduction` is truly dead, fix that block first; otherwise add a dedicated `OldEnglishWeakTailUnReduction` rule for `{*u}{*n} -> {*o}{*n}`.
1740: - Foma notes / recurring gotchas (2026-01-26, updated 2026-02-06):
```

#### Germanic/docs/DEV_NOTES.md:1773 (exact pair)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1771:     - `*fuwer → fȳr`: no rule converts `{uw}` before `{r}` into `{ȳr}`; add a `{uw}` contraction (or targeted `ur` rounding) so `fūr`-class stems reach OE fȳr.
1772:     - `*xattuz → hōd`: expected reflex doesn’t match the provided proto stem (phonologically it yields OE “hat”); fix data alignment rather than phonology.
1773:   - 2026-01-10b data note: the “fire” row now uses dat.sg. *fūri (> fȳre) to avoid modelling nominative levelling; see TSV comment.
1774:   - 2026-01-10 rollback: backed out the short-diphthong lengthening experiment; diagnostics back to the post-*fūri* baseline (293 mismatches) with `slaxăną` still in the long-vowel bucket for future work.
1775: 
```

#### Germanic/docs/DEV_NOTES.md:1774 (exact PROTOFORM)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1772:     - `*xattuz → hōd`: expected reflex doesn’t match the provided proto stem (phonologically it yields OE “hat”); fix data alignment rather than phonology.
1773:   - 2026-01-10b data note: the “fire” row now uses dat.sg. *fūri (> fȳre) to avoid modelling nominative levelling; see TSV comment.
1774:   - 2026-01-10 rollback: backed out the short-diphthong lengthening experiment; diagnostics back to the post-*fūri* baseline (293 mismatches) with `slaxăną` still in the long-vowel bucket for future work.
1775: 
1776: ---
```

#### Germanic/docs/DEV_NOTES.md:1810 (concept name)

- Nearby heading: ### Short-vowel split sequentialised (WIP)

```text
1808: ### Short-vowel split sequentialised (WIP)
1809: 
1810: - Broke `EnglishSandboxShortVowelSplit` into two parts so the contextual rewrites fire before the fallback defaults: `EnglishSandboxShortVowelContextual` now contains every `{u→ʊ}`/{`e→ɪ`}/{`i→ɪ` } clause, while `EnglishSandboxShortVowelFallback` holds the unconditional `{u→ʌ}` and `{e→ɛ}` conversions. The wrapper `EnglishSandboxShortVowelSplit` composes the two stages (`.o.`) so the historical order matches the FOOT/KIT contexts feeding the later defaults.
1811: - Probes (`*swestēr`, `*bardaz`, `*bebruz`, `*bergą`, `*utraz`) no longer branch at `EnglishSandboxVowelRules`; each lexeme now yields a single vowel reflex, which finally exposes the genuine coverage gaps instead of masking them behind duplicated outputs. Tracer log copied to `docs/debug_snapshots/english_tracer_log_2025-12-07b.txt`.
1812: - Regression: analyzer successes dropped to **146/376** because many STRUT/DRESS lexemes now lack the “extra” fallback paths that previously papered over incomplete conditioning. Next step is to audit the English TSV rows with no outputs (see `server/tmp/english_sandbox_results_current.json`, e.g. bæn/brɛd/blʌd) and backfill the missing contexts before moving on to weak-tail reductions. Hold off on adding `{*e}` tails until coverage recovers to the 185 baseline.
```

#### Germanic/docs/DEV_NOTES.md:1859 (concept name)

- Nearby heading: ### Rhotic colouring prototype (2025-12-06 — evening)

```text
1857: - No additional weak-tail rules were enabled yet—`EnglishSandboxWeakTailReductions` still only handles `{*a}` and `{*ą}`. Next session should start widening that stage one vowel class at a time while rerunning the workflow after each addition, so any regressions are easy to pinpoint.
1858: 
1859: - Follow-up determinism pass: instrumented `trace_english_sandbox.py` for the rhotic probes, then tried to sequentialise both `EnglishSandboxCoreVowelRules` and `EnglishSandboxShortVowelSplit` so each vowel rewrite would fire exactly once (logs in `/usr/app/tmp/vowel_branching_trace.txt`). That change did collapse the outputs (e.g., `*bardaz` finally reduced to a single path), but coverage cratered to 168/376. Reverted to the previous definitions and reran the workflow (`docs/debug_snapshots/english_tracer_log_2025-12-06l.txt`) so we’re back at **206/376** successes with the older branching behaviour intact.
1860: - Takeaway: branching now clearly comes from overlapping clauses inside the core vowel block and the short-vowel split, but wholesale sequentialisation is too disruptive. Next attempt should peel off one context at a time (e.g., only the `{*ō}` liquid rule) and validate immediately rather than rewriting the entire stage.
1861: 
```

#### Germanic/docs/DEV_NOTES.md:1955 (concept name)

- Nearby heading: ### GermanStar* regeneration

```text
1953: - Added `server/tools/generate_german_star_sets.py`; it parses the `pgrm*` macros and emits literal unions for `GermanStarVowel/Diphthong/Consonant` plus the front/back subsets (mirroring Burmish). Ran `python3 server/tools/generate_german_star_sets.py --output /tmp/german_star_defs.txt` and pasted the output into `server/fsts/germanic.txt` so every star set is now a single-tape brace list again (`{*a}`, `{*ai}`, `{*b}`, …).
1954: - Recompiled via `docker compose exec backend bash -lc "cd /usr/app && foma -f fsts/germanic.txt"` and sanity-checked with `regex GermanStarVowel; random-words 5` / `regex GermanStarConsonant; random-words 5`. Outputs now show plain `{*…}` tokens instead of the previous `0:yy` relations, confirming the contexts are real languages again.
1955: - Reran the stage tracer for `GermanAfterConsonant` and `GermanAfterStopShift` (with `--normalize-plain`), but the ach-Laut probes still emerge as `*l*au*k*a*z`. So the literal sets were necessary but not sufficient—the `{*k}` contexts still don’t fire even though the inventories now match. Next step is to instrument `GermanStopShift` again or log the immediate environments to see what’s still mismatched.
1956: 
1957: ### Tracer tweaks (still WIP)
```

#### Germanic/docs/DEV_NOTES.md:3208 (exact pair)

- Nearby heading: ### Case 1: *rastō → rast (expected ræst) — ō-stem feminine

```text
3206: **Proposed resolution — oblique form approach:**
3207: 
3208: Following the precedent of fire (*fūri → fȳre, dat.sg.), cow (*kūi → cȳ, dat.sg.), night (*naxti → niht, dat.sg.), and hammer (*xamaras → hameres, gen.sg.), we can use an oblique form of *rastō where the suffix does NOT trigger A-restoration.
3209: 
3210: The difficulty is that the standard ō-stem oblique endings (*-ōz gen.sg., *-ōi dat.sg.) contain *-ō, which is a back vowel that would ALSO trigger restoration in our pipeline. The pipeline applies rules at the PGmc input level and does not separately model the pre-AFB shortening of *-ōz → PWGmc *-a.
```

#### Germanic/docs/DEV_NOTES.md:3457 (exact pair)

- Nearby heading: ### Note on ræst oblique form problem

```text
3455: The ō-stem nom.sg. path is unaffected: `rastō → rast` (NWGmcFinalLongORaising still applies when *-ō is truly word-final).
3456: 
3457: TSV row 2152 (ræst) now uses genuine PGmc gen.sg. *rastōz, target ræste. This follows the same oblique-form approach as cow (*kūi → cȳ) and fire (*fūri → fȳre): the TSV records an oblique paradigm cell that can be derived lautgesetzlich, explaining the attested OE root vowel through regular sound change rather than analogical leveling.
3458: 
3459: ### Historical phonology of final *-z loss and its interaction with rhotacism
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:688 (concept name)

- Nearby heading: ### 10.4 Predicted effects of the recommended change (option B) on the six probed inputs

```text
687: | `*talōjaną` | single `*l` | `*ō` | `talian` | ✓ |
688: | `*nadrō` | `*dr` — **not** in set (not single, not geminate, not `sC`/`fC`) | (rule does not fire) | `nædre` (vowel; segmentals as before) | ✓ |
689: | `*bastą` | `*st` — **in set** as `sC` | `*ą` weak-tail (excluded) | `bæst` | ✓ |
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:751 (concept name)

- Nearby heading: ## 11. Affected TSV rows

```text
750: 
751: **Row 2205 (`*spárēną → sparian`)**: Probed output under current FST is `spearen`. The proposed fix changes `OEARestorationIntervening` so that the *r* of `*spár-` is no longer excluded, but the trigger vowel of `*spárēną` is `*ē` (front), so A-restoration still does not fire. The path to `sparian` requires a class III → class II morphological remap (`*sparēn- → *sparōjan-`) which appears to be missing or out of order in the FST pipeline. **This is a separate, larger issue** beyond the scope of this report.
752: 
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:163 (exact pair)

- Nearby heading: ### Case 7: *fúwerō / *fūri (fire) — fȳre (dat.sg.) vs. fȳr (nom.sg.)

```text
162: 
163: ### Case 7: *fúwerō / *fūri (fire) — fȳre (dat.sg.) vs. fȳr (nom.sg.)
164: 
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:175 (exact pair)

- Nearby heading: ### Case 7: *fúwerō / *fūri (fire) — fȳre (dat.sg.) vs. fȳr (nom.sg.)

```text
174: | **Attestation status** | **`fȳr` attested (nom.sg.); `fȳre` attested (dat.sg., post-apocope restoration); both valid OE forms from different paradigm cells.** |
175: | **Classification** | **Paradigm-cell case**: The dat.sg. `*fūri` → `fȳre` shows a **post-apocope analogical restoration** of the dative ending *-e (generalized from other weak stems). The nom.sg. `fȳr` is the pure lautgesetzlich product. The TSV targets the dat.sg. cell (`*fūri → fȳre`) because it preserves the original singular form; it is not a compound/fossil case but a **methodological choice to target oblique cells over analogically-restored nominatives**. |
176: | **Methodological use** | Parallel to cow (*kūi → cȳ*), night (*naxti → niht*), hammer (*xamaras → hameres*): when the lautgesetzlich nominative singular has been analogically restored with extraneous endings, the TSV explicitly targets the oblique paradigm cell (dat.sg., gen.sg., etc.) whose lautgesetzlich outcome is derivable. |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:177 (exact pair)

- Nearby heading: ### Case 7: *fúwerō / *fūri (fire) — fȳre (dat.sg.) vs. fȳr (nom.sg.)

```text
176: | **Methodological use** | Parallel to cow (*kūi → cȳ*), night (*naxti → niht*), hammer (*xamaras → hameres*): when the lautgesetzlich nominative singular has been analogically restored with extraneous endings, the TSV explicitly targets the oblique paradigm cell (dat.sg., gen.sg., etc.) whose lautgesetzlich outcome is derivable. |
177: | **Implementation** | TSV targets proto `*fūri` (dat.sg.) with target `fȳre`. The FST produces `fȳr` (nom.sg.), which is actually lautgesetzlich; the mismatch is resolved by understanding that `fȳre` is the attested dat.sg. form (post-apocope restoration). |
178: 
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:140 (exact pair)

- Nearby heading: ### Pipeline fix

```text
139: ```
140: This handles R/T §6.6.1 vowel-hiatus contraction in root nouns (and is consistent with the existing *fūri → fȳre treatment).
141: 
```

#### Germanic/docs/analysis/fryhtu_investigation.md:203 (concept name)

- Nearby heading: ### What our FST implementation revealed

```text
202: 
203: When we restricted the rule to fire only before dental obstruents (\*θ, \*ð,
204: \*d, \*t), all regressions disappeared and all known \*-iθō- abstracts produced
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:292 (note keyword: i-umlaut)

- Nearby heading: ### 4.1 Primary handbooks

```text
291:   - Standard breaking rule: *e → *eo / __ {r, x}C
292: - **§202** (pp. 80–82): Describes i-umlaut of breaking diphthongs
293:   - "A small group of words (§124) suggest that the mutation of eo was io"
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:483 (exact COUNTERPART)

- Nearby heading: ### H6: Genuine analogical exception

```text
482: 
483: **Hypothesis**: Like *fȳr*/*fȳre* (Campbell §§615–616) or *spere* (§17.16 analysis), perhaps `mēd` is analogically restored from somewhere else and we should classify it as an exception.
484: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:518 (note keyword: i-umlaut)

- Nearby heading: ### 6.2 Other *i + rd clusters (rhotacized)

```text
517: 1. `*búrdiz` 'birth' (row 1951) → FST: `byrd` ✓
518:    - Expected: `*búrdiz` → u-lowering → `*bordiz` → breaking (blocked, because *o not *e/*i) → i-umlaut `*byrd` ✓
519: 2. `*xérdō` 'herd' (row 2073) → FST: `heord` ✓
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:51 (note keyword: i-umlaut)

- Nearby heading: ## 1. Charge of this supplement

```text
50: 
51: 3. **Parallel with \*rēc** (notable_findings.md #10): OE *rēc* 'smoke' shows universal long ē across all dialects where we expect WS diphthong *īe (from *au + i-umlaut). Both *rēc* and *mēd* avoid expected diphthongs. Is there a systematic development *VzC → VːC* that yields ē regularly, making *meord* the marked form rather than *mēd*?
52: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:522 (note keyword: i-umlaut)

- Nearby heading: ### 5.1 The *rēc case (notable_findings.md #10)

```text
521: **OE rēc** 'smoke' < PGmc *\*raukiz (m. i-stem):
522: - **Expected WS outcome**: *\*rīec (from *au + i-umlaut → *īe)
523: - **Attested outcome**: **rēc** (long ē monophthong, **no diphthong**)
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:556 (note keyword: i-umlaut)

- Nearby heading: ### 5.3 Testing the VzC → VːC hypothesis

```text
555: Other *i + rd clusters (after rhotacism):
556: 1. *\*búrdiz* 'birth' → OE *byrd* (no issue; *u lowers, then i-umlaut)
557: 2. *\*xérdō* 'herd' → OE *heord* ✓ (regular breaking of *e → *eo)
```

#### Germanic/docs/analysis/notable_findings.md:44 (concept name)

- Nearby heading: ## 1. Medial high-vowel syncope: dental-obstruent conditioning

```text
43: 
44: When we restricted the rule to fire only before dental obstruents (*θ, *ð,
45: *d, *t), all regressions disappeared and all attested syncope forms (dozens of
```

#### Germanic/docs/analysis/notable_findings.md:201 (concept name)

- Nearby heading: ## 1. Medial high-vowel syncope: dental-obstruent conditioning

```text
200: 
201: **Implications for our implementation:** Our FST restricts syncope to fire
202: before dental obstruents `[{*θ}|{*ð}|{*d}|{*t}]`. This works empirically,
```

#### Germanic/docs/analysis/notable_findings.md:765 (concept name)

- Nearby heading: ## 4. A-restoration trigger set: {*æ} is NOT a trigger

```text
764: fronting of *a → *æ happens BEFORE restoration (so restoration sees *æ
765: and does not fire), while dissimilation of *ō > *e happens AFTER
766: restoration (so restoration has already fired and the later fronting is
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:749 (concept name)

- Nearby heading: ### B.2 Campbell, Old English Grammar sec. 218 (and 217, 219, 365, 373, 470)

```text
748:   exists, just with narrower scope (mostly North.). Examples with
749:   *a trigger that fire in WS too: wuton (< *witan, *a trigger),
750:   wutan wise men, gewuta. So in WS, trigger {*u, *a} both work.
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:774 (concept name)

- Nearby heading: ### B.2 Campbell, Old English Grammar sec. 218 (and 217, 219, 365, 373, 470)

```text
773:    in WS).
774: 2. *sw-, *kw-, *tw- clusters fire (wuton with optional w-loss,
775:    swustur, cwucu, twuwa).
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| SieversBrunner1965 | single available key for Sievers |
| Luick1914 | single available key for Luick |
| Kroonen2013 | explicit year mention (2013) |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |

## Paradigm probe

### Paradigm probe — fire / fȳre

- PROTO: *fūri
- PROTOFORM: *fūri
- DERIVATION_CLASS: known_unmodelled
- Morphology source: Hand-specified pilot comparison for the dat.sg. row input and the documented nominative-like outcome.
- ProtoGate bypassed: no
- Generated cells: dat.sg.
- Omitted cells: The inherited citation-form template is not yet generated automatically in v1; the probe centers on the TSV dat.sg. input and the known-problems interpretation.
- Winning form unique: no

| Cell | Candidate input | FST output | Match? | Comment |
|:---|:---|:---|:---|:---|
| dat.sg. | *fūri | fȳr | no | TSV input; attested target has analogically restored -e. |

