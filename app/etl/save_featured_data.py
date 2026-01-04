import pandas as pd
import logging
from extract_features import extract_features
from customerSegementation.app.config.settings import CURATED_FILE, FEATURES_FILE

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Loading cleaned dataset...")
    if not CURATED_FILE.exists():
        raise FileNotFoundError(f"Cleaned dataset not found at: {CURATED_FILE}")

    df = pd.read_parquet(CURATED_FILE)

    logging.info("Building features from cleaned dataset...")
    df_features = extract_features(df)

    FEATURES_FILE.parent.mkdir(parents=True, exist_ok=True)

    logging.info("Saving featured dataset...")
    df_features.to_parquet(FEATURES_FILE, index=False)

    logging.info(f"Done! Featured file saved at: {FEATURES_FILE}")

if __name__ == "__main__":
    main()






