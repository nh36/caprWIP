# Research memo — 2058 have / hæfeþ

## Starting point

- **ID:** 2058
- **CONCEPT:** have
- **COUNTERPART:** hæfeþ
- **PROTO:** *xabēną
- **PROTOFORM:** *xábēθi
- **DERIVATION_CLASS:** late_analogy
- **NOTE:** 3sg pres. indic. (lautgesetzlich); inf. habban is analogical (umlaut leveled, Fulk §12.47)

The live row already uses a paradigm-cell solution: cognate-set `*xabēną` is kept as the lexeme-level proto, but the actual derivational input is the 3sg present cell `*xábēθi`, targeting OE `hæfeþ` rather than citation-form `habban`.

## Packet evidence assessment

**Authoritative/current in the packet:**

- the live TSV row itself;
- the compact derivation trace, which now gives an exact match `*xábēθi -> hæfeþ`;
- the packet's basic project status signal that this row is no longer a live mismatch and has no `oe_known_problems.tsv` entry.

**Useful background but not final authority:**

- the `DEV_NOTES.md` excerpts on class-III stem alternation and the explicit project decision to use the 3sg present cell;
- the experimental note that both `hafēþi` and `habēþi` reach `hæfeþ`, which is useful as implementation background but not itself the philological decision;
- `old_english_wiktionary.tsv: have -> habban`, which is useful for identifying the ordinary headword, not for deciding the row target.

**Stale or superseded material in or around the packet evidence:**

- the regression note `*xábēθi -> hæfæþ` is diagnostic only; it records an earlier surface mismatch, not the current state of the row;
- older repo history, not surfaced as a packet high-confidence item, first treated the infinitive as the row target and proposed `*xabjăną` as the OE-specific input. That history matters for chronology, but it is superseded by the later paradigm-cell retargeting to `hæfeþ`.

**Irrelevant or misleading packet material:**

- the packet's concept-name collisions from unrelated `u`-lowering / `a`-restoration discussions are not evidence about `have`;
- the packet has no dedicated dossier hit for this row, so generic cross-row methodological snippets should not be promoted to row-specific authority.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at 4091-4145, 4326-4350, and 11548-11842.
- `Germanic/docs/dossier-spar-2025.md` for the broader repo treatment of OE weak class III as a residual category.
- `docs/references/campbell_old_english_grammar.txt` at §762/§766 passages (`22982-23161`, `23353-23366`).
- `docs/references/legacy/fulk_comparative_grammar_early_germanic.txt` at the §12.47 discussion of `habban` and umlaut leveling (`22552-22557`).
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` at the class-III present discussion (`2202-2203`, `5825-5827`, `20687-20724`).
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` and `docs/references/orel_handbook_germanic_etymology.vision.txt` for lexeme-level proto/headword treatment.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/data/oe_known_problems.tsv` (no entry for this row).
- `Germanic/tools/oe_paradigm_probe.py`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`, which confirms that row 2058 still has no pilot/final lexeme report.

That wider search did **not** uncover a dedicated have-specific dossier or an existing pilot report for this lexeme. The decisive evidence remains the class-III discussion in `DEV_NOTES` plus the in-repo reference texts.

## Reconstruction and early-stage forms

This row needs a three-way distinction kept explicit:

1. **Cognate-set proto / etymological headword:** TSV `PROTO` `*xabēną`, matching the lexeme-level dictionary tradition (`*habēn-` in Kroonen/Orel style), i.e. the broad Germanic verb 'have'.
2. **Project input form for derivation:** TSV `PROTOFORM` `*xábēθi`, the selected present-indicative **3sg** cell, ultimately reflecting the class-III non-`*-j-` stem (`*habaiþi > *habēþi` in the repo's staging).
3. **OE target form represented by the row:** `hæfeþ`, an OE 3sg present form, not the infinitive headword.

The important alternative form in the repo history is `*xabjăną`, the infinitival / `*-j-`-stem input. That form is crucial background because it explains why the ordinary OE infinitive should have passed through the geminating, umlauting pathway and why the FST's regular outcome there is `hebban`, not attested `habban`. But `*xabjăną` is **not** the live row input anymore.

So the current row is not saying that `*xabēną` directly yields `hæfeþ`. It says: keep `*xabēną` as the lexeme-level proto, but derive the OE row from the distinct 3sg paradigm cell `*xábēθi`.

## Old English philology

Philologically, three levels must stay separate:

- **ordinary lemma / citation form:** `habban` in the lexical tables and dictionaries;
- **more familiar WS singular paradigm:** syncopated `hæfð` beside `hæbbe, hæfst`;
- **selected row target:** unsyncopated `hæfeþ`, i.e. the regular 3sg cell the project wants to represent.

The repo evidence supports the unsyncopated class-III cell, but exact normalized `hæfeþ` should be handled carefully.

- Campbell §762 gives occasional WS uncontracted 2/3sg forms like `segep, hygep`, and specifically says `hafast, hafað` occur occasionally in WS prose.
- The same Campbell material also preserves Anglian/Rushworth fronted unsyncopated forms in OCR as `hxfest, hzfep`, which are best read as support for fronted `hæfest, hæfeþ`-type forms, though the exact token is not cleanly normalized in the packet.
- Ringe & Taylor explicitly reconstruct the class-III 2/3sg pathway and cite Northumbrian outcomes `heefes, hefed`.
- Fulk's point is different: he explains why the `*-j-` forms such as the infinitive/plural lost umlaut analogically, perhaps to avoid confusion with `hebban` 'raise'.

So `hæfeþ` is best treated as a **normalized OE 3sg present form supported by class-III evidence**, not as the default dictionary headword and not as a form that should erase the attested analogical infinitive `habban`.

## Project problem and solution

The project problem is the mismatch between the inherited class-III morphology and the ordinary OE citation form.

- If the row targets the infinitive, the correct derivational input is `*xabjăną`, and the FST gives regular `hebban`; attested `habban` is analogical.
- If the row instead targets the 3sg present indicative, the class-III non-`*-j-` stem gives a regular outcome of the `hæfeþ` type.

The live project solution is therefore coherent:

- keep `PROTO = *xabēną` as the cognate-set proto;
- keep `PROTOFORM = *xábēθi` as the selected paradigm-cell input;
- keep `COUNTERPART = hæfeþ` as the row target;
- keep `DERIVATION_CLASS = late_analogy`, because the row still exists to avoid the later analogical citation-form/plural remodeling centered on `habban`.

In short: row 2058 is a paradigm-cell rescue of a lexeme whose ordinary OE headword is analogical, not a claim that `hæfeþ` replaced `habban` as the lexeme's lemma.

## Paradigm probe

A paradigm probe **is required** for this row, because the whole justification for the entry is the contrast between the analogical citation-form side of the paradigm and the selected regular 3sg cell.

The repo currently has **no built-in `oe_paradigm_probe.py` spec** for `have / hæfeþ`, so the missing probe should cover at least:

- **pres. inf.** `*xabjăną` -> regular FST output `hebban` (showing why attested `habban` is analogical);
- **pres. 3sg. indic.** `*xábēθi` -> `hæfeþ` (the live TSV solution);
- **a `*-j-` present-plural cell** such as `*xabjanþ` / project-normalized equivalent -> expected umlauted/geminated plural output, to show why `habbaþ` belongs with the leveled infinitive side rather than with the selected 3sg cell.

The first two cells are the minimum decisive comparison. The plural cell is the main missing control if the final report wants to show that the analogical restructuring affected more than just the infinitive.

## Recommended final report

Recommend a concise final report that says the lexeme-level proto remains `*xabēną`, but row 2058 intentionally derives the OE verb through the regular 3sg class-III cell `*xábēθi -> hæfeþ` because ordinary `habban` belongs to the analogically leveled `*-j-` side of the paradigm. It should note that `hæfeþ` is a normalized unsyncopated OE 3sg backed by Campbell/Ringe-Taylor evidence, not the citation headword.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended; `hæfeþ` is still the right project target for the selected 3sg cell.
- **TSV `DERIVATION_CLASS`:** no change recommended; `late_analogy` remains an acceptable label for this paradigm-cell solution to an analogical lexeme.
- **TSV `NOTE`:** **change recommended** — tighten it so it explicitly distinguishes lexeme-level `PROTO` `*xabēną` from selected row input `*xábēθi`, and say that `hæfeþ` is the normalized unsyncopated 3sg target while `habban` is the analogical citation form.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` text:** **change recommended** in light-touch form. The earlier `*xabjăną -> habban` "TSV proto error" section should be marked more explicitly as superseded by the later paradigm-cell decision at `### Paradigm Cell Choice: habban -> hæfeþ (3sg)`, so future searches do not treat the abandoned infinitive-target analysis as current.
- **Dossier text:** no change recommended. No dedicated have-specific dossier was found; `dossier-spar-2025.md` is only general class-III background and does not need row-specific cleanup.
