# public/

Static files served by Create React App without processing. Anything placed here can be referenced from `index.html` using `%PUBLIC_URL%` or from code using an absolute path (e.g. `/logo192.png`).

## Contents

- `index.html` – The single HTML page that hosts the React app. The `<div id="root">` element is where React mounts.
- `favicon.ico` – Browser tab icon.
- `logo192.png`, `logo512.png` – App icons used by the PWA manifest.
- `manifest.json` – Web App Manifest for Progressive Web App support.
- `robots.txt` – Instructions for search-engine crawlers.
- `assets/` – Additional static images.
  - `user.png` – Default user avatar shown in the sidebar / topbar.

## Notes

- Files in `public/` are NOT processed by webpack. Prefer importing assets from `src/` when you want hashing and optimization.
- Only place a file here if it must keep its filename (e.g. `robots.txt`) or must exist at a stable URL.
