
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="FIRELENS | Public Mode",
    page_icon="🔥",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = (
    BASE_DIR / "data" / "processed"
    / "regional_detections_exploratory.csv"
)

st.markdown("""
<style>
.stApp {
    background-color: #0b1120;
    color: #f1f5f9;
}
.hero {
    padding: 30px;
    border-radius: 18px;
    background: linear-gradient(120deg, #172554, #7c2d12, #991b1b);
    margin-bottom: 24px;
}
.hero h1 {
    color: white;
    font-size: 40px;
}
.hero p {
    color: #e2e8f0;
    font-size: 16px;
}
.info-card {
    background: #172033;
    border: 1px solid #334155;
    padding: 18px;
    border-radius: 12px;
    min-height: 120px;
}
.info-card h4 {
    color: #fb923c;
}
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data(path):
    data = pd.read_csv(path)

    data["acquisition_date"] = pd.to_datetime(
        data["acquisition_date"], errors="coerce"
    )

    for col in ["latitude", "longitude", "frp"]:
        data[col] = pd.to_numeric(data[col], errors="coerce")

    return data


st.sidebar.title("🔥 FIRELENS")
st.sidebar.caption("Public Mode")
st.sidebar.info(
    "Untuk masyarakat umum, pelajar, "
    "dan siapa saja yang ingin memahami data kebakaran."
)

st.markdown("""
<div class="hero">
    <h1>🔥 Welcome to FIRELENS</h1>
    <p>
        Understanding wildfire activity through
        satellite data.
    </p>
    <p>
        Explore fire detection patterns in Riau and
        Central Kalimantan, Indonesia.
    </p>
</div>
""", unsafe_allow_html=True)

if not DATA_PATH.exists():
    st.error("Dataset tidak ditemukan.")
    st.stop()

try:
    df = load_data(DATA_PATH)
except Exception as error:
    st.error(f"Unable to load dataset: {error}")
    st.stop()

required = [
    "study_region_label",
    "sensor",
    "acquisition_date",
    "latitude",
    "longitude",
    "frp"
]

missing = [col for col in required if col not in df.columns]

if missing:
    st.error("Missing columns: " + ", ".join(missing))
    st.stop()

st.subheader("Wildfire Data at a Glance")

col1, col2, col3 = st.columns(3)

col1.metric("Satellite Detection Records", f"{len(df):,}")
col2.metric("Study Regions", df["study_region_label"].nunique())
col3.metric("Satellite Sensors", df["sensor"].nunique())

st.caption(
    "These numbers represent satellite detection records, "
    "not the number of unique wildfire events."
)

st.divider()

st.subheader("Where were fire detections recorded?")

region_counts = (
    df["study_region_label"]
    .value_counts()
    .rename_axis("Region")
    .reset_index(name="Detections")
)

fig_region = px.bar(
    region_counts,
    x="Region",
    y="Detections",
    color="Region",
    text="Detections",
    color_discrete_sequence=["#f97316", "#ef4444"]
)

fig_region.update_layout(
    template="plotly_dark",
    showlegend=False
)

st.plotly_chart(fig_region, use_container_width=True)

st.subheader("How did activity change over time?")

monthly = df.dropna(subset=["acquisition_date"]).copy()

monthly["Month"] = (
    monthly["acquisition_date"].dt.to_period("M").astype(str)
)

monthly_counts = (
    monthly.groupby("Month")
    .size()
    .reset_index(name="Detections")
)

fig_monthly = px.bar(
    monthly_counts,
    x="Month",
    y="Detections",
    text="Detections",
    color="Detections",
    color_continuous_scale="Oranges"
)

fig_monthly.update_layout(template="plotly_dark")

st.plotly_chart(fig_monthly, use_container_width=True)

st.subheader("Explore hotspot locations")

map_data = df.dropna(
    subset=["latitude", "longitude"]
).copy()

map_data = map_data[
    map_data["latitude"].between(-90, 90)
    & map_data["longitude"].between(-180, 180)
]

if not map_data.empty:
    fig_map = px.scatter_map(
        map_data,
        lat="latitude",
        lon="longitude",
        color="study_region_label",
        hover_data=["sensor", "frp", "acquisition_date"],
        zoom=4,
        height=500,
        map_style="open-street-map"
    )

    st.plotly_chart(fig_map, use_container_width=True)
else:
    st.info("No valid geographic coordinates available.")

st.divider()

st.subheader("What does this information mean?")

a, b = st.columns(2)

with a:
    st.markdown("""
    <div class="info-card">
        <h4>Satellite Detection</h4>
        A satellite detection indicates a location
        where a sensor identified a possible fire-related
        thermal anomaly.
    </div>
    """, unsafe_allow_html=True)

with b:
    st.markdown("""
    <div class="info-card">
        <h4>Fire Radiative Power (FRP)</h4>
        FRP is an estimate of the radiative energy
        released by a detected fire at the observation time.
    </div>
    """, unsafe_allow_html=True)

st.subheader("About this research")

st.write("""
FIRELENS explores NASA FIRMS satellite fire detection
records from MODIS and VIIRS in Riau and Central
Kalimantan during August–October 2024.

The platform is designed to make satellite-derived
fire information easier to explore and understand.
""")

with st.expander("Important information and limitations"):
    st.write("""
    - The dataset represents satellite detection records,
      not confirmed unique wildfire events.
    - The observation period is historical: August–October 2024.
    - Study-region boundaries are approximate.
    - Satellite detections are not a real-time emergency alert.
    - FRP does not directly measure total burned area or damage.
    - Map tiles require an internet connection.
    """)

st.caption(
    "FIRELENS | Public Mode | Historical exploratory data | 2024"
)
