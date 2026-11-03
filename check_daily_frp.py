import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FILE = BASE_DIR / "data" / "processed" / "daily_frp_temporal_summary.csv"

df = pd.read_csv(FILE)

for region in df["study_region"].unique():

    data = df[df["study_region"] == region].copy()

    print("\n================================")
    print("REGION:", region)
    print("================================")

    print("\nHighest daily mean FRP:")
    print(
        data.loc[data["mean_frp"].idxmax()].to_string()
    )

    print("\nHighest daily median FRP:")
    print(
        data.loc[data["median_frp"].idxmax()].to_string()
    )

    print("\nHighest daily detection records:")
    print(
        data.loc[data["detection_records"].idxmax()].to_string()
    )

    print("\nOverall daily statistics:")
    print(
        data[[
            "detection_records",
            "mean_frp",
            "median_frp",
            "total_frp"
        ]].describe().round(2)
    )
