# src/components/

Reusable presentational components shared across scenes.

## Contents

- `Header.jsx` – Section header used at the top of most scenes. Accepts `title` and `subtitle` props and renders them with the current theme's text and accent colors.

## Guidelines

- Keep components in this folder purely presentational; scene-specific logic belongs in `src/scenes/`.
- Use MUI's `Box`, `Typography` etc. and pull colors from `tokens(theme.palette.mode)` in `src/theme.js` so light/dark mode stays consistent.
