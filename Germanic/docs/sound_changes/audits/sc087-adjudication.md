# SC087 r-metathesis adjudication (Barrack 459.1/459.3)

## Identity

- **SC id:** SC087
- **Executable identifier:** `OERMetathesis` (NOT a stage claim)
- **Date / branch / base commit:** 2026-10, `update`, on top of
  `3cb109c9` (Barrack dossier QC `7eb79806` + test maintenance), itself
  following the Barrack phase-1 integration `d58f8c86`/`493b4ec7`.

## Question

- **Hypothesis or suspected problem (falsifiable):** Barrack (1975:
  115–18) rules 459.1 and 459.3 describe a broader r-metathesis complex
  than CAPR's SC087: progressive rV > Vr before *s or *n generally (459.1,
  with environment-simplification stages), and a regressive V́r > rV́
  before *xt (459.3). Hypothesis H2: SC087 is historically too narrow and
  should be broadened to the s/n domain. Hypothesis H3: the regressive
  pre-xt type is a separate missing law (SPLIT). H1: the current narrow
  `C _ st` law is the correct exceptionless West Saxon statement and the
  broader phenomena are variable/dialectal, handled by lexical selection.
- **What evidence would confirm it; what would refute it:** H2/H3 are
  confirmed if the sources treat the broader domains as regular
  (exceptionless) in West Saxon and if broadened counterfactual rules
  improve or at least do not damage the 389-row corpus. They are refuted
  if the sources themselves grade the broader domains as variable and the
  counterfactual rules corrupt attested selected outputs while deriving
  nothing new.

## Current state (before any edits)

- **Existing historical characterization:** registry row SC087: active
  historical_sound_change, pipeline stage Old English, hist_stage `oe`,
  hist_scope `english_specific`, confidence A, display name "OE R
  Metathesis", chronology profile `broad_far` (earlier boundary across
  SC044; later search runner-limited), status `unadjudicated`.
- **Existing executable behavior:** `define OERMetathesis` — eight
  clauses `{*r} {V} -> {V} {*r} || EnglishStarConsonant _ {*s} {*t}` for
  V ∈ {e,u,i,o,a,é,ó,á}; composed as tracer stage 99 of 108, immediately
  after `OEContraction`. The left consonant context was added earlier to
  protect word-initial *r (*rústaz > rust, not †orst; DEV_NOTES §17.42).
- **Selected-input assumptions:** corpus PROTOFORMs are PGmc citation
  forms; row 1974 burst *bréstaną > berstan and row 2035 frost *frústą >
  forst are the selected metathesized targets. Rows 2161 run *rínnaną >
  rinnan and 2045 grass *grásą > græs deliberately select the
  unmetathesized doublet variants (both attested; Campbell §459).
  Precedent: row 2273 wasp documents late-WS variable metatheses (wæps,
  wæsp) deliberately not implemented as laws.
- **Existing verdicts/dossiers consulted:** barrack_1975 dossier (census
  rows 459.1, 459.3; reverse index; QC report), chronology card
  SC087-oe-r-metathesis.md, book dossier 079-087, reader entry
  087-r-metathesis.md, sc023-adjudication.md (census methodology
  precedent), wasp corpus note.

## Diagnosis

- **Complete firing census:** `adjudicate.py SC087 --evidence` (fresh
  stage bins, container rebuild): exactly 2 of 389 selected rows fire —
  burst `*b*r*é*s*t*a*n` → `*b*é*r*s*t*a*n` (berstan) and frost
  `*f*r*ó*s*t` → `*f*ó*r*s*t` (forst). Both are in-domain live
  applications (rV́st > V́rst). No out-of-domain firing exists.
- **Principal witness traces:** stage-98 (post-OEContraction) inputs and
  stage-99 outputs listed above; all other r-bearing rows pass the stage
  unchanged, including the negative controls brand `*b*r*á*n*d*e*s`,
  drench `*d*r*e*n*ʧ`, string `*s*t*r*e*n*ʤ`, grass `*g*r*æ*s`, run
  `*r*í*n*n*a*n`, fright `*f*y*r*x*t*e`.
- **Counterfactual displacement (chronology):** the registry edge
  SC087 → SC044 (earlier boundary) is independently demonstrated by the
  burst displacement witness: metathesis shifted before breaking yields
  †beorstan for expected berstan. Later search reaches the runner limit
  with no real break.
- **Counterfactual broadening (this adjudication,
  `audits/sc087-experiments/experiment.py`, receipt.json):** five full
  cascade variants were compiled and applied to all 389 selected rows,
  with a truncation-identical production control that matched the
  canonical `old_english.bin` on every row before any comparison:
  - `broad_s` (drop the *t requirement; rV > Vr before any *s): 0 rows
    change — within this corpus the *st restriction and the plain *s
    domain are extensionally equivalent for the stressed-vowel clause
    set.
  - `broad_sn` (Barrack 459.1 matrix: before *s or *n): 3 rows corrupted,
    0 improved — brandes → †barndes, drenċ → †dernċ, strenġ → †sternġ.
  - `broad_sn_ae` (vowel set extended to the fronted *æ/*y present at the
    cascade site): 4 rows corrupted — additionally græs → †gærs.
  - `broad_sn_noleft` (Barrack's literal matrix has no left consonant
    requirement): 9 rows corrupted — additionally faran → †faarn,
    hameres → †hameers, ræste → †ærste, rust → †orst (re-demonstrating
    the DEV_NOTES §17.42 protection), sċieran → †sċiearn. (Run/rinnan
    escapes only because the clause enumeration lacks accented *í; a
    fully literal Barrack matrix would corrupt it too.)
  - `regressive_459_3` (V́r > rV́ / _ xt composed after OERMetathesis):
    1 row corrupted, 0 improved — fyrhte → †fryhte.
- **Witness role classification:** burst, frost — live applications;
  burst additionally the displacement witness for the SC044 edge; brand,
  drench, string, grass, run, fright — counterfactual negative controls
  (corrupted only under the rejected broadened variants); rust —
  protected by the left context (historical control from DEV_NOTES
  §17.42, re-demonstrated by `broad_sn_noleft`).

## Literature

- **Existing CAPR dossiers checked:** barrack_1975 (census, reverse
  index barrack_to_capr.tsv rows 459.1/459.3, citation ledger).
- **Sources checked, with page numbers:**
  - Barrack 1975: 115–17 (459.1 and discussion I–III E), 117–18 (459.3),
    34 (formal vs historical ordering), 81 (331.6a context). Verified
    against the printed page images, not the OCR transcript.
  - Campbell 1959: §155 (metathesis usually too late to feed breaking,
    except *i before rC), §459 (doublets: forst~frost, cerse~cresse,
    gærs~græs, rinnan~iernan/eornan etc.; §459.3 regressive practically
    limited to position before ht, mainly late Northumbrian; §459.4 low
    stress promotes metathesis, -ferþ names).
  - Ringe & Taylor 2014: 340–41 ("common, but variable, metathesis";
    Anglian burn/run metathesis fed breaking (Stanley 1952), West Saxon
    metathesis followed breaking; gærs~græs as evidence for contrastive
    /æ/).
  - Hogg 2011 (Vol. 1): §§5.26, 7.93–7.96 (r-metathesis before short
    vowel + s/n clusters; only "half-breaking" of *i is fed, normal
    breaking is not; rejects Luick's early-metathesis account of EWS
    biernan; the regressive pre-xt type is mainly late Northumbrian and
    is better analysed as epenthesis plus stress shift, with Brunner,
    pace Campbell).
- **Source-supported historical phenomenon:** Old English r-metathesis
  before s/n clusters is real, widespread and chronologically and
  dialectally heterogeneous. Every consulted source characterizes the
  broader domain as variable: Barrack himself grades his own
  environment-simplification stages ("a late stage of free variation",
  p. 116); Campbell's §459 lists pervasive unmetathesized doublets for
  precisely the forms a broad law would convert; Ringe & Taylor call it
  "common, but variable". The only exceptionless, West Saxon, corpus-
  relevant core is rV > Vr in the C_st environment (berstan, forst). The
  regressive pre-xt type rests on meager, mainly late-Northumbrian
  evidence (Barrack: "the evidence of this change is very meager", p.
  118; Campbell §459.3; Hogg §7.96 reanalyses it as epenthesis).
- **CAPR modelling decisions (explicitly NOT source claims):** the left
  consonant context (word-initial-r protection) is a CAPR corpus-exact
  statement of the West Saxon selection, not Barrack's matrix; the
  eight-vowel clause set is a notation-level enumeration; the cascade
  slot after OEContraction is compositional, not a dating.

## Historical analysis

- **Historical stage:** Old English (West Saxon target), unchanged.
- **Historical scope:** english_specific, unchanged. The Anglian
  pre-breaking metathesis of the burn/run family (Ringe & Taylor 341;
  Barrack's dialect-differentiated staging, pp. 116–17) is outside
  CAPR's West Saxon executable target.
- **Regular phonological conditioning:** r + short vowel > vowel + r
  before the st cluster, after a consonant — purely phonological; no
  grammatical or lexical conditioning. The broader s/n domain fails the
  exceptionless test in West Saxon: attested brandes, drenċ, strenġ,
  græs, rinnan all retain rV/Vr order in the selected forms, while the
  metathesized members of these doublet families (gærs, iernan, etc.)
  are precisely the variants Campbell and Ringe & Taylor class as
  variable. A neogrammarian law cannot be written over a domain whose
  outputs are doublets; CAPR handles such families by lexical selection
  (precedent: wasp row 2273).
- **Counterexamples and falsification:** the counterfactual receipts are
  the falsification record of H2/H3: every broadened variant strictly
  damages the corpus (3, 4 and 9 corrupted rows respectively, including
  rust under the literal Barrack matrix) and derives zero new correct
  outputs. No in-corpus form requires the broader law.
- **Positive evidence for analogy:** none required or invoked; the
  doublet distributions are inter-dialectal variation and lexical
  selection, not paradigm analogy.
- **Relationship between historical phenomenon and executable proxy:**
  the proxy is deliberately narrower than the full historical metathesis
  complex: it states the exceptionless West Saxon core (C_st) and leaves
  the variable s/n periphery, the Anglian pre-breaking metathesis, and
  the meager regressive pre-xt type to lexical selection and prose. It
  does not overgenerate; the counterfactuals show every broadening
  overgenerates.
- **Chronology evidence:**
  - SC087 after SC044 (breaking): `independently_demonstrated`,
    displacement witness burst (early metathesis ⇒ †beorstan). Supported
    by Campbell §155 and Ringe & Taylor's West Saxon ordering; Barrack's
    157 > 170a > 459.1 formal ordering agrees for West Saxon, though his
    ordering is formal, not chronological (p. 34).
  - Later boundary: runner-limited `boundary_observation`, unchanged.
  - No new edge is proposed. Barrack's dialect-differentiated staging
    (Anglian metathesis before breaking) concerns a scope CAPR does not
    execute and licenses no West Saxon edge.

## Verdict

- **Verdict:** RETAIN — the executable rule, its conditioning, stage,
  scope, cascade position and chronology edges are all unchanged. The
  Barrack-derived broadenings (H2) and the regressive split (H3) are
  rejected on the paired evidence of the sources' own variability
  grading and the strictly damaging counterfactual receipts.
- **Machine-readable line:**

Registry-verdict: SC087=RETAIN

- **Justification:** Every consulted source — including Barrack himself —
  treats r-metathesis outside the C_st core as variable, dialectally
  heterogeneous or meagerly attested, which already disqualifies it as an
  exceptionless West Saxon law. The executable counterfactuals confirm
  this independently: every s/n broadening corrupts attested selected
  outputs (barndes, dernċ, sternġ, gærs, and word-initial-r damage up to
  orst for rust), the bare *s broadening is extensionally vacuous on this
  corpus, and the regressive 459.3 variant
  corrupts fyrhte. The current narrow law is corpus-exact: it fires on
  exactly burst and frost, both correctly.

## Propagation (only after verdict)

- **Affected files/registries:** `registry/sc_registry.tsv` (SC087
  adjudication status/verdict/memo columns, via the canonical finalize
  interface); `reader_facing/087-r-metathesis.md` (corrected
  459.1/459.3 attribution — cyrps/firiþ belong to 459.1's discussion,
  459.3 is the regressive worhte~wrohte type — and added doublet/
  negative-control discussion); barrack_1975 dossier census row 459.3
  (pages 117–18, worhte~wrohte example, "very meager") and reverse-index
  rows for 459.1/459.3 updated to ADJUDICATED_RETAIN. No FST, corpus,
  staging, chronology or baseline change.
- **Regression tests added/updated:** `test_sc087_adjudication.py` —
  rule-shape stability (8 clauses, left context, st cluster, no nasal,
  no regressive rule in production), live firing census exactly
  {burst, frost} with domain checks, six negative controls untouched at
  the stage, and the SC044 displacement edge pinned.
- **Baseline/fingerprint effect:** none — RETAIN changes no executable
  behavior; the production control in the experiment matched the
  canonical bin on all 389 rows.

## Residue

- Anglian pre-breaking metathesis of the burn/run family (beornan/
  biernan/byrnan; iernan/iornan) is real, source-supported and outside
  the current West Saxon executable target; it would become relevant only
  if CAPR adds an Anglian branch.
- cærse 'cress' and the cyrps/firiþ (-ferþ names) types are genuine
  metathesis witnesses not in the corpus; adding them would require
  independent reconstruction work (cress < *krasjōn with umlaut
  interaction; low-stress second elements for -ferþ) and would not
  change the verdict, since their families are doublet-graded in the
  sources.
- The late West Saxon regressive/sporadic metatheses (wæps/wæsp type,
  áscian/ácsian 440b) remain documented, unimplemented variation;
  Barrack 440b is queued in the Part IV research agenda.
