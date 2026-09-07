# src/scenes/

Page-level views. Each subfolder is one route in the admin dashboard, exported as the default component from `index.js` / `index.jsx` inside that folder.

## Subdirectories

- `global/` – Shell UI that wraps every scene.
  - `Sidebar.jsx` – Collapsible left navigation built with `react-pro-sidebar`; lists routes to every scene.
  - `Topbar.jsx` – Top action bar with search input, color-mode toggle, notification, settings and profile buttons.
- `dashboard/` – Landing page (`index.jsx`). Shows KPI stat boxes, revenue line chart, bar chart, geography chart and recent transactions.
- `team/` – Team members data grid (`index.js`) rendered with `@mui/x-data-grid` and colored access-level chips.
- `contacts/` – Contacts data grid (`index.js`) using the MUI DataGrid with column filtering.
- `invoices/` – Invoices data grid (`index.js`) showing customer, amount and date columns.
- `form/` – User profile form (`index.js`) built with Formik + Yup validation.
- `calendar/` – Interactive calendar (`index.js`) built with FullCalendar plugins (dayGrid, timeGrid, interaction, list) and a side list of current events.

## Adding a new scene

1. Create `src/scenes/<name>/index.jsx`.
2. Export a default React component.
3. Add a `<Route path="/<name>" element={<Name />} />` entry in `src/App.js`.
4. Add a matching `Item` in `src/scenes/global/Sidebar.jsx`.
