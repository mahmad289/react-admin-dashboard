# backend/

Placeholder directory for future backend / server-side code.

## Current state

The folder is currently empty. The dashboard front-end runs entirely on mock data from `src/data/`.

## Suggested layout (when it grows)

```
backend/
  src/
    routes/      # HTTP route handlers
    controllers/ # Business logic
    models/      # Data models / ORM entities
    services/    # External integrations
  package.json   # Backend-only dependencies
  README.md      # Backend-specific instructions
```

Keep backend dependencies isolated from the React app's `package.json` so front-end and back-end can be deployed independently.
