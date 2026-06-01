# Page Rendering

This folder contains the shared page rendering logic for the static site.

## Flow

- `data/*.json` stores editable content.
- `src/pages/renderers.py` converts that content into HTML sections.
- `scripts/render_site.py` rebuilds all data-driven pages.
- `scripts/build_pages.py` and `scripts/rebuild_projects.py` remain as compatibility wrappers.

## Editing Content

- Add/edit project cards in `data/projects.json`
- Add/edit timeline entries in `data/journey.json` and `data/voluntary.json`
- Add/edit award cards in `data/awards.json`
- Add/edit art items in `data/art.json`
- Add/edit photo captures in `data/captures.json`
