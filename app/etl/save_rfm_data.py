import pandas as pd
import logging
from build_rfm_features import build_rfm_features
from customerSegementation.app.config.settings import FEATURES_FILE, RFM_FILE

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Loading featured dataset...")
    if not FEATURES_FILE.exists():
        raise FileNotFoundError(f"Featured dataset not found at: {FEATURES_FILE}")

    df = pd.read_parquet(FEATURES_FILE)

    logging.info("Building RFM from featured dataset...")
    rfm_df = build_rfm_features(df)

    RFM_FILE.parent.mkdir(parents=True, exist_ok=True)

    logging.info("Saving RFM dataset...")
    rfm_df.to_parquet(RFM_FILE, index=False)

    logging.info(f"Done! RFM file saved at: {RFM_FILE}")

if __name__ == "__main__":
    main()






