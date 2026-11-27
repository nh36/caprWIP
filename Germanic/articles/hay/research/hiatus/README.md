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
