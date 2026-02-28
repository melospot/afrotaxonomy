#!/usr/bin/env python3
"""Compile YAML sources into build/dist artifacts."""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
import sys

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Missing dependency: pyyaml. Install with `pip install pyyaml`.") from exc


ROOT = Path(__file__).resolve().parents[1]
GENRES_DIR = ROOT / "data" / "genres"
TAGS_DIR = ROOT / "data" / "tags"
RELATIONS_FILE = ROOT / "data" / "relations.yaml"
DIST_DIR = ROOT / "build" / "dist"


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def main() -> int:
    genre_files = sorted(GENRES_DIR.rglob("*.yaml"))
    tag_files = sorted(TAGS_DIR.glob("*.yaml"))

    genres = []
    for path in genre_files:
        item = load_yaml(path)
        item["source_path"] = str(path.relative_to(ROOT)).replace("\\", "/")
        genres.append(item)

    tags = [load_yaml(path) for path in tag_files]
    relations = load_yaml(RELATIONS_FILE) if RELATIONS_FILE.exists() else {}

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "genres": genres,
        "tags": tags,
        "relations": relations,
    }

    DIST_DIR.mkdir(parents=True, exist_ok=True)

    taxonomy_json = DIST_DIR / "taxonomy.json"
    taxonomy_min_json = DIST_DIR / "taxonomy.min.json"
    taxonomy_csv = DIST_DIR / "taxonomy.csv"
    taxonomy_graphql_json = DIST_DIR / "taxonomy.graphql.json"

    taxonomy_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    taxonomy_min_json.write_text(json.dumps(payload, separators=(",", ":"), ensure_ascii=False), encoding="utf-8")
    taxonomy_graphql_json.write_text(
        json.dumps({"Genre": genres, "Relation": relations.get("relations", [])}, indent=2, ensure_ascii=False)
        + "\n",
        encoding="utf-8",
    )

    with taxonomy_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["id", "name", "parents", "status", "source_path"])
        for genre in genres:
            writer.writerow(
                [
                    genre.get("id", ""),
                    genre.get("name", ""),
                    "|".join(genre.get("parents", [])),
                    genre.get("status", ""),
                    genre.get("source_path", ""),
                ]
            )

    print(f"Built {len(genres)} genres into {DIST_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
