import os
import pandas as pd

# ======================
# 1. 自动定位数据路径（避免路径报错）
# ======================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "demo_data", "demo_clip_scores.csv")

print("Loading data from:", DATA_PATH)

# ======================
# 2. 读取数据
# ======================
df = pd.read_csv(DATA_PATH)

print("\nData loaded successfully!")
print(f"Total records: {len(df)}")

# ======================
# 3. 基本统计（模拟论文核心步骤）
# ======================
print("\n=== Basic Statistics ===")

# 按城市聚合 vendor score
city_stats = df.groupby("city_id")["vendor_score"].agg(["mean", "count"]).reset_index()
city_stats = city_stats.rename(columns={"mean": "city_vendor_index"})

print("\nCity-level vendor index:")
print(city_stats)

# ======================
# 4. 全球层面统计
# ======================
print("\n=== Global Summary ===")

global_mean = df["vendor_score"].mean()
global_std = df["vendor_score"].std()

print(f"Global mean vendor score: {global_mean:.3f}")
print(f"Global std: {global_std:.3f}")

# ======================
# 5. 简单相关性（模拟论文逻辑）
# ======================
print("\n=== Example Correlation ===")

# 用纬度模拟一个“环境变量”
if "lat" in df.columns:
    corr = df["vendor_score"].corr(df["lat"])
    print(f"Correlation between vendor score and latitude: {corr:.3f}")
else:
    print("Latitude not found, skip correlation.")

# ======================
# 6. 输出一个简单结果文件（增强复现性）
# ======================
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

out_path = os.path.join(OUTPUT_DIR, "demo_city_stats.csv")
city_stats.to_csv(out_path, index=False)

print("\nSaved demo output to:", out_path)

print("\n=== Demo run completed successfully! ===")
