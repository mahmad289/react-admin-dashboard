# src/data/

Static mock data used by the dashboard. In a real application this would be replaced by API calls.

## Contents

- `mockData.js` – Mock records for the various tables and lists:
  - `mockDataTeam` – Rows for the Team scene (id, name, age, phone, email, access level).
  - `mockDataContacts` – Rows for the Contacts scene.
  - `mockDataInvoices` – Rows for the Invoices scene.
  - `mockTransactions` – Recent transaction items shown on the dashboard.
  - `mockBarData`, `mockPieData`, `mockLineData` – Series data for the Nivo charts.
- `mockGeoFeatures.js` – GeoJSON feature collection used by the Nivo geo (choropleth) chart.

## Guidelines

- Import mock arrays directly where they're used; do not mutate them.
- When wiring up a real backend, replace these imports with `fetch`/`axios` calls returning the same shape.
