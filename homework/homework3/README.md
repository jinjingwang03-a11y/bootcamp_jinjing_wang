# Budget Lens - Data Analysis (Homework 3)

## Overview

This homework demonstrates fundamental data analysis skills using NumPy and pandas for financial data processing. The project includes array operations, dataset loading, statistical analysis, and reusable utility functions.

## Project Structure

```
homework3/
├── data/
│   ├── starter_data.csv          # Sample financial transaction data
│   └── processed/                # Output directory for processed data
├── notebooks/
│   └── 01_data_analysis.ipynb    # Main analysis notebook
├── src/
│   └── utils.py                  # Reusable utility functions
└── README.md                     # This file
```

## Requirements

- Python 3.11+
- NumPy
- Pandas
- Matplotlib
- Seaborn

## Key Features

### 1. NumPy Operations
- Array creation and element-wise operations
- Performance comparison: loop vs vectorized execution
- Financial calculations (savings rate, expense ratios)

### 2. Dataset Loading & Inspection
- CSV loading using pandas
- Data inspection with `.info()` and `.head()`
- Missing value analysis

### 3. Summary Statistics
- Descriptive statistics using `.describe()`
- Category-based aggregation with `.groupby()`
- Custom statistical analysis

### 4. Data Export
- Save summary statistics to CSV and JSON formats
- Generate and save visualization plots
- Organized output in `data/processed/`

### 5. Reusable Functions
- `get_summary_stats()`: Calculate DataFrame summary statistics
- `category_analysis()`: Perform groupby analysis by category
- `save_summary_to_files()`: Export data to multiple formats
- `create_spending_plot()`: Generate comprehensive visualizations
- `compare_performance()`: Benchmark loop vs vectorized operations

## Usage

1. **Run the Analysis Notebook**:
   ```bash
   jupyter notebook notebooks/01_data_analysis.ipynb
   ```

2. **Import Utility Functions**:
   ```python
   from src.utils import get_summary_stats, category_analysis
   
   # Load your data
   df = pd.read_csv('data/starter_data.csv')
   
   # Get summary statistics
   summary = get_summary_stats(df)
   
   # Analyze by category
   category_stats = category_analysis(df)
   ```

## Sample Data

The `starter_data.csv` contains 30 sample financial transactions with:
- **date**: Transaction date
- **amount**: Transaction amount in USD
- **category**: Spending category (Food, Transport, Shopping, etc.)
- **merchant**: Merchant name
- **description**: Transaction description

## Output Files

After running the analysis, the following files are generated in `data/processed/`:
- `summary.json`: Complete summary data in JSON format
- `overall_summary.csv`: Basic descriptive statistics
- `category_analysis.csv`: Category-wise spending analysis
- `spending_analysis.png`: Comprehensive visualization plots

## Key Insights

The analysis reveals:
- **Performance**: Vectorized operations are ~10-100x faster than loops
- **Spending Patterns**: Clear categorization of expenses with statistical summaries
- **Data Quality**: Complete dataset with no missing values
- **Actionable Metrics**: Average spending, category rankings, and distribution analysis

## Next Steps

This foundation enables:
- Advanced time series analysis
- Predictive modeling for spending patterns
- Budget optimization recommendations
- Real-time expense tracking integration
