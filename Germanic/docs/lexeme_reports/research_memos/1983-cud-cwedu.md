# Research memo — 1983 cud / cwedu

## Starting point
- ID `1983`; CONCEPT `cud`; COUNTERPART `cwedu`.
- Live TSV `PROTO` = `*kwíθuz`; live TSV `PROTOFORM` = `*kwéðuz`; TSV `DERIVATION_CLASS` = `attested_variant`.
- TSV note already gives the current intended analysis: Kroonen/Orel/Ringe–Taylor support an e-grade, voiced-dental proto; OE attests a variant set `cwedu`, `cwidu`, `cweodu`, `cwudu`, `cudu`; and the direct FST path now runs `*kwéðuz -> cwedu`.
- A pilot report already exists at `Germanic/docs/lexeme_reports/pilot/cud.md`, but it is background only, not final authority.

## Packet evidence assessment
- **Authoritative/current:** the live TSV row; the packet trace showing `*kwéðuz -> cwedu`; and `DEV_NOTES §17.14`, which gives the full source survey, explains why `*kwíθuz` was wrong, and verifies the current FST output.
- **Useful background:** `pilot/cud.md`; the packet's extract from the older March 2026 DEV_NOTES section; and `widuwe-u-preservation.md` where Campbell/Ringe–Taylor quotations independently confirm the OE variant chain `cwidu > cwudu > cudu` and list `cweodu` beside it.
- **Stale or superseded:** the packet's older `DEV_NOTES` material at lines 6009-6085, which still frames `cudu` as the expected target and predates the later attested-variant framing; `Germanic/docs/non_firing_rules_analysis.md`, which still has the obsolete sample `*kwiθuz -> cwiþ (expected cudu)`; and the live TSV `PROTO` field, which still preserves the old reconstruction even though the note and later DEV_NOTES section no longer support it.
- **Irrelevant or misleading:** generic packet keyword hits on unrelated Anglian analysis files; and `old_english_wiktionary.tsv` if its headword `cudu` is mistaken for the row's required target rather than a dictionary normalization.

## Additional repo research
Checked beyond the packet: `Germanic/docs/DEV_NOTES.md` at lines 6009-6085 and `§17.14` (28401-28519), `Germanic/docs/lexeme_reports/pilot/cud.md`, `Germanic/docs/dossiers/widuwe-u-preservation.md` (especially Campbell and Ringe-Taylor canvass sections that cite `cwidu/cwudu/cudu/cweodu`), `Germanic/docs/non_firing_rules_analysis.md`, `Germanic/data/old_english_wiktionary.tsv`, `Germanic/data/oe_known_problems.tsv`, `Germanic/docs/lexeme_reports/report_manifest.tsv`, and `Germanic/docs/lexeme_reports/coverage_audit.md`. I also verified directly that `printf 'kwéðuz' | flookup -i backend/old_english.bin` returns `cwedu`, while `kwíθuz` still returns `cwiþu`.

## Reconstruction and early-stage forms
The row needs a strict three-way distinction.
- **Cognate-set proto / etymological headword:** this should be PGmc `*kwéduz` (Kroonen's citation style `*kweduz`, with Leiden `d` standing for intervocalic `[ð]`), not the old `*kwíθuz`.
- **Project input form for OE derivation:** `*kwéðuz` is the right explicit phonological input, because the OE pipeline hardens `ð > d` by rule and then reaches `cwedu` directly.
- **OE target form:** `cwedu` is the attested conservative OE e-grade variant chosen for this row.

The comparative argument in `DEV_NOTES §17.14` is coherent: PIE `*gʷet-u-` plus Sanskrit `jatú` supports original `*t`, Verner's Law gives PGmc `*ð`, ON `kváða/kvoða` preserves the voiced dental directly, and OHG `quiti/kuti` fits PWGmc hardening from `*ð` to `*d`. `cwidu` is not the proto-stage; it is the later levelled OE/WGmc i-grade member of the paradigm.

## Old English philology
`cwedu` should be treated as an attested OE form, not as a reconstructed convenience output. But it is also not the ordinary dictionary headword across repo-local materials: `old_english_wiktionary.tsv` gives `cudu`, Kroonen cites `cwidu, cweodu, c(w)udu`, and the older DEV_NOTES section grouped the lemma under `cwedu/cwidu/cudu`. The note's claim that `cwedu` is a conservative West Saxon e-grade form therefore matters: the row is intentionally selecting one attested variant from a wider lexical set, not claiming that the other spellings are wrong.

The philological distinctions that matter for the final report are: attested `cwedu` versus the more levelled `cwidu`; dialectal/phonological variants `cweodu`, `cwudu`, `cudu`; and the fact that the u-stem history is supported by forms such as Ringe-Taylor's cited gen.sg. `cwidwes`. This is a variant-selection problem, not an unattested-WS reconstruction problem.

## Project problem and solution
The project originally conflated two different issues: (1) a wrong proto reconstruction (`*kwíθuz`) and (2) uncertainty about which OE lexical variant to target (`cudu` as dictionary-like headword versus attested conservative `cwedu`). The current solution is basically right: keep `COUNTERPART = cwedu`, keep `DERIVATION_CLASS = attested_variant`, and keep `PROTOFORM = *kwéðuz` so the FST derives the intended form directly. The remaining problem is that the live TSV `PROTO` field still carries the obsolete cognate-set reconstruction, so the row still mixes corrected derivational input with stale etymological metadata.

## Paradigm probe
No new paradigm probe is required. This row is not using a hidden oblique test cell in the way `late_analogy` items do; it is selecting an attested nominative/citation-form variant. The only paradigm fact worth mentioning is the u-stem support from forms like `cwidwes`, and that can be handled in prose from the existing sources rather than by a new probe table.

## Recommended final report
Recommend a concise final report that says row 1983 targets attested OE `cwedu`, a conservative e-grade member of a wider variant set (`cwidu`, `cweodu`, `cwudu`, `cudu`), and that the real reconstruction issue was correcting the proto from old `*kwíθuz` to PGmc `*kwéduz` / derivational `*kwéðuz`.

## Data-change recommendations
- **TSV `PROTO`:** yes, change `*kwíθuz` to `*kwéduz` (or the repo's equivalent Kroonen-style citation form), because the live field is stale and no longer matches the note or `DEV_NOTES §17.14`.
- **TSV `PROTOFORM`:** no change; keep `*kwéðuz`.
- **TSV `COUNTERPART`:** no change; keep `cwedu`.
- **TSV `DERIVATION_CLASS`:** no change; keep `attested_variant`.
- **TSV `NOTE`:** yes, minor editorial cleanup is recommended once `PROTO` is fixed, so the note explicitly distinguishes `PROTO = *kwéduz` from `PROTOFORM = *kwéðuz` and states that `cwedu` is the chosen attested variant rather than the only OE lemma.
- **`oe_known_problems.tsv`:** no change.
- **DEV_NOTES/dossier text:** yes, light cleanup is recommended. The older March 2026 DEV_NOTES section and stale diagnostic text such as `non_firing_rules_analysis.md` should be marked as superseded so future packets do not over-weight the obsolete `*kwiθuz` / `cudu` state.
