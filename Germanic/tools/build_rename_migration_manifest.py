#!/usr/bin/env python3
"""Machine-readable rename migration manifest for the canonical-ontology relabel.

Behaviour-neutral migration only. Each row pairs a rule's former identifier /
display / stage / scope with its canonical target under the CAPR stage+scope
ontology (PGmc -> PNWGmc -> PWGmc -> EAF -> OE for stage; a separate hist_scope
axis). Former fields are auto-loaded from the registry so they cannot drift; the
canonical targets are encoded in RENAMES below.

migration_status values: pending | completed | deferred | not_required
As each rule migrates, set its migration_status=completed and migration_commit
to the rule's commit SHA (via --set-completed, or by editing the tracked TSV).
"""
from __future__ import annotations

import argparse
import csv
import io
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
STAGING_MAP = SC_DIR / "sound_change_historical_staging_map.tsv"
DEFAULT_OUT = SC_DIR / "cascade_baseline/rename_migration_manifest.tsv"

# Canonical rename set (task section 3). Each entry:
#   canonical_foma_identifier, canonical_display_name, canonical_hist_stage,
#   canonical_hist_scope, migration_status, notes
# Former fields are loaded from the staging map at build time.
RENAMES: dict[str, dict[str, str]] = {}

# --- 3.1 Proto-Northwest Germanic rules: NWGmc* -> PNWGmc*, nwgmc->pnwgmc,
#         pan_nwgmc->pan_pnwgmc, reader "NWGmc ..." -> "Proto-Northwest Germanic ..."
_PNWGMC = {
    "SC005": "PNWGmcAToUBeforeM",
    "SC014": "PNWGmcUnstressedAiMonophthongization",
    "SC015": "PNWGmcILowering",
    "SC017": "PNWGmcULowering",
    "SC018": "PNWGmcStressedMonosyllableORaising",
    "SC019": "PNWGmcFinalLongORaising",
    "SC021": "PNWGmcUnstressedORaising",
    "SC022": "PNWGmcMnDissimilation",
    "SC023": "PNWGmcNStemNLoss",
    "SC024": "PNWGmcLongELowering",
    "SC025": "PNWGmcLongENasalRounding",
    "SC028": "PNWGmcPreconsonantalXLoss",
}
for _sc, _canon in _PNWGMC.items():
    RENAMES[_sc] = {
        "canonical_foma_identifier": _canon,
        "canonical_display_name": "",  # derived: "NWGmc X" -> "Proto-Northwest Germanic X"
        "canonical_hist_stage": "pnwgmc",
        "canonical_hist_scope": "pan_pnwgmc",
        "migration_status": "pending",
        "notes": "PNWGmc convention: make Proto-Northwest Germanic explicit; body/order unchanged",
    }

# --- 3.2 Early Anglo-Frisian corridor rules ---
RENAMES["SC003"] = {
    "canonical_foma_identifier": "EAFRhotacism",
    "canonical_display_name": "West Germanic rhotacism",
    "canonical_hist_stage": "eaf", "canonical_hist_scope": "pan_wgmc",
    "migration_status": "pending",
    "notes": "Former identifier PGmcRhotacism. Scope kept pan_wgmc; medial-*z* rhotacism scoped to non-final (order unchanged).",
}
RENAMES["SC020"] = {
    "canonical_foma_identifier": "EAFFinalZDeletion",
    "canonical_display_name": "West Germanic final *z*-deletion",
    "canonical_hist_stage": "eaf", "canonical_hist_scope": "pan_wgmc",
    "migration_status": "pending",
    "notes": "Former identifier PGmcFinalZDeletion. Scope provisional: pan-WGmc vs narrower (Ingvaeonic) UNRESOLVED; not settled by this rename.",
}
RENAMES["SC012"] = {
    "canonical_foma_identifier": "EAFLThVoicing",
    "canonical_display_name": "Northern West Germanic *lþ*-voicing",
    "canonical_hist_stage": "eaf", "canonical_hist_scope": "north_wgmc",
    "migration_status": "pending",
    "notes": "Former identifier PWGmcLThVoicing. Confidence A->B; pan-PWGmc attribution must not survive (R/T pp.170-171).",
}
RENAMES["SC026"] = {
    "canonical_foma_identifier": "EAFNasalSpirantLengthening",
    "canonical_display_name": "North Sea Germanic nasal-spirant lengthening",
    "canonical_hist_stage": "eaf", "canonical_hist_scope": "north_sea_germanic",
    "migration_status": "pending",
    "notes": "Former identifier NWGmcNasalSpirantLengthening. Traditional scholarly label: Ingvaeonic. Keep SC026<SC027, two-rule split.",
}
RENAMES["SC027"] = {
    "canonical_foma_identifier": "EAFNasalSpirantLoss",
    "canonical_display_name": "North Sea Germanic nasal-spirant loss",
    "canonical_hist_stage": "eaf", "canonical_hist_scope": "north_sea_germanic",
    "migration_status": "pending",
    "notes": "Former identifier NWGmcNasalSpirantLoss. Traditional scholarly label: Ingvaeonic.",
}
RENAMES["SC043"] = {
    "canonical_foma_identifier": "EAFBrightening",
    "canonical_display_name": "Anglo-Frisian brightening",
    "canonical_hist_stage": "eaf", "canonical_hist_scope": "anglo_frisian",
    "migration_status": "pending",
    "notes": "Former identifier AngloFrisianBrightening. Aligns identifier to EAF stage; conventional name retained in book.",
}

# --- Rules explicitly excluded from the rename migration (task section 4) ---
EXCLUDED: dict[str, tuple[str, str]] = {
    "SC004": ("deferred", "Conflates distinguishable developments; split decision pending (do not rename)."),
    "SC064": ("deferred", "Stage unresolved (hist_stage nwgmc vs chapter 4/OE, confidence C); do not rename."),
    "SC016": ("not_required", "OE West Saxon; early position is a documented FST dependency, not a stage claim."),
    "SC041": ("not_required", "PWGmc name source-correct (R/T pp.60-61); no rename."),
    "SC042": ("not_required", "Model-shaped feeder; position-by-dependency; no rename."),
    "SC049": ("not_required", "PGmc *b allophony correct; late position is an FST dependency."),
    "SC050": ("not_required", "Eponymous SieversLawSyncope may keep no stage prefix; late position is a feeder."),
}

FIELDS = [
    "sc_id", "former_foma_identifier", "canonical_foma_identifier",
    "former_display_name", "canonical_display_name",
    "former_hist_stage", "canonical_hist_stage",
    "former_hist_scope", "canonical_hist_scope",
    "migration_status", "migration_commit", "notes",
]


def _read_staging() -> dict[str, dict[str, str]]:
    lines = [ln for ln in STAGING_MAP.read_text(encoding="utf-8").splitlines() if not ln.startswith("#")]
    return {r["sc_id"]: r for r in csv.DictReader(io.StringIO("\n".join(lines)), delimiter="\t")}


def _canonical_display(sc: str, former_display: str, entry: dict[str, str]) -> str:
    if entry.get("canonical_display_name"):
        return entry["canonical_display_name"]
    # PNWGmc convention: "NWGmc X" -> "Proto-Northwest Germanic X"
    if former_display.startswith("NWGmc "):
        return "Proto-Northwest Germanic " + former_display[len("NWGmc "):]
    return former_display


def build_rows() -> list[dict[str, str]]:
    staging = _read_staging()
    rows: list[dict[str, str]] = []
    for sc in sorted(set(RENAMES) | set(EXCLUDED), key=lambda s: int(s[2:])):
        s = staging.get(sc, {})
        former_id = s.get("fst_identifier", "")
        former_disp = s.get("display_name", "")
        former_stage = s.get("hist_stage", "")
        former_scope = s.get("hist_scope", "")
        if sc in RENAMES:
            e = RENAMES[sc]
            rows.append({
                "sc_id": sc,
                "former_foma_identifier": former_id,
                "canonical_foma_identifier": e["canonical_foma_identifier"],
                "former_display_name": former_disp,
                "canonical_display_name": _canonical_display(sc, former_disp, e),
                "former_hist_stage": former_stage,
                "canonical_hist_stage": e["canonical_hist_stage"],
                "former_hist_scope": former_scope,
                "canonical_hist_scope": e["canonical_hist_scope"],
                "migration_status": e["migration_status"],
                "migration_commit": "",
                "notes": e["notes"],
            })
        else:
            status, note = EXCLUDED[sc]
            rows.append({
                "sc_id": sc,
                "former_foma_identifier": former_id,
                "canonical_foma_identifier": former_id,  # unchanged
                "former_display_name": former_disp,
                "canonical_display_name": former_disp,
                "former_hist_stage": former_stage,
                "canonical_hist_stage": former_stage,
                "former_hist_scope": former_scope,
                "canonical_hist_scope": former_scope,
                "migration_status": status,
                "migration_commit": "",
                "notes": note,
            })
    return rows


def write_manifest(rows: list[dict[str, str]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    rows = build_rows()
    write_manifest(rows, args.out)
    print(f"wrote {args.out} ({len(rows)} rules)")
    if args.summary:
        from collections import Counter
        print("  status:", dict(Counter(r["migration_status"] for r in rows)))
        print("  renames pending:", [r["sc_id"] for r in rows if r["migration_status"] == "pending"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
