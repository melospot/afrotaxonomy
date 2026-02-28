# Genre Hierarchy Rules

## 1) One genre per file
- Store each genre in `data/genres/<region>/<country>/<name>.yaml` when possible.
- Use `data/genres/foundations/` for umbrella or cross-region parent genres.
- Keep `data/genres/root.yaml` as the single taxonomy root node.

## 2) Required fields
- `id`: stable snake_case identifier.
- `name`: primary display name.
- `parents`: list of parent genre IDs.

## 3) Recommended fields
- `aliases`: known alternate names.
- `origin.countries`: ISO 3166-1 alpha-2 country codes.
- `description`: short plain-language summary.
- `status`: `active`, `legacy`, or `experimental`.
- `subgenres`: optional convenience list of child IDs.

## 4) Subgenre modeling
- A subgenre must have its own file.
- A subgenre links to its parent via `parents: [<parent_id>]`.
- If `subgenres` is used on the parent, store child IDs only.
- Do not store free-text subgenre names in `subgenres`.

## 5) Validation checklist
- All `parents` IDs exist as files.
- All `subgenres` IDs exist as files.
- Country and tag values come from controlled vocab files.
