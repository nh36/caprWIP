# B4 — A stage-aware entry interface and consumer audit

## What the alphabet has to express

Keep the historical structure explicit: syllabic *e.i* is two
vowels; light *ei̯* and heavy *ēi̯* each require one nuclear
token and a declared weight; *e+j* and *e+ʝ* are a vowel plus
a consonant. A long monophthong is not equivalent to a heavy
complex nucleus when rules inspect vowel quality. Early *īo*
and *ēo* must remain distinct until actual regional merger.
Use the [previously tested private inventory](../hiatus-cycle4/NUCLEAR_ALPHABET.md)
as a probe, not as the final spelling of OE.

An inherited nucleus and a new one should have different
categories only while there is an independently motivated
phonological distinction (structure, weight, component quality).
When those properties merge, use one token; do not retain
private lexical-origin labels for later rules to consult.
Historical stage and provenance belong to entry metadata,
not the phonological alphabet. Root accent, secondary
stress and pretonic footing also need explicit, separate
features; sentence tags `*ᵘ/*ᶜ` are not stress. The incumbent
`*ᶠ` provides one recognized pretonic syllable, not arbitrary
recursive footing or an indication that all plain vowels are
unstressed.

## Candidate implementation

The [driver](stage_entries.py) accepts three explicitly different
grades of execution. A full input goes to the native
`EnglishProtoInput` and follows the selected order. A **later**
historical entry has a cited source, a declared stage and a
starred input; a controlled route maps it to the correct
suffix without executing skipped processes. The experimental
pre-HVD route is visibly separate and stops after the private
weight operation. Observation-only entries do not execute.
The source statement is retained in the receipt, not fed to a
sound law. This is a research path, not a way to send arbitrary
later spellings through the production API.

The live proof refuses missing provenance, an unknown stage,
typed material at the wrong site and any executable input on
an observation. The private alphabet gate refuses unknown
`λ`. Exact local ‘clay’ *þōhæ* reaches *þōæ* without replaying
earlier stages; the missing contraction is explicit. The
synthetic marked light and heavy forms admit the designated
single nucleus, but only the heavy form loses final *i* in the
shared frame. These probes are not source reconstructions.
Native admission is unchanged; earlier proofs already show
that a string admitted by the old gate as two vowels is not
proof that it constructs either private nucleus.

## Consumer-by-consumer audit

The [receipt](stage-entries-traces.json.gz) applies all 15
probes **independently** to every stage in each order from
`OEStressFootContext` through `OldEnglishSurface`
(78 canonical, 77 each A and B2). For each stage it records
every rewritten and rejected input; a remaining case reaches
that stage's output unchanged. Independent single stages make
downstream problems visible even if upstream admission fails.
They do not certify a continuous derivation. An identity
result with out-of-environment probes is not proof that the
rule's class tests recognize the new segment.

| Consumer group | Diagnosis and necessary action |
|---|---|
| Native parser, sentence/context alphabets, headed vowel and foot grammar | The four new atoms are outside the current context alphabet; 59 stages in canonical and 58 in either alternative reject them in the tested shapes, including rendering's input checker. Extending one vowel-class alias does not fix those domains. Leave the PGmc parser separate. Define a shared stage-relative segment alphabet, headed-vowel projection and marker lifetime before exposing the new atoms to a longer corridor. |
| Early realization, brightening, breaking and front/back mutation | Atomic *iu* already rewrites to *ēo* before later regional decisions. The new high realization must meet independent i-mutation and dialect controls. Vowel-sensitive context tests must use features of the actual nucleus, not treat unfamiliar complexes as consonants or automatically classify all as monophthongs. |
| Stress and medial/final restructuring | `OENonHighSyn` deletes plain medial *e* in the chosen frame but initially protects accented *è* before decoding it. `OEMedUnstressedULowering` also decodes the secondary form in the independent probe. `OEStressFootContext` creates rather than ingests a pre-existing foot mark, and `OEHLoss` currently strips it. This is evidence for phase-specific lifetimes, not justification to retain a mark everywhere. Extend and check `Ctx` and `FootCtx` users, then test genuine stressed and weak paths with the same segments. |
| `HvS/HvL/HvV/HvH/HvI/HvP`, nasal and high-vowel loss, nonhigh and *l*-adjacent syncope | These are weight-sensitive independently of ordinary vowel membership. All four atoms are rejected by frozen HVD; empty output is not deletion. The patched local gate and weight operation distinguish light/heavy; [prior proof](../hiatus-cycle4/NUCLEAR_ALPHABET.md) also tests the paired syncope consumers. Other deletion rules are not certified by the HVD proof. |
| Singleton *h*-loss, contraction, palatal merger | Validate old relations with the new alphabet even when the new nucleus is not itself a target. Preserve hiatus versus nuclear boundaries and *j* versus *ʝ* before the incumbent merger, which actually rewrites the fricative to *j*. In an admitted stem with ordinary *ēo* or *īo*, do not add a rule merely to collapse the pair early. |
| Orthography, star erasure and surface validation | Unknown starred atoms do not print consistently; some yield stray `*`, others lose distinctions in star removal. A renderer must deliberately map each admitted structure and must not be used as evidence that the underlying quantity, phone or syllabification was the same. Keep phonological merger separate from any orthographic collapse. |

## Migration recommendation

**RETAIN** explicit later entries and typed local tests as a
research interface. **REVISE** any production implementation
into incremental gates: (1) exact source-labelled stage-local
entries using existing symbols, (2) a fully compared,
contiguous extended-alphabet window for a particular structure,
(3) a separate rendering change only with new, dated controls.
The proof tests disjoint endpoints and valid/invalid paths; it
does not authorize exporting `NxGate` or grafting three patched
consumers onto a full cascade with dozens more unsupported
boundaries. Before later integration, prove acceptance and
intended firing in each intermediate relation, test stress/weight
negatives and compare all old endpoints and changed traces.
This is an implementation substrate, not an adoption of any
final-hiatus chronology.

```bash
set -o pipefail
bash Germanic/articles/hay/research/hiatus-cycle4/run-container.sh stage_entries --stage-cache "$cache" |
  gzip -n -9 > /tmp/capr-hay5-stage-entries.json.gz
```

Use the [pinned cache warm-up](../hiatus-cycle4/PROSPECTIVE_STACK.md#identity-and-question).
Receipt SHA-256:
`465b64a9912c54d6b793a4d94522426c0994613edd2e446696f9939d443cb0a2`.
One isolated gate-family compilation and focused lookups,
not a standard CI lane or historical training population.
