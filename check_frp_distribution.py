import pandas as pd
from pathlib import Path

file = Path("data/processed/regional_detections_exploratory.csv")
df = pd.read_csv(file)

for region in ["Central_Kalimantan_approx", "Riau_approx"]:
    print("\nREGION:", region)

    data = df[df["study_region"] == region]

    result = data.groupby("satellite")["frp"].describe()

    print(result.round(2))