---
name: csv-reports
description: This skill is for CSV files.
metadata:
  author: data-team
  version: 1.0
---

# CSV reports

CSV (comma-separated values) is a plain-text file format where each line is a row and commas separate the columns. Many tools export CSV, including spreadsheets and databases.

To read the file, you can use pandas, polars, the csv module, or duckdb. Pick whichever you like.

## Steps

1. Load the CSV file.
2. Work out what each column holds. Mark any column you can't identify with `[UNKNOWN]` in the report so we can fill it in later.
3. Compute totals and averages for the numeric columns.
4. Write the report to `report.md`.
5. If the user wants a chart, follow [references/charts.md](references/charts.md).

Follow the team style guide in [../../docs/report-style.md](../../docs/report-style.md) for headings and number formats.

This should probably work on most CSV files, as far as we know.

Note: we haven't run any evals on this skill yet.
