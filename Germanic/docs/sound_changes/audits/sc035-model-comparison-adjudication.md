# SC035 follow-up: compressed and staged weak-prefix models

## Identity

- SC id: SC035; executable identifier: `OEPrefixAReduction`.
- Date / branch / accepted base: 2026-10-22 / `update` /
  `5533f7653f87d3962a92935a280190882c16b61b`.
- This is a follow-up, not a rewrite of `sc035-adjudication.md` or its
  frozen `sc035-prefix-reduction/evidence.json`.

## Question

Can ordinary unstressed fronting, preservation of the prefix's weak
prosody, and a later front-vowel merger give a historically better account
than early conversion to technical `*ĕ`? A staged model must preserve
genuine stressed palatal-diphthongization witnesses, explain its treatment
of early *gi-* rather than invent that development, and expose every
change in the complete selected and migration-aware legacy populations.
An output match alone cannot decide between compatible reconstructions.

## Current state (before any edits)

The accepted characterization is pre-Old English onset, Old English
completion, `english_specific`, confidence A for existence, with a
restricted, boundary-free `gaCV` proxy. The literal law maps initial
unaccented `*a` to `*ĕ`; the one live application is believe, row1944,
selected `*galáubijaną` > *ġelīefan*. Its SC107 dependency is technical;
the older PWGmc bundle boundary is runner-limited. Neither dates an
independent historical event before stressed SC043.

The complete accepted memo, recorded experiment and code, actual
definitions/composition, published discussion, SC043 memo and adopted
component dossier were read. No SC036 work exists in the starting
worktree. The two pre-existing untracked scratch files remain untouched.

## Diagnosis

Fresh supported `SC035 --evidence` rebuilt and validated the canonical
bins and reconfirmed the one live application in selected389 and
migration-aware legacy380. The original closure's findings all survive.
`sc035-model-comparison/experiment.py` then used the established isolated
compiler, without changing canonical scientific sources.

### The representation problem

SC043's stressed clause maps `*á` to plain `*æ`. Thus guest has plain
`*æ` before ordinary palatal diphthongization even though its root is
stressed. Give retains `*é`; sheep has plain `*ǣ`. Gall already has `*ea`
from breaking and does not fire ordinary palatal diphthongization live.
Deleting its plain-vowel clauses, or treating absence of an acute as
absence of historical stress, is not a defensible restriction.

The post-tonic guard of `OEWeakTailReduction3` excludes an initial weak
prefix; it is not a source claim that prefixes failed to merge.
Conversely, removing that guard globally would expose stressed roots
whose acutes have already been absorbed. In a prefixed word, counting
the prefix as a preceding nucleus can also misclassify the root as
post-tonic. These are representation/domain issues, not discoveries of
different historical laws.

### Three serious complete-cascade models

| Model | Actual experiment | Historical assumption and limit |
| --- | --- | --- |
| A: accepted compression | Literal current cascade: weak `gaCV` becomes `gĕCV` early; `ĕ` surfaces as e. | Encodes the secure weak reflex, suppressing the unresolved internal route. Neither a separate dated early law nor a general prefix recognizer. |
| B: staged fronting/merger | At SC035 preserve weak-prefix context, leave `a` to SC107; prevent stressed processes on the weak vowel; merge weak `æ/i` to e late while preserving the root domain. | Makes ordinary fronting/merger participation explicit. Does not derive the attested early gi- from ga-; carrying weak æ through the intervening period is not established as its unique history. |
| C: staged prefix raising | B's explicit weak/root distinction, but raise weak `æ` to i after singleton g-palatalization; high i then needs no special exemption from ordinary PD; merge to e late. | Implements the regular-raising possibility at Ringe–Taylor p.335. Its regularity, precise domain and placement are not independently established; possible bi-influence remains an alternative. |

The experimental `*ᵖ` is a context annotation, not a vowel, phoneme or
sentence-level weak-word label. It uses the same context-lifting pattern
as existing `Ctx(T)`; it does not repurpose `*ᵘ` or `*ᶜ`. It is inferred
from initial unaccented `gaC+V` before root fronting loses stress, including
the cluster case. Like A it is not a general morphological boundary parser.
The input grammar already distinguishes ga-/bi- prefixes, but that
distinction is not carried as a persistent root-domain annotation.

B/C carry the annotation through 46 replaced components and remove it
after prefix-i reduction. Eight components need root-relative domains
(`OEBreaking`, `OEARestoration`, `OEIUmlaut`, `OEMedialSyncope`,
`OEUnstressedFrontingEarly`, `OEUnstressedLongVowelShortening`,
`OEMedUnstressedILowering1`, `OEMedUnstressedULowering`), in addition to
the explicit weak-prefix merger. This is not eight newly discovered
laws: it preserves which vowel is pretonic and which belongs to the
stressed root. In particular, root i cannot trigger umlaut of a prefix
merely because a macron/acute was computationally lost. Prefix protection
here does not deny the attested umlaut of other unstressed syllables.
Ordinary PD is initial-word restricted in the unchanged model; B exempts
only words whose initial vowel is positively marked weak, not all plain
front vowels. Neither candidate refactors the canonical stress system.

### Complete populations and intermediate differences

All **389 selected rows**, their **380 migration-aware legacy identities**
and **108 executable stages** were compared. Isolated A agrees with every
canonical stage snapshot as well as the final production transducer.
Incremental component execution agrees with the fully composed
transducer for every model.

B and C each change **only row1944 believe** at any selected intermediate
stage: 63 stages differ from A, initially through context annotation,
then through vowel representation, until surface conversion. All other
388 selected / 379 legacy rows have identical intermediate and final
outputs. Every model has **zero final differences** in both views.
All differences, complete focal traces, literal recipes and controls
are retained in the new `evidence.json`; the old experiment is untouched.

| Checkpoint in believe | A | B | C |
| --- | --- | --- | --- |
| After SC035 | `gĕ-` | marked weak `ga-` | marked weak `ga-` |
| After SC107 | `gĕ-` | weak `gæ-` | weak `gæ-` |
| After palatalization | `ʝĕ-` | weak `ʝæ-` | weak `ʝi-` |
| After ordinary PD | unchanged | unchanged | unchanged |
| After later merger | `ʝĕ-` | weak `ʝe-` | weak `ʝe-` |
| Final | *ġelīefan* | *ġelīefan* | *ġelīefan* |

Root quantity, root umlaut to `īe`, and the final selected output agree.
Guest still takes `æ > ea > ie`; give still takes `é > íe`; sheep still
takes `ǣ > ēa`; gall's breaking product remains unchanged at PD.
These are in-domain positive/root-negative controls, not a stress filter
inferred from missing acutes. Begin's `bi- > bĕ-` and stressed bind remain
identical at every stage. No selected ni-prefixed item exists; the ni
template is explicitly artificial, not a fabricated attestation.

### Source-backed cluster and representation controls

The full independently sourced input `gastḯganą`, outside the selected
corpus, gives A **ġiestīgan** but B/C **ġestīgan**, matching the source's
WS form. `ḯ` is CAPR's existing stressed-long-i notation for the source's
stressed root, not a new reconstructed sound. The stage-entry comparison
`*g*a*s*t*ḯ*g*a*n` agrees. This is real evidence of A's limited coverage;
it must not be hidden by unchanged corpus totals.

The separate control with plain `ī` reproduces **ġiestegan** under A:
it has omitted CAPR's independently available root-stress annotation,
so the shortening is a representation artifact, not evidence that the
historical root shortened. B/C's explicit root domain preserves it.
The stressed ga- control remains identical across all models; its suffix
is only a staged stress diagnostic, not a complete reconstruction of the
attested gear paradigm.

Supplying the independently attested early weak gi- at the merger,
with explicit weak/root context, gives ge- in B/C without raising the
root or shortening it. A's post-tonic merger alone leaves initial gi-
unchanged; A does not claim this component represents the whole prefix
history. Supplying gi- is **not** the same as deriving it: only C generates
it from ga-, under its explicit unproven regular-raising hypothesis.

The boundary-free gaCV and pre-lC strings are formal controls only.
They expose the absence of morphological recognition and the need to
distinguish pretonic from post-tonic position; no resulting synthetic
surface form is offered as a historical positive or negative.

## Literature

The consequential contrasts are narrowly defined:

- Campbell 1959 pp.140–141 §§333–334: ordinary unaccented fronting and
  its syllabic nasal distinction; pp.153–155 §§369–370: later merger,
  explicitly including early *bi-*, *ni-*, *gi-*.
- Campbell 1959 pp.69–70 §§185–188 and Ringe–Taylor 2014 pp.215–217:
  genuine palatal diphthongization, including give, guest and sheep.
- Ringe–Taylor 2014 p.206: the weak prefix does not diphthongize;
  pp.334–335: stressed prefix contrast, early *gi-*, later *ge-* and
  explicitly alternative regular-raising/*bi-*-influence explanations.

The regular pretonic raising hypothesis is therefore a reason to test a
third candidate, not a license to declare a new established sound law.
Local text holdings, not newly verified original page images, are used.

Focused checks also included Ringe–Taylor pp.192, 255, 264, 298–299:
unstressed æ is not retracted; only unstressed high front vowels trigger
mutation; syncope and shortening concern unstressed vowels. Campbell
pp.142–144 §§341–344 and p.148 §355 independently distinguish unstressed
syncope/shortening. These motivate preserving the root domain in B/C,
not a general prohibition on mutation of unstressed vowels (Campbell
p.142 §339 and Ringe–Taylor p.253 explicitly discuss that mutation).
The existing SC056 adjudication's ordinary-before-mutation analysis is
preserved and independently confirmed by the guest trace.

## Historical analysis

The historical stage remains pre-OE onset with OE completion, scope the
English trajectory, and confidence A for existence only. The prefix
participates in the ordinary fronting/merger history; a separate early
prefix-specific *a > e* law is not demonstrated.

B establishes that a protected special vowel is **not computationally
necessary** once weak-prefix/root context is retained. C establishes the
compatibility, not the truth, of regular raising after the palatal
fricative. The common endpoints and stressed/weak contrast are secure;
the precise intermediate route and its ordering relative to palatal
diphthongization remain underdetermined. B is a possible partial
staging, not a complete explanation of early gi-. C's fuller staging
requires a historical hypothesis the sources expressly do not decide.

A is consequently retained as a **provisional compressed model for its
declared restricted population**, not as the uniquely necessary or
universally best grammar. It commits to the secure weak outcome without
choosing an unestablished raising law or an exact period of retained weak
æ. Its superiority to B/C as historical reconstructions is not claimed.
The staged models' genuine coverage advantage for clusters is preserved
as an executable research result, not dismissed because it lies outside
the selected corpus. A future general prefix account should use that
comparison, but must resolve or openly parameterize the unresolved
pathway rather than silently declare either B or C the attested sequence.

No adjudicated conclusion about SC043 or SC056 is overturned. The
unchanged SC107 and SC073 fragments are not complete historical domains;
their combination with an explicitly weak prefix is coherent in B/C,
while A compresses that interaction. No canonical restrictions or broad
merger are adopted. Both existing SC035 edges remain technical/runner
observations, neither `stage_entailed` nor
`independently_demonstrated` historical precedence. No edge is added,
removed or reversed and no experiment dates SC035 before stressed SC043.

## Verdict

**Outcome C: historical pathway underdetermined; RETAIN A provisionally
and REFORMULATE its comparative justification and limitations.**

Registry-verdict: SC035=REFORMULATE

The sources secure fronting, weak prosody, early gi- and later ge-, but
do not establish the regular raising and exact chronology needed to
prefer one fully staged pathway. Successful B/C execution refutes a
claim that the incumbent marker is intrinsically necessary and improves
cluster coverage; it does not prove either proposed sequence. Compression
is retained to represent the shared secure outcome without silently
selecting among those historical premises. Its restricted domain and
provisional status, rather than only believe's correct output, justify
the current executable choice.

## Propagation (only after verdict)

The registry points to this follow-up and retains the original closure
as linked evidence. Update the SC035 human note, grouped dossier and
reader; correct only the stale FST composition comment. Literal rules,
order, corpus, contexts and baseline receipts remain unchanged.
Regression tests cover the complete comparison, the source-backed
cluster success/failure, genuine PD witnesses, root-stress representation,
early-gi input versus inferred raising, and old-closure integrity.

Believe has no current elaborated lexical entry or assembled entry block.
Its only row-local prose is an archived DEV_NOTES slice that preserves
older incompatible model statements. That archive is not rewritten or
promoted to current authority; the current scientific discussion and
full derivation are in this follow-up and the reader. No lexical entry
is added.

Expected baseline effect: none. All selected identities, inputs, outputs,
389/381/eight totals, 167 lexical blocks, classes and editorial order
remain protected. No baseline migration/refreeze is requested.

## Residue

The sources explicitly leave the early *gi-* pathway open. A staged
experiment must distinguish supplying an attested early weak vowel from
deriving it by a hypothetical regular raising operation.
Decisive further evidence would establish regular pretonic raising and
its domain independently of the ga-/bi- comparison, or positively
discriminate its timing relative to diphthongization and later merger.
No author decision is needed to retain this explicitly provisional
compression. The comparison does not authorize SC036 work.

## Validation and publication closeout (2026-10-23)

- Supported `SC035 --finalize` completed the full control-plane refresh and
  propagation checks. The only executable-source edit is the composition
  comment: the entire comment-stripped Foma source equals the accepted
  `5533f765` source. Its new source hash is honestly propagated through the
  build manifest and trace provenance; the frozen comparison retains the
  hash of the actual source used for that experiment.
- Targeted non-runtime SC035 regressions: 14 passed, two runtime tests
  deferred to the comprehensive run, nine subtests passed.
- Comprehensive strict Python suite, including the original SC035 assay,
  fresh three-model Docker/Foma replay, full corpus regressions and
  holding/provenance checks: 1497 passed, 9026 subtests passed, 39m16s.
  The fresh comparison reproduces every recorded scientific result and
  intermediate difference, while separately validating the current
  executable-source hash.
- Full artifact-graph checks passed before and after publication.
  `INDEX_VERBORUM_STRICT=1` combined-book build passed: zero gloss
  violations, zero unresolved references, clean index-policy/readiness
  checks and all 18 negative index fixtures.
- The combined book has 323 pages. Actual SC035 PDF pages 83–84 (printed
  81–82) were extracted and visually inspected: rule notation, breve,
  citations, stressed-root controls, successful staged alternatives,
  predicted incorrect clustered-prefix form and SC043/SC073 references
  render consistently. The standalone reader was rebuilt as well.
- All selected inputs, contexts, stage metadata, full scientific
  derivation traces and match buckets equal the accepted base:
  389 selected, 381 matches, the same eight mismatches. All protected
  baseline/migration receipts, the original SC035 memo, original assay
  and chronology card remain byte-identical.
- The 167-entry lexical Markdown, class manifest and editorial sequence
  are byte-identical. Every page of the rebuilt 158-page lexical PDF
  and four-page introduction has identical extracted text and rendered
  pixels to the accepted versions; only the resulting metadata-only
  PDF noise was restored. No selected lexical derivation changed.
- Only SC035's registry row changed, and the SC036/SC037 reader tail is
  byte-identical. Both pre-existing untracked scratch files remain
  untouched. No scientific baseline was refrozen and no later
  adjudication was begun.
