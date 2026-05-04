# Research memo — 1973 buck / bucc

## Starting point

- **ID:** 1973
- **CONCEPT:** buck
- **COUNTERPART:** bucc
- **PROTO:** *búkkaz
- **PROTOFORM:** *búkkaz
- **DERIVATION_CLASS:** unexplained_unmodelled
- **NOTE:** Campbell §115 names `bucca` as an exception to regular u-lowering/a-umlaut; regular sound change would give **`bocc`**, while high-vowel cells would create an i-umlauted **`byċċ`**-type outcome rather than the target `bucc`.

## Packet evidence assessment

**Authoritative/current in the packet:**

- The live TSV row and the matching `oe_known_problems.tsv` entry both treat `*búkkaz → bucc` as a documented `u_lowering_near_labial` exception rather than as a fixable FST error.
- The packet excerpts from `DEV_NOTES.md` summarizing Campbell, Luick, R/T, and the later retraction of the cell-switch idea are current and usable.
- The `notable_findings.md` material on the exception cluster and on `bucca`/`bucc` stem-class history is current background evidence.

**Useful background but not final authority:**

- `pilot/buck.md` is a concise pilot summary, but it predates this memo stage and should not control the conclusion.
- Schuhmacher's suggestion that `bucc` may once have involved a u-stem is worth mentioning as a hypothesis, but the repo's own follow-up does not verify it.
- The packet's lexical-table hit `buc` from `old_english_wiktionary.tsv` is only supplementary normalization data.

**Stale or superseded material inside the packet:**

- The packet still surfaces `DEV_NOTES §17.10.34` material claiming `*búkkis → bucces` as a regular rescue. That proposal was explicitly withdrawn in `DEV_NOTES §17.10.34a`.
- The packet also inherits the same superseded precedent from `dossier-shoulder-lautgesetz-2026.md`, where `*búkkis → bucces` is still cited in preserved historical argumentation.
- The packet's line saying a paradigm probe is required belongs to that earlier exploratory phase and is no longer decisive.

**Irrelevant or misleading packet material:**

- Most analysis/dossier hits in the packet are keyword collisions on “a-umlaut” or “i-umlaut” and do not discuss row 1973 directly.
- `old_english_wiktionary.tsv`'s `buc` should not be allowed to outweigh Campbell's `bucca` and Kluge-Seebold's `bucca` / `bucc` evidence.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md`:
  - the main “NWGmc u-lowering exceptions near labials” discussion;
  - `§17.10.34`, the now-withdrawn cell-switch proposal;
  - `§17.10.34a`, the current retraction and conclusion.
- `Germanic/docs/analysis/notable_findings.md` §2 and its expert-consultation subsection.
- `Germanic/data/oe_known_problems.tsv`, which already records `*búkkaz` as `wontfix`.
- `Germanic/docs/lexeme_reports/pilot/buck.md`, treated as background only.
- `Germanic/docs/dossier-shoulder-lautgesetz-2026.md`, because the packet names it and it still repeats the withdrawn `*búkkis → bucces` precedent.
- `Germanic/data/old_english_wiktionary.tsv`, which gives the supplementary form `buc`.

Direct search across `analysis/` and `dossiers/` did not turn up a stronger row-specific dossier than `notable_findings.md`; most other packet hits are generic umlaut references rather than `bucc` research.

## Reconstruction and early-stage forms

The project's **cognate-set proto/headword** is still `*búkkaz` in the TSV. That is the current project anchor for this OE row.

The fuller comparative background is more complicated. `notable_findings.md`, following Kroonen, says the lexeme was probably **originally an n-stem**, reconstructable as `*bukka(n)-`, with nominative `*bukō` and genitive `*bukkaz`; that history explains the geminate by Kluge's Law. Kluge-Seebold then matters because it confirms that Old English had both **`bucca`** (n-stem) and **`bucc`** (a-stem).

So the distinctions should be kept sharp:

- **Cognate-set proto:** the TSV's project headword `*búkkaz`.
- **Project input form:** also `*búkkaz` at present, because the row is left as an unresolved/documented exception rather than being retargeted to some other paradigm cell.
- **OE target form:** `bucc`, i.e. the a-stem OE counterpart represented by this row, not the parallel n-stem `bucca`.

No regular early-stage alternative now licensed in the repo solves the row. Low-vowel cells lead to regular lowered `bocc`-type outcomes; high-front-trigger cells lead to `byċċ`-type i-umlaut outcomes; the u-stem idea remains unverified background speculation, not a usable project input.

## Old English philology

This is **not** a reconstructed-OE case. The project is treating `bucc` as a real OE form, but the philology is lexically mixed:

- Campbell's exception list cites **`bucca`**.
- Kluge-Seebold explicitly gives **`bucca` (n-stem) beside `bucc`**.
- The row's target is therefore best understood as the OE **a-stem citation form** within a lexeme that also had an n-stem partner/history.

That headword situation matters. A final report should not flatten `bucca`, `bucc`, and the lexical-table `buc` into one undifferentiated form. The handbook/dictionary evidence supports saying that OE had `bucca` and `bucc`; the lightweight lexical table is only supplementary and may reflect a simplified lemma convention.

I found no repo evidence justifying a dialect-specific claim for this row, and the memo should not invent one.

## Project problem and solution

The project problem is not lexeme identity; it is **derivability**. The FST gives the regular lowered outcome, while the attested OE row keeps `u`.

An earlier project phase tried to solve this by switching to an oblique paradigm cell (`*búkkis → bucces`). The current repo no longer accepts that move. `DEV_NOTES §17.10.34a` explicitly says the proposal failed because any cell with the needed high front trigger also introduces i-umlaut, so the attempted rescue does not actually yield `bucc`.

The current project solution is therefore:

- keep row 1973 as an **unexplained/documented exception**;
- do **not** retarget the row to `bucces` or another oblique cell;
- explain in the eventual report that OE `bucc` stands against the regular `bocc` outcome, with `bucca` as relevant philological background but not as the row target.

## Paradigm probe

A paradigm probe is **not strictly required** to settle this memo, because the decisive repo conclusion is already the `§17.10.34a` retraction: no cell-consistent regular input yields the OE target.

If a later final report still wants a small diagnostic table, it should probe only as **contrastive background**, not as a search for a new TSV fix. The cells worth contrasting would be:

- citation-form `*búkkaz` (to show regular `bocc`);
- the abandoned high-vowel trial `*búkkis` (to show why the old rescue failed);
- Kroonen-style original n-stem material (`*bukō` / `*bukka(n)-`) to separate the `bucca` history from the row's `bucc` target.

## Recommended final report

Recommend a concise final lexeme report that says `bucc` is a genuine documented exception to NWGmc/OE `*u`-lowering, cites Campbell's `bucca` and the OHG comparison, and briefly notes that OE also had parallel `bucca`, so the row's target `bucc` should be framed as the a-stem OE form within a lexically mixed history. The withdrawn `*búkkis → bucces` proposal should be mentioned only as superseded project history.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended now.
- **TSV `PROTOFORM`:** no change recommended now.
- **TSV `COUNTERPART`:** no change recommended now.
- **TSV `DERIVATION_CLASS`:** no change recommended now.
- **TSV `NOTE`:** no change required; the current note already captures the key project conclusion that no lautgesetzlich input is available.
- **`oe_known_problems.tsv`:** no change recommended; the current `wontfix / u_lowering_near_labial` entry matches the best current conclusion.
- **`DEV_NOTES` text:** no essential change recommended; the authoritative retraction is already present.
- **Dossier text:** cleanup **is** recommended. `Germanic/docs/dossier-shoulder-lautgesetz-2026.md` still cites `*búkkis → bucces` as if it were a live precedent inside preserved historical argumentation. That should be flagged more directly as withdrawn/superseded so future packets do not promote it as current evidence.
