from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
GENRES_DIR = ROOT / "data" / "genres"


def test_no_orphans() -> None:
    genres = []
    for path in GENRES_DIR.rglob("*.yaml"):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        data["_path"] = path.relative_to(ROOT)
        genres.append(data)

    ids = {g["id"] for g in genres if "id" in g}

    for genre in genres:
        for parent in genre.get("parents", []):
            assert parent in ids, f"{genre['_path']} has missing parent `{parent}`"
