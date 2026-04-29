"""
Step 03: Generate image-level vendor scores.

In the full study, this step applies a CLIP vision-language model to compute
semantic similarity between each street-view image and vendor-related prompts.

For this demo, precomputed CLIP-derived vendor_score values are used to
demonstrate the expected data structure and scoring workflow.
"""

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
INPUT = BASE_DIR / "outputs" / "02_clean_records.csv"
OUTPUT = BASE_DIR / "outputs" / "03_image_vendor_scores.csv"

DETECTION_THRESHOLD = 0.5


def classify_vendor_activity(score: float) -> str:
    if score >= 0.7:
        return "high"
    if score >= 0.5:
        return "moderate"
    return "low"


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    if not INPUT.exists():
        raise FileNotFoundError(
            f"Input file not found: {INPUT}. "
            "Please run 02_preprocess_images.py first."
        )

    df = pd.read_csv(INPUT)

    required = [
        "city_id", "country_iso2", "city_name", "city_role",
        "street_id", "image_id", "lat", "lon", "captured_at",
        "vendor_score"
    ]

    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df["vendor_score"] = pd.to_numeric(df["vendor_score"], errors="coerce")
    df = df.dropna(subset=["vendor_score"]).copy()

    df["vendor_detected"] = df["vendor_score"] >= DETECTION_THRESHOLD
    df["vendor_activity_class"] = df["vendor_score"].apply(classify_vendor_activity)

    output_cols = required + ["vendor_detected", "vendor_activity_class"]
    scored = df[output_cols].copy()

    scored.to_csv(OUTPUT, index=False)

    print("Step 03 completed: image-level vendor scoring finished.")
    print("Note: this demo uses precomputed CLIP-derived vendor_score values.")
    print(f"Images scored: {len(scored)}")
    print(f"Detection threshold: {DETECTION_THRESHOLD}")
    print(f"Saved to: {OUTPUT}")


if __name__ == "__main__":
    main()
