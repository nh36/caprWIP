# Research memo — 2242 ten / tēon

## Starting point
- ID `2242`; CONCEPT `ten`; COUNTERPART `tēon`.
- Live TSV `PROTO` = `*téxun`; live TSV `PROTOFORM` = `*téxun`; TSV `DERIVATION_CLASS` = `attested_variant`.
- The current TSV note says the row was retargeted from WS `tīen` to `tēon` as the regular outcome of bare `*tehun` after breaking, intervocalic `h`-loss, and contraction; it treats WS `tien` as a secondary i-umlauted form and cites `tēoða` and `-tēontig` as preserving the un-umlauted stem.
- No standalone pilot report for this lexeme turned up in `Germanic/docs/lexeme_reports/pilot/`; the generated debug snapshot report is background only, not final authority.

## Packet evidence assessment
- **Authoritative/current:** the live TSV row; the packet’s compact trace showing the current derivation `*téxun -> tēon`; and `DEV_NOTES` `§17.48.1`, which is the fullest current repo-local source survey and clearly separates bare `*tehun` from inflected `*tehuni-`.
- **Useful background:** `DEV_NOTES` `§17.48` as the implementation dossier for the contraction fix; the packet’s summary of the contraction environment; and the generated debug snapshot entry that shows the row now outputs `tēon`.
- **Stale or superseded:** the older `DEV_NOTES` note at lines 2647-2662 treating `*texun -> tīen` as the expected target before the later retargeting; and the `§17.48` implementation checklist language about “TSV row 1210”, which is historical project chronology rather than the live row-ID framing.
- **Irrelevant or misleading if over-weighted:** `old_english_wiktionary.tsv` if its dictionary headword `tīen` is taken as the row’s governing target; and Orel/Kroonen-style cognate-set headword citations if they are mistaken for direct authority on the exact OE simplex target form.

## Additional repo research
Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at the older January 2026 `*-un` note, the project-status note at lines 1441-1467, and the full `§17.48` / `§17.48.1` dossier.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/data/oe_known_problems.tsv` (no live entry for this row).
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.md`.
- Repo-local reference extracts in `docs/references/`: Brunner (lines 5991-6008, 9799, 13271-13273, 28694-28697), Campbell (18870), Fulk (14357-14370), Ringe-Taylor (14642-14644), Orel (44735-44737), and Hirt (16842).

Main findings from that wider check:

- The strongest current repo-local evidence is not just “`tēon` exists”, but that the sources distinguish two different historical bases: bare `*tehun` versus inflected `*tehuni-`.
- Fulk and Ringe-Taylor explicitly connect OE `tien` to i-stem-inflected material, not to the bare cardinal alone.
- Campbell and Brunner list the attested simplex cardinal outputs as `tien/tȳn`, `tēn`, `tēo`, `tēa`; the exact simplex citation form `tēon` is much less directly attested than the row’s current wording might suggest.
- Brunner’s contraction discussion and the ordinal/compound evidence (`tēoða`, `-tēontig`, `hundteóntig`) strongly support an un-umlauted `tēon-` stem, even where the simplex numeral is later levelled or smoothed.
- No separate full dossier file named in the packet or TSV note appears to exist beyond the `DEV_NOTES` sections themselves.

## Reconstruction and early-stage forms
This row still needs a three-way distinction, even though the live TSV currently has the same string in `PROTO` and `PROTOFORM`.

1. **Cognate-set proto:** `*téxun` in the repo’s phonological notation, i.e. PGmc `*tehun`.
2. **Project input form for OE derivation:** also `*téxun` / `*tehun` for the current row, because the project is modelling the bare cardinal’s regular phonological development.
3. **Alternative inflectional source in the handbook tradition:** `*tehuni-` / `*teohuni-`, which explains the umlauted WS-type forms `tien/tīen`; this is relevant background, but it is not the same thing as the row’s chosen derivational input.
4. **OE target form represented by the row:** currently `tēon`, understood as the regular un-umlauted outcome of bare `*tehun`.

So the crucial distinction is not between two different live TSV proto strings, but between the bare-cardinal proto behind regular `tēon` and the inflectionally levelled i-stem material behind `tien/tīen`.

## Old English philology
The philological situation is narrower than the current `attested_variant` label suggests.

- **Attested simplex forms:** repo-local handbooks and lexical tables support WS `tien/tȳn`, Kentish/Mercian `tēn`, and Northumbrian `tēo/tēa`.
- **Direct attestation of exact simplex `tēon`:** weak at best in the repo-local evidence. Brunner uses `tēon` as the normalized regular outcome of `*tehun`, but the attestation tables and Campbell’s summary point instead to `tēn`, `tēo`, `tēa`, and WS `tien`.
- **Derivative/compound support for the un-umlauted stem:** strong. `tēoða` and `-tēontig` / `hundteóntig` show that an un-umlauted `tēon-` stem is real and productive in Old English, even if the simplex cardinal was often levelled or smoothed in transmitted forms.
- **Dictionary/headword issue:** `old_english_wiktionary.tsv` still gives `tīen`, so the repo’s dictionary-style lexical support does not by itself justify treating exact simplex `tēon` as the ordinary attested headword.

The upshot is that `tēon` is philologically well-motivated, but it behaves more like an inferred regular simplex form than like a straightforward directly attested citation-form variant.

## Project problem and solution
The original project problem had two layers:

1. a real FST gap (`*éo + *o` contraction was missing, so the model stalled at `teoon/teoun`-type outputs); and
2. a target-selection issue (`tīen` is a real OE form, but it reflects inflectional levelling rather than the bare cardinal’s regular phonological outcome).

The repo has already solved the first problem correctly: the cascade now derives `tēon`, and `§17.48.1` makes a strong case that this is the regular bare-cardinal outcome.

The remaining problem is classificatory. The row currently behaves like a **reconstructed or normalized regular OE target**, not like a simple attested-variant pick from directly attested simplex spellings. If the project wants the regular bare-cardinal outcome, keeping `COUNTERPART = tēon` is sensible; but then the row should probably not continue to advertise itself as `attested_variant`.

## Paradigm probe
No new paradigm probe is required for the current recommendation. The decisive issue is already established by the repo-local source dossier: the contrast is between the bare cardinal and the inflectionally levelled i-stem forms, not an unresolved FST paradigm-cell uncertainty that needs a fresh probe table.

If the project later reopens this as an attested-variant row instead of a reconstructed/normalized one, the cells worth probing would be: the uninflected simplex cardinal, the i-stem-inflected forms behind `tiene/tȳne`-type material, the ordinal `tēoða/teogeða`, the compound stem `-tēontig`, and the late Northumbrian `tēo/tēa` continuations. But that probe is not necessary for the present memo recommendation.

## Recommended final report
Recommend a concise final report that says the row models the **regular bare-cardinal outcome** of PGmc `*tehun` as OE `tēon`, while explaining that the directly attested simplex numeral is more often `tīen/tēn/tēo/tēa` and that the strongest support for un-umlauted `tēon-` comes from `tēoða` and `-tēontig`.

## Data-change recommendations
- **TSV `PROTO`:** no change recommended; `*téxun` is acceptable as the cognate-set proto in repo notation.
- **TSV `PROTOFORM`:** no change recommended; the project input for the current regular-outcome analysis can remain `*téxun`.
- **TSV `COUNTERPART`:** no change recommended if the project keeps the regular-outcome target; keep `tēon`.
- **TSV `DERIVATION_CLASS`:** change recommended from `attested_variant` to `reconstructed_oe`, because the live row now targets an inferred/normalized regular simplex form rather than a clearly directly attested simplex variant.
- **TSV `NOTE`:** change recommended. The note should explicitly say that exact simplex `tēon` is the project’s regularized target inferred from the bare-cardinal development and supported by `tēoða` / `-tēontig`, while the ordinary attested simplex forms are `tīen`, `tēn`, `tēo`, `tēa`.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** light cleanup recommended in `DEV_NOTES` only. The January 2026 `expected tīen` note should be marked as superseded by `§17.48` / `§17.48.1`, and the historical “TSV row 1210” implementation wording should be understood as old project chronology, not the present row-ID framing. No separate dossier file needs cleanup because none was found beyond the `DEV_NOTES` sections.
