# Research memo — 2184 shove / sċēaf

## Starting point
- ID `2184`; CONCEPT `shove`; COUNTERPART `sċēaf`.
- TSV `PROTO` = `*skéubaną`; TSV `PROTOFORM` = `*skáub`; TSV `DERIVATION_CLASS` = `late_analogy`.
- TSV note: the row now represents the 1/3 sg. preterite of `*sċūfan`, retargeted away from older 3pl pret. `*skúbun -> sċufon`; the note treats `sċēaf` as the genuinely Lautgesetzlich and corpus-attested cell, while OE infinitive `sċūfan` is the analogical `ū`-present.
- No pilot/full lexeme report for this row turned up in `Germanic/docs/lexeme_reports/pilot/`; the packet is a starting dossier, not final authority.

## Packet evidence assessment
- **Authoritative/current:** the live TSV row; the packet's compact trace `*skáub -> sċēaf`; `DEV_NOTES` §17.51.A1.4; `Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md`; and the current publish snapshot showing `PROTO: *skáub`, `OUTPUTS: sċēaf`.
- **Useful background:** `Germanic/docs/dossiers/bugun-scufun-attestation.md` for why the earlier 3pl solution is philologically weak as a lexeme-specific target; `old_english_wiktionary.tsv` for the ordinary citation headword `sċūfan`; and reference snippets in Brunner, Clark Hall, Bright, and Seebold showing the paradigm `scūfan/scēofan, sċēaf, scufon, scofen`.
- **Stale or superseded:** the older April-2026 `DEV_NOTES` section that declared the issue solved by retargeting to `*skubun -> sċufon`; the packet's preserved diagnostic hits around `*skeubăną -> sċēofan` vs. `sċūfan`; and the dossier's hybrid suggestion to keep an analogical 3pl row alongside a new `sċēaf` row. Those are important project history, but not the live row analysis.
- **Irrelevant or misleading:** packet hits about `*skuflō` / shovel and other concept-only `shove` mentions are root-family background, not evidence for this row's selected OE target; likewise `old_english_wiktionary.tsv` headword `sċūfan` should not be mistaken for support that the row ought to target the infinitive.

## Additional repo research
Checked beyond the packet: `Germanic/docs/DEV_NOTES.md` (especially the current §17.51.A1.4 closure at 43939-43998 and the older superseded April-2026 note at 14354-14513), `Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md`, `Germanic/docs/dossiers/bugun-scufun-attestation.md`, `Germanic/docs/dossier-medial-u-lowering-conditioning-2026.md`, `Germanic/docs/dossiers/widuwe-u-preservation.md`, `Germanic/docs/lexeme_reports/coverage_audit.md`, `Germanic/data/oe_known_problems.tsv`, `Germanic/data/old_english_wiktionary.tsv`, and reference files for Clark Hall, Bright, Brunner, and Seebold. I also spot-checked the live FST helper via `old_english.bin`: `*skéubaną -> sċēofan` and `*skáub -> sċēaf` are confirmed directly, which reinforces the need to keep citation-form and selected-cell evidence separate.

## Reconstruction and early-stage forms
This row needs the usual three-way distinction. TSV `PROTO` `*skéubaną` is the cognate-set / etymological proto headword for the verb 'shove'. TSV `PROTOFORM` `*skáub` is not that headword but the PGmc 1/3 sg. preterite cell chosen as the row's derivational input. The OE target is correspondingly not the citation infinitive `sċūfan` (or its attested variant `scēofan`) but the inflected preterite `sċēaf`. Repo history also preserves two other paradigm cells that matter as alternatives: old 3pl pret. `*skúbun -> sċufon` in the superseded project stage, and past participle `*skúbanaz -> sċofen` in the dossier's alternative recommendation.

## Old English philology
`Sċēaf` is an attested verbal preterite form, not a reconstructed placeholder and not the noun `sceaf` 'bundle'. The repo-local dossier and reference snippets treat it as well attested in both poetic and prose transmission (`Beowulf`, `Maldon`, Ælfric, etc.), while Clark Hall and Bright give the standard paradigm under the dictionary headword `scūfan`. That headword issue matters: OE is lexicographically cited as `sċūfan`, and Brunner/Kroonen/Seebold also preserve the variant `scēofan`, but the row intentionally targets the preterite cell because the citation form belongs to the analogically remodelled present system.

## Project problem and solution
The project problem was never the singular preterite; it was the analogical present and the misleadingly attractive 3pl workaround. First, the inherited infinitive path `*skéubaną -> sċēofan` did not match the ordinary late-WS citation form `sċūfan`, because the present system had been remodelled with analogical `ū`. Then the project temporarily switched to 3pl pret. `*skúbun -> sċufon`, which looked like a regular escape hatch. The later dossier and attestation work showed that this 3pl solution was not the right lexeme-level anchor: it stays entangled with analogical `-on` overlay and lacks direct support for an earlier `-un` form in this specific verb. The current solution `*skáub -> sċēaf` is better because it is both corpus-attested and the cleanest Lautgesetzlich cell in the paradigm; the past participle `*skúbanaz -> sċofen` remains a serious but secondary alternative.

## Paradigm probe
A paradigm probe **is required** for this `late_analogy` row, but the reusable probe is still missing: `Germanic/tools/oe_paradigm_probe.py` has no built-in `shove / sċēaf` specification. The dossier already performs the substantive philological survey, so the missing work is standardization, not discovery. The probe should cover at least these cells:
- infinitive `*skéubaną -> sċēofan`;
- 1/3 sg. pret. `*skáub -> sċēaf`;
- pret. pl. `*skúbun` against the attested/project-history plural target `sċufon`;
- past ptcp. `*skúbanaz -> sċofen`.
Optionally add 2 sg. pret. `*skúbi -> sċufe` as a control cell, but the four cells above are the minimum set needed to show why the row now targets the singular preterite.

## Recommended final report
Recommend a concise final report that explicitly separates `*skéubaną` (cognate-set proto), `*skáub` (selected PGmc paradigm cell), and `sċēaf` (attested OE target), while noting that `sċūfan/scēofan` remains the citation-form background and that the old `*skúbun -> sċufon` stage is superseded project history rather than the live analysis.

## Data-change recommendations
- **TSV `PROTO`:** no change.
- **TSV `PROTOFORM`:** no change.
- **TSV `COUNTERPART`:** no change.
- **TSV `DERIVATION_CLASS`:** no change.
- **TSV `NOTE`:** no required change; the current note already states the retargeting logic clearly enough.
- **`oe_known_problems.tsv`:** no change; this is no longer an active known-problem row.
- **`DEV_NOTES` / dossier text:** optional cleanup recommended. The older April-2026 `DEV_NOTES` section that presents `*skubun -> sċufon` as the resolution should be marked even more explicitly as superseded by §17.51.A1.4, so packet generation does not surface it as if it were still live guidance.
