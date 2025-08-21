# homework/homework6/src/cleaning.py
from __future__ import annotations
from typing import Iterable, Optional, Union
import pandas as pd
import numpy as np
from math import ceil

def drop_missing(df: pd.DataFrame,
                 threshold: Optional[Union[float,int]] = 0.5,
                 subset: Optional[Iterable[str]] = None) -> pd.DataFrame:
    out = df.copy()
    if threshold is None:
        return out.dropna(subset=subset)
    # how many columns are we measuring completeness over?
    ncols = len(subset) if subset is not None else out.shape[1]
    if isinstance(threshold, float) and 0 < threshold <= 1:
        req = max(1, ceil(threshold * ncols))
    elif isinstance(threshold, int) and threshold >= 1:
        req = threshold
    else:
        raise ValueError("threshold must be None, a float in (0,1], or an int >= 1")
    return out.dropna(thresh=req, subset=subset)

def fill_missing_median(df: pd.DataFrame,
                        columns: Optional[Iterable[str]] = None,
                        by: Optional[Iterable[str]] = None) -> pd.DataFrame:
    out = df.copy()
    if columns is None:
        columns = out.select_dtypes(include=[np.number]).columns.tolist()
    if by:
        med = out.groupby(list(by))[list(columns)].transform('median')
        out[list(columns)] = out[list(columns)].fillna(med)
    else:
        out[list(columns)] = out[list(columns)].fillna(out[list(columns)].median(numeric_only=True))
    return out

def normalize_data(df: pd.DataFrame,
                   columns: Optional[Iterable[str]] = None,
                   feature_range=(0.0, 1.0)) -> pd.DataFrame:
    out = df.copy()
    if columns is None:
        columns = out.select_dtypes(include=[np.number]).columns.tolist()
    a, b = feature_range
    for col in columns:
        cmin, cmax = out[col].min(), out[col].max()
        rng = cmax - cmin
        if pd.isna(rng) or rng == 0:
            continue
        out[col] = a + (out[col] - cmin) * (b - a) / rng
    return out
