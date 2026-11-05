# Adoption recommendations and certified-integration closure

Research closeout, 5 November 2026. No new production adoption, branch
push, merge, branch reassignment or book regeneration.

## SC052 and reader: closed for this investigation

Verified exact ranges:
`e842319430f9f41ac3cb9f1beb8173e1c3d07fb8` →
`529eeaa5864d37d2f67e54ae003247cb21421daa` →
`efd9ec412a36aa5e9705ccacb63038c114e39fa3`.
The first range contains 39 certified scientific/editorial/generated
files; the second contains 12 documentary/evidence files and changes no
protected scientific SOURCE. The sole production FST alteration is the
additional comma in `OEVelarPalatalizationStops` at line 3448.
The reader's definition matches the accepted executable.

The short integrity replay verifies both capsule manifests, the official
final COMPLETE journal, all five authentic final-publication receipts
and every one of the 39 tested file hashes against commit `529eeaa5`
and the current tree. The accepted FST SHA-256 is
`33d062fe6624a7eae3bf541dbf22a2f89eb4da101fcde5d2a4e8d702b27f41f6`;
the tested tree identity was
`d4ad42f9370239570785bfbc0fcb8161de536cd0b7adbf986769ca24a81b36fd`.
Three positive independent SC052 certificates also replay successfully.

The retained final validation is A: 29 passed; B: CONTROL PLANE CLEAN
and STATUS OK; C serial: 1,910 passed, five explicitly opt-in historical
recompilations skipped, 9,635 subtests passed; C exclusive: 26 passed.
No material inconsistency was found, so no full strict rerun was made.

The two preserved 320-page PDFs are distinct:

| Artifact | SHA-256 |
|---|---|
| exact four-cell-certified prior PDF from `1b0698223d7d4c46999a18c03c1d30fd60cd54e9` | `ba02ceca6b7f9b4c18970b53f3b5dad26f8b43df30983b8e95b7296c06c0866e` |
| accepted reader at `529eeaa5`, still current | `2145305916348cf0a0fc193fbe9f894dafeb97ff32730436d7af05d084c2aa09` |

The prior is preserved separately at
`.capr-work/sc052-adoption/prior-publication/certified-four-cell-1b069822.pdf`.
The recorded visual inspection covered eight amended passages across
PDF sheets 41, 60, 76, 77, 82, 83 and 85 (printed 39, 58, 74, 75,
80, 81 and 83). The integrity replay verifies the preserved rendered
page identities and inspection receipt. It does not substitute a new
publication build for that completed inspection.

Exact evidence roots:
`audits/sc052-reader-adoption-closeout.md`,
`audits/sc052-scoping-acceptance/{MANIFEST.json,evidence.zip}` and this
capsule's `analysis/integrity.json` / `analysis/integrity-receipt.json`.
SC052 and the Fulk/Seiler reader revision are closed here, without any
claim that the accepted full cascade is globally functional.

## Separate candidate dispositions

| Change | Readiness and required decision |
|---|---|
| Six mandatory parser groups | Concrete, independently functional parser candidate; no added input strings and no selected391 differences. Prepare a separate controlled parser-policy decision explicitly superseding the documented empty/vowelless compatibility policy. Not adopted; not `D_historical`; not a totality repair. |
| SC086 comma scoping alone | Not a repair: the compiled relation is unchanged. |
| SC086 whole-tag guard | Useful representational proposal; preserves selected stages but retains real overlap. It cannot be certified as a functionality repair. |
| Serial contractions | Reject this tested treatment: still nonfunctional and changes the accepted conservative three target. |
| Per-centre directional arrows | Reject as a functionality fix: complete compiled counterexamples remain. |
| Unified longest-leftmost relation | Complete formal functionality proof, including the full raw cascade, and no selected-stage differences. Retain as a formal comparator; do not adopt without a historical argument for its direction and an account of the independent stressed-i/ū+a controls. |
| Surviving-ɣ orthography | Ready for a separate, bounded controlled-adoption proposal as spelling projection, with the qualifications below. No production acceptance or fresh strict certification is claimed. |

No candidate is approved by this research closeout. A future acceptance
must bind its precise source delta, declared controls and independent
proofs to the protected workflow and required full source-bound
validation. Formal functionality, historical adequacy and strict
production acceptance are three different statements.

## Surviving ɣ: bounded orthographic proposal

The exact private source delta is one new first clause in
`OldEnglishOrthography` (FST line 823): `{*ɣ} -> g,`.
Candidate source SHA-256:
`c7fe01dc68c1dae78e17bd1e199aae4a3b14041d6d8513210a009569d468346b`.
This is not a special case for the synthetic alias control `ɣó`.

Direct source checks support written g for the velar fricative:
Campbell 1959 p.21 §50(4), and Ringe–Taylor 2014 p.4 on the
fricative/stop and palatal distinctions and editorial dots.
Campbell p.180 §446 also matters: final spirants devoice, and final
velar g/h spelling varies by period and text. Thus this proposal spells
the surviving representation; it does not perform final devoicing,
prove every surviving final ɣ historically appropriate, or settle a
uniform late-WS final-h editorial policy. That policy must be explicit
in any adoption decision rather than hidden in an orthographic patch.

Actual controls cover initial back vowels, clusters, medial/final
component positions, palatals, postnasals and geminates. Full cascades
give `ɣó → go`, `ɣú → gu`, `ɣrá → græ`; corresponding ordinary-g
controls agree. Already palatalized `ɣá/ɣí/ɣé/ɣjó` outputs remain
identical to their g counterparts. Stop g/ɡ, j/ʒ/ʤ, ç and x centres
are not changed. Direct tier controls are explicitly not claims that
raw `áɣ`, `ánɣi` or `áɣɣi` parse: they do not. `ággi` is also
parser-rejected and is not a valid whole-word geminate demonstration.

The closed-tier candidate equals the old orthographic relation composed
with a deterministic ɣ-spelling map. Its compiled symmetric path
difference is empty, independently checked by graph reachability;
the spelling map's complete functionality certificate has 106 arcs,
11 live twins and delay 0. Empty path difference is sufficient here;
no general semantic-equivalence theorem is inferred from a nonempty
transducer path difference. All 391 selected full output sets are
unchanged.

This proves no new branching in the orthographic mapping itself, not
unconditional single-valuedness of the full cascade. In particular,
`ɣò-oxun` was rejected at the surface filter; the candidate admits
`goōn` and `gōon`, exposing SC086's pre-existing earlier branching.
Both complete accepting paths are preserved. The full candidate
remains nonfunctional and its exact input-domain inclusion still fails
on epsilon; `ḗô` also remains rejected. Adoption need not await totality
on unrelated synthetic inputs, but these qualifications cannot be
omitted or recast as a global functionality success.

Both orthographic components independently remain nonfunctional on the
closed-tier `*ɔ̆ → a / ŏ` counterexample. Unrestricted flookup controls
on this decomposed symbol do not reproduce the same lookup behaviour;
the exact ATT paths are retained, and the operational discrepancy is
not diagnosed here. It is neither evidence against the complete graph
paths nor a reason to alter phonology.

See capsule `post-sc052-gamma-01/results/{outputs,proofs}/`,
especially `factorization-difference.proof.json`,
`gamma-map.proof.json`, `regression-and-controls.json`, and
`analysis/complete-paths.json`.

## Disposition of the retained 47-block audit

The existing source-bound inventory covers 264 reachable definitions
and 47 single-comma rulesets: 19 identical shared contexts, 11 deliberate
same-centre unions, nine unconditional distinct-centre groups, three
distinct-centre/context review groups, three equal-union groups and two
deliberate trailing shared-context groups. No scan or systematic comma
replacement is repeated.

| Priority / category | Actual compiled evidence | Action |
|---|---|---|
| High: SC086 | inherent pair overlaps and additional partial-tag matches | source-led decomposition decision, not punctuation automation |
| High: `OEBreakingA`, line 2105 | both versions nonfunctional; scoping removes the long alternative in `*a*r*t` but not `*a*x*a` | assess relevant reachable contexts and short/long conditioning before proposing a correction |
| High: orthography, line 823 | `*ɔ̆` prefix-centre ambiguity survives scoping and ɣ mapping | separate symbol-boundary/representation issue; preserve complete paths |
| Review: `OEBackMutation`, line 3246 | both versions functional, but `*e*r*a` changes only in the original | historical environment adjudication required; functionality alone cannot choose |
| Review: `OEHighVowelApocope`, line 3531 | both functional; original deletes final u in `*ū*u`, scoped retains it | distinguish intended heavy-syllable conditioning before editing |
| Retain: `OEDiphthongLeveling`, line 2212 | scoped/original actual component ATT identical and functional | no demonstrated defect |
| Retain: named shared unions | final-z loss and monosyllabic-r lengthening share trailing contexts deliberately; breaking E/I and WS palatal umlaut have equal unions | no blanket comma replacement |

A component counterexample is not automatically a reachable whole-cascade
counterexample. The old compiled tests and bounded controls are retained
in `sc086-totality-bounded/evidence.zip`; the current source hash agrees.
This ranking is actionable triage, not a fresh historical adjudication
or authorisation to change any of those rules.

## Preservation, export and outstanding work

The corpus SHA-256 remains
`acecb163dffba5c20109ca4951074056a697854fa69cf1f52bc0f82142b39d62`.
Selected391 fingerprint:
`ed765acdd0ddd7417941234a65be386cb7e617967a22549cbee20ca9d5d288f6`;
original380 fingerprint:
`4a5b126eae3dadf38f6ffd50b778009d79edae40407601a7c79de3d367688ed9`.
No baseline is refrozen. Earlier capsules, failed runs, formal
counterexamples, acquisition receipts and both publications remain intact.

`review-export.tar.gz` contains only UTF-8 text: commit metadata,
bounded text patches, all changed-file hashes, the current FST, these
three reports, proof/receipt summaries and explicit omissions. It excludes
scholarly originals, OCR, images, PDFs, native binaries and bulk graphs.
Complete graph replay instead uses the separately manifested local
`evidence.zip`. The export is for independent review, not a claim that
its small summaries alone reproduce the formal proofs.

Bennett1968, Stiles1995 and Hock1973 remain acquisition requests.
Independently verified off-machine preservation of the ignored scholarly
originals remains outstanding.
