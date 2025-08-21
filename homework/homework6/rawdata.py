import os
import pandas as pd
import numpy as np

# Define folder paths relative to this notebook
raw_dir = '../data/raw'
processed_dir = '../data/processed'

# Create folders if they don't exist
os.makedirs(raw_dir, exist_ok=True)
os.makedirs(processed_dir, exist_ok=True)

# Define the sample data
data = {
    'age': [34, 45, 29, 50, 38, np.nan, 41],
    'income': [55000, np.nan, 42000, 58000, np.nan, np.nan, 49000],
    'score': [0.82, 0.91, np.nan, 0.76, 0.88, 0.65, 0.79],
    'zipcode': ['90210', '10001', '60614', '94103', '73301', '12345', '94105'],
    'city': ['Beverly', 'New York', 'Chicago', 'SF', 'Austin', 'Unknown', 'San Francisco'],
    'extra_data': [np.nan, 42, np.nan, np.nan, np.nan, 5, np.nan]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV in raw data folder
csv_path = os.path.join(raw_dir, 'sample_data.csv')
if not os.path.exists(csv_path):
    df.to_csv(csv_path, index=False)
    print(f'Sample dataset created and saved to {csv_path}')
else:
    print(f'File already exists at {csv_path}.')
