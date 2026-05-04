# Research memo — 1936 ban / bannes

## Starting point

- **ID:** 1936
- **CONCEPT:** ban
- **COUNTERPART:** bannes
- **PROTO:** *bánną
- **PROTOFORM:** *bánnas
- **DERIVATION_CLASS:** late_analogy
- **NOTE:** Gen.sg. paradigm cell: *bannas → bannes. Word-final geminates are phonologically simplified; using gen.sg. preserves medial geminate. Note: a-stem neuter, gen.sg. same as masc.

The live TSV already treats this as a paradigm-cell row, not as a straight lemma-to-lemma match. A pilot report exists (`pilot/ban.md`), but it should be treated as background only.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the packet’s compact derivation trace showing `*bánnas → bannes`; the main `DEV_NOTES.md` section at 13663–13803 explaining the geminate-stem paradigm-cell solution; and the pilot paradigm probe showing `*bánną → ban` vs. `*bánnas → bannes`.

**Useful background:** the packet’s excerpts from `DEV_NOTES.md` on unstressed fronting and the note that neuter a-stems share gen.sg. `-es`; the packet’s manifest notice that a pilot report already exists.

**Stale or superseded:** older development history in the packet that still frames the row as `*banną → bann` before the TSV update; repo notes outside the packet that still treat row 1936 as a verb `*banną → bannan` are superseded by the current noun/paradigm-cell analysis.

**Irrelevant or misleading:** the packet’s local lexical-table hit `old_english_wiktionary.tsv: ban → bannan` is verb data, not noun evidence for this row; broad “gen.sg.” search hits for unrelated lexemes are methodological parallels, not direct evidence for `ban`.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/lexeme_reports/pilot/ban.md` — useful background, but not final authority.
- `Germanic/tools/oe_paradigm_probe.py` — confirms the existing pilot probe is hand-specified and compares only nom.sg. vs gen.sg.
- `Germanic/data/oe_known_problems.tsv` — no entry for this row/proto.
- `Germanic/data/old_english_wiktionary.tsv` — gives `bannan`, showing a verb/noun mismatch in that supplementary table.
- `Germanic/docs/germanic_notes/analogical_leveling_analysis.md` and `Germanic/docs/non_firing_rules_analysis.md` — both preserve stale pre-update history treating 1936 as verbal `bannan`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt` — `*bannan` sb.n., OE `ge-bann`.
- `docs/references/seebold_vergleichendes_woerterbuch.vision.txt` — distinguishes masculine `bann-a-z` and neuter `bann-a-m`; cites OE `gebann`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — headword `+bann` n. ‘proclamation, summons, command’.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` — headword `ge-bann` with oblique forms such as `to cyniges gebanne`.
- `docs/references/campbell_old_english_grammar.txt` plus the quoted Brunner/Kurath/Hogg discussion preserved in `DEV_NOTES.md` — support final-geminate simplification and the contrast with medial geminate preservation.

## Reconstruction and early-stage forms

The three levels need to stay separate:

1. **Cognate-set proto / etymological headword:** TSV `PROTO` `*bánną`, i.e. the noun represented at the lexeme level. Repo reference material also supports a PGmc bann-stem noun (`*bannan` in Orel’s citation style; Seebold distinguishes both masc. and neut. bann-stems).
2. **Project input form:** TSV `PROTOFORM` `*bánnas`, a selected **gen.sg.** paradigm cell.
3. **OE target form:** `bannes`, the project’s OE **gen.sg.** target cell, not the citation lemma.

The phonological point is straightforward: `*bannas` keeps the geminate medial before the suffix and regularly yields `bannes` via unstressed fronting/merger; `*banną` yields phonological `ban`, because final geminates simplify. So `PROTOFORM` is not a rival proto-lexeme; it is the chosen inflectional input for this row.

## Old English philology

Repo-local lexicographic evidence supports the **noun** (`+bann`, `ge-bann/gebann`) but not, in the materials checked, a clean direct citation for the exact unprefixed gen.sg. **`bannes`**. Clark Hall gives `+bann`; Bosworth-Toller and Orel/Seebold point especially to prefixed `gebann`. Bosworth-Toller also shows oblique `gebanne`, confirming real inflectional use of the noun.

That means the exact project target should presently be treated as a **regular inferred OE gen.sg. cell**, not as a securely cited dictionary headword. The pilot report’s wording about an “actually attested Old English form” is stronger than the repo evidence currently shown. Philologically, the key contrast is:

- **citation/headword:** `bann` / `gebann` (noun lexeme);
- **selected inflected cell:** `bannes` (project target);
- **phonological nominative outcome from `*bánną`:** `ban`, with final geminate simplification.

## Project problem and solution

The project problem is not the existence of the noun, but the mismatch between lexeme headword practice and OE final-geminate phonology. If the row targeted the citation form `*bánną`, the FST would give `ban`, while traditional OE headword spelling often preserves doubled `nn` by analogy from inflected forms. The project’s solution is therefore to target the inherited **gen.sg.** cell `*bánnas → bannes`, where the geminate remains medial and the sound laws produce the desired form without hacks.

So the row is best read as: “OE bann-noun, represented in the report by its conservative gen.sg. cell,” not as “the OE headword is bannes,” and definitely not as the older abandoned verb row `bannan`.

## Paradigm probe

A paradigm probe **is required**, and one already exists in the packet/pilot workflow. For this row, the current probe is sufficient for the core decision because it tests the decisive contrast:

- **nom.sg.** `*bánną → ban` (non-match)
- **gen.sg.** `*bánnas → bannes` (match)

No additional probe is required before a final report. If later expansion is desired, the next useful cells would be **dat.sg.** and **nom./acc.pl.**, but that is optional completeness work, not a current blocker.

## Recommended final report

Recommend a concise final report that says the lexeme-level proto is `*bánną`, the TSV input is the gen.sg. `*bánnas`, and the OE target `bannes` is a paradigm-cell solution chosen because OE final geminates simplify while medial geminates survive. It should avoid claiming direct attestation for exact `bannes` unless a specific citation is added.

## Data-change recommendations

- **TSV PROTO:** no change recommended.
- **TSV PROTOFORM:** no change recommended.
- **TSV COUNTERPART:** no change recommended for now; `bannes` works as the project’s selected OE gen.sg. target.
- **TSV DERIVATION_CLASS:** no change recommended; `late_analogy` still fits the paradigm-cell solution.
- **TSV NOTE:** **change recommended** — tighten the wording so it says this is the project’s selected/inferred gen.sg. cell, and do not imply stronger direct attestation than the repo currently documents.
- **`oe_known_problems.tsv`:** no change recommended; this is not an unmodelled FST failure.
- **DEV_NOTES / dossier text:** **change recommended** in stale background material. The old verb-oriented analyses in `germanic_notes/analogical_leveling_analysis.md` and `non_firing_rules_analysis.md` should be marked historical or cleaned up, and any pilot/dossier prose that calls `bannes` directly attested should be softened unless a citation is supplied.
