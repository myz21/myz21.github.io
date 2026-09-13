# Muhammed Yıldız — Portfolio

Vite-powered, multi-page portfolio built with vanilla JavaScript.

## Structure

- `data/` — retained structured content archive from the prior static generator
- `public/data/oss-contributions.json` — generated GitHub pull request and issue feed
- `src/main.js` — shared vanilla JavaScript entry point
- `src/theme.js` — theme interaction module
- `scripts/update-oss-contributions.mjs` — fetches the latest public OSS activity
- `.github/workflows/update-oss-contributions.yml` — refreshes the OSS feed every six hours
- `assets/styles/main.css` — shared site styles

## Vite Pages

- `projects.html`
- `journey.html`
- `voluntary.html`
- `awards.html`
- `art.html`

## OSS Contributions Feed

The home page reads its contribution list from `public/data/oss-contributions.json`; visitors do not call the GitHub API directly.
GitHub Actions refreshes that file every six hours and commits it only when the result changes. It can also be run immediately from the repository's **Actions → Update OSS contributions → Run workflow** screen.

To refresh it locally (public contributions only):

```bash
node scripts/update-oss-contributions.mjs
```

## Local Development

```bash
npm install
npm run dev
```

Vite prints the local address in the terminal. Build the production-ready `dist/` directory with:

```bash
npm run build
```

## Why this setup

- Vite provides a fast development server and optimized production build
- Shared JavaScript modules keep browser behavior consistent
- Shared CSS keeps typography, spacing, and responsive behavior aligned
- The contribution feed is generated server-side and contains no exposed token

## Links

- Site: `https://myz21.github.io`
- GitHub: `https://github.com/myz21`
- LinkedIn: `https://linkedin.com/in/myzz`
- Art Instagram: `https://instagram.com/delusional.myz`
