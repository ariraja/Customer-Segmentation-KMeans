import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler

def scale_features(df: pd.DataFrame) -> np.ndarray:
    X = df[['Recency', 'Frequency', 'Monetary']].copy()
    X = np.log1p(X)
    scaler = RobustScaler()
    return scaler.fit_transform(X)