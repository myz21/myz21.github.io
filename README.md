# Muhammed Yıldız — Portfolio

Static portfolio site generated from structured content files.

## Structure

- `data/site.json` — page titles and intro content
- `data/projects.json` — project cards
- `data/journey.json` — journey timeline items
- `data/voluntary.json` — voluntary timeline items
- `data/awards.json` — award cards and carousel media
- `data/art.json` — art gallery items
- `data/captures.json` — photo gallery items
- `src/pages/renderers.py` — shared render pipeline
- `scripts/render_site.py` — rebuilds all data-driven pages
- `assets/styles/main.css` — shared site styles
- `assets/scripts/theme.js` — shared light/dark theme behavior

## Generated Pages

- `projects.html`
- `journey.html`
- `voluntary.html`
- `awards.html`
- `art.html`
- `captures.html`

`index.html` remains hand-authored, but uses the shared stylesheet.

## Local Development

```bash
python3 -m http.server 8081
```

Then open:

```bash
http://localhost:8081
```

## Rebuild Pages

Rebuild every data-driven page:

```bash
python scripts/render_site.py
```

Compatibility wrappers:

```bash
python scripts/build_pages.py
python scripts/rebuild_projects.py
```

## Editing Content

### Add a new journey item

Add a new object to `data/journey.json`:

```json
{
  "year": "2026",
  "side": "right",
  "title": "Example title",
  "body": "Short description.",
  "date": "Jan 2026",
  "logo": "assets/example-logo.png",
  "link": "https://example.com",
  "link_label": "Example",
  "media": ["assets/example-image.jpg"]
}
```

Then run:

```bash
python scripts/render_site.py
```

### Add a new art or capture item

Append a new object to `data/art.json` or `data/captures.json`, then rebuild.

## Why this setup

- Content is separated from layout
- New cards and timeline items can be added without hand-editing HTML
- Shared rendering logic keeps page patterns consistent
- Shared CSS keeps typography, spacing, and responsive behavior aligned
- Shared theme logic keeps light/dark mode consistent across pages

## Links

- Site: `https://myz21.github.io`
- GitHub: `https://github.com/myz21`
- LinkedIn: `https://linkedin.com/in/myzz`
- Art Instagram: `https://instagram.com/delusional.myz`
