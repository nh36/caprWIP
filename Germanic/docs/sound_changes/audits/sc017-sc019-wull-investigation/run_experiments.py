"""Execute and persist protected recipes serially; never touch production."""
import json
from pathlib import Path
import sys
import time

sys.path.insert(0, "/usr/app/tools")
import anglo_frisian_experiments as assay

root = Path("/research")
data = assay.load_recipes(root / "recipes.json")
for recipe in data["recipes"]:
    name = recipe["id"]
    destination = root / f"{name}.json"
    if destination.exists():
        raise RuntimeError(f"Completed receipt already exists: {destination}")
    start = time.monotonic()
    print(f"START {name}", flush=True)
    report = assay.run(data, name)
    report["elapsed_seconds"] = time.monotonic() - start
    report["checkpoint_count"] = len(data["probes"])
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    if report["missing_output_ids"] or report["ambiguous_output_ids"]:
        raise RuntimeError(f"{name}: rejected or ambiguous corpus outputs")
    print(json.dumps({
        key: report[key] for key in (
            "selected_rows", "identity_equal", "canonical_artifacts_unchanged",
            "changed_ids", "variant_mismatch_ids", "missing_output_ids",
            "ambiguous_output_ids", "elapsed_seconds",
        )
    }), flush=True)
