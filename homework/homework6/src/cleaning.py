"""
Data cleaning functions for homework6 preprocessing.

This module contains functions for handling missing values and normalizing data.
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Any


def fill_missing_median(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Fill missing values in specified columns with their median values.
    
    Args:
        df (pd.DataFrame): Input dataframe
        columns (List[str]): List of column names to fill missing values
        
    Returns:
        pd.DataFrame: Dataframe with missing values filled
    """
    df_copy = df.copy()
    
    for col in columns:
        if col in df_copy.columns:
            if df_copy[col].dtype in ['int64', 'float64']:
                median_val = df_copy[col].median()
                df_copy[col].fillna(median_val, inplace=True)
                print(f"Filled {col} missing values with median: {median_val}")
            else:
                print(f"Skipping {col}: not a numeric column")
    
    return df_copy


def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """
    Drop columns that have more than the threshold proportion of missing values.
    
    Args:
        df (pd.DataFrame): Input dataframe
        threshold (float): Threshold proportion (0-1) for dropping columns
        
    Returns:
        pd.DataFrame: Dataframe with high-missing columns removed
    """
    df_copy = df.copy()
    
    # Calculate missing proportion for each column
    missing_prop = df_copy.isnull().sum() / len(df_copy)
    
    # Identify columns to drop
    cols_to_drop = missing_prop[missing_prop > threshold].index.tolist()
    
    if cols_to_drop:
        print(f"Dropping columns with >{threshold*100}% missing values: {cols_to_drop}")
        df_copy = df_copy.drop(columns=cols_to_drop)
    else:
        print(f"No columns exceed {threshold*100}% missing value threshold")
    
    return df_copy


def normalize_data(df: pd.DataFrame, columns: List[str], method: str = 'min-max') -> pd.DataFrame:
    """
    Normalize specified columns using min-max scaling.
    
    Args:
        df (pd.DataFrame): Input dataframe
        columns (List[str]): List of column names to normalize
        method (str): Normalization method (currently only 'min-max' supported)
        
    Returns:
        pd.DataFrame: Dataframe with normalized columns
    """
    df_copy = df.copy()
    
    for col in columns:
        if col in df_copy.columns and df_copy[col].dtype in ['int64', 'float64']:
            min_val = df_copy[col].min()
            max_val = df_copy[col].max()
            
            if max_val != min_val:  # Avoid division by zero
                df_copy[col] = (df_copy[col] - min_val) / (max_val - min_val)
                print(f"Normalized {col}: min={min_val}, max={max_val}")
            else:
                print(f"Skipping {col}: all values are the same ({min_val})")
        else:
            print(f"Skipping {col}: not a numeric column or doesn't exist")
    
    return df_copy
