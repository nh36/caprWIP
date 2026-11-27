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

The [adjudication and closeout](ADJUDICATION.md) give the historical
verdict, the chronological ledger and the focused second-cycle proposal.

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
| Weight, high-vowel loss and lowering | `OEWeightMarkers` and `OEHighVowelApocope` do not delete the observed A hiatus in ‘hay’, ‘call’ or ‘strew’. The literal `*ᶜ` cleanup in HVD is inside `FootCtx`; it does not erase the externally routed initial marker in the injected probes (§5). `OEMedUnstressedILowering1` requires intervening consonants, so it lowers *i* in ‘prepare’ and in ‘strike’ before *h*-loss but not hiatus *i* in ‘hay’. The second lowering component restores *i* from *e* before *ng*, not in generic hiatus. |
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

## 4. Competing generalizations, fixed before the trials

These are research overlays, not proposed edits to the canonical
cascade or alternative historical certifications. The exact definitions
and placement grid are in [candidates.py](candidates.py). The IDs here
are independent of the historical hypothesis numbering in the article.

| Arm | Operation and discriminating prediction |
|---|---|
| H0 | No overlay. The baseline can serialize syllabic *e.i* as ⟨ei⟩; that is neither contraction nor a glide. |
| H1 | *e.i > ē* even with no following consonant. Lengthens without retaining a palatal. An acute-only arm is a representation control, not a historically distinct rule. |
| H2 | *e.i > ej* regardless of the following segment. Can give final *eġ*, can leave a cluster before a consonant, and can feed existing intervocalic vocalization before a vowel. |
| H3 | *e.i > ē* before stops `{p b t d k g}`, dental stops `{t d}`, dental obstruents `{t d þ ð}`, coronals `{t d þ ð s z n l r}`, or any model consonant. Pair each with final retention and with an independent edge glide; the unmatched prevocalic environment retains both vowels. Dental stops predict no contraction before *þ* or *n*; adding coronals also predicts contraction before *s, l, r* and does not mean merely adding *n*. |
| H4 | *e.i > ej > ē* before *d, þ, ð, n*, using a separately compiled glide-loss operation with lengthening. The vowel may reach the same endpoint as H3, but this arm predicts an intervening consonant and can act on a pre-existing compatible *ej* regardless of origin. Before the merger it does not reach *eʝ*. After the merger it also tests that inherited population. The corpus may reject treating these two sources together. |
| H5 | *e.i > ē.i > ēj* against *e.i > ej > ēj*. Two distinct ordered events: transformed inputs may be intercepted by high-vowel loss or consonant rules. The second operations have no hidden origin restriction: inherited compatible long hiatus or *ej* can also be caught. A resulting *ēġ* is compatibility, not evidence that the lengthening occurred. |
| H6 | Glide only at the absolute word edge, or only before consonants. The latter explicitly leaves final hiatus. These arms separate retention from desyllabification without attributing either to a morphological boundary. |

The full early placement is immediately after labial loss, before the
A/B2 final identical-vowel rule (before `OELatePalatalDiphthong` for
canonical). H1 also brackets HVD and *i*-lowering, and contrasts with
insertion immediately before `OEContraction`; H2 tests that late
placement too. H4 brackets the existing heavy-context *j*-loss and
tests a late position at the merger to distinguish *j* from *ʝ*.
H5 puts its second operation immediately after heavy-context loss.
Those are ordering comparisons motivated by the states in §3, not
claims about historical placement. None rewrites the upstream
`OEUnstressedEIContraction` or adds a proto-parser exception.

Marked *é* is accepted on its own. For plain *e*, the overlay
recognizes the first nucleus of an unprefixed form, or the root
nucleus after one pretonic syllable with `*ᶠ`. This is a conservative
proxy, not stress recovered from the internal string: it may accept
a plain initial unstressed *e*, and after `OEHLoss` clears the flag
it misses a prefixed root without an acute. `*ᶜ` and `*ᵘ` are
preserved if present but cannot encode an internal boundary before
the second vowel. No lexical IDs appear in a rule. The explicit
coronal class is not the frozen lowering class, which excludes
nasals. All arms remain specific to *e.i* at initiation because
that is the comparison under test, not because other vowel
sequences are known to resist resolution. Test different vowels,
marked and unmarked stress, already-long sequences, and inherited
palatals rather than extending an unattested generalization.

The sources constrain different parts of this design. Luick §243
and Campbell §237 describe absorption without a necessary
intermediate consonant; Luick also considers remodelling from a
stem with *j*. Campbell §§243–245 and 489 document sporadic early
Anglian and predominantly West Saxon loss of palatal *g* before
dentals, not a general rule for every coronal, nor a demonstrated
ordering after gliding of post-*w*-loss hiatus. Hogg §§3.19, 5.131,
5.133, 5.147–149 distinguishes supported diphthongal patterns and
unresolved Anglian sequences; his assumption of prior length is
the reason to test H5, not a measurement of short-root post-*w*-loss
inputs. Mosionek and Zembrzuski (2019: §§2–6) separate diphthongization,
gliding, glide insertion and contraction. Their examples of gliding
and insertion (`nerian`, `lōcian`) have a different vowel and
consonant configuration; their phonotactic diagnostics motivate
testing adjacent consonants, prevocalic strings and long nuclei
separately, not assigning a particular outcome to *e.i*. Atomic
diphthongization and creation of consonantal *j* are not synonyms.

## 5. Synthetic environment matrix

The [35 internal probes](synthetic.tsv) are not witness evidence.
The [receipt](synthetic.json) contains 490 isolated predictions
(14 networks × 35 probes), 910 overlay suffix traces (26 × 35),
and 210 no-overlay suffix controls across six starting points in A.
All isolated firing sets, including negative cases, were checked
against the fixture expectations. Every overlay trace has all
immediate candidate before/after states and the untouched frozen
suffix endpoint. Compare to the no-overlay control **at its own
starting point**, not to a later injection that skips intervening rules.

| Contrast | Executed result |
|---|---|
| Contraction vs. glide vs. retention | At the edge the short marked input gives *tē*, *teġ*, or *tei*, respectively. Before *d*, H1 and H4 give *tēd*; H4 alone goes through *tej-d*. H2 keeps the new palatal as *teġd*. |
| Class scope | Stops contract before *k, p* as well as *d, t*; dental stops exclude *þ, ð*. Dental obstruents include those fricatives but exclude *n*. Coronals add *n, s, l, r*; any consonant adds the labial sonorant *m*. Final glide changes only the edge, not the preconsonantal contraction class. |
| Position before a vowel | Early H2 produces `*t*é*j*a` immediately, but the frozen intervocalic rule returns it to `*t*é*i*a`; the endpoint is *teia*. Late H2 produces *teġa* after skipping that operation. |
| Prior vs. subsequent lengthening | Prior length creates `*t*ḗ*i`, feeds HVD and gives *tē* word-finally, precluding subsequent gliding there. Glide-first survives as *tēġ*, but also lengthens pre-existing `*t*é*j` to *tēġ*. Preconsonantal inputs can converge as *tēġd* by the two different routes. |
| Palatal loss placement | H4 gives *tēd* from inherited `*t*é*j*d` at all three loss placements. The inherited `*t*é*ʝ*d` case only gives *tēd* when loss runs after merger; earlier arms give *teġd*. This is not a chronology for the originally post-labial controls. |
| Quality, quantity and stress | First-step rules leave already-long *ē*, lowered *e*, second-vowel *u/ī/í*, initial *á/è* and atomic `*ei` alone. H5's second-step tests intentionally differ. Acute-only misses the plain root; the foot proxy distinguishes flagged pretonic-plus-root from a plain later nucleus and from a plain first vowel in the flagged foot. |
| Boundary and routing | Two separately queried tokens prevent matching across the application boundary, unlike the same adjacent vowels in one token. There is no independent internal morphology token. `*ᶜ` and `*ᵘ` survive as externally routed flags in these injections (even across HVD) and the frozen suffix rejects those marked forms; late injection of `*ᶠ` similarly skips its cleanup. Their immediate outputs test routing, not actual compound derivations. No overlay adds a downstream rejection among the corresponding accepted controls. |

```sh
bash Germanic/articles/hay/research/hiatus/run-container.sh synthetic --stage-cache "$cache" \
  > Germanic/articles/hay/research/hiatus/synthetic.json
```

## 6. Common historical panel

The [comparison receipt](comparison.json) runs all 27 arms in
canonical, A and B2. Each arm uses the same 37 historical submissions
and 20 separately prefixed `local:` diagnostics. For each of the
4,617 traces it records the input, ordered changes, each candidate
before/after pair and the endpoint. H0 reproduces the earlier full
and local traces exactly; the eight unadmitted submissions and
twelve unsubmitted rows were not repaired or counted as negative
evidence. The candidate-source hash is identical to §5; component
binary hashes record each run's isolated compilation, not a
cross-run byte-identity claim.

| Arm or contrast | Full-cascade historical comparison |
|---|---|
| H1, marked vs. foot-aware | The marked-only rule never fires on this panel. Early and intermediate foot-aware H1 prevent A/B2 root-vowel deletion in ‘call’, producing *ġecēþ, ġecēd*, and change *streid* to conditional *strēd*. Late H1 still changes ‘strew’ but misses both ‘call’ forms. The assumed prefixed history should be compared with the relevant prefixed witnesses, not silently equated with simplex *cēþ*. A ‘hay’ becomes *hē*: contraction alone loses the palatal needed for ⟨heg⟩. |
| H2 | A ‘hay’ becomes *heġ*. Early A/B2 instead give ‘call’ and ‘strew’ *ġeceġþ, ġeceġd, streġd*, not the contracted forms; late H2 misses ‘call’. Preserving written ⟨g⟩ for A ‘hay’ does not establish short quality or quantity from the manuscript. |
| H3 | Both stop scopes improve the *d* participle if contraction is intended, but neither addresses ‘call’ before *þ*. Dental obstruents repair both ‘call’ forms. Coronal and any-consonant arms add no full-cascade change over dental obstruents on this inventory. Only locally injected ‘couch’ discriminates those wider scopes from dental obstruents. Keeping the edge as hiatus yields A *hei*; a final glide yields *heġ*. No late palatal restoration was introduced. |
| H4 | Both heavy-loss-bracketing arms give the same visible outcomes as early coronal contraction for ‘call’/‘strew’, but pass through a consonantal *j*. The late loss arm leaves *ġeceġþ, ġeceġd* because `OEHLoss` has cleared the prefix flag used by the plain-root guard. It contracts unprefixed ‘strew’ and the inherited rain/thane/ask clusters instead: *reġn, þeġn, freġnan > rēn, þēn, frēnan*. These replace attested retained forms; notably the last output does not match the panel's *frīnan* loss variant either. The late arm cannot be called a general repair. |
| H5 | Prior length gives A *hē*, with HVD deleting *i* before the glide stage. Glide-first gives A *hēġ*, but leaves long-vowel-plus-palatal clusters in the preconsonantal cases, where the proposed comparators contract. The two orderings agree on *ġecēġþ, ġecēġd, strēġd* and do not account for ‘call’/‘strew’ by themselves. |
| H6 | Final-only H6 gives A *heġ* without touching the troublesome preconsonantal cases; nonfinal-only gives early H2's nonfinal glide clusters without altering A *hei*. |

No e.i overlay explains the canonical ‘call’ or ‘strew’ histories
with their early long diphthong. Canonical and B2 retain their
West Saxon-comparable *hīeġ*, while A's protected predictions stay
unchanged. ‘Know’ and ‘crow’, the retained labial and back-vowel
controls, and the admitted negative controls ‘way’, ‘day’ and
‘island’ retain their full-cascade endpoints. No candidate resolves
the independent ‘see’/‘strike’ input problems. A/B2's unlevelled
‘ewe’ input changes whenever the final hiatus does; this is a
paradigm-input problem, not an extra success. Arms touching *þ*
often replace the documented exceptional ‘itch’ with a
*w*-less output (e.g. *clēþ* or *clēþu*), even bleeding its high
vowel in early arms; none derives the exceptional form. That
change is a warning, not a reason to add a lexical exception.

**Local-only diagnostics.** A/B2 and canonical can all take the
same injected input regardless of the history they reached above.
Early dental-stop contraction gives ‘flock’ *ēd* instead of *eide*;
it does not recover the cited *ēde*. Candidate length feeds
high-vowel loss there. Early coronal contraction or H4 give
‘couch’ *strēn* instead of *streinu*, while late H1 gives *strēnu*.
Early dental arms produce injected prefixed *ġecēde*; late
contraction cannot recover the deleted root. A late *h*-loss
probe can produce river *ē* under H1 or *eġ* under H2, but only
with the disputed short input. The deliberately lowered ‘strike’
probe needs neither overlay. Glide-first lengthens an injected
*weġ* to *wēġ* when *j* is present at the relevant stage; the
full input avoids this only because it still has *ʝ* there.
These results identify prerequisites and collateral effects, not
inherited cells that the full parser licensed.

```sh
bash Germanic/articles/hay/research/hiatus/run-container.sh historical --stage-cache "$cache" \
  > Germanic/articles/hay/research/hiatus/comparison.json
```

## 7. Unscored wider firing audit

The [audit](corpus.json) uses the 394 archived and 396 active
inputs and their captured stress/finality metadata, separately
keyed. It runs H0 and 17 informative arms in each model:
42,660 row–model–arm executions, including repeated comparison
inputs, not that many independent lexical observations. H0
reproduces all 394 archived endpoints in each model and all
396 active endpoints in each of A and B2. Canonical at the
396 active inputs is a new comparison on the inputs shared
with A, not an asserted match to an active canonical trace
receipt. All 490 isolated synthetic outputs match §5 on the
recompiled overlay components. No comparator is rescored.

The two panels show the same firing populations. The receipt
includes every individual candidate application, both ordered
traces for affected rows, and captured identities for unaffected
rows. A firing is a before/after state change at a candidate
component, not inferred from its endpoint. No affected row's
endpoint returns to its H0 value here.

| Complete population per panel | Output and interpretation |
|---|---|
| 2061 ‘hay’, A only | H1 early/late and H5 length-first give *hē*; H2 early/late, the three audited H3 edge-glide arms, all three H4 arms and H6 final-only give *heġ*; H5 glide-first gives *hēġ* with two firings. No other post-labial *e.i* lexeme fires on an archived or active selected input. |
| 2147 ‘rain’, all three models | H4 post-merger alone gives *rēn* instead of *reġn*. Campbell §243 cites the loss variant and §489 discusses chronology; the recorded palatal retention is a real alternative, not a feature to erase from every witness. |
| 2148 ‘rainbow’, all three models | H4 post-merger alone gives *rēnboga* instead of *reġnboga*. This was not used to formulate the candidates. The [existing source ledger](../../../../docs/lexeme_reports/model_entries/2148-rainbow-reġnboga.source_ledger.md) records Orel (2003: 300) with retained *gn*, but [Bosworth–Toller, p. 790](https://bosworthtoller.com/25654) cites loss forms in the vocabularies, Ælfric and Genesis 9:13. The overlay reaches a documented variant, not the selected CAPR form. The dictionary's quantity mark is editorial, and the compound shares its first member with ‘rain’; this is neither a new independent root nor evidence for preconsonantal post-*w*-loss contraction. |
| 2243 ‘thane’, all three models | H4 post-merger alone gives *þēn* instead of *þeġn*. Campbell §243 reports both shapes; an inherited cluster can undergo loss, but the result does not license categorical replacement of the retained variant across dialects. |

All other rows and placements have zero candidate firings.
In particular, the audit does **not** make the 396-row active
corpus an independent confirmation of preconsonantal
post-labial contraction. H3's wider classes do not enlarge its
actual census, and the H4 late class reaches a different
historical population. These are selection and domain findings,
not evidence that the broader rules are harmless historically.

```sh
bash Germanic/articles/hay/research/hiatus/run-container.sh corpus --stage-cache "$cache" \
  > Germanic/articles/hay/research/hiatus/corpus.json
```
