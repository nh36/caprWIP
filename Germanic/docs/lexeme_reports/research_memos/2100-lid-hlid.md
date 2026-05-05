# Research memo — 2100 lid / hlid

## Starting point

- **ID / concept / counterpart:** 2100, **lid**, **hlid**.
- **TSV `PROTO`:** `*xlídą`.
- **TSV `PROTOFORM`:** `*xlídą`.
- **`DERIVATION_CLASS`:** `regular`.
- **Current TSV note:** `Proto: *liθuz → *xlidą (Wiktionary *hlidą 'lid, cover')`.
- There is **no pilot lexeme report** for this row in `Germanic/docs/lexeme_reports/pilot/`, so the packet and wider repo evidence have to be weighed directly.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row and the compact derivation trace are current, and they agree that the present project input and OE target are `*xlídą > hlid`. The packet’s `DEV_NOTES` and `notable_findings` passages are most useful where they explicitly distinguish direct source claims from the project’s own extension to OE, especially the later caution that onset-velar blocking is **not** stated for Old English in Cercignani and is instead a project hypothesis supported by the OE outcomes `hlid` and `fyrhtu`.
- **Useful background:** the packet’s regression-history passages are still useful for explaining why this row matters in implementation terms: without the onset-velar condition the FST produced `hled`, and the repair restored `hlid`. The `old_english_wiktionary.tsv` hit is also useful as a quick lexical confirmation that `hlid` is a real OE form.
- **Stale or superseded:** the packet also includes earlier repo prose that states the result too strongly, e.g. the claim that the implementation “confirms” onset-velar blocking as a real OE phenomenon. That wording is superseded by the later, more careful repo position that the OE extension is a successful project analysis, not an explicitly attested traditional sound law.
- **Irrelevant or misleading:** the packet’s bare “no dossier hit” state should not be read as evidence that no wider source base exists; the real philological support lies in the reference texts and lexicographic files checked outside the packet. The TSV note’s earlier `*liθuz` stage is background etymology, not the row’s live PGmc modelling input.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` around the full onset-velar discussion and later direct-source verification.
- `Germanic/docs/analysis/notable_findings.md` around the implementation summary and the later clarification that the OE extension is the project’s own hypothesis.
- `Germanic/data/oe_known_problems.tsv`, which has no row-specific entry for `hlid`.
- `Germanic/data/old_english_wiktionary.tsv`, which gives `lid -> hlid`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`, which confirms that row 2100 requires report coverage because the TSV `NOTE` is non-empty.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.md`, which shows the current placeholder state but is only implementation output, not independent authority.
- `docs/references/lloyd_1966_a_umlaut_of_i.txt`, where OE `hlid` appears in a cross-dialect retention set with ON `hliþó` and OHG `(h)lit`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt`, which gives the lexical reconstruction as `*xliđan sb.n.` with OE `hlid`.
- `docs/references/seebold_vergleichendes_woerterbuch.vision.txt`, which likewise supports a neuter `*hlid-` lexeme with OE `hlid`, OFris `hlid`, and OS `hlid`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` and `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`, which support OE `hlid` as an attested noun meaning ‘lid/cover/door/gate’ and help separate it from the distinct topographic noun `hlið`.
- `docs/refs.bib`, which confirms that `Lloyd1966` and `Cercignani1980` are live bibliography keys if the eventual final report needs them.

This wider pass supports the live row while also showing that the repo contains both careful and over-strong formulations of the same implementation story.

## Reconstruction and early-stage forms

This row is easiest to handle if three levels are kept distinct.

1. **Earlier etymological background:** the TSV note mentions `*liθuz > *xlidą`. That earlier `*liθuz` stage is background derivational history only; it is not the live row’s OE target and should not replace the row’s PGmc modelling form.
2. **Cognate-set proto / project modelling proto:** TSV `PROTO = *xlídą`. Here `PROTO` and `PROTOFORM` are intentionally the same, because this is not a paradigm-cell workaround row.
3. **OE target form:** `hlid`, the attested OE citation form represented by the row.

Reference notation differs slightly from the TSV: Orel writes `*xliđan sb.n.`, and Seebold has a stem-class style `hlid-a-m (n)`. Those are compatible with the project’s normalized `*xlídą`; they do not argue for a different row target. The important distinction is therefore not between two competing PGmc lexemes, but between the older background preform `*liθuz` and the live derivational input `*xlídą`.

## Old English philology

- **Attested vs. reconstructed:** `hlid` is attested in repo-local lexicographic sources; this is not a reconstructed OE convenience form.
- **Citation form vs. inflected forms:** the row targets the citation form `hlid`, not an oblique paradigm cell. Clark Hall also records plural forms such as `hlidu, hleodu`, but those are background inflectional facts, not evidence that the row should target another cell.
- **Dictionary/headword issue:** Clark Hall distinguishes `hlid` ‘lid, covering, door, gate, opening’ from separate `hlið` ‘cliff, precipice, slope, hill-side’. The row is clearly the former. The cross-linguistic comparanda likewise show semantic spread (‘lid/cover’ in OE, OFris, OS; ‘gate/opening’ in ON), so the memo should not collapse the OE noun with the unrelated topographic homograph.
- **Literature on vowel history:** Lloyd uses `hlid` as one of the forms where `i` is retained across several dialects; he does **not** explain it by an OE-specific onset-velar rule, and indeed argues more broadly against a regular a-umlaut of `i`. That caution matters for how the project should describe this row.

## Project problem and solution

The project problem is explanatory rather than lexical. The row already targets the right OE lemma; the issue is why the model should keep `i` and output `hlid` instead of lowering to `hled`.

The current project solution is:

- keep `PROTO = PROTOFORM = *xlídą`;
- keep `COUNTERPART = hlid`;
- explain the successful derivation through the current implementation’s onset-velar blocking condition.

That solution is acceptable, but the memo should state it carefully. The repo’s best current position is **not** “scholarship proves an OE onset-velar sound law.” It is “the implementation now matches `hlid`, and the repo interprets this with an OE onset-velar blocking hypothesis that extends a pattern discussed for Old Icelandic, while later repo notes explicitly acknowledge that this OE extension is our own inference.” That distinction is the main thing the eventual final report must preserve.

## Paradigm probe

**No paradigm probe is required.**

This is not a row where `PROTOFORM` selects a non-lemma cell, and nothing in the checked evidence suggests that the correct outcome depends on choosing among competing OE paradigm cells. The issue is the treatment of prehistoric `i`-lowering, not unresolved noun morphology.

If a future appendix ever wanted an illustrative noun check anyway, the most relevant cells would be citation-form `hlid` and the plural forms `hlidu/hleodu`; but no such probe is needed for the memo stage or for the current row decision.

## Recommended final report

Recommend a short final report stating that OE `hlid` is an attested lemma regularly produced by the current cascade from `*xlídą`, while the non-empty note exists because the project explains retained `i` through a cautiously framed onset-velar blocking hypothesis. The report should distinguish background `*liθuz`, live modelling input `*xlídą`, and attested OE target `hlid`, and it should avoid presenting the OE onset-blocking claim as directly inherited from Cercignani.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended. `regular` is appropriate.
- **TSV `NOTE`:** **change recommended.** The current note is too compressed and risks collapsing background `*liθuz` with the live row input `*xlídą`; it would be better to say explicitly that the row models OE `hlid` from `*xlídą`, while the earlier `*liθuz` stage is only etymological background and the retained `i` is a project explanation issue.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** **light cleanup recommended.** `DEV_NOTES` and `Germanic/docs/analysis/notable_findings.md` should be harmonized so that stronger wording like “confirms a real OE onset-velar phenomenon” is clearly subordinated to the later, current caution that this is the project’s own OE extension rather than an explicit traditional claim. There is no separate row-specific dossier file to revise.
