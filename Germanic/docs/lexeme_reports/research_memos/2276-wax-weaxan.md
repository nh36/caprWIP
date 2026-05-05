# Research memo — 2276 wax / weaxan

## Starting point

- **ID:** 2276
- **CONCEPT:** wax
- **COUNTERPART:** `weaxan`
- **PROTO:** `*wáxsaną`
- **PROTOFORM:** `*wáxsaną`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `OE target: weax→weaxan (inf. of str.v. class VI; noun 'weax' in *waxsą row)`

This is a note-bearing regular row. `coverage_audit.md` marks row 2276 as report-requiring because the TSV `NOTE` is non-empty, and no pilot/full lexeme report for this lexeme turned up in the repo.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace, which already gives `*wáxsaną -> weaxan`; and the packet's direct `DEV_NOTES.md` row inventory showing that rows 2275-2276 are ordinary `*xs` cases that do **not** depend on the preconsonantal `x`-loss rule.
- **Useful background:** the packet's Campbell/Brunner material on `weaxan` and `wæstm` is genuinely helpful for chronology. It shows that `xs > s` belongs to `*xs + C` environments such as `wæstm`, while citation-form `weaxan` itself keeps `x`/`xs`.
- **Stale or superseded / diagnostic only:** the packet's lexical-table hit `wax -> weax` is noun-oriented background only, not authority for the verb row. Generated debug snapshots are useful as project-state artifacts but are not independent philological authority.
- **Irrelevant or misleading:** the note's shorthand `weax→weaxan` is easy to misread as if bare `weax` were the row's OE base or paradigm cell. In repo-local philology, bare `weax/wax` is ambiguous: it can point to the separate noun row 2275, and dictionary material also records `wax/wēox` as a preterite form of the verb. That shorthand therefore obscures rather than clarifies the present row.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/germanic-aligned-final.tsv` around rows 2275-2276.
- `Germanic/data/oe_known_problems.tsv` — no row-specific entry for `*wáxsaną` / `weaxan`.
- `Germanic/docs/DEV_NOTES.md` around the Campbell quotation (`8151-8155`), the A-restoration inventory (`30500-30510`), and the `x`-loss discussion plus row inventory (`39058-39276`).
- `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md` — older diagnostic material for noun-row `*waxsą -> weahsa (exp. weax)`, relevant only as stale background.
- `Germanic/docs/lexeme_reports/source_inventory.md` and `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/campbell_old_english_grammar.txt`.
- `docs/references/brunner_1965_altenglische_grammatik.vision.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bright_anglo_saxon_reader.vision.txt`.

No dedicated wax/weaxan dossier, analysis memo, or pilot report was named in the packet or TSV note, and none was found elsewhere in the repo beyond the general `DEV_NOTES` and handbook material.

## Reconstruction and early-stage forms

This row needs the usual three-way distinction:

1. **Cognate-set proto / etymological headword:** comparative sources use lemma-style forms such as Kroonen's `*wahs(j)an-` and Orel's `*waxsanan`, while Ringe-Taylor discuss historical staging from PGmc `*wahsijana` to NWGmc/West Germanic verbal forms.
2. **Project input form:** TSV `PROTO` and `PROTOFORM` are both `*wáxsaną`, the exact derivational input used by the project pipeline.
3. **OE target form:** `weaxan`, the Old English infinitive/citation form represented by row 2276.

The packet trace is internally coherent for the project input: `*wáxsaną` undergoes brightening and breaking (`*wæxsaną > *weaxsaną`) and surfaces as `weaxan`. Nothing in the extra repo check requires changing TSV `PROTO` or `PROTOFORM`; the main caution is simply not to collapse comparative headword shapes such as `*wahs(j)an-` into the live TSV input.

## Old English philology

This is an **attested** OE verb row, not a reconstructed-OE case. Repo-local dictionaries/readers support `weaxan` as the infinitive/headword, with spelling variants such as `weahsan`, `wexan`, and `wæxan`, and with related non-citation forms including present `wihst` / `wiex` and preterite `wēox` / `wōx`.

That matters because the current note points back to bare `weax`, but bare `weax/wax` is not a safe label for the infinitive:

- row 2275 separately uses `weax` for the noun `wax`;
- Clark Hall also records `wax = wēox`, a preterite singular of `weaxan`;
- Brunner and Bright explicitly treat `weaxan` as the verb lemma and note that it has adopted a reduplicating-type preterite.

So the philological target here is straightforwardly the infinitive `weaxan`, while noun `weax` and preterite `wax/wēox` belong to different lexical or paradigm slots.

## Project problem and solution

The project problem is not a live sound-change failure. The row already derives correctly and remains correctly classified as `regular`.

The real issue is **documentation framing**. The note currently explains the row by saying `weax→weaxan` and by pointing to the noun row, but that wording blurs together:

- the separate noun row 2275 `weax`;
- the verb row 2276 `weaxan`;
- and the fact that bare `wax/weax` can also show up in dictionary material as a non-infinitival verbal form.

The right project solution is therefore:

- keep `PROTO = PROTOFORM = *wáxsaną`;
- keep `COUNTERPART = weaxan`;
- keep `DERIVATION_CLASS = regular`;
- rewrite the note so it says directly that row 2276 targets the OE strong-verb infinitive `weaxan`, with row 2275 `weax` mentioned only as a separate noun row if that disambiguation is still desired.

## Paradigm probe

A paradigm probe is **not required** for this memo.

This row is not being rescued by a hidden paradigm-cell choice: the live citation-form input already yields the intended infinitive `weaxan`, and `oe_known_problems.tsv` does not treat it as an unresolved or intentionally unmodelled case.

If an optional philological appendix were ever wanted, the most informative extra cells would be:

- infinitive `*wáxsaną -> weaxan`;
- present 2 sg. `wihst`;
- present 3 sg. `wiex` / `wyx`;
- preterite singular `wēox` / `wōx`;
- past participle `weaxen`.

But that would be explanatory background, not a prerequisite for the final report.

## Recommended final report

Recommend a short final report stating that row 2276 is an ordinary inherited OE verb row: comparative proto lemmas (`*wahs(j)an-`, `*waxsanan`, etc.) should be kept distinct from the project's live input `*wáxsaną`, and the row's actual OE target is the attested infinitive `weaxan`. The report should mention briefly that older/note-level shorthand with bare `weax` is misleading because noun `weax` and verbal non-citation forms are separate from the infinitive target. No paradigm-probe subsection is needed unless the supervisor wants an optional cell-contrast table.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** **change recommended.** The current `weax→weaxan` wording is misleading because it uses an ambiguous bare form and foregrounds the noun row rather than the verb row's own citation form. The note should instead say directly that row 2276 targets the OE strong-verb infinitive `weaxan`, optionally adding that row 2275 covers the separate noun `weax`.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES/dossier text:** no mandatory change recommended. Existing `DEV_NOTES` material is usable as background, and the older `final_vowel_apocope_investigation.md` line is diagnostic history rather than something that must be cleaned up for row 2276 specifically.
