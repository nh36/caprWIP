---
row_id: 1952
concept: blood
counterpart: blōd
proto: *blōdą
protoform: *blōdą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1952 blood / blōd

## Current row state

- The live OE row currently reads `CONCEPT = blood`, `COUNTERPART = blōd`, `PROTO = *blōdą`, `PROTOFORM = *blōdą`, `DERIVATION_CLASS = regular`. The row carries inherited-source history only, not a row-local explanatory note [Germanic/data/germanic-aligned-final.tsv:80-80].
- `PROTO` and `PROTOFORM` are identical in the live TSV, so this row is **not** currently using a substitute OE-facing input, a different paradigm cell, or a repair-oriented proxy form. The active derivational input remains the same comparative protoform `*blōdą` [Germanic/data/germanic-aligned-final.tsv:80-80].
- Repo-local OE source data independently preserves the same lexeme pairing as `blood	blōd`, so the current row is not a dashed placeholder or a newly inferred counterpart without repository support [Germanic/data/old_english_wiktionary.tsv:20-20].
- `oe_known_problems.tsv` currently contains only unrelated exception rows and has no entry for `*blōdą`, `blood`, or `blōd`, so row `1952` is not being tracked as a live OE problem bucket [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure still records row `1952` as having no packet, no research memo, no attached dossier/analysis file, and issue status `none`, so the metadata link fields remain blank here [Germanic/docs/lexeme_reports/coverage_audit.md:201-201].

## Development-note summary

DEV_NOTES support for row `1952` is real but not row-packaged. No dedicated `blood / blōd` mini-dossier survives in `Germanic/docs/DEV_NOTES.md`; the core surviving material is an **archived** shared note on heavy-syllable deletion of final proto `*-ą`, and that note names this lexeme directly as a successful example [Germanic/docs/DEV_NOTES.md:1591-1637]. That means the slice should preserve two things at once: (i) the row is not undocumented, because `*blōdą → blōd` is explicitly cited in DEV_NOTES; but (ii) the strongest surviving note is project-history analysis rather than a fresh row-local literature memo.

The substance of that archived note matters. DEV_NOTES says the project implemented an “experimental rule deleting proto *-ą after heavy syllables,” motivated by the observation that most spurious final-vowel OE mismatches involved heavy stems. It then states, in wording worth preserving, that “Neither source explicitly extends this pattern to `*-ą`,” but that modeling showed “The same heavy/light conditioning that applied to `*-i/*-u` also applied to `*-ą`,” and calls the result a “learned phonological pattern” not fully articulated in the cited handbook literature [Germanic/docs/DEV_NOTES.md:1595-1615]. For row `1952`, the point is not that `blōd` was patched as a one-off. The point is that `*blōdą` was treated as one of the lexemes supporting a broader empirical generalization about heavy-stem OE apocope of final nasalized `*-ą` [Germanic/docs/DEV_NOTES.md:1599-1633].

DEV_NOTES is also explicit about implementation history. The same note says the project added `OldEnglishHeavySyllableNasalApocope`, extended `OldEnglishHeavyMarker` so `*-ą` could be marked after heavy syllables, and placed the new rule after `OldEnglishHighVowelApocope` but before `OldEnglishWeakTailReduction` [Germanic/docs/DEV_NOTES.md:1617-1620]. The tracked result was a net reduction from 282 to 262 mismatches, including `final_vowel_extra: 60 → 19`, and the examples list includes the exact row outcome: ``*blōdą → blōd` ✓ (was: blōda)` [Germanic/docs/DEV_NOTES.md:1622-1633]. For replacement-note purposes, this is the most important surviving statement of why the current OE row is regular in repo terms.

Two later current DEV_NOTES passages sharpen how that result should be read. First, the project’s notation inventory uses `*blōdą` itself as the example of a **stressed long root vowel** and separately defines `ą` as an **unstressed nasalized vowel (inflection)** [Germanic/docs/DEV_NOTES.md:20570-20578]. That supports the structural interpretation behind the heavy-syllable note: `*blōdą` is exactly the kind of form the project expects to be heavy in the root and weak in the final ending. Second, a later current rule-scoping note uses `*blōdai → blōde` as a regression-risk control and insists that polysyllabic inflected forms must remain untouched by any guard against overbroad final-long-vowel shortening [Germanic/docs/DEV_NOTES.md:37629-37641]. That later note does **not** compete with the row’s nom./acc. singular `blōd`; instead, it preserves an important scope distinction inside the same lexeme family: `*blōdą → blōd` is the heavy-stem final-`*-ą` case, whereas `*blōdai → blōde` is a different, still-productive inflectional pathway that later cleanup rules must not accidentally destroy.

The safest overall reading is therefore conservative but positive. Row `1952` currently looks stable and regular in repo terms, and DEV_NOTES does preserve explicit support for the specific OE surface `blōd`. But the key explanation is still an archived empirical-discovery note whose own wording stresses that the `*-ą` extension was inferred from model behavior rather than directly spelled out in the cited authorities [Germanic/docs/DEV_NOTES.md:1595-1615]. Later writers should preserve that epistemic status rather than silently rewriting the row as if DEV_NOTES already contained a fully literature-settled, row-specific philological essay.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1591-1637

- Source heading: `Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY`
- Source line or section hint: `lines 1591-1637`
- Fragment type: `shared_rule_discussion_with_row_explicit_hit`
- Status: `archived_but_material`
- Issue tags: `heavy_syllable`; `final_ą_loss`; `oe_apocope`; `row_explicit_example`
- Recommended next use: `cite_when_explaining_why_blōd_is_not_a_one_off`
- Shared with row IDs: other heavy-stem OE rows in the same `*-ą` cleanup pass

This is the core surviving DEV_NOTES support for row `1952`. It says the project “Implemented experimental rule deleting proto *-ą after heavy syllables,” then immediately frames the evidentiary problem: “Neither source explicitly extends this pattern to `*-ą`” [Germanic/docs/DEV_NOTES.md:1595-1607]. The note nevertheless concludes that “The same heavy/light conditioning that applied to `*-i/*-u` also applied to `*-ą`,” calls the result a “learned phonological pattern,” and records the rule/pipeline changes that made the improvement possible [Germanic/docs/DEV_NOTES.md:1609-1620].

For this lexeme the decisive sentence is the example list itself: ``*blōdą → blōd` ✓ (was: blōda)` [Germanic/docs/DEV_NOTES.md:1627-1633]. That makes the fragment stronger than generic background. It is an explicit in-repo claim that this exact row outcome was one of the successful motivations for the heavy-syllable `*-ą` apocope generalization.

### DEV_NOTES:line-20570-20578

- Source heading: `Inventory`
- Source line or section hint: `lines 20570-20578`
- Fragment type: `current_notation_context`
- Status: `current`
- Issue tags: `notation`; `stress`; `heavy_root`; `unstressed_inflection`
- Recommended next use: `cite_if_proto_structure_needs_explanation`
- Shared with row IDs: all rows using the current accented/weak-tail proto inventory

This fragment matters because it makes the internal structure of `*blōdą` explicit in current project notation. DEV_NOTES uses `*blōdą` itself as the example under “Stressed long root vowel,” while a separate row identifies `ą` as “Unstressed nasalized vowel (inflection)” [Germanic/docs/DEV_NOTES.md:20572-20578]. For row `1952`, that is the compact current notation statement underlying the archived apocope analysis: the root is heavy because it contains a stressed long vowel, and the deleted segment is the unstressed final inflectional nasal vowel.

This is not a row-specific derivation note by itself. Its value is explanatory control. It keeps later prose from flattening `*blōdą` into an opaque whole and helps justify why the archived heavy-syllable note treats this lexeme as a textbook heavy-root + weak ending configuration.

### DEV_NOTES:line-37629-37641

- Source heading: `Regression risk table and guard condition`
- Source line or section hint: `lines 37629-37641`
- Fragment type: `current_scope_control_for_same_lexeme_family`
- Status: `current`
- Issue tags: `scope_guard`; `regression_control`; `inflectional_forms`; `same_lexeme_family`
- Recommended next use: `cite_if_future_rule_changes_touch_blood_forms`
- Shared with row IDs: rows implicated in the stressed-monosyllable final-vowel guard work

This fragment is not about the nominative/accusative singular row directly, but it bears on row `1952` because it names a different inflected form of the same lexeme: `*blōdai | blōde | Final *-ai → -e` [Germanic/docs/DEV_NOTES.md:37629-37635]. DEV_NOTES then stresses that such forms are “polysyllabic” in the relevant sense and that a properly guarded rule leaves them untouched [Germanic/docs/DEV_NOTES.md:37637-37641].

For this slice, the point is to preserve scope. The project’s support for `*blōdą → blōd` does **not** authorize indiscriminate deletion or shortening of any final vowel in the `blood` paradigm. Later rule changes must still preserve ordinary inflected outcomes like `blōde`. That makes this a genuinely relevant shared fragment rather than a stray same-lemma search hit.

## Superseded or diagnostic material

- The strongest row-relevant DEV_NOTES passage is explicitly **archived** and explicitly presented as empirical discovery. Later writeups should therefore keep its status clear: it is strong repo-history evidence for why the current row reads `blōd`, but it is not the same thing as a finished literature-backed lexeme memo [Germanic/docs/DEV_NOTES.md:1591-1615].
- The archived note itself preserves the key caution that should not be erased in summary prose: “Neither source explicitly extends this pattern to `*-ą`” [Germanic/docs/DEV_NOTES.md:1604-1607]. Any later claim that the handbooks straightforwardly state `*blōdą → blōd` would overstate what this note actually says.
- The later `*blōdai → blōde` control is best treated as a **scope guard**, not as a competing derivation for the row. It matters because it protects the lexeme family from future overbroad final-vowel rules, not because it replaces the nominative/accusative singular pathway documented for row `1952` [Germanic/docs/DEV_NOTES.md:37629-37641].

## Open questions for later work

- If a literature-facing packet is ever created for row `1952`, it would be worth checking whether Campbell, Hogg, Fulk, Brunner, or Ringe–Taylor give a more direct statement for heavy-stem loss of final neuter `*-ą` than the archived note had available. The current replacement note can preserve the repo’s reasoning honestly, but that reasoning is still framed as an inferred extension rather than a directly quoted handbook rule [Germanic/docs/DEV_NOTES.md:1604-1615].
- If later indexing work is considered, keep the lexeme-family distinction explicit near the top: live row `*blōdą → blōd` for the singular target, versus separately preserved inflectional control `*blōdai → blōde` [Germanic/data/germanic-aligned-final.tsv:80-80; Germanic/docs/DEV_NOTES.md:37629-37641].
- On present evidence, this slice is strong enough to serve as a replacement working note, but any future “index-worthy” judgment should be made cautiously. The row has a direct explicit DEV_NOTES hit, yet that hit is archived/shared rather than a dedicated modern row memo [Germanic/docs/DEV_NOTES.md:1591-1637].
