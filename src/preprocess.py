# preprocess.py
import pandas as pd

def preprocess_data(df, target_col="total_person_income"):
    """Clean the dataset:
       1. Remove duplicate rows (ignoring target_col)
       2. Drop columns with >40% NaNs
       3. Drop rows with any remaining NaNs
    """
    # a) Remove duplicates ignoring the target column
    df_no_dup = df.drop_duplicates(subset=df.columns.difference([target_col]))
    
    # b) Drop columns with >40% missing values
    threshold = 0.4
    na_ratio = df_no_dup.isna().mean()
    df_reduced = df_no_dup.drop(columns=na_ratio[na_ratio > threshold].index)
    
    # c) Drop remaining rows with any missing values
    df_clean = df_reduced.dropna()
    
    return df_clean
