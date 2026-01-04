import kagglehub
import shutil
from pathlib import Path

def download_online_retail_data(target_folder="../data/raw"):
    target_folder = Path(target_folder)
    target_folder.mkdir(parents=True, exist_ok=True)
    path = kagglehub.dataset_download("mashlyn/online-retail-ii-uci")

    local_path = Path(path)

    for file in local_path.glob("*.csv"):
        shutil.copy(file, target_folder)
        print(f"Copied: {file.name}")

    print("\nDownload complete. Files available in data/raw/")

if __name__ == "__main__":
    download_online_retail_data()