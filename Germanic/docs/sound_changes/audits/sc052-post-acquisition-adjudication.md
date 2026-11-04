# SC052 post-acquisition: private context-scoping investigation

## Identity

SC052, `OEVelarPalatalization`; branch `research/full-cascade-functionality`,
base `7a3fb4df`. This follow-up does not supersede the adopted historical
`sc052-adjudication.md` or authorize propagation.

## Question

Does the geminate-before-j clause share the singleton clauses' contexts
because single commas group rewrite centres into one Foma ruleset?
Independent scoped relations, compiler parsing, complete accepting paths
and corpus conservation can confirm/refute that diagnosis. A unique sampled
final cannot prove global functionality.

## Current state (before any edits)

Registry: `preoe/english_specific`, confidenceA, `REFORMULATE/SPLIT`.
The accepted class-specific articulation/cutoff and postmutation merger
remain unchanged. Physical stage62 is an executable position, not a date.
The production stop block composes k-front handling, four singleton-g clauses
and the gg-before-j clause joined by single commas, then a g-before-j rule.
FST SHA256:
`18f69deaeb2385c94d65a9599f97a96aed9da2fd3065d908e194e9ab3e6cdb0f`.
Corpus SHA256:
`acecb163dffba5c20109ca4951074056a697854fa69cf1f52bc0f82142b39d62`.
All selected inputs and context metadata are preserved.

Consulted: the accepted SC052 memo, hinge literature/book dossiers,
chronology card, Anglo-Frisian synthesis/palatal note, original full-cascade
evidence capsule, and new direct Fulk1998 card14.

## Diagnosis

Complete selected391 firing census:32 rows, the same32 named in the accepted
memo; raw before/after sets and row identities are in the repair capsule's
`regression.json`. Candidate-versus-incumbent differences: zero at all110
cumulative stages for all391 selected inputs, hence also the protected380
subset. The complete final sets preserve383 matches, eight established
mismatches, zero missing and zero ambiguous selected outputs. This is finite
regression, not a global theorem.

The global original counterexamples are retained, not re-opened:
`ggai` → `gġē`/`ġġē`; `g-géua` → `gġēo`/`ġġēo`.
The private serial/pointwise repair gives only the first output in each case.
Original gg-before-j also branches: `*g*g*j` gives `*g*ʤ*j` and `*ʤ*ʤ*j`;
both private forms give the intended complete `*ʤ*ʤ*j`.

Witness roles: ggai/g-géua are parser-valid computational counterexamples,
not attested lexical histories or chronology witnesses. The gg/j control is
an inherited-j pathway test; ng/i and singletonɣ/i distinguish classes;
g/a, ng/a, gg/a and medial k/e are negative controls. Thirteen paired
component controls are saved in `component-controls.json`. No new historical
edge is inferred from their executable effects.

### Exact cause: context grouping, not a native checker defect

The backend Dockerfile pins Foma commit
`82f9acdef234eae8b7619ccc3a386cc0d7df62bc`.
The image's compiler sources were checked against that commit:
`regex.y` SHA256
`2bf2f6204265b9241d791a92b53cdd602459627e675330586bfdcc033095aa7f`;
`rewrite.c` SHA256
`54ccbe2f3d92253b35031b9de6c5e8ff9f330ad38f73de73982d06344bc9c699`.
Installed foma SHA256
`b2e1c7d8bc966624367cd03c9ccfad04760eac6f2e64d49403639f865b89e824`.

In `regex.y`128–145, `add_rewrite_rule()` attaches accumulated centres
and contexts to one ruleset and clears both. The single-comma productions
at270–277 and288 add centres/contexts without closing that ruleset;
double-comma at293 closes it. `rewrite.c`132–150 unions centre cross
products, then193–203 restricts each centre with its **ruleset's** contexts.
Thus the original g and gg centres share the union of all listed contexts:
the gg replacement can occur before a front vowel with no j, while the
singleton can occur before j. Overlapping centres then permit distinct
coverings. This is actual comma/ruleset semantics, not evidence that the
native functionality diagnostic misclassified a functional SC052.

Miniature `[a -> b || _ e, a a -> b b || _ j]` demonstrates the same
ambiguity on aae (abe/bbe) and aaj (abj/bbj). Serial and pointwise versions
are independently globally functional. Complete accepting-path replay is
stored in `verified-paths.json`; native outputs and actual ATT relations
are preserved. The latest proof's chosen miniature witness may be aaj:
both counterexamples remain valid.

## Literature

Accepted direct source evidence is reused explicitly:
Fulk2018 pp.130–132 for singleton fricatives versus gg/ng stops,
Ringe–Taylor2014 pp.203–214 (merger p204),
Hogg1979 pp.102–111 (key/day p105 and objection),
Laker2007 pp.166–168,175–184 for articulation/assibilation distinctions.
Fresh Fulk1998 pp.145–149,153–154 corroborates separating early reversible
articulation from assibilation and limits common-inheritance claims. It does
not supply a new gg/j conditioner or resolve key/day merger.

Those sources justify the existing historical classes and conditioners;
they do not dictate Foma punctuation. The published comment and accepted
gg/j specification already intend complete geminate conversion before j.
Restoring distinct context scope is a computational convention implementing
that retained intent, not a new historical date or exception.

## Historical analysis

Stage/scope: retain the accepted `preoe/english_specific` characterization,
without excluding possible earlier shared allophony. No stage is read from
the SC name, physical position or new native result.
Conditioning: retain ordinary front-vocalic and j environments, class
distinctions, independently encoded stress/boundaries, and the existing
productive cutoff. No lexical-ID, grammatical category or output preference
condition is introduced.

The formal counterexamples reveal overgeneration of the original proxy,
not positive evidence for analogy. No analogy is proposed. A later residual
counterexample belongs to a separate operation, not a counterexample to
the source-supported SC052 class distinction. All historical chronology
edges are retained; no new `stage_entailed` or
`independently_demonstrated` edge is promoted.

## Verdict

Retain production unchanged. Context-scoping repair is a private,
scientifically neutral proposal pending a controlled decision. The
incumbent registry verdict remains:

Registry-verdict: SC052=REFORMULATE/SPLIT

This line records the already adopted historical verdict, not new
authorization. Serial separation and a pointwise equal-centre formulation
have globally functional actual compiled components. Their wrapper and
stop ATT files are byte-identical after compilation on the recorded closed
alphabet. The actual repaired cumulative physical-stage62 relation also
has an independently verified global certificate, despite native result0.
A separately compiled minimal punctuation candidate is evaluated in the
repair-capsule README; its result is not assumed from syntax alone.

## Propagation (only after verdict)

None: no production FST, corpus, registry, protected baseline or published
definition changed. The proposed minimal source patch is one extra comma
before the gg clause, delimiting its contexts (` , ` → ` ,, `); exact
candidate/source comparisons and compiled certificates belong to the
capsule. Any adoption still requires its own controlled scientific decision
and protected source-bound validation.

Tests cover definition-span replacement with comment semicolons, exact
one-character scoped mutation, isolated proof loading and accepting-path
replay. The parser proof itself is unchanged. Fingerprint targets are not
used to select a history; complete selected output conservation is an
observed result.

## Residue

The repaired complete cascade is **still nonfunctional** over the actual
canonical parser domain. Its independent full-relation proof provides
`ò-oxun` → `oōn`/`ōon`. That witness first branches at physical-stage100
SC086 `OEContraction`, after `*o*o*o*n` admits contracting either adjacent pair.
The preceding physical-stage99 relation is independently globally
functional; the following relation is independently nonfunctional.
This is a certified boundary pair, not a claim that every intervening
earlier prefix was freshly certified or that contraction has been repaired.

The input has a grave-marked first member, not an explicit primary acute.
It is accepted by the adopted parser; it must not be silently removed to
obtain a theorem. If “fully specified” instead requires an independently
defined primary-accent restriction, that domain and its own functionality
remain to be certified. Positive controls `ó-oxun`, `ó-óxun` and `ó-òxun`
do not share the same ambiguity. This qualification is not a new parser
decision.

Totality remains independently refuted by parser-valid `ɣó`; see
`full-cascade-functionality/totality-followup.md`. No contraction rewrite,
parser restriction or surface patch is adopted in this bounded SC052 pass.
The complete relation, paths, attempts and limitations are preserved rather
than calling an incomplete traversal a proof or issuing a general DEFER.
