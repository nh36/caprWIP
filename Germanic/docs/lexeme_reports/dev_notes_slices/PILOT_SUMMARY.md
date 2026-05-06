# DEV_NOTES slicing pilot summary

## Scope

Created **10** lexical-item files for these rows:

- 1959 `bottom / botm`
- 1992 `door / dor`
- 2030 `fowl / fugol`
- 2068 `heaven / heofon`
- 2126 `milk / meoloc`
- 2139 `nettle / netle`
- 2162 `rust / rust`
- 2288 `widow / wuduwe`
- 2298 `wolf / wulf`
- 2300 `wool / wull`

## Filename reuse

Reused existing packet or research-memo stems for:

- `1959-bottom-botm`
- `1992-door-dor`
- `2030-fowl-fugol`
- `2068-heaven-heofon`
- `2126-milk-meoloc`
- `2162-rust-rust`
- `2298-wolf-wulf`
- `2300-wool-wull`

Used canonical new stems for:

- `2139-nettle-netle`
- `2288-widow-wuduwe`

## Fragments copied into more than one lexical item file

- `DEV_NOTES:line-63-166` copied into `2030`, `2162`, `2298`, `2300`
- `DEV_NOTES:section-17.10.34-25940-26067` or its row-specific subranges reused across `2030`, `2162`, `2298`, `2300`

## Material that attached cleanly

The easiest material to attach was:

- lexeme-specific mismatch sections with explicit recommendations (`door`, `bottom`, `milk`, `nettle`, `heaven`);
- later closure sections that clearly state current row policy (`widow`);
- row notes whose current TSV state still matches the DEV_NOTES diagnosis (`wool`).

## Material deferred as sound-change or chronology work

The most obviously non-lexeme-first material was:

- broad `u`-lowering exception surveys;
- the general Campbell §373 / medial-`u` architecture discussion;
- sound-change split notes distinguishing different `*u > o` processes;
- syncope rule overviews that precede the milk/nettle-specific discussion.

These are parked in `deferred_sound_change_material.md`.

## Clearly superseded chunks

The clearest superseded project-history material in the pilot is:

- the abandoned paradigm-cell retargeting proposals for `fugol`, `wulf`, and `rust`;
- the `rust -> orst` metathesis-debugging episode as a temporary intermediate bug state;
- the earlier widow canvass once §17.51.A1.3-A1.4 closes the question more cleanly.

## Later external literature / dossier dependence

No row in this pilot was flagged as immediately needing a new external-literature dossier before further slicing work continues. The rows with the heaviest existing dossier dependence are:

- `2288 widow / wuduwe`
- `2068 heaven / heofon`
- `2030 fowl / fugol`
- `2162 rust / rust`
- `2298 wolf / wulf`
- `2300 wool / wull`

## Later consultation needs

Before final reports, the following rows should definitely be checked back against the existing packet / memo / dossier layer:

- `2030`, `2162`, `2298`, `2300` for exception framing and abandoned paradigm-cell ideas;
- `2288` for the final widow closure versus the earlier mixed March notes;
- `2068` for the march from `*xemenăz` to the current oblique-form input;
- `1959` and `1992` for the project principle behind cell-specific or etymological targeting.

## Index-column assessment

The current index columns are workable for the broader pass. The only likely pressure point is `date_or_section`, which may become partly redundant once more fragments are section-based rather than date-based, but there is no immediate need to change the schema before continuing.
