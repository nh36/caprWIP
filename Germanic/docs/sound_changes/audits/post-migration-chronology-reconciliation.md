# Post-migration chronology reconciliation

## Identity

- SC016 `OEWsPalatalGlide`, SC017 `PNWGmcULowering`, SC040
  `OEMedUnstressedULowering`, SC072 `OEUnstressedLongVowelShortening`.
- Linked consistency findings: SC039's former reciprocal displacement and
  the accepted SC026/027 component-dependency classification.
- Branch `update`; base `2fc696ec55aa2b1eae80aaabf0ed9bcd726921d9`.
- Scope: propagate already accepted decisions and classify obsolete
  experiments. No ordinary SC040/SC072 adjudication, rule movement or
  new sound law is authorized or performed.

## Question

Do the reciprocal SC016-before-SC017 measurements and the youth-based
SC040-before-SC072 measurement establish current historical constraints,
or do they depend on the superseded early glide-insertion architecture?
An unchanged failure under the adopted late spelling would refute the
architecture-dependent explanation. Recovery of youth with delayed lowering
after changing only that spelling architecture confirms it.

## Current state (before edits)

The SOURCE edge registry calls all three measurements independently
demonstrated historical chronology. The accepted SC016/017 adjudication
instead adopts late written-surface SC016, after SC017. The SC021
adjudication, section 9a, explicitly adopts late SC040 after the earlier
unstressed-shortening and vowel-resolution history.

Both current SC040 and its original experimental formulation lower medial
short u after a non-u vowel and consonants, excluding a following m.
The current selected inputs are *júką (yoke), *júgunθ (youth),
*wíduwōn (widow) and *wír-àldu (world); no input is changed.
Preparation followed `adjudicate.py SCNNN --prepare` for SC016/017/040/072;
SC016/017 and SC021 accepted memos, old cards, pilot summaries and the
current registry sources were consulted.

## Diagnosis

Fresh canonical `--evidence` rebuilding gives the complete 389-row census:

- SC016 changes yoke and youth only: ġ*ó*k → ġ*éo*k and
  ġ*ú*g*uþ → ġ*éo*g*uþ.
- SC040 changes hawk, head, heaven, milk, navel, nine, rainbow, seven,
  soul, ten and world (11 rows), each a medial-u application in the
  adopted model. Youth *j*ú*g*u*θ and widow *w*ú*d*u*w*e are unchanged.
  World changes *w*éo*r*u*l*d → *w*éo*r*o*l*d.

`test_chronology_consistency.py` reproduces the actual pilot-era source
from commit `515b0f4b`, whose recorded summary includes both disputed
experiments. It uses the shared composition parser and variant appendix,
not a separate cascade-order parser. All writes and Foma compilation occur
in disposable container-local directories.

| Assay | Yoke | Youth | Meaning |
| --- | --- | --- | --- |
| Original identity | ġeoc | ġeoguþ | Old experimental control |
| Original SC016 moved after SC017 | ġoc | ġeoguþ | Old u-only insertion cannot act on lowered o |
| Original SC040 moved after SC072 | ġeoc | ġeogoþ | Reproduces the archived youth failure |
| Same delayed SC040, adopted late back-vowel spelling instead of early insertion | ġeoc | ġeoguþ | The old youth failure depends on the retired glide architecture |
| Current identity | ġeoc | ġeoguþ | Accepted model |
| Current SC040 moved immediately before SC072 | ġeoc | ġeoguþ | Youth does not discriminate this pair's order now |
| Current SC016 omitted | ġoc | ġuguþ | Written-surface positive controls, not a dating experiment |

All paired replay assertions passed in a single targeted invocation
(12 tests, 290.64 seconds), including the following additional controls.

The old insertion changes the first nucleus to a front-vowel-plus-u
sequence before lowering. Once SC072 supplies medial short u, delayed
SC040 can lower it after that altered nucleus. Without the early
insertion, accented root u remains and blocks medial lowering. Thus this
is an architecture-dependent displacement result, not independent
historical SC040-before-SC072 evidence.

Widow and world remain positive/negative controls under the two current
SC040/SC072 serializations. Delaying current SC039 until after late SC040
gives *wudowe* for widow and retains *weorold* for world. Advancing SC040
before SC039 instead preserves *wuduwe* and gives *weorald*: the accepted
SC099/100 resolution intervenes after early lowering. Thus the current
SC039-before-SC040 dependency survives, but the original reciprocal
early-SC040 measurement does not. It is separately classified as superseded,
not treated as a current widow result. No executable change follows.

## Literature

Existing accepted accounts checked:
`sc016-017-adjudication.md`, `sc017-sc019-adoption.md`,
`sc021-adjudication.md` section 9a and the SC039–041 book dossier.

- Ringe and Taylor 2014 p. 5 distinguishes written *eo* in *geoc* from
  spoken /jok/. Fulk 2018 p. 56 §4.3 and Campbell 1959 p. 43 §115
  support lowering in yoke. Brunner 1965 pp. 64–65 §92.1 and Bülbring
  1902 p. 120 §§298–299 supply the back-vowel spelling distribution,
  including retained-u youth. These are the accepted SC016/017 sources,
  not new historical conclusions.
- Campbell 1959 pp. 155–156 §373 supplies later unstressed u-to-o lowering
  and preservation after accented u.
- Stausland Johnsen 2015 pp. 21–22 explicitly distinguishes the earliest
  eighth-century unstressed u/a system from ninth-/early-tenth-century
  u/o writing. Pages 28–31, especially chronology (8) pp. 29–30, place
  unstressed long-vowel shortening after loss of short unstressed vowels.
  The held text was rechecked. This is the source-backed chronology
  already adopted in the SC021 repair, not a stage inferred from `OE`
  identifiers or a shared coarse `oe` label.

Current spelling and the chosen computational serialization are CAPR
modelling decisions. Neither correct final outputs nor a changed
counterfactual result independently proves historical chronology.

## Historical analysis

- Stage/scope remain exactly as registered. SC016 is West Saxon orthographic
  rendering; SC017 is the accepted Northwest Germanic phonological lowering.
  SC040/072 retain their existing OE historical metadata.
- The source-backed earlier-shortening/later-lowering distinction governs
  SC072 versus SC040. It does not rest on the two rules' identical coarse
  stage code, nor on a fabricated current lexical feeding witness.
- Positive phonological/prosodic conditioning and selected inputs are
  unchanged. Youth is negative evidence for current SC040 application,
  not a discriminating historical precedence witness.
- No analogy is proposed. No wider law or new counterexample programme
  is adjudicated here.
- SC017 before SC016 is `stage_entailed`, with visible yoke feeding but no
  final-output discriminator because modern spelling covers both o and u.
  SC072 before SC040 is `stage_entailed` in the accepted narrower source-dated
  intervals, with no asserted live lexical feeding.
- The three initially disputed measurements and the additional obsolete
  reciprocal widow measurement remain in SOURCE as
  `superseded_experiment` / `archived_experiment`, and every frozen card,
  summary and original receipt is retained unchanged.
- The accepted SC026/027 adjudication explicitly treats lengthening and
  deletion as components of one historical process. Their reciprocal
  executable dependency is now `technical_computational` / `technical`,
  not independently demonstrated successive historical chronology. The
  separately published identities and canonical shared historical identity
  remain unchanged.

## Verdict

REFORMULATE live chronology classification and current explanations;
RETAIN every executable definition, order and selected lexical datum.

Registry verdicts remain SC016=REFORMULATE/REORDER and
SC017=REFORMULATE/RETAIN. SC040 and SC072 remain unadjudicated:
this scoped reconciliation does not replace either ordinary adjudication
or add a misleading per-SC `Registry-verdict:` receipt.

The old measurements reproduce, but their historical interpretations do
not survive replacement of the retired insertion architecture. The accepted
late spelling and late SC040 placement therefore stand on their existing
source-backed grounds, not on automatically reversing old arrows.

## Propagation

SOURCE changes: live edge classifications and registry descriptions,
SC040 reader prose, the current grouped research dossier, control-plane
documentation and focused regression tests. Registry projections, reader,
combined book and indexes regenerate only through `adjudicate.py --refresh`.

Normal registry validation diagnoses contrary current historical and
technical precedence, and separately reports archived, nonordering,
unavailable and non-numbered endpoints. It uses complete physical
`exec_index`, not an invented historical-order field.

Baseline/fingerprint effect: none. The complete scientific non-regression
and publication results are recorded in
`../../assembly/post_migration_consistency.md`.

## Residue

The ordinary SC040/072 adjudications remain pending. This cleanup neither
establishes their full empirical generality nor reopens SC035. No historical
source, rule change or baseline approval is needed to resolve these three
obsolete live claims.
