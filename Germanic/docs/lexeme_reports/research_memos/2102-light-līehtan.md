# Research memo — 2102 light / līehtan

## Starting point

- **ID:** 2102
- **CONCEPT:** `light`
- **COUNTERPART:** `līehtan`
- **PROTO:** `*léuxtijaną`
- **PROTOFORM:** `*léuxtijaną`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `OE target: lēoht→līehtan (wk.v. I 'to light', matching verb proto *leuxtijăną; noun 'lēoht' from *leuxtą)`

This is a note-bearing `regular` row, so it still requires memo/report treatment even though the live derivation already succeeds. Repo searches found no existing pilot or full lexeme report for this exact lexeme; `coverage_audit.md` and the missing-reports snapshot still flag row 2102 only because `NOTE` is non-empty.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*léuxtijaną -> līehtan`; `DEV_NOTES.md` 8963, where Fulk's `*liuxtijanan > līehtan` matches the current PGmc `*-ij-` policy [@Fulk2018]; and `DEV_NOTES.md` 39278-39284, where row 2102 is listed among current `*xt` cases preserved in OE.
- **Useful background:** the packet's imported material from `ws_vs_anglian_dialect_differences.md` is useful for the broader lexical family and dialect background: related OE noun/adjective material shows WS `lēoht/léoht` beside Anglian `léht/liht`, and the same file also discusses WS `liehtan` versus Anglian `lihtan` [@RingeTaylor2014; @Campbell1959; @SieversBrunner1965]. The packet's `old_english_wiktionary.tsv` hit `light = lēoht` is useful only as family background confirming the related noun.
- **Stale or superseded:** the packet's `DEV_NOTES.md` hit at line 8727 (`*leuxtjăną ... līehtan`) comes from the explicitly superseded pre-PGmc-notation stage before the project adopted `*-ij-` spellings for heavy class-I weak verbs. It is useful as project history, but not as live row authority.
- **Irrelevant or misleading:** the packet's noun hit `lēoht` is not evidence that row 2102 should target the noun rather than the verb; the packet's various concept-name hits in unrelated analysis/dossier files (`widuwe`, general syncope notes, etc.) are false positives; and the packet's smoothing excerpts for noun/adjective `light` are background, not direct evidence that the row's verbal target should be retargeted dialectally.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at 8763-8970 and 39278-39284.
- `Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md` at 130-170, 604-646, and 708-716.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.missing_reports.md`.
- `Germanic/data/oe_known_problems.tsv` (no row-specific entry).
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/campbell_old_english_grammar.txt`.
- `docs/references/brunner_1965_altenglische_grammatik.txt`.
- `docs/references/fulk_comparative_grammar_early_germanic.vision.txt`.
- `docs/references/bright_anglo_saxon_reader.vision.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.

Main findings from that wider check:

- There is **no dedicated 2102 dossier** and no pre-existing pilot/full report for this lexeme.
- Fulk gives the comparative verb directly as `PGmc. *liuxtijanan > līehtan 'illuminate'`, which supports the row's current PGmc `*-ij-` input and OE target [@Fulk2018].
- Ringe & Taylor explicitly distinguish the verbal reflexes `PGmc *liuhtijana > OE *liohtjan > WS liehtan`, versus Anglian `Merc. lihtan, North. lihta`, and separately note late-WS `lyhtan` for a related `*linhtijana` series [@RingeTaylor2014].
- Campbell and Brunner confirm the same dialectal philology: WS `liehtan`, Anglian `lihtan`, later WS `lyhtan`, with Kentish `liohtan` also noted in Brunner [@Campbell1959; @SieversBrunner1965].
- Bright, Clark Hall, and Bosworth-Toller confirm an attested OE verb family under `lihtan/līhtan/liehtan/lyhtan`; they also show that the lexical family includes several related meanings ('illuminate', 'shine', 'grow light', 'make light/easy', 'alight'), so the report must keep the row's intended sense explicit [@ClarkHall1960; @BosworthToller1898].

## Reconstruction and early-stage forms

This row still needs the standard three-way distinction, even though TSV `PROTO` and `PROTOFORM` happen to agree:

1. **Cognate-set proto:** `*léuxtijaną` in TSV `PROTO`, i.e. the comparative Proto-Germanic weak verb; comparative sources often print this as `*liuxtijana(n)` rather than with the project's accent notation [@Fulk2018; @RingeTaylor2014].
2. **Project input form:** `*léuxtijaną` again in TSV `PROTOFORM`; the current project deliberately keeps the PGmc `*-ij-` form, not the older post-syncope shorthand `*leuxtjăną`.
3. **OE target form:** `līehtan`, i.e. the project's normalized West-Saxon verbal target.

The important contrast is therefore not a `PROTO`/`PROTOFORM` split, but **current PGmc input versus later OE dialect outputs**. Repo-local handbook evidence gives the path `*liuxtijana > *liohtjan > WS liehtan`, with Anglian smoothing to `lihtan` and later WS `lyhtan` as a subsequent spelling/outcome history [@RingeTaylor2014; @Campbell1959; @SieversBrunner1965]. The related noun/adjective material (`*leuxtą`, `*liuhtaz`) yielding OE `lēoht/léoht` belongs to the same lexical family, but it is not the row's project input and should not be collapsed with the verbal etymon.

## Old English philology

This is an **attested OE verb**, not a reconstructed-OE target and not a paradigm-cell workaround. But the philology is not just "OE = `līehtan`":

- handbook sources usually print **WS `liehtan`**, not the project's macronized `līehtan` [@RingeTaylor2014; @Campbell1959];
- Brunner explicitly contrasts **Angl. `lihten/lihtan`**, **WS `liehtan`**, and **Kent. `liohtan`** [@SieversBrunner1965];
- later West Saxon also shows **`lyhtan`** [@RingeTaylor2014; @Campbell1959];
- dictionaries index the verb family under forms like `lihtan`, `līhtan`, `liehtan`, or cross-references among them, rather than under one single universal headword spelling [@ClarkHall1960; @BosworthToller1898].

So the row's `COUNTERPART = līehtan` is best understood as a **project-normalized WS target**, not as a claim that every source headwords the verb exactly that way. The memo/report should also keep the **verb** separate from the related noun `lēoht` 'light, brightness' and adjective `leoht/liht` 'light (not heavy)', which are philologically relevant family members but not the row target.

## Project problem and solution

The live project problem is not an unresolved derivation. The FST already reaches the target, and the row remains correctly `regular`.

The real issue is **lexeme-family and normalization hygiene**:

1. packet evidence mixes current PGmc `*leuxtijăną`/`*liuxtijanan` support with superseded project shorthand `*leuxtjăną`;
2. repo background includes noun/adjective `lēoht/léoht/liht` smoothing material that is easy to mistake for direct verbal evidence;
3. source headwords vary among `liehtan`, `lihtan`, `lyhtan`, and related dictionary cross-references, whereas the TSV chooses normalized `līehtan`.

The right project reading is therefore:

- keep the row as the **regular weak verb** from PGmc `*léuxtijaną`;
- treat `līehtan` as the project's normalized WS target;
- mention Anglian `lihtan` and later WS `lyhtan` only as dialectal/orthographic background;
- keep noun/adjective `lēoht/leoht/liht` family material in the report as contrastive background, not as competing row targets.

## Paradigm probe

No paradigm probe is required.

This row is not a late-analogy or oblique-cell case, and the current derivation already matches the intended infinitive. The memo task is evidential clarification and normalization control, not proving a paradigm-cell choice.

## Recommended final report

Recommend a short final report stating that row 2102 is the regular class-I weak verb `*léuxtijaną` / comparative `*liuxtijana(n)` > OE WS `liehtan` / project `līehtan`, while explicitly distinguishing it from related noun/adjective `lēoht/leoht/liht` and noting the dialectal/background variants `lihtan` and `lyhtan`. Cite Fulk for the PGmc verb, and Ringe & Taylor plus Campbell/Brunner for the OE dialect/normalization side; no paradigm-probe subsection is needed.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended. `līehtan` is defensible as the project's normalized WS target, provided the eventual report explains that many source headwords instead print `liehtan`/`lihtan`/`lyhtan`.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** **change recommended.** The current note usefully distinguishes verb from noun, but it should say more explicitly that the row targets the normalized **WS verbal form** (`līehtan` / source `liehtan`), while `lēoht` belongs only to the related noun and Anglian `lihtan` is background rather than the selected counterpart.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` text:** **minor cleanup recommended.** The superseded heavy-stem table around line 8727 should ideally carry an even more explicit inline "old `*-jăną` notation" label so packet excerpts do not make `*leuxtjăną` look current.
- **Dossier text:** no change recommended; no row-specific dossier text was found.
