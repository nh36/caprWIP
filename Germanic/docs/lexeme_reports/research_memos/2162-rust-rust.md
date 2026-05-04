# Research memo — 2162 rust / rust

## Starting point

- **ID:** 2162
- **CONCEPT:** rust
- **COUNTERPART:** rust
- **PROTO:** `*rústō`
- **PROTOFORM:** `*rústō`
- **DERIVATION_CLASS:** `unexplained_unmodelled`
- **NOTE:** the row currently treats `rust` as a documented u-lowering exception and says regular development gives `**rost`; it also says no lautgesetzlich paradigm cell is available because high-vowel cells would give `**ryst`.

The packet is therefore starting from an unresolved-exception framing, but the row also appears to preserve an older, philologically suspect stem-class choice: `*rústō` implies a feminine ō-stem, whereas the OE noun is treated elsewhere in the repo and in the dictionaries as masculine.

## Packet evidence assessment

**Authoritative/current:**
- The aligned TSV row is current for project data state.
- The packet's main phonological claim is current: the live source-backed OE FST still gives regular `rost` for citation-form inputs (`Germanic/fsts/old_english.bin` and `backend/old_english.bin`).
- The `oe_known_problems.tsv` entry is current in substance: this row belongs in the u-lowering-exception bucket.
- The packet is also right that a paradigm probe is relevant and that no built-in rust probe exists yet.

**Useful background:**
- The packet's excerpts from `DEV_NOTES.md` on Campbell, Bülbring, Luick, Brunner, and the Schuhmacher consultation are useful background for the scholarly status of OE `u`-retention.
- The packet's metathesis material is useful only to show that older `orst` outputs were diagnostic noise from a separate bug, not the core philological issue.

**Stale or superseded:**
- The packet preserves an older `DEV_NOTES` proposal that row 2162 could be rescued by retargeting to `*rústis → rustes`. That proposal is not authoritative now: it was never implemented in the TSV, and under the current project input notation / live FST the comparable a-stem gen.sg. input is `*rústas`, which yields `rostes`, not `rustes`.
- Older `orst` evidence is superseded by the later metathesis fix; the live issue is `rost`, not `orst`.
- A repo-root `old_english.bin` artifact currently returns `rust`, but it disagrees with `Germanic/fsts/old_english.bin`, `backend/old_english.bin`, and the source rules. I treated the repo-root binary as stale build output, not as authority.

**Irrelevant or misleading:**
- Several packet "analysis" hits are keyword noise triggered by generic `gen.sg.` / `i-umlaut` strings in unrelated dossiers; they do not bear directly on row 2162.
- Bibliography-candidate lines that only register the surname `Stiles` are not evidence.

## Additional repo research

Checked beyond the packet:
- `Germanic/docs/DEV_NOTES.md`
- `Germanic/data/oe_known_problems.tsv`
- `Germanic/docs/analysis/notable_findings.md`
- `Germanic/data/old_english_wiktionary.tsv`
- `docs/references/campbell_old_english_grammar.txt`
- `docs/references/brunner_1965_altenglische_grammatik.vision.txt`
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`
- `docs/references/orel_handbook_germanic_etymology.vision.txt`
- `docs/references/ringe_vol1_pie_to_pgmc.txt`
- live FST artifacts: `Germanic/fsts/old_english.bin`, `backend/old_english.bin`, and the stale repo-root `old_english.bin`

Main findings from that repo research:
- `DEV_NOTES`' general literature review remains sound: OE `rust` belongs with genuine `u`-preservation exceptions.
- `DEV_NOTES` §17.10.34's specific rescue proposal for `*rústis → rustes` does **not** line up with the current project input notation or the live FST.
- `Ringe` gives `*rustaz ‘rust’ (cf. OE rust, OHG rost)`; `Orel` likewise gives `*rustaz sb.m./f.` with OE `rust`, OS/OHG `rost`.
- `Clark Hall` has `rūst m. ‘rust’`; `Brunner` lists `rust stm.`; `Bosworth-Toller` also treats `rust/rúst` as the OE noun entry. These support masculine stem status, not a feminine ō-stem.
- `old_english_wiktionary.tsv` has `rust`, which is compatible with the attested headword but adds no new morphological evidence.

## Reconstruction and early-stage forms

Three levels need to be kept apart:
- **Cognate-set proto / etymological headword:** comparative repo sources support `*rústaz`, not `*rústō`.
- **Project input form used for derivation:** if the row is meant to target the attested citation form `rust`, the input should also be the citation-form masculine a-stem `*rústaz`; the current `*rústō` is a stem-class error.
- **OE target form:** the row's target is attested OE `rust`, the citation form of the noun.

With the live source-backed FST, both `*rústō` and corrected citation-form `*rústaz` produce regular `rost`. So correcting the proto/stem class does **not** solve the mismatch; it only makes the row philologically cleaner.

The only probed inherited cell that yields `rust` regularly is `*rústu`, i.e. the high-vowel instrumental-singular-type comparator already discussed in `DEV_NOTES` as the marginal analogical escape hatch. That is not the same thing as showing that the citation-form row is regular.

## Old English philology

The OE target is an attested noun, not a reconstructed phantom form. Repo lexicographic materials support `rust/rūst` as a masculine noun:
- `Clark Hall`: `rūst m. 'rust'`
- `Brunner`: `rust stm.`
- `Bosworth-Toller`: noun entry under `rust/rúst`

That matters because the current row's `*rústō` collapses the attested OE headword onto the wrong inherited stem class. The philological issue is therefore twofold:
1. the attested OE target `rust` is real;
2. the current inherited form attached to it is wrong even before the exception note is evaluated.

I did not find repo evidence requiring a special dialect or manuscript claim for this row beyond ordinary OE lexicographic attestation. The safe description is simply that `rust` is the attested OE citation form, while regular inherited citation-form development would point to `rost`.

## Project problem and solution

The project problem is not just "why doesn't the FST reach `rust`?" It is also that the row currently encodes the lexeme with a likely wrong inherited noun class.

Best current solution:
- treat `rust` as a **genuine OE u-lowering exception** at the citation-form level;
- correct the row's inherited proto/stem-class metadata from `*rústō` to masculine `*rústaz`;
- do **not** treat the older `*rústis → rustes` proposal as live authority;
- use any paradigm-cell discussion only diagnostically, not as proof that the citation-form row has become regular.

In other words: the row should remain an exception row, but it should be an exception row with the right proto and the right explanation.

## Paradigm probe

A paradigm probe **is required** for this row, because the key project question is exactly whether any inherited cell gives a defensible regular outcome. No built-in rust spec exists yet, but a manual probe against the authoritative live bin is enough to show the shape of the problem:

- `*rústō` → `rost`
- `*rústaz` → `rost`
- `*rústas` → `rostes`
- `*rústai` → `roste`
- `*rústi` → `ryst`
- `*rústu` → `rust`

So the missing reusable probe should include at least these cells:
- citation-form comparator: `*rústaz`
- current-row legacy comparator: `*rústō`
- gen.sg. comparator under current project notation: `*rústas`
- dat.sg. comparator: `*rústai`
- high-vowel/i-trigger comparator: `*rústi`
- high-vowel instrumental-singular comparator: `*rústu`

Interpretation: the probe does **not** rescue the citation form. It only shows that the sole regular `rust` output comes from the already-discussed marginal instrumental-singular path.

## Recommended final report

The eventual `### Lexeme report` should say briefly that OE `rust` is an attested masculine noun, that the row's current `*rústō` is philologically wrong and should be separated from the comparative headword `*rústaz`, and that regular citation-form development gives `rost`, leaving `rust` as a genuine u-lowering exception. It may mention the probe result that only `*rústu` yields regular `rust`, but that this is not a defensible retargeting for the citation-form row.

## Data-change recommendations

- **TSV `PROTO`: change.** Recommend `*rústō` → `*rústaz`.
- **TSV `PROTOFORM`: change.** If the row continues to target citation-form `rust`, recommend `*rústō` → `*rústaz` here as well. Do **not** switch to `*rústis`; that proposal is stale under current project notation and live FST behavior.
- **TSV `COUNTERPART`: no change.** Keep `rust`.
- **TSV `DERIVATION_CLASS`: no change.** `unexplained_unmodelled` still fits better than a fake regularization.
- **TSV `NOTE`: change.** Revise it so it reflects the real state of evidence: regular citation-form development from masculine `*rústaz` gives `rost`; `*rústi` gives `ryst`; only marginal `*rústu` gives `rust`; therefore there is no convincing paradigm-cell retargeting for the citation-form row even though one high-vowel comparator exists.
- **`oe_known_problems.tsv`: change.** Update the proto key from `*rústō` to `*rústaz` if the TSV row is corrected; keep the row in the u-lowering-exception bucket.
- **`DEV_NOTES` / dossier text: change.** Clean up or annotate the stale `*rústis → rustes` proposal in §17.10.34 so future packets do not treat it as current live guidance.
