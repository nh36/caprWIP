# SC068 adjudication — OE preconsonantal degemination

## Identity

- **SC id:** SC068
- **Executable identifier:** `OEPreconsonantalDegemination` (NOT a stage
  claim)
- **Date / branch / base commit:** 2026-10-30 / `update` / `6309e621`

## Question

- **Hypothesis or suspected problem (falsifiable):** (1) Whether the
  degemination of *tt (bottom) and *nn (spindle) before sonorants is one
  regular historical change or an artificial union of distinct
  developments; (2) whether the SC066 < SC068 ordering is independently
  established or an artifact of the computational decomposition; (3)
  whether Barrack's more general cluster simplification (rule 476)
  shows the CAPR formulation to be wrongly conditioned.
- **What evidence would confirm it; what would refute it:** A split
  would be required if the sources assign the *ttm and *nnl
  simplifications to different changes, conditions or periods; it is
  refuted if the grammars state one general degemination adjacent to a
  consonant covering both. The ordering is independent if a lexical
  witness breaks under permutation for historical (not merely
  technical) reasons.

## Current state (before any edits)

- **Existing historical characterization:** order 77 (stage 78 of 108),
  stage `oe`, english_specific, unadjudicated. Registry display name
  "OE Preconsonantal Degemination".
- **Existing executable behavior:**

  ```foma
  define OESonorant [{*m}|{*n}|{*l}|{*r}];
  define OEPreconsonantalDegemTT [ {*t} -> 0 || {*t} _ OESonorant ];
  define OEPreconsonantalDegemNN [ {*n} -> 0 || {*n} _ OESonorant ];
  define OEPreconsonantalDegemination Ctx(OEPreconsonantalDegemTT .o. OEPreconsonantalDegemNN);
  ```

  Cascade position: after `OEDentalAssimilation` (SC067), before
  `OEPostVelarWLoss`. The comment block correctly describes the rule as
  a case-by-case application of R/T §6.8.1's general degemination,
  restricted to pre-sonorant position to avoid regressing intervocalic
  geminates and gemination products before *j.
- **Selected-input assumptions:** bottom row 1959 `*búttmaz → botm`
  (Kroonen's geminate stem variant pre-encodes *tt in the protoform);
  spindle row 2208 `*spénnilō → spinl` (the *nnl cluster is created
  in-cascade by SC066).
- **Existing verdicts/dossiers consulted:** sc066-adjudication.md (this
  round), sc065-adjudication.md, chronology card
  SC068-oe-preconsonantal-degemination.md, book dossier 066-068,
  barrack_1975 dossier tables, cluster_adjudication_queue.md.

## Diagnosis

- **Complete firing census** (fresh `adjudicate.py SC068 --evidence`,
  2026-10-30; germanic.txt sha `5c160755…`, corpus sha `557113f8…`):
  2 of 390 selected rows change:
  - bottom `*b*ó*t*t*m → *b*ó*t*m` (→ botm) — inherited geminate;
    independent of SC066.
  - spindle `*s*p*i*n*n*l → *s*p*i*n*l` (→ spinl) — geminate exposed by
    SC066's syncope.
- **Principal witness traces** (counterfactual receipt,
  `sc066-068-experiments/counterfactual_receipt.json`):
  - `sc068_retired`: bottom → bottm, spindle → spinnl (and nothing
    else changes). No later rule repairs either cluster, so the rule
    carries live explanatory load for both rows.
  - `sc068_before_sc066`: spindle → spinnl; bottom unaffected. The
    ordering constraint is carried by spindle alone.
- **Witness role classification:**
  - bottom: live application; NOT an ordering witness (its geminate is
    inherited, not syncope-fed).
  - spindle: live application + reciprocal SC066↔SC068 displacement
    witness (feeding: SC066 creates the *nnl cluster).
  - Gemination products before *j and intervocalic geminates
    (e.g. settle-type, sellan-type rows): counterfeeding-negative
    controls motivating the pre-sonorant restriction (documented in the
    production comment; no corpus row changes under the current rule
    beyond the two above).

## Literature

- **Existing CAPR dossiers checked:** barrack_1975 tables (rule_census,
  barrack_to_capr, capr_crosswalk, citation_ledger),
  syncope_cluster_comparative_dossier.md, cluster_adjudication_queue.md.
- **Sources checked, with page numbers:**
  - Ringe & Taylor 2014 p. 296 (§6.8.2 context): "geminate consonants
    were also degeminated next to another consonant (cf. cyste, brycte
    above)", with the caution that these assimilations "could have been
    more or less automatic consequences of syncope"; §6.8.1 (pp.
    279–296) for the syncope-fed cluster families; pp. 332, 354 for
    botm.
  - Barrack 1975 (print verified 2026-10-30): rule 476 p. 122 — general
    cluster simplification in BOTH directions, (A) C₁C₁C₂ → C₁C₂ and
    (B) C₂C₁C₁ → C₂C₁ (derivations: seldl- > sellic; wiersa; þridda ~
    þirda; cyning > 477b > 476 cyng), ordered after the syncope rules
    (459.1; 481.2; 358; 351 > x); rule 457b p. 115 — degemination
    V C₁C₁ → V C₁ (acumba > LWS acuma; neahhebur), distinct from 476;
    rule 286 p. 71 — vowel shortening before geminates (blīþs > bliss
    path), NOT a cluster simplification (census gloss corrected this
    round); rule 453 pp. 114–115 — gemination before liquids after
    short vowels (betr- > bettr-), i.e. the OPPOSITE direction,
    likewise fed by syncope (388, 355.1, 351 > x).
  - Kroonen 2013 p. 82 s.v. *budman- ~ *buttman-: "OE botm <
    *buttma-"; Kroonen 2006 (mn-stems) for the paradigm *budmē ~
    *buttaz behind the stem variants.
  - Ringe & Taylor 2014 pp. 332, 354: alternative derivation of botm
    from *buþm- with WS *þm > tl/tm-type developments (ME bothem),
    concluding "we cannot recover in any detail what happened to these
    words" (citing Weyhe 1905: 67–75).
- **Source-supported historical phenomenon:** a general simplification
  of geminates adjacent to another consonant in the period after the
  OE syncopes (R/T §6.8.1/6.8.2; Barrack 476 with explicit
  post-syncope ordering). The sources treat it as ONE general process
  over cluster types, not as separate *tt- and *nn-laws.
- **CAPR modelling decisions (explicitly NOT source claims):** the
  *tt/*nn segmental enumeration and the pre-sonorant restriction are
  executable narrowings of the general change, chosen so that
  intervocalic geminates and *j-gemination products are untouched; the
  choice of Kroonen's *buttma- variant for the bottom protoform (the
  R/T *buþm- route would bypass degemination entirely for this
  lexeme); the TT/NN subsidiary defines are one historical change
  expressed as two composed segmental cases, not two changes.

## Historical analysis

- **Historical stage:** early Old English, after the syncopes that
  create most of the affected clusters (R/T §6.8.1; Barrack's 476
  ordering line).
- **Historical scope:** common OE; CAPR's cascade stresses West-Saxon
  conditions.
- **Regular phonological conditioning:** geminate simplifies adjacent
  to another consonant. The executable proxy restricts to the
  pre-sonorant slice actually exercised by the corpus (tt/nn before
  m, n, l, r).
- **Counterexamples and falsification:** none in the corpus; the
  near-miss space (other geminates before consonants) is unexercised —
  no selected row presents *ss, *ll, *mm etc. before a consonant at
  this stage. Negative controls: intervocalic geminates and
  *j-gemination products must survive to their own later rules, which
  the pre-sonorant restriction guarantees.
- **Positive evidence for analogy:** none invoked; none required.
- **Relationship between historical phenomenon and executable proxy:**
  the proxy is deliberately narrower than the general degemination of
  the sources (general CC → C / adjacent C, both directions per
  Barrack 476). Broadening is not justified by any current witness and
  risks regressing correctly-preserved geminates; the brief's
  instruction that a simpler-looking formula is not a goal applies.
  One historical change, two segmental cases: no SPLIT.
- **Chronology evidence:**
  - SC066 < SC068 — `independently_demonstrated` (reciprocal
    displacement witness spindle; fresh receipt `sc068_before_sc066`
    rows_changed=1, output spinnl). The dependency is historical, not
    merely technical: the handbooks derive spinl via syncope feeding
    cluster simplification (R/T §6.8.1), and Barrack orders 476 after
    his syncope rules on independent material (fint, besta, cyste).
    bottom does NOT order the pair (inherited cluster).
  - SC067 < SC068 — `stage_entailed` (adjacent composition; no
    witness).
  - Later boundary — none found before the runner boundary at order 86
    (chronology card; not a historical claim).

## Verdict

- **Verdict:** RETAIN (executable rule and conditioning unchanged; the
  production comment already states the narrow-proxy relationship
  accurately). Documentation updated with the print-verified Barrack
  correspondences and the R/T alternative derivation of botm.
- **Machine-readable line:**

Registry-verdict: SC068=RETAIN

- **Justification:** Both firings instantiate the one general
  degemination adjacent to a consonant that the sources describe; the
  corpus provides no witness that discriminates a broader formulation
  from the current pre-sonorant tt/nn proxy, and broadening without a
  witness risks regressing geminates that must survive to later rules.
  The feeding order SC066 < SC068 is independently demonstrated by
  spindle and corroborated by the handbooks' own derivations. No
  evidence supports splitting the rule: *ttm (bottom) and *nnl
  (spindle) differ only in which lexeme supplies the cluster, not in
  conditioning or period.

## Propagation (only after verdict)

- **Affected files/registries:** `registry/sc_registry.tsv` (verdict);
  reader file `reader_facing/068-preconsonantal-degemination.md`
  (Barrack discussion; botm alternative derivation); book dossier
  066-068; barrack_1975 dossier tables (dispositions for 453, 457b,
  476, 286); comparative dossier; cluster queue. No FST change.
- **Regression tests added/updated:** receipt pins `sc068_retired`
  (bottm/spinnl) and `sc068_before_sc066` (spinnl); evidence-interface
  census pins remain (2 firings).
- **Baseline/fingerprint effect:** none — no executable change.

## Residue

- **Unresolved uncertainty / deferred questions / author decisions
  required:**
  - The botm protoform choice (Kroonen *buttma- vs. R/T *buþm-) is a
    reconstruction selection, with R/T explicitly agnostic; if the
    corpus ever revisits the row, the degemination reading of this
    lexeme stands or falls with Kroonen's variant. spindle is
    unaffected.
  - Barrack 476's postconsonantal direction (C₂C₁C₁ → C₂C₁; wiersa,
    þirda) and 457b's intervocalic/late degemination (acuma) are
    unexercised by the current corpus; they belong to the deferred
    late-cluster round with SC080.
  - SC067 (OEDentalAssimilation) corresponds to Barrack's 481.1/481.7 +
    476 composites (fint, besta families); explicitly out of scope this
    round, queued with its paradigm-cell policy question.
