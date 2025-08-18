# Homework 5: Data Formats and Storage

## Overview

This homework demonstrates working with different data formats (CSV and Parquet) and environment-driven configuration for data storage paths.

## Folders

- `data/raw/` — raw captures (immutable, append-only)
- `data/processed/` — cleaned/typed data ready for analysis

## Formats 

- CSV in `data/raw/`: human-readable, easy to diff/review, good for raw drops.
- Parquet in `data/processed/`: columnar, type-preserving, compressed; faster IO and smaller size for analytics.

## Env

- Paths are configured via `.env`:
  - `DATA_DIR_RAW=data/raw`
  - `DATA_DIR_PROCESSED=data/processed`
- The notebook loads environment variables with `python-dotenv`, then reads/writes by suffix:
  - `write_df(df, path)` supports `.csv` and `.parquet` (tries `pyarrow`, then `fastparquet`).
  - `read_df(path)` auto-routes and parses dates from CSV when present.

## Project Structure

```
homework5/
├── notebooks/
│   └── homework5_data_formats.ipynb    # Main notebook (executed)
├── data/
│   ├── raw/
│   │   └── sample_YYYYMMDD-HHMM.csv   # Raw CSV data
│   └── processed/
│       └── sample_YYYYMMDD-HHMM.parquet # Processed Parquet data
├── .env                                # Environment configuration
└── README.md                          # This file
```

## Features

### Data Validation
- `validate_df()` function checks column presence and data types
- Supports datetime, float, int, string, and exact dtype validation
- Returns detailed validation messages

### File I/O Utilities
- `write_df()` - Universal writer supporting CSV and Parquet formats
- `read_df()` - Universal reader with automatic format detection
- Automatic date parsing for CSV files
- Fallback engine support for Parquet (pyarrow → fastparquet)

### Environment Configuration
- Uses `python-dotenv` for configuration management
- Configurable data directory paths
- Safe fallbacks for missing environment variables

## Requirements

- pandas
- python-dotenv
- pyarrow (recommended) or fastparquet

## Usage

1. **Set up environment**:
   ```bash
   pip install pandas python-dotenv pyarrow
   ```

2. **Configure paths** (optional):
   Edit `.env` file to customize data directories

3. **Run the notebook**:
   ```bash
   jupyter notebook notebooks/homework5_data_formats.ipynb
   ```

## Generated Files

The notebook creates timestamped files:
- `data/raw/sample_YYYYMMDD-HHMM.csv` - Sample stock data in CSV format
- `data/processed/sample_YYYYMMDD-HHMM.parquet` - Same data in Parquet format

Both files contain 8 rows of AAPL stock data with columns: date, symbol, adj_close.

## Key Benefits

- **CSV**: Human-readable, version control friendly, universal compatibility
- **Parquet**: Compressed, type-preserving, faster I/O for analytics workloads
- **Environment-driven**: Flexible configuration without code changes
- **Validation**: Ensures data quality and type consistency
