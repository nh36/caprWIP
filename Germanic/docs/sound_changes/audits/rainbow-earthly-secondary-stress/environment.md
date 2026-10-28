# Isolation and the shared environment

The research branch was created at local `update` commit
`3cb109c981c8868bf383172e2be06cdc88c00fb0`, not at a subsequently
advanced remote tip. A separate worktree was necessary because the original
worktree contained unrelated, active SC087/Barrack work. None of that
work was stashed, reset, cleaned, staged, or overwritten by this research.

The requested essay filename ending in `(2).docx` was unavailable.
The user approved using the supplied
`Secondary_Stress_in_Old_English_revised_comments.docx` instead;
`source-holdings.json` records that actual file's hash.

The first development compilation had a syntax error in the diagnostic
overbroad rule. It produced no accepted research result. A corrected
matrix completed its model evaluations but failed the final preservation
guard: the shared canonical bins and `oe_build_manifest.json` had been
rebuilt during the assay. That run was invalidated, not accepted as a
production-unchanged receipt.

Another development assay exposed a separate implementation error:
using `0 -> marker` permitted optional/repeated syllable markers and
therefore multiple forward stress outputs. That is not linguistic
optionality and cannot be an admissible historical model. Minimal
isolated Foma tests identified the error. Compulsory insertion first
corrected the finite controls, but whole-relation checks required further
investigation. The final implementation marks each vowel's existing
star delimiter with a single-codepoint syllable marker using a compulsory
non-epsilon replacement, then moves that marker over literal onsets.
The metrical projection recognizes the pretonic syllable itself rather
than treating `FootCtx` as a stress oracle.
The discarded development receipt is not the committed scientific
receipt. The harness now rejects any tested stage or component producing
multiple distinct downward outputs, and the portable receipt tests
independently enforce determinism. Reverse lookup need not be one-to-one.

The final formal receipt preserves both `test functional` and
`ambiguous upper; test null` diagnostics. The main composed early,
metrical and late sound operations pass both. Internal `RSyll`,
`RSyllOne` and sensitivity `RFootOne` yield conflicting diagnostics:
the functionality test is false although the extracted ambiguous domain
is empty. That discrepancy remains visible rather than being renamed
“all functional.” The check is over the declared segment/context-marker
domain, not merely the finite control list.

Both canonical and private-extended parsers have a distinct, genuine
segmentation defect: `biu` yields `*b*i*u` and `*b*iu`.
It is independently reproduced and recorded as a pre-existing follow-up,
not corrected in production, not treated as historical optionality, and
not encountered among the selected/protected populations or tested
candidate cells.

Investigation found that the original worktree's HEAD had independently
advanced to `e18ea205ddf426acdc1874d6e5af781dabbeba59`, including
the SC087 adjudication and Barrack agenda commits. Its previously
uncommitted file contents still matched the captured initial dirty-file
hashes; they had been committed elsewhere without this research changing
them. The canonical manifest reported an external rebuild at
2026-10-27 22:29:06 UTC. No matching refresh/rebuild process remained
running at the subsequent check.

The experimental source was compiled in private backend temporary
directories. In particular its relative `save stack` commands could
not write into `/usr/app`; `compile_isolated` also rejects absolute
destinations and source includes. This research did not invoke
`adjudicate --evidence`, `--refresh`, a canonical rebuild, or any
publication command. The unrelated commits and rebuild were not undone.

`results.json.gz` is the separately repeated, accepted assay, not that
invalidated development run. It records exact canonical before/after
hash dictionaries, checks the live manifest, requires scientific source
equality with the clean base snapshot, and cross-checks every identity
stage against the corresponding canonical snapshot bin. Each run also
requires the frozen scientific summary to match live output.

The guarantee is deliberately precise: the accepted interval is
byte-stable; all tracked production sources in the research worktree
remain identical to the recorded base; the experiment installed nothing.
It is not a false assertion that another session never advanced the
shared original `update` branch or rebuilt its bins during the entire
research period.

## Final archival run

A successful shared-container run first confirmed the final scientific
definitions and all 19 models. A subsequent run to retain the complete
immutable380 stage arrays was rejected because another shared rebuild
changed the canonical bins/manifest (manifest timestamp
2026-10-27 23:26:46 UTC). The failure did not overwrite the accepted
receipts. The unrelated SC087 experimental file was also externally
modified; it was not reverted or included in this branch.

The final archival assay therefore used an unmounted temporary backend
container, `capr-secondary-stress-e8b280d3`, from the identical
`capr-backend` image. The normal backend's `/usr/app` tree was streamed
read-only into that container as its reference, then the existing
`reproduce.py --container` entry point staged the exact base and research
separately. Identity and manifest validation still applied. The final
receipt's canonical hash maps refer to that private reference tree,
not a claim that the original shared runtime remained untouched by other
sessions. No bind mounts allowed the final assay to write to production.

The container's start, staging, assay and targeted removal were managed
inside one bounded shell command. A prior idle-container attempt expired
before staging and produced no result. All owned temporary containers
and the earlier private development directory were removed. Runtime:
Foma 0.10.0alpha; Flookup 1.03 using the same Foma library.

The final reference contains 3,330 protected files, versus 3,302 in the
earlier shared assay, reflecting external additions before the clone.
All 3,448 initially tracked files in the research worktree still match
their captured base hashes. The original worktree remains independent:
16 of its 20 initially dirty files still match their initial hashes, while
these four were subsequently changed outside this research:

- `Germanic/docs/sound_changes/audits/sc087-adjudication.md`
- `Germanic/docs/sound_changes/literature_dossiers/barrack_1975/research_agenda.md`
- `Germanic/docs/sound_changes/reader_facing/087-r-metathesis.md`
- `Germanic/tests/test_sc087_adjudication.py`

They were not readjusted to the old snapshot, staged, or included in the
research commit. The earlier preservation observation remains true for
its recorded checkpoint, not a claim that unrelated work later stopped.
