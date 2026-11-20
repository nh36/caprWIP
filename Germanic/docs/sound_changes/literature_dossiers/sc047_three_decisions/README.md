# SC047: three source-led decisions

Control: `634a133538bed66df7edd0737b1c5776cda8739d`; PR #19 remains
open for review. Read [source-assessment.md](source-assessment.md) for
the first-order attestations, competing accounts, exact predictions,
indirect-only references and dispositions. No production rule, order,
selected cell, target, context or baseline changes here.

## Decisions

1. Propose deer1988 genitive plural *déuzô → dēora, retaining headword
   dēor and the direct-case diagnostic. This is a review proposal, not
   a migrated corpus or a refrozen baseline. CAPR ô encodes the quantity
   of source *-ôⁿ without separately encoding its nasality.
2. Unchanged SC112 can precede early SC047. It then sees suffixed dorą
   and does not lengthen door; the same there/where applications survive.
   This is a candidate's implementation prerequisite, not a new strict
   historical edge established by two adverbs.
3. Retain the live SC047 placement. Early loss plus glide nuclearization
   improves rīkī/rīċe; searu has positive source evidence for extension
   from searwes, rather than an unexplained historical failure. The
   complete candidate still requires explicit paradigm histories and
   changes hay/net/hue. The SC111 obstacle is separately repairable,
   without pretending that modelled strēa is attested strēaw.

## Seven-way selected-corpus comparison

| Configuration | Matches / 394 | Changed endpoints |
|---|---:|---:|
| identity | 386 | 0 |
| after_SC041 | 386 | 0 |
| joint_pre_gemination | 384 | 3 |
| SC112_before_early_SC047 | 385 | 2 |
| SC112_early_SC047_glides | 382 | 5 |
| SC112_early_SC047_aw | 385 | 1 |
| SC112_early_SC047_glides_aw | 382 | 4 |

Every selected record is accepted and unambiguous. The exhaustive union
of changed rows is deer1988 dēor→dēo, door1992 dor→dōr (only without
moved SC112), hay2061 hīeġ→hēa, net2138 nett→nete, straw2224
strēa→stræw (without the SC111 companion), and hue2332 hīew→hii.
Hii is an incomplete model derivation, not an attested historical form.
The best complete early package still changes deer/hay/net/hue.

All40 SC017 firing identities survive all seven configurations.
SC112 has precisely the original two identities except the unmoved
early-loss trial, which additionally lengthens door. SC047 has159
live/after-SC041 firings and160 early ones: only straw is added.

## Reproducible evidence

`experiments.zip` contains the immutable preregistration, FST/corpus,
worker/helpers, complete observations, authentic logs and receipts for
`sc047-followup-a2ca7453`. `manifest.json` pins every member, the control
hashes and the archive itself. Earlier matrices are not rewritten.
The archived worker exposes `--capture PLAN` for snapshot capture and
Docker execution, and `--worker SNAPSHOT` for its container-side work.
Docker backend Foma is required, never a host-local Foma installation.

The TSVs preserve all2,758 selected output sets, every changed row,
complete SC017/047/112 firing censuses and compiled stage checkpoints.
`deer-cell-proposal.tsv` gives exact review-only fields.
`scores-and-proposed-cell.tsv` separates original scores from the
hypothetical one-row migration: identity386, early-SC112386, and
complete early glides+aw383. No hypothetical score is a live certificate.

The retained-o *déuzomiz diagnostic is rejected by EnglishProtoInput;
no downstream result is inferred. The staged hay alias using native-
inappropriate h is preserved with its original rejection. Correctly
serialized canonical hay2061 supplies the operative full trace.

No acquired book, article full text or page image is included. Original
holdings are private; their safe metadata is in
`docs/references/sc047_early_apocope/`.

## Validation cost review

This opt-in experiment compiled740 finite-domain networks across seven
configurations: common definitions317.398s, peak RSS2,243,756KiB;
batched relations8.014s, peak RSS1,149,852KiB; total327.113s.
It adds no routine test compiler, fixture scope, sweep, rebuild or
concurrency change. The supplied staged suite is frozen research
evidence, not a new expensive default pytest lane. Final A/B/C and
publication results are reported separately for the final commit.
