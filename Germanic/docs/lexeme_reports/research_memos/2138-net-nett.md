# Research memo — 2138 net / nett

## Starting point

- **ID:** 2138
- **CONCEPT:** net
- **COUNTERPART:** nett
- **PROTO:** *nátją
- **PROTOFORM:** *nátją
- **DERIVATION_CLASS:** regular
- **NOTE:** Orel: OE nett (geminate); Source: Wiktionary etymology (template:inh)

The live row is a note-bearing regular row. The project’s current derivational input and target are already aligned (`*nátją -> nett`), but the note and packet preserve older project history in which `net` had temporarily been treated as the expected OE form.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the packet’s compact derivation trace, which matches the current debug snapshots and yields `nett`; and the packet’s row-specific `DEV_NOTES.md` section on the resolved ja-stem gemination chronology bug.

**Useful background:** the packet’s reminders that there is no `oe_known_problems.tsv` entry and that older lexical tables exist; the local `old_english_wiktionary.tsv` hit is useful as evidence of a simplified dictionary form `net`, but not as stronger authority than the dictionary and grammar references.

**Stale or superseded:** the packet’s own quoted `DEV_NOTES` lines saying “The TSV expects net” are now stale, because the live TSV already expects `nett`. The packet’s “possibly stale or diagnostic” hits from older `DEV_NOTES`, `notable_findings.md`, and the early apocope investigation belong to pre-fix implementation history and should not be treated as current lexical authority.

**Irrelevant or misleading:** the packet’s analysis hits for `arestoration_r_l_research.md` are false positives on the English word “net”, not lexeme-specific evidence. Any inference that `old_english_wiktionary.tsv: net` alone settles the OE target would also be misleading, because the stronger repo-local dictionary and grammar evidence favors underlying `nett`.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at 12064-12177.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md` and `...with_lexeme_reports.md` — both show live `EXPECTED: nett`, `OUTPUTS: nett`.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.missing_reports.md` — confirms row 2138 still requires a lexeme report because of `NOTE`.
- `Germanic/data/oe_known_problems.tsv` — no entry for this row.
- `Germanic/data/old_english_wiktionary.tsv` — gives `net`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt` — `*natjan ... OE nett`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — headword `nett`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` — simplex and compounds with `nett`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` — PGmc `*natja` with PWGmc `*nati, *nat/t-` and OE `nett`.
- `docs/references/fulk_comparative_grammar_early_germanic.vision.txt` — gemination before `j` is regular after a short vowel.
- `docs/references/campbell_old_english_grammar.txt` — final written simplification of geminates is common, but graphic.
- No pilot lexeme report for `net / nett` is present under `Germanic/docs/lexeme_reports/pilot/`.

No full dossier or lexeme-specific analysis file was named in the packet or TSV note. The broader repo materials that mention `net` outside the row-specific `DEV_NOTES` section are implementation-history documents rather than dedicated lexical dossiers.

## Reconstruction and early-stage forms

This row still needs the usual three-way distinction, even though TSV `PROTO` and `PROTOFORM` are identical.

1. **Cognate-set proto / etymological headword:** dictionary-style scholarship cited in the repo often gives a stem label such as Orel’s `*natjan`.
2. **Project input form:** TSV `PROTOFORM = *nátją`, the project’s PGmc neuter singular input used for the derivation.
3. **OE target form represented by the row:** `nett`.

Ringe-Taylor’s summary is important here: the lexeme belongs to a set with PWGmc variation `*nati, *nat/t-`, but the current project has correctly chosen the geminating path for the OE row. The current FST derivation is therefore not claiming that every West Germanic reflex must show gemination; it is claiming that the OE target represented here is the regular geminated outcome.

## Old English philology

The strongest repo-local philology supports **OE `nett`** as the lexical target.

- **Dictionary support:** Orel gives `OE nett`; Clark Hall gives headword `nett`; Bosworth-Toller’s simplex and compounds (`fengnett`, etc.) likewise support geminate `-tt-`.
- **Orthographic caution:** Campbell §66 says final double consonant symbols are often simplified graphically. That means written `net` can exist as a spelling simplification without proving that the underlying lexical form lacked gemination.
- **Supplementary lexical table:** `old_english_wiktionary.tsv` gives `net`, but this is weaker than the handbook and dictionary evidence above and is best read as a simplified citation form inherited from the Wiktionary table, not as decisive evidence against `nett`.

So the safest philological distinction is:

- **underlying/headword target for this row:** `nett`;
- **possible graphic simplification in transmission or secondary lexical tables:** `net`.

This is not a reconstructed-WS problem or a paradigm-cell problem. It is mainly a headword/orthography judgment about whether the OE row should preserve the historically regular geminate.

## Project problem and solution

The project problem was a collision between older implementation history and the stronger lexical evidence.

Earlier repo work had a stage where `*natją` was routed through premature `j` vocalization, producing non-geminated outcomes (`net`, `nete`, even older diagnostic `netta`). The row-specific `DEV_NOTES` section now explains the fix: West Germanic gemination must precede the `j`-loss/vocalization sequence, yielding `*nattją` and ultimately `nett`.

The live row already reflects the right project solution:

- keep the cognate-set row on `*nátją` / `*natjan`-type material;
- keep the OE target as `nett`, not `net`;
- treat `net` only as a possible graphic simplification or weaker lexical-table normalization, not as the preferred lexical counterpart.

## Paradigm probe

A paradigm probe is **not required** for this row.

The issue is not hidden cell selection or analogical competition between paradigm cells; the same lexeme-level input already derives the intended citation form. A probe would add little, because the dispute is about gemination chronology and OE headword choice, not about whether nominative, genitive, dative, or plural cells point to different project targets.

If the supervisor nonetheless wants a minimal diagnostic check later, it should not be framed as a paradigm probe but as a derivational sanity check of the single citation-form path `*nátją -> nett`.

## Recommended final report

Recommend a short final report stating that row 2138 now correctly derives and targets **OE `nett`**, with support from Orel, Clark Hall, Bosworth-Toller, and the current FST trace. It should note briefly that spelling `net` can reflect graphic simplification or weaker table normalization, but that the row’s preferred OE counterpart is the geminated form.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended; `nett` is the best-supported OE target.
- **TSV `DERIVATION_CLASS`:** no change recommended; this remains a `regular` row with a note, not a paradigm-cell or reconstructed-OE case.
- **TSV `NOTE`:** **change recommended.** The current note still leans on “Source: Wiktionary etymology” and should be tightened so it foregrounds the stronger repo-local authorities: Orel/Clark Hall/Bosworth-Toller support `nett`, while `net` is at most a simplified spelling.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** **change recommended** in `Germanic/docs/DEV_NOTES.md` at the resolved bug section, because lines saying “The TSV expects `net`” and “This should probably be `nett`” are now stale relative to the live TSV. No dossier cleanup is needed, because no dedicated dossier was found for this lexeme.
