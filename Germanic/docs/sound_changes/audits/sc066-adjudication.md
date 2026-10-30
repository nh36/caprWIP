# SC066 adjudication — OE l-adjacent syncope

## Identity

- **SC id:** SC066
- **Executable identifier:** `OELAdjacentSyncope` (NOT a stage claim)
- **Date / branch / base commit:** 2026-10-30 / `update` / `6309e621`

## Question

- **Hypothesis or suspected problem (falsifiable):** The current single
  environment `{*i} -> 0 || V C+ _ {*l}` fires correctly on the three
  selected rows but asserts a broader historical claim than any
  consulted source: it would syncopate a kettle-type nominative
  (*katilaz → ×cetl) that every grammar keeps disyllabic. The comment
  block in `germanic.txt` explains the cetel contrast as "lexically
  variable", which is not a mechanism this project accepts. Suspected
  resolution: the three firings decompose into the regular
  heavy-syllable syncope (spindle, thistle) plus a light-syllable
  deletion that all categorical formulations restrict to OPEN medial
  syllables (nettle), with cetel's nominative falling outside the
  structural description altogether.
- **What evidence would confirm it; what would refute it:** Confirmed if
  (a) the handbooks state an open-syllable/weight conditioning under
  which cetel's nominative never meets the environment, and (b) a
  reformulated rule with that conditioning reproduces all 390 selected
  outputs while a kettle probe retains its medial vowel. Refuted if the
  sources demonstrate deletion in closed final syllables of the cetel
  shape, or if the reformulation changes any selected output.

## Current state (before any edits)

- **Existing historical characterization** (inventory + staging map):
  order 75, stage `oe`, english_specific, confidence A, unadjudicated.
  Registry display name "OE L Adjacent Syncope".
- **Existing executable behavior:**

  ```foma
  define OELAdjacentSyncope Ctx([
      {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant+ _ {*l},
      {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ {*l},
      {*i} -> 0 || EnglishStarDiphthong OEAnyConsonant+ _ {*l}
  ]);
  ```

  Cascade position: after `OEMedialSyncope` (SC065), before
  `OEDentalAssimilation` (SC067) and `OEPreconsonantalDegemination`
  (SC068); stage 76 of 108. The site is post-apocope: inputs are
  selected-cell strings such as `*s*p*i*n*n*i*l` with word-final `*l`.
  The accompanying comment block claimed the change "targets both *i
  and *e" (false — the rule deletes only `{*i}`) and called it
  "lexically variable (cetel 'kettle' does NOT syncopate)".
- **Selected-input assumptions:** nettle row 2139 `*nátilōn → netle`
  (nom.), spindle row 2208 `*spénnilō → spinl` (nom.), thistle row 2250
  `*θístilas → þistles` (GENITIVE cell). The genitive selection for
  thistle means the historically open medial syllable is restored by
  the following `*æ*s`; spindle's nominative reaches the rule as a
  closed-final-syllable string although the historical deletion
  happened in trisyllabic *spinnilō while the syllable was open.
- **Existing verdicts/dossiers consulted:** sc065-adjudication.md
  (methodological precedent; heavy-syllable law adjudicated),
  sc087-adjudication.md, cluster_adjudication_queue.md,
  syncope_cluster_comparative_dossier.md, chronology card
  SC066-oe-l-adjacent-syncope.md, book dossier
  066-068-syncope-and-degemination-corridor.book-dossier.md.

## Diagnosis

- **Complete firing census** (fresh `adjudicate.py SC066 --evidence`,
  2026-10-30; germanic.txt sha `5c160755…`, corpus sha `557113f8…`):
  3 of 390 selected rows change:
  - nettle `*n*e*t*i*l*ǭ → *n*e*t*l*ǭ` (→ netle) — light syllable,
    open medial syllable (following `*ǭ`).
  - spindle `*s*p*i*n*n*i*l → *s*p*i*n*n*l` (→ spinl) — heavy syllable
    (geminate `nn`), word-final `*l` at the rule site.
  - thistle `*θ*i*s*t*i*l*æ*s → *θ*i*s*t*l*æ*s` (→ þistles) — heavy
    syllable (cluster `st`), open medial syllable (following `*æ*s`).
- **Principal witness traces:** see census above and the counterfactual
  receipt (`sc066-068-experiments/counterfactual_receipt.json`):
  `sc066_retired` corrupts exactly these three rows and no others;
  `sc068_before_sc066` leaves nettle and thistle intact but strands
  spindle at `spinnl`. The kettle probe additionally exposed a symbol
  classification error: it reaches the rule as `*ʧ*ie*t*i*l` with
  unmarked `{*ie}` (WS palatal diphthongization of SHORT *e), which the
  diphthong classes kept in `EnglishStarLongDiphthong` with an explicit
  "pending probe" note — so the weight-split formulation alone still
  wrongly syncopated the probe via its heavy clause
  (`weight_open_split`, kettle VIOLATED). Reclassifying `{*ie}` as a
  short diphthong (the long product of *ē is `{*īe}`, already classed
  long; handbooks treat ie < *e as short) resolves the probe with zero
  corpus delta (`weight_open_split_ie_short`, kettle OK). Neither
  change alone suffices: under the old environment the probe deletes
  after any diphthong regardless of weight.
- **Witness role classification:**
  - nettle: live application (sole light-syllable witness).
  - spindle: live application + reciprocal SC066↔SC068 displacement
    witness + SC066→SC055 one-sided displacement witness.
  - thistle: live application (heavy clause; genitive cell).
  - milk (row 2126, meoloc): counterfeeding-negative control — medial
    `*u` must not delete (rule targets `{*i}` only), and Barrack's 390
    post-liquid deletion would corrupt it (receipt:
    `barrack_390_postliquid`).
  - kettle (*kátilaz, out-of-sample probe): negative control for the
    light-closed environment; not admitted to the corpus.
  - angel (*ángilaz, out-of-sample probe): latent heavy-closed
    overgeneration, identical in current and reformulated rule;
    documented residue.

## Literature

- **Existing CAPR dossiers checked:** barrack_1975/rule_census.tsv,
  barrack_to_capr.tsv, capr_crosswalk.tsv, citation_ledger.tsv,
  cluster_adjudication_queue.md, syncope_cluster_comparative_dossier.md.
- **Sources checked, with page numbers:**
  - Ringe & Taylor 2014 pp. 270–278 (§6.7.3–6.7.4): high vowels not
    syncopated after light syllables generally, but "unstressed *i in
    open syllables is often syncopated next to l" (fetlum, netle ~
    netele, dat. cryple, micle, yflan, yslan) "though apparently not of
    cytel, cetel 'kettle'" and not in the inflected forms of crypel
    'burrow'; they propose a change "arrested before it went to
    completion, giving rise to stable variation"; p. 273: *u does not
    syncopate next to l after light syllables (meoloc).
  - Sievers–Brunner 1965 §159c pp. 132–133 (with §159 Anm. 3): after a
    short syllable, i-syncope is "ziemlich regelmäßig" in the oldest
    sources except between stops and in d_l and Gmc f/β_l; late WS
    netele, cytele carry "neu entstandene Sekundärvokale" (anaptyxis);
    nom. sg. netl attested in CorpGl.
  - Luick 1914–40 §336 (following Weyhe 1905 pp. 94ff.): medial i (and
    e < i) before l deleted in TRISYLLABIC forms with open middle
    syllable, after all consonants except Gmc f and b; demonstrably
    pre-literary after t and þ, 8th century after gutturals; nearly
    common English, but part of the Saxon area resisted and influenced
    late WS; §336.2: medial u before l retained much longer (Nbr ~900;
    WS only after s and f, 10th/11th c.).
  - Campbell 1959 §388 (medial vowels "very freely dropped after short
    syllables" when a C+l/r group arises, with byforms yfle ~ yfele,
    betra ~ betera), §§389–391, §392 (heavy-syllable prehistoric law),
    §589 (netel/spinel class: nominative retains the vowel, oblique
    cases syncopate).
  - Hogg (& Fulk) 2011 §6.20 with n3 (netel as unapocopated ō-stem
    nominative; Angl. milc beside WS meolc).
  - Barrack 1975 (print verified 2026-10-30): rule 351 p. 87 — medial
    high-vowel deletion in open syllable after long accented syllable,
    with "In West-Saxon M6 undergoes PES with the dropping of lng 1"
    (his generalization to light syllables); rule 388 p. 96 — deletion
    of an unstressed vowel before liquid/nasal + vowel, with the
    sonorant term dropped by PES and "in some dialects, including
    West-Saxon, the environment … further simplified with the dropping
    of M7 entirely" (the following vowel); rule 390 p. 96 — post-liquid
    deletion V L V₂ C → V L Ø C, his derivation *meluk > meolc.
  - Orel 2003 p. 211 s.v. *katilaz (Lat. catillus loan; OE cytel).
  - Kroonen 2013 p. 384 s.v. *natōn- (dimin. *natilōn-); p. 82 s.v.
    *budman- ~ *buttman-.
- **Source-supported historical phenomenon:** (1) An exceptionless
  prehistoric deletion of unstressed high vowels in open medial
  syllables after heavy syllables (R/T §6.7.3, Campbell §392, Barrack
  351 core; adjudicated for the pre-dental slice as SC065). (2) A later
  deletion of *i before l that also applies after LIGHT syllables, in
  open medial syllables only, treated as categorical with
  consonant-class and date conditioning by Weyhe/Luick and
  Sievers–Brunner (netele anaptyctic), but as arrested variation by
  Ringe & Taylor (cryple vs. crypel). No source deletes *i in a
  closed final syllable of the cetel/netel nominative shape; nom. netl
  (CorpGl) is attested but treated by Brunner as spread from the
  syllabifiable inflected forms. (3) Medial *u next to l is NOT deleted
  in the relevant WS cells (meoloc).
- **CAPR modelling decisions (explicitly NOT source claims):** the
  selected-cell architecture feeds post-apocope citation-form strings;
  thistle's genitive cell and spindle's nominative cell are corpus
  selections; the executable split between SC065 (pre-dental) and SC066
  (pre-l) is architectural, not a claim of two historical laws
  operating by following-consonant class; placement of SC066 at a
  single cascade site compresses the real diachronic spread
  (pre-literary after dentals, 8th c. after gutturals).

## Historical analysis

- **Historical stage:** prehistoric-to-early Old English (heavy clause:
  prehistoric OE; light pre-l deletion: pre-literary after dentals per
  Luick §336, continuing into the literary period for other consonant
  classes).
- **Historical scope:** heavy-syllable law common OE (shared Germanic
  inheritance of weight-conditioned syncope); light pre-l deletion
  nearly common English with a resistant Saxon sub-area feeding late WS
  netele (Luick §336); CAPR's cascade stresses West-Saxon conditions.
- **Regular phonological conditioning:** deletion of unstressed `*i`
  (i) after a heavy syllable before `*l` (the SC065 law's pre-l slice;
  at the post-apocope site this includes spindle's closed final
  syllable because the historical deletion occurred in the open
  trisyllabic form), and (ii) after a light syllable before `*l` only
  in an OPEN medial syllable (following vowel required). No following
  vowel, no deletion: cetel's nominative is outside the structural
  description, not an exception to it.
- **Counterexamples and falsification:** cetel (probe: retained under
  the reformulation, wrongly syncopated under the old environment);
  meoloc (u, selected row, unaffected); R/T's crypel/cryple minimal
  pair and the netele byforms are recorded as the strongest evidence
  against a fully categorical light-syllable law — they concern
  consonant classes (post-labial/velar; Brunner's "between stops"
  exclusion) and inflected cells that the current corpus does not
  select, so the corpus does not discriminate Weyhe/Luick/Brunner
  categoricity from R/T's arrested variation. The executable clause
  (post-`t`, open syllable) lies in the territory ALL parties treat as
  deleted (pre-literary deletion after dentals).
- **Positive evidence for analogy:** none required and none invoked.
  Late WS netele is anaptyxis per Brunner (§159 Anm. 3), i.e. a later
  regular epenthesis, not analogical restoration; R/T's alternative is
  arrested sound change, also not analogy. The rejected explanation is
  the old comment's "lexically variable", which named no mechanism.
- **Relationship between historical phenomenon and executable proxy:**
  the reformulated rule is a NARROWER, corpus-exact proxy: heavy
  clauses (long V / diphthong + C+; short V + CC+) cover spindle and
  thistle; the light clause (short V + single C + `*l` + vowel) covers
  nettle and excludes the kettle shape. The reformulation also requires
  correcting the shared diphthong classes: `{*ie}` (WS palatal
  diphthongization of short *e) moves from `EnglishStarLongDiphthong`
  to `EnglishStarShortDiphthong`, resolving that class's own "pending
  probe" annotation; the move is extensionally identity on the selected
  corpus (receipt) and historically required (short nucleus → light
  syllable). Latent overgeneration remains
  for heavy-syllable closed-final nominatives of the engel type
  (gen. engles syncopates, nom. engel does not): the post-apocope site
  cannot distinguish *spinnil (historically trisyllabic) from a
  never-trisyllabic nominative. Out of corpus; requires the queued
  paradigm-cell policy, not a rule change here. The rule deletes only
  `{*i}` — the old comment's claim that it targets *e as well was
  false and is removed.
- **Chronology evidence:**
  - SC055 (OEIUmlaut) < SC066 — `independently_demonstrated`
    (displacement witnesses nettle, spindle: pre-umlaut shift yields
    nætle/spenl; chronology card SC066).
  - SC066 < SC068 — `independently_demonstrated` (reciprocal
    displacement witness spindle: SC068-early yields spinnl; fresh
    receipt `sc068_before_sc066`, rows_changed=1).
  - SC065 < SC066 — `stage_entailed` (adjacent composition order; no
    displacement witness distinguishes them in the current corpus).

## Verdict

- **Verdict:** REFORMULATE (executable environment narrowed to the
  source-supported weight/open-syllable conditioning; `{*ie}`
  reclassified as a short diphthong; comment block rewritten; no corpus
  output changes). The historical content is: the
  heavy-syllable syncope law plus the regular light-syllable pre-l
  deletion in open medial syllables.
- **Machine-readable line:**

Registry-verdict: SC066=REFORMULATE

- **Justification:** The previous environment `V C+ _ *l` reproduced
  the three selected rows but encoded an overbroad claim that would
  syncopate kettle-type nominatives, and its documentation explained
  the mismatch as lexical variability, which no consulted source
  asserts and this project does not accept. Every categorical source
  (Weyhe/Luick §336, Brunner §159c, Campbell §§388/589, Barrack 388)
  restricts the light-syllable deletion to open medial syllables, and
  R/T's variationist reading likewise concerns open syllables only.
  The reformulated clauses implement exactly that conditioning,
  reproduce all 390 selected outputs (receipt:
  `weight_open_split_ie_short`, rows_changed=0), and
  retain the kettle probe's medial vowel.

## Propagation (only after verdict)

- **Affected files/registries:** `Germanic/fsts/germanic.txt` (SC066
  define + comment block + `{*ie}` diphthong-class membership),
  `registry/sc_registry.tsv` (verdict),
  reader file `reader_facing/066-l-adjacent-syncope.md`, book dossier
  066-068, Barrack dossier tables (rule_census.tsv corrections for
  286/351/388/453/481.7; barrack_to_capr.tsv dispositions;
  capr_crosswalk.tsv; citation_ledger.tsv), comparative dossier and
  cluster queue; canonical refresh via `adjudicate.py --refresh`.
- **Regression tests added/updated:** evidence-interface census pins
  (3 firings unchanged); experiment receipt asserts control ==
  canonical and reformulation delta == 0; kettle/angel probes recorded
  in the receipt. Full suite reruns the corpus equivalence and
  fingerprint checks.
- **Baseline/fingerprint effect:** none expected — the reformulated
  rule is extensionally identical on the selected corpus (expanded-390
  fingerprint `35bbd32d…` unchanged); verified by Level B refresh and
  the strict suite.

## Residue

- **Unresolved uncertainty / deferred questions / author decisions
  required:**
  - Categorical (Weyhe/Luick/Brunner + anaptyxis) vs. arrested
    variation (R/T, crypel/cryple) for the light-syllable deletion
    outside the post-dental slice: the current corpus cannot
    discriminate; recorded in the reader discussion, no forced choice.
  - Latent engel-type heavy-closed overgeneration at the post-apocope
    site (shared by old and new formulation): awaits the paradigm-cell
    policy queued with SC067.
  - Consonant-class refinements (Brunner's "between stops"/d_l/f_l
    exclusions; Luick's dating ladder) are not expressible without
    witnesses; revisit only if such lexemes are admitted.
  - Barrack's PES generalizations (351/388) and his 390 post-liquid
    deletion are recorded as considered and rejected for CAPR's
    selected corpus (meoloc corruption; receipt
    `barrack_390_postliquid`).
