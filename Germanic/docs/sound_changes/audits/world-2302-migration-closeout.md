# World: inherited nominative migration closeout

Date: 27 October 2026. Branch: `update`. Starting commit:
`5665e3038dab311a4803e64b0f517b03b4806b4d`.
Scientific authority: [SC036 current migration](sc036-adjudication.md).
The older world closeout, evidence/reassessment receipts and SC036 experiments
remain historical, byte-identical records.

## Adopted model

| Question | Adopted answer |
| --- | --- |
| Input | Inherited compact i-stem nominative `*wír-àldiz`; comparative PROTO `*wíra-àldiz` and selected OE *weorold* unchanged. |
| Early transponent | No necessary early ō-stem intervention or mixed-stage transponent. Class `regular` applies to the selected compact-input span, not a newly derived compound junction. |
| Accent lifetime | Earlier grave retained in the input and through SC037; existing SC038 removes it before weak raising. No global early stripping or new deaccentuation law. |
| Weak rule | Plain short a becomes u before l+C in initial C* V́ C a l C, where V́ is an acute short vowel. Exactly one intervening consonant bounds the light initial domain; no word identities or morphological flags. |
| Chronology | Architecture A after SC038 and before early unstressed fronting/breaking. B after fronting also succeeds. Luick's rounding environment and Goering's LH footing motivate the qualified choice; Versloot challenges compulsory fronting before lC without supplying this weak rule. No independent absolute date is inferred. |
| SC036 arrangement | Reformulated and relocated, retaining its identifier and composing `OELHWeakRaising` with the separately named temporary `OESoulProxy`. No new independently dated SC. |
| Other implementations | No other sound-law kernel changed; SC037/SC038 merely precede the relocated operation. SC040 and SC100 retained. Narrow u-only back mutation also succeeds; SC059's shared-context defect remains a separate follow-up. |
| Soul | Same selected input and *sāwol* output, protected by the temporary pre-u branch. Its source-led syncope/epenthesis implementation remains for separate authorization. |
| Evidence and uncertainty | Inherited i-stem, weak rounding, differentiated prominence and early-OE single LH footing have explicit source support. Exact i/e, accent, compact-junction development, the bounded generalization and detailed o/u chronology remain qualified reconstruction. |
| Regular span | Early short-i apocope, SC015 i-lowering, final-z loss, grave removal, weak raising, SC059 back mutation and SC040 medial lowering derive *weorold*. No final high vowel remains for later high-vowel apocope. This extends the defensible regular span without claiming the earlier junction has been solved. |

The six-model [placement receipt](world-2302-experiments/migration.json)
compares both placements and both technical arrangements on 389 selections,
the overlapping 380 protected identities, eight complete-input candidates
and focused component controls. Unrestricted raising affects the
heavy-initial onefold-shaped control; bounded raising excludes it and
permits weak twofold-shaped raising. Actual rainbow and lung remain unchanged.
Neither synthetic controls nor later spellings are presented as new
attestations of hypothetical intermediates.

## Exact production and baseline effects

Only 2302's `proto`, `proto_norm` and `fst_input` baseline fields change:
`*wír-àldu`/`wír-àldu` to `*wír-àldiz`/`wír-àldiz`.
All 389 outputs, targets, stress/finality contexts, acceptance, multiplicity
and match flags remain identical: 381 matches, eight mismatches, no rejection
or ambiguity. Fresh SC036 evidence still finds exactly soul and world.
The coverage changes are SC006 9→10, SC020 113→114 and SC063 64→63:
the inherited ending now loses i and z, rather than a later final u.

The existing approved-cell interface adopted
`approved_world_input_migration.json`, preserving separate
`cascade_baseline_{outputs,summary}_pre_sc036_world.*` snapshots.
No registered archive is modified; the immutable 380 hash is unchanged.

| Projection | Adopted SHA256 |
| --- | --- |
| selected 389 evaluator | `d6e8b90551e4bb57d8d161a8f2334c29620533a487a0e64f8857f500380d5e45` |
| lexical input | `7f7994848fba1b86b3c3b24d5d8ae41fab30e2f86e6816c92f63a7810cd69142` |
| active original 380 identities | `9fb5d393e2f91ad077115593034099851c2d067f5dfefec5859f516a93783597` |
| immutable 380 archive | `fae656520e9ebf446854643907a1ba48a511877fc25b1fae39649d5b97e9a6cf` |

The editorial manifest still contains 167 entries, now 89 regular. World
sorts between wold and yarn. The stage audit and sidecar agree, with confidence
still provisional and independent of the stage/variety labels. Eight exact
semantic-index approvals replace only world's four old transponent
provenances with their inherited-input counterparts. Four scoped index
overrides classify junction notation and mechanical intermediates, not
reword scholarly prose to satisfy an indexer.

## Validation and publication

- Fresh canonical `SC036 --evidence`: production/sandbox equivalent across 389
  selections; complete live firing census after SC038.
- Full strict pytest run: 1600 passed, 21 failed, 9114 subtests passed.
  All 43 runtime tests passed, including the actual migrated isolated assay.
  Failures identified outdated historical/current migration contracts and
  index approvals, not new final-output regressions.
- After exact fixture/projection reconciliation, the full non-runtime suite:
  1578 passed, 43 runtime deselected, 9090 subtests passed. Historical adopter
  tests exclude later migrations from their temporary old snapshots; no
  production validator is relaxed. Final targeted migration/SC036/baseline
  check: 54 passed, one runtime deselected, six subtests passed.
- `SC036 --finalize`, post-publication `SC036 --check`, and
  `git diff --check` passed. No registered frozen archive changed.
- Strict supported book build completed with
  `INDEX_VERBORUM_STRICT=1 ASSEMBLY_KEEP_DEBUG_TEX=1`.
  The first attempt caught two missing reader glosses; those were supplied
  before the successful build. Index parity, negative fixtures, references,
  heading wrapping and bibliographic locator checks passed.
- Rendered combined PDF 302 sheets, lexical 160, reader 108. Image-inspected
  combined sheets 69–71 (discussion and three Foma blocks), 181–184 (complete
  world entry and following yarn), 299 (OE index), 301 (inherited-input index);
  standalone lexical 61 and reader 69. No clipping, missing accents, stale
  input label or broken cross-reference was found. New debug TeX was removed;
  original scratch files were not touched.

No next adjudication or soul implementation was begun.
