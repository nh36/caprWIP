# CAPR's two SC047 research models

See the [production integration record](integration-record.md) for the
disposition of the [adoption candidate](adoption.md). The current
[A](A-volume.pdf) and [B2](B2-volume.pdf) companions project the
[current capture](captures/sc047-current.json.gz), with the complete
orders and changed-stage traces for the same selected catalogue.
`adjudicate.py --refresh` owns the current capture and companion PDFs.
The capture and installed binaries are refreshed together only when
stale; rendering a stale companion requires Pandoc, XeLaTeX and the
book fonts. The publisher checks the same source digests as the main
book. Historical captures, including the first production capture,
remain separate immutable records.

**A (Ringe–Taylor)** loses short oral and nasal low vowels before West
Germanic j-gemination. **B2 (Dahl–Hogg–Fulk)** loses oral *a* before
gemination but nasal *ą* afterwards. The labels specify their apocope
chronologies, not adoption of every reconstruction in those authors.
The original B is archived, not selectable. Neither model changes
the historical compatibility order or rewrites the original 394-input
experiment.

## Source and build

`sc047_models.py` compiles the shared production definitions and executes
two explicitly ordered cascades. It first reproduces the canonical
394-row endpoints by sequential stage lookup on the original FST.
`--active` also evaluates the shared live corpus in compatibility, A
and B2, and compares each complete composition with its stage lookups.
Each selectable arm runs
the identical frozen inputs, the model-specific selections, and the
paradigm controls. Every changed stage is recorded: a missing stage in a
trace means identity at that stage. The shared compilation and all
lookups are isolated, disposable and opt-in; ordinary CI does not gain
any Foma runs. The historical files and their hashes are inputs, not
outputs. An individual arm can run with `--model A` or `--model B2`.

To run an independent replay against the original FST from the warmed
historical checkout:

```sh
mkdir -p .capr-work/sc047-models
docker compose exec -T backend sh -lc \
  'cd /usr/app && python3 tools/sc047_models.py --form sáiwalōi --form sáiwalôi' \
  > .capr-work/sc047-models/results.json
python3 Germanic/docs/models/sc047/publish.py .capr-work/sc047-models/results.json \
  .capr-work/sc047-models
```

Add `--pdf` to the publication command to render the independent volumes
with Pandoc, XeLaTeX and the existing book fonts. The publisher also accepts
a compressed result (`.json.gz`); the archive can be rendered without
repeating Foma. The model chapter and bibliography are shared. Each
catalogue is accompanied by complete changed-stage derivations and a
394-row inventory; the cross-model comparison is restricted to frozen
inputs.

The [corpus audit](results.md) links the current and previous captures,
documents remaining unmatched forms, and distinguishes the results of
the two comparisons.

`cells.tsv` is a small overlay on stable row IDs. The two common
corrections come from the unmerged proposal `399c50ad1dd339df4d235dda53334b39fb5fec14`;
they are not claims about `update`. The baseline target identifies the
frozen diagnostic, not necessarily the citation headword or the selected
cell in a given model. The existing shared lexeme dossiers own the
headwords, bibliography, and mature philological prose. The overlay
records which form each model actually evaluates; a normalized *hīewes*
target is not a derivation of the headword *hīew*. The same normalized
spelling in two grammatical cells does not merge their identities.

Bed, pledge, and kin have no row in this frozen 394-word selection.
Their direct and protected forms are computed in both models, but not
added to either denominator. `expansions.tsv` selects the proposed
bed and kin cells under stable research identities and places them
in separate per-model tables and `*-expansions.tsv` files. Pledge
remains an unscored control. The [lexical follow-up](lexical-followup.md)
describes the unscored fen and wicg probes and their source limits.
In A, *nette* and Cotton *hiewes* provide
independent protected selections. *Hay* has no verified target for a
protected reconstructed cell; its frozen direct comparison remains a
visible unresolved mismatch rather than a falsely certified selection.
The proposed extension of oblique stems into direct cells is a
philological explanation, not a rule in either cascade.

## Scientific scope

Ringe–Taylor pp. 44–47 and Hogg–Fulk §2.23 give contrary predictions for
light neuter direct singulars. Both permit a geminate in protected
cells, so those cells test the derivations but cannot decide the order.
The shared sequence restores final oral long-*ō* raising before final
*z*-loss. The dative change instead implements final *ōi* > *ē*
(Ringe–Taylor p. 61; Ringe 2017 p. 225), with a productive, unambiguous
input extension that does not override any existing admitted parse.
Trimoric *ôz* is a separate test; neither its phonology nor the source's
genitive cell assignment is assumed to be the bimoric account.

Both models use the same post-nasal-loss labial carrier. It preserves only
stranded geminated *wwj*, so it cannot recreate the geminate that A
never made in the inherited direct singular. Campbell §120.2, Hogg
§3.18 and Ringe–Taylor pp. 246–250 motivate later palatal conditioning,
not the survival of a separately contrastive *j*. Fulk's alternative
inherited *auj* input is a probe, not a third model. The front-vowel
restriction of the singleton-*aw* proxy and word-final short *i.i*
resolution are bounded implementations: the former does not establish
a late English singleton *hay* reflex, and the latter does not establish
general medial hiatus contraction.

The [source audit](../../sound_changes/literature_dossiers/sc047_paired_chronologies/comparative_followup/cell-sources.md)
and [discrepancy classification](../../sound_changes/literature_dossiers/sc047_paired_chronologies/comparative_followup/discrepancy-classification.md)
give edition, manuscript, and source qualifications. Publication files
retain those distinctions and identify unmatched rows; scores on differing
selected cells are not relative evidence for the chronologies.

## Validation cost

The tests in `test_sc047_models.py` read the existing frozen inputs
and plan without compiling: the first rejects unintended order or rule
inventory differences, and the second rejects unrecognized or multiply
selected corpus cells. The recorded-run check verifies the exact corpus
deltas, the 40 lowering identities, the lengthening controls, and the
quantity and dative probes. The archived replay checks still test historical
artifacts; they cannot validate the new selections. Ordinary test runs add no Foma process, rebuilt fixture, corpus runtime sweep
or concurrency. The SC083 controls reuse the current capture; the refresh
now owns the previously manual selectable-app build, and the same component
image serves the extra compatibility paths and two prefixed ‘call’ forms.
The explicit research build uses one disposable common image and one
component compile for both variants, then performs batched lookups.
Neither it nor the PDF render writes production bins or generated
production publication sources.

Revision 2 measured 5m41s end to end for the opt-in two-model command
(two compiler calls, 120 component networks, no fixture setup). The
peak observed resident high-water mark for Foma was 2,243,756 KiB,
sampled from `/proc/<pid>/status` inside the backend. Normal tests
have zero Foma calls before or after this change.

The lexical expansion checks reuse the existing trace archives.
`test_light_neuter_paradigms_distinguish_loss_gemination_and_simplification`
checks first divergent stages, protected doubling, oral negatives,
final nasal simplification and the stranded-*w* controls.
`test_supplemental_capture_preserves_the_benchmark_and_records_new_probes`
guards the old corpus and trace inventory while checking the new
palatalization and *r* controls. The publisher test checks separation
of proposals from the scored inventories. No fixture setup, compiler
call, additional emitted network, live corpus sweep or concurrency
was added to the test lane. The opt-in research run reused the full
two-model build once and added 11 batched query inputs; see
[results and provenance](results.md#lexical-expansion-capture).
