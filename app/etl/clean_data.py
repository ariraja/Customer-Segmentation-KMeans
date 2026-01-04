import pandas as pd

def clean_retail_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df = df.dropna(subset=['Customer ID'])
    df['Description'] = df['Description'].fillna("NA").str.lower().str.strip()
    df = df.drop_duplicates()

    # Stock codes :
    # #  TEST       :  Test transactions
    # #  BANK CHARGES : Bank fees
    # #  POST       : Frais de port/ shipping/ postage
    # #  D          : Discount
    # #  DOT        : DOTCOM / e-commerce operation items
    # #  CRUK       : Donations to charity (Cancer Research UK)
    # #  M, ADJUST, ADJUST2  : Manual adjustments
    # #  TEST001, TEST002 : Additional test transactions
    exclude_stock_code_list = ['TEST', 'BANK CHARGES', 'POST', 'D', 'DOT',
                               'CRUK', 'M', 'ADJUST', 'ADJUST2', 'TEST001', 'TEST002']
    df = df[~df['StockCode'].astype(str).isin(exclude_stock_code_list)]

    # Delete gifts items
    df = df.loc[df['Price'] > 0]

    # df_returns = df[df['Quantity'] < 0]
    # Exclude returns in the analysis
    df = df[df['Quantity'] > 0]

    return df