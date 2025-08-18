Folders
- `data/raw/` — raw captures (immutable, append-only)
- `data/processed/` — cleaned/typed data ready for analysis

Formats 
- CSV in `data/raw/`: human-readable, easy to diff/review, good for raw drops.
- Parquet in `data/processed/`: columnar, type-preserving, compressed; faster IO and smaller size for analytics.

Env
- Paths are configured via `.env`:
  - `DATA_DIR_RAW=data/raw`
  - `DATA_DIR_PROCESSED=data/processed`
- The notebook loads environment variables with `python-dotenv`, then reads/writes by suffix:
  - `write_df(df, path)` supports `.csv` and `.parquet` (tries `pyarrow`, then `fastparquet`).
  - `read_df(path)` auto-routes and parses dates from CSV when present.
