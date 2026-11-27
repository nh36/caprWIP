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
