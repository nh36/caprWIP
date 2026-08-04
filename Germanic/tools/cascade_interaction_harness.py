#!/usr/bin/env python3
"""Cross-stage rule-interaction harness for the historical-cascade-order project.

Phase 5 machinery. Lexical equivalence (Phase 4) proves two orders agree on the
current lexicon; it does not prove they agree over the whole admitted input
language. This harness answers the stronger, formal question for a pair of rules
by composing them with ``EnglishProtoInput`` (which restricts the domain to the
admitted proto input language) in both orders and asking foma whether the two
transducers are equivalent:

    T_forward  = EnglishProtoInput .o. EARLIER .o. LATER
    T_reversed = EnglishProtoInput .o. LATER   .o. EARLIER
    commute?   = ( T_forward == T_reversed )

``commute = yes`` means the pair may be reordered freely; ``no`` means the order
is load-bearing and must be justified by a demonstrated dependency (the
handover's feeding/bleeding/counterfeeding/... analysis).

The harness is *descriptive*: it reports commutation, it does not reorder
anything. Rule identity is taken from the caller (defaults derive the PNWGmc and
PWGmc rule sets from the sourced registry's curated ``hist_stage``, never from
FST name prefixes).

Implementation. Compiling ``germanic.txt`` once and running many ``test
equivalent`` calls in a single foma session segfaults foma (stack growth). So we
compile once, ``save defined`` the whole definition table to a reusable image,
then run one fresh foma process per pair (``load defined`` + one test). Because
it invokes ``foma``, this tool runs inside the backend container.
"""
from __future__ import annotations

import argparse
import csv
import io
import re
import subprocess
import sys
import tempfile
from pathlib import Path

_RESULT_RE = re.compile(r"^([01])\s*\(1 = TRUE, 0 = FALSE\)")


def _read_tsv_skip_comments(path: Path) -> list[dict[str, str]]:
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines() if not ln.startswith("#")]
    return list(csv.DictReader(io.StringIO("\n".join(lines)), delimiter="\t"))


def registry_rules_by_stage(staging_map: Path, order_manifest: Path, stage) -> list[str]:
    """Return pipeline Foma identifiers whose curated hist_stage is in ``stage``.

    ``stage`` may be a single stage string, a comma-separated list of stages, or
    an iterable of stages. Restricted to rules that appear in the executable-order
    manifest and returned in executable order. Stage comes from the sourced
    registry, not the FST name.

    Accepting a set of stages lets the PNWGmc relabelling migration run
    rule-by-rule: the 'earlier' set is queried as {nwgmc, pnwgmc} so a rule stays
    in the set whether it has been relabelled yet or not (and the still-unresolved
    SC064, kept at nwgmc, remains included).
    """
    if isinstance(stage, str):
        stages = {s.strip() for s in stage.split(",") if s.strip()}
    else:
        stages = set(stage)
    staging = {r["fst_identifier"]: r for r in _read_tsv_skip_comments(staging_map)}
    with order_manifest.open(encoding="utf-8") as handle:
        manifest = [r["foma_identifier"] for r in csv.DictReader(handle, delimiter="\t")]
    return [f for f in manifest if staging.get(f, {}).get("hist_stage") in stages]


def build_defs_image(fst_path: Path) -> Path:
    """Compile germanic.txt once and save the full definition table to an image."""
    image = Path(tempfile.mkstemp(suffix=".defs.bin")[1])
    script = f"source {fst_path}\nsave defined {image}\n"
    with tempfile.NamedTemporaryFile("w", suffix=".foma", delete=False, encoding="utf-8") as handle:
        script_path = Path(handle.name)
        handle.write(script)
    try:
        subprocess.run(["foma", "-q", "-f", str(script_path)],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    finally:
        script_path.unlink(missing_ok=True)
    if not image.exists() or image.stat().st_size == 0:
        raise RuntimeError(f"failed to build foma definition image from {fst_path}")
    return image


def test_pair(defs_image: Path, earlier: str, later: str) -> bool:
    """True iff EARLIER.o.LATER == LATER.o.EARLIER over the admitted input language."""
    script = (
        f"load defined {defs_image}\n"
        f"regex [ EnglishProtoInput .o. {earlier} .o. {later} ];\n"
        f"regex [ EnglishProtoInput .o. {later} .o. {earlier} ];\n"
        "test equivalent\n"
    )
    with tempfile.NamedTemporaryFile("w", suffix=".foma", delete=False, encoding="utf-8") as handle:
        script_path = Path(handle.name)
        handle.write(script)
    try:
        proc = subprocess.run(["foma", "-q", "-f", str(script_path)],
                              stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=True)
    finally:
        script_path.unlink(missing_ok=True)
    for line in proc.stdout.decode("utf-8", errors="replace").splitlines():
        m = _RESULT_RE.match(line.strip())
        if m:
            return m.group(1) == "1"
    raise RuntimeError(f"no equivalence result for pair ({earlier}, {later}); check identifiers")


def run_matrix(fst_path: Path, pairs: list[tuple[str, str]], *, progress: bool = False) -> list[dict[str, str]]:
    defs_image = build_defs_image(fst_path)
    try:
        rows: list[dict[str, str]] = []
        for i, (earlier, later) in enumerate(pairs, start=1):
            commute = test_pair(defs_image, earlier, later)
            rows.append({"earlier_rule": earlier, "later_rule": later,
                         "commute": "yes" if commute else "no"})
            if progress:
                print(f"[{i}/{len(pairs)}] {earlier} x {later} -> "
                      f"{'commute' if commute else 'NONCOMMUTE'}", file=sys.stderr)
    finally:
        defs_image.unlink(missing_ok=True)
    return rows


def write_matrix(rows: list[dict[str, str]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["earlier_rule\tlater_rule\tcommute"]
    for r in rows:
        lines.append(f"{r['earlier_rule']}\t{r['later_rule']}\t{r['commute']}")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fst", type=Path, default=Path("fsts/germanic.txt"))
    parser.add_argument("--staging-map", type=Path,
                        default=Path("docs/sound_changes/sound_change_historical_staging_map.tsv"))
    parser.add_argument("--order-manifest", type=Path,
                        default=Path("docs/sound_changes/cascade_baseline/cascade_order_manifest.tsv"))
    parser.add_argument("--earlier-stage", default="nwgmc,pnwgmc",
                        help="curated hist_stage(s) for the 'earlier' (Proto-Northwest Germanic) rule set; comma-separated")
    parser.add_argument("--later-stage", default="pwgmc",
                        help="curated hist_stage(s) for the 'later' (PWGmc) rule set; comma-separated")
    parser.add_argument("--pairs", nargs="*", default=None,
                        help="explicit EARLIER:LATER pairs, overriding the stage cross-product")
    parser.add_argument("--out", type=Path,
                        default=Path("docs/sound_changes/cascade_baseline/cascade_interaction_matrix.tsv"))
    parser.add_argument("--print", dest="print_only", action="store_true")
    parser.add_argument("--progress", action="store_true", help="print per-pair progress to stderr")
    args = parser.parse_args()

    if args.pairs:
        pairs = [tuple(spec.split(":", 1)) for spec in args.pairs]  # type: ignore[misc]
    else:
        earlier_rules = registry_rules_by_stage(args.staging_map, args.order_manifest, args.earlier_stage)
        later_rules = registry_rules_by_stage(args.staging_map, args.order_manifest, args.later_stage)
        pairs = [(e, l) for e in earlier_rules for l in later_rules]

    rows = run_matrix(args.fst, pairs, progress=args.progress)
    commute_yes = sum(1 for r in rows if r["commute"] == "yes")
    commute_no = sum(1 for r in rows if r["commute"] == "no")
    if args.print_only:
        for r in rows:
            print(f"{r['earlier_rule']}\t{r['later_rule']}\t{r['commute']}")
        print(f"# pairs={len(rows)} commute={commute_yes} noncommute={commute_no}")
    else:
        write_matrix(rows, args.out)
        print(f"wrote {args.out}: pairs={len(rows)} commute={commute_yes} noncommute={commute_no}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
