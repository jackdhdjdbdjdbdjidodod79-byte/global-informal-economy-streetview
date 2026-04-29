"""
Step 05: Statistical summary.

This script performs a simple demonstration of the statistical workflow:
1. descriptive statistics of vendor activity;
2. city-level ranking;
3. example association between vendor activity and latitude.

The full manuscript includes broader statistical analyses with environmental
and socioeconomic covariates.
"""

from pathlib import Path
import pandas as pd
from scipy.stats import spearmanr


BASE_DIR = Path(__file__).resolve().parents[1]
IMAGE_INPUT = BASE_DIR / "outputs" / "03_image_vendor_scores.csv"
CITY_INPUT = BASE_DIR / "outputs" / "04_city_vendor_index.csv"
OUTPUT = BASE_DIR / "outputs" / "05_statistical_summary.txt"


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    if not IMAGE_INPUT.exists():
        raise FileNotFoundError(
            f"Input file not found: {IMAGE_INPUT}. "
            "Please run 03_clip_vendor_scoring.py first."
        )

    if not CITY_INPUT.exists():
        raise FileNotFoundError(
            f"Input file not found: {CITY_INPUT}. "
            "Please run 04_aggregate_street_city.py first."
        )

    img = pd.read_csv(IMAGE_INPUT)
    city = pd.read_csv(CITY_INPUT)

    img["vendor_score"] = pd.to_numeric(img["vendor_score"], errors="coerce")
    img["lat"] = pd.to_numeric(img["lat"], errors="coerce")
    img = img.dropna(subset=["vendor_score", "lat"]).copy()

    city["city_vendor_index"] = pd.to_numeric(
        city["city_vendor_index"], errors="coerce"
    )

    n_img = len(img)
    n_city = city["city_id"].nunique()
    n_street = img["street_id"].nunique()

    mean_score = img["vendor_score"].mean()
    std_score = img["vendor_score"].std()

    rho, p_value = spearmanr(img["vendor_score"], img["lat"])

    ranked = city.sort_values("city_vendor_index", ascending=False)[
        ["city_name", "country_iso2", "city_vendor_index", "n_img", "n_street"]
    ]

    summary = [
        "Demo statistical summary",
        "",
        f"Number of images: {n_img}",
        f"Number of cities: {n_city}",
        f"Number of streets: {n_street}",
        "",
        f"Mean image-level vendor score: {mean_score:.3f}",
        f"Standard deviation: {std_score:.3f}",
        "",
        "Example Spearman correlation:",
        "vendor_score vs latitude",
        f"rho = {rho:.3f}",
        f"p = {p_value:.4f}",
        "",
        "City-level vendor index ranking:",
    ]

    for _, row in ranked.iterrows():
        summary.append(
            f"- {row['city_name']} ({row['country_iso2']}): "
            f"{row['city_vendor_index']:.3f}, "
            f"n_img = {int(row['n_img'])}, "
            f"n_street = {int(row['n_street'])}"
        )

    summary.append("")
    summary.append(
        "This demo illustrates the computational workflow used in the manuscript: "
        "image-level CLIP-derived vendor scores are aggregated to street and city "
        "levels and then used for statistical analysis."
    )

    text = "\n".join(summary)

    OUTPUT.write_text(text, encoding="utf-8")

    print(text)
    print(f"\nStep 05 completed: statistical summary saved to {OUTPUT}")


if __name__ == "__main__":
    main()
