# SC047 parallel models: verification and historical review

## Identity, question and current state

SC047 (`OEHeavySyllableNasalApocope`), compared with SC041 and SC010.
Review base: `b649dcea5e139dadcf9c016d55cf32a262b0c127`.
Executable source: `60d6e3f0f3631fbdb63588830650b57a413af1e3`.
Can the three experimental placements reproduce both archived outcomes
and the particular contrast predicted by the published chronologies,
without unequal treatment of either arm? This is a review of the
[research configuration](README.md), not a new production adjudication.
The canonical registry, 158-application census, order and selected
cells remain as previously adjudicated.

## Diagnosis

Both models read the same corpus/context metadata and same reconstructed
cells, with the same input acceptor, scoring and normalization. The full
orders are identical except for the permutation of the three operations
immediately after `FON`. On the shared path both move SC017 before
apocope so the vowel triggers are still available (all 40 archived
firing identities agree). SC112 follows SC017, sees `*dórą` unlengthened,
and still lengthens the stems of *þǣr* and *hwǣr* (two archived
firings). SC020 exposes short oral `*a` for SC041; `FON` immediately
vocalizes stranded consonant-following `*ij/j/w` in both arms. A then
runs SC047 → `FNU` → SC010, B runs SC010 → SC047 → `FNU`. `FON` and
`FNU` implement the same vocalization; SC010 itself is the same rule.
SC111's shared proxy `FW` retains its original `*awą → *au` branch
and adds final `*aw → *au` now that SC047 removes the nasal vowel
upstream. The shared labial consumers and the remaining cascade are
unchanged across A/B. The separate forced preservation of `*wwj` and
other labial/hiatus options are not parts of the principal comparison.
SC017, SC112 and SC111 here specify executable feeding or recovery,
not independently dated historical edges. See the
[archived census and causal traces](../source_integration/README.md).

Each order has 115 stages. SHA-256 of the ordered Foma identifiers
joined by LF and ending in LF:

| Configuration | Order SHA-256 |
|---|---|
| SC047-A-early-v1 | `79d6ff53edf23084db644af524638cb9195ab5b73b51ad53b97cec95bba2814a` |
| SC047-B-split-v1 | `0ee86357bed4b30207fbe04b07258689dd69159613d1219aa6733a5030e87579` |

All ten pinned file digests in `observations.json.gz` agree with the
review checkout, including the FST, rule plan, corpus, context
metadata, runner and the five helpers.

A fresh backend replay, using the pinned runner command in the model
README, reproduced the raw JSON byte-for-byte (SHA-256
`bffedc5f370422522927578171fc6db9e3b8e89b796875bec2299a3e2f2dab8e`),
including all 14,539 probe/control states at 217 checkpoints.
Both TSV exports reproduced byte-for-byte. Eight focused SC047 tests
passed; read-only production status reported all artifact nodes fresh
and the 394/386 baseline unchanged. This is not a new strict certificate.

| ID | Canonical | A | B | Earliest effective cause |
|---|---|---|---|---|
| 2061 hay | *hīeġ* | *hēa* | *hewe* | With nasal loss first, the block supplies singleton `*xáwi`; with doubling first it supplies `*xáwwi`. A's later singleton diphthong proxy contributes to *hēa*. In B, immediate vocalization bleeds the later doubled labial consumer. The chronology changes the input to those processes, but neither base endpoint tests the chronology alone. |
| 2069 hedge | *heġġ* | *heġe* | *heġe* | Early shared SC020/SC041/FON bleeds gemination on the selected oral ending; not a nasal discriminator. Scored ‘hedge’ is not independently a parsed masculine nominative like the proposed *seċġ* example. |
| 2138 net | *nett* | *nete* | *nett* | At the first operation after `FON`, A drops `*ą` and B doubles `*t`; following vocalization removes the trigger in A. The doubled protected cells converge. A needs a later historical explanation for *nett*, not an FST rescue rule. |
| 2152 rest | *ræste* | *rast* | *rast* | Shared early SC020 exposes `*rástō` before final long-*ō* raising (SC019); the following `*z` still protects the vowel at that checkpoint in production. Not an effect of the disputed edge. |
| 2332 hue | *hīew* | *hii* | *hiewe* | Singleton `*xíwi` loses `*w` before *i* and leaves hiatus; in B `*xíwwi` lacks the `*j` required by the later cluster treatment. The surviving protected stems and the independent sensitivity runs do not determine a direction of historical transfer. |

All other selected outputs are identical across all three lanes.
Canonical ↔ A: five deltas; canonical ↔ B: four; A ↔ B: three
(*net*, *hay*, *hue*). The 394 endpoint rows in each lane match both
archives exactly. At matching checkpoints, 4,896 source-integration
and 42 morphology probe/control observations agree, matching scored
controls by row ID and unscored inputs by their encoded form. These are
the intersecting observations, not full intermediate coverage of all
394 rows. The eight inherited target → output mismatches are *bucc* →
*bocc*, *fȳre* → *fȳr*, *fugol* → *fogol*, *rust* → *rost*,
*strēaw* → *strēa*, *tæppa* → *tappa*, *wulf* → *wolf*, and
*wull* → *woll*. Both arms preserve them. Deer remains row 1988
`*déuzô → dēora`; direct `*déuzą → dēo` in A/B is unscored.

### Probe and exclusion register

The [matched-cell table](matched-cells.tsv) supplies the unique IDs,
input forms, matched checkpoints and endpoints. The following partitions
all 52 unscored rows by purpose (15 additional scored traces are not
counted). Some cells within a group serve different roles: a credible
input is not equivalent to an independently attested inherited outcome.

| Rows | Included groups | Interpretation and provenance |
|---:|---|---|
| 14 | `nett.*` (5), `bedd.*`, `wedd.*`, `cynn.*` (3 each) | Four comparative light neuter stems, using dental stops and *n*; nasal direct differs, protected genitive/dative and net plural controls converge. Paris Psalter, poetic loci, and biblical cases in the [English register](../morphology/english-cells.md); *nettes* is predicted, not attested. *Cynn* also tests final nasal simplification (B surface *cyn*). |
| 7 | `secg.*` (4), `hyll.*` (3) | Distinguish the proposed nasal accusative and common oral nominative; protected donors converge. The velar and lateral show that the effect is not peculiar to dental stops. The starting case oppositions and *hyle* are reconstructed, not direct witnesses; see Dahl pp. 81–86, Hogg pp. 68–73, Hogg–Fulk §2.23. |
| 3 | `hyse.proposed_ja.*` | Conditional ja analysis of an *s*-final root (Dahl pp. 81–86); one admitted accusative contrasts *hyse/hyss*. Nominative and dative rejected by both arms, as explained below; none establishes the inherited class. |
| 7 | `mete.*` (2), `mene.proposed_neuter.*` (3), `dili.proposed_i.*` (1), `ende.nom.sg` (1) | i-stem controls (*mete*, proposed i-stem *dile*); `mátis` is a reconstructed genitive probe, not the Vespasian plural. *Mene* is conditional on disputed neuter inheritance; its protected probes are structural. *Ende* is Hogg–Fulk's heavy oral control with long nuclearized `*ī`. |
| 3 | `dili.proposed_ja.*` | Hypothetical masculine ja paradigm: both produce *dile* in the oral nom.; A *dile* vs B *dill* in the nasal acc.; both *dille* in the protected dat. Grounded as a comparative counterfactual, not a documented doubled English donor. See the [bounded inquiry](README.md#residue-and-bounded-source-follow-up). |
| 15 | `hay.*`, `hue.*`, `searu.*` (3 each), `rice.*`, `deer.*`, `strew.*` (2 each) | Labial and high-vowel mechanisms, heavy *ij*, inherited *w*, final consonant/rhotacism, and competing strew root analyses. These distinguish mechanisms or establish convergence, not 15 independent witnesses. The protected forms are reconstructed inputs; possible donor shapes and actually attested cases are distinguished in the [source ledger](../sources.md) and [comparative register](README.md#historical-analysis-forms-versus-interpretation). |
| 3 | `here.nom.sg`, `yellow.nom.sg`, `yellow.gen.sg` | Shared input-gate rejects. Intended as *r* exemption and protected *lw* controls, not positive evidence of either rule or a scored regression. |

All five rejects are empty already at `EnglishProtoInput`; 47 forms
reach one endpoint in each arm. The two *hyse* spellings use ordinary
CAPR symbols; the problem is segmentation. The native grammar has no
simple `sj` coda cluster to combine with a vowel-first `az` or `ai`
tail, and no productive `jaz` or `jai` tail to combine with a root
ending in `s`. The fallback starts from the same coda inventory and
expects vowel-first extensions as well. By contrast, explicitly
listed `ją` licenses the nasal input as an `s`-final root plus that
tail. This is a restricted serialization grammar, not a finding
against the historical cluster. Dahl's `*husjaz` is reasonable as a
conditional hypothesis, but the English stem assignment is not
independently secured and there is no decisive comparison that would
follow from admitting it. No gate or fixture bypass is introduced:
these runs do not compute the paired oral nominative or protected
dative of this proposed paradigm. A future, provenance-backed
research-only component assay could feed explicitly encoded strings
after the acceptor if a specific historical claim warrants it.

The TSV's “first unequal block step” is a comparison by execution
position, not by rule name. The entire prefix through `FON` is
identical. For nasal light stems the first difference is different
phonological action on the same input (deletion against doubling).
For protected stems the temporarily different checkpoint just records
B doubling sooner; the block then converges. For *rīċe*, deer and the
door control the first difference is temporary survival of a vowel,
not an effect of gemination. For shared oral cases such as ‘hedge’ the
causal fork is relative to **production**, not between A and B.

## Literature and historical judgment

Ringe–Taylor pp. 44–47 and Campbell §576 (pp. 229–230) gain a
single early low-vowel schedule; the earliest Continental *peti/bedi*
gloss types support it **if** the written singleton is inherited.
Two manuscripts strengthen one lexical example, not two paradigm
histories. Dahl pp. 81–86, Hogg pp. 68–73 and Hogg–Fulk §2.23 make
regular direct *nett/bedd/wedd* economical in English. Dahl's
*hyss* and Hogg's *hyle* are predicted stages. Continental split
loss would need another development, or the English split could
be regional. Boutkan pp. 209–213, 435–436 supply one alternative
mechanism, not independent confirmation of it. The current evidence
does not distinguish common early timing from Continental timing
or exclude a secondary singleton.

The protected doubles are both regularly derivable and actually
attested in several paradigms. That establishes donor availability.
The Vespasian *mete : mettas* evidence and *Maldon* transmission
independently support restructuring, not the ancestral class or
direction of every case replacement. Adamczyk's 86% plural vs 4%
singular (2018: 150) concerns eligible light i-stem observations
only: a doubled plural can coexist with a singleton singular. A
productive neuter levelling pattern would not amount to four
unrelated lexical exceptions, but an early transfer before high-vowel
loss and a later bare-stem transfer are different hypotheses.
B's hypothetical masculine accusative could supply an entire direct
form, but its proposed priority cannot be inferred from syncretism.
Neither analogy nor an added Continental change is free explanatory
currency. The one-match difference has no evidential weight.

## Book review

The chapter correctly separates reconstructed endings, recorded
spellings, phonological prediction and morphological interpretation.
The revisions specify Boutkan's southern mechanism and its independent
burden of proof, identify *hyle* and *hyss* as reconstructions, and
remove any suggestion that B's predicted accusative supplies independent
support for B. The appendix now states the actual coverage of the
traces and rejects, and typesets paired reconstructions independently.
Its inventory and full checkpoint data are in the research supplement,
not in the PDF. The reader proposals separately qualify SC010's
inheritance premise, describe SC041's oral environment, and specify
SC047's weight-independent executable environment and late position.
They have not been applied to the reader.

Removing the two preview insertions recovers the canonical assembled
Markdown byte-for-byte. The rendered copy was inspected at the chapter
and appendix, with a single bibliography, a valid chapter-to-appendix
link, and the existing index (2,057 entries accepted). For the local
367-page research PDF, the chapter and appendix start on printed
pp. 138 and 346 (PDF pages 140 and 348). Its build command is
`SC047_PREVIEW_MONOFONT='Courier New' bash Germanic/docs/assembly/sc047_preview/render.sh`.
The local PDF at `.capr-work/sc047-parallel/book/preview.pdf` is
1,620,274 bytes, SHA-256
`6b9838207486e79f004dceec362d4e7b1bc669150e7eaa6ffae8bcfa7a68fd6c`.
It is not a canonical publication artifact.

## Verdict, propagation and stopping rule

Retain the existing executable serialization and defer the
historical nasal loss–gemination edge. `Registry-verdict: SC047=REFORMULATE/RETAIN`.
No registry, corpus, FST, published reader, canonical book or strict
certificate changes. The preview chapter is separate from the
proposed replacement text for the three reader entries.

The model contrast, the actual observed donors, and the cause of the
five selected deltas are sufficiently understood. Another run of
the same orderings or a higher-scoring hybrid cannot determine
inheritance, direction of levelling or geographical scope. The
priority is Dal's original when obtained, or a manuscript-level
singleton *weti* with independently established dialect, case,
and history of final *i*. *Dili/dile* needs a new primary witness
or a new class-specific argument; there is no basis for repeating
the earlier searches. A securely parsed nonlabial direct/oblique
pair or an independent test of the labial mechanism would make
another experiment informative.
