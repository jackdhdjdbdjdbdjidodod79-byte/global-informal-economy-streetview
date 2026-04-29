"""
Step 04: Aggregate image-level vendor scores to street and city levels.

This script reproduces the core aggregation logic used in the manuscript:
image-level CLIP vendor scores are summarized at the street level and then
aggregated to city-level vendor activity indices.
"""

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
INPUT = BASE_DIR / "outputs" / "03_image_vendor_scores.csv"
STREET_OUTPUT = BASE_DIR / "outputs" / "04_street_vendor_index.csv"
CITY_OUTPUT = BASE_DIR / "outputs" / "04_city_vendor_index.csv"


def top_fraction_mean(series: pd.Series, fraction: float = 0.2) -> float:
    """Mean of the highest fraction of vendor scores."""
    n = max(1, int(len(series) * fraction))
    return series.sort_values(ascending=False).head(n).mean()


def compute_street_index(df: pd.DataFrame) -> pd.DataFrame:
    street = (
        df.groupby(
            ["city_id", "country_iso2", "city_name", "city_role", "street_id"],
            as_index=False
        )
        .agg(
            n_img=("image_id", "count"),
            street_vendor_score_mean=("vendor_score", "mean"),
            street_vendor_detect_rate=("vendor_detected", "mean"),
            street_vendor_top20_mean=("vendor_score", top_fraction_mean),
        )
    )

    # Demonstration formula.
    # In the manuscript, use the exact index formula described in Methods.
    street["street_vendor_index"] = (
        0.5 * street["street_vendor_score_mean"]
        + 0.3 * street["street_vendor_detect_rate"]
        + 0.2 * street["street_vendor_top20_mean"]
    )

    return street


def compute_city_index(street: pd.DataFrame) -> pd.DataFrame:
    city = (
        street.groupby(
            ["city_id", "country_iso2", "city_name", "city_role"],
            as_index=False
        )
        .agg(
            n_street=("street_id", "nunique"),
            n_img=("n_img", "sum"),
            city_vendor_score_mean=("street_vendor_score_mean", "mean"),
            city_vendor_detect_rate=("street_vendor_detect_rate", "mean"),
            city_vendor_top20_mean=("street_vendor_top20_mean", "mean"),
            city_vendor_index=("street_vendor_index", "mean"),
        )
    )

    return city


def main():
    STREET_OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    if not INPUT.exists():
        raise FileNotFoundError(
            f"Input file not found: {INPUT}. "
            "Please run 03_clip_vendor_scoring.py first."
        )

    df = pd.read_csv(INPUT)

    df["vendor_score"] = pd.to_numeric(df["vendor_score"], errors="coerce")
    df["vendor_detected"] = df["vendor_detected"].astype(bool)
    df = df.dropna(subset=["vendor_score"]).copy()

    street = compute_street_index(df)
    city = compute_city_index(street)

    street.to_csv(STREET_OUTPUT, index=False)
    city.to_csv(CITY_OUTPUT, index=False)

    print("Step 04 completed: street- and city-level aggregation finished.")
    print(f"Street-level output saved to: {STREET_OUTPUT}")
    print(f"City-level output saved to: {CITY_OUTPUT}")
    print("\nCity-level demo results:")
    print(city[["city_name", "city_vendor_index", "n_img", "n_street"]])


if __name__ == "__main__":
    main()
