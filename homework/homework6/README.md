# Cleaning strategy 

Missing values: Median fill on numeric columns 

Row completeness: Keep rows with ≥60% non-missing fields to avoid over-imputation.

Scaling: Normalize numeric features (choose one: z-score or min–max). Skip zero-variance columns.

Categoricals: Not scaled (e.g., IDs/labels).

Reproducibility: Functions live in src/cleaning.py; 

# Tradeoffs

Median vs mean: Median resists outliers; mean can skew.

Global vs group-wise fill: Group-wise preserves segments but needs enough data per group.

Row threshold: Higher = cleaner but fewer rows; lower = more data but more imputation.

Z-score vs min–max: Z-score for model comparability; min–max for bounded [0,1] range/visuals.
