from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"

RAW_DIR = DATA_DIR / "raw"
CURATED_DIR = DATA_DIR / "curated"
FEATURES_DIR = DATA_DIR / "features"
RFM_DIR = DATA_DIR / "rfm"

RAW_FILE = RAW_DIR / "online_retail_II.csv"
CURATED_FILE = CURATED_DIR / "cleaned_retail_data.parquet"
FEATURES_FILE = FEATURES_DIR / "featured_retail_data.parquet"
RFM_FILE = RFM_DIR / "rfm_retail_data.parquet"
SEG_RES_FILE = RFM_DIR / "rfm_seg_results.parquet"

