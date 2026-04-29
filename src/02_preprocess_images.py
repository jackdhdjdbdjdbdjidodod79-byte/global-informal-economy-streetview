"""
Step 02: Preprocess image metadata.

This demo performs basic quality control:
1. validates coordinates;
2. validates timestamps;
3. removes duplicate image records;
4. keeps records suitable for image-level vendor scoring.
"""

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
INPUT = BASE_DIR / "outputs" / "01_metadata.csv"
RAW_WITH_SCORE = BASE_DIR / "demo_data" / "demo_clip_scores.csv"
OUTPUT = BASE_DIR / "outputs" / "02_clean_records.csv"


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    if not INPUT.exists():
        raise FileNotFoundError(
            f"Input file not found: {INPUT}. "
            "Please run 01_download_mapillary_metadata.py first."
        )

    metadata = pd.read_csv(INPUT)
    raw = pd.read_csv(RAW_WITH_SCORE)

    # Merge back vendor_score for downstream demo scoring.
    # In the full workflow, vendor_score would be generated from CLIP inference.
    df = metadata.merge(
        raw[["image_id", "vendor_score"]],
        on="image_id",
        how="left"
    )

    df["lat"] = pd.to_numeric(df["lat"], errors="coerce")
    df["lon"] = pd.to_numeric(df["lon"], errors="coerce")
    df["captured_at"] = pd.to_datetime(df["captured_at"], errors="coerce")
    df["vendor_score"] = pd.to_numeric(df["vendor_score"], errors="coerce")

    clean = df.dropna(
        subset=["lat", "lon", "captured_at", "vendor_score"]
    ).copy()

    clean = clean.drop_duplicates(subset=["image_id"])

    clean.to_csv(OUTPUT, index=False)

    print("Step 02 completed: metadata preprocessing finished.")
    print(f"Original records: {len(df)}")
    print(f"Clean records: {len(clean)}")
    print(f"Saved to: {OUTPUT}")


if __name__ == "__main__":
    main()
