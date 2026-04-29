import pandas as pd

# =========================
# Load demo data
# =========================
df = pd.read_csv("demo_data/demo_clip_scores.csv")

print("=== Demo dataset loaded ===")
print(df.head(), "\n")

# =========================
# Basic statistics
# =========================
print("=== Basic statistics ===")

print(f"Number of images: {len(df)}")
print(f"Number of cities: {df['city_id'].nunique()}")
print(f"Number of streets: {df['street_id'].nunique()}")

mean_score = df["vendor_score"].mean()
print(f"Mean vendor score: {mean_score:.3f}")

# =========================
# Street-level aggregation
# =========================
street_stats = df.groupby("street_id")["vendor_score"].mean().reset_index()

print("\n=== Street-level aggregation ===")
print(street_stats.head())

# =========================
# City-level aggregation
# =========================
city_stats = df.groupby("city_name")["vendor_score"].mean().reset_index()

print("\n=== City-level aggregation ===")
print(city_stats)

# =========================
# Simple correlation demo
# =========================
if "lat" in df.columns:
    corr = df["vendor_score"].corr(df["lat"], method="spearman")
    print("\n=== Example correlation ===")
    print(f"Spearman correlation (vendor_score vs latitude): {corr:.3f}")

print("\n=== Demo completed successfully ===")
