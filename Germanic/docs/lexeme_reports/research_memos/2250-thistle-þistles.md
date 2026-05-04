# Research memo — 2250 thistle / þistles

## Starting point

- **ID:** 2250
- **CONCEPT:** thistle
- **COUNTERPART:** þistles
- **PROTO:** *θéstilaz
- **PROTOFORM:** *θístilas
- **DERIVATION_CLASS:** late_analogy
- **NOTE:** Paradigm-cell target: GenSg þistles (masc. a-stem). NomSg simplex *þistl is unattested in OE manuscripts; the only attested simplex NomSg is broken þistel (via late-WS svarabhakti, Campbell §§360–363, Hogg §§6.30–6.36), which is not modeled in this FST since the other ten -Cl/Cn/Cm# rows (bōsm, botm, hæsl, nǣdl, ofn, hræfn, scofl, stefn, tācn, wǣpn) deliberately target unbroken Beowulf-poetic / early / Anglian forms. GenSg þistles is fully attested as the inflectional stem and lautgesetzlich (medial cluster, no parasiting; Campbell §363 textbook trio). See DEV_NOTES §17.18.

The live row is already a paradigm-cell solution. A pilot report exists at `Germanic/docs/lexeme_reports/pilot/thistle.md`, but for memo purposes it is background only, not final authority.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet trace showing `*θístilas -> þistles`; `DEV_NOTES.md` §17.18.7, which records the current policy of keeping the other ten cluster nouns unbroken while moving only thistle to an attested gen.sg. cell; and the packet's paradigm probe as a current verification aid for the selected row.
- **Useful background:** `notable_findings.md` §8 and the older `DEV_NOTES.md` 2026-03-18 thistle section for the real `*e/*i` etymological dispute; the pilot `thistle.md`; `old_english_wiktionary.tsv`; and dictionary-style headword material confirming simplex `þistel`.
- **Stale or superseded as live-row authority:** packet excerpts from the 2026-03-18 phase where the row still targeted nominative `þistel` from `*θistilaz`; the older mismatch framing in `analysis/fryhtu_investigation.md`; and the packet's resurfaced exact-pair history around `*θístilaz -> þistel`, which is real project history but no longer the active row design after §17.18.7.
- **Irrelevant or misleading:** packet hits that only capture broad workflow metadata or unrelated Anglian discussions; and any reading of the March 2026 `*θistilaz -> þistel` material as if it overrode the present gen.sg. row.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md`, especially the 2026-03-18 thistle discussion and the later §17.18 cluster-cell decision.
- `Germanic/docs/analysis/notable_findings.md` §8.
- `Germanic/docs/analysis/fryhtu_investigation.md` (older diagnostic background, now superseded for this row).
- `Germanic/tools/oe_paradigm_probe.py` (built-in `thistle:þistles` pilot probe exists).
- `Germanic/data/oe_known_problems.tsv` (no entry for row 2250).
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/docs/lexeme_reports/coverage_audit.md` and `pilot/thistle.md`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt`.
- `docs/references/kluge_seebold_etymologisches_woerterbuch.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/pokorny_iew_pages/00000526.txt`.

This extra pass clarifies two separate questions that the packet alone can blur: the etymological `*e/*i` controversy belongs to the cognate-set headword problem, while the live row itself is now a paradigm-cell choice about which OE form should be derived.

## Reconstruction and early-stage forms

This row needs a strict three-way distinction.

1. **Cognate-set proto / etymological headword:** TSV `PROTO` is `*θéstilaz`. In current project usage this functions as the cognate-set headword and preserves the Orel-style `*e` reconstruction as background etymology, not as the form actually fed through the OE derivation.
2. **Project input form for derivation:** TSV `PROTOFORM` is `*θístilas`, the selected **gen.sg.** paradigm cell. This is the live row input, and it already encodes the project decision to use `*i` in the derivational form.
3. **OE target form:** `þistles`, likewise a **gen.sg.** form, is the attested OE target represented by the row.

The repo's March 2026 history shows why this split exists. Orel gives `*þe(x)stilaz`; Kluge-Seebold gives `*þistila-`; Pokorny material supports the prick-root line behind the `*i` tradition; and all Germanic daughters cited in `notable_findings.md` show `i`. Even if one keeps `*θéstilaz` as the etymological headword, the derivational row no longer depends on deriving OE from that exact citation-form proto. The live row instead says: headword-level controversy remains, but the OE derivation is run from the selected gen.sg. input `*θístilas`.

One live inconsistency should be noted explicitly: `DEV_NOTES.md` §17.18.7.2 says "retain `*θístilaz`" for `PROTO`, but the live TSV and packet use `*θéstilaz`. For memo purposes the TSV is the authority; the `DEV_NOTES` wording should be treated as stale or mistaken project history, not as current row data.

## Old English philology

The philology is comparatively clear once citation form and inflected form are separated.

- **Attested simplex/headword:** OE dictionaries in the repo give broken simplex `þistel`/`ðistel` as the ordinary headword.
- **Unattested simplex target:** unbroken `*þistl` is not supported as an attested simplex nominative in the repo's project notes; it survives only as the inflectional stem and in discussions of the unbroken cluster.
- **Attested inflected target:** `þistles` is directly attested as the gen.sg. / oblique stem form and is phonologically regular for a medial cluster where parasite-vowel insertion does not apply.
- **Dialect/register issue:** broken `þistel` belongs to the late-WS/normalized simplex tradition; the project deliberately does **not** generalize that parasitic-vowel treatment across the whole `-Cl/-Cn/-Cm#` class because the other ten rows are being kept in unbroken poetic / early / Anglian-looking forms.
- **Compound evidence:** `DEV_NOTES` notes compounds such as `þistel-twige` and `þistel-mere`, which show restored broken `þistel-` at the composition boundary; that supports the headword tradition but does not undo the fact that the selected row target is the unbroken oblique `þistles`.

So the safest statement is: `þistel` is the attested citation form, `þistles` is an attested inflected form, and the row intentionally represents the latter because it is where attestation and the current FST policy line up most cleanly.

## Project problem and solution

The project problem was not the existence of OE `þistel`; it was that the live FST policy for this cluster class yields unbroken word-final clusters, so a direct nominative-style run produces unattested `*þistl` rather than the normalized simplex `þistel`. Generalizing late-WS parasiting would fix thistle but would also disturb the ten parallel rows that the project intentionally keeps unbroken.

The current solution is therefore narrow and coherent:

- keep the cluster-class policy for the ten comparable nouns;
- keep `PROTO` as the cognate-set/etymological headword;
- switch only this row's `PROTOFORM` and `COUNTERPART` to the attested, lautgesetzlich gen.sg. pair `*θístilas -> þistles`.

`late_analogy` remains a defensible class label because the row is still being handled specially due to the analogically/orthographically reshaped simplex tradition, even though the chosen gen.sg. cell itself is regular.

## Paradigm probe

A paradigm probe **is required** for a `late_analogy` row like this, and the repo already has one: the packet, pilot report, and `oe_paradigm_probe.py` all include the hand-specified `thistle:þistles` comparison.

So there is **not** a blocking missing probe. But the current v1 probe is still narrower than ideal: it compares etymological `PROTO` nom.sg. `*θéstilaz` against selected gen.sg. `*θístilas` and explicitly omits the alternative `*i`-root nominative plus other oblique cells. Before the final report, the probe should be expanded to include at least:

- the project-input **nom.sg.** `*θístilaz` -> expected non-match `þistl`;
- the winning **gen.sg.** `*θístilas` -> `þistles`;
- at least one additional oblique/plural control cell corresponding to the attested unbroken stem (`þistlas` or another straightforward oblique), so the gen.sg. is not the only non-nominative comparison point.

## Recommended final report

Recommend a concise final report that says row 2250 is a paradigm-cell entry: `PROTO = *θéstilaz` is retained as the disputed cognate-set headword, `PROTOFORM = *θístilas` is the selected gen.sg. derivational input, and `COUNTERPART = þistles` is the attested OE target. It should mention broken simplex `þistel` as the ordinary OE headword and explain that the row avoids making late-WS parasiting the active derivational policy for the whole cluster class.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended. Keeping `*θéstilaz` is acceptable if the project intends `PROTO` to remain the etymological/cognate-set headword rather than the exact derivational input.
- **TSV `PROTOFORM`:** no change recommended. `*θístilas` is the right live gen.sg. input.
- **TSV `COUNTERPART`:** no change recommended. `þistles` is the right current OE target.
- **TSV `DERIVATION_CLASS`:** no change recommended. `late_analogy` remains defensible.
- **TSV `NOTE`:** **change recommended.** The current note explains the paradigm-cell switch well, but it should add one explicit sentence distinguishing `PROTO` (etymological headword) from `PROTOFORM` (selected gen.sg. input), because the row now depends on that distinction.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** **change recommended.** The 2026-03-18 thistle section should be marked more explicitly as superseded for the live row after §17.18.7, while remaining usable as background on the `*e/*i` controversy; and the inconsistent §17.18.7.2 wording about retaining `PROTO = *θístilaz` should be corrected or annotated so it no longer conflicts with the live TSV `PROTO = *θéstilaz`.
