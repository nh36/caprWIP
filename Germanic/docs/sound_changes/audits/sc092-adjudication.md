# SC092: surviving velar fricative spelling

## Identity

2026-11-05; SC092; `OldEnglishOrthography`, physical stage107; orthography/surface support, not a sound-change date. Branch `research/full-cascade-functionality`, base `7e6023eda8a52df8916181aa98bbd935f331d069`; coordinated certification with the separately justified SC001 parser repair.

## Question

Does the unprojected surviving `{*ɣ}` symbol wrongly prevent otherwise valid OE spelling outputs? Test general late spelling projection, not a new phonological merger or a lexical exception.

## Current state (before any edits)

The registry has no previous SC092 adjudication. Orthography already projects stop and palatal reflexes, but lacks surviving `{*ɣ}`. `ɣó` parses and reaches the spelling boundary, then has no accepted final output. These are formal controls, not newly claimed historical etymologies. The391 selected inputs/targets and their383 matches/eight inherited mismatches remain untouched.

## Diagnosis

Add exactly `{*ɣ} -> g,` to the existing orthography replacement group. Actual complete controls now give `ɣó -> go`, `ɣú -> gu`, `ɣrá -> græ` and `á-ɣan -> agan`; already palatalized `ɣá/ɣí/ɣé/ɣjó` and `á-ɣa` remain unchanged. Closed-tier controls include medial/final, voiceless-following, sonorant-following, postnasal, geminate, stop, palatal and x/ç classes. Raw `áɣ/ánɣi/áɣɣi` do not parse and must not be presented as complete-word positive controls.

The complete finite-tier mapping certificate has106 arcs,13 reachable twins,11 live, delay0, ATT SHA `1c2b88b9b552f60990e46667315372136305e2b263b9fb763ac2b1d483fd26b1`. The symmetric path difference between current closed-tier orthography and previous orthography composed with that deterministic map is empty. The frozen actual source and compiler identities bind this factorization. All391 actual final outputs and parser analyses are conserved; selected stage histories are checked during canonical refresh.

## Literature

Directly checked sources and retained page-image identities are recorded in `post-sc052-domain-and-contraction/`: Campbell1959 p21 §50(4), written g often representing a fricative and initial stop articulation late; p180 §446, final spirant devoicing and date/text-dependent final g/h spelling; RingeTaylor2014 p4, distinct stop/fricative/palatal values, editorial dotting and postnasal fricatives after syncope.

These sources justify a written-g projection for the surviving velar class. They do not establish that every occurrence was a stop, abolish palatal reflexes, or require invariant final-g spelling across periods.

## Historical analysis

This is the terminal orthographic representation of the surviving velar fricative, after independently owned palatalization and consonantal rules. Stage/scope labels remain technical, without a new chronological assertion. No phonological environment is conditioned by lexical identity or grammar. Stops and palatals retain their existing handling; the mapping neither licenses an earlier velar/palatal merger nor asserts phonetic stop realization. Final written g is an explicit general spelling policy, not a substitute for source-supported final devoicing, and not a mandatory late-West-Saxon h policy.

No positive evidence for analogy is relevant. No chronology edges change. The general modelling choice is spelling projection; raw controls establish implementation scope, not unattested Proto-Germanic constructions.

## Verdict

REFORMULATE the late spelling relation.

Registry-verdict: SC092=REFORMULATE

A deterministic, source-supported surviving-class projection fixes a general representation omission without changing selected derivations. Unrelated broad-domain surface failures are not grounds for withholding it.

## Propagation (only after verdict)

Authorized combined source SHA `c51c3f440e48c320968dd7a12c3b9995c2b16f5e766ef075f16f7af8eba76d3d`; SC001 separately owns the six nucleus-group repairs. Source, complete graphs/certificates, raw/tier controls, compiler transcripts and391 regression are in `bounded-domain-adoption/evidence.zip`. Its manifest and the immutable `final-bounded-adoption-02` experiment bind the exact tested bytes. `test_bounded_domain_adoption.py` pins this clause/dependency closure and checks actual selected/contrasting outputs. Three cumulative inventories explicitly allow this independently pinned clause; the third was identified by the preserved first strict failure. No SC035 rule or verdict is changed. Protected baselines and reader remain unchanged.

## Residue

The preexisting orthography ambiguity on decomposed `*ɔ̆ -> a/ŏ` remains visible and is not introduced by this deterministic factor. SC086 still branches on artificial inputs; `ɣò-oxun -> goōn/gōon` newly exposes that earlier ambiguity rather than creating a second spelling for one input representation. `ḗô` and the exact `à` domain-difference witness remain surface-rejected. No totality or global functionality claim is made for the broad synthetic domain, and no independently supported historical ambiguous input has been demonstrated. See the final decision memo for protected certification and bounded disposition.
