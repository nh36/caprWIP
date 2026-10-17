# Provenance: place adverbs and inherited-r lengthening

## Authority and preservation

This is a research-only investigation on `update`, beginning at
`c92cbd9d541785986998ab2ab99a416f87da4f68`. The local commit and
`origin/update` were independently checked to agree before preparation.
The released SC015 decision remains the production authority. No trial
authorizes a corpus admission, a sound-law change, a new active SC,
a chronology edge, a baseline migration or revised book prose.

The preparation followed `RESEARCH_ADJUDICATION_PROTOCOL.md`,
`CURRENT_STATE.md` and the adjudication template. Non-Foma
`adjudicate.py SCNNN --prepare` packets were obtained for SC015, SC024,
SC025 and SC101. The healthy Docker stack, `/usr/app`, mounted FST
directory, `foma` and `flookup` were checked before experimental work.

An immutable session start manifest pins 4,108 files: tracked files,
canonical runtime artifacts and the pre-existing untracked
`Germanic/fsts/tmp_probe.foma`. Preparation preserved every pinned hash.
The unrelated probe is not part of this investigation and is excluded
from its release. Experiments must use isolated temporary builds, not
overwrite canonical bins or rebuild them concurrently.

## Scientific starting fingerprints

| Owner or projection | SHA256 |
| --- | --- |
| `Germanic/fsts/germanic.txt` | `da04db7a21664bf9a606e331c5dd484a023d00e00a5ecf7c19ea3e8e310789e9` |
| `Germanic/data/germanic-aligned-final.tsv` | `514cfe096b636ea6790361787a154a70e6dafb7d8bf3e4936fced51f3b1b2a6f` |
| Selected-387 evaluator projection | `b85be7e765245d5fabc05f536b19a8e35f0ec2e4220e6f23237d81d83ceb42bb` |
| Lexical-input projection | `e495ab40d4fb34f2117c6d8590ee11e18166271e01712755b99507bf9933aef2` |
| Active original-380 projection | `43de8a47b7aaf17f860c9e3009617002ddb36e4d32a90ede1a99525858a417ce` |
| Immutable original-380 archive | `fae656520e9ebf446854643907a1ba48a511877fc25b1fae39649d5b97e9a6cf` |

The baseline has 387 accepted, determinate selections: 379 matches and
eight established mismatches. Their identities and directions are:

| Row | Concept | Predicted | Selected target |
| --- | --- | --- | --- |
| 1973 | buck | bocc | bucc |
| 2013 | fire | fȳr | fȳre |
| 2030 | fowl | fogol | fugol |
| 2162 | rust | rost | rust |
| 2224 | straw | strēa | strēaw |
| 2240 | tap | tappa | tæppa |
| 2298 | wolf | wolf | wulf |
| 2300 | wool | woll | wull |

The source TSV's maximum row ID is 2332 and its maximum cognate-set
number is 555. The existing allocation convention increments the
maximum numeric ID (`Germanic/tools/add_old_english_rows.py`, lines
35–48). Research reservations 2333, 2334 and 2335 designate proposed
Old English here, where and there respectively; they are not inserted
rows or a reservation in the canonical dataset. Any eventual admission
must recheck availability, cognate-set ownership and structural sibling
requirements. No daughter-language forms or placeholder rows are
invented by this investigation.

## Independent tracks and order of evidence

The historical/philological track assesses the held sources, printed
symbols, morphology, attestations and competing reconstructions without
experimental match results. The computational track audits the existing
inventory and constructs the isolated harness without running Foma.
The lead reconciles a source-backed witness table before permitting
compiled trials. Comparative citation, an earlier historical hypothesis
and a selected executable input remain separate fields.

The earlier `sc015-a-ablaut-investigation/chronology.py` and
`chronology.json` are historical component-only experiments pinned to a
different source. They are neither rerun nor repinned. Their schematic
acute-e to acute-long-e mapping is a hypothesis to test against SC024,
not a previously validated full-cascade solution.

## Dictionary page-image verification

The earlier draft citations confused PDF sheet positions with printed
folios. The selected source pages were rendered from the held PDFs and
inspected as images. In these sampled entries, Kroonen's PDF sheet number
is 40 greater than the printed folio; Orel's is 39 greater. Cite the
printed pages below, not the PDF sheet numbers.

| Source entry | PDF sheet → printed folio | Image SHA256 | Source PDF SHA256 | Image observation |
|---|---:|---|---|---|
| Kroonen *hiar* | 265 → 225 | `13e28b6f2dcbecb7a55cf3ee1952eb22eb73b95eddc39b9ea8d1a5966efc6422` | `c450806b88cac9fe5dbb7ba163bcc83a54168d3a87c8a9da48801795db5090f7` | Entry gives *hiar* and unmarked OFris `hir`; it does not print a macron on that Frisian form. |
| Kroonen *hwar* | 303 → 263 | `5207248ab3a4a58b174a4b30d09fc00840e350c4d92f0fde798ae5ca94b73d34` | same | Entry treats West Germanic long-vowel forms as lengthened; the folio number is 263. |
| Kroonen *þar* | 574 → 534 | `87a06d4ffef0e5381c5090793819d069528849c5bf224f6e5df926003a7972f1` | same | Entry has the corresponding *þar* forms; the folio number is 534. |
| Orel *xē₂r* | 211 → 172 | `b32fad6af19f2acf1def29bc0d6bb9d0f14734f3b6fc4fc3864fc5ac73fde234` | `c18865720a05accb2b40d0c244d03f767a7679c58f16283696e04d663805c3f9` | Entry prints *xē₂r*, OFris *hīr*, and cites the lowering of *ī* to *ē*. |
| Orel *xwar ~ xwēr* | 237 → 198 | `af6e95a702fafd7c117c40b47c4a3fa94a7ae7e01b9cf42f9e1307eb881a2620` | same | Printed page 198 contains the alternating *xwar ~ xwēr* entry. |
| Orel *þar ~ þēr* | 455 → 416 | `bb598fa212a015294455f4962111bbcc57c01aa8c69f71d46580e99b2cd4ab2c` | same | Printed page 416 contains the alternating *þar ~ þēr* entry. |

The two *here* entries therefore disagree in their Old Frisian
transcription (*hir* versus *hīr*). The images verify what each
dictionary prints; they do not establish the manuscript spelling,
editorial policy or phonetic quantity behind that spelling. Keep the
disagreement explicit rather than using either dictionary alone to
resolve Old Frisian quantity.

This also corrects the historian's follow-up handoff: it cited Kroonen
PDF sheet 265 as printed p. 265 and quoted an OFris. macron from the
OCR. The scanned sheet is printed p. 225, and the image reads unmarked
`hir`. Therefore the handoff's claim that Kroonen independently confirms
long OFris. *hīr* is rejected. Only Orel's inspected entry prints *hīr*;
Ringe–Taylor's claim that a short reading is unlikely is an authorial
assessment, not a direct manuscript quantity measurement.

## Experimental contract

The research driver expands the current `oe_pipeline` model into its 107
leaf events. It does not maintain an independently transcribed cascade.
Each recipe records exact definitions, source substitutions and relative
insertion anchors. New symbols must be single Unicode scalars, explicitly
assigned to vowel, quantity, stress and front-vowel classes as appropriate;
the framework's consonant-extension hook is not used for vowels.

Execution is gated by the SHA256 of the completed historical witness table,
four source/context pins, a fresh existing canonical build manifest and
explicit container-only `--execute`. Identity is checked against the
isolated native wrapper, the existing canonical native bin and all 387
frozen row identities and outputs, joined by stable row ID. Each edited
wrapper records all selected-row before/after states, supplementary states
separately, every event's census, all final deltas and explicit rejection
or ambiguity. Compilers write only inside unique investigation-local work
directories; canonical runtime bins are not rebuilt.

Before compiled results, the contrasting explanations are:

1. With Hill's short antecedent, lowering-first can feed lengthening of
   short e; lengthening-first instead removes short i from SC015's domain.
   This is a conditional ordering test, not evidence that the short
   antecedent is independently proven.
2. Mapping newly lengthened stressed e to inherited `ḗ` before SC024 can
   create a representational collision. Distinct long-path results must
   be compared before interpreting a wrong output as historical evidence.
3. A unified early rule and an early r-only component may have identical
   outcomes. A split requires independently supported history or a
   discriminating witness, not simply a more elaborate formalism.
4. An already-long comparative input may derive the same Old English
   target without testing the origin of its quantity. Such an input is a
   genuine comparator but not an application witness for new lengthening.
5. Hill (2017:148) also states the sequence `*hir > *hīr > *hẹ̄r`.
   A simple lengthening-before-short-*i*-lowering recipe does not test it:
   after lengthening, short SC015 no longer matches. A separate sensitivity
   recipe maps long `ī/ḯ` to `ē` before final `r`. It models Hill's stated
   order, but its rule, domain and date remain assumptions; it is not the
   adopted SC015 rule or an implementation of Ringe's full account.

The driver, declarative recipe builder, receipt comparator, witness-table
shape and probe references pass 30 text-only tests. No
compilation was performed to obtain those checks; they establish schema,
isolation, source expansion and recipe construction, not the correctness
of a historical recipe.

The builder prepares 20 base candidate/representation combinations plus a
separate long-*ī*-lowering sensitivity recipe, without selecting witnesses
or executing Foma. Its four base architectures are current
SC015 with alternative lengthening placements; unified early lowering;
early r-only lowering with z/st at the current position; and an
independently sourced already-long comparator with later lengthening.
Reverse-order and inherited-long-e collision recipes are controls, not
recommended sound laws.

The three representations use existing e/é and ē; explicit lowered short
ẹ/plain and ḙ/acute with long ệ; or transient origin labels ị/plain and
ỉ/acute that lengthen to existing ē. The nonstandard diacritics are
single-scalar technical labels, not independent claims about phonetic
values. Class extensions, literal consumers and mergers are recorded in
each recipe. Immediate merger and merger before final-z compensatory
lengthening are separately testable assumptions. Optional persistence
until breaking is explicitly a representation-stress control because it
can bypass native literal-vowel rules.

Late placement has two declared limitations: earlier loss can erase weak
word-stress marking, and rhotacism can make secondary r indistinguishable
from inherited r. Negative controls must measure those effects; successful
adverb outputs cannot establish a general inherited-r law by themselves.

## Historical evidence gate: initial handoff review

The independent historical track delivered its initial assessment before
any compilation. The lead did not accept that handoff as a verified witness
table: its descriptions conflated quantity and quality in Old Frisian
long high *hīr*, described Old English long *hē* as short, and described
the *e* of *meord* as retained *i*. It also failed to keep a dictionary's
comparative citation reconstruction separate from Hill's earlier
historical antecedent. Those statements are not adopted findings.
Original-page corrections, dictionary reconstruction checks and better
attestation receipts were requested from the same historical track,
still blind to experimental outputs. The compilation gate remains closed
until those corrections are reconciled. This record prevents later
computational success from retrospectively being presented as the basis
of an independent reconstruction.

The lead also added `summarize.py`, a non-Foma receipt comparator. It
retains intermediate differences even when finals agree, aligns common
named events rather than shifted numerical positions, and enumerates
every pair of candidate recipes. Its comparison is mechanical, not an
automatic claim about historical chronology.

## Completed full-cascade run

The corrected witness package passed the source-status review with
uncertainties retained rather than resolved by model fit. Its SHA256 is
`b9d346112fafb27a5de26b91eed1696ef622ed2c5f12970e21f38fdfd6651a87`.
The pinned recipe specification (`recipes.json`) has SHA256
`111bc28a18d591716a2b37c045de8ce05672edfcb7e8a08958bcb10af6a99da8`.

The isolated driver completed 21 recipes, all 387 selected rows, and
34 supplementary probes through 107 events in Foma `0.10.0alpha`.
`experiments.json.gz` has SHA256
`55f8acc519ea78f1c61a5c4a502286bea5060fd64b86a7dbfc697669ca9f541c` and
records `status=complete`, every row/probe trace, event firing censuses,
rejected and ambiguous inputs, and `protected_unchanged=true`.
`comparison.json` has SHA256
`9a751db5bb2d0d6438235774a6d825d4caf70a51b1a706b92a2ce0181c6e4beb`;
it contains 210 pairwise comparisons and preserves intermediate
divergence even when final outputs agree.

The comparison pins the runtime inputs:

| Input | SHA256 |
|---|---|
| `Germanic/fsts/germanic.txt` | `da04db7a21664bf9a606e331c5dd484a023d00e00a5ecf7c19ea3e8e310789e9` |
| Corpus TSV | `514cfe096b636ea6790361787a154a70e6dafb7d8bf3e4936fced51f3b1b2a6f` |
| Wrapper context | `6a69a8d450a0ad5898bed7150136dc70e5731422c29803608825cdefc6b0f914` |
| Context helper | `b770b83ffc2bd863c9cd5dec6bcae67ecda60efe8ce0af7fa8cdf136e077b961` |
| Research driver | `e2ddc83571332293f3e5c66733859891f7472633509c777604ad53a3c8a25a66` |

Independently of the driver's protected snapshot, every path in the
recovered original start manifest was rehashed against its initial
SHA256: all 4,108 files exist and match, with zero changed or missing.
No production rule, corpus row, registry, baseline, generated bin, or
book artifact was changed.

The result is conditional, not a chronology proof. Under the reconstructed
short-*i* `hir` input, lowering before `XRLen` yields *hēr*, while
lengthening before short-*i* lowering yields *hīr*. The second order also
yields *hēr* if a separate long-*ī* lowering is added, as Hill (2017:148)
explicitly allows. That added process has not been independently
established here. The full adjudication, recipe comparison, final-output
effects, and corpus-admission recommendation are in `REPORT.md`.

The completed experimental results supersede the initial status above
that the compilation gate remained closed. That gate was opened only
after the source corrections and recipe pins were reconciled; the
completed Foma run did not modify production files.
