# Research memo — 1943 begin / beġinnan

## Starting point

- **ID:** 1943
- **CONCEPT:** begin
- **COUNTERPART:** beġinnan
- **PROTO:** *bigínnaną
- **PROTOFORM:** *bigínnaną
- **DERIVATION_CLASS:** regular
- **NOTE:** Palatalization of *g between *i and *i is regular per R/T §6.4.1 Rule 1. OE beġinnan confirmed (Wiktionary, BT).
- **HISTORY:** none in the TSV row.
- `coverage_audit.md` lists this row as report-required because the TSV `NOTE` is non-empty and no manual report yet covers it.

## Packet evidence assessment

**Authoritative/current:**
- The live TSV row and the current compact trace/debug snapshots agree on `*bigínnaną > beġinnan`.
- The current FST (`Germanic/fsts/germanic.txt`) still derives the form by ordinary OE velar palatalization plus `OEPrefixIReduction`.
- The packet's lexical-table evidence is useful as lemma support: `old_english_wiktionary.tsv` has `beginnan`, and Bosworth-Toller / Clark Hall support the same lemma spelling.
- The palatalization dossier is current background for conditioning: front-vowel environments palatalize `*g`, while front-vowel + following back-vowel cases do not.

**Useful background:**
- `DEV_NOTES.md` 6777-6922 preserves the earlier debugging history: one failed fix produced `beġennan`, then a marking-based fix restored `beġinnan`.
- `DEV_NOTES.md` 17441-17452 is especially useful because it states explicitly that `be-` here is from separate unstressed prefix lowering, not from NWGmc medial `*i > e`.

**Stale or superseded:**
- `Germanic/docs/dossier-ibreve-cleanup-2026.md` §2.3 still explains this item through the older three-step `*ĭ`-marking system as though that were the live mechanism. Later `DEV_NOTES.md` 38378-38441 and the current FST show that this case is now carried by `OEPrefixIReduction`, with `OEUnstressedIMarking2` dropped from the active composition.
- `Germanic/docs/non_firing_rules_analysis.md` line 442 (`*biginnăną -> biġinnan (expected beginnan)`) is diagnostic history only; it predates the current target/output and should not be treated as live lexical evidence.

**Irrelevant or misleading if taken too literally:**
- The TSV `NOTE` / packet wording cites R/T §6.4.1 **Rule 1**, but the exact local environment here is non-initial intervocalic `*g` between front vowels, i.e. closer to R/T **Rule 3**.
- `old_english_wiktionary.tsv` writes `beginnan` with plain `g`; in this project that is compatible with normalized `beġinnan`, so it is not counter-evidence.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at 6516-6518, 6777-6875, 17441-17452, 38373-38441.
- `Germanic/fsts/germanic.txt` at the live `OEPrefixIReduction` and `OEVelarPalatalization` definitions.
- `Germanic/docs/dossier-ibreve-cleanup-2026.md` §§2.3 and 6.
- `Germanic/docs/dossiers/g-palatalisation-conditioning.md` §§2.2-2.3.
- `Germanic/docs/non_firing_rules_analysis.md` for stale diagnostics.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `Germanic/data/old_english_wiktionary.tsv`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` ("So also bi- > be-, ni 'not' > ne.").
- `docs/references/campbell_old_english_grammar.txt` (§428 `ginnan begin`).
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` and `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` for lemma support.
- `docs/references/kluge_seebold_etymologisches_woerterbuch.txt` for comparative etymological background (`*-genn-a`).

No pilot lexeme report for this item appears to exist yet; only the packet is present.

## Reconstruction and early-stage forms

The current row is internally coherent: both TSV `PROTO` and TSV `PROTOFORM` are `*bigínnaną`, i.e. the project is modelling the **prefixed verb** directly. That should be kept distinct from Kluge's comparative background statement that the verb is a prefixed formation to a root/stem `*-genn-a`. The latter is useful etymological context, but it is **not** this row's modelling input and should not replace the TSV form.

Likewise, historical project notes that write `*biginnăną`, `*bĭg...`, or similar are internal staging/debug spellings, not rival protoforms for the TSV. For this row the clean distinction is:

- **cognate-set / comparative background:** prefixed verb built to a root/stem also described as `*-genn-a` in comparative lexicography;
- **project input form:** `*bigínnaną`;
- **OE target form:** `beġinnan`.

The current derivational story is straightforward: `*bigínnaną` undergoes regular OE palatalization of `*g` in a front-vowel environment, then the unstressed prefix vowel is reduced (`bi- > be-`), yielding the normalized target `beġinnan`.

## Old English philology

This row is about the **infinitive citation form**, not an oblique paradigm cell. Repo-local lexical support is consistent on the lemma: `old_english_wiktionary.tsv`, Bosworth-Toller, and Clark Hall all support `beginnan`/`be-ginnan` as the dictionary form. The project's `beġinnan` spelling is therefore best understood as a normalized phonological/orthographic representation of palatal `g`, not as a different lexeme.

Campbell's `ginnan begin` is useful only as background evidence that palatal `g` before front-vowel environments is a real OE phenomenon; it is not direct proof that the prefixed lemma itself should be cited without further qualification. Conversely, nothing in the repo material supports a strong dialect/manuscript claim for this row, so the eventual report should avoid over-claiming a specific dialectal status.

This is not an `attested_variant` or `reconstructed_oe` case. The main philological caution is simply to avoid conflating plain-dictionary `g` spelling with the project's normalized `ġ`.

## Project problem and solution

The project issue here was implementation chronology, not uncertainty about the OE target. Earlier debugging history shows two different failure modes:

- missing prefix reduction / wrong handling gave outputs like `biġinnan`;
- an overbroad lowering fix damaged the stressed root vowel and produced `beġennan`.

Current evidence shows the row is now behaving as intended. The live solution is:

1. regular OE velar palatalization gives palatal `ġ` in the `i-g-i` environment;
2. separate OE unstressed prefix reduction gives `bi- > be-`;
3. the root vowel remains `i`, so the correct target is `beġinnan`.

So the row should remain a **regular** row describing an inherited prefixed infinitive, not a paradigm-selection or analogical exception case.

## Paradigm probe

No paradigm probe is required.

Reason: `PROTO` and `PROTOFORM` are identical, the row is not choosing an oblique cell, and the whole issue is a resolved segmental/chronological one already visible in the citation-form trace. This is unlike the late-analogy or known-unmodelled cases for which `oe_paradigm_probe.py` was built.

## Recommended final report

Recommend a **short** final lexeme report only. It should:

- distinguish comparative `*-genn-a` background from the row's actual input `*bigínnaną`;
- say that `ġ` is regular OE palatalization of `*g` in the front-vowel environment;
- say that `be-` reflects separate unstressed prefix reduction (`bi- > be-`), not NWGmc medial `*i > e`;
- cite dictionary support cautiously (`beginnan` in Wiktionary / BT / Clark Hall) without turning plain `g` spelling into a variant problem;
- omit any paradigm-probe subsection.

## Data-change recommendations

- **TSV `PROTO`:** no change.
- **TSV `PROTOFORM`:** no change.
- **TSV `COUNTERPART`:** no change.
- **TSV `DERIVATION_CLASS`:** no change.
- **TSV `NOTE`:** **change recommended.** The note should separate the two facts now blurred together: (1) regular palatalization of `*g` in the actual OE environment, and (2) separate unstressed prefix reduction `bi- > be-`. It should also replace the current citation to R/T §6.4.1 **Rule 1** with a more exact description/reference for the intervocalic/front-vowel `*g` case.
- **`oe_known_problems.tsv`:** no change.
- **`DEV_NOTES` text:** no change required; the later entries already preserve the debugging chronology and the present resolution.
- **DEV_NOTES/dossier text:** **dossier change recommended.** If `Germanic/docs/dossier-ibreve-cleanup-2026.md` is still being used as a live explanatory source, its begin subsection should be marked as superseded by the later `OEPrefixIReduction` solution documented in `DEV_NOTES.md` §17.36.3 and in the current FST. Without that, it is too easy to cite an outdated mechanism as current authority.
