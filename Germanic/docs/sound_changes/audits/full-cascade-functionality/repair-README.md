# SC052 bounded repair capsule

Historical status notice: the proposal-state statements below record the
original research capsule, whose evidence is preserved unchanged. The bounded
repair was subsequently adopted in `529eeaa5`; see
[`sc052-reader-adoption-closeout.md`](../sc052-reader-adoption-closeout.md)
for controlled acceptance and publication. SC086 and totality remain unresolved.

## Result and status

The minimal private correction is **one additional comma** before the
gg-before-j clause in `OEVelarPalatalizationStops`. Foma `,,` closes the
previous ruleset's contexts; `,` does not. No phonological environment,
historical date, class, input grammar or preferred-output filter is added.
The actual candidate source differs from the protected source by precisely
that one character, retaining all comments.

This candidate is globally functional at SC052 but **does not make the full
cascade functional or total**. It is proposed, not adopted. The accepted
four-cell production source, selected corpus and protected baselines remain
unchanged. No reader-facing executable definition or publication was replaced.
The full template assessment is
[`sc052-post-acquisition-adjudication.md`](../sc052-post-acquisition-adjudication.md).

## Exact compiler semantics

Pinned commit: `82f9acdef234eae8b7619ccc3a386cc0d7df62bc`.
`regex.y`128–145 and270–293 accumulate centres and contexts until
`add_rewrite_rule()` closes a ruleset; single comma continues it, double comma
closes it. `rewrite.c`132–150 and193–203 compiles each centre under the
ruleset's pooled contexts. Image sources match the pinned public sources;
hashes are in `repair-provenance.json`.

In the incumbent, g and gg centres consequently share front-vowel **and** j
contexts. This explains both the unwanted gg conversion before a front vowel
without j and the partial singleton covering before j. Overlapping centres
give distinct accepted outputs; it is not a spurious native diagnostic.
The miniature a/aa relation and exact accepted paths independently reproduce
the semantics. No patch to Foma itself is proposed.

## Formal results

The accepted input-synchronized twin method was reused unchanged. All
analyzed exports have a finite closed alphabet; no unknown/identity symbolic
arc was silently admitted. Positive certificates enumerate the complete
live twin graph and verify delay invariants, without a word or delay cutoff.
The method establishes at-most-one output, not totality.

| Actual compiled relation | Independent result | Native result / limitation |
|---|---|---|
|Original stop/wrapper|Nonfunctional, complete accepting-path counterexamples|Native failure is genuine here.|
|Serial, pointwise and minimal scoped stop/wrapper|Globally functional on the recorded closed input alphabet; compiled ATT relations are byte-identical|Scoped stop and wrapper return1. No unsafe inference from transducer subtraction is used.|
|Repaired cumulative physical-stage62 (`candidate-prefix-061`)|Functional:238221 arcs,236192 reachable twins,75712 live twins; maximum delay3|Native0 is a false negative for this actual relation.|
|Repaired cumulative physical-stage99 (`candidate-prefix-098`)|Functional:1227402 arcs,3355552 reachable twins,409632 live twins; maximum delay5|Native0; independent certificate verified.|
|Repaired cumulative physical-stage100, SC086 (`candidate-prefix-099`)|Nonfunctional; a complete witness survives the full suffix|This is a certified boundary pair, not a fresh certificate for every intervening prefix.|
|Actual complete repaired `OldEnglish`|Nonfunctional:1906381 arcs; explicit distinct final outputs|Native0 is genuine. Minimal scoped and pointwise full ATT files are byte-identical, SHA256 `10246fbb754e3b9323c3c9d307baa8e784c9d682ffcdee4911c84e217b7ee1de`.|

The minimal candidate's complete relation is thus independently checked,
not inferred from a few words. Its exact equality to the analyzed full
pointwise relation follows from byte-identical actual ATT exports.

## Complete downstream effects and stopping point

SC052 examples:

- `ggai`: incumbent `gġē`/`ġġē`; candidate only `gġē`.
- `g-géua`: incumbent `gġēo`/`ġġēo`; candidate only `gġēo`.
- `*g*g*j`: incumbent `*g*ʤ*j`/`*ʤ*ʤ*j`; candidate only `*ʤ*ʤ*j`.

The full repaired relation instead provides `ò-oxun` → `oōn`/`ōon`.
Its110-stage traces first branch at SC086 `OEContraction`, physical-stage100,
when `*o*o*o*n` contracts its first or second adjacent pair. The prefix-stage
proof also finds `o-òxun` with the same two starred outputs. Complete accepting
paths are replayed in `verified-paths.json`. The original cascade already
has the ò-oxun ambiguity: this is newly exposed, not introduced by the repair.

These are accepted computational inputs, not attestations. The grave-marked
witness has no explicit primary acute; do not extrapolate it to a separately
defined historically well-formed primary-stressed domain. The declared
actual-parser domain remains the tested domain. `ó-oxun` and `ó-óxun`
are retained distinguishing controls, not an ad hoc domain restriction.

All391 selected inputs, their complete output sets and all110 cumulative
stages were compared against the preserved actual original bins:43010
selected-stage comparisons, zero differences. That includes the protected380
subset. There are383 matches, the same eight mismatches
1973,2013,2030,2162,2224,2240,2298,2300, zero missing and zero ambiguous selected
outputs. The complete32-row SC052 firing census and thirteen positive/negative
class controls are preserved. This conservation is **finite regression**.
The unchanged fricative/merger source and global wrapper equality preserve
the accepted key/day class distinction; no new key/day historical
adjudication or fresh protected adoption assay is claimed.

Totality remains independently false for `ɣó`; see
[`totality-followup.md`](totality-followup.md). The surviving-ɣ mapping and
historical-input-domain choices are separate unadopted questions.
No SC086 or surface-filter rewrite is attempted in this bounded pass.

## Evidence, receipts and reproducibility

`repair-evidence.tar.gz`:70 members,28628340 bytes,
SHA256 `25a41ea59695fd179a324b715baf295bb8ea72fcaa42418e0b40bc6f63a3939e`.
It contains exact candidate sources, compiled relations/bins, native logs,
all reported positive certificates and negative witnesses, the unchanged
proof helper, immutable compiled worker, full selected/context inputs,
firing census,110-stage counterexample traces, source identities and receipts.
`repair-manifest.json` supplies every included member's SHA256.
Original protected scientific evidence remains in the previous
`evidence.tar.gz`, unchanged; source scans/OCR and source images are not
included in either new public report or this computational capsule.

The two completed pre-compilation failed attempts, partial invalid-label
snapshot03 and partial incorrect-context regression snapshot01 are recorded
as harness failures. No candidate was scientifically tested in those failed
invocations. Successful immutable compilation is repair04 and
scoped-context01; complete census/conservation is regression03. Receipts
record full-cascade failure rather than passing the global gate.

For independent rechecking, extract the capsule into a **new private
directory**, verify its manifest, then run:

```sh
python3 Germanic/docs/sound_changes/audits/full-cascade-functionality/repair_probe.py \
  --analyze NEW_PRIVATE_DIRECTORY
python3 -m pytest -q Germanic/tests/test_cascade_functionality_witnesses.py \
  Germanic/tests/test_parser_functionality_proof.py
```

`--analyze` reports each relation's `functional` flag; successful process
completion is not a claim that all those flags are true. It fails rather
than approving unsupported symbolic arcs. Recompilation must run inside
the verified backend container using an immutable snapshot and a new output
directory. The final worker retains `--worker`, `--scoped` and `--regress`
modes; the capsule pins the exact version used for scoped compilation.
Source preparation never writes production FSTs or canonical runtime bins.

No strict current-source publication certification is claimed. Documentary
refresh is portable, and the existing scholarly publication and accepted
scientific certification are retained as historical evidence.

Focused validation:37 tests passed across
`test_cascade_functionality_witnesses.py`,
`test_parser_functionality_proof.py` and
`test_adjudication_protocol_guardrails.py`. The original chapter/derivative
hash and restoration-member checks also passed without a Desktop dependency.
