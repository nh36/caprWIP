# Research memo — 2068 heaven / heofon

## Starting point

- **ID:** 2068
- **CONCEPT:** heaven
- **COUNTERPART:** heofon
- **PROTO:** *xémenaz
- **PROTOFORM:** *xémonų
- **DERIVATION_CLASS:** late_analogy
- **NOTE:** PGmc mn-stem acc.sg. *xemonų (Kroonen p.220, Fulk §6.14). Derives via: o-raising (*o→*u before *ų), mn-dissimilation (*m→*β), back umlaut (*e→*eo), trisyllabic apocope (*ų→Ø).

The live row already treats this as a paradigm-cell case, not as a straight citation-form derivation. No pilot lexeme report for this lexeme was found in `Germanic/docs/lexeme_reports/pilot/`.

## Packet evidence assessment

**Authoritative/current:** the live TSV row with `PROTOFORM = *xémonų`; the packet's compact derivation trace showing `*xémonų -> heofon`; the absence of an `oe_known_problems.tsv` entry; and the live FST comments in `Germanic/fsts/germanic.txt` that now explicitly document `*hemonų/*xémonų` as the relevant acc.sg./oblique input for `heofon`.

**Useful background:** the packet's `DEV_NOTES.md` excerpts on the earlier mismatch work; the analysis excerpts from `compound_archaism_inventory.md` and `ws_vs_anglian_dialect_differences.md`; and the dossier excerpts from `un-to-on-chronology.md` and `widuwe-u-preservation.md`, which are valuable for the chronology of unstressed `u > o` and for the WS-vs-Anglian contrast.

**Stale or superseded:** the packet's older March 2026 `DEV_NOTES.md` material built around now-abandoned inputs such as `*xemenăz`, `*xemunăz`, and bare `*xemon`. Those notes are still useful project history, but they are not the live row state now that the TSV has `*xémonų` and the FST has explicit `*-onų > *-unų` support.

**Irrelevant or misleading:** the packet sentence saying no built-in paradigm-probe specification exists is partly stale. The probe tool now exists, but this row still lacks a dedicated built-in probe spec. The supplementary lexical-table hits are useful only for lemma presence (`heofon`), not for deciding which pre-OE paradigm cell the project should feed into the cascade.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at 12822-13140, which preserves the full `*xemenăz -> *xemunăz -> *xemon -> *xémonų` project history.
- `Germanic/docs/analysis/compound_archaism_inventory.md` and `Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md`.
- `Germanic/docs/dossiers/un-to-on-chronology.md` and `Germanic/docs/dossiers/widuwe-u-preservation.md`.
- `Germanic/fsts/germanic.txt`, whose comments now explicitly cite `*hemonų` / `*xémonų` as the heaven example for NWGmc `*-onų > *-unų`, mn-dissimilation, and trisyllabic apocope.
- `Germanic/tools/oe_paradigm_probe.py`, confirming that the tool exists but has no built-in `heaven / heofon` spec.
- `Germanic/data/old_english_wiktionary.tsv` and `Germanic/data/old_english_swadesh.tsv`, which support lemma-level `heofon` but not the proto-cell choice.
- `docs/references/fulk_comparative_grammar_early_germanic.vision.txt`, which preserves the comparative discussion and the relevant metric/weight passage.

A manual probe was also run with the live FST: `*xémenaz -> hefen`, `*xémō -> heomu`, `*xémnaz -> hemn`, `*xémeni -> +?`, but `*xémonų -> heofon`.

## Reconstruction and early-stage forms

This row needs the same three-way distinction that several other late-analogy memos require:

1. **Cognate-set proto / etymological headword:** TSV `PROTO` `*xémenaz`. This is the project's lexeme-level PGmc label for the cognate set, not the exact row input that feeds the OE cascade.
2. **Project derivational input:** TSV `PROTOFORM` `*xémonų`, explicitly an **mn-stem accusative singular / generalized oblique** form. This is the form the current FST is designed to map to OE `heofon`.
3. **OE target:** `heofon`, a WS citation-form outcome that reflects earlier generalization of an oblique stem with back-vocalic suffixal material.

The repository history shows some instability in how this middle level was represented. Older notes tried `*xemenăz`, then `*xemunăz`, then bare `*xemon`; the live row and FST now converge on `*xémonų`, which best matches the explicit NWGmc `*-onų > *-unų` raising logic and the row note's appeal to an acc.sg. paradigm cell.

## Old English philology

The OE target itself is not the problem: repo-local lexical materials support lemma-level `heofon`, and the analysis files consistently treat it as the standard WS form. The philological issue is what stands behind that lemma.

The checked materials support the following cautious description:

- **attested/citation side:** `heofon` is the ordinary OE lemma targeted here; `hefen` is an attested Anglian comparator in repo analysis, not the target of this row.
- **earlier/reconstructed stage:** Campbell's quoted `hefzen` belongs to earlier OE history and helps explain the dissimilation and later umlaut outcome, but it is not the row target.
- **paradigmatic status:** the row is modeling a WS nominative/citation form that has been leveled from an oblique stem with back-vocalic suffixal material.

So the final report should not talk as if `*xémonų` were the lexeme headword, and it should not flatten `heofon`, `hefen`, and earlier `hefzen` into one undifferentiated “OE form.”

## Project problem and solution

The project problem was that lexeme-level `*xémenaz` does not directly yield the target: the live FST probe still gives `hefen`, i.e. the front-vocalic non-target. The current solution is to keep that headword-level proto in `PROTO`, but to use `PROTOFORM = *xémonų` as the derivational input, because the row is meant to represent the WS form that reflects oblique-stem generalization, NWGmc `o`-raising before `*ų`, mn-dissimilation, back umlaut, and later apocope.

In other words, this `late_analogy` row is best read as: “heaven, represented in CAPR by the oblique/acc.sg. source form that actually feeds the attested WS citation form `heofon`.” That is narrower and more defensible than the older project stages that tried to force the lexeme headword itself through the cascade.

## Paradigm probe

A paradigm probe **is required** for this row because it is a `late_analogy` paradigm-cell case. There is still **no built-in row-specific probe spec** in `oe_paradigm_probe.py`, so the reusable probe is missing even though the tool itself exists.

The manual probe already confirms the core contrast:

- **lexeme-level proto / citation-style competitor:** `*xémenaz -> hefen` (non-match)
- **tested archaic nom.sg.:** `*xémō -> heomu` (non-match)
- **tested gen.sg.:** `*xémnaz -> hemn` (non-match)
- **tested dat.sg.:** `*xémeni -> +?` (non-match)
- **acc.sg. / selected oblique cell:** `*xémonų -> heofon` (match)

Before final-report automation, the missing built-in probe for this row should therefore cover at least **archaic nom.sg., gen.sg., dat.sg., and acc.sg.** If the team wants one extra diagnostic cell, add a **generalized NWGmc nominative-style oblique form** as a background comparator, but the indispensable cell is the acc.sg. `*xémonų`.

## Recommended final report

Recommend a concise final report that says `PROTO = *xémenaz` is only the cognate-set headword, `PROTOFORM = *xémonų` is the selected acc.sg./oblique input, and OE `heofon` is the WS citation form produced after oblique-stem generalization. It should explicitly separate live evidence from the older `*xemenăz` / `*xemunăz` project history and mention `hefen` only as a dialectal comparator.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended; `*xémonų` is the best current project input.
- **TSV `COUNTERPART`:** no change recommended; `heofon` is the intended OE target.
- **TSV `DERIVATION_CLASS`:** no change recommended; `late_analogy` is appropriate.
- **TSV `NOTE`:** **change recommended** — keep the current acc.sg. analysis, but tighten the note so it explicitly says `heofon` is a WS citation-form outcome built from generalized oblique material, with `hefen` as the front-vocalic comparator.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** **change recommended** in `DEV_NOTES.md` only. The older `*xemenăz`, `*xemunăz`, and bare `*xemon` stages should be marked more clearly as superseded project history so future packets do not over-weight them. No dossier cleanup is required from the materials checked.
