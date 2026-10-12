---
row_id: 2287
concept: whore
counterpart: hōre
proto: *xōrōn
protoform: *xōrōn
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2287 whore / hōre

## Current row state

- CONCEPT: `whore`
- COUNTERPART: `hōre`
- PROTO: `*xōrōn`
- PROTOFORM: `*xōrōn`
- DERIVATION_CLASS: `regular`
- The live TSV row is unusually simple at face value: `COUNTERPART = hōre`, `PROTOFORM = *xōrōn`, `PROTO = *xōrōn`, and the source-note field still contains only duplicated inherited-etymology placeholders rather than any row-local philological note [Germanic/data/germanic-aligned-final.tsv:2287-2287].
- Unlike rows such as `wæter` or `hwīnan`, the distinction among **PROTO**, **PROTOFORM**, and **COUNTERPART** is analytic rather than contrastive here. `PROTO = *xōrōn` is the dataset's comparative lexeme label, `PROTOFORM = *xōrōn` is also the active derivational input because no alternate paradigm cell or repair preform is currently needed, and `COUNTERPART = hōre` is the attested Old English reflex in the row's target language [Germanic/data/germanic-aligned-final.tsv:2287-2287; Germanic/data/old_english_wiktionary.tsv:344-344].
- Existing row-specific support infrastructure is absent. `coverage_audit.md` still marks row 2287 as having no packet, no memo, no linked note anchor, and `none` for report infrastructure, which matches the file search result for the designated packet/memo/pilot locations [Germanic/docs/lexeme_reports/coverage_audit.md:411-411].
- The published derivation snapshot is mechanically clean: the compact trace block for `# whore` lists `PROTO: *xōrōn`, `EXPECTED: hōre`, `OUTPUTS: hōre`, so the current cascade does not treat the row as a live mismatch or workaround case [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.txt:8651-8654].

## Development-note summary

The surviving DEV_NOTES material for row 2287 is real but thin, and that thinness should be stated plainly. No lexeme-local dossier on `hōre` survives in `Germanic/docs/DEV_NOTES.md`. Instead, the row appears only inside the project's broader documentation of the West Germanic rule `*ō → *a` before word-final `*r`. That means this slice should not pretend that the project carried out a row-specific controversy review for `hōre`; what survives is shared sound-law documentation plus ordinary lexical confirmation from the reference files.

Within that shared material, the row is nonetheless useful because it is a clean example of the rule operating without secondary complications. DEV_NOTES formalizes the relevant Auslautgesetz as “**Bimoric `*ō` → `*a` word-finally and before word-final `*r`**” and illustrates it first with `*fedwōr` and `*watōr` [Germanic/docs/DEV_NOTES.md:16527-16534]. Later, in the Stiles summary table, the same rule is explicitly extended to this lexeme: ``*xōrōn | *ō → *a before *r# | *xōran → hōre ✓`` [Germanic/docs/DEV_NOTES.md:16785-16789]. For future work, that is the main project-local statement that connects the general rule directly to row 2287.

The philological baseline outside DEV_NOTES is straightforward and agrees with the row. Kroonen gives `*hōrōn- f. 'whore'` with OE `hōre`, alongside the expected West Germanic cognates including OHG `huora` [@Kroonen2013; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:13412-13415]. Orel likewise reconstructs `*xōrōn sb.f.` with ON `hóra`, OE `hóre`, MLG `hōre`, and OHG `huor`, explicitly deriving the noun from `*xōraz` [@Orel2003; docs/references/orel_handbook_germanic_etymology.vision.txt:21230-21233]. Clark Hall then gives the ordinary OE lexical target as `hōre f. whore, prostitute` [@ClarkHall1960; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:22914-22914]. Nothing in those lexical sources suggests that the OE form requires analogical retargeting, special paradigm selection, or exception-bucket handling.

Fulk's comparative grammar is also useful here because it ties the noun-family to a deeper inherited base rather than merely listing daughter-language matches. In the consonant-development discussion, Fulk cites “PIE `*keh₂-ro-` in Go. `hōrs` ‘adulterer', OE `hōre` 'whore', etc.” [@Fulk2018; docs/references/fulk_comparative_grammar_early_germanic.vision.txt:6380-6383]. That does not itself prove the `*ō → *a before final *r` step, but it reinforces that the repo's `*xōrōn` / `*hōrōn-` family is standard comparative material rather than a project-internal invention.

The most important caution for later report-writing is therefore methodological rather than lexical. Because `hōre` enters DEV_NOTES only as a confirming table example, the row should be described as **supported by shared rule documentation**, not as possessing a strong independent DEV_NOTES narrative of its own. The row's current `regular` label is plausible and the implementation trace agrees with it, but the development-note basis is still mostly inherited from the larger `*ō → *a before final *r` discussion rather than from any dedicated `hōre` note [Germanic/docs/DEV_NOTES.md:16525-16573,16785-16789; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.txt:8651-8654].

A second distinction worth preserving is chronological. Later DEV_NOTES work on unstressed long-vowel shortening insists that OE late unstressed `*ō` also goes to `a`, but by a different and much later process; DEV_NOTES explicitly contrasts that late change with the earlier PWGmc/WGmc pre-final-`r` rule [Germanic/docs/DEV_NOTES.md:19623-19739,19866-19901]. For row 2287, this matters because `hōre` belongs to the **early inherited pre-final-`r` pathway**, not to the late OE unstressed-shortening pathway used to explain forms like `macaþ` or `mōnaþ`. The row should not be cited as evidence for the later rule merely because both rules can be paraphrased as `*ō → *a`.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-16525-16573

- Source heading: `The *ō → *a Rule (R/T §3.1.4)`
- Source line or section hint: `lines 16525-16573`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `pre_final_r_shortening`; `shared_sound_change`; `regular_reflex`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2274; 2127; 2287`

This is the main rule statement the row depends on, even though `hōre` is not named in the first illustration list. DEV_NOTES defines the relevant Auslautgesetz in compact form: “**Bimoric `*ō` → `*a` word-finally and before word-final `*r`**,” with `*fedwōr` and `*watōr` as the headline examples [Germanic/docs/DEV_NOTES.md:16527-16534]. The section is valuable for row 2287 because it identifies exactly which sound law makes a preform like `*xōrōn` compatible with OE `hōre`: not a late OE repair, not epenthesis, and not analogical leveling, but the shared PWGmc/WGmc shortening before final `*r`. Its limitation should also be preserved: the fragment is rule-level support, not a lexeme-local dossier.

### DEV_NOTES:line-16785-16789

- Source heading: `Implementation validation` table inside the Stiles summary
- Source line or section hint: `lines 16785-16789`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `explicit_row_example`; `shared_validation_table`; `xōrōn`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the narrowest but most directly row-relevant surviving anchor. DEV_NOTES explicitly includes the lexeme in the validation table: ``*xōrōn | *ō → *a before *r# | *xōran → hōre ✓`` [Germanic/docs/DEV_NOTES.md:16785-16789]. That line is strong enough to show that the project did consciously check row 2287 against the rule after the `PWGmcFinalOrLowering` work was in place. At the same time, the fragment is thin: it proves direct inclusion in the shared table, but it does not supply any broader lexical discussion beyond “this rule yields the expected OE form.”

### DEV_NOTES:line-19623-19901

- Source heading: `§15.2: RESEARCH — Unstressed *ō Shortening: *ō → *a, NOT *o`; `Important distinction: bimoraic vs trimoraic *ō in OE chronology`
- Source line or section hint: `lines 19623-19901`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `chronology`; `early_vs_late_ō_to_a`; `do_not_conflate_rules`
- Recommended next use: `cite_as_chronology_guardrail`
- Shared with row IDs: `2127; 2274; 2287`

This fragment is not about `hōre` by name, but it is important as a safeguard against overreading the row. DEV_NOTES distinguishes two different changes that can both look like `*ō → *a`: an **early** PWGmc/WGmc shortening before final `*r`, which feeds Anglo-Frisian developments and underlies forms like `wæter`, and a **late** OE unstressed-long-vowel shortening, which yields stable `a` in forms like `macaþ` and `mōnaþ` [Germanic/docs/DEV_NOTES.md:19668-19702,19871-19901]. For row 2287, the practical use is negative but important: `hōre` belongs with the early inherited pre-final-`r` rule and should not be cited as evidence for the later unstressed-shortening rule just because both rules share the surface notation `*ō → *a`.

## Superseded or diagnostic material

- No superseded row-specific DEV_NOTES note was located for `hōre`. That absence matters because it means there is no preserved project history of failed target selection, no analogical workaround phase, and no row-local debate to summarize. The slice should remain conservative about this rather than reverse-engineering a controversy from the mere existence of a shared rule table.
- The derivation trace is diagnostic support, not DEV_NOTES evidence. Its value is that it confirms the current cascade already derives `hōre` from `*xōrōn` without repair (`EXPECTED: hōre`, `OUTPUTS: hōre`) [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.txt:8651-8654].
- `coverage_audit.md` is similarly infrastructural, not philological. Its `no` / `none` state for row 2287 is useful only to show that this slice is filling a real gap in row-local note coverage rather than replacing a packet or memo already present [Germanic/docs/lexeme_reports/coverage_audit.md:411-411].

## Open questions for later work

- If a final lexeme report is eventually written, decide whether the report should normalize the proto spelling to the handbook-style `*hōrōn-` while still recording that the live TSV currently stores `*xōrōn`; this slice records both without attempting to resolve orthographic normalization.
- If later indexing work requires stronger row-local anchors, row 2287 may still remain a weak candidate because its best DEV_NOTES support is shared-rule material rather than an independent lexeme discussion.
- If the project later consolidates a dedicated note on the whole `*ō → *a before final *r` class, `hōre` would be a good minimal comparator beside `wæter` and `fēower`, precisely because it currently looks regular and uncomplicated.
