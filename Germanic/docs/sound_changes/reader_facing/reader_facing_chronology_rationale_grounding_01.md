# Reader-facing chronology rationale grounding 01

## Latest commit inspected

1. `d6bdd644 docs: add source-based chronology rationales`

## Reader-facing files edited

1. `Germanic/docs/sound_changes/reader_facing/012-lth-voicing.md`
2. `Germanic/docs/sound_changes/reader_facing/013-dental-hardening.md`
3. `Germanic/docs/sound_changes/reader_facing/014-015-opening-vowel-prelude.md`
4. `Germanic/docs/sound_changes/reader_facing/018-stressed-monosyllable-o-raising.md`
5. `Germanic/docs/sound_changes/reader_facing/022-mn-dissimilation.md`
6. `Germanic/docs/sound_changes/reader_facing/025-long-e-nasal-rounding.md`
7. `Germanic/docs/sound_changes/reader_facing/028-preconsonantal-x-loss.md`
8. `Germanic/docs/sound_changes/reader_facing/053-054-pre-umlaut-bridge-and-w-loss.md`
9. `Germanic/docs/sound_changes/reader_facing/058-nasal-dissimilation.md`
10. `Germanic/docs/sound_changes/reader_facing/064-065-post-apocope-tail.md`
11. `Germanic/docs/sound_changes/reader_facing/066-068-syncope-and-degemination-corridor.md`
12. `Germanic/docs/sound_changes/reader_facing/076-prefix-i-reduction.md`

## Ancillary files edited

1. `Germanic/docs/sound_changes/reader_facing/reader_facing_chronology_rationale_grounding_01.md`
2. `Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py`
3. `Germanic/docs/sound_changes/reader_facing/check_reader_facing_citations.py`
4. `Germanic/docs/sound_changes/reader_facing/check_reader_facing_foma_width.py`
5. `Germanic/docs/sound_changes/reader_facing/check_reader_facing_chronology_evidence.py`

## Terminology replaced

1. Replaced test-runner phrasing about undetected breaks, search limits, and negative results with plain statements about whether moving a rule earlier or later affected the checked forms.
2. Replaced local-boundary wording with direct statements about whether the order test does or does not by itself determine a closer relative position.
3. Kept the distinction between strongly constrained and weakly constrained rules, but recast it in historical prose rather than runner prose.

## Full-directory grep note

1. A full grep for the banned jargon still finds older occurrences in out-of-scope chapters and generated local-section snapshots.
2. This pass intentionally left those older files untouched, because the task was limited to the files changed in `d6bdd644`.
3. The edited weak-rule file set itself no longer contains the banned terminology.

## Source-based claims checked

1. `SC012` and `SC013` were checked against the cited handbook statements already present in the chapters; the prose now separates strong source support for the changes themselves from weak local order evidence.
2. `SC014`, `SC018`, `SC022`, and `SC025` were checked against `018-025-early-nwgmc-unstressed-and-boundary-limited-zone.review-dossier.md` and against the nearby chapter citations.
3. `SC028` was checked against `028-030-glide-and-fronting-entry.dossier.md` and `028-030-glide-and-fronting-entry.book-dossier.md`.
4. `SC053` was checked against `053-054-pre-umlaut-bridge-and-w-loss.dossier.md` and `053-054-pre-umlaut-bridge-and-w-loss.book-dossier.md`.
5. `SC058` was checked against `058-oe-nasal-dissimilation-residual.dossier.md`.
6. `SC065` was checked against `064-065-post-apocope-tail.dossier.md` and `064-065-post-apocope-tail.book-dossier.md`.
7. `SC067` was checked against `066-068-syncope-and-degemination-corridor.dossier.md` and `066-068-syncope-and-degemination-corridor.book-dossier.md`.
8. `SC076` was checked against `069-078-late-unstressed-tail-cluster.dossier.md` and `069-078-late-unstressed-tail-cluster.book-dossier.md`.

## Claims strengthened

1. `SC012` now states more clearly that the historical reality of \emph{lþ}-voicing is well supported even though the tested forms do not fix a close local order.
2. `SC013` now makes the same distinction for dental hardening: the change itself is secure, while the exact local placement remains open.
3. `SC014` now says plainly that it opens the unstressed-vowel prelude because the comparative sources place it in that broad early development, not because the tested forms force a neighboring seam.

## Claims weakened

1. `SC025` no longer says that the literature defines a special nasal-vowel region; it now says only that the handbooks document the month-type and moon-type material without fixing a close local chronology.
2. `SC028` no longer attributes the local placement directly to a literature-backed handoff into glide and fronting; it now says that CAPR keeps the rule there as a short prefatory note before the better-constrained rules to the right.
3. `SC053` no longer implies that the sources themselves define a strong bridge position; it now says that CAPR keeps the narrow \emph{*singwan > singan} rule in that stretch on modest comparative grounds.
4. `SC058` no longer suggests that the handbooks define a sharply bounded middle zone for the rule; it now says only that the relevant lexical outcomes occur among surrounding weak-vowel and suffixal developments.

## Claims left unchanged, with reason

1. `SC018` keeps its broad long-vowel placement because the review dossier and nearby citations support that level of claim, but not anything narrower.
2. `SC022` still presents \emph{mn}-dissimilation as a real but limited tendency because that is exactly what the review dossier and Campbell citation support.
3. `SC065`, `SC067`, and `SC076` still place the rules in broader late weak-tail settings because the dossiers support that wider chronology even while leaving the local order approximate.

## Rules where the literature gives a real chronology

1. `SC014` — the sources place it in the earliest Northwest Germanic unstressed-vowel simplification.
2. `SC018` — the sources place it in the early long-vowel history of stressed monosyllabic \emph{*ō}.
3. `SC065` — the sources place late medial syncope in the post-apocope weak-tail sequence.
4. `SC067` — the sources support syncope followed by later cluster simplification, even though not as a sharply separated law.
5. `SC076` — the sources place prefix-vowel weakening in the late weak-tail history.

## Rules where the literature documents the change but does not fix chronology

1. `SC012`
2. `SC013`
3. `SC022`
4. `SC025`
5. `SC028`
6. `SC053`
7. `SC058`

## Rules where CAPR placement remains approximate

1. `SC012`
2. `SC013`
3. `SC014`
4. `SC018`
5. `SC022`
6. `SC025`
7. `SC028`
8. `SC053`
9. `SC058`
10. `SC065`
11. `SC067`
12. `SC076`

## Checks run and results

1. `bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_19_docker.sh`
   - passed
   - regenerated `reader_facing_local_section_19.md`
   - regenerated `reader_facing_local_section_19.pdf`
   - regenerated `reader_facing_manifest_coverage_07.md`
2. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py`
   - no warnings
3. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_citations.py`
   - files checked: `54`
   - citation issues: `0`
4. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_section_order.py --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_19_docker.sh`
   - passed
5. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_crossrefs.py --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_19_docker.sh`
   - files checked: `54`
   - links checked: `485`
   - issues: `0`
6. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_chronology_evidence.py`
   - sections checked: `85`
   - warnings: `0`
7. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_generated_prose.py --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_19_docker.sh`
   - paragraphs checked: `5`
   - issues: `0`
8. `git diff --check`
   - passed

## Scope confirmations

1. No new sound-change chapters were added.
2. No local section 20 was created.
3. No manifest files were changed.
4. No FST rules were changed.
5. No lexical TSV data were changed.

## Handoff for the next task

1. Within the edited weak-rule set, reader-facing chronology prose no longer uses internal test-runner jargon.
2. Each edited weakly constrained rule now either has a properly cited source-based placement rationale or an explicit statement that CAPR's placement is approximate and model-driven.
3. Outside this edited weak-rule set, older reader-facing chapters still contain some of the earlier chronology wording and would need a separate scope-limited pass.
4. The next pass should review whether any remaining one-sided chronology cases need similar treatment, starting only with rules whose current prose still overstates how tightly the chronology is known.
