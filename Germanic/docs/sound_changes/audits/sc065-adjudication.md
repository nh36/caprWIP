# SC065 OE medial syncope adjudication (with lexical witness admission)

## Identity

- **SC id:** SC065
- **Executable identifier:** `OEMedialSyncope` (Foma `define` name; NOT a stage claim)
- **Date / branch / base commit:** 2026-10-29 / `update` / `2c5b139c`

## Question

- **Hypothesis or suspected problem (falsifiable):** SC065 fired on zero
  selected corpus rows at the start of this round. The suspected problem was
  threefold: (a) the rule might be vacuous dead weight; (b) its pre-dental
  restriction might be an unmotivated narrowing of the handbooks'
  weight-conditioned high-vowel syncope; (c) its cascade position (after
  high-vowel apocope, after i-umlaut) might be computationally arbitrary.
- **What evidence would confirm it; what would refute it:** Vacuousness is
  confirmed if replacing the rule with identity changes no selected output
  and no admissible lexical witness exists; it is refuted by admitting an
  independently defensible *-iþō abstract whose derivation requires the
  rule. The restriction is unmotivated if broadening it (to *u, or to any
  following consonant, or to the handbook open-syllable law) leaves all
  selected outputs correct; it is load-bearing if any broadening corrupts
  previously correct predictions. The position is arbitrary if the rule can
  move before OEIUmlaut or before OEHighVowelApocope without changing any
  witnessed output.

## Current state (before any edits)

- **Existing historical characterization** (inventory + staging map rows,
  quoted): registry row SC065: `active · historical_sound_change · Old
  English · OEMedialSyncope · "OE Medial Syncope" · hist_stage oe ·
  hist_scope english_specific · confidence A · adjudication_status
  unadjudicated`. The germanic.txt comment block characterized the rule as
  "R/T §6.8, Campbell §§389-393: medial high vowel syncope" best attested
  in *-iþō- abstracts "(strengþu, hǣlþu, fyrhtu, wiermþu)" — none of which
  were in the pipeline.
- **Existing executable behavior** (rule text; environment; cascade
  position): three-clause deletion of `{*i}` after a heavy syllable
  (long vowel + C⁺, long diphthong + C⁺, or short vowel + CC⁺) before a
  dental obstruent `[{*θ}|{*ð}|{*d}|{*t}]`, wrapped in `FootCtx`;
  composed at cascade order 74, after `OEIUmlaut` (65) and
  `OEHighVowelApocope` (72). Firing census before this round: 0 of 389
  selected rows.
- **Selected-input assumptions** (which cell/citation form the corpus
  feeds; what is pre-encoded in the protoforms): the corpus feeds
  endingless OE nominative singulars of the *-iþō feminine abstracts via
  the regular phonological route PGmc `*-iθō` > PNWGmc `*-iθu` (final-ō
  raising) > apocope of `*-u` after the resulting heavy syllable > medial
  syncope. Nothing SC065-specific is pre-encoded in the protoforms; the
  new witness enters as plain PGmc `*fūliþō`.
- **Existing verdicts/dossiers consulted:** SC087 adjudication
  (`audits/sc087-adjudication.md`) for method and the cress residue;
  Barrack 1975 dossier (`literature_dossiers/barrack_1975/`: rule census,
  crosswalk, research agenda); reader chapter `065-medial-syncope.md`;
  chronology card `SC065-oe-medial-syncope.md` (negative first-break
  result, now superseded in part — see Chronology evidence).

## Diagnosis

- **Complete firing census** (every lexeme the rule changes, both
  corpora; in-domain vs out-of-domain): before admission: 0 rows. A
  whole-corpus near-miss census over all 389 pre-SC065 stage outputs
  found exactly one medial high vowel in a syncope-like configuration:
  head 2063 `*ç*ēa*β*u*d` (hēafod), whose `*u` before a dental is
  correctly skipped by the i-only restriction. After admission of filth
  (row 2335, PGmc `*fūliþō` → OE `fȳlþ`): 1 firing, filth, in-domain.
  No out-of-domain applications.
- **Principal witness traces** (form immediately before/after the rule;
  counterfactual skip/displacement where chronology is at issue): filth
  canonical trace: `*fūliθō` → (PNWGmcFinalLongORaising) `*fūliθu` →
  (OEIUmlaut) `*fȳliθu` → (OEHighVowelApocope) `*fȳliθ` →
  (OEMedialSyncope) `*fȳlθ` → `fȳlþ`. Counterfactual skip (rule
  retired): `fȳleþ`, unattested. Counterfactual displacement before
  OEIUmlaut: `fūlþ`, unattested (the syncopated `*i` can no longer
  trigger umlaut). Out-of-sample probes (not admitted): health `*xáiliþō`
  → `hǣlþ`, theft `*θéubiþō` → `þīefþ`, warmth `*wármiþō` → `wiermþ`,
  all matching the attested abstracts; under displacement before umlaut
  they yield unattested `hālþ`, `þēofþ`.
- **Witness role classification** (per witness): filth — live
  application, and displacement witness for OEIUmlaut < SC065 (bleeding
  under the counterfactual early order). health/theft/warmth —
  out-of-sample live-application probes confirming the same pattern.
  head (2063) — negative control for the i-only restriction. harvest
  (2057) and shilling (2181) — negative controls for the pre-dental
  restriction (corrupted to rejection under `any_consonant`). soul
  (2201) — negative control for the cascade site (corrupted to `sāwl`
  by the handbook open-syllable law composed pre-apocope).
  strength/length probes — recorded but unsuitable as witnesses: the
  current cascade renders them with palatal `ġ` (`strenġþ`, `lenġþ`)
  against attested velar `strengþu`; this is an unresolved
  palatalization-chronology issue independent of SC065 (see Residue).

## Literature

- **Existing CAPR dossiers checked:** Barrack 1975 dossier (rule census
  rows 345, 347, 351, 358, 359, 388, 390; crosswalk; research agenda
  part on vowel loss); SC087 adjudication memo; reader chapters 063–068.
- **Sources checked, with page numbers:** Ringe & Taylor 2014 §6.7.3
  (pp. 264–267, weight-conditioned loss of medial *i/*u) and §6.8
  (pp. 268 ff.); Campbell 1959 §§388–393 (pp. 157–159) and §589.6
  (p. 236, the *-iþō abstracts, fȳlþ among them); Luick §306; Bülbring
  §§431–439; Hogg 1992 §6.19 ff.; Kroonen 2013 p. 158 s.v. *fūla-
  (deriving *fūliþō, citing OS fulitha 'filth'); Toller 1921 Supplement
  p. 276 s.v. fylþ (attestations An. Ox. 3323, Scint. 38,19; inflected
  fylþu An. Ox. 1790; OS fúlitha and OHG fülida cognates); Clark Hall
  1960 p. 125 (fýlð f.); Bammesberger 1990 §4.5 pp. 117–118 (the *-iþō
  type); Orel 2003 p. 121 s.v. *fūlaz (the adjectival base, OE fūl;
  no *-iþō abstract is listed); Barrack 1975 pp. 86–87 (rules
  345/347/351), p. 90 (358/359), p. 96 (388/390).
- **Source-supported historical phenomenon** (exactly what the sources
  demonstrate): a regular Old English loss of unstressed medial high
  vowels in open syllables after heavy syllables, ordered after
  i-umlaut (the abstracts show umlauted root vowels) and interacting
  with high-vowel apocope; the *-iþō abstracts (Campbell §589.6)
  uniformly show syncope: strengþu, hǣlþ(u), fȳlþ, þīefþ, wiermþu.
- **CAPR modelling decisions** (explicitly NOT source claims): the
  pre-dental consonant enumeration `[θ|ð|d|t]` is an executable proxy,
  not a historical conditioning claim: no handbook restricts the
  syncope to pre-dental position. CAPR restricts the rule because at
  its cascade site (after apocope) the handbook open-syllable condition
  is unstatable, and broader statements corrupt selected outputs (see
  Historical analysis). Likewise i-only (excluding *u) is a
  site-specific proxy choice protecting hēafod, whose medial *u the
  handbooks treat under separate developments.

## Historical analysis

- **Historical stage:** Old English (pre-literary; the abstracts are
  fixed in syncopated shape across early WS and Anglian texts).
- **Historical scope (geographical/genealogical):** English-specific as
  implemented; the cognate OS fulitha and OHG fülida retain the medial
  vowel, so the deletion is not common West Germanic.
- **Regular phonological conditioning** (phonetic/prosodic environment):
  historically, unstressed medial high vowel in an open syllable
  following a heavy syllable (weight-conditioned, foot-based). The
  executable statement conditions on a heavy left flank and a following
  dental obstruent because it applies post-apocope, where the open-
  syllable requirement cannot be expressed.
- **Counterexamples and falsification** (including non-morpheme-matched
  forms sharing the proposed phonological environment; evidential gaps):
  the controlled counterfactuals falsify every tested broadening at the
  current site: `u_extension` (targets *u too) corrupts hēafod →
  `hēafd`; `any_consonant` (drops the dental restriction) corrupts
  harvest and shilling to rejection; the handbook open-syllable law
  composed at the current site (`open_syllable_insitu`) never fires
  there — post-apocope the medial syllable is closed — so it corrupts
  the admitted witness (filth → `fȳleþ`) and fails every out-of-sample
  probe; the same law composed
  pre-apocope derives all witnesses correctly but corrupts soul →
  `sāwl` (the hēafudu-type medial-*u problem; cf. Goering 2023 on the
  bimoraic trochee). Evidential gap: with only one admitted firing, the
  corpus cannot discriminate the dental enumeration from, e.g., a
  θ-only statement; the enumeration follows the handbook class of weak
  preterite and comparative environments not yet in the pipeline.
- **Positive evidence for analogy** (if none, say so): none required
  for the selected cell. Campbell §589.6 derives the endingless
  nominative singular of the *-iþō abstracts analogically (after the
  lār-type ō-stems), whereas CAPR reaches `fȳlþ` by the regular
  phonological route (raising > apocope > syncope). Both routes
  converge on the attested form; the corpus form does not decide
  between them, and the SOURCE apparatus for row 2335 records
  Campbell's analogical account explicitly. No demonstrated failure of
  the regular account exists.
- **Relationship between historical phenomenon and executable proxy**
  (narrower proxy? overgeneration? exact match? why): deliberately
  narrower proxy. The historical law is weight-conditioned high-vowel
  syncope in open medial syllables; the executable rule implements the
  slice of that law recoverable at a post-apocope cascade site —
  *i-only, pre-dental — which handles every selected and probed
  abstract correctly and nothing else. The experiments show this
  narrowing is load-bearing, not decorative: every broadening tested
  at the site corrupts a previously correct prediction, and the
  faithful handbook formulation is only statable pre-apocope, where it
  breaks soul. Retaining the proxy is therefore an executable-
  architecture decision, documented as such; it is not a claim that
  the historical change was pre-dental.
- **Chronology evidence** — list each edge and mark it
  `stage_entailed` or `independently_demonstrated`, with the witness
  and its role:
  - SC055 OEIUmlaut < SC065 — `independently_demonstrated`;
    displacement witness filth: composing the identical rule before
    OEIUmlaut bleeds the umlaut trigger, yielding unattested `fūlþ`
    for attested `fȳlþ` (probes agree: `hālþ`, `þēofþ`). New
    chronology edge recorded.
  - SC063 OEHighVowelApocope ~ SC065 — not discriminated by the
    admitted corpus: under the pre-dental formulation filth syncopates
    whether or not final `*-u` is still present, so the admitted
    witness does not order the two rules. (The handbook open-syllable
    formulation would require syncope before apocope, but that
    formulation is not the executable rule.) No edge promoted.
  - Later boundary: unchanged negative result (no later real break
    before the runner limit; see chronology card).

## Verdict

- **Verdict:** RETAIN executable rule; historical characterization
  clarified in reader prose (executable pre-dental statement is a
  narrow proxy of the weight-conditioned handbook law, now witnessed).
- **Machine-readable line** (must match the `verdict` column in
  `registry/sc_registry.tsv`; slash-join multiple tokens):

Registry-verdict: SC065=RETAIN

- **Justification (2–5 sentences):** The zero-firing census was a
  corpus coverage gap, not a vacuous rule: admitting the independently
  reconstructed witness *fūliþō → fȳlþ (Kroonen p. 158; Toller Suppl.
  p. 276; Campbell §589.6) gives SC065 a live, source-backed firing,
  and retiring the rule now corrupts that row (`fȳleþ`). Controlled
  counterfactuals demonstrate that both executable restrictions
  (*i-only; pre-dental) are load-bearing at the current cascade site
  and that the faithful handbook formulation either never fires there
  (corrupting the witness) or corrupts soul when moved pre-apocope. The
  displacement experiment
  supplies a new independently demonstrated chronology edge OEIUmlaut
  < SC065. The rule is retained unchanged as a deliberately narrow,
  now-witnessed executable proxy of the handbook weight law.

## Propagation (only after verdict)

- **Affected files/registries:**
  - `Germanic/data/germanic-aligned-final.tsv` — row 2335 (filth)
    appended (lexical admission).
  - `Germanic/docs/lexeme_reports/pgmc_reconstructions/{coverage,forms,analyses,comparisons,rationales}.tsv`
    and `pgmc_integration/editorial_inventory.tsv` — full SOURCE
    apparatus for row 2335.
  - `Germanic/docs/sound_changes/cascade_baseline/` — baseline migrated
    389 → 390 rows (see Baseline/fingerprint effect).
  - `registry/sc_registry.tsv` — SC065 adjudicated/RETAIN/memo path;
    chronology summary updated.
  - `registry/chronology_edges.tsv` — new edge SC065→SC055
    (`broad_far_chronology`, `independently_demonstrated`,
    displacement witness filth); existing boundary rows' notes updated.
  - `Germanic/fsts/germanic.txt` — SC065 comment block updated to cite
    fȳlþ as the live witness (comment only; rule text untouched).
  - `reader_facing/065-medial-syncope.md` + book dossier — revised per
    verdict; Barrack dossier crosswalk/citation ledger —
    examined-in-SC065 dispositions.
  - `audits/sc065-experiments/{experiment.py,counterfactual_receipt.json}`
    — harness and machine-readable receipt (receipt regenerated against
    the admitted 390-row corpus).
- **Regression tests added/updated** (positive AND negative controls):
  `Germanic/tests/test_sc065_adjudication.py` — rule-shape pin;
  whole-corpus runtime firing census over ALL selected rows expecting
  exactly {filth}; negative controls (head, harvest, shilling retain
  their selected outputs; rule does not syncopate *u or pre-non-dental
  *i); chronology-edge registry pin; receipt-pinning tests.
- **Baseline/fingerprint effect** (expected none / changed): changed by
  admission only. `cascade_baseline_outputs.tsv` gained exactly one row
  (2335 filth, accepted, matched); 390 rows, 390 accepted, 382 matched,
  8 mismatched (the 8 pre-existing mismatches unchanged);
  `outputs_sha256` now `35bbd32df3f8…`; `legacy_subset_sha256`
  unchanged (`9fb5d393…`), proving no legacy row's derivation moved.
  No FST rule text changed; the production-control variant matches
  canonical output on every selected row.

## Residue

- **Unresolved uncertainty / deferred questions / author decisions
  required:**
  1. strength/length (*strángiþō, *lángiþō) are unusable as witnesses
     because the current cascade outputs palatal `ġ` (`strenġþ`) where
     the attested abstracts have velar g (strengþu): an unresolved
     palatalization/syncope chronology interaction. Recorded as an
     issue for the palatalization complex; NOT adjudicated here.
  2. The SC066 comment in germanic.txt describes l-adjacent syncope as
     "lexically variable (cetel …)", which is in tension with the
     project's neogrammarian stance; flagged for the SC066
     adjudication, untouched here.
  3. Campbell's analogical route to the endingless nominative
     (§589.6) vs CAPR's phonological route: both derive fȳlþ; recorded
     in the row-2335 SOURCE apparatus; no corpus evidence discriminates.
  4. SC063 ~ SC065 relative order remains undiscriminated by the
     admitted corpus under the executable formulation (see Chronology
     evidence).
  5. Weak-preterite (*-idē) and comparative (*-ira) syncope
     environments remain outside the corpus; the dental enumeration
     covers them prospectively but untested.
