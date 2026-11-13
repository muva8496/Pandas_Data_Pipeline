import pandas as pd
import numpy as np
import logging

def apply_business_transformations(df: pd.DataFrame) -> pd.DataFrame:
    """Applies business logic like total values, tiering, and status filtering."""
    logging.info("Applying business logic tranformations...")
    df = df.copy()

    # Example logic: Total transaction value
    if 'amount' in df.columns and 'quantity' in df.columns:
        df['total_value'] = df['amount'] * df['quantity']

    # Example logic: Customer/Transaction tiering
    if 'total_value' in df.columns:
        df['tier'] = np.select(
            [df['total_value'] > 1000, df['total_value'] > 500],
            ['Enterprise', 'Mid-Market'],
            default='Standard'
        )

    # Filter out test statuses if status column exists
    if 'status' in df.columns:
        df = df[df['status'].str.lower() != 'test']

    logging.info("Transformations applied successfully.")
    return df


