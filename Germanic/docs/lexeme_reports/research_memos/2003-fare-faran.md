# Research memo — 2003 fare / faran

## Starting point

- **ID:** 2003
- **CONCEPT:** fare
- **COUNTERPART:** faran
- **PROTO:** *fáraną
- **PROTOFORM:** *fáraną
- **DERIVATION_CLASS:** regular
- **NOTE:** OE target faran (inf. of str.v. class VI 'to fare, go'). Earlier note had færan, conflated with i-umlauted 2/3sg pres fær(e)þ or with weak causative færan 'to frighten' (< *fōrjaną); on the §17.26.0 hypothesis the wrong target was set to match the pre-§17.25 buggy FST output. Corrected per DEV_NOTES §17.26.

This is a note-bearing regular row. `coverage_audit.md` marks row 2003 as report-requiring because the TSV `NOTE` is non-empty, and no pilot/full lexeme report for this lexeme was found.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*fáraną -> faran`; the packet's excerpts from `DEV_NOTES.md` §17.26; and the packet's hit from `Germanic/docs/analysis/arestoration_r_l_research.md`, which agrees that the corrected OE infinitive is `faran`.

**Useful background:** the packet's bibliography-key table and its quotations from Fulk, Campbell, Ringe/Taylor, and Brunner are genuinely relevant, because repo reference files do support the distinction between infinitive `faran`, umlauted present forms such as `færst/færð`, and the separate weak verb `færan`.

**Stale or superseded:** packet excerpts preserving the old mismatch state (`*fáraną` versus TSV `færan`) are project history only. They are useful for explaining how the mistake arose, but not for deciding the present target.

**Irrelevant or misleading:** many packet keyword hits under generic `i-umlaut` searches point to unrelated analyses or dossiers and should not be promoted into lexeme evidence. Likewise `Germanic/data/old_english_wiktionary.tsv` maps modern English **fare** to OE noun `fær` 'journey', which is a different lexeme and therefore misleading for row 2003.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` §17.26 and the surrounding mismatch log.
- `Germanic/docs/analysis/arestoration_r_l_research.md`.
- `Germanic/docs/analysis/notable_findings.md`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `Germanic/data/oe_known_problems.tsv` — no entry for row 2003 / `*fáraną` / `faran`.
- `Germanic/data/old_english_wiktionary.tsv` — supplementary but misleading here, because it gives noun `fær` for English “fare”.
- `docs/refs.bib` — confirms usable keys `[@Kroonen2013]`, `[@Orel2003]`, `[@RingeTaylor2014]`, `[@Campbell1959]`, `[@SieversBrunner1965]`, `[@Fulk2018]`, `[@ClarkHall1960]`, and `[@BosworthToller1898]`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` — comparative lemma `*faran-` with OE `faran` [@Kroonen2013].
- `docs/references/orel_handbook_germanic_etymology.vision.txt` — comparative lemma `*faranan` with OE `faran`, and separate `færan` under the causative entry [@Orel2003].
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` — derives `*faraną` to OE `faran`, with umlauted 2sg/3sg present forms [@RingeTaylor2014].
- `docs/references/campbell_old_english_grammar.txt` — cites `faran` as a textbook A-restoration example and gives class-VI present/participle forms [@Campbell1959].
- `docs/references/brunner_1965_altenglische_grammatik.txt` — cites `faran` as the standard class-VI verb, while also recording some secondary umlauted infinitive variants in less strict/dialectal material [@SieversBrunner1965].
- `docs/references/fulk_comparative_grammar_early_germanic.vision.txt` — distinguishes infinitive `faran` from pp. `faren- < *faræn- < *faran-` [@Fulk2018].
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` and `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` — distinguish verb `faran` from weak `færan/feran` 'to frighten' [@ClarkHall1960; @BosworthToller1898].

No dedicated faran dossier was named in the row note; the one clearly relevant full analysis file named in the packet is `arestoration_r_l_research.md`, and it was checked directly.

## Reconstruction and early-stage forms

Three levels need to stay separate:

1. **Cognate-set proto / etymological headword:** repo dictionaries use lemma-style comparative forms `*faran-` [@Kroonen2013] and `*faranan` [@Orel2003]. Those are cognate-set headwords, not the TSV's exact derivational input.
2. **Project input form:** TSV `PROTO` and `PROTOFORM` are both `*fáraną`, the singular verbal input actually fed to the derivational pipeline.
3. **OE target form:** normalized OE infinitive `faran`, the citation form the row is meant to represent.

The early chronology is straightforward. Comparative and handbook sources support PGmc `*faraną` > pre-OE fronted `*færaną`, then OE A-restoration back to `*faraną`, with later reduction/apocope yielding `faran` [@RingeTaylor2014; @Campbell1959]. Fulk's discussion is important because it explains why the past participle can show fronting (`faren- < *faræn- < *faran-`) without making the infinitive fronted as well [@Fulk2018].

The weak causative `færan` belongs to a different proto-base (`*fōrjaną` / `*fōrjan-`), so it must not be collapsed with the strong verb row [@Orel2003; @Kroonen2013].

## Old English philology

This is an **attested** OE verb, not a reconstructed-OE target. Clark Hall gives headword `faran`, and separately gives `færan` 'to frighten' plus `fære/færst/færð` as present-tense forms of `faran` [@ClarkHall1960]. Bosworth-Toller likewise distinguishes `faran` from `féran`/`færan` [@BosworthToller1898].

Philologically, the row should target the citation infinitive, not a different paradigm cell. Campbell explicitly treats class-VI `faran` as the pattern with analogical `a` spreading through forms such as subjunctive `fare`, present participle `farende`, and past participle `faren` [@Campbell1959]. Brunner also treats `faran` as the standard class-VI infinitive while noting that some less strict WS/Anglian traditions show secondary infinitive variants such as `fseran/fearan` by analogical spread from umlauted present forms [@SieversBrunner1965]. Those variant spellings are real background, but they do **not** justify making normalized TSV `COUNTERPART` `færan` without an explicit dialect/manuscript rationale.

## Project problem and solution

The project problem was not an unresolved sound law. It was a **row-targeting mistake**: an older TSV target `færan` matched the pre-fix buggy FST output and then acquired an explanatory note that blurred together three different things:

- the class-VI infinitive `faran`;
- umlauted 2sg/3sg present forms such as `færst/færð`;
- the separate weak causative `færan` 'to frighten'.

The current project solution is the right one:

- keep `PROTO = PROTOFORM = *fáraną`;
- keep `COUNTERPART = faran`;
- keep `DERIVATION_CLASS = regular`;
- treat the note as correction history explaining why the row once drifted to the wrong target.

So row 2003 is now a corrected regular citation-form derivation, not a paradigm-cell workaround and not a known-unmodelled exception.

## Paradigm probe

A paradigm probe is **not required** for this memo.

The decisive issue is already settled by handbook and dictionary evidence: the row targets the infinitive `faran`, while umlauted present forms belong to other cells and weak `færan` is a different lexeme. If a later appendix wants a compact explanatory probe anyway, the most useful cells would be:

- infinitive `*fáraną -> faran`;
- 2sg present `*farizi -> færst`;
- 3sg present `*faridi -> færð`;
- past participle stem `*faranaz -> faren/færen`.

That would be explanatory confirmation, not a prerequisite for the final report.

## Recommended final report

Recommend a short final report that says the row is now a corrected regular derivation: comparative proto lemmas (`*faran-`, `*faranan`) and the project input `*fáraną` all point to OE citation-form `faran`; the earlier `færan` target came from stale project history plus conflation with umlauted present forms and the separate weak causative. A paradigm-probe subsection can be omitted unless the supervisor wants an explicit cell-contrast table.

## Data-change recommendations

- **TSV PROTO:** no change recommended.
- **TSV PROTOFORM:** no change recommended.
- **TSV COUNTERPART:** no change recommended.
- **TSV DERIVATION_CLASS:** no change recommended.
- **TSV NOTE:** no change recommended; the current note already records the correction and the source of the earlier error.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** no change recommended. `DEV_NOTES` §17.26 and `arestoration_r_l_research.md` already preserve the needed project history without needing further cleanup.
