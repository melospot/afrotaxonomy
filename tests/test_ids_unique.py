from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
GENRES_DIR = ROOT / "data" / "genres"


def test_ids_unique() -> None:
    ids = []
    for path in GENRES_DIR.rglob("*.yaml"):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        assert "id" in data, f"Missing id in {path.relative_to(ROOT)}"
        ids.append(data["id"])

    assert len(ids) == len(set(ids)), "Duplicate genre IDs found"
