"""Preserve declared science; context-lift private transparent placeholders."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).parent
original = root / "recipes.json"
destination = root / "recipes-context-v2.json"
if destination.exists():
    raise RuntimeError("Technical revision already exists")
data = json.loads(original.read_text())
changes = []
for recipe in data["recipes"]:
    for name in ("AFId18", "AFId19", "AFPass"):
        before = f"define {name} [[EnglishStarAlphabet]*];"
        after = f"define {name} [Ctx([[EnglishStarAlphabet]*])];"
        if before in recipe["definitions"]:
            recipe["definitions"] = recipe["definitions"].replace(before, after)
            changes.append({"recipe": recipe["id"], "before": before, "after": after})
destination.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
receipt = {
    "original_sha256": hashlib.sha256(original.read_bytes()).hexdigest(),
    "revision_sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
    "changes": changes,
    "operational_failure": (
        "A's segment-only transparent placeholder rejected selected you2326 "
        "(raw ᵘízwiz), because EnglishStarAlphabet excludes the word-unstressed "
        "context prefix. This is a private helper defect, not a sound-law result."),
    "scientific_definitions_order_predictions_source_pins_unchanged": True,
}
(root / "context-identity-repair.json").write_text(
    json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
