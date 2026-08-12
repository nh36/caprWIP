# Candidate probe: row 2216 i-stem derivation

## Commands
```bash
docker compose run --rm --no-deps --entrypoint sh backend -lc 'cd /usr/app && foma -q -l fsts/germanic.txt -e quit'
docker compose run --rm --no-deps --entrypoint sh backend -lc 'cd /usr/app && foma -f fsts/old_english_sandbox.txt'
docker compose run --rm --no-deps --entrypoint sh backend -lc 'cd /usr/app && PYTHONPATH=/usr/app/tools python3 <probe-snippet>'
```

## Probe results
| Input | Accepted | Outputs | Multiplicity | Note |
| --- | --- | --- | --- | --- |
| `*stámnaz` | yes | `stamn` | 1 | current live mismatch |
| `*stámniz` | yes | `stemn` | 1 | hypothesis target hit |
| `*stamni` | yes | `stemn` | 1 | raw candidate probe only |

## Changed-stage traces
- `*stámnaz -> EAF Final Z Deletion *stámna -> PWGmc Final Bare A Loss *stámn -> Outcome stamn`.
- `*stámniz -> EAF Final Z Deletion *stámni -> OE I Umlaut *stemni -> OE High Vowel Apocope *stemn -> Outcome stemn`.

## Controls
- Ordinary i-mutation: `*strángiz -> strenġ` via `EAFFinalZDeletion -> OEVelarPalatalization -> OEIUmlaut -> OEHighVowelApocope`.
- Final high-vowel loss: `*wúrmiz -> wyrm` via `EAFFinalZDeletion -> OEIUmlaut -> OEHighVowelApocope`.
- Live sieve relevance: row 2189 uses `PROTOFORM = *síbi`; it yields `sife` by `PGmcBAllophony -> OEMedUnstressedILowering1`, so not every final `-i` path apocopates.

No FST source changed; the successful candidate path is entirely within the unchanged cascade.
