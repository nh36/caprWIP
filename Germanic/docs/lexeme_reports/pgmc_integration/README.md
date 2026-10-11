# Proto-Germanic audit / lexical-volume integration

Status: provisional integration design, not scientific adoption or publication
promotion. Base: `27c552bf429ccbb563b365b8e72d5ee0bf5c905d`, branch `update`.
The completed 49-tranche alignment supplies evidence, not 393 settled histories.

## Artefacts and authority

- [Population crosswalk](population_crosswalk.tsv) and
  [summary](population_summary.md): GENERATED, one record per live stable ID.
- [Editorial inventory](editorial_inventory.tsv): GENERATED inspection routes
  for the complete audit population, separate from reviewed judgements.
- [Editorial cases](editorial_cases.tsv) and [source checks](source-checks.md):
  SOURCE, nine scoped judgements covering six examples and a control.
- [Schema proposal](schema-proposal.md): SOURCE proposal, not the live schema.
- [Resumption plan](resumption.md): SOURCE routing and research proposal,
  subordinate to the existing scientific registry and comparative synthesis.
- [Protocol record](../../sound_changes/audits/pgmc-lexical-integration-design.md):
  bounded investigation, explicitly no SC verdict.

The six [provisional examples](examples/) are outside production. They reuse
the existing model entries, source ledgers and pilots while incorporating the
completed survey. No existing production text or publication manifest is replaced.
The source checks retain evidence IDs and holding/page provenance outside the
reader-facing argument.

`Germanic/tools/pgmc_lexical_integration.py` reuses the audit validator,
legacy migration resolver and existing report-selection logic. It has no
generation/write switch: inspection is read-only, and `--check` checks freshness.
The sole writing route is `python3 Germanic/tools/adjudicate.py --refresh`,
through the new research projection in the existing artifact graph.
There is no second corpus, bibliography, sound-change registry or mutable database.
Current selected forms in the crosswalk are generated from live owners, not edited
in the editorial cases.

## What the populations mean

| Population | Meaning at this base |
| --- | --- |
| 380 | Original runnable identity set in the immutable legacy output snapshot, not every live audit row |
| 387 | Current runnable OE rows and selected sound-change baseline |
| 393 | All live OE data points admitted to the reconstruction survey, including six without runnable targets |
| 148 | Selective requirement at the historical production-backlog commit `16fe8ad3`, on its then-380 runnable rows |
| 150 | Those same original 380 identities under today's selective policy |
| 157 | Current selective requirement across the 387 runnable rows |
| 147 | Earlier model-entry assembly stage described in the assembly README, not current report-manifest coverage |
| 160 | Current class-assembly model entries actually consumed by the lexical-volume and combined-book builders |
| 11 + 1 | Eleven pilot production records and one adder format-test record in the separate report manifest |

The strict legacy resolver uses frozen selected-input/target/concept identities
and the exact approved migrations to recover stable IDs. It does not claim the
legacy table originally contained IDs, compare old inputs as live errors, or
join homonyms by gloss. Gift 2040 and knee 2085 are the two approved legacy
input transitions; their old bytes remain historical authority.

To reproduce current counts, run the read-only integration helper. To reproduce
the two historical counts independently without editing the worktree:

```bash
python3 - <<'PY'
import subprocess, sys, tempfile
from pathlib import Path
sys.path.insert(0, "Germanic/tools")
import oe_lexeme_report_coverage as coverage
old = subprocess.check_output([
    "git", "show", "16fe8ad3:Germanic/data/germanic-aligned-final.tsv"])
with tempfile.TemporaryDirectory() as directory:
    path = Path(directory) / "historical.tsv"
    path.write_bytes(old)
    rows = coverage.load_oe_rows(path)
    print(len(rows), sum(row.requires_report for row in rows))  # 380, 148
manifest = subprocess.check_output([
    "git", "show", "97face4b:Germanic/docs/assembly/manifest_all_by_class.tsv"])
print(len(manifest.splitlines()) - 1)  # 147
PY
```

The seven later runnable witnesses are who 2322, you 2326, wound 2327, sow 2328,
betray 2329, thought 2330 and hue 2332. All seven currently satisfy the NOTE
criterion. The remaining difference from 148 to 157 is two legacy entries:
gift gained its source-choice NOTE; knee gained its short-dative NOTE and
late-analogy/paradigm selection class. This was checked against the corpus at
`16fe8ad3`; it is not a guessed subtraction.

The six research-only rows are ball 1935, the two bid data points 1947/1948,
dove 1994, roe 2156 and stilt 2218. Their live target is `-`. Audit membership
does not make them runnable or silently authorize an attested publication target.
They remain visible in the crosswalk and editorial inventory, not missing from
the reconstruction research. Additional paradigm cells 2309–2318 were already
in the original 380: they are not ten new post-baseline witnesses.

The report manifest and class assembly are separate production contracts.
`oe_lexeme_report_coverage.py` validates the former and selects extended-report
obligations from NOTE, nonregular class or pilot/full status.
`build_class_manifests.py` assembles stable-ID `.model.md` entries;
`build_full_lexical_volume.py` consumes its class manifest and compact traces;
`build_capr_book_draft.py` consumes that lexical aggregate. The generated
manuscript confirms the live 82/4/36/28/3/2/5 class counts, totalling 160.
A model entry in the book is therefore real assembled prose even if the older
pilot/full manifest has not certified it as a production report.

## Actual coverage discrepancies

Of 157 required entries, 152 are in the 160-model assembly. Five are absent:
handle 2055, boundary noun march 2120, wound 2327, sow 2328 and betray 2329.
These are genuine policy-versus-assembly gaps, not absent audit research.
All are retained by stable ID in the crosswalk with their audit and
filename-owned materials. The seven new witnesses split into four assembled
(who, you, thought, hue) and those three unassembled witnesses.

Eight assembled entries do not meet the older selective trigger:
adder 1933, book 1955, dew 1989, flea 2018, four 2029, goose 2044,
hew 2074 and louse 2113. They are neither duplicates nor erroneous additions:
the assembly has a broader editorial history than that policy.
Adder's `format_test` alone does not activate the production requirement.
Its current ordinary-control pilot is an author-review candidate for
supersession, not silently corrected here.

The old handle "no source material" warning came from fuzzy discovery that
assigned handle-named files to hand 2054. Filename-prefix discovery now records
2055's own packets/memos without that misassignment. It certifies
stable-ID ownership of a file, not its philological correctness or readiness.
Shared batch summaries and unprefixed materials are deliberately not inferred
to belong to every word they mention. Existing audit evidence supplies explicit
shared links without duplicating author votes.

The stale 148/147 narratives should eventually be replaced by links to generated
counts. The historical assembly manifest at `97face4b` reproduces 147 entries.
Those narratives are left untouched in this design assignment to preserve the
requested production boundary. Likewise, do not promote all 160 models into
the pilot/full manifest by assumption: author approval should select the
production contract and validation status first.

## Editorial method and first-pass result

The classification unit is a named question about a formation, cell or feature,
not the entire etymological family. Establish identity, author commitment,
historical endpoint and comparison unit before deciding scholarly significance.
Then ask whether the difference changes the account of the selected formation:

1. Substantive disagreement: competing analyses of that relevant object with a
   consequential formation, vowel, consonant, quantity, accent, dating or
   etymological difference. The cause can remain unknown.
2. Qualified alternative: a potentially consequential alternative whose
   comparability, admission premise or explanation is still missing.
3. Non-substantive difference: established presentation, cell, endpoint or
   related-unit distinction rather than rival analyses of one object.
4. No special discussion: ordinary support for the selected object within an
   explicitly reviewed scope, without a consequential interpretative issue.

These judgements are independent of derivation class and match status.
Different-unit evidence may coexist with a genuine formation controversy;
one case does not inherit another case's resolved cause.
Transcription equivalence needs a source-backed convention, not a global
character substitution. Explicit quotation, endorsed theory, reported theory,
rejected hypothesis and CAPR component assembly must remain different.

The first-pass inventory is complete as an inventory, not as a new 393-row
editorial adjudication. Its reproducible routes are 91 focused-comparison
reviews, one other candidate-comparison review, eight unit-comparability
reviews and 293 ordinary-evidence reviews. Those are workloads, not counts of
controversies. They use existing scoped comparisons and comparability outcomes,
not `bounded_limit`, output success, source counts or `type_tags`.
All 393 bounded audit alignments remain unchanged. Seven rows now have
scoped manual assessments; the other 386 say `not_editorially_reviewed`.
Even an ordinary inspection route does not grant "no special discussion".

The calibration shows why classification must be scoped: adder is a qualified
feminine alternative; knee's cell contrast is non-substantive but its ending
premise is qualified; you and hue have consequential competing accounts;
thought has explicit inherited finite evidence but an unsettled formation;
fire combines substantive ancestry differences with an unverified exact
selected proxy. Barrow 1937 is the control: the overlapping m./n. presentations
are not a gender dispute, and the selected masculine hill/mound has ordinary
support. Its remote etymology and phonemic sign interpretation are not declared
settled by that scoped negative assessment.

## Author decisions and next bounded task

Approve or revise the density and scope of the six examples and the two-axis
policy before changing production. Decide which manifest certifies model-entry
production; avoid maintaining two independently editable completion statuses.
Next, perform a bounded editorial review of a small subset of the 91
focused-comparison routes, prioritizing comparisons relevant to selected inputs.
Record scoped judgements and missing premises using the same SOURCE relation.
Include ordinary and non-substantive controls; do not generate 393 long reports.

In parallel as a separate authorized scientific task, resume SC032's
component specification using the existing sources and queue, not another
thirteen-source comparative survey. After editorial approval, close the five
real assembly gaps before scaling optional regular-controversy entries.
Keep reporting repairs, input legitimacy, sound-law validity and final-output
correctness separately reviewable throughout.
