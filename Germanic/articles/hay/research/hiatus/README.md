# Hiatus resolution experiments

Article intake `4fc313d19a52e5b6471afcb664b41bb797d70e98`; frozen
canonical/A/B2 source and runner `113101ac5f169b589e1a9647cdf24d32cdd4d919`.
The article worktree had no tracked changes; existing untracked
`.playwright-mcp/`, `comparative_followup/run_obliques.py` and
`Germanic/tests/test_sc047_finite_receipts.py` are out of scope.
Cycle 22 `DRAFT.md` and PDF remain fixed (PDF SHA-256
`75968371a1fcc8d998c41afabb33c10e6ba7a9d3d7431c86956bc569fcb3d335`).
The adoption worktree is read-only. No production model, target, corpus
row, certificate or publication artifact belongs to this experiment.

## 1. Historical comparison fixed before execution

The [historical manifest](historical.tsv) separates the independently
motivated input from its experimental encoding. Blank `submit` means
the evidence does not justify a full-cascade input at that stage;
it does not mean parser rejection. Forms labelled PWGmc or pre-OE
are explicitly later inputs; a run through the proto parser with
these spellings is an encoding test and may reapply earlier changes.
The accent on `submit` marks root stress, not length. `#` in the
environment column is a word edge, `+` a morphological boundary,
and `.` syllable separation. The first vowel is stressed, the second
unstressed except where otherwise stated. Source locators give the
reported forms and attribution; this is not a new manuscript census.

The source checks use Ringe and Taylor (RT) §§2.1, 3.1.5, 5.2,
6.2, 6.7.1 and 6.9.3; Campbell (C) §§120, 234–245, 405–406
and pp. 327–328; Hogg (H) §§3.19, 5.129–154; Luick §243 and
Sievers–Brunner (SB) §§127–135, 174. Compare the earlier
[source dossier](../REGULAR_SURVIVAL.md) and [Cycle 9](../../RESEARCH_MEMO_CYCLE9.md).
The Early Mercian ‘strew’ spellings are not securely assigned to
the weak verb (Pheifer §59.2 n. 1), and the Mercian *strēn* is
an independent **nasal** comparator if the derived *-in-* stem
is correct; it is not evidence that all surviving controls have
dental stops. The apparently Anglian oblique ‘river’ can continue
inherited *-i* or be formed to a contracted nominative; neither
the shortness of its input nor its role as a final contraction
control is unconditional. RT's staging of ‘knees’, ‘trees’ and
‘claw’ places final gliding early; the corresponding Hogg account
uses final back-vowel hiatus. Both yield a diphthongal comparison,
not independent proof of a short vowel plus consonantal coda.

Campbell §§243–245 distinguishes typically West Saxon loss before
þ, d and n, some Anglian and Kentish outcomes, and sporadic loss
before l. Retained clusters and analogical back-g forms must be
kept separate. These are comparison processes, not proof that
the *i* of early Anglian post-*w*-loss forms first became a
consonant. No new chronology edge is asserted.

The old `direct_cell.foma` runs stipulated post-umlaut forms
through small, hand-written transductions. Its 14/14 result checks
those rules and expectations, including a known exception classified
as such; it does not check proto admission, the creation and survival
of hiatus in a full cascade, or that its unrestricted contraction
ever applied to final *he.i*.

## 2. Frozen full-cascade execution

From the repository root, executed:

```sh
bash Germanic/articles/hay/research/hiatus/run-container.sh \
  > Germanic/articles/hay/research/hiatus/baseline.json
```

The launcher reads the exact adoption commit using `git archive`,
extracts only into a private backend `/tmp` directory, and runs
Foma 0.10.0alpha there. It does not use or replace mounted binaries.
The [execution record](baseline.json) gives the FST and input-manifest
hashes, full component orders, parser output, all changed stages,
identity or change before/after each named operation, the input to
orthography, and final output for every submitted form. It runs the
complete physical sequence through surface filtering, using the
authoritative compiler and per-component lookup from `sc047_models`.
As a frozen identity check, each of the three orders reproduces all
394 archived diagnostic endpoints, without rescoring or recertifying
anything. The historical probes are a separate batch. Of 49 inventory
rows, 37 have submissions; 29 are admitted and eight rejected in
each model. Twelve rows with no submission remain unrun, not failed.

| Class | Executed comparison and interpretation |
|---|---|
| ‘Hay’ | A admits `xáwją`, removes the labial at `OEWLossBeforeI`, and reaches the orthography boundary as `*ç*e*i`; `hei` serializes separate vowels. Canonical and B2 give *hīeġ*, consistent with the West Saxon high-vowel comparison, not a reconstruction of Vespasian quantity. Protected genitive/dative probes render *hīeġes/hīeġe* in all three; projected outputs are not attested donor cells. |
| Identical hiatus and long controls | A gives *glī*, with `SC047FinalIi` visibly active; both other models give *glīew*, a different stem history. All give *sǣ, ǣ*, which do not discriminate deletion from contraction. No compound was fabricated for *nī-*. |
| Short nonfinal post-labial hiatus | ‘Flock’ and ‘couch’ are parser gaps. A/B2 *ġeciþ, ġecid* diverge after successful *w*-loss: `OEUnstressedEIContraction` deletes the root *e* in its executable context. The canonical model takes a different nucleus path earlier (*ġecēaiþ, ġecēaid*). A/B2 retain hiatus in *streid*, not contracted *strēd*; the verse comparator may itself preserve hiatus. Canonical *strēaid* diverges before loss of *w*. The preterite submissions end in unadmitted tails, so they do not independently confirm the participle's problem. |
| Other post-labial outcomes | *Ġiereþ* and *ġierwan* reproduce the expected loss/retention contrast; the preterite is unadmitted. The pillow loan input is also unadmitted. Long-sequence *cnǣiþe/crǣiþe* lose *w* but do not match the w-less historical long-vowel relics; neither mere spelling nor Anglian smoothing explains away the residual *i* and ending. ‘Ewe’ lacks the required stem transfer in its submission, and ‘itch’ is a documented exceptional form, not a scoring target. |
| Back-vowel and *h*-loss comparisons | *Clēaw, cneowu, treowu* retain *w* or lose only the following vowel; none models the relevant back-vowel incorporation. *Slēan, tēon* succeed. *Seohwan* retains *hw* and is a discrepancy even against the West Saxon comparator, conditional on the submitted inherited input; *slieeþ* is distinct both from contracted Anglian *slēð* and the recorded West Saxon syncopated form. This cannot be attributed to an *e.i* repair in isolation. |
| Palatals and negatives | *Reġn, þeġn, wæġn, freġnan* retain the palatal; retention is attested and does not model the reported contracted variants. *Weġ, dæġ, īeġ* reproduce controls without post-*w*-loss hiatus. Context and not simply spelling determines their value. |

The eight rejected spellings are `áwidī`, `stráwinu`, `gakáwidē`,
`stráwidē`, `lḗwidē`, `gárwidē`, `púlwin` and `brégdaną`.
The execution record,
not the historical endpoint, is authoritative for parser acceptance.

## 3. Stage-local diagnosis

The [local inputs](local.tsv) begin immediately before a named
component, not at `EnglishProtoInput`. A successful suffix trace
cannot repair or count as a successful full historical derivation.
These probes are kept apart from the pre-execution inventory.

| Executable component | Relevant behaviour in the frozen source and full traces |
|---|---|
| `EAFBrightening` → `OEIUmlaut` | A changes stressed `*á` to plain `*æ`, then `*e`, in ‘hay’, ‘call’, and ‘strew’. This is the first **representational** loss of stress marking, not historical destressing. A rule requiring `*é` alone would miss these inputs. The prefix marker `*ᶠ` is not a vowel-stress bit and is not present in every relevant word. |
| `OEWLossBeforeI` | `Ctx` deletes noninitial `*w` after a vowel and zero or more consonants before `*i` or `*ī`. A creates `*e*i` in ‘hay’ and ‘call’, and `*ie*r*i` in ‘prepare’. The latter is not hiatus. |
| `SC047FinalIi` | A/B2 insert `*í*i` > `*ḯ` at the word edge immediately after *w*-loss. A's ‘glee’ fires; plain `*e*i`, `*é*i`, and nonfinal sequences are outside this rule. |
| Weight, high-vowel loss and lowering | `OEWeightMarkers` and `OEHighVowelApocope` do not delete the observed A hiatus in ‘hay’, ‘call’ or ‘strew’. The latter rule also erases the word-initial citation compound marker `*ᶜ`; it is not an internal boundary token. `OEMedUnstressedILowering1` requires intervening consonants, so it lowers *i* in ‘prepare’ and in ‘strike’ before *h*-loss but not hiatus *i* in ‘hay’. The second lowering component restores *i* from *e* before *ng*, not in generic hiatus. |
| `OEJLossAfterHeavy` and `OEIntervocalicJVocalization` | The former removes `*j` after a heavy configuration ending in consonants, not a preconsonantal postvocalic `*j` in `*e*j*d`. The latter can turn an intervening `*j` between vowels into `*i`; a glide probe followed by another vowel can therefore be undone at an early placement. Final `*j` is neither of those environments. |
| `OEUnstressedEIContraction` | Implements `*e` deletion after V+C⁺ before `*i`. It is not lengthening or a generic remedy: in the prefixed ‘call’ probes its left context reaches the **root** plain `*e`. It leaves final ‘hay’ alone. |
| `OEHLoss` and `OEContraction` | `OEHLoss` removes intervocalic `*x/*ç` under `FootCtx` and clears `*ᶠ`; retained `*x*w` in ‘see’ is not intervocalic. `OEContraction` contains explicit unlike combinations and identical-vowel pairs, but no `*e*i` or `*é*i` clause. `*ie*e` in ‘strike’ is also unhandled. |
| Merger and rendering | `OEPalatalFricativeMerger` changes `*ʝ` to `*j` before orthography; `OECjCleanup` only simplifies `*ʤ*j`. `OldEnglishOrthography` renders `*j` as ⟨ġ⟩; stripping the internal marker from `*e*i` gives ⟨ei⟩ without glide formation. |

These are physical component positions, not historical dates. In A
(one-based) labial loss is 70, high-vowel loss 81, the two lowerings
95–96, heavy-context *j*-loss 100, intervocalic vocalization 103, the
unstressed contraction 104, *h*-loss 106, contraction 107, and the
palatal merger 111. In particular:

- Canonical ‘call’ and ‘strew’ first leave the short-root comparison
  at `OEAwLongDiphthong`; ‘hay’ diverges on the protected stem path
  before A's apocope and final glide vocalization. The other models
  cannot be treated as running the same hiatus input.
- In A ‘strew’, contraction is the first missing operation **if** the
  target requires a contracted vowel; the verse does not make that
  target obligatory. In ‘hay’, the same identity leaves the intended
  alternative (short glide or contracted long nucleus) unimplemented;
  ⟨ei⟩ does not select between histories.
- In ‘know’ and ‘crow’, successful *w*-loss leaves `*ǣ*i`; the
  later lowering acts on the **ending after** the dental, not the
  hiatus vowel. There is no matching clause at contraction. Neither
  the initial vowel's quality nor the extra ending is repaired by
  an operation on short `*e*i`.
- ‘Claw’ first takes a long diphthong path at `OEAwLongDiphthong`
  and loses the high vowel rather than *w* at HVD. ‘Knee’ and ‘tree’
  first reach the potential environment at `PNWGmcFinalLongORaising`,
  but lack labial loss before *u*; `OEBreaking` gives a competing
  *eo* nucleus before the later loss stage. ‘See’ has `*x*w`, which
  blocks the existing intervocalic environment; ‘strike’ already
  has `*ie`, not smoothed *e*, after umlaut, then has `*e`, not
  `*i`, after lowering.
- The palatal-cluster controls reach `*ʝ` before the late merger;
  there is no corresponding pre-dental deletion with lengthening.
  Their retained outcomes are valid controls, not failures unless
  the intended target is the separately documented loss variant.
  ‘Ewe’ lacks its necessary paradigm input before any phonological
  operation; ‘itch’ enters ordinary *w*-loss despite its documented
  exceptional retention. Neither is clean evidence for the
  conditioning of hiatus resolution.

All 20 inputs were executed in each model; all 60 ordered suffix
traces were checked against the manifest and the frozen component order.
The [receipt](local.json) records every before/after state.

| Injected comparison | Result and limit |
|---|---|
| ‘Flock’, ‘couch’, ‘strew’ | Labial loss creates hiatus as intended but leaves *eide, streinu, streide*. ‘Flock’ lowers the separate final *i*; ‘couch’ retains its ending. None establishes a new historical derivation. |
| Prefixed ‘call’ | The early injection gives *ġecide* via root-vowel deletion. Entry just before contraction gives *ġeceid* instead, localizing the two problems separately. |
| ‘Pillow’, ‘new’, and retained *w* | *Pyle* needs labial loss plus lowering but no hiatus rule. A/B2 *nī* comes from their final identical-hiatus rule; the fake edge is not an actual compound juncture. *Clawu* is unchanged at labial loss, which does not match before *u*. |
| River and ‘strike’ | Short and long river inputs give *ei* and *ēi*. For an already smoothed nucleus in ‘strike’, changing only the suffix input *i* to *e* gives *slēþ* instead of *sleiþ*: the existing identical-vowel rule is sufficient for that synthetic path. The full trace does not reach that input. |
| Representation | `*t*é*i*d`, `*t*e*i*d` and `*t*ei*d` all render *teid* without changing at contraction. `*t*e*e*d` gives *tēd*; the inherited palatals give *reġn, weġ*, not a hiatus output. |

```sh
cache=$(docker compose exec -T backend mktemp -d /tmp/capr-hay-stages.XXXXXXXX)
bash Germanic/articles/hay/research/hiatus/run-container.sh local --stage-cache "$cache" \
  > Germanic/articles/hay/research/hiatus/local.json
```
