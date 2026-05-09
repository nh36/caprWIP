---
row_id: 1940
concept: beard
counterpart: beard
proto: *bárdaz
protoform: *bárdaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
  - Germanic/docs/analysis/mismatch_dossier_mizdo.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1940 beard / beard

## Current row state

- Live OE row `1940` currently reads `CONCEPT = beard`, `COUNTERPART = beard`, `PROTO = *bárdaz`, `PROTOFORM = *bárdaz`, `DERIVATION_CLASS = regular`; the source field is still just duplicated inherited-etymology placeholders, not a row-local explanatory note [Germanic/data/germanic-aligned-final.tsv:32-32].
- No matching packet or research memo file exists for row 1940 at present. `coverage_audit.md` still records the row as `regular | no | - | - | - | none`, so this slice is replacing an absence rather than extending an existing row report [Germanic/docs/lexeme_reports/coverage_audit.md:196-196].
- The published OE derivation trace currently succeeds without repair: `PGmc Final Z Deletion: *bárda`, then `PWGmc Final Bare A Loss: *bárd`, `Anglo Frisian Brightening: *bærd`, `OE Breaking: *beard`, with surface `Outcome: beard` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:106-125].
- Repo-side analysis files mention the row only as a regular comparator. `arestoration_r_l_research.md` lists row 1940 among the wider `*aCr-*` inventory with the comment `breaking before *rC*`, and `mismatch_dossier_mizdo.md` treats `*bárdaz` as an already-correct `-rd-` case (`FST: beard ✓`) rather than as an unresolved mismatch [Germanic/docs/analysis/arestoration_r_l_research.md:722-735; Germanic/docs/analysis/mismatch_dossier_mizdo.md:523-530].

## Development-note summary

Most of the usable DEV_NOTES support for row 1940 comes from a specific engineering regression, not from a long lexeme dossier. After the Phase 1d-β migration that changed Role-1 breve tails to plain `*a`, DEV_NOTES records that heavy a-stem nominatives such as `*bárdaz` started surfacing with a false final `e`: “forms such as `*bárdaz` now surface with a spurious final `e` (`bearde`, `bōsme`, `botme`, …) instead of the correct apocoped `beard`” [Germanic/docs/DEV_NOTES.md:22065-22085]. The note then traces the failure step by step: the final tail was being fronted by Anglo-Frisian Brightening to `*æ`, after which the apocope rule no longer deleted it [Germanic/docs/DEV_NOTES.md:22072-22085].

The same DEV_NOTES passage is important because it does not stop at “bearde is wrong”; it argues for a historical ordering. Two fixes were considered: delete final `*æ` in apocope, or stop AFB from applying word-finally. DEV_NOTES explicitly prefers the second path on chronological grounds, citing Ringe/Taylor's ordering in which loss of final `*-a` is pre-OE and earlier than OE fronting: “Both are pre-OE PWGmc changes... Hence at AFB time, no short word-final `*a` exists to front” [Germanic/docs/DEV_NOTES.md:22087-22137]. For row 1940, that is the main current project explanation of why the good path is `*bárda > *bárd > *bærd > *beard`, not `*bearde`.

A second DEV_NOTES cluster preserves an intermediate diagnostic stage that should be kept but not over-read. After the split-AFB fix, the file reports that some rows now lost fronting instead, including “`*bárdaz → bard`,” because `OEARestoration` was retracting `*æ` back to `*a` when the weak tail was plain `{*a}` or `{*a}{*z}` [Germanic/docs/DEV_NOTES.md:22241-22325]. That matters as project history: row 1940 was temporarily used as a blocker test case for the A-restoration rewrite. But a later inventory sharply narrows the scope and classifies row 1940 as “`*rd` cluster, breaking before `*r`+C, no A-restoration question” [Germanic/docs/DEV_NOTES.md:30599-30612]. The safest reading is therefore: beard was useful during regression diagnosis, but the settled project position is that its controlling phenomenon is breaking after regular fronting, not an ongoing A-restoration exception.

There is also a separate set of English-sandbox notes that mention `beard`, but those are about the later history of modern English outputs and should not be mistaken for OE row authority. In those passages `*bardăz/*bardaz` is grouped with `barrow/bier/birth` and later KIT or post-vocalic `/r/` problems [Germanic/docs/DEV_NOTES.md:1787-1801; Germanic/docs/DEV_NOTES.md:1808-1828; Germanic/docs/DEV_NOTES.md:2306-2324]. They are useful only as diagnostic background showing why the lexeme name kept reappearing elsewhere in the repo.

## Relevant DEV_NOTES fragments

### Fragment A — final-vowel regression on `*bárdaz`

This is the most important surviving row-local material. DEV_NOTES identifies the exact regression and names row 1940's expected output explicitly:

> “forms such as `*bárdaz` now surface with a spurious final `e`
> (`bearde`, `bōsme`, `botme`, …) instead of the correct apocoped
> `beard`.” [Germanic/docs/DEV_NOTES.md:22068-22070]

The diagnostic trace immediately below shows why:

> `*bárdaz at AFB         → *b*æ*r*d*æ     (root á→æ, tail a→æ)`
> `*bárdaz at A-rest.     → *b*ea*r*d*æ    (breaking intervenes)`
> `*bárdaz at apocope     → *b*ea*r*d*æ    (rule targets {*ă}/{*a} only)` [Germanic/docs/DEV_NOTES.md:22072-22085]

For later reporting, the substance to preserve is not just “bug fixed.” The note's point is that the regression exposed a real chronology assumption inside the OE cascade: the weak tail on heavy a-stem nominatives must disappear before Anglo-Frisian fronting can touch it. That is why row 1940 is a good witness for the interaction of final-vowel loss, AFB, and breaking [Germanic/docs/DEV_NOTES.md:22065-22085].

### Fragment B — chronology argument against `bearde`

DEV_NOTES then turns the regression into a chronological argument, using Ringe/Taylor as its explicit source claim. The key project statement is:

> “Both are pre-OE PWGmc changes. AFB ... is an OE/Ingvaeonic innovation
> that presupposes the PWGmc monosyllabic stem.... Hence at AFB time, no
> short word-final `*a` exists to front.” [Germanic/docs/DEV_NOTES.md:22114-22121]

That line matters more than the implementation detail. It means the preferred solution is not a late clean-up rule deleting fronted final `*æ`, but a rule domain in which word-final short `*a` is already gone before fronting. DEV_NOTES makes this operational consequence explicit: “We can still respect R/T's chronology phonologically by conditioning AFB not to fire word-finally” [Germanic/docs/DEV_NOTES.md:22123-22137]. Row 1940 therefore carries a specific chronological lesson: the good `beard` output depends on preserving early apocope and letting breaking apply only after the stem is already monosyllabic [Germanic/docs/DEV_NOTES.md:22095-22137].

### Fragment C — temporary A-restoration regression, later narrowed

The next relevant passage is diagnostically important but not fully current as row policy. After the split-AFB fix, DEV_NOTES says:

> “Remaining regressions are `fronting_missing__afb` cases such as
> `*dágaz → dag (expected dæġ)`, `*kráftaz → craft`, `*stábaz → staf`,
> `*bárdaz → bard`. The root `*á` is being retracted back to `*a`.”
> [Germanic/docs/DEV_NOTES.md:22241-22245]

The note goes on to show that `OEARestoration` was firing when the tail was bare `{*a}` or `{*a}{*z}`, and it explicitly includes `*bardaz` among forms a future rewrite must block on [Germanic/docs/DEV_NOTES.md:22247-22325]. That history should be kept because it explains why beard appears inside the A-restoration research trail at all.

But the later cluster inventory is the controlling follow-up. There row 1940 is reclassified as:

> “| 1940 | *bárdaz | beard | *rd* cluster, breaking before *r*+C, no A-restoration question |” [Germanic/docs/DEV_NOTES.md:30609-30612]

So the slice should preserve both layers: yes, `*bárdaz` was temporarily swept into the regression bucket; no, the settled note does not treat row 1940 as an active A-restoration problem [Germanic/docs/DEV_NOTES.md:22241-22325; Germanic/docs/DEV_NOTES.md:30599-30612].

## Superseded or diagnostic material

The English-sandbox passages mentioning `beard` are real, but they belong to a different problem space. DEV_NOTES repeatedly uses `*bardăz`/`*bardaz` as a probe for later English rhotic handling: “Expand `EnglishSandboxProtoRhoticFronting` ... so `*bergą/*bardăz/*barwōn/*burdiz` feed the ME vowel system with the right backness, unlocking `barrow/beard/bier/birth` reflexes” [Germanic/docs/DEV_NOTES.md:1791-1794]. A nearby scaffold note likewise says the new stage still leaves `*bergą/*bardaz/*barwōn/*erθo` with bad modern-style outputs and needs `{*rdă → {*ər}}` tuning [Germanic/docs/DEV_NOTES.md:1798-1800].

More such English-side diagnostics follow in the short-vowel and KIT notes. `*bardaz` appears as one of the vowel-rule probes that “no longer branch” [Germanic/docs/DEV_NOTES.md:1808-1812], and later `beard` is counted among the stubborn `{ɪə}+r` / KIT-adjacent modern outputs (`beard/bier/deer/spear/year`) needing post-vocalic `/r/` smoothing [Germanic/docs/DEV_NOTES.md:2306-2324]. These passages are worth retaining only so later readers do not confuse them with row-1940 OE policy. They are superseded or diagnostic only for this slice: later-English engineering history, not authority for the Old English row.

## Open questions for later work

- If row 1940 is ever proposed for indexing, decide whether the present DEV_NOTES record is strong enough on its own. It is more substantial than a pure no-note row, but most of the preserved discussion is cascade chronology and regression analysis rather than a standalone lexeme dossier [Germanic/docs/DEV_NOTES.md:22065-22325; Germanic/docs/lexeme_reports/coverage_audit.md:196-196].
- If A-restoration work is revised again, re-check that `*bárdaz` stays out of the live exception bucket. DEV_NOTES preserves both the temporary regression (`*bárdaz → bard`) and the later narrowing (“no A-restoration question”), so a future rule rewrite should verify that those two layers remain consistent [Germanic/docs/DEV_NOTES.md:22241-22325; Germanic/docs/DEV_NOTES.md:30599-30612].
- If a later packet or research memo is created, it would be useful to add explicit handbook citations for OE `beard` and for the chronology of breaking after fronting. The current slice can stand without a literature-agent follow-up, but its strongest support is still project-internal rather than bibliography-driven [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:106-125; Germanic/docs/analysis/arestoration_r_l_research.md:724-728].
