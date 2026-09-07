# src/

The main React application source code. Everything here is processed by Create React App's webpack build.

## Top-level files

- `index.js` – Entry point. Bootstraps React 18 (`ReactDOM.createRoot`) and mounts `<App />` inside `<div id="root">`.
- `App.js` – Root component. Wires up routing (react-router-dom), the color-mode / theme provider, the sidebar and topbar, and renders each scene by route.
- `index.css` – Global CSS resets and font imports (Source Sans Pro).
- `theme.js` – Central theme configuration:
  - `tokens(mode)` – returns the color palette for light/dark mode.
  - `themeSettings(mode)` – returns the MUI theme object.
  - `ColorModeContext` – React context used to toggle color mode.
  - `useMode()` – hook returning `[theme, colorMode]`.

## Subdirectories

- `components/` – Reusable presentational components. See [src-components.md](./src-components.md).
- `data/` – Static / mock data used by tables, charts and maps. See [src-data.md](./src-data.md).
- `scenes/` – Page-level views mapped to routes. See [src-scenes.md](./src-scenes.md).
