"""
Step 01: Prepare Mapillary-style image metadata.

In the full study, image metadata were retrieved from the Mapillary API.
For this demo, we use the provided example dataset to reproduce the same
metadata structure required by the downstream workflow.
"""

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
INPUT = BASE_DIR / "demo_data" / "demo_clip_scores.csv"
OUTPUT = BASE_DIR / "outputs" / "01_metadata.csv"

REQUIRED_COLUMNS = [
    "city_id", "country_iso2", "city_name", "city_role",
    "street_id", "image_id", "lat", "lon", "captured_at"
]


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    if not INPUT.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT}")

    df = pd.read_csv(INPUT)

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required metadata columns: {missing}")

    metadata = df[REQUIRED_COLUMNS].copy()

    metadata.to_csv(OUTPUT, index=False)

    print("Step 01 completed: metadata prepared.")
    print(f"Input records: {len(df)}")
    print(f"Output records: {len(metadata)}")
    print(f"Saved to: {OUTPUT}")


if __name__ == "__main__":
    main()
