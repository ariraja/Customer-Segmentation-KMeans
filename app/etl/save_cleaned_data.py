import pandas as pd
import logging
from clean_data import clean_retail_data
from customerSegementation.app.config.settings import RAW_FILE, CURATED_FILE

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Loading raw dataset...")
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Raw dataset not found at: {RAW_FILE}")

    df = pd.read_csv(RAW_FILE)

    logging.info("Cleaning dataset...")
    df_clean = clean_retail_data(df)

    CURATED_FILE.parent.mkdir(parents=True, exist_ok=True)

    logging.info("Saving cleaned dataset...")
    df_clean.to_parquet(CURATED_FILE, index=False)

    logging.info(f"Done! Clean file saved at: {CURATED_FILE}")

if __name__ == "__main__":
    main()






