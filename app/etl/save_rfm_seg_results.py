import pandas as pd
import logging
from run_rfm_segmentation import run_segmentation
from customerSegementation.app.config.settings import RFM_FILE, SEG_RES_FILE

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Loading RFM data...")
    if not RFM_FILE.exists():
        raise FileNotFoundError(f"RFM data not found at: {RFM_FILE}")

    df = pd.read_parquet(RFM_FILE)

    logging.info("Building segmentation results from RFM data...")
    rfm_df = run_segmentation(df)

    SEG_RES_FILE.parent.mkdir(parents=True, exist_ok=True)

    logging.info("Saving segmentation results...")
    rfm_df.to_parquet(SEG_RES_FILE, index=False)

    logging.info(f"Done! RFM segmentation results saved at: {SEG_RES_FILE}")

if __name__ == "__main__":
    main()






