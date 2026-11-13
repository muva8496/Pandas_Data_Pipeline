import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans column names, coerces data types, and removes malformed rows."""
    logging.info("Starting data cleaning process...")
    df = df.copy()
    
    # 1. Standardize column names (strip spaces, lowercase, underscores)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    
    # 2. Coerce dates if date column exists
    date_cols = [c for c in df.columns if 'date' in c]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')
        
    # 3. Coerce numeric columns (e.g., amount, quantity)
    if 'amount' in df.columns:
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce').fillna(0.0)
    if 'quantity' in df.columns:
        df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').fillna(0).astype(int)
        
    # 4. Drop rows missing critical IDs
    if 'transaction_id' in df.columns:
        df = df.dropna(subset=['transaction_id'])
        
    logging.info(f"Cleaning complete. Rows remaining: {len(df)}")
    return df