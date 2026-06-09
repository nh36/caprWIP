# Reader-facing PDF QC 02 report

## Scope

No new reader-facing sound-change chapters were added in this pass.

The current ten-chapter local section remains:

1. `049-050-b-allophony-and-sievers-law-syncope.md`
2. `051-sk-palatalization.md`
3. `052-velar-palatalization.md`
4. `053-054-pre-umlaut-bridge-and-w-loss.md`
5. `055-056-i-umlaut-core.md`
6. `057-j-cluster-coalescence.md`
7. `058-nasal-dissimilation.md`
8. `059-oe-back-mutation.md`
9. `060-ws-palatal-umlaut-note.md`
10. `061-weak-tail-nasal-loss-note.md`

## FOMA overflow problem

Two reader-facing `foma` blocks still contained lines long enough to risk
running past the right margin under the old PDF rendering:

- `SC056. West Saxon palatal diphthongization`
- `SC058. Nasal dissimilation in short-vowel environments`

The source lines themselves were not the problem. The problem was that the
build path rendered them without a dedicated width-safe code environment.

## Build-side solution implemented

The PDF build now uses a dedicated LaTeX rendering protocol for fenced `foma`
blocks:

1. `reader_facing_foma.lua` converts fenced `foma` blocks to a dedicated
   LaTeX environment, `ReaderFacingFoma`.
2. `reader_facing_pdf_header.tex` defines `ReaderFacingFoma` with:
   - `fvextra`
   - `Verbatim`
   - `breaklines=true`
   - `breakanywhere=true`
   - `fontsize=\small`
   - a simple frame for visual separation
3. `build_reader_facing_local_section_02_docker.sh` now ensures `fvextra` is
   available inside the Docker XeLaTeX build with:
   - `kpsewhich fvextra.sty >/dev/null 2>&1 || tlmgr install fvextra >/dev/null`

The final build route therefore uses:

- `fvextra`
- `Verbatim`
- the custom `ReaderFacingFoma` environment
- a Pandoc Lua filter

No `adjustbox` or `minipage` layer was needed after `fvextra` wrapping proved
reliable in the Docker XeLaTeX environment.

## FOMA blocks checked

The width audit scanned all 17 `foma` blocks in the ten chapter files. The full
per-block register is written to:

- `reader_facing_foma_width_check_01.md`

The checked rule sections were:

- `SC049` `PGmcBAllophony`
- `SC050` `SieversLawSyncope`
- `SC051` `OESkPalatalization`
- `SC052` `OEVelarPalatalizationKFront`
- `SC052` `OEVelarPalatalization`
- `SC053` `OEPostVelarWLoss`
- `SC054` `OEWLossBeforeI`
- `SC055` `OEIUmlautFronting`
- `SC055` `OEIUmlautRaising`
- `SC055` `OEIUmlautDiphthong`
- `SC055` `OEIUmlaut`
- `SC056` `OEWsPalatalDiphthongization`
- `SC057` `OEJClusterCoalescence`
- `SC058` `OENasalDissimilation`
- `SC059` `OEBackMutation`
- `SC060` `OEWsPalatalUmlaut`
- `SC061` `OEWeakTailNasalLoss`

The two blocks that exceeded the conservative pre-wrap threshold were:

- `055-056-i-umlaut-core.md` — `SC056. West Saxon palatal diphthongization`
- `058-nasal-dissimilation.md` — `SC058. Nasal dissimilation in short-vowel environments`

Under the hardened build protocol, these lines now wrap inside the PDF instead
of running off the right edge.

## Final FOMA-width result

Command run:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_foma_width.py
```

Result:

- 17 `foma` blocks checked
- 2 blocks flagged as over-threshold under the old unwrapped rendering
- the new `ReaderFacingFoma` protocol is active in the build

The rebuilt PDF was spot-checked on the pages containing the formerly longest
blocks. The code now wraps visibly inside the text area; no remaining
right-margin spill was observed in those checked blocks.

## Citation page-number rule

Reader-facing citations now follow a hard rule:

- every chapter citation must include page number(s);
- section numbers may be kept, but they do not replace pages;
- page-less citations are allowed only if they are explicitly whitelisted as
  whole-work/general.

The whitelist file is:

- `reader_facing_citation_whitelist.tsv`

At the end of this pass the whitelist remains empty.

## Citations corrected

This pass corrected page-less or under-specified citations in:

- `049-050-b-allophony-and-sievers-law-syncope.md`
  - `Adamczyk2001` -> `pp. 61--72`
  - `Fulk2018` for `§6.15` -> `p. 127`
- `051-sk-palatalization.md`
  - `RingeTaylor2014 §§6.4.1, 6.5.1` -> `pp. 213--216`
  - `Luick1914 §168` -> `p. 157`
  - removed the page-less `SieversBrunner1965 §91.a` support line from the
    affected sentence rather than guessing a page
- `053-054-pre-umlaut-bridge-and-w-loss.md`
  - `RingeTaylor2014 §6.4.2` -> `p. 214`
  - `Campbell1959 §406` -> `p. 167`
  - `RingeTaylor2014 §6.7.1` -> `p. 257`
  - `Luick1914 §187` -> `p. 173`
- `057-j-cluster-coalescence.md`
  - `Campbell1959 §§170, 248--251` -> `pp. 89, 107--108`
  - `RingeTaylor2014 §§6.4.1, 6.5.1, 6.6.1--6.6.4` -> `pp. 213--251`
  - `Fulk2018 §§4.7, 4.13` -> `pp. 65, 75`
- `059-oe-back-mutation.md`
  - `Campbell1959 §207` -> `p. 86`
  - `RingeTaylor2014 §6.9.4` -> `p. 319`
  - `Fulk2018 §4.8` -> `p. 69`
- `060-ws-palatal-umlaut-note.md`
  - `Campbell1959 §§248--251` -> `pp. 107--108`
  - `RingeTaylor2014 §§6.5.1, 6.6.1--6.6.4` -> `pp. 215--251`
  - `Fulk2018 §§4.7, 4.13` -> `pp. 65, 75`
- `061-weak-tail-nasal-loss-note.md`
  - `Campbell1959 §§345--349` -> `pp. 144--145`
  - `Fulk2018 §5.6` -> `p. 91`

## Page-less citations still allowed

None.

No page-less chapter citations remain, and the whitelist contains no active
whole-work/general exceptions.

## Checker commands run

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_citations.py
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_foma_width.py
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_section_order.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_02_docker.sh
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_chronology_evidence.py
```

## Final checker results

- style checker: passes with no warnings
- citation checker: passes with zero issues
- foma width audit: 17 blocks checked, 2 would have overflowed under the old
  rendering, both handled by the new wrapping protocol
- section-order check: passes and confirms SC049 through SC061 in cascade order
- chronology-evidence check: 17 sections checked, 0 warnings

## PDF build command run

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_02_docker.sh
```

## Final PDF build result

- `reader_facing_local_section_02.md` generated successfully
- `reader_facing_local_section_02.pdf` generated successfully
- `References` heading remains present
- SC numbers remain present in rule-level headings
- no accidental italics from bare starred forms returned

## Scope confirmation

- No new reader-facing chapters were added.
- No FST rules were changed.
- No TSV files were changed.
- No chronology cards were changed.
- No standardized source reports were substantively changed.
- No source dossiers or book dossiers were substantively changed.
