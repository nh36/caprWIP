# SC086: functional boundary and historical-domain decision

## Identity

SC086, `OEContraction`; research branch `research/full-cascade-functionality`,
reference `e842319430f9f41ac3cb9f1beb8173e1c3d07fb8`. This is a bounded
investigation, not a propagated adjudication. The compiled source includes only
the separately controlled SC052 comma correction, SHA256
`33d062fe6624a7eae3bf541dbf22a2f89eb4da101fcde5d2a4e8d702b27f41f6`.

## Question

Does SC086's ambiguity require accidentally shared replacement contexts, and
does independently motivated stress screening remove it? Refutation requires
an actual competing pair of accepting paths, not a native checker flag.
Historical acceptability requires evidence independent of those paths.

## Current state (before any edits)

The registry characterizes SC086 as Old English, English-specific, and
unadjudicated: "OE intervocalic h-loss and subsequent vowel contraction; both SCs
share OE stage." Its owning reader is `reader_facing/086-contraction.md`;
the cluster dossier is
`book_dossiers/079-087-final-j-contraction-and-metathesis-cluster.book-dossier.md`.
No registry field, chronological edge or production definition is changed here.

The executable has 27 unconditional pair-replacement clauses at physical
cumulative stage 100; physical stage 99 is independently functional on the
actual parser domain. Selected inputs and their stress/context annotations
remain exactly those of the accepted391 population. Physical position is not
an independently established historical date.

## Diagnosis

The isolated relation `[*o *o -> *ō]` already maps `*o*o*o` both to `*o*ō` and
to `*ō*o`. For every clause A+B in the complete 27-clause relation, the
constructed A+B+B triple has two outputs: A+B contraction competes with the
following B+B contraction. This does not claim that every clause overlaps
itself in isolation. Thus the defect does not require shared contexts or
mixed-length grouping.

There is a second, distinct problem: braces denote character strings, not
indivisible vowel tokens. A centre ending in `{*e}` can match the beginning
of `{*eo}`. The private candidate appends the single shared right context
`|| _ [{*} | .#.]` to the final clause. This intentionally guards all centres.
It blocks partial-token matches but does not disambiguate overlapping whole
pairs. Its source hash is
`d0e09f092965715477a4f4636966fb9629be61bda7694e8bdd40c1bfa26b194a`.
It conserves all391 selected final output sets; it is not a complete repair.

The evidence capsule supplies complete native 110-component traces, matching
the actual complete network, and accepting arc paths in the complete exported
relation:

| Input | Immediately before SC086 | Immediately after SC086 | Complete outputs |
|---|---|---|---|
| `ò-oxun` | `*o*o*o*n` | `*o*ō*n` / `*ō*o*n` | `oōn` / `ōon` |
| `é-ìwi` | `*i*i*i` | `*i*ī` / `*ī*i` | `iī` / `īi` |
| `éu-òxun` | `*ēo*o*o*n` | `*ēo*o*n` / `*ēo*ō*n` | `ēoon` / `ēoōn` |
| `ái-èxun` | `*ā*eo*o*n` | `*ā*ēo*n` / `*āo*o*n` | `āēon` / `āoon` |

These are synthetic computational witnesses, not attested words or established
Proto-Germanic reconstructions. The second explicitly marks both heads: grave
removal at physical46, w-loss at65 and mutation at67 leave three i-tags.
Consequently, adding a primary accent alone does not establish functionality.

The complete canonical391 firing census, including its legacy380 members, is:

| Selected lexeme | Before | After | Role |
|---|---|---|---|
| flee | `*f*l*ēo*a*n` | `*f*l*ēo*n` | live application |
| slay | `*s*l*ea*a*n` | `*s*l*ēa*n` | live application |
| ten | `*t*éo*o*n` | `*t*ḗo*n` | live application |
| three | `*θ*r*i*i*e` | `*θ*r*ī*e` | live application |
| toe | `*t*ā*e` | `*t*ā` | live application |

All five concepts belong to the protected legacy380 population. This is the
complete current canonical firing census, not a new experiment on refrozen
legacy inputs. The underlying trace excludes its separate raw-fidelity appendix.
In particular, three (2254) has a triple tagged-vowel sequence already in an
accepted selected derivation, though only its first pair contracts. Its mature
model entry cites Campbell §683 and Fulk2018 §10.1 for the target *þrīe* and
records `θrije > θriie > þrīe`. A blanket formal ban on three adjacent tagged
vowels would therefore discard an accepted derivation. This does not establish
that each tag denotes a separate historical syllabic nucleus. Repeated
application to a fixed point would additionally absorb `*ī*e`, changing this
accepted target; it is not an innocent implementation convention.

## Literature

The existing SC086 reader, cluster dossier and accepted chronology were retained.
Direct page images checked: Campbell1959 p.30 §§71–72 (initial stress and
preverbs), p.34 §§87–89 (compound half-stress and qualifications), p.98 §234
(accented/unaccented hiatus, diphthongs, exceptions and absorption), pp.186–187
§§461–465 (h-loss, boundaries and stress qualifications); Ringe–Taylor2014
pp.314–316 §6.9.3 (h-loss and contraction, including dialect qualifications).
These support conditioned contraction, not an arbitrary leftmost/rightmost
resolution of every constructed triple. The executable comment's reference to
Ringe–Taylor §6.6.1 should be corrected to §6.9.3, pp.314ff, in a separately
declared editorial change; it is not silently corrected here.

The source-directed *fehiwi* probe is a useful negative finding. Ringe–Taylor
pp.315–316 gives *fehiwi > fehē > feohe > fēo*. The current `féxiwi` probe loses
the relevant final i early and arrives before SC086 as `*f*íe*ç*eo*w`, finally
`fieheow`. It establishes neither a triple witness nor an accepted account of
that cited history. No corpus row or rule is changed to force it to fit.

## Historical analysis

Stage and scope remain the registry's Old English/English-specific claims.
Stress, syllabification and boundary conditions must be specified independently
of problematic outputs. No positive evidence for analogy is introduced.
No new chronology edge is proposed: the traces show model-local order only.

The exact experimental domains are recorded in the capsule's worker:
`HMarked` requires one explicitly marked primary head after an optional parser
prefix; `HGeneral` additionally permits unaccented long/nasal/diphthong heads;
`HProsodic` requires a single primary head and, for compounds, a marked secondary
head. All intersect the actual parser language. These are stress-motivated
screens, not complete historically certified phonotactic grammars.

Regular-language certificates and complete witnesses give:

| Actual relation | Independent result |
|---|---|
| broad cumulative physical99 | functional (existing repaired certificate) |
| broad physical100 | nonfunctional: `o-oxun`, two complete paths |
| HProsodic physical99 | functional; 193159 arcs, 710128 reachable twins, maximum delay5 |
| HProsodic physical100 | nonfunctional: `é-ìwi`; 198667 arcs |
| guarded HProsodic physical100 | nonfunctional: the same witness |

The positive HProsodic99 ATT hash is
`521193764b1fd6803297b2d95d46a236fef4ccc452177682b22b1dd75a75c040`;
the negative HProsodic100 hash is
`7111c8b6ad667243b9f9c48f259238b52da94adfec8146c76c30c967f982b79b`.
Certificates cover the entire compiled restricted relations, not bounded word
enumeration.

HMarked and HProsodic include358 selected inputs and exclude33; HGeneral includes
390 and excludes the explicitly unstressed sentence-context *you* (2326).
Acute-only screening incorrectly discards ordinary long-head inputs including
beech1942, blood1952, book1955 and bosom1957. Absence of an acute is not absence
of historical primary stress. Quantity, stage, context, clitics and compound
boundaries cannot be collapsed into a universal one-acute requirement.

A separate32-case probe uses nonempty onsets and long/diphthong first heads
`réu/rái/rḗ/rḯ`, followed by `à/è/ì/ù + x + un/an`. All32 parse; six retain
partial-centre branching, e.g. `rái-èxun` gives `rāoon/rāēon`. This avoids the
illicit short-o-root premise of the original witness, but still does not make
the constructed roots attested words. No attested lexeme requiring a choice
between two overlapping whole-pair contractions has been established.

## Verdict

DEFER a production SC086 repair and any replacement historical input grammar.
The machine-readable propagation line is inapplicable: this investigation
does not replace the registry's `unadjudicated` value. Whole-token matching is
a well-defined candidate representation repair, but is insufficient for
functionality. A contraction policy or historical domain requires a separate
scientific decision with independently supported stress, segments and nuclei.

## Propagation (only after verdict)

None. No SC086 punctuation, parser restriction, baseline, corpus, chronological
edge or publication is changed. The private guard has zero391 final differences.
The independent evidence replayer checks complete certificates and accepting
paths. It is not strict production approval of the guard.

## Residue

Resolve the representation of nuclei/glides and long diphthongs; identify
source-backed critical triple histories; account for valid unaccented long
heads and unstressed contexts. Do not select one output or exclude a witness
merely to obtain a theorem. Keep totality and SC052 adoption separate.
