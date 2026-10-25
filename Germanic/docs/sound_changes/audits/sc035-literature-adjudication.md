# SC035: specialist literature, accentuation and manuscript evidence

Source-critical amendment to the delivered text at `976c1d07`:
[the final scholarly audit](sc035-source-critical-audit.md) records the
scan/manuscript checks and claim-by-claim statuses. Sweet and Pheifer agree
on *gihiodum* (Sweet p.40); *gibiodun* in the frozen ledger is a CAPR
transcription error, not an editorial disagreement. Samuels p.110 prints
*gisihðe*, and Sweet p.602 glosses Corpus *gibrec* as 'phlegm', not
'breaking'. The corrections below amend active interpretation explicitly;
the 51-observation ledger and earlier validation receipts are unchanged.
RETAIN/B, stage, scope, order, rule and corpus remain unchanged.
The expanded final audit additionally rechecks the competing historical
accounts, the lack of independent non-ga controls and the bounded formal
domain. Its [edition-separated apparatus](sc035-source-collation.md)
covers all51 frozen observations and the modern revised edition; its
[validation closeout](sc035-final-validation.md) distinguishes fresh
runtime checks from reused historical experiments. Together these amend
the active interpretation here without replacing frozen receipts.

## Identity

- **SC id:** SC035.
- **Executable identifier:** `OEPrefixAReduction`; the identifier supplies
  neither the historical stage nor a morpheme-identity condition.
- **Date / branch / base commit:** 2026-10-25 / `update` /
  `fdee650f2c0084bbc05c5b683ea0545d0f49081c`.
- This follow-up supersedes the current interpretation, not the preserved
  observations, of `sc035-generality-adjudication.md`. All four earlier
  adjudications and their frozen assays remain historical receipts.

## Question

- **Hypothesis or suspected problem (falsifiable):** does the specialist
  evidence favour regular raising of short weak pretonic ae after a
  palatal fricative, or establish a better regular pathway or positive
  analogical replacement? Is *ġeatwe* independently established to contain
  the inherited prefix, and can manuscript or stacked-prefix evidence
  refute the current historical environment or its bounded implementation?
- **What evidence would confirm it; what would refute it:** early high-vowel
  forms, independently reconstructed weak stress and a genuine palatal
  trigger support raising. A securely unraised short weak vowel in the
  same early environment would refute the proposed exceptionless law.
  An independent non-ga positive would strengthen its generality.
  A demonstrated redistribution of prefix allomorphs could favour analogy.
  Late e alone cannot choose among these pathways. An uncertain etymology
  cannot establish an exceptional inherited accent.

## Current state (before any edits)

- **Existing historical characterization:** registry `preoe`,
  `english_specific`, confidence `B`, verdict `RETAIN`; inventory
  "Pretonic front-vowel raising after a palatal fricative",
  `source_partial_chain`. The reader nevertheless called *ġeatwe* an
  exceptional accented prefix without discussing competing etymologies.
- **Existing executable behavior:**

  ```foma
  define OEPrefixAReduction SentenceCtx([
      {*æ} -> {*i} || .#. {*ᶠ} OEAnyConsonant* {*ʝ} _
  ]);
  ```

  The positive context marks one initial short weak syllable followed
  across consonants by an independently accented head. It is preserved
  after earlier rules consume acute accents. This is not a general parser
  of metrical or compound domains. The prepare packet's numbered position
  is 61; the execution-registry index is 63; the firing census labels the
  result stage 62/108. These are different coordinate systems, not dates.
- **Selected-input assumptions:** *believe*, stable row 1944, feeds
  `*galáubijaną`, with root stress explicitly encoded, and targets
  *ġelīefan*. No new input accent, paradigm cell or target is inferred from
  an Épinal spelling.
- **Existing verdicts/dossiers consulted:** original SC035 closure,
  model-comparison, prosody and generality adjudications and assays;
  grouped 035–037 book dossier; SC052, SC056, SC073 and SC076 discussions.
  Superseded protective-vowel arguments are not current chronology.

## Diagnosis

- **Complete firing census:** supported `SC035 --prepare` and
  `SC035 --evidence` were run before SOURCE edits. The forced canonical
  rebuild and production/sandbox comparison agree on all 389 selected
  rows. The sole firing is *believe1944*, also a member of the original-380
  identity population; it is in-domain. There are no additional live
  positives in the remaining selected rows or an independent second
  population of 380 new observations.
- **Principal witness traces:** census display
  `*ʝ*æ*l*ēa*β*j*ą*n` → `*ʝ*i*l*ēa*β*j*ą*n`.
  Internally both carry the initial `*ᶠ` context annotation. SC107
  supplies the front vowel; SC052 supplies the palatal fricative; SC073
  leaves raised i intact; SC076 lowers it and removes the annotation.
  FST SHA256:
  `421e7ae9c0a705f910e081e20242f8f7b3a42731b9dc908124217d32826a9d77`;
  corpus SHA256:
  `d40b6e65280d4cbe8acb08271803ef8acc64b3ff8e6b2656d416951aebdfa0a0`.
- **Witness role classification:** *believe* is the live application and
  model-feeding witness. The existing full-input *ġestīgan* assay is an
  isolated historical positive, not a selected-corpus firing.
  *sċeaft/ġesċeaft* is a source-backed stem comparison for headed-foot
  diphthongization; it does not provide an independently accented full
  PGmc citation cell. *ġiest, ġiefan, sċēap* are stressed negative controls;
  *ġealla* already contains a breaking product. The 345 artificial cases
  check implementation boundaries, not 345 historical attestations.
  No new skip/displacement experiment is needed: no order change is
  proposed, and earlier counterfactuals are preserved without promotion
  to independent chronology.

## Literature

- **Existing CAPR dossiers checked:** those listed under Current state,
  including their source locators and the 51-observation generality
  ledger. That ledger is not silently corrected or enlarged with
  overlapping aggregate counts.
- **Sources checked, with page numbers:** Bammesberger1981, pp. 377–391;
  Quinlin1991, pp. 145–159; Gante2012, handout pp. 1–4 and slides 7–9;
  Crouch1995, pp. 173–176; Minkova2008, pp. 22–23, 38–41;
  Pheifer1974, pp. xxi–xxxi, xl–xli, lxxv §63, and pp. 2, 6, 13, 39,
  74, 108; Pheifer1987, pp. 34–37; HerrenSauer2016, pp. 129–132;
  Samuels1949, pp. 109–112, especially 110; Campbell1959, pp. 31 §74,
  140–141 §§333–334, 149 §358 n. 6, 153–155 §§369–370;
  HoggGrammar1992, §§5.48 n. 1, 6.48–6.54 (held 2011 reprint,
  pp. 104, 236–239); RingeTaylor2014, pp. 206, 334–335;
  Ringe2017, pp. 305–306; Berg2014, pp. 60–61;
  Orel2003, pp. 128, 331, 403; Kroonen2013, pp. 84–85, 170–171.
  Existing Sweet/Toller, manuscript-catalogue, Northumbrian and prosody
  evidence remains available through the earlier ledger.
- **Source-supported historical phenomenon:** inherited ga has weak OE
  reflexes and genuinely early i spellings alongside e; nominal accent
  and some alleged exceptional etymologies are disputed. Weak vowels,
  palatal articulation and stress-foot structure supply phonological
  motivations, not proof that every written vowel names a distinct
  prehistoric phoneme.
- **CAPR modelling decisions:** retain the specific ae-to-i realization
  after the palatal fricative and the positive one-pretonic-syllable
  context as the best bounded representation. Neither a universal
  PGmc clitic analysis nor a universal OE compound parser is adopted.

### Direct comparison of the accentuation arguments

Bammesberger starts with Germanic initial word stress for inherited nominal
compounds, explicitly distinguishing verbal ga constructions
(pp. 377–378). His argument is not merely that nouns "should" have prefix
stress. In §3.2, p. 381, West Germanic d in the birth noun is contrasted
with Gothic þ. Starting from original voiced d, he invokes Thurneysen's
Law in an unstressed root syllable, hence a stressed prefix. His n. 9
rejects a root-stressed alternant on reconstruction/Indic grounds; n. 10
acknowledges other Gothic ti abstracts for which analogy would be needed.
The singleton n of Gothic *gaman* is a further, defeasible unstressed-root
argument (p. 382). The comparison with OE *gamen* 'game' requires a semantic
bridge from companionship; *gamall* is expressly unsafe if its formation
is uncertain (pp. 383–384). Later accent retreat is attributed to the
increasing influence of verbal/deverbal formations (pp. 384–385), not to
documented bi-driven vowel replacement.

Quinlin reconstructs a clitic whose syntactic accent must be distinguished
from primary word stress (pp. 145–146, 150–153). He contests the geminate,
semantic and formation assumptions behind *gaman/gamen* and *gamall*
(pp. 153–155), then challenges the accentual implications of the birth noun
(pp. 156–157). This makes a never-primary-stressed account possible; it does
not independently prove every etymology in that account. Independently,
Ringe2017, pp. 305–306, treats *gaburþi- / gaburdi-* among inherited
Verner alternations of ti abstracts, discussing subsequent generalization.
Thus Bammesberger's insistence on a unique voiced preform and his
Thurneysen inference are not compulsory. Conversely, none of this refutes
the comparative consonantal observation itself.

Gante's handout distinguishes nominal bases from merely nominal results;
the handout and slide survey are comparative/classificatory support, not
an independent date or demonstration of OE raising. Crouch's weak ge and
host-unit discussion is about clitic/affix properties; its historical
stress claims partly depend on Quinlin and Bennett. It is not another
independent vote for never-stressed PGmc ga. Bennett1968 remains unread
and no argument is attributed to its unavailable text.

### The category membership of ġeatwe

The result is **competing interpretations, not securely accented inherited
ga**. Campbell's traditional exception (p. 31 §74 n. 5) must be read
alongside his explicit doubt about the relationship of the associated
forms (p. 149 §358 n. 6). Bammesberger assigns *ġeatwe* and ON *gǫtvar*
to a prefixed equipment formation and treats the contrasting vowel/stress
pattern secondarily (p. 384 n. 17). Quinlin separates *ġeatwe* from
*getāwe* 'deeds', the latter associated with Gothic *gataujan/taui*,
and relates equipment *gǫtvar* and Gothic *gatwō* 'street' through an
unprefixed gat stem and a wō formation (pp. 155–156). His semantic bridge
through burial equipment is plausible but not independently demonstrated.
The relation of the manuscript/lexicographic forms conventionally grouped
as *getuwe/getāwe* cannot simply be assumed to supply an accentual doublet.

The consonantal g-t framework and w extension alone do not choose between
a lexical gat stem and a prefix plus dental-initial base. The inferred
vowel alternations and accent differ precisely because segmentation and
stem formation differ; no independent inherited accent resolves them.
Orel's equipment entry remains under *tawō* (p. 403), with origin unknown:
later scholarship has not simply converged on Quinlin. Orel p. 128 and
Kroonen pp. 170–171 support a hole/road family, but do not establish its
equation with the equipment word. Kroonen also treats the defecation sense
as secondary and proposes a different semantic history. These are limits
on corroboration, not reasons to select an etymology by output fit.

Consequently *ġeatwe* is excluded from secure stressed-prefix diagnostics
and from decisive dating of the prefix's reduction relative to palatal
diphthongization. Its ordinary stressed-vowel history is not denied.
Quinlin's full alternative is not promoted to a proved corpus input.

### Pheifer's aggregate evidence and textual layers

`sc035-literature-counts.tsv` transcribes the four gi/ge and bi aggregate
rows of §63, p. lxxv. These are the edition's counts, not a fresh
token-by-token recensus:

| Witness | gi | ge | gi + ge | i proportion | bi / be |
|---|---:|---:|---:|---:|---:|
| Épinal | 40 | 13 | 53 | 75.47% | 11 / 0 reported |
| Erfurt | 31 | 34 | 65 | 47.69% | 11 / 0 reported |

Pheifer separately reports Épinal ti once (195), Erfurt te twice
(343–344). Hogg's aggregate prefix totals (§6.53: 52/13 and 42/36) combine
these categories and bi: they are not contradictory gi counts.
Pheifer's footnotes 2–6 on this page qualify the preceding medial/final
counts; they must not automatically be imposed on the initial-prefix
denominators. The edition does not supply a complete row-level list of
the 53 and 65 gi/ge classifications or say explicitly how every corrected
prefix enters those totals. That inclusion policy remains unverified.

The descriptive difference is 27.78 percentage points, not a transition
rate or a significance test. Denominators differ, token identity is not
fully enumerated here, and the witnesses share transmitted material.
The old nine paired comparisons show both directions of spelling
difference; adding their 27 readings to these aggregates would double-count.
Corpus ge is frequent, not categorical: the earlier ledger's *gibrec*
remains. Pheifer's editorial conventions (p. 2) deliberately omit merely
orthographic/phonological OE differences from some collations, so his
apparatus cannot establish an exhaustive Corpus-vowel census.

Pheifer suggests that stressed bi might affect its contrasting frequency,
or that ge includes an ablaut variant corresponding to continental ga.
He points to Erfurt *gaesetu* (728) and possibly *gaeadun* (76). These are
hypotheses, not demonstrated prefix-allomorph replacement. Uniform bi
beside variable gi does not provide a matched weak-syllable experiment:
stress, lexical distribution and transmission are not controlled.
It neither proves analogy nor by itself refutes a later general weak-i
lowering. Whole-prefix alternation in Samuels is a different phenomenon.

The new `sc035-literature-readings.tsv` supplements, rather than mutates,
the 51-observation Sweet-based ledger. Three important qualifications:

- EE76 (correction C01): Pheifer p. 6 and Sweet p. 40 both print Épinal
  *gihiodum*. The manuscript f.1v (bound94v), column d, confirms h.
  Pheifer p. lxxxiii §72 n. 6 interprets it as apparently marking hiatus;
  p. xxiii §4 n. 1 questions expansion of the final nasal. The visible
  written m, an explanation involving an erroneous expansion, and an
  emended n are distinct. The apparatus gives Corpus *geeodun, -on*.
  The frozen ledger's *gibiodun* is erroneous, not Sweet's transcription.
- EE228: *gybyrdid / gebyrdid* belongs to the gloss for *clabatum*.
  Pheifer p. 74 interprets it as 'striped(?)', comparing *bord* and
  Latin *clauus*. The former reader gloss 'born' was wrong; this is not
  an attestation of the birth noun *ġebyrd*. Its y remains a grapheme,
  not proof of another rounded-vowel law.
- EE728: Pheifer p. 39 gives Épinal *saegesetu*, Erfurt *saegaesetu*,
  and Corpus *saegesetu* in the apparatus; p. 108 interprets maritime
  regions. This internal weak syllable is genuinely relevant to domain
  research, but its early stress, vowel quantity/value and trigger are
  not independently established by that spelling.

| Witness | Surviving copy | Exemplar / linguistic layer | Consequence |
|---|---|---|---|
| Épinal | Around 700; England, precise location uncertain | Earlier compiled material; conventional dialect labels do not localize every entry | Not an unmixed spoken sample |
| Erfurt | Cologne, second or third decade of 9c in Herren/Sauer | Common ancestor with Épinal; Pheifer argues for an intervening English scribe | Continental copy date does not date English vowels |
| Corpus | 9c; first-half dating in Lucas, mid-century in Herren/Sauer | Related expanded/revised recension, not a direct copy of surviving Épinal | No independent universal e endpoint |

The updated Erfurt date is HerrenSauer2016, p. 130, citing Bischoff's
catalogue; it supersedes the uncertainty of the older intake summary,
not the bytes of its historical witness ledger. Pheifer1974 p. xli §24
argues Erfurt is not copied directly from Épinal and requires an
intermediate English layer. Pheifer1987 pp. 34–37 and Herren/Sauer
pp. 131–132 qualify the relationships and reconstruction. Manuscript
date, exemplar, English dialect, copy spelling and phonological stage
are therefore separately recorded, not collapsed into gi-before-ge.

Early Northumbrian *gistiga*, Vespasian and Alfredian ge, Durham Ritual gi,
and Corpus gi remain the independent textual traditions already documented.
Samuels1949 p. 110 adds the Lindisfarne–Rushworth comparison: prefixed and
unprefixed nouns alternate in Lindisfarne, while Rushworth2 has gi forms,
including *gisihðe* (correction C02: the earlier image transcription
incorrectly omitted h). His subject is prefix presence/function,
not a gi/ge frequency census. Late Northumbrian gi may involve continued
spelling or raised allophony (Hogg §6.54); it is not the date of one
pan-English lowering event.

### Image checks and limits of the source witnesses

The actual canonical PDF images were opened at these locations:

| Source | Printed pages | PDF sheets, respectively |
|---|---|---|
| Bammesberger1981 | 381, 384 | 5, 8 |
| Quinlin1991 | 155, 156 | 11, 12 |
| Pheifer1974 | lxxv, 6, 13, 39, 74 | 73, 95, 102, 128, 163 |
| Minkova2008 | 39 | 19 |
| Samuels1949 | 110 | 49 |
| Orel2003 | 128, 403 | 167, 442 |
| Kroonen2013 | 170 | 210 |
| Ringe2017 | 305 | 316 |

The ga-prefix holdings manifest supplies the intake PDFs' identities and
SHA256s; the established dictionary/grammar holdings resolve through their
bibliographic records. Session image exports are disposable aids, not a
new source authority. Quinlin p. 155's damaged OCR `*/--/` reads
`*/-ō-/` beside `*/-wō-/` on the image. Samuels's damaged *gisihoe*
reads *gisihðe*, not the earlier audit's *gisiðe* (C02).
No global OCR substitution or source-text rewrite was made.

Pheifer's supplied PDF is itself a converted reprint with missing
diacritics. Its image confirms numbers and the visible letter readings,
not lost original type. No restored accents are inferred. Campbell and
Ringe/Taylor are held as searchable texts; an independent PDF witness was
not available for their passages. Their page/section locators are retained
and no new fine typographic distinction rests solely on their extraction.

## Historical analysis

- **Historical stage:** retain pre-OE raising, with later weak-i lowering
  treated separately in OE; no absolute date is deduced from the FST name
  or a surviving copy.
- **Historical scope:** retain `english_specific` for this English
  reconstruction, not a claim that continental gi is absent or shares
  exactly its trigger/history. Continental ga and gi do not date English
  palatalization.
- **Regular phonological conditioning:** short weak pretonic front vowel
  immediately after palatal fricative ʝ, with independently established
  stress. Morphological analysis may recover accent/domain but is not a
  condition such as "belongs to ge".

### Four accounts and discriminating predictions

| Account | Early / late prediction | Positive evidence and assumptions | Refutation / unresolved prediction | Chronology |
|---|---|---|---|---|
| A: fronting, palatalization, ae > i, later i > e | Early high forms; late weak e | Ringe/Taylor p. 335 proposes this regular mechanism; early gi, weak stress and palatal articulation support it. Exact ae/i height remains reconstructed | Secure short weak ae after established ʝ at the relevant early stage would refute it; no such negative or independent non-ga positive verified | Fronting and palatalization feed raising; lowering follows raising |
| B: another regular phonetic/allophonic pathway | Early i spelling could record a raised realization rather than a separate obligatory i stage; later e | Hogg §§6.51–6.52 establishes weak front-vowel raising BEFORE following palatals; §6.54 allows late Northumbrian raised allophony | These are opposite trigger direction or a later variety, not independent evidence for early raising AFTER ʝ. A broad all-palatal trigger predicts more than the examined sources establish | Could permit merger before some raised realizations; no new historical ordering demonstrated |
| C: fronting and merger without obligatory high stage | Late e straightforward; earliest gi still needs an account | Ordinary fronting/merger is independently supported | Without an evidenced early allophonic or spelling account, genuine gi remains unexplained. Equal late outputs do not solve that problem | Fronting before merger; no reason for obligatory raising/lowering under this account |
| D: bi-driven analogy | gi after replacement; later lowering can yield ge | Possible influence in Ringe/Taylor p. 335 and Berg pp. 60–61; no examined positive replacement record | Requires independently motivated redistribution, a model and chronology of replacement; resemblance and uniform bi do not supply them | Replacement must precede affected gi attestations, but its date/mechanism is not established |

Ringe/Taylor's bi suggestion is attributed to Bammesberger *p.c.*; it
must not be conflated with Bammesberger1981's nominal-stress argument.
The latter's analogical accent retreat is another distinct proposed
process. Account A wins on positive explanatory coverage of the early
forms and an explicitly proposed, plausible regular environment, not
because all its phonetic details are observable or because analogy is
forbidden in principle. Account B is a real alternative worth testing,
but the sources examined do not establish a better early pathway.
No artificial displacement or final-output tie breaks that comparison.

For B, extending the trigger to all palatals would predict raising after
other palatal onsets in the same short weak environment; a securely
unraised early counterpart would refute that extension. The narrower
allophonic version needs an independently evidenced relation between
vowel realization and spelling, not simply permission to interpret every
awkward grapheme differently. For C, early gi is the actual adverse
observation against a merger-only account with no additional mechanism.
For D, there is not yet a specified and independently evidenced
redistribution from which token-level positives/negatives can be predicted.
That under-specification is a weakness, not permission to invent
unobserved replacement conditions. An independent non-ga positive in
the same environment would support the regular mechanism without proving
that analogy never operated anywhere.

### Prosodic domain and generality

Minkova2008 pp. 38–41 independently prevents equating "weak ge" with
"first syllable immediately before primary stress":

| Attested analysis | Prosodic finding | Consequence for SC035 |
|---|---|---|
| *mísgewìeld* 'error': (mís-ge)-(wìeld) | Internal unstressed ge is incorporated into the first prosodic word by postlexical foot-binarity adjustment | Real internal weakness; not the current initial pretonic configuration |
| *geédnìwad* 'restored': ge-(éd)-(nì.wad) | Weak initial ge before an independently stressed inner prefix; hiatus | Cannot be encoded by inventing a consonantal bridge |
| *únforcùð* 'dishonest' | Multiple stress domains; related prosodic configuration, no same palatal trigger | Useful domain comparison, not another raising positive |

Minkova explicitly limits the evidence for extending the noun/adjective
analysis to finite double-prefixed verbs (p. 39). This is OE prosodic
evidence, not a direct reconstruction of the PGmc accent of every component.
The current marker faithfully covers the independently specified
one-weak-syllable citation-word cases. It does not encode all three
structures above, and should not be described as doing so.

Internal *modgidanc* in Sweet and *saegaesetu* in Pheifer deserve future
early-domain analysis, not dismissal because a regex is word-initial.
Neither presently establishes the same early short vowel, trigger,
prosodic position and chronological layer. No source-backed new case
justifies expanding the marker or all-palatal raising. Long weak vowels,
hiatus and multiple pretonics remain historically unanalyzed cases, not
negatives refuting the short-vowel law or positives obtained by synthetic
accent placement.

- **Counterexamples and falsification:** no independent non-ga positive
  and no genuine same-environment negative has been established.
  Stressed *ġeatwe* is etymologically contested; *gaeadun* has additional
  vowel-initial-root/transmission issues; internal *saegaesetu* has unresolved
  prosody. None is declared irrelevant or silently assigned a rescuing
  vowel quantity. The restricted data leave exact historical generality
  open. Stressed palatal-diphthongization controls remain genuine negatives
  for applying the weak-vowel operation.
- **Positive evidence for analogy:** none for bi-driven replacement in the
  sources examined. Pheifer's distribution raises a question, not an
  allomorph-migration record; Samuels's prefix-presence alternations do not
  answer that question.
- **Relationship between historical phenomenon and executable proxy:**
  the executable is explicitly narrower than the possible historical
  weak-syllable domain. Its regular phonological kernel remains the
  best-supported representation of the covered witnesses. It is not
  claimed that all complex compounds have been shown to satisfy it.

### Candidate disposition

| Candidate | Status and reason |
|---|---|
| *ġestīgan*, early *gistīga* | Existing source-backed isolated full-input witness, with independently accented verbal root; retain its established assay, no redundant selected-corpus addition |
| *ġesċeaft/sċeaft* | Existing source-backed headed-root stem comparison; Orel p. 331 corroborates the creation formation, but no new fully specified regular PGmc cell is supplied here |
| *ġebyrd* | Comparative formation genuine; dental alternation/accent and selected paradigm cell need independent work. Not identified with EE228 |
| Pheifer early gi/ge/ga/gy | Manuscript evidence, not automatically executable full historical inputs or late WS targets |
| Gante's *ġesīþ, ġelīc, ġemæne* | Comparative nominal candidates, but another inherited prefix alone does not discriminate the alternatives; no new accented cells admitted |
| Internal/stacked forms | Source-backed domain constraints; no invented early accent or full PGmc compound supplied |
| Artificial controls | Technical positives/negatives only; do not count as lexical expansion |

No new selected entry or protected-output migration is proposed.

- **Chronology evidence:** the two existing SC035 earlier-boundary
  relations name SC107 and SC052 as prerequisites, classified
  `technical_computational` / `technical`. They are conditional feeding
  requirements of account A, not new independently demonstrated historical
  edges and not stage-entailed dates. SC056 remains stressed-foot
  diphthongization; its root/weak-vowel contrast survives without using
  *ġeatwe* to date prefix accent loss. SC073 before SC076 follows Hogg's
  relative account of weak-vowel mergers, not a universal manuscript
  calendar. Pheifer's gi/ge counts alone do not establish that ordering
  or an interval. No edge is newly promoted as `stage_entailed` or
  `independently_demonstrated`; no edge, rule position or chronology card
  is changed.

## Verdict

- **Verdict:** RETAIN executable rule, bounded domain, stage, scope and
  ordering; confidence **B**. Revise the historical explanation and
  remove the unqualified stressed-prefix diagnostic and erroneous
  'born' gloss.

Registry-verdict: SC035=RETAIN

- **Justification:** regular raising explains genuine early high-vowel
  forms through an independently motivated weak/palatal environment,
  whereas merger alone leaves them unexplained and no positive bi-driven
  replacement has been established. The specialist evidence neither
  supplies a better regular mechanism nor demonstrates an unraised vowel
  in the same securely reconstructed environment. It does establish
  important limits: *ġeatwe* is not a secure prefixed exception, aggregate
  spelling counts are transmitted and non-independent, and stacked-prefix
  prosody extends beyond the current implementation. These justify a
  substantially corrected account with qualified confidence B, not a
  gratuitous formal change or a claim of universal demonstration.

## Propagation (only after verdict)

- **Affected files/registries:** this follow-up and its two evidence
  tables; SC035 reader; narrow SC076 chronology clarification; current
  preface of the grouped book dossier; SC035 registry authority pointer
  and inventory judgement. Previous records, original texts/PDFs, FST,
  chronology and corpus SOURCE remain unchanged. All derived views and
  assembled volumes are owned by the artifact graph.
- **Regression tests added/updated:** the active authority assertion
  follows this memo. New tests distinguish aggregate populations from
  repeated attestations and preserve source/edition identity, correction
  qualifications and the disputed readings. Existing positive and negative
  phonological assays remain the semantic tests; documentary assertions
  are not presented as proof of a sound law.
- **Publication tooling repair:** the citation checker previously recognized
  only Arabic page numbers and rejected Pheifer's actual Roman pagination.
  It now accepts Roman locators, with positive/negative regression cases.
  The unpaginated Pforzen object retains its explicit catalogue-locator
  exception. Scholarly locators and prose were not distorted to satisfy
  the checker.
- **Baseline/fingerprint effect:** none expected. Selected-389
  `53769ef582dd6d119bacc18f808612980a1f02dfed2f94a6e30645bb9de00a9e`;
  original-380 identity
  `43de8a47b7aaf17f860c9e3009617002ddb36e4d32a90ede1a99525858a417ce`;
  lexical projection
  `c44d73698e2fa2717366e951a75bbb02d19aa677faf51fc86dfa25187556b6da`;
  immutable legacy archive
  `fae656520e9ebf446854643907a1ba48a511877fc25b1fae39649d5b97e9a6cf`.

### Validation receipt

- Supported `SC035 --finalize` passes; strict `artifact_graph.py --check`
  reports `CONTROL PLANE CLEAN`.
- The affected SC035, registry, inventory, reader architecture, citation,
  lexical-integration and protected-baseline regression selection passes:
  **170 tests, 5 runtime tests deselected, 5,989 subtests passed**.
  The separate fresh adopted-cascade test also passes: all 389 selected
  rows agree with canonical production at the checked stages, composed
  and incremental execution agree, and the established historical
  positives and stressed/other-environment negatives retain their results.
  The five deselected historical/domain runtime assays were not replayed;
  their frozen receipts and scripts are byte-preserved. No formal,
  chronological or lexical change called for a new full-suite refreeze.
- `INDEX_VERBORUM_STRICT=1 ASSEMBLY_KEEP_DEBUG_TEX=1 bash
  Germanic/docs/assembly/build_capr_book_draft_docker.sh` completes,
  including standalone reader, standalone lexical volume and combined
  book. Exact executable-order parity is 97 identities; the reader prints
  the canonical definitions. Bibliography, cross-references, semantic
  policy, paragraph glosses, heading wrapping, index occurrence parity,
  print-index readiness and all 18 negative index fixtures pass.
  Combined and lexical publication checks report zero unresolved internal
  references; combined TeX/PDF have no residual sect/sects locators.
- Visually inspected final SC035 pages in the standalone reader
  (physical/printed 77–80) and combined book (physical 79–82, printed
  77–80), including the aggregate table, accents, rule and cross-references.
  SC076 was checked at reader p. 94 and combined physical pp. 96–97
  (printed 94–95). New bibliography entries were checked in the reader
  pp. 103–105 and combined physical pp. 288–291 (printed 286–289).
  The manuscript counts, Roman locators and specialist citations render
  legibly; the printed reconstruction agrees with the retained rule.
- Byte comparison with the base preserves FST, corpus data, chronology
  edges, selected-output/input baselines, lexical models/editorial order,
  original source holdings/bibliography, all earlier SC035 adjudications,
  their 51-observation ledger and experimental receipts. The two
  pre-existing untracked scratch files remain untouched. Generated
  manuscripts/indexes and registry views change only through their owners.

## Residue

- Exact phonetic height and chronology of early raising; independent
  non-ga evidence; early internal weak-syllable histories; *ġeatwe*
  segmentation and inherited accent; full row-level reconstruction and
  correction policy of Pheifer's prefix counts remain open.
- Bennett1968 remains unavailable. Pheifer's removed diacritics need an
  independent printed witness where they become decisive; no marks are
  fabricated. These limitations do not prevent the present bounded verdict.
- No author decision or baseline adoption is required for these
  prose/evidence corrections. No SC036 investigation is begun.
