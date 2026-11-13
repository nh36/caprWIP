# Nightmare2141: attested weak nominative selection

## Identity

13 November 2026; `review/2141-nightmare-maere`, base `9882f3e7`.
One-lexeme editorial selection, not a sound-change adjudication.
No executable identifier, historical stage, scope or chronology is changed.

## Question

Select attested weak feminine nominative singular mære for the simplex
indexed by English 'nightmare'. Retain *márōn as both PROTO and PROTOFORM
and test the prediction that unchanged production still yields mare.
A changed executable output or any second changed target would invalidate
this target-only transition.

## Current state (before any edits)

The live target and mature entry were mare; the note incorrectly rejected
mære as a stale headword/conflation. Fresh production evaluation reproduces
394 accepted forms, 386 matches, eight mismatches, no ambiguity.
Row2141 has output mare. SC042's registry verdict is DEFER.

## Diagnosis

COUNTERPART changes mare → mære; TOKENS, ALIGNMENT and IPA are synchronized
to the short-vowel simplex. Identity, grouping, contexts, input, PROTO,
DERIVATION_CLASS and import HISTORY are conserved. The selected nominative
is a historical comparator, not permission to repair the output by fiat.

All394 outputs and multiplicities must be identical to the fresh before
evaluation, with exactly row2141's comparator and match flag changing.
The input/outputs projections and original380 archive remain protected.
This is an out-of-fit witness for the current vowel history, not new
relative-chronology evidence. No rule firing census or counterfactual
sound-law adjudication is undertaken.

## Literature

Original images checked: Lindsay1921 printed96, I225 (PDF116), maere
under incuba; RingeTaylor2014 printed192 (PDF207), front-root nominative
and endpoint mære. Hall2007 §2,301–302, distinguishes weak mære and strong
mær and explicitly identifies maran as a levelling donor. Table1,313–314,
documents mare in Bald's Leechbook and maran in Leechbook III.
Hall's I225 transcription merae differs from Lindsay's maere; the
diplomatic spelling here follows the edition directly.
The source ledger records source-versus-normalized spelling and limits.

## Historical analysis

The short-vowel weak nominative is selected, not the strong noun mær
or adjective mǣre 'famous'. Mare remains an attested, levelled variant.
Ringe–Taylor's reconstructed front-root nominative is not evidence that
the current cascade's restoration in that cell is correct.
The current retained nasal ending still causes restoration.
Model B's mære is a frozen research result, not an adopted production rule.
No new stage, scope, conditioning or chronology edge is proposed.
Positive analogy evidence concerns the variant and named oblique donor,
not the regular selected mære.

## Verdict

Adopt only the authorized lexical comparator and publication corrections.
The historical and computational classifications are distinguished:
regular selected history, currently mismatching implementation.

Registry-verdict: SC042=DEFER

This line records the unchanged registry authority. The baseline interface
requires an SC namespace, so the exact approval refers to SC042 with
transition_id `nightmare_target`; it neither completes nor changes that
sound-change verdict.

## Propagation (only after verdict)

The current baseline is adopted only through:

```sh
python3 Germanic/tools/adjudicate.py SC042 --adopt-cell-baseline \
  --approval approved_nightmare_target_migration.json
python3 Germanic/tools/adjudicate.py --refresh
```

The adopter preserves the exact old outputs/summary as
`*_pre_sc042_nightmare_target.*`; no historical archive is edited.
The expected new counts are385/394 matches and nine mismatches, with
all executable-output fingerprints conserved. The existing migration
ledger permits this exact old/new target while requiring identical input
and output. The known-problems ledger parks the implementation gap.
Mature and compact prose sources keep their stable filenames.
The earlier lexical memo is marked superseded; frozen research inputs,
receipts, archived reports and extraction-time source records are retained.

## Residue

No sound-law correction, target change for another lexeme, or Model B
adoption is authorized. The outstanding implementation decision remains
separate from the philological legitimacy of mære.

## Executed validation and publication

The fresh protected adoption and subsequent control-plane refresh succeeded.
Production accepts all394 inputs without ambiguity or rejection. Matches
change386 →385 and mismatches eight →nine solely because row2141 now
compares output mare against target mære. Every input/context and all394
complete stage trajectories are unchanged, apart from the selected comparator
and its resulting report bucket. Witness-list ordering changes in generated
censuses follow that bucket movement; firing counts and memberships agree.

The old active baseline/summary are byte-for-byte preserved in the new
pre-nightmare archive pair. All earlier baseline archives remain byte-identical.
The conserved fingerprints are:

| Projection | SHA-256 |
|---|---|
| Production FST source | `62fb821f9988cf995043cb9a978b76a5a3fc83caff5b026928c64a0dd378062c` |
| All executable outputs | `43a57847b70b39ec130b4b52a17065be8cedd0e5fe7c6cc801ae1bcecae9fe2c` |
| Lexical executable outputs | `2783f9617b26caf0ad10836a99d4502f80f47ee13f858aaea123b9351b1c5514` |
| Protected migrated380 | `a004ea461f76e5ca0c00d4ab407648247222a5123ccad31e2c6a89fe0223ed47` |
| Literal original380 | `fae656520e9ebf446854643907a1ba48a511877fc25b1fae39649d5b97e9a6cf` |

Focused regression:96 tests and826 subtests passed across
`test_cascade_baseline.py`, `test_lexical_editorial_publication.py`,
`test_pgmc_lexical_integration.py`, `test_lexical_editorial_order.py`,
`test_sc112_monosyllabic_final_r.py` and `test_sc042_adjudication.py`.
The new transition test requires exactly the one comparator/match change,
conserved output fingerprints, and rejection of an invented mære output.
The full/compact rendering test requires the implementation-gap explanation
and rejects the former regular-outcome claim and reconstructed-output markup.

The normal strict publication command succeeded:

```sh
INDEX_VERBORUM_STRICT=1 ASSEMBLY_KEEP_DEBUG_TEX=1 \
  bash Germanic/docs/assembly/build_capr_book_draft_docker.sh
```

Its passing gates include reader-facing semantics, predicted-form policy,
bibliography sanity, index validation and assembled occurrence parity,
paragraph glosses, executable/reader order parity, unresolved references,
rendered index structure and TeX policy, print readiness, bibliographic
locator rendering, and18 index-architecture negative fixtures.
An initial fingerprint failure was resolved through the existing scoped
semantic allowlist, preserving the historical snapshots. Newly indexed
variant/oblique mentions carry their required first-mention glosses.
No scholarly account was changed to manufacture an index match.

Actual final PDFs were text-checked and inspected as page images:
the combined entry is printed178–179 (PDF sheets180–181), and the
standalone lexical entry is47–48. The Old English index on printed334
(PDF sheet336) has mære178, mare179 and maran179. The first is the selected
heading; the others lead to the attested variant and oblique discussion.
The current compact prose was also rendered as an isolated entry with the
existing renderer, metadata, citation machinery and publication filters:
its page1 agrees on mære, the unchanged *márōn → mare output, and the
unadopted status of Model B. This is a compact-entry check, not a fresh
certification of older whole-volume compact rollout artifacts.

Genuine command receipts and complete logs are retained privately under
`.capr-work/nightmare-2141/validation/`, including failed attempts.
Final receipt labels are `nightmare-refresh-verified`,
`nightmare-tests-verified`, `nightmare-publication-verified` and
`nightmare-compact-render`; original scholarly PDFs are not redistributed.
This focused editorial/publication validation is not a new whole-suite
strict scientific certification or an adoption of the deferred SC042 work.
