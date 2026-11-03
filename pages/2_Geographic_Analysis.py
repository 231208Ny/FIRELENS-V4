
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# =====================================================
# FIRELENS V3 - GEOGRAPHIC ANALYSIS
# =====================================================

st.set_page_config(
    page_title="Geographic Analysis | FIRELENS",
    page_icon="🗺️",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "regional_detections_exploratory.csv"
)


# =====================================================
# STYLE
# =====================================================

st.markdown("""
<style>
    .stApp {
        background-color: #0b1120;
        color: #f1f5f9;
    }

    [data-testid="stSidebar"] {
        background-color: #111827;
    }

    .geo-header {
        background: linear-gradient(120deg, #172554, #7c2d12);
        padding: 25px;
        border-radius: 16px;
        margin-bottom: 20px;
    }

    .geo-header h1 {
        color: white;
        font-size: 34px;
    }

    .geo-header p {
        color: #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)


# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data(path):
    data = pd.read_csv(path)

    data["acquisition_date"] = pd.to_datetime(
        data["acquisition_date"],
        errors="coerce"
    )

    for col in ["latitude", "longitude", "frp"]:
        data[col] = pd.to_numeric(
            data[col],
            errors="coerce"
        )

    return data


st.title("🗺️ Geographic Analysis")

if not DATA_PATH.exists():
    st.error("Dataset tidak ditemukan.")
    st.code(str(DATA_PATH))
    st.stop()

try:
    df = load_data(DATA_PATH)
except Exception as error:
    st.error(f"Gagal membaca dataset: {error}")
    st.stop()


required_columns = [
    "study_region_label",
    "sensor",
    "acquisition_date",
    "latitude",
    "longitude",
    "frp"
]

missing = [
    col for col in required_columns
    if col not in df.columns
]

if missing:
    st.error(f"Kolom dataset tidak lengkap: {missing}")
    st.stop()


# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="geo-header">
    <h1>Geographic Distribution of Fire Detections</h1>
    <p>
        Explore the spatial distribution of satellite-based
        fire detections across Riau and Central Kalimantan.
    </p>
</div>
""", unsafe_allow_html=True)


# =====================================================
# FILTERS
# =====================================================

st.sidebar.header("Geographic Filters")

regions = sorted(
    df["study_region_label"].dropna().unique().tolist()
)

sensors = sorted(
    df["sensor"].dropna().unique().tolist()
)

selected_regions = st.sidebar.multiselect(
    "Study Region",
    options=regions,
    default=regions
)

selected_sensors = st.sidebar.multiselect(
    "Satellite Sensor",
    options=sensors,
    default=sensors
)

valid_dates = df["acquisition_date"].dropna()

if valid_dates.empty:
    st.error("Tidak ada tanggal pengamatan yang valid.")
    st.stop()

min_date = valid_dates.min().date()
max_date = valid_dates.max().date()

selected_dates = st.sidebar.date_input(
    "Observation Period",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if not selected_regions or not selected_sensors:
    st.warning("Pilih minimal satu wilayah dan satu sensor.")
    st.stop()

if isinstance(selected_dates, (tuple, list)):
    if len(selected_dates) == 2:
        start_date, end_date = selected_dates
    elif len(selected_dates) == 1:
        start_date = end_date = selected_dates[0]
    else:
        st.warning("Pilih periode tanggal pengamatan.")
        st.stop()
else:
    start_date = end_date = selected_dates


# =====================================================
# APPLY FILTERS
# =====================================================

filtered = df[
    df["study_region_label"].isin(selected_regions)
    & df["sensor"].isin(selected_sensors)
    & df["acquisition_date"].dt.date.between(
        start_date,
        end_date
    )
].copy()


# =====================================================
# VALID GEOGRAPHIC COORDINATES
# =====================================================

map_data = filtered.dropna(
    subset=["latitude", "longitude"]
).copy()

map_data = map_data[
    map_data["latitude"].between(-90, 90)
    & map_data["longitude"].between(-180, 180)
]


# =====================================================
# KPI
# =====================================================

st.subheader("Geographic Indicators")

k1, k2, k3, k4 = st.columns(4)

k1.metric(
    "Filtered Records",
    f"{len(filtered):,}"
)

k2.metric(
    "Valid Coordinates",
    f"{len(map_data):,}"
)

k3.metric(
    "Study Regions",
    filtered["study_region_label"].nunique()
)

mean_frp = filtered["frp"].mean()

k4.metric(
    "Mean FRP",
    f"{mean_frp:.2f} MW" if pd.notna(mean_frp) else "N/A"
)

st.caption(
    "Map points represent individual satellite detection records, "
    "not necessarily unique wildfire events."
)


# =====================================================
# INTERACTIVE MAP
# =====================================================

st.divider()
st.subheader("Interactive Fire Detection Map")

if map_data.empty:
    st.warning(
        "Tidak ada koordinat geografis valid untuk filter yang dipilih."
    )

else:
    color_options = ["study_region_label", "sensor"]

    if "satellite" in map_data.columns:
        color_options.append("satellite")

    selected_color = st.selectbox(
        "Color points by",
        options=color_options,
        format_func=lambda x: {
            "study_region_label": "Study Region",
            "sensor": "Sensor",
            "satellite": "Satellite"
        }.get(x, x)
    )

    hover_columns = {
        "study_region_label": True,
        "sensor": True,
        "acquisition_date": True,
        "frp": ":.2f",
        "latitude": ":.4f",
        "longitude": ":.4f"
    }

    if "satellite" in map_data.columns:
        hover_columns["satellite"] = True

    fig_map = px.scatter_map(
        map_data,
        lat="latitude",
        lon="longitude",
        color=selected_color,
        hover_data=hover_columns,
        zoom=5,
        height=650,
        opacity=0.65,
        color_discrete_sequence=[
            "#f97316",
            "#ef4444",
            "#fbbf24",
            "#38bdf8",
            "#a78bfa"
        ],
        map_style="open-street-map"
    )

    fig_map.update_traces(
        marker={"size": 7}
    )

    fig_map.update_layout(
        margin={"r": 0, "t": 10, "l": 0, "b": 0},
        legend_title_text="Detection Category"
    )

    st.plotly_chart(
        fig_map,
        use_container_width=True
    )


# =====================================================
# REGIONAL COMPARISON
# =====================================================

st.divider()
st.subheader("Detection Records by Study Region")

regional_summary = (
    filtered.groupby("study_region_label")
    .agg(
        total_detections=("sensor", "size"),
        mean_frp=("frp", "mean"),
        median_frp=("frp", "median")
    )
    .reset_index()
)

if not regional_summary.empty:

    fig_region = px.bar(
        regional_summary,
        x="study_region_label",
        y="total_detections",
        color="study_region_label",
        text="total_detections",
        color_discrete_sequence=[
            "#f97316",
            "#ef4444"
        ],
        labels={
            "study_region_label": "Study Region",
            "total_detections": "Detection Records"
        }
    )

    fig_region.update_layout(
        template="plotly_dark",
        showlegend=False
    )

    st.plotly_chart(
        fig_region,
        use_container_width=True
    )

    st.dataframe(
        regional_summary.round(2),
        use_container_width=True,
        hide_index=True
    )


# =====================================================
# COORDINATE DATA
# =====================================================

st.divider()
st.subheader("Geographic Detection Records")

st.caption(
    "The following table contains records with valid geographic coordinates."
)

display_columns = [
    col for col in [
        "study_region_label",
        "sensor",
        "acquisition_date",
        "latitude",
        "longitude",
        "frp",
        "confidence"
    ]
    if col in map_data.columns
]

st.dataframe(
    map_data[display_columns],
    use_container_width=True,
    hide_index=True
)

csv_data = map_data[display_columns].to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Geographic Data CSV",
    data=csv_data,
    file_name="FIRELENS_geographic_analysis.csv",
    mime="text/csv"
)


# =====================================================
# RESEARCH NOTE
# =====================================================

with st.expander("Geographic Interpretation & Limitations"):

    st.write("""
    1. Each plotted point represents a satellite detection record.
    2. Multiple detections may correspond to the same wildfire event.
    3. No cross-sensor deduplication is applied.
    4. Geographic study boundaries are exploratory approximations.
    5. Coordinate validity does not guarantee detection accuracy.
    6. Spatial proximity alone cannot establish that two records
       represent the same fire event.
    """)


st.markdown("---")

st.caption(
    "FIRELENS V3 | Geographic Analysis | Exploratory Research"
)
