
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# =====================================================
# FIRELENS V4 - RESEARCH MODE
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "regional_detections_exploratory.csv"
)


# =====================================================
# PAGE STYLING
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

    .hero {
        padding: 30px;
        border-radius: 18px;
        background: linear-gradient(
            120deg,
            #172554,
            #7c2d12,
            #991b1b
        );
        margin-bottom: 25px;
    }

    .hero h1 {
        color: white;
        font-size: 42px;
        margin-bottom: 8px;
    }

    .hero p {
        color: #e2e8f0;
        font-size: 16px;
    }

    .section-title {
        color: #f8fafc;
        font-size: 23px;
        font-weight: 700;
        margin-top: 25px;
    }

    .research-note {
        background-color: #172554;
        padding: 16px;
        border-radius: 10px;
        border-left: 4px solid #60a5fa;
    }
</style>
""", unsafe_allow_html=True)


# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)

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
        raise ValueError(
            f"Missing required columns: {', '.join(missing)}"
        )

    df["acquisition_date"] = pd.to_datetime(
        df["acquisition_date"],
        errors="coerce"
    )

    for col in ["latitude", "longitude", "frp"]:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    df["month"] = (
        df["acquisition_date"]
        .dt.to_period("M")
        .astype(str)
    )

    return df


if not DATA_PATH.exists():
    st.error("Dataset tidak ditemukan.")
    st.code(str(DATA_PATH))
    st.info(
        "Pastikan file regional_detections_exploratory.csv "
        "berada di folder data/processed."
    )
    st.stop()

try:
    df = load_data(DATA_PATH)
except Exception as error:
    st.error(f"Gagal membaca dataset: {error}")
    st.stop()


# =====================================================
# DATA PREPARATION
# =====================================================

df = df.dropna(
    subset=[
        "study_region_label",
        "sensor",
        "acquisition_date",
        "latitude",
        "longitude"
    ]
).copy()

if df.empty:
    st.error("Tidak ada data valid untuk ditampilkan.")
    st.stop()

regions = sorted(df["study_region_label"].unique())
sensors = sorted(df["sensor"].unique())

min_date = df["acquisition_date"].min().date()
max_date = df["acquisition_date"].max().date()


# =====================================================
# SIDEBAR FILTERS
# =====================================================

st.sidebar.title("🔬 Research Controls")
st.sidebar.caption("FIRELENS V4 | Research Mode")

selected_regions = st.sidebar.multiselect(
    "Study Regions",
    options=regions,
    default=regions
)

selected_sensors = st.sidebar.multiselect(
    "Satellite Sensors",
    options=sensors,
    default=sensors
)

date_range = st.sidebar.date_input(
    "Observation Period",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date, end_date = min_date, max_date

filtered = df[
    df["study_region_label"].isin(selected_regions)
    & df["sensor"].isin(selected_sensors)
    & (
        df["acquisition_date"].dt.date >= start_date
    )
    & (
        df["acquisition_date"].dt.date <= end_date
    )
].copy()

if filtered.empty:
    st.warning(
        "No records match the selected filters. "
        "Please adjust your research filters."
    )
    st.stop()


# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
<div class="hero">
    <h1>🔥 FIRELENS Research Mode</h1>
    <p>
        Satellite-Based Wildfire Detection Research
        & Advanced Analytical Workspace
    </p>
    <p>
        Explore geographic distribution, temporal patterns,
        satellite sensors, and Fire Radiative Power (FRP).
    </p>
</div>
""", unsafe_allow_html=True)

st.caption(
    f"Observation period: {start_date} to {end_date}"
)


# =====================================================
# RESEARCH OVERVIEW
# =====================================================

st.markdown(
    '<div class="section-title">Research Overview</div>',
    unsafe_allow_html=True
)

total_records = len(filtered)
total_regions = filtered["study_region_label"].nunique()
total_sensors = filtered["sensor"].nunique()

mean_frp = filtered["frp"].mean()
median_frp = filtered["frp"].median()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Detection Records",
    f"{total_records:,}"
)

col2.metric(
    "Study Regions",
    total_regions
)

col3.metric(
    "Satellite Sensors",
    total_sensors
)

col4.metric(
    "Mean FRP",
    f"{mean_frp:.2f} MW" if pd.notna(mean_frp) else "N/A"
)

col5, col6 = st.columns(2)

col5.metric(
    "Median FRP",
    f"{median_frp:.2f} MW" if pd.notna(median_frp) else "N/A"
)

col6.metric(
    "Maximum FRP",
    f"{filtered['frp'].max():.2f} MW"
    if filtered["frp"].notna().any()
    else "N/A"
)


# =====================================================
# GEOGRAPHIC ANALYSIS
# =====================================================

st.markdown(
    '<div class="section-title">Geographic Analysis</div>',
    unsafe_allow_html=True
)

geo_col1, geo_col2 = st.columns(2)

with geo_col1:
    region_counts = (
        filtered["study_region_label"]
        .value_counts()
        .reset_index()
    )

    region_counts.columns = ["Region", "Detections"]

    fig_region = px.bar(
        region_counts,
        x="Region",
        y="Detections",
        color="Region",
        title="Detection Records by Region",
        text="Detections"
    )

    fig_region.update_layout(
        template="plotly_dark",
        showlegend=False
    )

    st.plotly_chart(
        fig_region,
        use_container_width=True
    )

with geo_col2:
    sensor_counts = (
        filtered["sensor"]
        .value_counts()
        .reset_index()
    )

    sensor_counts.columns = ["Sensor", "Detections"]

    fig_sensor = px.pie(
        sensor_counts,
        names="Sensor",
        values="Detections",
        title="Satellite Sensor Distribution",
        hole=0.45
    )

    fig_sensor.update_layout(
        template="plotly_dark"
    )

    st.plotly_chart(
        fig_sensor,
        use_container_width=True
    )


# =====================================================
# TEMPORAL ANALYSIS
# =====================================================

st.markdown(
    '<div class="section-title">Temporal Analysis</div>',
    unsafe_allow_html=True
)

monthly = (
    filtered
    .groupby(
        [
            "month",
            "study_region_label"
        ])
    .size()
    .reset_index(name="detections")
)

fig_monthly = px.bar(
    monthly,
    x="month",
    y="detections",
    color="study_region_label",
    barmode="group",
    title="Monthly Satellite Detection Activity",
    labels={
        "month": "Month",
        "detections": "Detection Records",
        "study_region_label": "Study Region"
    }
)

fig_monthly.update_layout(
    template="plotly_dark"
)

st.plotly_chart(
    fig_monthly,
    use_container_width=True
)

daily = (
    filtered
    .groupby("acquisition_date")
    .size()
    .reset_index(name="detections")
)

fig_daily = px.line(
    daily,
    x="acquisition_date",
    y="detections",
    markers=True,
    title="Daily Detection Activity",
    labels={
        "acquisition_date": "Observation Date",
        "detections": "Detection Records"
    }
)

fig_daily.update_layout(
    template="plotly_dark"
)

st.plotly_chart(
    fig_daily,
    use_container_width=True
)


# =====================================================
# FIRE RADIATIVE POWER ANALYSIS
# =====================================================

st.markdown(
    '<div class="section-title">Fire Radiative Power Analysis</div>',
    unsafe_allow_html=True
)

frp_data = filtered.dropna(subset=["frp"]).copy()

if not frp_data.empty:

    frp_col1, frp_col2 = st.columns(2)

    with frp_col1:
        fig_hist = px.histogram(
            frp_data,
            x="frp",
            color="study_region_label",
            nbins=40,
            title="FRP Distribution",
            labels={
                "frp": "Fire Radiative Power (MW)"
            }
        )

        fig_hist.update_layout(
            template="plotly_dark"
        )

        st.plotly_chart(
            fig_hist,
            use_container_width=True
        )

    with frp_col2:
        fig_box = px.box(
            frp_data,
            x="study_region_label",
            y="frp",
            color="study_region_label",
            title="FRP Comparison by Region",
            labels={
                "frp": "Fire Radiative Power (MW)",
                "study_region_label": "Study Region"
            }
        )

        fig_box.update_layout(
            template="plotly_dark",
            showlegend=False
        )

        st.plotly_chart(
            fig_box,
            use_container_width=True
        )

    st.markdown("#### FRP Statistical Summary")

    frp_summary = (
        frp_data
        .groupby("study_region_label")["frp"]
        .agg(
            ["count", "mean", "median", "std", "min", "max"]
        )
        .reset_index()
    )

    frp_summary.columns = [
        "Study Region",
        "Records",
        "Mean (MW)",
        "Median (MW)",
        "Standard Deviation",
        "Minimum (MW)",
        "Maximum (MW)"
    ]

    st.dataframe(
        frp_summary,
        use_container_width=True,
        hide_index=True
    )

else:
    st.info("FRP data is unavailable for the selected filters.")


# =====================================================
# GEOGRAPHIC HOTSPOT MAP
# =====================================================

st.markdown(
    '<div class="section-title">Satellite Detection Map</div>',
    unsafe_allow_html=True
)

map_data = filtered.dropna(
    subset=["latitude", "longitude"]
)

if not map_data.empty:

    fig_map = px.scatter_map(
        map_data,
        lat="latitude",
        lon="longitude",
        color="study_region_label",
        hover_data={
            "sensor": True,
            "frp": True,
            "acquisition_date": True,
            "latitude": False,
            "longitude": False
        },
        zoom=4,
        height=600,
        map_style="open-street-map",
        title="Geographic Distribution of Satellite Detections"
    )

    fig_map.update_traces(
        marker={"size": 7, "opacity": 0.65}
    )

    st.plotly_chart(
        fig_map,
        use_container_width=True
    )


# =====================================================
# DATA EXPLORER
# =====================================================

st.markdown(
    '<div class="section-title">Research Data Explorer</div>',
    unsafe_allow_html=True
)

st.write(
    "Explore the filtered satellite detection records "
    "used in the current analysis."
)

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)

csv_data = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Research Data",
    data=csv_data,
    file_name="firelens_filtered_research_data.csv",
    mime="text/csv"
)


# =====================================================
# METHODOLOGY AND LIMITATIONS
# =====================================================

st.markdown(
    '<div class="section-title">Methodology & Limitations</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="research-note">
<strong>Research methodology</strong><br><br>
FIRELENS explores historical active-fire detection records
from NASA FIRMS MODIS and VIIRS satellite products.
The platform provides exploratory geographic, temporal,
sensor, and Fire Radiative Power analysis.
</div>
""", unsafe_allow_html=True)

with st.expander("Important Research Limitations"):

    st.markdown("""
    - Satellite detection records do not necessarily represent
      unique wildfire events.
    - Cross-sensor records have not been completely deduplicated.
    - Study-region boundaries are approximate.
    - MODIS and VIIRS have different observation characteristics.
    - FRP is not a direct measurement of burned area or total damage.
    - Temporal and spatial proximity alone cannot prove that
      detections belong to the same fire.
    - This historical dataset does not provide real-time alerts.
    """)


# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "FIRELENS V4 | Research & Analytical Workspace"
)

st.caption(
    "Historical satellite detection records | "
    "Riau and Central Kalimantan, Indonesia"
)
