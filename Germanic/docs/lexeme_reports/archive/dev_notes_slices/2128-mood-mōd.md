---
row_id: 2128
concept: mood
counterpart: mōd
proto: *mōdaz
protoform: *mōdaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: Germanic/docs/lexeme_reports/coverage_audit.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2128 mood / mōd

## Current row state

- CONCEPT: `mood` [Germanic/data/germanic-aligned-final.tsv:768].
- COUNTERPART: `mōd` [Germanic/data/germanic-aligned-final.tsv:768].
- PROTO: `*mōdaz` [Germanic/data/germanic-aligned-final.tsv:768].
- PROTOFORM: `*mōdaz` [Germanic/data/germanic-aligned-final.tsv:768].
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:768].
- Repo-local row identity is stable across the live aligned TSV and the OE lexical import table: both give `mood / mōd`, and the coverage audit marks row `2128` as a regular row that previously had no note coverage [Germanic/data/germanic-aligned-final.tsv:768; Germanic/data/old_english_wiktionary.tsv:189; Germanic/docs/lexeme_reports/coverage_audit.md:311].
- Comparative and lexicographic framing is likewise straightforward. Orel gives `*mōdaz` with OE `mód` 'mind, spirit, courage', and Bright indexes `mōd, n., mood, mind, courage, pride`, so the current target is a normal inherited noun row rather than a paradigm-cell workaround or a mismatch-repair row [docs/references/orel_handbook_germanic_etymology.vision.txt:30827-30831; docs/references/bright_anglo_saxon_reader.vision.txt:23247-23250].

## Development-note summary

No securely attachable **dedicated** row-2128 DEV_NOTES dossier currently survives in `Germanic/docs/DEV_NOTES.md`. A targeted search of current DEV_NOTES turns up no noun-side block for `*mōdaz -> mōd`; the only lexeme-family hits are indirect references to derivative `mōdig (< *mōdagaz)` inside the OE `-ag > -ig` discussion and its later source audit [Germanic/docs/DEV_NOTES.md:12418-12434; Germanic/docs/DEV_NOTES.md:26224-26234]. This slice is therefore a replacement working note, not a condensation of a lost row-specific section.

The securely current claim for this row is narrower and simpler than many neighboring slices. `PROTO = *mōdaz` is the comparative lexeme-level reconstruction carried in the aligned TSV, `PROTOFORM = *mōdaz` is the same form reused as the present project input because no paradigm-cell substitution is in play, and the OE target is normalized noun `mōd` [Germanic/data/germanic-aligned-final.tsv:768]. Nothing in current repo-local row materials suggests a need to retarget the row, introduce an analogical cell, or preserve a mismatch history; the live TSV, the OE lexical import table, and the coverage audit all point instead to a stable regular row with previously missing note coverage [Germanic/data/germanic-aligned-final.tsv:768; Germanic/data/old_english_wiktionary.tsv:189; Germanic/docs/lexeme_reports/coverage_audit.md:311].

Because the row-specific DEV_NOTES authority is missing, local philological support has to come from the references rather than from invented project archaeology. Orel's entry explicitly reconstructs `*mōdaz` and gives OE `mód` with the sense range 'mind, spirit, courage', while Bright's glossary independently records `mōd, n., mood, mind, courage, pride` and inflected forms such as gen.sg. `mōdes` and dat.sg. `mode` [docs/references/orel_handbook_germanic_etymology.vision.txt:30827-30831; docs/references/bright_anglo_saxon_reader.vision.txt:23247-23250]. Those citations support the current noun row directly and make clear that the slice should describe `mōd` as an ordinary inherited OE noun with a broad semantic field, not as a special-case engineering problem.

The indirect DEV_NOTES material still has limited value if handled carefully. The `mōdig` references matter because they show that current DEV_NOTES already treats `mōd-` as a productive lexical base inside the project and cites Campbell for the `-ag > -ig` history of the derivative adjective [Germanic/docs/DEV_NOTES.md:12423-12434; Germanic/docs/DEV_NOTES.md:26226-26234]. But those passages are about `*mōdagaz -> mōdig`, not about `*mōdaz -> mōd`; they belong under secure background/context, not under row-specific authority for the noun itself [Germanic/docs/DEV_NOTES.md:12423-12434; docs/references/orel_handbook_germanic_etymology.vision.txt:30814-30819, 30827-30831].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-12418-12434

- Source heading: `OE Unstressed -ag Raising (Campbell §376)`
- Source line or section hint: `lines 12418-12434`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `background`
- Issue tags: `mōdig_derivative`; `lexeme_family`; `suffix_history`; `campbell`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This fragment is not a row-2128 noun note, but it is the clearest current DEV_NOTES place where the `mōd-` lexeme family surfaces. DEV_NOTES sets out the rule `*-ag > -æg > -eg > -ig / _g#` and says the change is part of the broader `-ig` pattern, listing `mōdig (< *mōdagaz)` alongside `halig` and `bodig` as examples [Germanic/docs/DEV_NOTES.md:12418-12434]. For row 2128, the usable takeaway is only that current project notes already recognize a derivative built on `mōd-` and treat that derivative as regular under Campbell's `-ag > -ig` account; the fragment should **not** be repurposed as if it supplied a noun-side derivation or a special history for `*mōdaz -> mōd` [Germanic/docs/DEV_NOTES.md:12423-12434; docs/references/orel_handbook_germanic_etymology.vision.txt:30814-30819, 30827-30831].

### DEV_NOTES:line-26224-26234

- Source heading: `Sources (opinio communis)`
- Source line or section hint: `lines 26224-26234`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `background`
- Issue tags: `mōdig_derivative`; `campbell`; `suffix_etymology`; `lexeme_family`
- Recommended next use: `check_against_literature`
- Shared with row IDs:

This later source-audit fragment is again indirect but still worth indexing because it preserves the explicit handbook framing behind the derivative. DEV_NOTES quotes Campbell §275(7) that the suffix `-ig` represents earlier `-æg` and includes `mōdig` among the examples, then quotes Campbell §376 that `e > i` before `g` is seen in that same suffix history [Germanic/docs/DEV_NOTES.md:26224-26234]. For row 2128, this is best treated as bibliographic background showing that the project's `mōd-` family material is being tied to standard OE handbooks; it does **not** create dedicated current authority for the noun row, whose direct support still comes from the live TSV and independent lexical references to `mōd` itself [Germanic/docs/DEV_NOTES.md:26226-26234; Germanic/data/germanic-aligned-final.tsv:768; docs/references/orel_handbook_germanic_etymology.vision.txt:30827-30831; docs/references/bright_anglo_saxon_reader.vision.txt:23247-23250].

## Superseded or diagnostic material

No securely attachable superseded row-2128 dossier was found in current DEV_NOTES. The main interpretive danger is not loss of a known current note but over-reading the surviving `mōdig` material: those passages belong to derivative adjective history and should be marked as indirect background if later extracted into reports [Germanic/docs/DEV_NOTES.md:12418-12434; Germanic/docs/DEV_NOTES.md:26224-26234].

It would likewise be misleading to manufacture a project-history problem for this row merely because the slice had to be rebuilt from sparse evidence. The live row is already regular `*mōdaz -> mōd`, the OE lexical import table agrees, and the coverage audit marks the gap as missing note coverage rather than as an unresolved philological defect [Germanic/data/germanic-aligned-final.tsv:768; Germanic/data/old_english_wiktionary.tsv:189; Germanic/docs/lexeme_reports/coverage_audit.md:311].

## Open questions for later work

- If later literature cleanup reaches this row, add a cleaner dictionary-headword citation from Clark Hall or Bosworth-Toller for bare `mōd`; the present replacement note relies mainly on Orel plus Bright because those were the clearest repo-local extracts recovered quickly for the noun itself [docs/references/orel_handbook_germanic_etymology.vision.txt:30827-30831; docs/references/bright_anglo_saxon_reader.vision.txt:23247-23250].
- If a packet or research memo is created later, add the full stage trace for `*mōdaz -> mōd`; no row-local packet or memo currently survives, so this slice cannot yet quote an internal derivational probe.
- If `index.tsv` is updated later, index both preserved DEV_NOTES fragments explicitly as **indirect lexeme-family material** rather than as row-specific noun authority, so later extraction does not mistake `mōdig` evidence for direct `mōd` evidence [Germanic/docs/DEV_NOTES.md:12418-12434; Germanic/docs/DEV_NOTES.md:26224-26234].
