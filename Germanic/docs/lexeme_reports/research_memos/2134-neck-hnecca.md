# Research memo — 2134 neck / hnecca

## Starting point

- **ID / concept / counterpart:** 2134, **neck**, **hnecca**.
- **Live TSV row:** `PROTO=*xnákkaz`, `PROTOFORM=*xnékkô`, `DERIVATION_CLASS=early_analogy`, with an empty `NOTE` and a `HISTORY` field explaining that the earlier TSV form `*xnakkăz` had the wrong class and wrong grade for Old English (`Germanic/data/germanic-aligned-final.tsv:792`).
- **Immediate live state:** the packet’s compact trace already shows the current derivation `*xnékkô -> hnecca`, so this is no longer a live mismatch (`Germanic/docs/lexeme_reports/packets/2134-neck-hnecca.md:17-41`).
- **Core distinction to preserve:**
  1. **cognate-set proto / comparative label:** current TSV `PROTO=*xnákkaz`;
  2. **project input for the OE derivation:** `PROTOFORM=*xnékkô`;
  3. **OE target represented by the row:** attested citation form **hnecca**.

## Packet evidence assessment

- **Authoritative/current:**
  - the aligned TSV row itself (`Germanic/data/germanic-aligned-final.tsv:792`);
  - the packet’s live compact derivation trace showing `*xnékkô -> hnecca` (`Germanic/docs/lexeme_reports/packets/2134-neck-hnecca.md:17-41`);
  - the packet’s row-specific DEV_NOTES excerpts explaining why inherited `*xnakk-` is wrong for OE and why the e-grade matters (`Germanic/docs/lexeme_reports/packets/2134-neck-hnecca.md:69-139`).
- **Useful background:**
  - the packet’s `old_english_wiktionary.tsv` hit confirming **hnecca** as an OE lexeme (`Germanic/docs/lexeme_reports/packets/2134-neck-hnecca.md:145-152`);
  - the packet’s bibliography-key suggestions;
  - the packet’s Orel/Kluge/Seebold references as leads for wider repo checking.
- **Stale or superseded:**
  - the embedded DEV_NOTES line “OE row changed from `*xnakkăz` to `*xnekkô` (both PROTOFORM and PROTO columns)” no longer matches the live TSV, which now keeps `PROTO=*xnákkaz` and only uses `PROTOFORM=*xnékkô` for the derivation (`Germanic/docs/DEV_NOTES.md:3782-3785`; `Germanic/data/germanic-aligned-final.tsv:792`);
  - older diagnostics built around legacy `*xnakkăz` are historical project chronology, not current lexical authority.
- **Irrelevant or misleading:**
  - the packet’s Swadesh hit `neck -> swēora` is a concept-level alternative lexeme, not evidence against **hnecca** for this row (`Germanic/docs/lexeme_reports/packets/2134-neck-hnecca.md:153-158`);
  - the packet has no dossier/analysis hits, but that absence should not be mistaken for proof that no wider repo evidence exists.

## Additional repo research

Beyond the packet, I checked:

- `Germanic/docs/DEV_NOTES.md:3715-3797`, plus the later appendix-table mention at `30628`;
- `Germanic/docs/non_firing_rules_analysis.md:466-478`;
- `Germanic/docs/lexeme_reports/coverage_audit.md:118`;
- `Germanic/data/oe_known_problems.tsv` (**no matching entry for row 2134 / hnecca**);
- `Germanic/data/old_english_wiktionary.tsv:195`;
- `docs/references/kroonen_2011_n_stems.vision.txt:7601-7692`;
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:13122-13125`;
- `docs/references/orel_handbook_germanic_etymology.vision.txt:20861-20866`;
- `docs/references/kluge_seebold_etymologisches_woerterbuch.txt:36064-36068, 65059-65065`;
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:22663`;
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:89387-89388`;
- live FST comparison via `Germanic/tools/oe_full_trace_report.py` against `backend/old_english.bin` and `Germanic/fsts/old_english.bin`.

Main results from that extra pass:

- `kroonen_2011_n_stems.vision.txt` is the strongest direct repo-local source for the ablaut analysis. It explicitly gives `*hnekkō, *hnukkaz 'neck'`, separates e-grade descendants (`OE hnecca`, `OFri. hnekka`, `MLG/MDu. necke`) from a-grade descendants (`ON hnakki`, `OHG ...`, `G Nacken`), and reconstructs a paradigm `*hnekkō, gsg. *hnukkaz, apl. *hnakkuns` (`docs/references/kroonen_2011_n_stems.vision.txt:7601-7669`).
- `Kluge/Seebold` independently supports the same basic split: `Nacken` is from `*hnakka-/ōn`, while `ae. hnecca` and `afr. hnekka` stand “im Ablaut” to it (`docs/references/kluge_seebold_etymologisches_woerterbuch.txt:36064-36068, 65059-65065`).
- `Clark Hall` and `Bosworth-Toller` confirm that **hnecca** is an attested OE masculine headword, not a reconstructed convenience form (`docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:22663`; `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:89387-89388`).
- `Orel` is weaker for this row: it gives `*xnakkaz *xnakkōn` with ON/MLG/OHG evidence but omits OE **hnecca** and does not explain the ablaut (`docs/references/orel_handbook_germanic_etymology.vision.txt:20861-20866`).
- No pilot or full lexeme report for this lexeme appears to exist yet; coverage audit still shows it as uncovered (`Germanic/docs/lexeme_reports/coverage_audit.md:118`).

## Reconstruction and early-stage forms

This row only makes sense if three levels are kept separate.

1. **Current TSV cognate-set proto:** `*xnákkaz`.
   - In the live row this functions as a comparative/cognate-set label, not as the direct OE source form.
   - Philologically it is also the weakest part of the current row, because the repo’s stronger sources treat the word as a weak n-stem and distinguish e-grade and a-grade branches rather than endorsing a simple strong a-stem for OE (`Germanic/data/germanic-aligned-final.tsv:792`; `docs/references/kroonen_2011_n_stems.vision.txt:7601-7669`; `docs/references/kluge_seebold_etymologisches_woerterbuch.txt:65059-65065`).
2. **Project derivational input:** `*xnékkô`.
   - This is the form that actually matters for the OE cascade. Both live bins produce **hnecca** from it.
   - Repo-local support is good: Kroonen’s n-stem discussion explicitly reconstructs e-grade `*hnekkō` and ties it to OE **hnecca** (`docs/references/kroonen_2011_n_stems.vision.txt:7601-7669`).
3. **OE target form:** **hnecca**.
   - This is the attested OE citation form represented by the row, not a reconstructed oblique cell and not a broader semantic gloss set.

The most important historical distinction is therefore not “Proto-Germanic versus Old English” in the abstract, but **which ablaut grade and noun class the OE branch actually continues**. The e-grade branch is the right one for OE; the a-grade branch better explains ON/OHG/German material (`docs/references/kroonen_2011_n_stems.vision.txt:7640-7656`; `docs/references/kluge_seebold_etymologisches_woerterbuch.txt:65059-65065`).

## Old English philology

- **Attested vs. reconstructed:** **hnecca** is attested. `Clark Hall` gives `hnecca m. 'neck'`; `Bosworth-Toller` adds glosses such as `occipitium`, `occiput`, and `cervix, posteriora colli` (`docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:22663`; `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:89387-89388`).
- **Citation form vs. paradigm:** the row targets the ordinary citation/headword form **hnecca**. The memo issue is not a missing OE case-form but the pre-OE reconstruction behind that citation form.
- **Dialect/manuscript status:** the checked repo sources support ordinary lexicographic attestation, but they do not justify a strong dialect-specific claim beyond the dictionary citations already noted.
- **Headword competition:** the packet’s Swadesh `swēora` entry shows that “neck” can map to another OE lexeme in a concept list, but that does not undermine **hnecca** as a valid and attested OE headword for this row (`Germanic/docs/lexeme_reports/packets/2134-neck-hnecca.md:153-158`).

## Project problem and solution

The original project problem was that the inherited comparative proto imported into the row encoded the wrong shape for OE. DEV_NOTES is explicit: legacy `*xnakkăz` was wrong in **declension class** and **root-vowel grade** for Old English, and no ordinary OE sound change will turn that a-grade input into **hnecca** (`Germanic/docs/DEV_NOTES.md:3723-3733`).

The current solution is the right kind of solution:

- keep the OE target as attested **hnecca**;
- feed the cascade with `PROTOFORM=*xnékkô`;
- treat the row as representing the **e-grade branch** of the Germanic ablaut cluster.

That makes the OE derivation regular from the chosen input. The unresolved project issue is documentary consistency: live TSV, live FST behavior, and Kroonen/Kluge-Seebold all support the e-grade OE solution, but the current row still carries `PROTO=*xnákkaz`, and DEV_NOTES still preserves an older stage where both `PROTO` and `PROTOFORM` were said to have been changed together.

## Paradigm probe

A paradigm probe is **not required**.

This is not a `late_analogy` problem where the project must decide between genitive, dative, or other OE paradigm cells. The decisive question is upstream ablaut/stem selection, and the relevant comparator test is already enough: live bins give `*xnékkô -> hnecca`, `*xnakkô -> hnacca`, and legacy `*xnakkăz` no output. No missing OE inflectional cells need to be probed before writing the final report.

## Recommended final report

Recommend a short final `### Lexeme report` that does four things only: (1) state that **hnecca** is an attested OE masculine headword; (2) distinguish current TSV `PROTO` from derivational `PROTOFORM`; (3) explain, with Kroonen 2011 and Kluge/Seebold, that OE belongs to the e-grade branch while German/Norse reflect a-grade generalization; and (4) note that older project history around `*xnakkăz` is diagnostic background, not current authority.

## Data-change recommendations

- **TSV `PROTO`:** **change recommended.** If `PROTO` is meant to be a philological cognate-set headword, it should no longer be bare `*xnákkaz`, since the repo’s stronger sources treat the word as a weak n-stem and distinguish e-grade and a-grade branches. A weak-noun comparative headword such as `*xnakkōn` / Kroonen-style `*hnakka(n)-` would fit the evidence better than the current strong a-stem label.
- **TSV `PROTOFORM`:** **no change recommended.** Keep `*xnékkô`; it is the right OE modelling input and is supported by the strongest repo-local evidence.
- **TSV `COUNTERPART`:** **no change recommended.** Keep **hnecca**.
- **TSV `DERIVATION_CLASS`:** **no change recommended.** `early_analogy` is still a defensible project label for an early branch-level e-grade generalization, and this is not a late-cell selection case.
- **TSV `NOTE`:** **change recommended.** The row’s `NOTE` is currently empty, so a short note should be added explaining that OE **hnecca** reflects the e-grade weak-noun branch (`*xnékkô`), while a-grade forms underlie Germanic relatives such as German `Nacken`.
- **`oe_known_problems.tsv`:** **no change recommended.** The row is not a current unresolved known-problems case.
- **`DEV_NOTES` text:** **change recommended.** Update the neck section so it no longer implies that the live row has both `PROTO` and `PROTOFORM` set to `*xnekkô`, and mark older `*xnakkăz` diagnostics explicitly as historical if they are kept.
- **Dossier / analysis text:** **no dedicated dossier-text change required.** There is no neck-specific dossier to repair. Optional cleanup would only be for archival diagnostics such as `non_firing_rules_analysis.md` if the project wants that file kept strictly current.
