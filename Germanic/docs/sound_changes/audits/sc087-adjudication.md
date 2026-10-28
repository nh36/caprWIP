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
  pre-xt type is a separate missing law (SPLIT). H1: retain the current
  categorical `C _ st` operation for the selected corpus, without treating
  its environment as the complete historical domain.
- **What evidence would confirm it; what would refute it:** H2/H3
  require independently supported phonological, chronological and dialectal
  domains. A counterfactual departing from a selected target refutes its
  unqualified adoption across these selections, not every historically
  delimited version of the broader development. Coexisting byforms do not
  by themselves demonstrate optional sound change or invalidate regularity.

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
  protect word-initial *r (DEV_NOTES §17.42). The current rust selection
  *rústaz still predicts rost, not its target rust; see the correction below.
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
  stage-99 outputs listed above; all other selected rows pass the stage
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
    domain are extensionally equivalent for the original eight-vowel
    clause set only. The controlled follow-up below resolves this limitation.
  - `broad_sn` (s/n extension inspired by 459.1, not a diplomatic
    implementation of all its accent/quantity conditions): 3 previously
    matching selections cease to match, 0 improved — brandes → barndes,
    drenċ → dernċ, strenġ → sternġ. Attestation of these particular
    counterfactual outputs was not established.
  - `broad_sn_ae` (vowel set extended to the fronted *æ/*y present at the
    cascade site): 4 previously matching selections cease to match —
    additionally græs → gærs, an attested but unselected byform, not an
    intrinsically erroneous or unattested output.
  - `broad_sn_noleft` (Barrack's literal matrix has no left consonant
    requirement): 9 rows change, of which 8 previously matched their
    selections. Additional changes: faran → faarn, hameres → hameers,
    ræste → ærste, sċieran → sċiearn; rust's existing mismatch rost
    becomes orst, still not selected rust. Thus this is not nine lost
    correct predictions. Run/rinnan is unchanged: the enumeration lacks
    accented *í. None of these variants implements Barrack's matrix in full.
  - `regressive_459_3` (short Vr > rV / _ xt composed after
    OERMetathesis; the experiment includes unaccented vowels as well):
    1 previously matching selection ceases to match, 0 improved —
    fyrhte → fryhte. Campbell (p. 184, §459.3) records related late
    Northumbrian fryhto; that does not establish this exact counterfactual
    spelling/cell as the appropriate target here.
- **Witness role classification:** burst, frost — live applications;
  burst additionally the displacement witness for the SC044 edge; brand,
  drench, string, grass, run, fright — production negative controls
  (run is not changed by the tested variants); rust —
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
    pace Campbell; the regressive discussion is §7.95, not §7.96).
- **Source-supported historical phenomenon:** Old English r-metathesis
  before s/n clusters is real, widespread and chronologically and
  dialectally heterogeneous. Every consulted source characterizes the
  broader distribution as variable: Barrack himself grades his own
  environment-simplification stages ("a late stage of free variation",
  p. 116); Campbell's §459 lists pervasive unmetathesized doublets for
  precisely the forms a broad law would convert; Ringe & Taylor call it
  "common, but variable". Those descriptions record heterogeneous
  attestations, not an optional historical mechanism. They do not prove
  that C_st was the only regular environment: frost itself occurs without
  metathesis (Campbell §459; Sievers–Brunner §179 n. 2). The
  regressive pre-xt type rests on meager, mainly late-Northumbrian
  evidence (Barrack: "the evidence of this change is very meager", p.
  118; Campbell §459.3; Hogg §7.95 reanalyses it as epenthesis).
- **CAPR modelling decisions (explicitly NOT source claims):** the left
  consonant context (word-initial-r protection) is a CAPR corpus-exact
  guard on the present selections, not Barrack's matrix; the
  eight-vowel clause set excludes historically relevant *æ/*y, as the
  follow-up demonstrates, and is not the whole short-vowel class; the cascade
  slot after OEContraction is compositional, not a dating.

## Historical analysis

- **Historical stage:** Old English (West Saxon target), unchanged.
- **Historical scope:** english_specific, unchanged. The Anglian
  pre-breaking metathesis of the burn/run family (Ringe & Taylor 341;
  Barrack's dialect-differentiated staging, pp. 116–17) is outside
  CAPR's West Saxon executable target.
- **Regular phonological conditioning:** r + short vowel > vowel + r
  before the st cluster, after a consonant, describes the executable
  proxy, not a demonstrated exhaustive historical law. A regular historical
  account must specify phonological/prosodic, chronological and dialectal
  conditions without grammatical or lexical-identity conditions. The current
  targets retain rV in brandes, drenċ, strenġ, græs and rinnan, but that
  does not explain the provenance of their alternative orders.
- **Counterexamples and falsification:** the counterfactual receipts are
  a record of incompatibility with unqualified adoption of the tested
  broadenings across the selected targets: s/n variants lose 3, 4 and 8
  existing matches respectively; the nine-change variant additionally
  alters rust's pre-existing mismatch. No selected target gains a match.
  Gærs is nevertheless independently attested; lack of a selected match
  is not proof of historical impossibility.
- **Positive evidence for analogy:** none established in this bounded
  investigation. Distinct dialect histories, borrowing, earlier/later
  transmission, analogy and finer phonological conditions are possible
  explanations requiring independent evidence; none is adopted merely
  to reconcile the byforms.
- **Relationship between historical phenomenon and executable proxy:**
  the proxy is deliberately narrower than the full historical metathesis
  complex: it models the presently selected berstan/forst histories.
  Broader s/n metathesis and dialectally delimited developments belong in
  the historical discussion, even when not executed. Selected corpus
  endpoints constrain a model but cannot alone delimit a productive
  historical domain. No optional rewrite is warranted.
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
  not adopted as unqualified production replacements. Their historically
  delimited explanation remains unresolved rather than refuted by byforms.
- **Machine-readable line:**

Registry-verdict: SC087=RETAIN

- **Justification:** The current categorical operation has exactly two
  live applications, berstan and forst, and both agree with their selected
  targets. The tested broader operations do not preserve other selections,
  so are not justified as unchanged production replacements. This supports
  RETAIN for the present implementation, not a proof that C_st was the sole
  regular historical environment. The controlled follow-up distinguishes
  before-s from before-st when *æ is included; its gærs output is attested.

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
  justify automatic admission or a different verdict. Cress is assessed
  out of sample in the bounded follow-up below.
- The late West Saxon regressive/sporadic metatheses (wæps/wæsp type,
  áscian/ácsian 440b) remain documented, unimplemented variation;
  Barrack 440b is queued in the Part IV research agenda.
- The Barrack census's 459.1 `input_output_glyphs` field still resembles
  the separate regressive 459.3 formula. This residual transcription
  issue is flagged for original-passage QC, not used as evidence for
  conditioning here; the cited discussion and examples were consulted
  independently.

## Bounded follow-up: discriminating witnesses and cleanup

This follow-up starts from `e18ea205`, following adjudication `e02e5260`.
It does not reopen SC087 or begin any other adjudication. RETAIN, FST
definitions, chronology, metadata, inputs, targets and frozen baselines
remain unchanged. The interpretation above is corrected: the categorical
CAPR proxy is not thereby proved the sole exceptionless West Saxon law.

### Controlled question and witness roles

The falsifiable claim is that the original zero-difference finding for
before-s versus before-st depends on its incomplete vowel enumeration.
Four otherwise
identical cascades preserve the same left-consonant condition:

| Variant | Following environment | Vowels |
| --- | --- | --- |
| A | st | Existing eight |
| B | s | Existing eight |
| C | st | Existing eight plus æ, y |
| D | s | Existing eight plus æ, y |

`sc087-experiments/controlled_receipt.json` records the exact Foma
definitions, source/corpus/context and selected-input identities,
production equivalence, all changed rows, actual pre-SC087 strings,
selected-target match assessments and independent byform references.
The original `receipt.json` remains the record of the earlier experiment.
Grass is a production negative control and a discriminator between C and D;
its attested byform gærs is positive evidence for the broader historical
phenomenon, not a reason to alter its selected target silently.

All four variants were compiled and applied to all 389 selected rows in
isolated container workspaces. A agrees with the canonical production
cascade on every row. A/B and A/C each change zero rows. C/D and B/D each
change exactly row 2045: *grásą reaches SC087 as `*g*r*æ*s`; A, B and C
return selected græs, while D returns attested but unselected gærs
(Campbell 1959, p. 184, §459; Hogg 2011, p. 297, §7.94). No other row
changes, including none attributable to adding *y.

The original zero difference is therefore literally correct for the
eight-vowel executable definition but misleading as an unqualified claim
about corpus discrimination: exclusion of *æ masks an existing selected
rVs witness. Adding vowels alone under st changes nothing; removing t
with the expanded class does. Historical non-discrimination nevertheless
remains in a different sense: græs/gærs and these selected-target results
do not establish the productive phonological, chronological and dialectal
domain of a regular historical law. They do not license optional rewriting
or identify the mechanism transmitting both byforms.

The statistical correction for the original nine-change `broad_sn_noleft`
run is eight lost selected matches plus one changed existing mismatch
(rost → orst, selected rust). The other changed rows were previously
matching. Gærs must be distinguished from counterfactual outputs whose
attestation/cell has not been established. No new chronology edge is
inferred from either experiment.

### Cress: independent evidence and admission decision

The following are source claims, not a selected reconstruction assembled
to fit SC087:

| Source | Evidence and limitation |
| --- | --- |
| Campbell (1959), p. 184, §459.1 and n. 1; p. 190, §476 | Lists cerse and cresse; derives cerse via *cersse from cresse. Middle English kers supports velar initial c and metathesis after assibilation. Does not assign both byforms to one synchronous West Saxon paradigm. |
| Sievers–Brunner (1965), pp. 146–147, §179; §231 n. 1 | Lists cærse, and residual cærssan in the discussion of geminate simplification. The original printed locator is 146–147, not scan sheet 159. The inflected cærssan is not the same cell as a cresse citation. |
| Hogg (2011), p. 288, §7.80; p. 297, §7.94 | Gives cresse → *cersse → cerse and the broader r-metathesis environment. Establishes an rVss witness, not a uniform date/dialect for every spelling. |
| Ringe and Taylor (2014), p. 263 | The original PDF gives cærse < *cræsse, discussing voiceless s from degemination beside another consonant. The OCR's cerse/*creesse is not a diplomatic transcription. |
| Bülbring (1902), p. 198, §493 (original checked) | Gives cerse with Germanic *krasjōn and discusses initial velar retention after late metathesis. The original establishes the printed long ō; the family/stem basis does not independently settle the selected nominative cell. |
| Kluge–Seebold (2011), p. 540, s.v. Kresse¹ | Reconstructs West Germanic *krasjō f., with OE cressa. Its stage and ending must not silently become a PGmc weak-feminine nominative *krasjōn. |
| Clark Hall (1960), pp. 56, 66, s.vv. cærse, cressa | Distinguishes feminine cærse/cresse and masculine cressa (glossaries). Cærse is referenced to Leechdoms; no single dated/dialect-attributed token and paradigm cell is established by the headwords alone. |
| Sweet (1885), p. 96, Epinal–Erfurt 917; p. 523, s.v. cressa | The edited gloss has Epinal cressae beside Erfurt cressa, and the lexicon classifies cressa as weak masculine. These are gloss forms, not interchangeable evidence for a West Saxon weak-feminine nominative cresse. |

Campbell, Brunner, Sweet's p. 523, Clark Hall's p. 66 and Kluge's p. 540
were checked against local original-page images; Ringe–Taylor's original
PDF text was also checked for the æ readings. Hogg's held text supplies
the section-level evidence; no new original-scan verification is claimed
for it. The user-supplied Bülbring original was ingested as a local,
ignored holding alongside the unchanged text. Its title/imprint (sheet 7:
Heidelberg, Carl Winter, 1902, part I, Lautlehre) and printed p. 198,
§493 (sheet 220) were checked, including *krasjōn. PDF SHA-256:
`339065ffa9a264d39a5684ec309f678c563da0b4ae2031102513a3ee2bf8aa52`.
Its existing source-register entry now includes both holdings; this does
not upgrade the review status of unexamined passages.

The defensible inherited family contains *krasj-, independently of any
desired output. A full history has to reconcile j-triggered consonant
gemination, vowel fronting/i-umlaut, loss of j, retention of initial velar k
behind intervening r, metathesis, and simplification of the resulting rss
cluster. The published cresse/*cræsse → *cersse/*cærsse history is a
genuine non-st witness; the two vowel spellings must not be collapsed into
a source claim about a single dialect. Early glossary cressa/cressae and
dictionary cresse/cærse differ in recorded gender/form and transmission.
Sweet's nineteenth-century dating discussion (pp. 2–3) places Epinal early
and labels Corpus Mercian in the preface (p. vii); those edition-level
judgments are not a modern token-specific West Saxon attribution.
Exact manuscript date, dialect and inflectional cell for a selected
feminine cresse/cærse target remain unestablished here.

Only local out-of-sample probes are warranted. The harness tests the
*krásjōn and *krásjō families separately; acute stress is CAPR notation,
and neither probe is an adjudicated PGmc input or admitted paradigm cell.
Neither inherited-family probe reaches SC087: the canonical input gate
`EnglishProtoInput` rejects both. This is not a diagnosis of a defective
earlier sound law and is not repaired here. A separate local component
receipt, `sc087-experiments/cress_receipt.json`, tests the published
intermediate histories without asserting a complete inherited derivation:

| Local pre-SC087 probe | A | B | C | D |
| --- | --- | --- | --- | --- |
| *cresse (`*k*r*e*s*s*e`) | unchanged | *cersse | unchanged | *cersse |
| *cræsse (`*k*r*æ*s*s*e`) | unchanged | unchanged | unchanged | *cærsse |

These are component outputs, not final cerse/cærse predictions:
post-metathesis degemination is independently required by the cited
histories. They confirm that a literature-based rVss witness can separate
the hypotheses locally, but do not establish which reconstructed cell
reaches the corresponding stage in CAPR. No word is admitted:
grass already supplies the selected rVs discriminator, and
cress adds a real rVss historical witness but not a fully established new
selected cell. Resolving its stem/ending and source-specific target would
require an explicit lexical-admission/baseline migration, not housekeeping.

### Follow-up validation and closeout

The focused SC087 run passed all seven tests and eight subtests in strict
mode. Both runtime tests executed in the backend container: the census
compares the actual before/after stage outputs for every selected row,
keyed by stable row ID rather than concept or an inherited-r filter.
Exactly burst and frost fire; all six negative controls remain unchanged.

The complete strict Germanic suite, excluding the separately sequenced
evidence-interface module, passed 1,608 tests and 9,131 subtests. The
evidence-interface module then passed all 24 tests, without overlapping
the protected private assays with its canonical-bin rebuild. No tests
were skipped in either run. Canonical SC087 finalization and the final
strict artifact-graph check both reported `CONTROL PLANE CLEAN`.
Reader/book/index and Bülbring holding-provenance projections were
regenerated only through the adjudication interface.

No executable FST, corpus row, selected input/target, historical metadata,
chronology relation, approved migration or frozen baseline changed.
SC087 remains RETAIN. No late consonant-cluster adjudication was begun.
