"""Build data/processed/gurgaon_properties_cleaned.csv from the raw feed.

Usage (from the repo root):
    python scripts/make_clean_dataset.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.cleaning import clean_raw_data, load_raw
from src.config import PROCESSED_DATA_PATH, RAW_DATA_PATH


def main() -> None:
    df = load_raw(RAW_DATA_PATH)
    cleaned, log = clean_raw_data(df)
    for line in log:
        print(f"  - {line}")
    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    cleaned.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"Saved {len(cleaned)} rows -> {PROCESSED_DATA_PATH}")


if __name__ == "__main__":
    main()
