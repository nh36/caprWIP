# SC035: unstressed prefix vocalism

## Identity

- SC id: SC035.
- Executable identifier: `OEPrefixAReduction` (not a date).
- Date / branch / base commit: 2026-10-21 / `update` /
  `60b91080d2adadf431c92f7388ab1dd6199a4c7a`.

## Question

Does the current rule accurately represent a historically motivated reduction
of unstressed prefixal *a*, and does the evidence justify its historical and
chronological claims? A source-supported weak-prefix development and an
in-domain live application would support retaining a narrow executable proxy.
A genuinely morphological or phonetic domain matching every `gaCV` string,
or an independent stressed-fronting chronology, must not be inferred from
successful output alone. Unprefixed positives, excluded genuine prefixes,
multistage source histories, or a dependency confined to SC107 would refute
the stronger claims.

## Current state (before any edits)

The registry calls this “OE Prefix A Reduction Early”, `oe/english_specific`,
confidence A, unadjudicated, with a one-sided later boundary “across SC043”.
The canonical edges already distinguish the runner limitation at
`PWGmcChanges` from the technical SC035 -> SC107 displacement.

The literal rule is:

```foma
define OEPrefixAReduction [
    {*a} -> {*ĕ} || .#. {*g} _ [EnglishStarConsonant | EnglishPalatalConsonant] EnglishStarVocalic
];
```

It is at numbered cascade position 42, physical execution index 44.
The selected input of row 1944, believe, is PGmc *galáubijaną,
with the prefix unaccented and the root accented, targeting OE *ġelīefan*.
No prefix boundary is supplied to the transducer.

The mandatory protocol/template, current control plane, historical SC035
card, grouped SC035–SC037 dossier/reader, complete SC043 adjudication and
component dossier (including the adopted section 12) were read. The old
chronology card remains an experiment-time record.

## Diagnosis

`SC035 --evidence` rebuilt the backend stage bins, checked provenance and
verified production/sandbox equivalence on all 389 selected rows. The
companion `sc035-prefix-reduction/experiment.py` uses the existing isolated
experiment compiler, compares its identity with production, and protects
canonical sources, bins and baselines against writes. Its complete JSON
record is `sc035-prefix-reduction/evidence.json`.

### Complete census: selected389 and current legacy380 identity view

There is exactly **one** firing in each view: row 1944, *believe*. The
legacy view uses the established migration-aware identity mapping, not
the immutable archive's superseded inputs. All other 388 selected and
379 legacy-identity rows are unchanged at SC035.

| Row / selected input / target | Immediately before SC035 | Immediately after SC035 | Final |
| --- | --- | --- | --- |
| 1944 / `*galáubijaną` / *ġelīefan* | `*g*a*l*ēa*b*i*j*a*n*ą` | `*g*ĕ*l*ēa*b*i*j*a*n*ą` | *ġelīefan* |

This is an in-domain live application, and a model-local bleeding/protection
witness: the marked vowel avoids subsequent ordinary unstressed fronting
and palatal diphthongization. It is not an independently dated historical
feeding witness for ordinary stressed fronting.

### Principal trace and controlled counterfactuals

The live prefix remains `*g*ĕ-` through SC107, SC043 and breaking.
Immediately before and after `OEWsPalatalDiphthongization`, the live form
is `*ʝ*ĕ*l*ēa*β*j*ą*n`. Surface conversion ultimately writes its breve
vowel as *e*.

Four full-corpus alternatives were compiled in temporary directories:
skip SC035; delay it to after SC107; delay it to after SC043; delay it
to after breaking. Each changes exactly row 1944 and no other selected
row. Each yields *ġealīefan* instead of *ġelīefan*, with the following
diagnostic path:

1. Before SC107: `*g*a*l*ēa*b*i*j*a*n*ą`.
2. After SC107: `*g*æ*l*ēa*b*i*j*a*n*ą`.
3. SC043 and breaking leave that form unchanged.
4. Before palatal diphthongization: `*ʝ*æ*l*ēa*β*j*ą*n`.
5. After palatal diphthongization: `*ʝ*ea*l*ēa*β*j*ą*n`.

The delayed SC035 cannot recover its input because it rewrites `*a`,
not `*æ`. The old “cross SC043” failure therefore belongs to the
unstressed member of the former composite, followed by a stress-domain
representation error. Historically the weak prefix could itself undergo
fronting: bypassing SC107 is not evidence that a distinct historical
prefix reduction preceded unstressed fronting, still less SC043.

### Positive and negative domain controls

| Control | Actual SC035 pre/post | Interpretation |
| --- | --- | --- |
| *gall*, 2037, `*gállô` > *ġealla* | `*g*á*l*l*ô`, unchanged | Root accent blocks the rewrite. |
| *guest*, 2049, `*gástiz` > *ġiest* | `*g*á*s*t*i`, unchanged | Root accent and the consonant cluster exclude it. |
| *goose*, 2044, `*gánsz` > *gōs* | `*g*ō*s`, unchanged | Earlier nasal developments have removed eligible *a*. |

At the isolated component, changing the live prefix's `*a` to `*á` or
`*à` blocks reduction. A noninitial `ga` and a prefix followed directly
by a vowel are excluded too. Conversely synthetic `*g*a*t*á` changes
whether or not an analyst assigns it a morpheme boundary: the FST has no
such information. These are formal controls, not invented attestations.

Ringe–Taylor p.335 supplies a genuine omitted shape: PGmc *gastīganą*,
PWGmc *gastīgan*, early Northumbrian *gistīga*, later *gestīga*, and
WS *gestīgan* 'climb into/onto'. The staged component probe
`*g*a*s*t*ī*g*a*n` is unchanged because `s` is followed by `t`, not a
vowel. This is a source-backed domain limitation, not a new admitted
corpus input or a claim that this unaccented transcription is an attested
intermediate. The consonant-plus-vowel condition does not “ensure prefix
structure”. It captures the selected *believe* shape; it neither identifies
all *ga-* prefixes nor licenses a general morphological exception.

## Literature

The local text holdings were checked, including their printed page
markers. No new original-source page-image verification is claimed.
The old grouped dossier/card and the complete SC043 component analysis
were checked against these passages, rather than treated as source evidence.

| Source / local holding | Verified claim and limit |
| --- | --- |
| Campbell 1959, p.31 §74 and n.5; `docs/references/campbell_old_english_grammar.txt` | Normally unstressed *ge-*; the footnote separates the accented form in *ġeatwe* 'armour'. This is a stress distinction, not grammatical conditioning of a sound law. |
| Campbell 1959, pp.140–141 §§333–334 | Ordinary unstressed *a*-fronting, with a nasal/syllabic distinction. It does not establish the exact `gaCV` conditioner. |
| Campbell 1959, p.147 §354 | Pretonic **loss of *i*** in *bi-*, *ni-*; not evidence for a distinct *ga-* > *ge-* rule. The previous citation is withdrawn for SC035. |
| Campbell 1959, pp.153–155 §§369–370 | Later merger of unstressed front vowels; early spellings and later *be-*, *ge-* outcomes. |
| Hogg 1992, “Phonology and Morphology”, §3.3.1.3, p.88; pp.99–100; `docs/references/hogg_vol1.txt` | General unstressed-vowel system and the normally unstressed prefix; neither passage establishes an early *a* > *e* date. The chapter is `HoggPhonology1992`, not Hogg's separate Grammar. |
| Ringe–Taylor 2014, p.206; `docs/references/ringe_taylor_linguistic_history_vol2.txt` | PGmc/PWGmc *ga-*, Gothic *ga-*, OS/OHG *gi-*, OE *ge-*, OF *e-*; lack of diphthongization in the weak prefix. |
| Ringe–Taylor 2014, pp.245, 267 | Present *galaubijaną* and past *galaubidē* histories, with West Saxon versus Anglian root outcomes. These are comparative derivations, not proof of the CAPR intermediate or a SC043 boundary. |
| Ringe–Taylor 2014, pp.334–335, especially p.335 | Front-vowel merger; early *gi-* and later *ge-*; the exceptional stressed prefix and *ġeatwa*; possible regular pretonic raising after a palatal versus possible influence of *bi-*. Actual *gistīga/gestīga*, *gidyrstig/gedyrstig*, *gibēatæn/gebēaten* comparisons. |

The literature supports ordinary weak-prefix fronting and later
unstressed-vowel convergence, not an independently proven single abrupt
*a* > *e* event before stressed first fronting. The precise history of
early *gi-* is disputed; a possible analogy in a secondary source is
recorded as an alternative explanation, not imported as morphological
conditioning or lexical diffusion in CAPR.

The direct `*a` -> `*ĕ` mapping, its `gaCV` filter, its early serialization,
and the bypass of intervening rules are CAPR modelling decisions.
`*ĕ` is a technical reduced/unstressed front-vowel token, not a
claim of a separately attested phonetic [ĕ] stage, or proof that late
OE schwa already existed. It compresses *a* > *æ* and later *i/e*
developments; no new historical segment is proposed.

## Historical analysis

- **Stage:** pre-Old English onset, Old English completion; the registry
  uses its established “Pre-Old English” label and `hist_stage=preoe`
  for the onset, with the later completion explicit in the staging notes,
  rather than moving the entire compressed operation to one asserted
  historical date. The executable position stays unchanged.
  No experiment dates the completion before SC043.
- **Scope:** the English development of inherited *ga-* (`english_specific`
  identifies the trajectory modelled, not a uniquely English invention
  of reduction). Gothic *ga-* versus OS/OHG *gi-* and OE *ge-* show the
  inherited prefix and wider West Germanic reduced reflexes, not a uniquely
  demonstrated common PWGmc *ga* > *ge* event. Ringe–Taylor explicitly
  reconstructs PWGmc *ga-*. Neither pan-West-Germanic restaging nor a new
  ancestral innovation follows from resemblance alone; the Frisian
  *e-* comparison does not independently date its vowel or consonant loss.
- **Confidence:** retain A for the existence of the English weak-prefix
  development. Its exact date, path through early *gi-*, and literal
  proxy conditioner are not thereby assigned A. Stage/scope and this
  confidence are independent; no date is derived from a confidence code.
- **Domain:** a stress-conditioned historical process versus a deliberately
  narrower, boundary-free selected-input proxy. Positive and negative
  coverage is satisfactory for the current corpus; expansion to clusters,
  prevocalic prefixes or inner prefixes requires its own justified
  representation/coverage work. No corpus expansion or input correction
  is required by this adjudication.

### Chronology, edge by edge

1. **SC035 -> SC107:** retain `technical_computational`, evidence basis
   `technical`, role `displacement_witness`. Fresh full-corpus displacement
   reproduces the old output, isolates the unstressed helper and explains
   the later erroneous diphthong. This is neither `stage_entailed` nor an
   `independently_demonstrated` historical chronology: the proxy compresses
   the very fronting/merger history the helper partly represents.
2. **SC035 -> PWGmcChanges:** retain `runner_limited_boundary`, evidence
   basis `boundary_observation`. It preserves the old inability to test
   farther into the bundle, not a historical must-follow relation. This
   is neither historical category above.
3. **SC035 / SC043:** no canonical edge, and no independent historical
   relation established here. The old card referred to a composite;
   the completed SC043 adjudication already separated the domains.

The sources distinguish inherited PGmc/PWGmc *ga-*, fronted English
prefix vocalism and later documented *gi-* > *ge-*. Those broad successive
states are source-supported; they supply no additional strict edge to a
separately dated SC in the current cascade. The stressed *ġeatwa* comparison
is a stress contrast, not a terminus for the weak-prefix merger.
No edge is added, reversed or removed, and no old experiment is rewritten.

## Verdict

**REFORMULATE historical metadata and interpretation / RETAIN executable
law, serialized order and all selected data.**

Registry-verdict: SC035=REFORMULATE

The existence of a reduced English reflex of inherited unstressed *ga-*
is secure, but CAPR's one-step mapping is a compressed, narrower proxy
for a multistage history. The only fresh displacement failure is
component-local to SC107 and subsequent inappropriate diphthongization;
it does not date reduction before SC043. Correct the onset/completion
description, scope/confidence qualifications and publication claims,
retaining the literal rule and both accurately classified edge records.

## Propagation (only after verdict)

- Registry: SC035 stage/display/verdict/memo, chronology summary and source
  pointers; SC035 edge annotations only (categories/endpoints unchanged);
  human inventory note. No other SC verdict changes.
- FST: correct SC035's misleading source/domain comment only. The literal
  law, definitions and complete composition remain identical.
- Grouped SC035–SC037 dossier and reader: replace only SC035's analysis,
  correct SC043 cross-references and explain the technical breve. Do not
  adjudicate SC036/SC037 or reorganize their material.
- Tests: paired live/domain controls, component-local chronology and
  historical-card integrity; isolated runtime assay. The SC112 publication
  no-science-delta assertion is checked between its original scientific
  base and pinned publication closure `3c015def`, not the evolving worktree.
  Its original base and the exact stage-resolution migration assertion
  are retained. Current corpus/baseline and lexical invariants remain strict.
- Generated propagation: exclusively `SC035 --finalize`, then strict tests,
  full graph and strict book build with rendered-page inspection.
- **Baseline effect expected: none.** No input, target, sound-law mapping,
  order, selected identity, class or editorial order changes. Expected
  389 selected / 381 matches / eight mismatches; 167 lexical entries.
  No receipt authorizes, and no command performs, a baseline refreeze.

## Residue

The precise comparative chronology of reduced West Germanic prefix vowels
and the regular-raising versus analogical account of early *gi-* remain
uncertain. CAPR does not claim to resolve them through one live witness.
The current corpus does not discriminate a complete prefix boundary/stress
model; genuine clustered prefix forms illustrate the proxy's incompleteness,
not a new lexical selection obligation. No author decision is required to
retain the presently correct narrow rule or to withdraw the unsupported
SC043 dating claim. SC036 and SC037 remain unadjudicated.

## Validation and publication closeout

- The full strict suite passed: **1489 tests and 9026 subtests**, including
  the actual Docker/Foma replay of the five isolated models. After the
  final prose-only gloss corrections, the paragraph-gloss tests passed
  (12 tests, 32 subtests), as did the non-runtime SC035/SC112 checks
  (14 tests, nine subtests). No scientific code changed after the full run.
- `SC035 --finalize` passed its propagation checks; the full artifact
  graph reported `CONTROL PLANE CLEAN`. The strict Docker book build
  (`INDEX_VERBORUM_STRICT=1`) passed, including paragraph glosses, internal
  references, bibliographic locators, index structure and print readiness.
- The combined PDF was inspected visually on PDF pages 83–84 (printed
  pages 81–82): the complete revised SC035 discussion, literal rule,
  breve, citations and transition into the unchanged SC036/SC037 material
  render correctly. The SC043 link resolves to ordinary English fronting
  on PDF page 88 (printed page 86), not to an asserted historical edge.
- All 389 selected identities and outputs remain unchanged: 381 matches,
  eight mismatches and no ambiguous outputs. All 167 lexical entry blocks,
  class assignments and their approved editorial sequence are preserved;
  the lexical volume and class manifests are byte-identical to the base.
  The comment-stripped complete FST, all corpus data, frozen baselines,
  approved migration receipts and survey provenance are likewise unchanged.
  The full trace differs only in its provenance header. Other registry
  rows and the SC036/SC037 reader text remain unchanged.
- Correcting the FST comment changed its source hash from
  `d9b8e0f8698870d73a78e505c9615ce6040239be66d5f7c845c0e2d8093c0a21`
  to `be1b265e9a5cfb539f650708cf38ed2b18d6d2e319b08503ce5cb882d20746af`.
  The regenerated equivalence/trace provenance records that real source
  change and rebuild; this is not a new output baseline. The experiment's
  original source hash remains preserved, and its fresh runtime test
  compares actual scientific results rather than pretending source-byte
  identity. SC112's historical publication assertion retains its original
  scientific base, now bounded by its pinned publication closure; the
  exact later stage-resolution provenance-migration assertion remains
  separately enforced.
- The control plane identifies SC036 as the next pending sound change.
  Its packet was not prepared and its adjudication was not begun.
