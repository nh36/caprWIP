# Clay and fringe: external glossary-stage controls

## Identity

13 November 2026; `review/clay-fringe-stage-witnesses`, base `1fa39ed8`.
Authorized reader clarification and runtime regressions for SC073, SC085
and SC086, not lexical admission or a new sound-law implementation.

## Question

Before fresh execution, predict that the current clay stage entry
`*θ*á*n*x*ō*n` before `PGmcNasalLossBeforeX` reaches a front ending with
the fricative retained, then hiatus before `OEContraction`, then þō.
Predict that `OEHLoss` maps `*w*l*ō*x*u*m` to `*w*l*ō*u*m`.
Reversing loss/contraction must strand clay's hiatus; restricting loss to
an adjacent front vowel must retain fringe's fricative. Rejection, missing
checkpoints or multiple outputs refute the runtime predictions.

## Current state (before any edits)

Production remains the unchanged cascade at `1fa39ed8`. The protected
population is 394 accepted inputs, 385 matches and nine mismatches.
Neither clay nor fringe belongs to it. The clay raw input θánxōn was
rejected by the earlier research tokenizer; no parser repair is authorized.
The documented post-tokenization boundary bypasses only that limitation,
not the subsequent ending or consonant rules.

The registry-driven SC073/085/086 packets, their chronology cards, the
SC035 prosody decision and the late-tail/closing-cluster dossiers are the
current routing authorities. SC073 is adjudicated REFORMULATE;
SC085/086 remain unadjudicated. Their historical stage and scope remain
Old English, English-specific, independently of their identifiers.
The current reader overstates the toe displacement as historical proof
of merger before loss, and says that contraction resolves hiatus
"immediately". Both claims require qualification.

## Diagnosis

Fresh execution passed all five focused runtime tests, with no skips,
on 13 November 2026 (09:52:10--09:56:50 UTC).
Named checkpoints come only from `oe_pipeline`; ordinary toe uses the
existing cumulative snapshots. Clay uses the existing isolated stage-slice
compiler's diagnostic bins from its recorded entry boundary, applying
the production sequence including inline operations. The initial attempt
to compose unrestricted whole networks timed out after 600 seconds;
this is an assay-construction failure, not a linguistic counterexample.
The next attempt exposed an omitted orthography operation in the negative
control's surface rendering. That control now uses the entire unchanged
post-contraction production tail, rather than a hand-picked cleanup pair.
Fringe uses the actual loss
component, not a reconstructed full Proto-Germanic citation.
The two counterfactuals exist only in disposable test networks.

These are external application/feeding witnesses. Clay tests production
loss before contraction; fringe independently tests back-vowel loss and
the survival of u and m. Neither adds a lexical row or an endpoint count.
The existing accepted-corpus baseline is freshly evaluated, not adopted.
No new full firing census or SC-wide adjudication is claimed.

The [unaltered runtime observations](clay-fringe-stage-witnesses.observed.json)
were extracted from the successful run's stdout, including every clay
stage, both perturbations and the fresh accepted-corpus summary.

| Named checkpoint | Observed clay output |
|---|---|
| Before PGmcNasalLossBeforeX | `*θ*á*n*x*ō*n` |
| After PGmcNasalLossBeforeX | `*θ*ã*x*ō*n` |
| After OEVelarFricativePalatalization | `*θ*ō*x*ǭ` |
| After OEUnstressedLongVowelShortening | `*θ*ō*x*æ` |
| After OEUnstressedAEMerger / before OEHLoss | `*θ*ō*x*e` |
| After OEHLoss / before OEContraction | `*θ*ō*e` |
| After OEContraction | `*θ*ō` |
| After OldEnglishSurface | `þō` |

Thus the observed hiatus is ō + e. The feature assertion accepts a front
ending without requiring æ; the exact current-output assertion separately
pins e. Neither assertion identifies diplomatic ae with e. The actual
tokenizer still rejects raw θánxōn. Ordinary toe, evaluated through existing
cumulative snapshots, has `*t*ā*x*e`, then `*t*ā*e`, then `*t*ā`, then tā.

Production OEHLoss maps fringe `*w*l*ō*x*u*m` exactly to `*w*l*ō*u*m`:
ō and u flank the deleted x, and both u and m survive.

The two deliberate trials trigger the same assertion helpers used for the
positive witnesses:

| Trial | Observed failure |
|---|---|
| OEContraction before OEHLoss | At contraction's input/output the fricative remains, `*θ*ō*x*e`; later loss gives `*θ*ō*e`, and the unchanged remaining tail gives þōe. Both the pre-contraction-hiatus and contracted-endpoint assertions fail. |
| OEHLoss restricted to an adjacent front vowel | Fringe remains `*w*l*ō*x*u*m`, failing the exact hiatus assertion. The same trial deletes x before clay's e, giving `*θ*ō*e`, so it is not merely a disabled rule. |

These are expected assertion failures caught by pytest, not failing
regressions. Both temporary rule definitions remain in the test source;
neither is installed in production.

Every one of the 394 accepted records equals the existing baseline,
including all outputs and targets: 385 matches, nine mismatches, no
rejections and no ambiguities. The canonical FST, corpus, manifest,
tested canonical binaries and every baseline file are byte-identical
before and after the assay.

The production source SHA256 is
`62fb821f9988cf995043cb9a978b76a5a3fc83caff5b026928c64a0dd378062c`;
the accepted-output projection remains
`43a57847b70b39ec130b4b52a17065be8cedd0e5fe7c6cc801ae1bcecae9fe2c`.
The tested file's SHA256 is
`1c59a0a2fcefa4ed69470f0edbd78c96ca1fb7bf848c5e74af8d3db51a13af44`.
The full-runtime receipt records unchanged source identity during execution
and five passes, zero failures/errors/skips; its SHA256 is
`b5565ab1c4e4d24811a7854d3fcea75d1401b91adb71fdb5c56b46534fe72788`.
Full logs, failed construction attempts and JUnit receipts are retained
in the local `.capr-work/clay-fringe-stage-witnesses/validation/` directory.
The successful stdout SHA256 is
`1859a90cce7410716d452dddac87e44873790bb4af5df1f3b5f2ed218981ba55`.

## Literature

Original printed images checked:

| Edition and gloss | Diplomatic reading | Normalized interpretation and limit |
|---|---|---|
| Sweet1885 p.36, Épinal3, argillus (-a) | thohae | RingeTaylor2014 p.314 reads thōhæ, 'clay'; written h is not an IPA transcription. |
| Sweet1885 p.41, Corpus207, argilla | thoae | RingeTaylor reads thōæ, hiatus before contracted þō. |
| Sweet1885 p.104, Épinal1066 and aligned Erfurt parallel, villis | uulohum in both | Dative plural wlōhum, 'fringe'. |
| Sweet1885 p.107, Corpus2122, villis | uuloum | Dative plural wlōum with retained u and m and no h. |

RingeTaylor2014 §6.9.3, printed p. 314, was image-checked: its contracted
*wlōm is explicitly unattested in the cited texts, unlike the hiatus
form. The related early Mercian glossary witnesses compare preserved
states, not independent samples dated by the ages of surviving copies.
The readings are edition-level verification, not new manuscript collation.
Sweet's old copy-dating deductions are not adopted here.

The frozen research traces at `9882f3e7`, especially their clay supplement,
are comparison evidence, not current scientific authority. Their
current-identity trial has x with a late e ending; Model B has an earlier
front ending and palatal ç. The same final þō does not collapse those
different intermediate histories.

## Historical analysis

Retain the registry's Old English stage and English-specific scope.
Intervocalic loss is phonologically conditioned; grammatical dat.pl.
identifies fringe's attested cell, not a condition on the rule.
Clay's front ending and fringe's back/back environment must not be
conflated. Hiatus is a preserved historical state, not an instantaneous
orthographic fiction. No analogy is proposed.

The h-loss-before-contraction sequence is supported independently by
the compared clay readings and the historical account in RingeTaylor2014,
p. 314.
No absolute date or adjacency in historical time follows.
The toe displacement shows the current merger/contraction implementation's
dependency; it does not independently date the historical ae/e merger.
If Corpus thoae preserves distinct unstressed æ, clay instead puts loss
before merger in that form. Whether ae distinguishes æ from e here is
left open. Written h likewise does not decide [x] versus [ç]; assigning
the palatal allophone before a front vowel is a model analysis.

## Verdict

REFORMULATE the three reader discussions; RETAIN production rules,
serialization, registry metadata and corpus. This is not completion of
SC085/086 adjudication, nor a new registry verdict or chronology edge.
The existing SC073 verdict remains unchanged:

Registry-verdict: SC073=REFORMULATE

## Propagation (only after verdict)

Update the three authoritative reader sources, this record and the focused
runtime tests. Refresh derived products solely through
`adjudicate.py --refresh`, then use the normal reader publication wrapper.
Protect every accepted record, canonical binary and baseline file during
the isolated assays. No refreeze or lexical migration is permitted.

## Publication verification

The following completed successfully:

```text
python3 Germanic/tools/adjudicate.py --refresh
python3 -m pytest -q -s --durations=5 Germanic/tests/test_glossary_h_loss.py --validation-mode=full
python3 -m pytest -q Germanic/tests/test_reader_architecture.py Germanic/tests/test_cascade_baseline.py --validation-mode=full
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_20_docker.sh --check-fresh
INDEX_VERBORUM_STRICT=1 ASSEMBLY_KEEP_DEBUG_TEX=1 bash Germanic/docs/assembly/build_capr_book_draft_docker.sh
python3 Germanic/tools/adjudicate.py --status
```

The two pytest commands have authenticated JUnit receipts: five runtime
passes, then 56 reader/baseline passes and 397 subtests. No full Germanic
suite is claimed. The strict normal publication wrapper passed semantic,
predicted-form, paragraph-gloss, bibliography, citation, rule-order,
cross-reference, index parity/structure/readiness, bibliographic-locator
and 18 negative-fixture checks. It reports no unresolved internal
references or paragraph-gloss violations. Informational style/width
warnings and Pandoc ticker messages do not prevent successful renders.

The rendered standalone reader was inspected at pp. 108--109 (SC073),
115--116 (SC085) and 116--117 (SC086), including visual checks on
pp. 108, 115 and 117. The final combined PDF was also checked at physical
PDF pages 111--112 and 118--120. Diplomatic and normalized readings,
edition-page citations, rule cross-references, the e hiatus and the
reconstruction asterisk on *wlōm survive rendering. The exact compiled
rule bodies remain unchanged. The introductory and full lexical PDFs
were also regenerated by the normal wrapper; their extracted text is
identical to the base commit, so incidental PDF/log churn is not retained.

The final control-plane check reports every artifact-graph node fresh.
Corpus, production source, registry, protected baselines and the frozen
final-vowel research directory have no changes against the base commit.
The scope is the three reader sources, this evidence record and its
observations, focused regressions, the programme pointer and their
dependent publication products.

## Residue

The phonetic value of written h and the diagnostic value of written ae
remain separate philological questions. No rule change is adopted from
either spelling. Any proposed extension to palatal-fricative loss or
changed merger/contraction chronology requires separate source-backed
adjudication and full-corpus regression.
