# Reviewer checklist result — 2027 follow / fylġan

**Overall result:** pass, with minor human-review points noted at the end.

## Genre and scope

| Item | Result | Note |
| :--- | :--- | :--- |
| Does the entry read like a book entry about the word? | yes | The prose centers on the lexical and class history of `follow`, not on repository process. |
| Does it avoid project autobiography? | yes | Local files are confined to the ledger and implementation report. |
| Is the prose about linguistic history rather than repository history? | yes | The entry discusses reconstruction, OE evidence, development, and class choice. |
| Is the entry as short as the case permits, rather than inflated to match a harder entry? | yes | It is shorter than shoulder and no longer than needed for the class split. |

## Evidence and forms

| Item | Result | Note |
| :--- | :--- | :--- |
| Does the entry give actual source forms? | yes | It names `*fulgen-`, `*fulgjan-`, `*fulgija- ~ *fulgai-`, `folgian`, `fylgan`, and `fylgean`. |
| Does it avoid vague statements such as “the handbooks disagree” unless the forms are immediately named? | yes | The class split is stated with concrete forms and authors. |
| Does it distinguish attested, normalized, reconstructed, and project-selected forms? | yes | `folgian` and `fylgan/fylgean` are treated as source forms, `fylġan` as normalized comparison form, and `*fulgēną` / `*fúlgijaną` as distinct inherited inputs. |
| Does it establish the Old English evidence before the paradigm comparison? | yes | The OE evidence section precedes the `Class comparison` section. |
| If an OE target is reconstructed, is that stated explicitly? | n/a | `fylġan` is a normalized spelling of attested class-I forms, not a wholly reconstructed OE form. |

## Citations

| Item | Result | Note |
| :--- | :--- | :--- |
| Do all citations use bibliography keys present in `docs/refs.bib`? | yes | `BosworthToller1898`, `BrightCassidyRingler1971`, `ClarkHall1960`, `Kroonen2013`, and `RingeTaylor2014` were checked. |
| Are sources cited in prose rather than hidden behind local file names? | yes | The model entry cites named sources only. |
| If a cited source lacks a key, is that problem recorded in the ledger or implementation report rather than silently patched over? | yes | The local trace and analysis-only evidence remain confined to the supporting files. |

## Claims and certainty

| Item | Result | Note |
| :--- | :--- | :--- |
| Does the entry distinguish documented outputs from inferred/expected outputs? | yes | The comparison table distinguishes the compact-trace output `fylġan`, the local-probe mismatch `folgon`, and Ringe-Taylor's documented `folgian` branch. |
| If a comparison is manual, is it labeled as manual? | yes | The class-comparison introduction states this explicitly. |
| Does the entry avoid overstating certainty? | yes | It avoids making a stronger dialect claim than the sources require. |
| Does it avoid inventing unattested forms or automatic probe results? | yes | No unattested OE form or unrun automatic class probe is claimed. |

## Style

| Item | Result | Note |
| :--- | :--- | :--- |
| Does it avoid repetitive “not X but Y” rhetorical negation? | yes | The prose uses direct positive statements. |
| Does it avoid generic summary endings? | yes | There is no conclusion section. |
| Does it avoid a conclusion unless there is a strong reason to include one? | yes | The entry ends with `Class comparison`. |
| Does it avoid unnecessary project-facing terms after the brief metadata section? | yes | The entry stays in historical-linguistic prose after the metadata table. |

## Forbidden project-facing content in the book-style prose

| Item | Result | Note |
| :--- | :--- | :--- |
| Does it avoid mentioning packets, DEV_NOTES, backlog, manifest, implementation log, or project history in the final entry prose? | yes | Those appear only in the supporting files. |
| Are local tools discussed only in the ledger and implementation report? | yes | The final entry does not narrate them. |

## Process record

| Item | Result | Note |
| :--- | :--- | :--- |
| Does the implementation report state what was checked? | yes | Files inspected, citation checks, and the manual class comparison are recorded. |
| Does the implementation report state what was not checked, when relevant? | yes | It states that no automatic class probe was run and notes unresolved uncertainties. |
| Does the implementation report confirm that no TSV, FST, manifest, packet, memo, bibliography, derivation trace, or pilot report was changed? | yes | Scope confirmation is explicit. |

## Cleanup note

- Post-audit cleanup pass 01 recast the flagged formulaic final-prose wording in
  the paired model entry without changing the analysis, citations, selected
  input, target form, classification, or comparison tables.

## Remaining human-review points

1. The strongest evidence supports the class split more securely than a narrow
   dialect label, so the draft keeps the OE evidence at the level of class-I
   versus class-II forms rather than making a stronger Mercian/Northumbrian
   claim.
2. The normalized `<ġ>` in `fylġan` reflects project orthographic practice; the
   source forms themselves appear mainly as `fylgan` and `fylgean`.
