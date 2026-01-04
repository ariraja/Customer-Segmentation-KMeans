import pandas as pd
import numpy as np

def cyclic_encoding(df: pd.DataFrame, col: str, max_val: int):
    df[f"{col}_sin"] = np.sin(2 * np.pi * df[col] / max_val)
    df[f"{col}_cos"] = np.cos(2 * np.pi * df[col] / max_val)
    return df

def extract_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Feature Engineering

    ## Temporal features
    df['DayOfWeek'] = df['InvoiceDate'].dt.dayofweek
    df['Month'] = df['InvoiceDate'].dt.month

    df = cyclic_encoding(df, 'DayOfWeek', 7)
    df = cyclic_encoding(df, 'Month', 12)

    df['HighSeason'] = df['Month'].isin([9, 10, 11]).astype(int)
    df['IsWeekend'] = (df['DayOfWeek'] >= 5).astype(int)

    invoice_gaps = (
        df.groupby(['Customer ID', 'Invoice'])['InvoiceDate']
        .min()  # 1 date per invoice
        .reset_index()
        .sort_values(['Customer ID', 'InvoiceDate'])
    )
    invoice_gaps['DaysSincePrevInvoice'] = (
        invoice_gaps.groupby('Customer ID')['InvoiceDate']
        .diff()
        .dt.days
    )

    df = df.merge(
        invoice_gaps[['Customer ID', 'Invoice', 'DaysSincePrevInvoice']],
        on=['Customer ID', 'Invoice'],
        how='left'
    )

    return df