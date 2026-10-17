# SC015 follow-up experiment receipt summary

The complete deterministic receipt is
`followup-receipt.json.gz`. It is the byte-preserving gzip compression of
the previously committed `followup-receipt.json`; decompression reproduces
the original JSON bytes exactly. The compressed receipt records all 389 row
traces, all three recipes, intermediate censuses, candidate results,
protected-row deltas, source pins and receipt metadata.

| Placement | Result | Candidate outputs | Original-row final deltas |
| --- | --- | --- | --- |
| Early, before `EAFRhotacism` | 381/389 exact; 8 historical mismatches | `*θár → þǣr`; `*xwár → hwǣr` | none |
| Intermediate, before short-*a* brightening | 379/389 exact; 10 mismatches | `*θár → þār`; `*xwár → hwār` | none |
| Late, after short-*a* brightening | 380/389 exact; 9 mismatches | `*θár → þǣr`; `*xwár → hwǣr` | row 1992 *door*: `dor → dōr` |

The early architecture is therefore the selected working model. This
experiment does not establish a strict historical date or an SC015/SC024
chronology edge.

Receipt integrity:

- uncompressed JSON SHA-256:
  `059993fe139d03b5cdd1475e0a22e29f79844020201db959055f15a3300ac252`
- compressed receipt SHA-256:
  `1c10e6908f8aa309693e9c7c6b9ccf859aa7ce5ab40cb6ed5617b15f262b760c`
- uncompressed size: 36,739,197 bytes
- compressed size: 1,034,466 bytes
