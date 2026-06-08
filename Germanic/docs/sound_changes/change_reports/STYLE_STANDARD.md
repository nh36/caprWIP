# Sound-change report style standard

This file records the **actual production pattern** established by the current
pilot/full sound-change reports. It is the standard for manifest-backed reports
under `change_reports/pilot/` and `change_reports/full/`.

## Pilot models

Use these reports as the reference set for section order and report shape:

- `pilot/016-020-early-vocalic-final-corridor.md` — strong multi-change corridor
- `full/014-015-opening-vowel-prelude.md` — asymmetric opening bridge
- `full/018-stressed-monosyllable-o-raising-note.md` — boundary-limited singleton
- `full/035-037-prefix-and-compound-adjustments.md` — grouped report with one clear center and two flanks
- `full/058-oe-nasal-dissimilation-residual-note.md` — short chronology-negative residual note
- `full/069-early-o-shortening-context-note.md` — broad/far opener/context note
- `full/081-083-j-strengthening-vocalization-and-ei-contraction-bridge.md` — technical middle bridge with a stronger center

## Required source structure

Every production report uses this source-Markdown skeleton:

```md
# <unit title>

### Sound-change report

#### Historical formulation
#### Source tradition
#### CAPR implementation
#### Place in the cascade
#### Order evidence
#### Interpretation
#### Remaining cautions
```

The sequence is fixed. Do not rename, omit, or duplicate these headings.

## Section functions

| Section | Required job | Keep out |
| --- | --- | --- |
| `Historical formulation` | State the historical phenomenon, the unit shape, and the internal hierarchy if the unit is grouped. | Workflow history, manifest status, promotion language. |
| `Source tradition` | State what the grammars, handbooks, or other sources actually support, with page-numbered citations and concrete forms. | Exact CAPR rule names unless a source itself uses them. |
| `CAPR implementation` | Name the exact modeled rule or rules and explain how CAPR segments or sharpens the source-backed phenomenon. | Repository/process autobiography. |
| `Place in the cascade` | Show the local cascade neighborhood and the immediately relevant neighboring reports. | Non-local chapter-building language. |
| `Order evidence` | State which boundaries are real, broad/far, runner-bounded, boundary-limited, technical-marker only, or negative. | Overclaiming beyond the card evidence. |
| `Interpretation` | Say what kind of report this is in the book: core, bridge, flank-led group, residual note, opener, hinge. | Internal process narration or “why we promoted it.” |
| `Remaining cautions` | Preserve the limits: outward links that stay cross-references, runner bounds, weak members, residual uncertainty. | Generic conclusions or recap language. |

## Source tradition vs. CAPR implementation

- **Source tradition** is about the historical phenomenon as the sources describe
  it: named developments, handbook formulations, philological examples, and
  comparative placement.
- **CAPR implementation** is where exact modeled stage names belong. This is the
  only section that should foreground identifiers such as
  `OEVelarPalatalization` or `NWGmcFinalLongORaising`.
- If the sources support a broader phenomenon than CAPR's exact segmentation,
  say so directly: the report should distinguish the historical development from
  the tighter modeled rule.

## Order-evidence language

- **Strong local evidence**: use for genuinely adjacent or reciprocal seams.
- **Broad/far**: use when the boundary is real but non-local. Keep it as a
  cross-reference, not a larger chapter claim.
- **Boundary-limited / negative**: say that the search reaches the relevant
  boundary with no real break. Do not convert that into positive chronology.
- **Runner-bounded**: say explicitly that the search stops at a methodological
  runner limit such as bundled `PWGmcChanges` or the current right-edge search
  boundary. Do not rewrite the limit as a historical anchor.
- **Technical-marker only**: if the only break crosses a technical stage, say so
  plainly and do not present it as ordinary chronology.

For weak or bounded cases, the prose should say **what the card does show** and
**what it does not show**.

## Grouped reports

- Name the internal hierarchy in `Historical formulation` and keep it visible in
  `Interpretation`.
- If one member carries the argument and another is only a flank, prelude,
  bridge member, follower, or residual technical companion, say that directly.
- Do not flatten grouped reports into coequal chapter heads when the evidence is
  asymmetric.
- Do not split or merge units in the prose unless there is a real structural
  reason beyond presentation taste.

## Cross-reference rule

- Outward links stay **cross-references**, not larger chapter claims.
- Phrase them as earlier/later comparisons or leftward/rightward relations, not
  as repository architecture.
- Prefer formulations such as “the later comparison remains a cross-reference
  only” or “the outward relation should not expand the report.”
- Avoid project-facing phrasing such as `promoted`, `production report`,
  `assembled half`, `pilot corridor`, `chapter architecture`, `book
  architecture`, `finished prose`, or similar lifecycle language in the body
  prose.

## Typographic conventions

| Item | Source-Markdown convention | Assembled/book expectation |
| --- | --- | --- |
| Change IDs and exact order relations | Use code spans for exact identifiers and relations when they function as identifiers: ``SC052``, ``SC050 < SC052 < SC055``. | Keep them visually distinct from ordinary prose. |
| Exact CAPR/FOMA rule names | Use code spans: ``OEVelarPalatalization``. | Keep exact rule labels distinct from ordinary historical names. |
| Historical phenomenon names | Write in ordinary prose, not as raw FOMA labels. | Read like historical-linguistic prose. |
| Linguistic forms in report source | Use inline code spans for linguistic forms during authoring when needed; keep each form compact and readable. | The volume build should render linguistic forms as reader-facing linguistic text rather than repository/code syntax. |
| Reconstructed forms | Keep the leading `*` visible. | Preserve the visible reconstruction marker in book output. |
| Old English forms | Treat as linguistic forms, not file/code identifiers. | They should read as ordinary linguistic examples in the built volume. |
| Raw FOMA syntax | Only inside fenced ````foma```` blocks. | Never leak raw rewrite syntax into ordinary prose. |
| Citations | Use Pandoc citations from `docs/refs.bib`, with page/section references where available: `[@Campbell1959, §170]`. | Stay source-facing and page-specific. |

## Negative rules

- Do not narrate repository workflow inside the body prose.
- Do not talk about a report being “promoted,” “scaffolded,” “book-facing,” or
  “reader-facing” inside the report itself.
- Do not let outward broad/far links create non-contiguous chapters.
- Do not let runner-bounded or boundary-limited results turn into “must precede
  the rest of the half” claims.
- Do not put raw `->`, `||`, `.o.`, `define`, or similar FOMA syntax in prose
  paragraphs.

## Check command

Run:

```bash
python3 Germanic/tools/audit_sound_change_report_style.py
```

The audit writes:

```text
Germanic/docs/sound_changes/change_reports/sound_change_style_audit.md
```
