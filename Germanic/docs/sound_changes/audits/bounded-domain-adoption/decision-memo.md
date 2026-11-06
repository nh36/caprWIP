# Decisive closeout: canonical input and surviving velar spelling

Scientific commit: `c9b2527979603b0a881ef3f134f22eff291a6915`, on `research/full-cascade-functionality`.
Both bounded changes share the certified `Germanic/fsts/germanic.txt` SHA256
`c51c3f440e48c320968dd7a12c3b9995c2b16f5e766ef075f16f7af8eba76d3d`.

## Decisions

| Question | Disposition |
|---|---|
| Empty canonical input | Corrected and certified. Six optional native grouping pairs now require their nucleus/root. Actual canonical, native and productive ATT reject epsilon; no blacklist or output-success filter was introduced. |
| Surviving velar fricative | Adopted: `{*ɣ} -> g,` in terminal `OldEnglishOrthography`. `ɣó -> go` is repaired; already palatalized controls and all selected outputs remain unchanged. This is spelling projection, not phonetic stop merger or a new sound-change date. |
| SC086 | Unchanged; this ambiguity inquiry is closed. No independently supported reconstructed historical input with competing outputs was established among the 391 selected inputs and licensed controls. Confirmed full ambiguities use artificial, independently unlicensed constructions. This is a bounded historical judgment, not a universal historical-functionality theorem. |
| Selected derivations | All 391 unique previous analyses, final outputs and 110-stage histories are conserved: 43,010 unchanged stage comparisons. There are 383 attestation matches and the same eight mismatches: buck, fire, fowl, rust, straw, tap, wolf, wool. No target, selected cell, input-stage metadata or baseline was refrozen. |

The [SC001 memorandum](../sc001-lexical-nucleus-adoption.md) identifies the two independent native empty branches: optional heavy nucleus and optional simple-word roots; the productive branch already rejected epsilon. The [SC092 memorandum](../sc092-adjudication.md) documents all consonantal contexts and spelling qualifications. Campbell1959 p21 §50(4), p180 §446, and RingeTaylor2014 p4 support written g for surviving fricatives, without asserting stop realization or invariant final-g spelling across periods. Registered originals are `docs/references/campbell_old_english_grammar.pdf` and `docs/references/ringe_taylor_linguistic_history_vol2.pdf`; restricted holdings are not exported.

## Output contract and retained limitations

`D_selected` is the 391 actual context-bearing model inputs, with independently recorded stages and attested targets. They must parse uniquely and have unique outputs; agreement with attested OE is independently evaluated. `D_historical` requires independently justified stems, constructions, accentuation and historical applicability; inputs to which the account applies should have unique outputs. No global historical language or global historical-functionality certificate is claimed, and that language is not defined as the compiled OE domain.

`D_raw` is the corrected parser language, not an inventory of possible Proto-Germanic words. Parser functionality is globally certified there. Complete-cascade functionality and totality remain false and are not adoption conditions for these bounded fixes. Final accepted outputs still pass `OldEnglishSurface`; this filter does not license historical inputs.

Actual current full ATT SHA256: `651e15cc483eb2fbd558c36e68a4eb81f289221807145344482b1a8b03f1751e`. Complete paths retain `é-ìwi -> iī / īi` and newly exposed `ɣò-oxun -> goōn / gōon`. Exact, correctly oriented domain subtraction remains nonempty, with witness `à`. `ḗô` still parses as `*ḗ*ô`, becomes `*ā*ô` at stage 7, remains `ā*ô` at 109 and first fails at surface stage 110: the relevant shortening requires an intervening consonant, absent here. No historical lexeme/construction was established for that input.

For SC086, `é-ìwi` loses secondary stress at 46 and w at 65, creating `*é*i*i`; umlaut at 67 yields `*i*i*i`. H-loss at 99 does nothing. Overlapping centres at 100 yield the two surviving outputs. Acute plus grave does not establish historical stems or compound inflection. Contraction is not restricted to h-loss: Campbell1959 pp98,100 and RingeTaylor2014 pp259,318 also discuss inherited/w-loss hiatus. The [preserved scientific report](../post-sc052-domain-and-contraction/sc086-scientific-report.md) distinguishes the supported flee/slay/ten/toe controls, the separate draw control, and three's normalization proxy.

No directional historical ordering, h-loss-only restriction, lexical exception or application tie-breaker was adopted. The functional comparator remains an explicitly computational research artifact. Source-staged niwi/gliwi and ū+a coverage observations, and preexisting unrestricted orthography `*ɔ̆ -> a / ŏ`, remain acknowledged; they are not demonstrated competing outputs of a supported reconstructed historical word.

## Exact certification

Compiler: Foma 0.10.0alpha, commit `82f9acdef234eae8b7619ccc3a386cc0d7df62bc`, executable SHA256 `b2e1c7d8bc966624367cd03c9ccfad04760eac6f2e64d49403639f865b89e824`; execution was inside the isolated backend.

| Complete certificate | ATT SHA256 | Verified result |
|---|---|---|
| Canonical parser | `4ede972d3b60683d2897134c72b668a8b4eac3f730e69ae792293678d296e452` | 8116 arcs; 2986 reachable twins; 2914 live; delay 1. Complete independent closure/delay verification passes. |
| Closed-tier surviving-ɣ map | `1c2b88b9b552f60990e46667315372136305e2b263b9fb763ac2b1d483fd26b1` | 106 arcs; 13 reachable twins; 11 live; delay 0. Current orthography equals prior orthography composed with this deterministic map on the declared tier; symmetric path difference empty. |

The source's native builder reports functionality 0/unambiguity 1, versus 1/1 when a fresh process loads its identical saved parser. The ATT is byte-identical to the independently certified graph. Both transcripts and the first failed instrumentation assertion are retained, not suppressed or promoted into phonological evidence.

Official coordinated `SC001 --finalize` and `SC092 --finalize` passed source-bound preflight, frozen-archive and protected-baseline checks. Required validation completed:

| Level | Actual result |
|---|---|
| A | 38 passed: bounded-adoption, lexical-gate, SC036, parser-proof tests and the dependent SC035 preservation selector below. |
| B | `adjudicate.py --refresh`: CONTROL PLANE CLEAN; `adjudicate.py --status`: STATUS OK. |
| C serial | `python3 -m pytest -q --ignore=test_evidence_interface.py --validation-mode=full --fresh-isolated-definitions`: 1914 passed, 5 historical-replay skips, 9635 subtests passed. |
| C exclusive | `python3 -m pytest -q test_evidence_interface.py --validation-mode=full --fresh-isolated-definitions`: 26 passed. |

Focused selector, from `Germanic/tests/`:

```text
python3 -m pytest -q test_bounded_domain_adoption.py test_lexical_witness_input_gate.py test_sc036_adjudication.py test_parser_functionality_proof.py test_sc035_prosody.py::test_context_lifting_preserves_the_other_segmental_rule_kernels
```

The failed first strict attempt (1913 passed, one stale expected-definition inventory, 5 skips, 9635 subtests) is preserved. Its sole correction permits the separately pinned SC092 spelling clause; no SC035 rule, context, historical account or verdict changed. Three historical delta inventories now rely on exact independent pins, not broad exceptions.

`evidence.zip` and `MANIFEST.json` preserve 51 text members: complete graphs/certificates, current whole-relation paths, 391 regression and compiler receipts. `certification.zip` and `CERTIFICATION_MANIFEST.json` preserve the final COMPLETE journal, exact argv/JUnit/logs, earlier failed receipts, source declarations and byte-for-byte binding of every tested worktree file to the scientific commit. No copyrighted holdings or native compiled binaries are included.

## Preservation and stopping point

SC052 and its 320-page reader revision remain closed at `529eeaa5864d37d2f67e54ae003247cb21421daa` and `efd9ec412a36aa5e9705ccacb63038c114e39fa3`. The three reports and compact text-only review export were independently committed/pushed as `7e6023eda8a52df8916181aa98bbd935f331d069`; new immutable evidence was committed separately before propagation. Both distinct 320-page PDFs and prior certifications remain preserved. Reader prose/code are unchanged; no full book render was run.

The artifact graph alone refreshed canonical projections. Its native interaction matrix changed one diagnostic cell, RootNounNomZLoss × PNWGmcPreconsonantalXLoss; no chronology SOURCE edge changed, and that native result is not promoted into history or an independent theorem. Four accepted cells, SC035/SC052/SC114, Fulk–Seiler discussions, prospective find classification, original-380 protections and acquisition/backup residues remain unchanged. The 47-block audit was not repeated. `update` remains `8f7713c39f26a7f81ef04d29d54070f1b83ab0e0`.

No further synthetic-domain investigation is required to close this assignment.
