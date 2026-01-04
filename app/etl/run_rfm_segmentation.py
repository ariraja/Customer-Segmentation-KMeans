import pandas as pd
from scale_features import scale_features
from sklearn.cluster import KMeans

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    """
    df = df.copy()

    # One-shot customer have a null AvgGap, so we suppose they have the maximum AvgGap
    df['AvgGap'] = df['AvgGap'].fillna(df['AvgGap'].max())
    return df


def run_segmentation(df: pd.DataFrame, n_clusters: int = 4) -> pd.DataFrame:
    df = preprocess_data(df)
    X = scale_features(df)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X)
    df['Cluster'] = kmeans.labels_

    return df