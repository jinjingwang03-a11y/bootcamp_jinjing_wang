# Homework 4: Data Acquisition and Ingestion

## Overview

This homework demonstrates data acquisition from APIs and web scraping, with proper validation and file naming conventions.

## Project Structure

```
homework4/
├── data/
│   └── raw/                      # Raw data files
│       ├── api_*.csv            # API-sourced data files
│       └── scrape_*.csv         # Web-scraped data files
├── stage04_data-acquisition-and-ingestion_homework-starter.ipynb  # Main notebook
├── .env                         # Environment variables (optional)
├── .gitignore                   # Git exclusions
└── README.md                    # This file
```

## Requirements

- Python 3.11+
- pandas
- requests
- beautifulsoup4
- yfinance
- python-dotenv

## Features

### 1. API Data Acquisition
- Fetches stock data using yfinance (with Alpha Vantage fallback)
- Proper error handling and data validation
- Standardized file naming: `api_<SOURCE>_<TICKER>_<YYYYMMDD-HHMMSS>.csv`

### 2. Web Scraping
- Demonstrates HTML table parsing with BeautifulSoup
- Automatic numeric column detection and conversion
- Standardized file naming: `scrape_<SITE>_<TABLE>_<YYYYMMDD-HHMMSS>.csv`

### 3. Data Validation
- Comprehensive validation function for DataFrames
- Column existence checks
- Data type validation with coercion
- Missing value analysis
- Minimum row requirements

### 4. Helper Functions
- `safe_stamp()`: Generate timestamp strings
- `safe_filename()`: Create standardized filenames
- `validate_df()`: Comprehensive DataFrame validation
- `parse_first_table()`: HTML table parsing

## Generated Files

The notebook generates two CSV files in `data/raw/`:

1. **API Data**: Stock price data from yfinance
   - Columns: `date`, `adj_close`
   - ~125 rows of 6-month AAPL data

2. **Scraped Data**: Demo S&P 500 company data
   - Columns: `Ticker`, `Company`, `Price`, `Market Cap`
   - 5 rows of sample data

## Usage

1. **Run the Notebook**:
   ```bash
   jupyter notebook stage04_data-acquisition-and-ingestion_homework-starter.ipynb
   ```

2. **Optional: Set Alpha Vantage API Key**:
   ```bash
   echo "ALPHAVANTAGE_API_KEY=your_key_here" > .env
   ```

## Code Quality

- ✅ Proper error handling with try/catch blocks
- ✅ Type hints for function parameters
- ✅ Comprehensive data validation
- ✅ Standardized file naming conventions
- ✅ Clean separation of concerns
- ✅ Detailed logging and status messages

## Output Validation

Both generated CSV files pass validation checks:
- All required columns present
- Correct data types
- No missing values
- Minimum row requirements met

This homework demonstrates best practices for data acquisition, validation, and storage in a production-ready format.
