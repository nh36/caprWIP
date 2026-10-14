# Nasal bimoric vowel: technical adoption

## Identity

SC017 `PNWGmcULowering`, shared SC015 conditioning, and the general input/vowel
classes. Branch `update`, base `812cc437`, containing the completed SC034
adjudication and the published investigation. This is the first of the two
explicitly authorized adoption commits, not a new chronology decision.

## Question

Does recognizing inherited nasal bimoric *ǭ* throughout the actual OE input
pathway correct its missing lowering domain without changing any selected
input, target, context, or derivation? A changed selected checkpoint, rejection,
ambiguity, or conflation with oral *ō* or trimoric *ô* would refute the proposed
output-neutral repair.

## Current state (before any edits)

Bare final *ǭ* was absent from the weak-tail parser, although complex *anǭ*
was admitted. Alphabet admission did not imply vowel recognition:
`PGmcStarVowel`, its back-vowel class, the English long-vowel class and the
non-high conditioner omitted it. The inherited accusative *wúllǭ* therefore
rejected as raw input; entering its starred symbols bypassed that rejection
but incorrectly retained root *u*. The current order is SC017 → SC018 → SC019.
All 387 selected rows were deterministic, with 379 matches and eight mismatches.

## Diagnosis

The fresh SC017 evidence census reproduces the 39 applications listed, with
stable IDs and pre/post states, in the frozen investigation's
`complete_sc017_sc018_sc019_firing_census.tsv`. None acquires a different
development. The new `sc017-nasal-vowel-adoption-receipt.json` compares all
41,409 row/checkpoint pairs (387 rows × 107 checkpoints), independently checks
the complete compiled wrapper against replay, and records 53 component checks.
Raw nominative *wúllō* gives *woll*; raw accusative *wúllǭ* gives *wolle*.
Unaccented spellings give the same finals.

The receipt enumerates every direct and transitive consumer of the seven
modified classes, using the comment-aware executable-definition parser.
Raw-parser consumers include strong heavy roots, weak tails and compounds;
starred vowel consumers include final-z loss/rhotacism, allophony and consonant
loss, vowel shortening, hiatus/glide treatment, mutation/restoration, syncope,
apocope, alphabet filters and cleanup. These operations must recognize a real
back long vowel; the repair changes membership, not their rewrites.
The separate weak-tail mirror keeps breaking's weak-tail/non-weak-tail
partition consistent. SC015 shares the non-high class: its coronal-only
lowering before *ǭ* is tested explicitly, without changing its other restrictions.
The long class makes *ǭ* available to existing weight tests; it does not make
short nasal *ą*, *ę* or *ų* long or merge their distinct lowering behavior.
The source's legacy shared German wrapper also consumes `PGmcStarVowel`;
it inherits correct vowel recognition, but no non-OE historical account is
adjudicated here.

The component checks cover nasal/j blockers, unrelated nasal-vowel negatives,
oral/nasal/trimoric contrast, SC018's separate monosyllable, and both context
prefixes. Row 2326 retains exactly `ᵘízwiz` → *ēow*. No marker enters its final.

## Literature

The source-backed domain and distinction are established in the completed
investigation: Ringe (2017, pp. 242–243) prints wool's nominative *wullō* and
accusative *wullǭ*; Fulk (2018, pp. 82–85, 155) distinguishes oral, nasal and
overlong endings. Ringe and Taylor (2014, pp. 27–34, 58–60) supply the lowering
and later ending discussion. The implementation retains nasal *ǭ* symbolically
until SC072 → *æ*, then SC073 → *e*: that serialization does not claim that
nasality persisted historically until Old English.

## Historical analysis

No stage, scope or executable position changes in this technical commit.
Adding a missing genuine non-high vowel is a general domain repair, not an
exception for wool or an analogical rule. SC019 still matches only final oral
*ō*, not nasal *ǭ* or trimoric *ô*. SC019's protection of *ōz* before SC020
is untouched. The comparative chronology interpretation follows in the
separately reviewable scientific adoption.

## Verdict

Repair general input and vowel-class recognition; retain all rule bodies and
SC017 → SC018 → SC019 ordering. The shared conditioner now includes *ǭ*.
This technical memo does not independently replace the canonical SC017
historical verdict; the scientific supplementary memo owns that qualification.

## Propagation (only after verdict)

Editable owners are `germanic.txt`, the focused verifier and its tests.
The receipt is produced by:

```
docker compose exec -T backend python3 /usr/app/tools/verify_sc017_nasal_vowel.py --output /usr/app/docs/sound_changes/audits/sc017-nasal-vowel-adoption-receipt.json
python3 Germanic/tools/adjudicate.py --refresh
```

The verifier refuses an existing receipt and compiles only in a temporary
container directory. Historical SC034 assay pins remain historical rather than
being silently repinned to this new source. No selected field, frozen baseline,
protected experiment, or historical receipt is changed.

## Residue

### Technical closeout

Canonical `adjudicate.py --refresh` completed with `CONTROL PLANE CLEAN`.
The regenerated 126-pair interaction matrix is byte-identical; only its
definition provenance changes. The focused run passes 52 tests and 32
subtests. `sc017-nasal-vowel-protection.json` verifies all 163 original
protected paths: 48 unchanged, one expressly authorized FST SOURCE repair,
and 114 required generated runtime/provenance rebuilds. All protected
corpus, sidecar, frozen-baseline and historical-receipt files are unchanged,
as is every artifact listed by the frozen investigation's publication
hash manifest. Rebuilt binaries are not described as byte-identical:
the admitted input language has intentionally expanded.

The trimoric genitive *wúllôz* still rejects as raw input, and the underlying
general starred vowel inventory still lacks *ô*. Its incomplete final-z and
ending pathway is explicitly separate from this nasal-bimoric repair.
Wool remains `unexplained_unmodelled`: regular *woll* is not attested *wull*.
The unchanged mismatch IDs are 1973, 2013, 2030, 2162, 2224, 2240, 2298 and 2300.
