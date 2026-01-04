import pandas as pd

def build_rfm_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["TotalPrice"] = df["Price"] * df["Quantity"]
    snapshot_date = df['InvoiceDate'].max()

    rfm_df = df.groupby('Customer ID').agg(
        Recency=('InvoiceDate', lambda x: (snapshot_date - x.max()).days),
        Frequency=('Invoice', 'nunique'),  # total number of invoices/checkout transactions
        Monetary=('TotalPrice', 'sum'),  # total spent amount
        CustomerLifespan=('InvoiceDate', lambda x: (x.max() - x.min()).days), # number of days between 1st and last purchase
        AvgGap=('DaysSincePrevInvoice', 'mean'),  # mean gap between invoices
        MedianGap=('DaysSincePrevInvoice', 'median'),
        MaxGap=('DaysSincePrevInvoice', 'max')
    ).reset_index()

    # Favorite month of purchase
    fav_month = (
        df.groupby(["Customer ID", "Month"])["Invoice"]
        .count()
        .reset_index()
        .sort_values(["Customer ID", "Invoice"], ascending=[True, False])
        .drop_duplicates("Customer ID")
        .rename(columns={"Month": "FavMonth"})
        [["Customer ID", "FavMonth"]]
    )

    rfm_df = rfm_df.merge(fav_month, on='Customer ID', how='left')

    # Purchase % in high season (Sep, Oct, Nov)
    rfm_df = rfm_df.merge(
        df.groupby("Customer ID")["HighSeason"]
        .mean()
        .rename("PctHighSeason"),
        on="Customer ID",
        how="left",
    )

    # Purchase % on weekends
    rfm_df = rfm_df.merge(
        df.groupby("Customer ID")["IsWeekend"]
        .mean()
        .rename("PctWeekend"),
        on="Customer ID",
        how="left",
    )

    return rfm_df