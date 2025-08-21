# Homework 6: Data Preprocessing

This project implements data cleaning and preprocessing functions for handling missing values and normalizing data.

## Project Structure

```
homework6/
├── data/
│   ├── raw/
│   │   └── sample_data.csv          # Original dataset with missing values
│   └── processed/
│       └── sample_data_cleaned.csv  # Cleaned dataset (generated)
├── notebook/
│   └── stage06_preprocessing.ipynb  # Main preprocessing notebook
├── src/
│   ├── __init__.py
│   └── cleaning.py                  # Data cleaning functions
└── README.md
```

## Data Cleaning Strategy

### 1. Missing Value Imputation (`fill_missing_median`)
- **Strategy**: Fill missing values in numeric columns with their median values
- **Rationale**: Median is robust to outliers and provides a reasonable central tendency estimate
- **Assumptions**: 
  - Missing values are Missing At Random (MAR)
  - Median is representative of the typical value for each column
  - Only applied to numeric columns (int64, float64)

### 2. Column Dropping (`drop_missing`)
- **Strategy**: Remove columns that exceed a specified threshold of missing values
- **Default Threshold**: 50% missing values
- **Rationale**: Columns with excessive missing data provide limited analytical value
- **Assumptions**:
  - Columns with >50% missing values are not critical for analysis
  - Remaining data in other columns is sufficient for analysis

### 3. Data Normalization (`normalize_data`)
- **Strategy**: Min-max scaling to transform values to 0-1 range
- **Formula**: `(x - min) / (max - min)`
- **Rationale**: Ensures all numeric features are on the same scale for analysis
- **Assumptions**:
  - Linear scaling preserves relative relationships
  - 0-1 range is appropriate for the intended analysis
  - No extreme outliers that would skew the scaling

## Sample Dataset

The `sample_data.csv` contains:
- **7 rows** of sample data
- **6 columns**: age, income, score, zipcode, city, extra_data
- **Missing values** strategically placed to test cleaning functions:
  - age: 1 missing value (14.3%)
  - income: 3 missing values (42.9%)
  - score: 1 missing value (14.3%)
  - extra_data: 5 missing values (71.4%) - will be dropped

## Usage

1. **Run the notebook**: Open `notebook/stage06_preprocessing.ipynb`
2. **Execute all cells** to see the complete preprocessing pipeline
3. **Review outputs**: 
   - Data audit results
   - Function execution logs
   - Before/after comparison
   - Processed data saved to `data/processed/`

## Functions

### `fill_missing_median(df, columns)`
- Fills missing values with median for specified numeric columns
- Returns: DataFrame with imputed values
- Prints: Median values used for each column

### `drop_missing(df, threshold=0.5)`
- Drops columns exceeding the missing value threshold
- Returns: DataFrame with high-missing columns removed
- Prints: List of dropped columns

### `normalize_data(df, columns, method='min-max')`
- Normalizes specified numeric columns using min-max scaling
- Returns: DataFrame with normalized columns
- Prints: Min/max values used for scaling

## Expected Results

After processing:
- **extra_data** column dropped (>50% missing)
- **age, income, score** missing values filled with medians
- **income, score** normalized to 0-1 range
- Clean dataset saved to `data/processed/sample_data_cleaned.csv`

## Assumptions and Limitations

1. **Data Quality**: Assumes missing values are not systematically biased
2. **Distribution**: Median imputation assumes reasonably normal distributions
3. **Scale**: Min-max normalization assumes no extreme outliers
4. **Context**: Cleaning strategy may need adjustment based on specific use case
5. **Temporal**: No consideration for time-series patterns in missing data
