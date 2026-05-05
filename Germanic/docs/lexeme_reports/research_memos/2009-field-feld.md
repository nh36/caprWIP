# Research memo — 2009 field / feld

## Starting point

- **ID / concept / counterpart:** 2009, **field**, **feld**.
- **TSV `PROTO`:** `*félθuz`.
- **TSV `PROTOFORM`:** `*félθuz`.
- **`DERIVATION_CLASS`:** `regular`.
- **Current TSV note:** `R/T §5.1.3 p.171: *felθu-/*feldu- may reflect Verner's alternation or regular PWGmc *lθ→*ld; either gives OE feld`.
- There is **no pilot lexeme report** for this row in `Germanic/docs/lexeme_reports/pilot/`, so the packet and wider repo evidence have to be weighed directly.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row, the packet's compact derivation trace, and the row-specific `DEV_NOTES` hits at `Germanic/docs/DEV_NOTES.md:1334-1356` and `:24453-24459` are current. Together they show the implemented project position: the live input is `*félθuz`, the FST now outputs `feld`, and the project treats `feld` as a case where the existing `*lþ > ld` machinery is sufficient even though Ringe-Taylor also note possible Verner-style alternation.
- **Useful background:** `old_english_wiktionary.tsv` usefully confirms that `field -> feld` is a real OE lexical pairing, but it does not address the internal historical question behind `-ld-`. The packet's coverage-audit style traces are also useful only for showing that the row requires a report because `NOTE` is non-empty.
- **Stale or superseded:** the packet's diagnostic mention of `Germanic/docs/non_firing_rules_analysis.md` (`*felθuz -> feolþ`) is old regression history, not current row evidence; the live FST no longer behaves that way. The packet's broad concept-name hits from older debugging prose are likewise implementation archaeology rather than authority.
- **Irrelevant or misleading:** the packet's analysis/dossier hits from `compound_archaism_inventory.md`, the `mismatch_dossier_mizdo*` files, `notable_findings.md`, and `dossiers/g-palatalisation-conditioning.md` are false-positive file mentions caused by generic words like `Field` or `field`; after checking them, they do not supply row-specific evidence for `feld`.

## Additional repo research

Files checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md`.
- `Germanic/docs/non_firing_rules_analysis.md`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `Germanic/data/oe_known_problems.tsv`.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/tools/oe_paradigm_probe.py`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/campbell_old_english_grammar.txt`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.
- The packet-named but non-row-specific files `Germanic/docs/analysis/compound_archaism_inventory.md`, `Germanic/docs/analysis/mismatch_dossier_mizdo.md`, `Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md`, `Germanic/docs/analysis/notable_findings.md`, and `Germanic/docs/dossiers/g-palatalisation-conditioning.md`.
- Direct live-FST verification via `oe_full_trace_report` helper: `*félθuz -> feld`, and `*félduz -> feld` in the current binary.

Main findings from that wider pass:

- `oe_known_problems.tsv` has **no entry** for this lexeme, which matches the row's current status as a solved regular derivation rather than an unresolved exception.
- `Ringe & Taylor` explicitly treat OE `feld` as one of the ambiguous examples where either inherited `*þ ~ *d` alternation or regular West Germanic `*lþ > ld` could underlie the OE form.
- `Campbell` independently supports both parts of the philological picture: `feld` belongs among OE forms with `d` beside Germanic `þ`, and early OE place-name spellings in `-felth` preserve the older dental fricative spelling historically.
- `Kroonen`, `Clark Hall`, and `Bosworth-Toller` all support `feld` as a genuine OE lexical item; `Clark Hall` and `Bosworth-Toller` also preserve inflected forms (`felda`, `felde`, `feldum`, rare `felða`) showing mixed u-stem/a-stem behaviour.
- The packet-named mizdō and palatalisation dossiers are unrelated background only and should not be treated as evidence for row 2009.

## Reconstruction and early-stage forms

This row is straightforward only if the three levels are kept separate.

1. **Cognate-set proto / etymological headword:** TSV `PROTO = *félθuz`. This is the comparative Proto-Germanic form represented by the row.
2. **Project input form used for derivation:** TSV `PROTOFORM = *félθuz`. Unlike an `early_analogy` or `late_analogy` case, the project is not feeding a special oblique cell or remodelled pre-OE form into the cascade here.
3. **OE target form:** `feld`, the Old English lemma represented by the row.

The uncertainty lies not in the live TSV distinction but in the earlier historical interpretation of medial `-ld-`:

- `Ringe & Taylor` allow two pre-OE stories: inherited alternation `*felθu- ~ *feldu-` or regular PWGmc `*lþ > ld`.
- The project's current implementation does **not** need a separate Verner-style mechanism for this row, because the existing `PWGmcLThVoicing` treatment already maps the live input to the correct OE target.
- The checked FST output `*félduz -> feld` is therefore useful as a comparator, but it should remain a diagnostic early-stage form, not a proposed replacement for TSV `PROTOFORM`.

So there is no present mismatch between cognate-set proto, modelling input, and OE target: the row intentionally keeps `PROTO` and `PROTOFORM` identical and lets the note carry the historical ambiguity.

## Old English philology

- **Attested vs. reconstructed:** `feld` is an attested OE noun in repo-local lexicographic sources, not a reconstructed convenience form.
- **Citation form vs. inflected forms:** the row targets the citation form `feld`. Repo-local dictionary and grammar material also attest inflected forms such as dat.sg. `felda/felde`, dat.pl. `feldum`, and rare gen.pl. `felða`; these are philological background, not evidence that the row should target a different cell.
- **Morphological status:** `Campbell` treats `feld` among masculine nouns that retain traces of the old u-declension while also showing encroachment from a-declension endings. That mixed inflectional history is real, but it does not alter the lemma-level target.
- **Historical spelling evidence:** `Campbell` notes early OE place-name spellings in `-felth`, which are useful historical support for the older `þ` stage behind later standard `feld`.
- **Dictionary/headword issue:** `Clark Hall` and `Bosworth-Toller` both support `feld` directly as the OE headword. Nothing in the checked repo materials suggests that the row should switch to another lemma or to a reconstructed pre-standard form.
- **Dialect/manuscript caution:** the safe claim is only that early `-felth` spellings exist and that later lexical sources attest `feld`; the memo should not overstate a narrower dialect or manuscript conclusion beyond that.

## Project problem and solution

The project problem here is explanatory, not corrective. The row already derives correctly; the only question is how to describe why OE has `-ld-`.

The current project solution is sound:

- keep `PROTO = *félθuz` as the cognate-set proto;
- keep `PROTOFORM = *félθuz` as the actual derivational input;
- keep `COUNTERPART = feld` as the attested OE target;
- keep the note as a concise reminder that the historical `-ld-` can be understood either through inherited alternation or through the regular PWGmc `*lþ > ld` development.

This row therefore belongs with the project's **regular but note-bearing** items, not with `known_unmodelled`, `late_analogy`, or `attested_variant` cases.

## Paradigm probe

**No paradigm probe is required.**

This is not a row where the project must choose among competing OE paradigm cells or where `PROTOFORM` diverges from the citation-form proto. The live row already models the citation form successfully, and the philological issue is the prehistoric source of `-ld-`, not a missing OE cell.

If a future appendix wanted an illustrative noun-paradigm check anyway, the most relevant cells would be nom./acc.sg. `feld`, dat.sg. `felda/felde`, gen.pl. `felða`, and dat.pl. `feldum`. But no such probe is needed for the memo stage or for the current row decision.

## Recommended final report

Recommend a short final report stating that `feld` is an attested OE lemma regularly derived by the current cascade from `*félθuz`, while the note should explain that the medial `-ld-` can be interpreted either as inherited `*þ ~ *d` alternation or as the ordinary PWGmc `*lþ > ld` development cited by `Ringe & Taylor` and reflected in the project's existing rule treatment.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended. `regular` is appropriate.
- **TSV `NOTE`:** no change recommended. The current note already captures the real historical ambiguity without forcing a premature choice.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** no change recommended. The checked `DEV_NOTES` discussion remains current for this row, and the packet-named analysis/dossier files are unrelated rather than in need of row-specific cleanup.
