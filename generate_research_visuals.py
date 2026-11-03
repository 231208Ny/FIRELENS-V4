
from pathlib import Path
import pandas as pd
import plotly.express as px

# ==========================================
# FIRELENS - RESEARCH TABLES AND VISUALS
# ==========================================

ROOT = Path(__file__).resolve().parent

DATA = (
    ROOT / "data" / "processed" /
    "regional_detections_exploratory.csv"
)

OUTPUT = ROOT / "research_outputs"
CHARTS = OUTPUT / "charts"

OUTPUT.mkdir(exist_ok=True)
CHARTS.mkdir(exist_ok=True)

print("=" * 55)
print("FIRELENS RESEARCH VISUALIZATION GENERATOR")
print("=" * 55)

# 1. Load dataset
if not DATA.exists():
    raise FileNotFoundError(f"Dataset not found: {DATA}")

df = pd.read_csv(DATA)

required = [
    "study_region_label",
    "sensor",
    "acquisition_date",
    "frp",
]

missing = [col for col in required if col not in df.columns]

if missing:
    raise ValueError(f"Missing required columns: {missing}")

df["acquisition_date"] = pd.to_datetime(
    df["acquisition_date"], errors="coerce"
)

df["frp"] = pd.to_numeric(df["frp"], errors="coerce")

df = df.dropna(
    subset=["study_region_label", "sensor", "acquisition_date"]
).copy()

df["month"] = df["acquisition_date"].dt.to_period("M").astype(str)
df["date"] = df["acquisition_date"].dt.date

print(f"\nDataset records loaded: {len(df):,}")

# 2. Regional distribution
regional = (
    df.groupby("study_region_label")
    .size()
    .reset_index(name="detection_records")
)

regional["percentage"] = (
    regional["detection_records"] / len(df) * 100
).round(2)

regional.to_csv(
    OUTPUT / "table_01_regional_distribution.csv",
    index=False
)

# 3. Sensor distribution
sensor = (
    df.groupby("sensor")
    .size()
    .reset_index(name="detection_records")
)

sensor["percentage"] = (
    sensor["detection_records"] / len(df) * 100
).round(2)

sensor.to_csv(
    OUTPUT / "table_02_sensor_distribution.csv",
    index=False
)

# 4. Monthly detection distribution
monthly = (
    df.groupby(["study_region_label", "month"])
    .size()
    .reset_index(name="detection_records")
    .sort_values(["study_region_label", "month"])
)

monthly.to_csv(
    OUTPUT / "table_03_monthly_distribution.csv",
    index=False
)

# 5. FRP descriptive statistics
frp = (
    df.dropna(subset=["frp"])
    .groupby("study_region_label")["frp"]
    .agg(
        count="count",
        mean="mean",
        median="median",
        std="std",
        minimum="min",
        maximum="max",
    )
    .reset_index()
    .round(3)
)

frp.to_csv(
    OUTPUT / "table_04_frp_statistics.csv",
    index=False
)

# 6. Daily detection peaks
daily = (
    df.groupby(["study_region_label", "date"])
    .size()
    .reset_index(name="detection_records")
)

daily_peaks = (
    daily.sort_values(
        ["study_region_label", "detection_records"],
        ascending=[True, False]
    )
    .groupby("study_region_label")
    .head(10)
)

daily_peaks.to_csv(
    OUTPUT / "table_05_daily_peaks.csv",
    index=False
)

# 7. Regional distribution chart
fig1 = px.bar(
    regional,
    x="study_region_label",
    y="detection_records",
    color="study_region_label",
    title="Satellite Fire Detection Records by Study Region",
    labels={
        "study_region_label": "Study Region",
        "detection_records": "Detection Records",
    },
    text="detection_records",
)

fig1.write_html(
    CHARTS / "chart_01_regional_distribution.html"
)

# 8. Sensor distribution chart
fig2 = px.pie(
    sensor,
    names="sensor",
    values="detection_records",
    title="Detection Records by Satellite Sensor",
    hole=0.35,
)

fig2.write_html(
    CHARTS / "chart_02_sensor_distribution.html"
)

# 9. Monthly trends chart
fig3 = px.bar(
    monthly,
    x="month",
    y="detection_records",
    color="study_region_label",
    barmode="group",
    title="Monthly Satellite Fire Detection Trends",
    labels={
        "month": "Month",
        "detection_records": "Detection Records",
        "study_region_label": "Study Region",
    },
    text="detection_records",
)

fig3.write_html(
    CHARTS / "chart_03_monthly_trends.html"
)

# 10. FRP distribution chart
fig4 = px.histogram(
    df.dropna(subset=["frp"]),
    x="frp",
    color="study_region_label",
    marginal="box",
    barmode="overlay",
    opacity=0.65,
    title="Fire Radiative Power Distribution by Region",
    labels={
        "frp": "Fire Radiative Power (MW)",
        "study_region_label": "Study Region",
    },
)

fig4.write_html(
    CHARTS / "chart_04_frp_distribution.html"
)

# 11. Summary
summary = [
    f"Total analyzed records: {len(df):,}",
    f"Regional groups: {df['study_region_label'].nunique()}",
    f"Satellite sensors: {df['sensor'].nunique()}",
    f"Date range: {df['acquisition_date'].min().date()} "
    f"to {df['acquisition_date'].max().date()}",
    f"FRP observations: {df['frp'].notna().sum():,}",
]

(OUTPUT / "research_summary.txt").write_text(
    "\n".join(summary),
    encoding="utf-8"
)

print("\nTABLES CREATED:")
for file in sorted(OUTPUT.glob("*.csv")):
    print(" -", file.name)

print("\nCHARTS CREATED:")
for file in sorted(CHARTS.glob("*.html")):
    print(" -", file.name)

print("\nSUMMARY:")
for line in summary:
    print(line)

print("\n" + "=" * 55)
print("RESEARCH OUTPUT GENERATION COMPLETED")
print("Output folder:", OUTPUT)
print("=" * 55)
