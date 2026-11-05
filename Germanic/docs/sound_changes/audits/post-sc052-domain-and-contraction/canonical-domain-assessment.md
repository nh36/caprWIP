# Canonical-domain assessment

Research only, 5 November 2026. Branch: `research/full-cascade-functionality`;
base: `efd9ec412a36aa5e9705ccacb63038c114e39fa3`. No production parser,
sound law, selected input, surface filter or publication is changed.

## Result and domain contracts

Epsilon genuinely belongs to the current canonical parser's upper domain.
The discrepancy is in the assumption that its inherited root groups are
mandatory, not in the orientation of the totality subtraction. Removing that
acceptance requires a separate parser-policy change. It does not repair
SC086 or establish totality.

| Domain | Independent definition | Appropriate claims |
|---|---|---|
| `D_raw` | `EnglishProtoInput.u`, from the actual accepted FST | Parsing functionality is proved. Output functionality and totality remain separate research questions; both fail for the present full relation. Membership is not historical validation. |
| `D_historical` | Source-licensed forms and constructions, typed by historical input variety/stage, morphological cell and independently warranted prosody | Require a valid analysis, regular development over the intended historical span and suitable OE realization. No complete implementation or global certificate for this language is claimed here. It must not be defined by successful cascade outputs. |
| `D_selected` | The 391 accepted, context-bearing `fst_input` values, including the explicitly unstressed input | All have unchanged unique finals: 383 matches and eight retained mismatches. Parsing, availability and agreement with attested targets are separate assertions. These finite results do not prove a theorem over either larger domain. |

`OldEnglishSurface` (`Germanic/fsts/germanic.txt:793–817`) explicitly calls
itself “Deliberately baggy.” It is a nonempty output-shape filter, not an
input grammar or a complete theory of OE phonotactics. Passing it does not
make synthetic `iī` an attested or historically defensible word.

The parser's governing account,
`audits/parser-formal-resolution/README.md:209–234`, expressly conserves
inherited empty/vowelless acceptances. Its future totality programme is not
an accomplished production guarantee. Thus totality on `D_raw` is a useful,
strong research diagnostic, but the documentation does not establish it as
an already satisfied software contract. Adopting it as a new requirement
would require an explicit compatibility decision, not quiet witness removal.

Acute/grave counting is insufficient to define the historical domain.
`pgrmShortVowel` and `pgrmLongVowel` admit mixed accent conventions; long
vowels do not uniformly carry a separate acute. The compound grammar
requires neither exactly one acute nor a source-licensed stem combination.
Conversely, an intentionally unstressed selected form must not be discarded
by an indiscriminate primary-accent requirement. Historical stage is an
explicit metadata axis, not something inferred from `EnglishProtoInput`'s
name; selected PROTOFORMs are not uniformly identical to citation PROTOs.

## Epsilon: actual compiled paths and source cause

Fresh immutable experiment `post-sc052-domain-03` exports the canonical
parser and both projections. Its parser ATT has SHA-256
`ceea3a0d3b9e8ae92051abad9c825ecf9df7ce317642ccbe83fb64053879b6fc`.
State 0 is final: the complete accepting path has zero arcs, empty upper
input and empty lower output. An independent exhaustive path checker
confirms this on the actual ATT. Both `.u` and `.l` accept epsilon.
`PGCellRoot` and `PGCellInput` do not.

Two independent inherited mechanisms explain it:

1. At FST lines 285–290, `pgrmStrongPlainHeavy` uses
   `(pgrmLongVowel | pgrmDiphthong)`. Foma parentheses mean optionality,
   not grouping; onset and coda may also be empty.
2. At lines 503–509, all five root alternatives in `pgrmSimpleWord` are
   parenthesized. Two can be followed by `pgrmWeakTailZero`.

The final canonical union at lines 4049–4053 deliberately retains the
unambiguous inherited-native relation. The mandatory vowel in
`PGCellRoot` does not remove that native empty branch.

The subtraction is `EnglishProtoInput.u - OldEnglish.u`: two acceptors,
correctly oriented and composed from the same declared source. The actual
closed-alphabet ATT contains no symbolic unknown/identity arcs. Its
independently checked shortest witness is epsilon, with final state 0 and
an empty accepting arc path. The full transducer independently rejects
empty upper input. No complement normalization, output projection or
epsilon-to-literal-zero conversion manufactured the witness.

Two instrumentation mistakes are preserved rather than used as evidence
for a repair. Experiment `post-sc052-domain-01` lost parameterized macro
signatures during source reconstruction and failed. In `-02`, normalized
`definition_raw` strings did not match original byte spans: its supposed
corrections were no-ops, exposed by identical source hashes. Its status is
inconclusive. Corrected `-03` preserves the macros and validates each
changed source span and parsed body before compilation.

## Separate, unadopted parser correction

The private candidate changes six parenthesis pairs to square brackets:
the one heavy-root nucleus group and five simple-root groups above.
All other optional constituents are retained. Candidate source SHA-256:
`47dfb7ca0569b4bc607b81a9ced42b60da8d73128b356218c83cba37c4de076f`.

Changing only the nucleus group still accepts epsilon. Changing only the
five simple groups leaves the compiled canonical relation byte-identical.
Changing both eliminates epsilon and every vowel-free accepted input.
Exact acceptor differences prove that the candidate adds no input strings
and strictly removes part of `D_raw`; this is not a claim that every
removed string is itself vowel-free.

The candidate parser is globally functional: 8,116 arcs, 2,986 reachable
twins, 2,914 live twins, maximum delay 1; the certificate is independently
verified. All 391 parser analyses and full output sets are unchanged.
Nevertheless its full cascade remains nonfunctional, and its exact
totality difference remains nonempty, with shortest witness `à`.
Consequently this is a bounded syntax-policy proposal, not a historically
complete input language or a global cascade repair.

## `ḗô`: different, genuine representational failure

`ḗô` parses uniquely as `*ḗ*ô`. One native factorization is a heavy root
`ḗ` plus the bare nominal weak-tail `ô` (`pgrmWeakTailVowel`, line 461).
This analysis is also accepted after the private mandatory-root correction;
the failure is not caused by an empty root.

| Physical stage | Actual representation |
|---|---|
| 1, parser | `*ḗ*ô` |
| 7, `PNWGmcLongELowering` | `*ā*ô` |
| 8–108 | `*ā*ô` |
| 109, `OldEnglishRemoveStars` | `ā*ô` |
| 110, `OldEnglishSurface` | rejection |

`OEUnstressedLongVowelShortening8` (lines 2760–2763) maps trimoric
`*ô` only after a vowel followed by at least one consonant. Immediate
hiatus supplies no such consonant. No later rule or orthographic mapping
removes the surviving `*ô`. Complete accepting-path checks confirm the
parser analysis and exhaustive full-relation rejection.

The parser permits this formal stem-plus-tail concatenation; no consulted
source establishes the corresponding historical lexeme and construction.
It is therefore an exact `D_raw` totality counterexample, not positive
evidence for extending a historical shortening law to every V+ô sequence.
It is independent of epsilon, SC086 and the surviving-ɣ spelling gap.

## Reproducibility and limits

All Foma execution used the isolated backend container, Foma
`0.10.0alpha`, commit `82f9acdef234eae8b7619ccc3a386cc0d7df62bc`,
binary SHA-256
`b2e1c7d8bc966624367cd03c9ccfad04760eac6f2e64d49403639f865b89e824`.
Accepted FST SHA-256:
`33d062fe6624a7eae3bf541dbf22a2f89eb4da101fcde5d2a4e8d702b27f41f6`.

`MANIFEST.json` authenticates `evidence.zip`. Experiment names are capsule
root directories, mirrored locally under `.capr-work/experiments/`.
See `post-sc052-domain-03/results/{outputs,proofs}/`,
`post-sc052-contact-01/results/outputs/original-full.att`,
`analysis/complete-paths.json` and the retained
`prior-research/complete-traces.json`. Positive certificates enumerate all
live twins and are replayed with `functionality.verify`; negative results
include complete accepting paths. Language differences use exhaustive
graph reachability, not the unreliable native functionality diagnostic.
No new strict production certification or historical-domain theorem is
represented by these research results.
