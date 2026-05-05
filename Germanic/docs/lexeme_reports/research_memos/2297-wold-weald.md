# Research memo — 2297 wold / weald

## Starting point

- **ID / concept / counterpart:** 2297, **wold**, **weald**.
- **TSV `PROTO`:** `*wálθuz`.
- **TSV `PROTOFORM`:** `*wálθuz`.
- **`DERIVATION_CLASS`:** `regular`.
- **Current TSV note:** `Kroonen p.572 *walθu- > OE weald; wald is Anglian (R/T p.313 WS wealdan vs Merc. waldan)`.
- No pilot lexeme report appears to exist for this row in `Germanic/docs/lexeme_reports/pilot/`, so the packet is only a starting dossier.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*wálθuz -> weald`; `DEV_NOTES.md:30639`; and `analysis/arestoration_r_l_research.md:747`, all of which agree that this row is a straightforward **breaking** case and that the live cascade already outputs `weald`.
- **Useful background:** the packet's citation of Kroonen for PGmc `*walþu-` and its lexical-table hit `old_english_wiktionary.tsv: wold -> wald`, which is relevant as background for variant/headword handling.
- **Stale or superseded:** there is no row-specific superseded dossier in the packet. The duplicated debug-snapshot material is only a mirror of live data, not independent evidence.
- **Irrelevant or misleading if read too quickly:** the packet's many generic `Anglian` hits from unrelated files (`widuwe`, `meord`, `rēc`, etc.) are not evidence for row 2297 itself. They only show that Anglian variation exists elsewhere in the project. Likewise, the Ringe-Taylor citation in the TSV note is directly about **wealdan / waldan**, so for this noun it is analogical support, not primary noun attestation by itself.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` around line 30639.
- `Germanic/docs/analysis/arestoration_r_l_research.md`.
- `Germanic/data/old_english_wiktionary.tsv`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `Germanic/docs/lexeme_reports/pilot/` (no existing pilot report found).

Main findings from that wider check:

- Kroonen gives PGmc **`*walþu-`** and cites OE **`weald`** as the Old English outcome; this is the strongest repo-local etymological authority for the noun.
- Ringe-Taylor explicitly give **WS `wealdan` ~ Merc. `waldan`** for the cognate verb. That strongly supports the TSV note's claim that **`wald`** is an Anglian-type form in the same phonological environment, but it remains supporting comparison rather than the noun's main lexicographic evidence.
- Clark Hall is especially helpful for OE headword status: it lists **`weald`** as the main noun ('forest, wood, grove') and cross-refers both **`wald`** and **`wold`** to **`weald`**. That makes `weald` the normalized dictionary headword within repo-local reference material, with `wald`/`wold` treated as variants.
- `old_english_wiktionary.tsv` gives **`wold -> wald`**. That is useful as a signal that the Anglian-looking form exists in supplementary tables, but it is not better authority than Kroonen + Clark Hall for the row target.
- `oe_known_problems.tsv` has no live entry for this row, which fits the fact that the sound-law derivation itself is not broken.

## Reconstruction and early-stage forms

This row also needs a three-way distinction, even though TSV `PROTO` and `PROTOFORM` currently coincide.

1. **Cognate-set proto / etymological headword:** Kroonen's PGmc stem **`*walþu-`** for the noun family.
2. **Project derivational input:** TSV `PROTOFORM` **`*wálθuz`**, i.e. the nominative singular input form actually fed to the cascade.
3. **OE target form:** **`weald`**, the normalized Old English citation form represented by the row.

The packet's derivation path is philologically plausible and not in dispute at project level: `*wálθuz` > PWGmc `*wálduz` > NWGmc `*wáldu` > OE brightening `*wældu` > OE breaking `*wealdu` > apocope **`weald`**. The important memo point is that OE **`wald`** should not be confused with the PGmc/project input. It is a later Old English dialectal variant, not an alternative protoform.

## Old English philology

- **Attested vs. reconstructed:** repo-local dictionary material treats **`weald`** as the main OE noun headword. Clark Hall also cross-refers **`wald`** and **`wold`** to that headword, so variant spellings/forms are real background, but they do not displace `weald` as the primary lemma.
- **Citation form vs. inflected form:** this row targets a citation-form noun, not a special oblique cell. Nothing in the evidence suggests that the row should be recast as a paradigm-cell entry.
- **Dialect/manuscript status:** the local evidence supports **`wald`** as an Anglian/Northumbrian-type variant (Clark Hall `wald (N, VPs) weald`; Ringe-Taylor's WS/Mercian verb comparison), but the memo should not overstate a full noun-distribution map that the repo has not assembled.
- **Dictionary/headword issue:** Kroonen and Clark Hall both point to **`weald`** as the normalized OE lemma. The supplementary Wiktionary-derived table's `wald` is therefore background evidence about variants, not a reason to retarget the row.

## Project problem and solution

The project problem here is not a failed derivation. The FST already yields the live target **`weald`**. The real issue is how to interpret the note's Anglian aside and the supplementary lexical-table form **`wald`** without collapsing variant evidence into the row target.

The current row is best understood as follows:

- the row models the normalized OE noun **`weald`**;
- the note preserves the useful fact that **`wald`** is a dialectal/Anglian variant in the same lexical family;
- no retargeting is needed, because repo-local lexicography still prefers **`weald`** as the headword.

So the solution is to keep the row as a regular `weald` row and mention `wald` only as variant background in later report prose.

## Paradigm probe

A paradigm probe is **not required** for this row.

The row's issue is lexical headword normalization versus dialectal variant evidence, not uncertainty about a particular inflectional cell. The nominative singular target `weald` is already supported and the live cascade already matches it.

## Recommended final report

Recommend a short lexeme report stating that row 2297 is a regular noun with PGmc etymon `*walþu-` / project input `*wálθuz`, that the live OE output **`weald`** is the normalized headword supported by Kroonen and Clark Hall, and that **`wald`** (with `wold` as a cross-referred variant spelling) should be mentioned only as Anglian/background evidence rather than as the row target.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** **change recommended**. The current note is basically right, but it should say more clearly that `weald` is the normalized OE target/headword and that `wald` is only variant background. Ideally it should rely less exclusively on the verbal comparison `wealdan ~ waldan` and mention noun-headword support such as Kroonen/Clark Hall.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` text:** no change recommended; the current `breaking` classification is adequate.
- **Dossier text:** no change recommended; there is no row-specific dossier needing cleanup here.
