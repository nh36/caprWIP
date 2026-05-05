# Research memo — 2141 nightmare / mare

## Starting point

- **ID:** 2141
- **CONCEPT:** nightmare
- **COUNTERPART:** mare
- **PROTO:** *márōn
- **PROTOFORM:** *márōn
- **DERIVATION_CLASS:** regular
- **NOTE:** Unattested OE compound *nihtmare; second element is OE mare 'nightmare' (n-stem fem., < PWGmc *mara, *marōn-, cf. ON mara, OHG mara). Per Ringe & Taylor *Development of Old English* vol. 2 p. 192 the attested OE forms are mare (nom.sg.), maran (obl.), and variant mere. Earlier target mære reflected Wiktionary headword (Orel-style spelling) and was conflated with the unrelated OE adjective mǣre 'famous' (< PGmc *mēriz, jō/jā-stem); corrected per §17.28.

This is a note-bearing regular row. The concept-side reconstruction `*nihtmare` is not itself the attested OE target: the live row now deliberately targets simplex `mare`, with the unattested compound left in the note as background only.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*márōn -> mare`; the packet's excerpts from `DEV_NOTES.md` §17.28; and the packet's `analysis/arestoration_r_l_research.md` quotation from Ringe & Taylor giving OE `mare, maran, and mere` [@RingeTaylor2014].

**Useful background:** the packet's older diagnostic `DEV_NOTES` hits showing how `mære` was recognized as a target problem before the correction landed; the packet's Orel citation, which is relevant for explaining where the stale `mære` headword came from even though it is not the best OE-philological authority [@Orel2003].

**Stale or superseded:** the packet's `old_english_wiktionary.tsv` hit `nightmare -> mære`; the older mismatch-log excerpts where row 2141 still carried target `mære`; and the packet's inherited analysis-table row that still labels 2141 as `mære` and "out of scope of short A-restoration." Those are useful as project chronology, not as current evidence.

**Irrelevant or misleading:** the packet's "no manifest entry" line is workflow metadata, not lexical evidence; and generic repo hits on unrelated `mære` or `mere` lexemes should not be allowed to blur together the nightmare noun, the sea-word `mere`, and the adjective `mǣre`.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` §17.28 directly.
- `Germanic/docs/analysis/arestoration_r_l_research.md` directly, including the earlier stale affected-rows table.
- `Germanic/data/oe_known_problems.tsv` — no entry for row 2141 / `*márōn`.
- `Germanic/data/old_english_wiktionary.tsv` — still has stale `mære` for English “nightmare”.
- `docs/refs.bib` — confirms usable keys `[@RingeTaylor2014]`, `[@Orel2003]`, and `[@ClarkHall1960]`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` — direct repo-local support for OE `mare, maran, and mere` [@RingeTaylor2014].
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — direct entries `mare ... nightmare, monster` and `mera m. incubus` [@ClarkHall1960].
- `docs/references/orel_handbook_germanic_etymology.vision.txt` — comparative lemma `*marōn` with OE `mære`, useful as background for the stale secondary tradition but not decisive for OE targeting [@Orel2003].
- No pilot lexeme report for nightmare / mare was found under `Germanic/docs/lexeme_reports/pilot/`.

No dedicated dossier was named in the packet or TSV note; the clearly relevant full analysis file named there was `arestoration_r_l_research.md`, and it was checked directly.

## Reconstruction and early-stage forms

Three levels need to stay distinct:

1. **Cognate-set proto / comparative headword:** comparative work treats the lexeme as PGmc/PNWGmc `*marōn-`, with PWGmc paradigm material `*mara, *marōn-` behind the OE forms [@RingeTaylor2014; @Orel2003].
2. **Project derivational input:** TSV `PROTO = PROTOFORM = *márōn`, the single form fed to the OE derivation pipeline.
3. **OE target form for this row:** attested simplex `mare`, not reconstructed compound `*nihtmare`.

At the early sound-change level, the current project solution is coherent: the row's input is an n-stem form whose pre-OE fronted stage is then A-restored before a surviving back-vocalic ending, yielding OE `mare`; Ringe & Taylor's paradigm line confirms the broader outcome set `mare, maran, and mere` [@RingeTaylor2014]. The important project distinction is therefore not between two competing protoforms, but between the comparative lexeme-level paradigm and the specific OE form the row chooses to represent.

## Old English philology

This memo should keep three philological distinctions explicit.

- **Attested simplex vs reconstructed compound:** repo-local evidence supports simplex OE `mare`; the compound `*nihtmare` is reconstructed and explicitly unattested.
- **Citation form vs oblique/paradigm evidence:** Ringe & Taylor give `mare` as the nominative singular and `maran` as the oblique form, with variant `mere` also noted [@RingeTaylor2014].
- **Dictionary/headword issue:** Clark Hall directly supports `mare` as the nightmare noun and also has `mera m. incubus`, which fits the repo's warning that variant `mere/mera` belongs to the attested tradition, whereas long-vowel `mære` belongs to a weaker secondary headword tradition [@ClarkHall1960].

The safe philological statement is therefore: OE had an attested nightmare lexeme `mare`, with oblique `maran` and a variant `mere/mera`; what is unattested is the exact compound `*nihtmare`, not the simplex noun. The row should not imply that `mære` is the attested normalized target.

## Project problem and solution

The project problem was a mixed **headword and row-targeting error**. Older repo history and Wiktionary-derived material treated `mære` as the OE equivalent for “nightmare,” apparently on Orel-style comparative authority and with some risk of conflation with unrelated adjective `mǣre` [@Orel2003]. But the stronger repo-local OE evidence points to `mare`, not `mære`, and the FST output `mare` was already regular.

The current project solution is the right one:

- keep `PROTO = PROTOFORM = *márōn`;
- keep `COUNTERPART = mare`;
- keep `DERIVATION_CLASS = regular`;
- treat `*nihtmare` as an unattested concept-level reconstruction mentioned in the note, not as the attested OE target of the row.

If the project ever wanted a row whose actual OE target was reconstructed `*nihtmare`, that would be a different editorial decision and probably a different row type. It is not what the current live row represents.

## Paradigm probe

A paradigm probe is **not required** for this memo.

The decisive issue is already settled by source hierarchy: this row is not an unresolved paradigm-cell selection problem, but a corrected simplex-target problem. If an explanatory probe is ever wanted anyway, the most useful cells would be:

- nominative singular `*márōn -> mare`;
- oblique stem/cell yielding `maran`;
- optional variant note for `mere/mera`.

That would be confirmatory only, not a prerequisite for the final report.

## Recommended final report

Recommend a short final report saying that row 2141 now correctly targets attested OE simplex `mare` for the concept “nightmare,” while `*nihtmare` remains only an unattested conceptual reconstruction; the earlier `mære` target came from stale Orel/Wiktionary-style headwording, whereas stronger OE evidence supports `mare`, `maran`, and variant `mere/mera` [@RingeTaylor2014; @ClarkHall1960].

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** no change recommended; the live note already captures the essential correction and the attested/simplex-versus-unattested/compound distinction.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** no change recommended; `DEV_NOTES` §17.28 already preserves the correction history adequately, and no dedicated dossier exists for this lexeme.
- **Additional non-requested cleanup:** `Germanic/data/old_english_wiktionary.tsv` still preserves stale `nightmare -> mære`, and `Germanic/docs/analysis/arestoration_r_l_research.md` still contains an older affected-rows line with target `mære`. Those are not blockers for the final report, but they remain worth future cleanup or explicit historical labelling.
