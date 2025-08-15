"""
Utility functions for Budget Lens data analysis.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Any
import json
import os


def get_summary_stats(df: pd.DataFrame, numeric_only: bool = True) -> pd.DataFrame:
    """
    Calculate summary statistics for a DataFrame.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        numeric_only (bool): Whether to include only numeric columns
        
    Returns:
        pd.DataFrame: Summary statistics
    """
    if numeric_only:
        return df.describe()
    else:
        return df.describe(include='all')


def category_analysis(df: pd.DataFrame, amount_col: str = 'amount', 
                     category_col: str = 'category') -> pd.DataFrame:
    """
    Perform groupby analysis by category.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        amount_col (str): Name of the amount column
        category_col (str): Name of the category column
        
    Returns:
        pd.DataFrame: Aggregated statistics by category
    """
    return df.groupby(category_col)[amount_col].agg([
        'count', 'sum', 'mean', 'median', 'std', 'min', 'max'
    ]).round(2)


def save_summary_to_files(summary_data: Dict[str, Any], output_dir: str = 'data/processed'):
    """
    Save summary statistics to both CSV and JSON formats.
    
    Args:
        summary_data (dict): Dictionary containing summary data
        output_dir (str): Output directory path
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Save to JSON
    json_path = os.path.join(output_dir, 'summary.json')
    with open(json_path, 'w') as f:
        # Convert numpy types to native Python types for JSON serialization
        json_data = {}
        for key, value in summary_data.items():
            if isinstance(value, pd.DataFrame):
                json_data[key] = value.to_dict()
            elif isinstance(value, (np.integer, np.floating)):
                json_data[key] = value.item()
            else:
                json_data[key] = value
        json.dump(json_data, f, indent=2)
    
    # Save DataFrames to CSV
    for key, value in summary_data.items():
        if isinstance(value, pd.DataFrame):
            csv_path = os.path.join(output_dir, f'{key}.csv')
            value.to_csv(csv_path)
    
    print(f"Summary data saved to {output_dir}")


def create_spending_plot(df: pd.DataFrame, save_path: str = None) -> plt.Figure:
    """
    Create a basic spending analysis plot.
    
    Args:
        df (pd.DataFrame): Input DataFrame with spending data
        save_path (str): Path to save the plot (optional)
        
    Returns:
        plt.Figure: The created figure
    """
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Budget Lens - Spending Analysis', fontsize=16, fontweight='bold')
    
    # 1. Spending by Category (Bar plot)
    category_totals = df.groupby('category')['amount'].sum().sort_values(ascending=False)
    axes[0, 0].bar(category_totals.index, category_totals.values, color='skyblue')
    axes[0, 0].set_title('Total Spending by Category')
    axes[0, 0].set_xlabel('Category')
    axes[0, 0].set_ylabel('Amount ($)')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 2. Spending Distribution (Histogram)
    axes[0, 1].hist(df['amount'], bins=15, color='lightgreen', alpha=0.7, edgecolor='black')
    axes[0, 1].set_title('Distribution of Transaction Amounts')
    axes[0, 1].set_xlabel('Amount ($)')
    axes[0, 1].set_ylabel('Frequency')
    
    # 3. Average Spending by Category (Horizontal bar)
    category_avg = df.groupby('category')['amount'].mean().sort_values(ascending=True)
    axes[1, 0].barh(category_avg.index, category_avg.values, color='coral')
    axes[1, 0].set_title('Average Spending by Category')
    axes[1, 0].set_xlabel('Average Amount ($)')
    
    # 4. Transaction Count by Category (Pie chart)
    category_counts = df['category'].value_counts()
    axes[1, 1].pie(category_counts.values, labels=category_counts.index, autopct='%1.1f%%', startangle=90)
    axes[1, 1].set_title('Transaction Count by Category')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    
    return fig


def compare_performance(data_size: int = 1000000) -> Dict[str, float]:
    """
    Compare loop vs vectorized operations performance.
    
    Args:
        data_size (int): Size of the array to test
        
    Returns:
        dict: Performance comparison results
    """
    import time
    
    # Create test data
    arr = np.random.rand(data_size)
    
    # Loop-based operation
    start_time = time.time()
    result_loop = []
    for x in arr:
        result_loop.append(x ** 2 + 2 * x + 1)
    loop_time = time.time() - start_time
    
    # Vectorized operation
    start_time = time.time()
    result_vectorized = arr ** 2 + 2 * arr + 1
    vectorized_time = time.time() - start_time
    
    speedup = loop_time / vectorized_time
    
    return {
        'data_size': data_size,
        'loop_time': loop_time,
        'vectorized_time': vectorized_time,
        'speedup_factor': speedup
    }
