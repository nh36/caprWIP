# Research memo — 2268 wake / wacan

## Starting point

- **ID:** 2268
- **CONCEPT:** wake
- **COUNTERPART:** `wacan`
- **PROTO:** `*wakēną`
- **PROTOFORM:** `*wákaną`
- **DERIVATION_CLASS:** `early_analogy`
- **NOTE:** OE `wacan` is the strong verb (Class VI) 'to wake up' < PGmc `*wakaną`, not the weak Class III `*wakēną` 'to be awake' (→ OE `wacian`). The cognate set GLOSSID 299 conflates both; German `wachen` continues the weak verb.

The live row already encodes the key split: the cognate-set proto stays weak, while the OE-facing derivational input is strong. No pilot or full lexeme report for this lexeme appears to exist in the repo, so the packet is background only.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*wákaną -> wacan`; `DEV_NOTES.md` at 3891-3893 and 3965-3966, which explicitly distinguish strong `wacan` from weak `wacian`; and the current coverage/debug material showing row 2268 as a report-requiring matched row.
- **Useful background:** the packet's `old_english_wiktionary.tsv` hit; the Kroonen-based note that the strong verb is `*wakan-`; and lexicographic background from Clark Hall and Bosworth-Toller, which help separate strong `wacan` from weak `wacian`.
- **Stale or superseded:** the packet's preserved `DEV_NOTES.md` table at 3873, where row 2268 still sits under erroneous TSV `*wakēną`; the March 2026 debugging stage at 9499-9513 using `*wakăną`; and the generic "Fixed: 6" concept hit at 9538. These are useful chronology, not current lexical authority.
- **Irrelevant or misleading:** any packet inference that treats weak-verb evidence for `wacian` as if it directly proved the strong OE row; and any assumption that the packet alone settles attestation status without checking the dictionaries.

## Additional repo research

Beyond the packet, I checked:

- `Germanic/docs/DEV_NOTES.md` at 3870-3966, 9498-9515, and 10087-10095.
- `Germanic/docs/germanic_notes/weak_tail_vowels_and_a_restoration.md`, especially the discussion of weak class-II `*wakōn -> wacian`.
- `Germanic/docs/analysis/arestoration_r_l_research.md`, including the Campbell quotations on A-restoration and the inventory line for `wacian`.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/data/oe_known_problems.tsv` (checked; no row-specific entry).
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.

This extra pass confirms the packet's main point but adds one philological caution the packet does not foreground: the strong/weak split is real, yet Bosworth-Toller treats simplex `wacan` as a normalized dictionary headword whose infinitive is not directly attested, apparently displaced in the corpus by `wæcnan`.

## Reconstruction and early-stage forms

This row needs a strict three-way distinction.

1. **Cognate-set proto / etymological headword:** TSV `PROTO` `*wakēną` represents the weak 'be awake/watch' lexeme that underlies much of the non-OE cognate set and yields OE `wacian`, not the strong OE row target.
2. **Project input form for derivation:** TSV `PROTOFORM` `*wákaną` is the strong Class VI input chosen for the OE derivation. `DEV_NOTES` and packet diagnostics often write the same input as unaccented `*wakaną`; the March `*wakăną` notation is debugging history, not the live canonical row input.
3. **OE target form:** `wacan` is the normalized OE strong-verb target represented by the row.

So `PROTO` and `PROTOFORM` are not rival spellings of one reconstruction. They point to two related but distinct lexemes that the comparative cognate set has collapsed together. The project solves that by keeping the cognate-set label in `PROTO` while feeding the OE derivation from the strong verb.

## Old English philology

The philological distinction between strong `wacan` and weak `wacian` is well supported in the repo-local sources. Kroonen gives strong `*wakan-` with OE `wacan`, while Ringe/Taylor's class-III/class-II discussion treats weak `*wakē-` as the source of OE `wacian` [@Kroonen2013; @RingeTaylor2014]. Clark Hall likewise separates `wacan` 'to awake, arise, be born, originate' from `wacian` 'to be awake, keep awake, watch'.

Bosworth-Toller complicates the headword picture: under `wacan` it says "This infinitive form does not occur, its place seems taken by wæcnan." That means the row's `COUNTERPART` should be read as a normalized lexical headword for the strong verb family, not as a directly cited simplex infinitive from a specific manuscript. The strong family itself is still real in OE lexicography, since the same local dictionaries preserve forms such as preterite `wōc` and prefixed strong derivatives (`āwacan`, `onwacan`).

Accordingly, the memo should not collapse three different things: attested weak citation `wacian`, normalized strong headword `wacan`, and directly cited inflected or prefixed strong forms. The live row is about the second of these.

## Project problem and solution

The project problem is not a sound-law mismatch inside one verb class; it is a lexeme-selection problem caused by a conflated cognate set. If row 2268 were forced to inherit directly from TSV `PROTO` `*wakēną`, the expected OE target would belong with weak `wacian`, not strong `wacan`. The current row instead aims at the related strong Class VI verb.

The live project solution is therefore sensible:

- keep `PROTO = *wakēną` as the comparative/cognate-set label;
- keep `PROTOFORM = *wákaną` as the OE-facing strong input;
- keep `COUNTERPART = wacan` as the normalized strong OE target;
- explain in the note/report that weak `wacian` belongs to the other lexeme.

Within the current project taxonomy, `early_analogy` is an acceptable label for this early lexeme/stem substitution, even though the deeper issue is really cognate-set conflation rather than a late OE paradigm-cell repair.

## Paradigm probe

No paradigm probe is required.

This is not a `late_analogy` or paradigm-cell case like rows that depend on choosing 3sg, imperative, or oblique forms. The decisive move happens upstream, in selecting the strong verb `*wákaną` instead of the weak cognate-set proto `*wakēną`. If a future final report wants a diagnostic comparison, a simple contrast between the strong infinitival input and the weak `wacian` pathway would be enough; no missing OE paradigm cells need formal probing.

## Recommended final report

Recommend a concise final report stating that row 2268 intentionally separates the weak cognate-set proto `*wakēną` from the strong OE derivational input `*wákaną`, so the row represents normalized OE strong `wacan` rather than weak `wacian`; it should also note briefly that Bosworth-Toller treats simplex `wacan` as a normalized headword rather than a directly attested infinitive.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended. `*wakēną` still works as the cognate-set label for the conflated comparative set.
- **TSV `PROTOFORM`:** no change recommended. `*wákaną` is the right OE-facing strong input.
- **TSV `COUNTERPART`:** no change recommended for now. Keep `wacan`, but understand it as a normalized strong headword rather than a directly cited simplex infinitive.
- **TSV `DERIVATION_CLASS`:** no change recommended. `early_analogy` is the best available current label for this early lexeme/stem substitution.
- **TSV `NOTE`:** **yes, minor clarification recommended.** The note should say more explicitly that `wacan` is a normalized strong headword and that the weak OE citation verb is `wacian`; that would prevent readers from assuming the row's target is a directly attested simplex infinitive.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES`:** **yes, minor cleanup recommended.** Mark the old `*wakēną -> wacan` table entry and the March `*wakăną` debugging stage more explicitly as superseded, so future packets do not over-promote stale workflow history.
- **Dossier text:** no change identified. No dedicated row-specific dossier was named in the packet or TSV note, and the general A-restoration/weak-verb analysis files are still usable as background.
