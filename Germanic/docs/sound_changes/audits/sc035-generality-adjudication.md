# SC035: empirical generality and manuscript distributions

## Identity

- SC035, `OEPrefixAReduction`.
- 2026-10-25; branch `update`; accepted base
  `c1b573078c521121dde670e735f3907e7494cb16`.
- Follow-up to the three preserved SC035 adjudications and their experiments;
  none is overwritten.

## Question

Before new comparisons: does regular raising of short pretonic *ae*
immediately after a palatal fricative remain the best explanation of early
English spellings once related manuscript traditions and dialects are
distinguished? A securely weak, unraised short front vowel in the same
early phonological environment would challenge the law. Early and late
spellings alone cannot prove a uniform date, vowel height or universal
lexical generality. Positive evidence for replacement, rather than mere
resemblance to *bi-*, is required to prefer analogy.

Separately, does the bounded positive-stress annotation implement exactly
one weak syllable before a headed foot without grammatical recognition,
stress inference from a missing acute, or unintended root-vowel changes?
Artificial strings can refute formal-domain claims but cannot confirm
historical regularity.

## Current state (before any edits)

Supported preparation and forced evidence rebuilding completed. The sole
live firing is believe1944, selected `*galáubijaną`, targeting *ġelīefan*.
All 389 selected rows agree between production and sandbox. The adopted
law is short pretonic *ae* to *i* after *ʝ*, confidence B, English scope
with pre-OE onset and OE completion. All three earlier closures, associated
assay code and related SC052/056/073/076 preparation packets were read.

## Diagnosis

The sole live application among all389 selected identities (and within the
active legacy380 population) is believe1944. Its independently selected input
is `*galáubijaną`; the stage changes `*ᶠ*ʝ*æ*l*ēa*β*j*ą*n` to
`*ᶠ*ʝ*i*l*ēa*β*j*ą*n`. The focal root accent has already been consumed,
but the annotation was inserted while primary stress remained explicit.
Production/sandbox equivalence covers all389. Source SHA256 is
`421e7ae9c0a705f910e081e20242f8f7b3a42731b9dc908124217d32826a9d77`.

Believe is a live application and conditional feeding witness, not independent
dating of the whole law. The full climb comparison and shaft/prefixed-shaft
stem comparisons test the weak/headed-foot distinction outside that single
selected firing. The earlier frozen no-raising model reaches the same final
e but does not generate early i; rerunning the old experiment under a new
name would not add evidence.

The new isolated assay passes345 predictions:300 annotation,28 raising,
four diphthongization,five ae-merger,eight i-lowering. It includes onsetless
and clustered onsets, several positively headed vowels, long/secondary-only/
missing-head negatives, hiatus, multiple pretonic syllables, internal weak
positions, sentence-context wrappers, nonfricative palatals and nonpalatals.
These are artificial formal controls, except the explicitly normalized later
lowering comparisons. They are not new historical attestations or invented
PGmc inputs.

`OEPretonicInput` recognizes exactly one initial short weak vowel followed
by consonants and an acute head. `OEStressFootContext` marks that disjoint
input branch and otherwise preserves the input; it does not discover stress
from its absence. `SentenceCtx` preserves selected word-level context.
`FootCtx` exposes the headed remainder after an annotated weak syllable,
or the ordinary root without such a syllable, to a root-foot operation.
It is not a general metrical parser. SC035 consumes the positive annotation,
short ae and immediately preceding phonetic fricative, not morpheme identity
or origin. The flag preserves information after accent-consuming changes.
SC073 merges weak ae/e; SC076 separately lowers short i and deletes the flag.
Long/stressed roots remain outside these weak-prefix branches.

## Literature

All three previous SC035 memos/receipts and related SC052/056/073/076 accounts
were consulted. Existing holdings: RingeTaylor2014 pp.206,334-335; Campbell1959
p.31 §74/n.5,pp.140-141 §§333-334,pp.153-155 §§369-370; HoggGrammar2011
pp.4-7,104 §5.48 n.1,237-239 §§6.49-6.54; Berg2014 pp.28-30,39-42,60-61;
MinkovaZhou2022 pp.535-536; RieggerBogelWalkden2024 pp.2065-2068.
Their functions differ: distributions, weak fronting, stress and foot evidence
do not each independently prove raising or its date.

Toller1921 p.284, ge-, was verified against the local supplement image and
the online entry. Its nine EE pairs were checked in Sweet1885 p.48 and the
actual Corpus pages; all counts agree. Sweet's EE marginal cross-references
for189/191 are wrong (actual Corpus503/505). The exact spellings, corrections,
restorations and locator discrepancies are recorded rather than normalized
away. Full sources acquired: Sweet1885; Stevenson1840; Sweet1871; Lucas/
Lucas2012 (Epinal catalogue); Lucas2016 (Corpus catalogue); and the licensed
RuneS Pforzen database record. Metadata, original hashes, acquisition,
rights and exact passages are registered in the normal reference indexes.

The51-observation ledger joins to explicit witness dates/dialect reliability.
27 observations are nine related EE/Corpus alignments of one inherited prefix,
not27 independent sound laws. Other observations cover gi/ge/gy/ga, VP ge/bi,
early Northumbrian, late Northumbrian and early WS. Gothic ga-, OS/OHG gi-
are explicitly handbook comparanda, not newly inspected diplomatic tokens.
Toller's later gi-mynd in Wright volumeII remains secondary reporting;
the local Wright holding is volumeI.

The primary edition shows real mixed early spelling and later Northumbrian
gi. Modern catalogue dates place Epinal around/before700 and Corpus in the
first half of9c, not Sweet's or Berg's old absolute dates. Erfurt's date is
inconsistent in directly consulted accounts, and its early linguistic
exemplar cannot be equated with its continental copy. No conclusion here
depends on choosing an exact date for that copy. RuneS find201 externally
dates the Pforzen object585-610, not an English raising event.

## Historical analysis

- **Stage/scope:** retain pre-OE onset with OE completion and
  `english_specific`. Neither spelling geography, a code prefix nor confidence
  determines the label. Comparable continental reductions need not be one
  inherited event.
- **Regular conditioning:** short weak pretonic ae immediately after the
  palatal fricative. Campbell supports ordinary weak fronting; Ringe/Taylor
  supplies the specific regular-raising possibility. Weakness and following
  root stress have independent metrical support; they are not grammatical
  conditions. Raising is phonetically compatible with high front articulation,
  not established as a direct acoustic fact by written i.
- **Positive evidence:** inherited a is comparative; gi is genuinely early
  and not confined to one Northumbrian monument. Lowering belongs to a wider
  weak-vowel history, not a special permission for ga. Many ga words and several
  textual traditions improve the distributional case without establishing an
  independent non-ga witness to the entire raising environment.
- **Negative evidence:** stressed gear/geatwe and ordinary guest/give/sheep
  root histories support the stressed/weak distinction. Nonpalatal, long and
  otherwise-matched artificial controls prove only formal restriction.
  No independently established non-ga positive and no securely same-environment
  unraised early ae were found.
- **Candidate difficulties:** early ge can reflect lowering, orthographic
  overlap or transmitted layers, not necessarily phonemic failure of raising.
  Erfurt gaeadun is not ignored: vowel-initial root, uncertain consonant value/
  quantity, related gibiodun/geeodun and continental copying prevent treating it
  as established short-ae-after-palatal counterevidence. Gybyrdid is not proof
  of a distinct y law. Internal modgidanc requires compound prosody; it does
  not refute a bounded citation-word implementation.
- **Chronology:** fronting and palatalization supply the adopted raising
  environment; these existing SC107/SC052 relations are conditional technical
  feeding dependencies, not newly independently demonstrated historical
  intervals. Lowering after the earlier front-vowel merger has handbook
  support, but the precise interval is not fixed by displaced output. No new
  historical edge is promoted, and no chronology or stage change is adopted.
- **A, regular raising:** best current explanatory account, with a coherent
  independently weak domain and no verified phonological counterexample.
- **B, fronting/merger without raising:** explains eventual e, but has no
  independently specified account of the whole early i distribution.
- **C, alternative regular pathway:** later raised allophones or spelling
  conventions are real interpretive possibilities (Hogg6.54); they do not
  independently establish a replacement early a/e-to-i pathway. Exact
  intermediate height remains inferred, not proved by the ledger.
- **D, bi analogy:** serious published possibility, but Berg's objection to
  phonetic attractiveness and the similarity of two weak prefixes supply no
  positive substitution, allomorph-replacement or grammatical-distribution
  evidence. No demonstrated failure of regular phonology requires analogy.
- **Formal/historical relation:** the implementation is a narrower recognizer,
  not a claim that all internal, long, hiatus or multi-pretonic cases underwent
  this law. No source-backed example here requires extending it. Keep the
  architecture rather than undertake a speculative stress-system refactor.

## Verdict

**RETAIN** the staged regular account, its executable conditioning, order,
stage/scope and confidence B. Correct the manuscript-distribution exposition.

Registry-verdict: SC035=RETAIN

Regular raising retains explanatory priority: actual early i needs explaining,
and no positive analogy evidence or securely same-environment counterexample
overturns it. The wider ledger does not convert repeated inherited ga into
independent proof of universal lexical generality. The observed distribution
is a mixture of phonological history, variety, orthography and transmission;
it cannot be flattened into a universal early-gi/later-ge calendar.
Confidence B remains appropriate to the specific raising reconstruction,
independently of the stage label. No indeterminate whole-law verdict or
confidence upgrade follows from passing more computational controls.

## Propagation

Point the canonical registry to this follow-up and retain all earlier memos/
receipts unchanged. Update the inventory note, current dossier preface and
SC035 publication; qualify the directly affected SC076 chronology statement.
Register all newly consulted sources, witness metadata and focused ledger.
Add portable relational ledger/receipt checks and a fresh Foma domain test
to the normal suite; update only live-current verdict assertions.

No executable source, cascade order, corpus/context selection, lexical model,
editorial ordering, protected output or baseline changes are authorized or
needed. The existing full live verifier supplies selected389/intermediate109/
composed equivalence and full/source-backed controls. The migration-aware
legacy380 and all fingerprints must remain unchanged. No SC036 work is begun.

## Final validation

Supported SC035 finalization passed with `CONTROL PLANE CLEAN`. The complete
strict Python/Foma suite passed: 1576 tests and 9071 subtests, no skips, in
3684.95 seconds. This includes the current 389-row, 109-stage comparisons,
production/sandbox and composed/incremental equivalence, the preserved model
comparisons, source-backed controls and the new 345-case domain assay.

The selected corpus remains 389 accepted, 381 matched and eight mismatched,
with no rejected or ambiguous outputs. The migration-aware legacy380
fingerprint and immutable legacy archive are unchanged. Against the accepted
base, 561 existing protected tracked files are byte-identical, including
executable source, scientific data, earlier adjudications and receipts,
baselines, lexical model entries and lexical ordering sources/manifests.
All 167 elaborated lexical entries retain their editorial sequence. The
executable source SHA256 remains the value recorded above; no cascade,
historical chronology edge or protected output changed. All 97 published
reader identities retain their canonical executable order.

The strict publication wrapper completed the reader, lexical and combined
builds. Semantic markup, bibliography and section-locator source checks,
predicted-form policy, cross-references, index invariants and TeX index policy
passed. Assembled explicit index parity is 1467 printable and 81 excluded,
with zero predicted, unknown, duplicate, missing or semantic-mismatch cases;
all 18 negative index fixtures passed. There are zero unresolved publication
references. Index occurrence changes are downstream source-line locations,
not altered lexical identities or scientific forms.

Rendered inspection covered combined PDF pages 79--83 (SC052, SC035 and
SC056), 94 (SC073), 96 (SC076) and 290 (new bibliography), and standalone
reader pages 77--79 and 93--94. The complete SC035 evidence, rule box,
citations and alternatives render correctly, without new file-driven page
breaks or blank pages. SC035 remains after the relevant palatalization and
before SC056. The resulting reader, lexical and combined PDFs contain
105, 158 and 298 pages respectively.

## Residue

Missing evidence: an independent non-ga positive, secure absolute raising
date, exact early vowel height, and enough same-environment contrasts to
choose a broader palatal/internal domain. Those are not established by
more prefix tokens.

Missing source access/verification: Pheifer1974 full critical edition and
the relevant1987 study, direct modern Erfurt palaeography/facsimile review,
and Wright volumeII for Toller's gi-mynd. They would improve the exceptional
ga collation, witness relationships/dates and that later token; no inaccessible
page is presented as read. Toronto required human verification; the Bodleian
catalogue likewise did not yield an accessible record. Sweet's directly read
Hatton transcription and Hogg's Alfredian dating remain the declared basis.
No author decision is needed for a protected-output transition.
