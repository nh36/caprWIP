# Assembly pilot 03 report

## Summary

- Pilot entries assembled: **8**
- Entries with trace blocks injected: **8**
- Entries without trace blocks: **0**
- Duplicate metadata removed: **yes**
- Linguistic forms converted away from code font: **yes, in assembled prose and compact metadata**
- PDF generation succeeded: **yes**
- Original model entries edited: **no**

## Trace-source matching

| Model entry file | Matched compact trace entry | Match basis | Confident |
| :--- | :--- | :--- | :--- |
| `1934-bake-bacan.model.md` | `bake` (`PROTO: *bákaną`, `EXPECTED/OUTPUTS: bacan`) | lexical item + `PROTOFORM` + `PROTO` + `EXPECTED` + `OUTPUTS` | yes |
| `1962-bow-bēag.model.md` | `bow` (`PROTO: *báug`, `EXPECTED/OUTPUTS: bēag`) | lexical item + `PROTOFORM` + `EXPECTED` + `OUTPUTS` | yes |
| `1981-craft-cræft.model.md` | `craft` (`PROTO: *kráftaz`, `EXPECTED/OUTPUTS: cræft`) | lexical item + `PROTOFORM` + `EXPECTED` + `OUTPUTS` | yes |
| `2030-fowl-fugol.model.md` | `fowl` (`PROTO: *fúglaz`, `EXPECTED: fugol`, `OUTPUTS: fogol`) | lexical item + `PROTOFORM` + `PROTO` + `EXPECTED` | yes |
| `2250-thistle-þistles.model.md` | `thistle` (`PROTO: *θístilas`, `EXPECTED/OUTPUTS: þistles`) | lexical item + `PROTOFORM` + `EXPECTED` + `OUTPUTS` | yes |
| `2278-weapon-wǣpn.model.md` | `weapon` (`PROTO: *wḗpną`, `EXPECTED/OUTPUTS: wǣpn`) | lexical item + `PROTOFORM` + `PROTO` + `EXPECTED` + `OUTPUTS` | yes |
| `2293-will-willa.model.md` | `will` (`PROTO: *wéljô`, `EXPECTED/OUTPUTS: willa`) | lexical item + `PROTOFORM` + `PROTO` + `EXPECTED` + `OUTPUTS` | yes |
| `2308-youth-ġeoguþ.model.md` | `youth` (`PROTO: *júgunθ`, `EXPECTED/OUTPUTS: ġeoguþ`) | lexical item + `PROTOFORM` + `EXPECTED` + `OUTPUTS` | yes |

## Document-structure changes

Each entry now begins with one compact metadata table, followed immediately by `### Derivation trace`, `Proto input`, the two-column trace table, and `Outcome` or the `Transducer outcome` / `Selected target` split where needed.

The earlier duplicated metadata presentations were removed: the assembled document no longer includes both the `Field / Value` block and the separate `Transducer input and output` table. The original model-entry prose sections remain in their existing order after the trace block, aside from skipping the source `### Transducer input and output` section in the assembled copy.

## Typography changes

Inline linguistic code spans are now rewritten in the assembly generator as italics in the assembled output, including reconstructed forms, Old English forms, and short comparative examples. This change is applied only in the assembled copy; the source model-entry Markdown files remain untouched.

Random bold around isolated forms was demoted in the assembled prose, while structural bold was retained inside the trace tables for stage labels such as `Proto-West Germanic`, `Northwest Germanic`, and `Old English`. Actual file references such as `.model.md`, `pilot_manifest.tsv`, and `oe_derivation_class_trace_report.compact.md` remain in code font.

## PDF inspection

- Trace tables render acceptably: **yes, for pilot purposes**
- Old English and reconstructed forms appear in italics: **yes in metadata and prose**
- Citations and bibliography still render: **yes**
- Unicode remains correct: **yes**

Inspection notes:

1. `pilot_assembled.pdf` was regenerated successfully through the Docker-backed Pandoc/XeLaTeX path using `Noto Serif` and `Noto Sans Mono`.
2. The trace tables are now readable in PDF form because the collapsed intra-cell line-break problem was replaced with stage-labelled two-column summaries.
3. The `fowl / fugol` entry correctly distinguishes `Transducer outcome: fogol` from `Selected target: fugol`.
4. The document still uses the same `--citeproc` immediate-rendering path validated in pilot 02, and citations plus bibliography remained intact.

## Remaining issues

- The trace tables are still fairly dense in entries with long Old English-stage histories; they are readable, but a later style pass could refine spacing or column proportions.
- Some manual comparison tables remain visually busy; that is acceptable for the pilot but not yet final publication typography.
- The host still lacks local `pandoc` and local Unicode-capable LaTeX engines, so PDF generation still depends on the Docker wrapper on this machine.

## Recommendation

**Decision: B. Pilot is close, but needs one more visual/style pass.**

Reasoning:

1. The target structure is now back in place: compact metadata, derivation trace near the top, and unmodified philological prose below it.
2. The typography regression from code-font linguistic forms has been fixed in the assembled copy.
3. The PDF is readable and technically sound, but the trace tables and comparison tables are still dense enough that one more visual cleanup pass is worth doing before scaling to full-corpus assembly alpha.

## Scope confirmation

- No original model entries were changed.
- No TSV source data, FST files, manifest files, packets, dev-note slices, research memos, bibliography files, OCR/reference files, or citation-locator reports were edited.
- Changes were limited to `Germanic/docs/assembly/build_pilot.sh`, regenerated pilot outputs (`pilot_assembled.md`, `pilot_assembled.tex`, `pilot_assembled.pdf`), and this report.
