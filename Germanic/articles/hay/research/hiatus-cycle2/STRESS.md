# Cycle 2: experimental stress substrate

## Identity and scope

Stress checkpoint S1 (reproduction only); SC083 `OEUnstressedEIContraction`,
also involving the representation at SC043 and SC085. Branch
`research/hay-article`; intake `f220d31157eaa10fcb9a3785ac349bdfac8d6c22`.
The 18 commits since `0982628b83183afde27bb36af1912987c208f13d` remain in
order. Three unrelated untracked paths were present at intake and are out
of scope. All executable evidence below uses the frozen research model
at `113101ac5f169b589e1a9647cdf24d32cdd4d919`, not live production.

## Question and current state

**Hypothesis:** the A and B2 prefixed forms of ‘call’ lose a genuinely
stressed root vowel after its accent is no longer represented. This would
be refuted if the accent persisted to deletion, if deletion did not account
for the missing vowel, or if the input positively encoded unstressed *e*.
The exact counterfactual skips only the existing deletion: it must leave
unresolved hiatus, not yield a contracted long vowel.

The frozen registry treats SC043 as ordinary English stressed *a*-fronting
and SC083 as an unadjudicated OE contraction. The latter follows
`OEIntervocalicJVocalization` and precedes `OEWeightCleanup` and `OEHLoss` in
the compiled order. Its only target is plain `*e`, after a vocalic segment
plus consonant(s) and immediately before `*i`. This positional context is
not a test for posttonic position or for an unstressed vowel. The submitted
forms are the same 3sg present and past participle as in the previous
[inventory](../hiatus/historical.tsv); the past submission is inadmissible
and is not evidence about the deletion.

## Executable diagnosis

The table gives the A/B2 present; the participle has `*d` in place of
`*θ`. These strings are serialized FST tokens, not phonetic transcriptions.
The full changed-stage traces, unchanged anchors and contrasts are in
[`stress-reproduction.json`](stress-reproduction.json).

| Component | State entering | State leaving |
|---|---|---|
| `SC047ProtoInput` (A/B2 admission wrapper) | `gakáwiθi` | `*g*a*k*á*w*i*θ*i` |
| `OEStressFootContext` | `*g*a*k*á*w*i*θ` | `*ᶠ*g*a*k*á*w*i*θ` |
| `EAFBrightening` | `*ᶠ*g*æ*k*á*w*i*θ` | `*ᶠ*g*æ*k*æ*w*i*θ` |
| `OEIUmlaut` | `*ᶠ*ʝ*i*k*æ*w*i*θ` | `*ᶠ*ʝ*i*k*e*w*i*θ` |
| `OEWLossBeforeI` | `*ᶠ*ʝ*i*k*e*w*i*θ` | `*ᶠ*ʝ*i*k*e*i*θ` |
| `OEUnstressedEIContraction` | `*ᶠ*ʝ*e*k*e*i*θ` | `*ᶠ*ʝ*e*k*i*θ` |
| `OEHLoss` | `*ᶠ*ʝ*e*k*i*θ` | `*ʝ*e*k*i*θ` |

`EAFBrightening` is the first loss of **nucleus-local** accent on this path,
not the first loss of **all** prosodic information: `*ᶠ` remains until
`OEHLoss`. Umlaut does not reconstitute the accent, and SC083 fails to
consult the surviving pretonic annotation. This is a distinction between
normalizing a spelling of stress and losing or failing to read the
information needed to apply a historical rule. Nothing here demonstrates
any historical movement or loss of stress.

H0 gives `ġeciþ/ġecid`; bypassing only SC083 gives `ġeceiþ/ġeceid`.
Canonical `ġecēaiþ/ġecēaid` is unchanged by that bypass: its earlier
long-diphthong route is already outside the SC083 target. The two A/B2
‘call’ traces are out-of-domain firings for a historical **unstressed**
reduction. Canonical and the unprefixed local probe are negative controls
for different reasons: lack of the target and lack of an earlier nucleus.
The explicit-acute root is protected by symbol identity; a genuinely
posttonic plain sequence after a marked head still reduces. A synthetic
marked prefix likewise does not protect a following weak vowel. The
pretonic weak sequence at the left edge does not reduce under the current
rule. These are local contrasts, not a census of the rules or evidence
for the historical weakness of any unattested input.

## Literature and historical interpretation

[Regular survival](../REGULAR_SURVIVAL.md) and the
[Dahl–Jones dossier](../hiatus/DAHL_JONES.md) record the source
collation. Ringe and Taylor (2014: 260, 318) and Campbell (1959:
§237.1b) make the ‘call’ forms short-root post-*w*-loss comparisons.
Sweet (1885: 416) supplies the Mercian participial spelling. Their
phonological reconstruction, not the experimental spelling, supports
a stressed root and subsequent resolution. Ringe and Taylor (2014:
156–157), cited with the frozen contraction definition, discuss the
weak *-ej-* sequence; that is not evidence for reducing a stressed
root. Campbell (1959: 31 §74 and n. 5), checked in the
[SC035 adjudication](../../../../docs/sound_changes/audits/sc035-adjudication.md),
provides an independent contrast between ordinary weak *ge-* and
exceptionally stressed *ġeatwe*. The distinction is prosodic, not
conditioned by verb or prefix identity.

**Historical stage and scope:** the preceding distinctions concern the
pre-OE input to fronting and early OE phonology. The comparative Anglian
evidence for ‘call’ does not make the executable order a historical stage
assignment. **Analogy:** no positive evidence for analogy follows from this
failure. **Chronology:** the trace establishes a model-local feeding
relation (loss of accent and *w* makes SC083 possible); it does not rank
early versus late historical contraction. Bypassing the deletion is a
diagnostic, not a repair: it would also suppress the weak reduction.

## Verdict and propagation

**DEFER** production adjudication. This checkpoint diagnoses an encoding
and rule-context interaction, not a new phonological law. There is no
registry verdict, scoped historical change, production propagation,
benchmark change or fingerprint reset. The dedicated research regression
replays the original three cells against all three frozen models and
checks the counterfactual and six paired synthetic inputs.

```bash
cache=$(docker compose exec -T backend mktemp -d /tmp/capr-hay-stress.XXXXXXXX)
bash Germanic/articles/hay/research/hiatus/run-container.sh local --stage-cache "$cache"
bash Germanic/articles/hay/research/hiatus-cycle2/run-container.sh --stage-cache "$cache"
```

The runner checks source and physical order against the Cycle 1 receipt,
compares the full changed-stage records and outputs, and checks the exact
local differences. It builds only in container-private storage and can
reuse a verified frozen stage cache. The warm-up reproduced the previous
60 local traces byte for byte (SHA-256
`7b1d62d3e04fc6d2eb0a58173cc9271be7302e2ce8b765c5d5d5903ca5ab352e`).
The focused regression reused that cache without additional compilation;
it has no default-suite or shared-runtime cost.

## Residue

The complete stress architecture, actual firing population, independent
lexical controls and two repairs are separate checkpoints. `*ᶠ` tracks
pretonic structure, not an arbitrary stressed nucleus, and disappears in
`OEHLoss` independently of whether that rule deletes a consonant. `*ᵘ`
and `*ᶜ` are routing symbols, not accent annotations. The prior
`HiHeadContext` is positional; the joint assay's atomic `*ei` is not
accent-contrasted. Neither establishes a durable stress representation.
An independent panel must separate prefix stress, secondary stress,
quantity, syllabic *i*, a complex nucleus, and the two palatal types.

## S2 checkpoint: independent panel and two repairs

[The panel](stress-panel.tsv) keeps its five full submissions separate
from fourteen synthetic entries. The frozen captures independently
give `ġelīefan` for ‘believe’ (1944), with a pretonic syllable,
root *áu* and a long weak tail; and `weorold` for ‘world’ (2302), with
explicit primary and secondary accent. The latter is a reconstruction
of a compound formation, not independent evidence for every detail of
its compaction or accent history. Campbell §237.1b supports the
unprefixed verbal comparison. There is no full submission for the
exceptionally stressed ‘armour’: its stress is independently motivated
but the local contrast does not assert a reconstructed earlier input.

| Component | Frozen function and limits |
|---|---|
| `EnglishProtoInput` / `SC047ProtoInput` | Parse and star tokens; native input accepts acute/grave distinctions. A/B2 also have the documented additional cell branch. Admission is not evidence that stress is specified on every submitted input. |
| `OEStressFootContext`, `FootCtx` | The first inserts `*ᶠ` before one initial pretonic syllable recognized from a following positively marked head; the second can pass that syllable outside an inner rule's domain. Neither marker identifies all heads or all compounds. |
| `*ᵘ`, `*ᶜ` | The input interface routes weak final and weak nonfinal sentence contexts, respectively. These are word-level context tags, not lexical stress on a particular syllable and not compound boundaries. |
| `EAFBrighteningUnstressed`, `EAFBrightening` | Separate plain and accented source clauses. The latter maps primary acute *á* to plain *æ* but retains a separate reflex *ǽ* for its grave input. |
| `OEStripSecondaryStress`, `OEInterStressRaising` | The former normalizes grave *ò*; the latter includes a weak between-stresses configuration and consumes a grave low/front input on the ‘world’ path. The earlier label is not a universal date at which all secondary accent disappeared. |
| `OEIUmlaut`, `OEHighStressDecode` | Fronting/raising can neutralize accent with plain outputs; the latter separately maps residual grave high vowels to plain high vowels. These executable decodings are not claims of historical accent displacement. |
| Weight, syncope and `OEHLoss` | The cascade reads nucleus, consonants and foot domain to resolve weight. `OEWeightMarkers` and `OEWeightCleanup` do not supply a persistent primary-head slot. `OEHLoss` strips the foot marker even when its consonant target is absent; the subsequent physical context alone cannot reliably recover the old head. |

**Repair S1, foot-domain guard.** Replace only SC083 with
`FootCtx(OEUnstressedEIContraction)`. On a marked word the pretonic
nucleus cannot license deletion of the first following root nucleus;
a root nucleus can still license the same rule later in the foot.
This is not a filter on `ge-` or on a verb class. It changes no
weight or vowel rules. The two A/B2 ‘call’ cells and the plain-root
local contrast are its only SC083 changes on this panel. Each model
retains the three posttonic local firings (after an ordinary head,
after a stressed prefix, and later in a marked word), and does not
add a pretonic reduction. Unprefixed ‘call’ and both corpus controls
retain their H0 endpoints. In A/B2 the simplex has **earlier** palatal
diphthongization (`ċieiþ`): it is not another instance of SC083.

**Repair S2, explicit tier.** Seed private `*⌃` / `*⌄` tags from
explicit primary and secondary accent immediately after admission,
not from first-syllable position or `*ᶠ`. In synthetic local entries
with otherwise unmarked heads the independently specified probe
tags supply the intended contrast. Change SC083 only insofar as
an immediately preceding tag prevents its ordinary left-context
match (a following tagged nucleus also cannot serve as weak *i*).
For other components, frozen identity lookups retain the exact
annotation; changed lookups thread the markers through the frozen
transduction using Foma ignore insertion. Project intermediate
results back onto the ordinary representation and record the
disagreement or ambiguous attachment rather than choosing an
alignment. This leaves the underlying weight and syllabicity rules
unchanged and allows a stressed `*ei` without recoding it as
syllabic `*e*i` or as consonantal `*e*j`. The five local
head contrasts verify quantity, nucleus, and palatal type separately.

The explicit tier is **not** a general solution. It retains the head
through brightening, umlaut, w-loss and foot-marker stripping in
‘call’ and the vowel changes in ‘believe’. In all three cascades it
fails at `OEMedUnstressedULowering` in ‘world’: the network returns
tags inside the serialized segment tokens, so the valid annotation
set is empty although the untagged result exists. Treat this as a
technical failure of the lift, not a prediction about compounds.
The existing atomic `*ei` alone has no explicit head contrast;
the tag demonstrates how to distinguish that property, but says
nothing about its historical weight or whether all subsequent
rules recognize the atomic nucleus.

### Keeping hiatus resolution separate

The [receipt](stress-repairs.json.gz) has all three no-overlay arms
and twelve H arms per frozen model (three operations × two positions
× two repairs). The early insertions follow `OEWLossBeforeI`.
S1 late uses the still-present foot marker immediately before
`OEHLoss`, already after SC083. S2 late uses the explicit tier
after `OEHLoss`, immediately before `OEContraction`.
These anchors are intentionally not treated as identical when the
intervening h-loss itself matters. All H rules are local stress
diagnostics, not independently established claims of unrestricted
resolution.

Both no-overlay repairs retain short *e.i* in the affected ‘call’
forms. In A and B2 both early and late direct contraction now give
`ġecēþ/ġecēd`. Late consonantal gliding instead supplies *j*
(`ġeceġþ/ġeceġd`); late nuclear incorporation supplies atomic *ei*,
rendered with `ei` by the experimental printer. The spelling of the
nuclear outcome is identical to that of unresolved hiatus, not proof
that the two phonologies are equivalent. Neither repair changes
canonical ‘call’ to the short input; its long nucleus is upstream.

**Interim verdict:** S1 is the sounder minimal candidate for wider
auditing; S2 is useful for targeted post-foot and nuclear diagnostics
where its alignment is valid, not for unqualified full-model use.
Late direct contraction is no longer computationally excluded on
these prefixed paths. This removes a stress-induced argument for
early contraction, not evidence concerning independent ordering
relative to umlaut, apocope, lowering or palatal developments.

```bash
bash Germanic/articles/hay/research/hiatus-cycle2/run-container.sh --repairs --stage-cache "$cache"
gzip -t Germanic/articles/hay/research/hiatus-cycle2/stress-repairs.json.gz
```

The live private panel verifies the two protected ‘call’ cells,
the independent weak reduction, and the early/late direct predictions.
It reuses the frozen definition image and adds only isolated component
compilation. The full archived/active firing census remains S3.

## S3 checkpoint: archived and active census

The [census](stress-census.json) replays each model on 394 archived
and 396 active inputs (2,370 model–input records), matching input
and endpoint to the joint audit before substituting the S1 network
at SC083. Canonical at the 396 active inputs is the comparison on
the A active input set, not a separately certified canonical capture.
The [baseline source](../hiatus/joint-corpus.json), frozen commit,
and component order are unchanged.

The full firing population is the same in S0 and S1 in all three
models and both panels: **bore** 1956, **handle** 2055, **learn**
2095, **lick** 2099, **make** 2117, **show** 2186, **spare**
2205, and **sunder** 2232. Each deletes plain posttonic *e*
from weak *e.i* before the remaining *-an*. These are in-domain
weak-sequence firings, not evidence that the cascade's physical
position corresponds to a uniquely established historical date.
The output of the substituted component is identical on every
input, and therefore there are no downstream derivation changes.
The stress failure is real in the independently supplied prefixed
‘call’ forms; it is not demonstrated in another selected corpus
row by this census. The S2 compound failure belongs to the new
marker lift and is not an existing frozen-cascade discrepancy.

**Preferred experimental substrate:** S1 for stress-only full
replay. The result supports a bounded implementation audit of
SC083 separately from any proposal for a new hiatus rule. Corpus
parity does not establish that one pretonic syllable suffices as
a full prosodic representation. Post-foot experiments should use
independently anchored local entries, or explicitly validate
attachment of the S2 tier before making claims that depend on
it. No production action, chronological registration, or scientific
recertification follows.

```bash
bash Germanic/articles/hay/research/hiatus-cycle2/run-container.sh --census --stage-cache "$cache"
```

This opt-in experiment reuses the already validated frozen common
image, compiles one additional component, and batches the S1
comparison on the original SC083 inputs. A full repaired derivation
is needed only where the component diverges.
