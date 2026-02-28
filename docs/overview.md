# Overview

This repository stores a structured taxonomy of African music genres.

## Goals
- Keep genre definitions machine-readable and versioned.
- Separate hierarchy (`parents`) from discovery metadata (`tags`).
- Support transparent contributions and contested-genre documentation.

## Source of truth
- `data/genres/**/*.yaml`: canonical genres and subgenres.
- `data/tags/*.yaml`: controlled vocabularies for tagging.
- `data/relations.yaml`: cross-genre relations beyond parent/child.
