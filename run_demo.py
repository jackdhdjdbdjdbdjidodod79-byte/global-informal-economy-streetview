import os
import pandas as pd

INPUT = "demo_data/demo_clip_scores.csv"
OUTPUT = "outputs/demo_vendor_index.csv"

os.makedirs("outputs", exist_ok=True)

df = pd.read_csv(INPUT)

required = {"city_id", "street_id", "image_id", "vendor_score"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing columns: {missing}")

street = (
    df.groupby(["city_id", "street_id"], as_index=False)
    .agg(
        n_img=("image_id", "count"),
        street_vendor_score_mean=("vendor_score", "mean"),
        street_vendor_detect_rate=("vendor_score", lambda x: (x > 0.5).mean()),
        street_vendor_top20_mean=("vendor_score", lambda x: x.sort_values(ascending=False).head(max(1, int(len(x)*0.2))).mean())
    )
)

street["street_vendor_index"] = (
    0.5 * street["street_vendor_score_mean"] +
    0.3 * street["street_vendor_detect_rate"] +
    0.2 * street["street_vendor_top20_mean"]
)

city = (
    street.groupby("city_id", as_index=False)
    .agg(
        n_street=("street_id", "count"),
        city_vendor_index=("street_vendor_index", "mean")
    )
)

street.to_csv(OUTPUT, index=False)
print(f"Demo completed. Output saved to: {OUTPUT}")
print(city)
