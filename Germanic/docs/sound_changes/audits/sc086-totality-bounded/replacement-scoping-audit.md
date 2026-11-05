# Old English replacement-block inspection

This is a risk inventory, not authorization for a punctuation sweep or a new
historical adjudication. The actual `OldEnglish` dependency closure contains
264 definitions and47 single-comma rulesets at source SHA256
`33d062fe6624a7eae3bf541dbf22a2f89eb4da101fcde5d2a4e8d702b27f41f6`.
The capsule's `replacement-block-inventory.json` lists every centre, context,
literal width and source line.

| Classification | Count |
|---|---|
| identical shared context | 19 |
| same centre, deliberate context union | 11 |
| unconditional distinct centres | 9 |
| distinct centres/contexts requiring review | 3 |
| equal context unions per centre | 3 |
| single trailing shared context | 2 |

Shared trailing contexts are deliberate in
`MonosyllabicFinalZLoss` (1378) and
`PNWGmcMonosyllabicFinalRLengthening` (1204).
`OEBreakingE` (2120), `OEBreakingI` (2136) and
`OEWsPalatalUmlaut` (3282) have equal context unions per centre.
The corrected SC052 Stops rulesets and the separate KFront/fricative blocks
retain legitimate same-centre context unions.

Five actual original/scoped components were compiled with the pinned Foma
binary and independently checked as complete finite-state relations. The
scoped variants are diagnostic, not proposed production corrections:

| Risk | Definition / line | Actual result |
|---|---|---|
| high, context pooling | `OEBackMutation` /3246 | both functional; original changes `*e*r*a` to `*eo*r*a`, scoped does not; the ae/a context can broaden the e-before-u centre |
| high, residual ambiguity | `OEBreakingA` /2105 | both nonfunctional; original `*a*r*t` has short/long breaking, scoped only short; scoped `*a*x*a` still branches |
| high, context pooling | `OEHighVowelApocope` /3531 | both functional; original deletes final u in `*ū*u`, scoped retains it; the direct-long i-context pools into u/nasal-u |
| medium, string-prefix matching | `OldEnglishOrthography` /823 | original/scoped relations identical but nonfunctional on `*ɔ̆`: `a` versus `ŏ`; persists independently of the gamma mapping |
| low, intentional string distinctions | `OEDiphthongLeveling` /2212 | original/scoped relations identical and functional; `*eu` and `*e*u` are intentionally distinguishable |

Mixed known literal widths occur in `OEContraction` (3705),
`OEDiphthongLeveling`, `OldEnglishOrthography` and `OldEnglishRemoveStars` (880).
Mixed length alone is not proof of an error. SC086's isolated pair overlap
branches without any pooled context; splitting commas cannot cure it.

These results separate three issues: pooled contexts can broaden a functional
relation; substring centres can introduce competing outputs; genuine pair
overlap can branch even with one rule. Component ambiguity is not automatically
reachable from actual parser inputs. In particular, the independently certified
cumulative physical99 relation remains functional after SC052, so these
component findings do not establish an earlier full-domain functional boundary.

No punctuation change beyond the separately controlled SC052 repair is adopted.
Historical conditioning and source-backed near-neighbours must be adjudicated
before any further change. Stored positive certificates and competing complete
component paths are replayable; native flags alone are not the evidence.
