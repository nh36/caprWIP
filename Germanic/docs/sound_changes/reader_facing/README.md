# Reader-facing sound-change pilot

This directory is a **new book-facing layer** for the sound-change half. The
existing reports, dossiers, chronology cards, and FOMA definitions remain the
source material; the files here test how that material can be rewritten for a
historical-linguistic reader who does not need the internal workflow.

The present pilot contains three deliberately different cases:

1. `052-velar-palatalization.md` — a major consonantal change with rich
   scholarship and clear local chronology.
2. `055-056-i-umlaut-core.md` — a grouped chapter with one major central change
   and one narrower right-edge follower.
3. `058-nasal-dissimilation.md` — a residual change with thin source support and
   boundary-limited chronology.

An expanded local batch now also exists for a separate pilot-02 build:

1. `049-050-b-allophony-and-sievers-law-syncope.md`
2. `051-sk-palatalization.md`
3. `053-054-pre-umlaut-bridge-and-w-loss.md`
4. `057-j-cluster-coalescence.md`

## Current scope

These files do **not** replace the existing sound-change reports. They are a
controlled pilot for tone, structure, quotation practice, code presentation,
and chronology explanation.

## Pilot PDF build

To assemble the three pilot chapters into one reviewable PDF, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_pilot_docker.sh
```

This writes:

- `reader_facing_pilot_01.md`
- `reader_facing_pilot_01.pdf`

To build the expanded batch without altering the original pilot target, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_pilot_02_docker.sh
```

This writes:

- `reader_facing_pilot_02.md`
- `reader_facing_pilot_02.pdf`

To build the ordered seven-chapter local section without altering the preserved
pilot outputs, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_01_docker.sh
```

This writes:

- `reader_facing_local_section_01.md`
- `reader_facing_local_section_01.pdf`

To extend that ordered section rightward through back mutation and the two short
weak-tail notes, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_02_docker.sh
```

This writes:

- `reader_facing_local_section_02.md`
- `reader_facing_local_section_02.pdf`

To extend the same ordered section through high-vowel apocope and the next late
weak-tail batch, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_03_docker.sh
```

This writes:

- `reader_facing_local_section_03.md`
- `reader_facing_local_section_03.pdf`

To extend that ordered section through unstressed long-vowel shortening and the
unstressed ae-merger core, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_04_docker.sh
```

This writes:

- `reader_facing_local_section_04.md`
- `reader_facing_local_section_04.pdf`

To extend the same ordered section through medial unstressed-i lowering,
prefix-vowel reduction, and weak-tail reduction, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_05_docker.sh
```

This writes:

- `reader_facing_local_section_05.md`
- `reader_facing_local_section_05.pdf`

To extend the same ordered section through final-j loss, contraction, and
r-metathesis, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_06_docker.sh
```

This writes:

- `reader_facing_local_section_06.md`
- `reader_facing_local_section_06.pdf`

To extend the same ordered section leftward through surviving bimoric
o-unrounding, Anglo-Frisian brightening, breaking, and restoration, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_07_docker.sh
```

This writes:

- `reader_facing_local_section_07.md`
- `reader_facing_local_section_07.pdf`

To extend the same ordered section further leftward through prefix and
compound adjustments, medial unstressed vowel changes, and final bare-a
loss, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_08_docker.sh
```

This writes:

- `reader_facing_local_section_08.md`
- `reader_facing_local_section_08.pdf`

To extend the same ordered section further leftward through the West Saxon
diphthong sequence, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_09_docker.sh
```

This writes:

- `reader_facing_local_section_09.md`
- `reader_facing_local_section_09.pdf`

To extend the same ordered section further leftward through preconsonantal
x-loss, awj glide formation, and au-fronting, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_10_docker.sh
```

This writes:

- `reader_facing_local_section_10.md`
- `reader_facing_local_section_10.pdf`

## Style audit workflow

After drafting or revising any reader-facing chapter, run:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py
```

Inspect the warnings manually. If the pilot PDF is being rebuilt, run the
checker before:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_pilot_docker.sh
```

## Numbering note

The current sound-change assembly wrappers do **not** request numbered section
headings. `Germanic/docs/assembly/build_sound_change_volume.sh` passes Markdown
through Pandoc, but it does not add `--number-sections`, and
`full_volume_metadata.yaml` does not currently override that. A later
reader-facing assembly should enable numbering there rather than hard-coding
numbers in prose.
