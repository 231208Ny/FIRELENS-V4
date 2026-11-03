import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

FILE = (
    BASE_DIR / "data" / "processed"
    / "spatial_cluster_riau_20240826.csv"
)

df = pd.read_csv(FILE)

# Group detections by satellite and observation time
summary = (
    df.groupby(["satellite", "acquisition_time_hhmm"])
    .agg(
        detection_records=("frp", "count"),
        mean_frp=("frp", "mean"),
        median_frp=("frp", "median"),
        maximum_frp=("frp", "max"),
        mean_distance_km=("distance_km", "mean")
    )
    .reset_index()
    .round(2)
)

print("\nSPATIAL CLUSTER - TIME ANALYSIS")
print("Date: 2024-08-26")
print("\nSummary by satellite and observation time:")

print(summary.to_string(index=False))

# Save summary
output = (
    BASE_DIR / "data" / "processed"
    / "spatial_cluster_time_summary.csv"
)

summary.to_csv(output, index=False)

print("\nSaved:", output)
