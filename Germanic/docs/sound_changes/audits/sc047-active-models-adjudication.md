# SC047: active research-model adjudication

## Identity

- **SC id:** SC047, with dependencies SC010, SC014, SC017, SC019,
  SC020, SC034, SC041 and SC112.
- **Executable identifier:** `OEHeavySyllableNasalApocope`.
- **Branch / base commit:** `research/sc047-two-models` / `1afba2a8`;
  lexical source proposal `399c50ad1dd339df4d235dda53334b39fb5fec14`.

## Question

- **Hypothesis:** Early and split short-low-vowel loss can be implemented
  on one shared phonology without changing inherited inputs to fit the
  comparison or encoding paradigm transfer as a sound law.
- **Discriminating evidence:** A securely inherited light neuter direct
  singleton with a final vowel would support early loss in its variety.
  A secure inherited geminate direct cell, demonstrably not remodelled,
  would support split loss. Attested protected cells test both cascades
  and provide possible donors, not evidence of the direction of transfer.

## Current state (before any edits)

- **Historical characterization:** SC047's registry identifies “Final
  short nasal low-vowel apocope” as Proto-West Germanic, with
  “no historical gemination edge.”
- **Executable behavior:** `OEHeavySyllableNasalApocope` deletes word-final
  short *ą*. The retained production slot is not itself a historical
  verdict for light ja-stems; A and B2 reuse the same deletion.
- **Input assumptions:** The comparison pins the original 394 rows,
  including the already selected deer genitive plural. The selectors
  separately apply the unmerged common hedge/rest proposal.
- **Earlier evidence:** [SC047 adjudication](sc047-adjudication.md),
  [SC010 labial adjudication](sc010-w-gemination-and-hay-depth-adjudication.md),
  and the archived [paired comparisons](../literature_dossiers/sc047_paired_chronologies/README.md).

## Diagnosis

- **Firing census:** The active runner records every changed stage on
  every frozen and selected input and every paradigm probe. Empty output
  after input admission is rejection, not a negative firing. The
  [complete captures and result audit](../../models/sc047/results.md)
  identify all firing and endpoint differences.
- **Principal witnesses:** Direct *natją* tests whether nasal loss and
  glide vocalization bleed gemination; protected *natjai* tests live
  gemination in both. Direct hay and hue test the same dependency plus
  the downstream labial history. The oral masculine *sagjaz* and heavy
  *andijaz* are negative chronology controls. Final *z* in *rastōz*
  shields *ō* during raising; *rastōi* tests an independent contraction.
- **Control roles:** *dorą* is a counterfeeding negative for final-*r*
  lengthening in the serialized experiment; there and where are positive
  lengthening controls. *Searu : searwes* tests vocalism and proposed
  transfer without gemination. The two ‘strew’ inputs test source
  reconstruction, not a third chronology.

## Literature

- **Dossiers:** The [comparative chapter](../../assembly/sc047_preview/chronologies.md)
  and [cell source register](../literature_dossiers/sc047_paired_chronologies/comparative_followup/cell-sources.md)
  give the source passages and manuscript limitations.
- **Sources:** Ringe–Taylor pp. 44–47 and Hogg–Fulk §2.23 give the
  different orders; Dahl pp. 81–86 does not require a uniform
  West Germanic schedule. Campbell §§576–582, Boutkan pp. 209–213
  and Versloot pp. 78–92 inform conditioning or regional comparison,
  not an independent English chronology decision.
- **Long endings:** Ringe–Taylor pp. 58–61, 299–300 distinguish
  unprotected final *ō*, bimoric *ōz* and *ōi* > *ē*. Fulk
  pp. 155–156 proposes a different genitive quantity. The accusative
  witness for ‘rest’ is Morris p. 101, l. 26; Fox pp. 88.29–32
  gives the dative, not a genitive.
- **Modelling decisions:** Campbell §120.2, Hogg §3.18 and Ringe–Taylor
  pp. 246–250 motivate palatal conditioning on the labial geminate.
  Encoding it as a retained token does not decide its segmental status.
  The narrow singleton-*aw* proxy and word-final short *i.i* contraction
  are bounded implementations, not claims about all English hiatus.

## Historical analysis

- **Stage and scope:** The registry places the shared loss in
  Proto-West Germanic. The rival relative orders are being applied
  to the ancestry of Old English; no new uniform Continental or
  Frisian chronology follows.
- **Conditioning:** Finality and vowel quality, independent of case,
  control apocope. A short stem vowel, eligible single consonant and
  surviving nonsyllabic *j* condition gemination. Nuclearization
  removes that trigger from a stranded singleton.
- **Counterexamples and analogy:** Continental *peti* and *bedi*
  complicate a uniform split account. The English obliques establish
  possible donors but not transfer. Cotton *hiewes* and Hatton *hiwes*
  are spelling/stem witnesses, not successive stages. No protected
  hay form with the predicted overt ending is verified.
- **Proxy limits:** The input extension for *ōi* parses phonologically
  admitted structures, not an inventory of dative words. Different
  end quantities run separately; they are not special-cased by cell.
  Admitting inherited *ōmiz* (Ringe 2017, p. 312) exposes a distinct
  unresolved plural issue: both *ōmaz* and *ōmiz* yield *-em* under
  the shared shortening path, not the usual OE *-um*. Admission is
  not proof of the plural's full phonological derivation.
- **Chronology:** Raising before loss of shielding *z* is
  `independently_demonstrated` by the long-ending contrast discussed
  above. The oral-loss/gemination order is a shared premise of the
  two sources; each nasal edge belongs to its respective source
  reconstruction, not a newly demonstrated adopted edge. Placement
  of SC112 relative to the assay's early loss is a control constraint,
  not a historical date claim.

## Verdict

- **Registry verdict:** Retain production position and characterization.
  Run A and B2 as the only active research implementations; retain B
  as archival evidence for the labial encoding dependency.

  `Registry-verdict: SC047=REFORMULATE/RETAIN`

  The active models implement competing inherited histories. Their
  independent lexical choices describe which cells are supported for
  regular derivation, not a verdict from aggregate scores.

## Propagation

- **Affected files:** The research runner, cell register, reports and
  research book assembly. No production registry or canonical artifact
  is regenerated.
- **Guards:** The focused tests cover the shared rule inventory, order
  constraints, frozen identities and intentional cell overlays. Live
  reports additionally expose endpoints and controls for both runs.
- **Baseline effect:** No change to the frozen input dataset, the
  canonical FST or `update`. Model output differences are research
  results, not baseline migrations.

## Residue

Secure case-specific hay evidence, independent evidence for a broader
short-hiatus rule, and the history of the conflicting stem vowels in
the labial class remain open. An unselected form and its possible donor
are preserved even when the selected form derives regularly.
