# Supplementary SC047 cell assay

Run in the existing healthy Germanic backend from the repository root:

```sh
docker compose exec -T backend python3 /usr/app/docs/sound_changes/literature_dossiers/sc047_paired_chronologies/comparative_followup/run_cells.py
```

The [receipt](cell-probes.json) (SHA-256 `0027866fa2bc47dcc1a8fb83813ca688e19ba8f9888accb828e382fd35f9ed8e`) records the finite input lists, source digests, and selected checkpoints from one isolated definition image. A/B use the unmodified [`run_parallel.py`](run_parallel.py) recipe and stage order. Identity uses the canonical order. This is not a corpus rerun or admission change. The operation was run only in the backend, with no new CI workload. Eight of the nine full inputs were admitted (including two frozen controls); the PGmc dative `rástōi` was rejected in all arms. `[]` is no output, not a segment zero.

- **Feminine hedge:** `xágjō` and `xágjǭ` both double `*g` at SC010 with the long vowel still present and give `heġġ` and `heġġe` in identity, A and B. Compare the frozen masculine `xágjaz → heġe` in both research arms.
- **Rest:** In identity, `rástōz` retains `*z` through SC019 and gives `ræste`. In A and B its pre-SC019 output after ordinary final `*z` deletion is `*r*á*s*t*ō`; SC019 raises the exposed `*ō` to `*u` and the output is `rast`. The nominative `rástō` raises even in identity. The long nasal accusative `rástǭ` is untouched by that raising and gives `ræste` everywhere. Independently, an existing-bin lookup with later-stage `rástē` is admitted and gives `ræste` in canonical identity; it neither runs the PGmc dative nor demonstrates the intervening monophthongization.
- **Protected labials:** `xáwjai` and `xíwjai` give `hīeġe` and `hīewe` in all three orders. These are predictions from protected dative inputs, not new attestations.

The four component inputs begin at the output of `EnglishProtoInput`, leaving all subsequent stages unchanged. The two fixed conditional *hyse* strings test Dahl's proposed masculine ja-stem, not a productive override or an established inherited class. Both A/B give nominative `hyse` and dative `hysse`; the former follows shared oral vocalization, the latter geminates while `*ē` protects `*j`. Identity gives `hyss/hysse`, as its oral loss is later. The two positive controls use already admitted representations: net gives the same values with and without the gate at every recorded downstream checkpoint, and *hyse* accusative gives frozen `hyse/hyss` (identity `hyss`). These component results do not replace the original gate rejects for nominative and dative *hyse*. *Here* is a well-supported reconstruction with an independently exempt *r*, and the *yellow* s-bearing control is not a secure PGmc adjectival genitive; neither was bypassed.
