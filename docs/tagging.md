# Tagging Guide

Use tags for discovery, not hierarchy.

## Field shape
```yaml
tags:
  geo: [southern_africa]
  language: [english, setswana]
  culture: [south_african]
  mood: [lyrical]
  rhythm: [dance]
  style: [vocal_led]
```

## Rules
- Values must be defined in `data/tags/*.yaml`.
- Keep tags specific and low-noise.
- Prefer 1 to 4 values per tag set.
- Do not encode parent/child taxonomy as tags.

## Common usage
- `geo`: geographic scene or market context.
- `language`: common lyrical language(s).
- `culture`: cultural identity context.
- `mood`: expressive intent.
- `rhythm`: groove structure.
- `style`: broad sonic markers.
