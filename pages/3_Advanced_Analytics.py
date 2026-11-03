
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# =====================================================
# FIRELENS V3 - ADVANCED ANALYTICS
# =====================================================

st.set_page_config(
    page_title="Advanced Analytics | FIRELENS",
    page_icon="📊",
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

    .analytics-header {
        background: linear-gradient(120deg, #172554, #7c2d12);
        padding: 25px;
        border-radius: 16px;
        margin-bottom: 20px;
    }

    .analytics-header h1 {
        color: white;
        font-size: 34px;
    }

    .analytics-header p {
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

    for col in ["frp", "latitude", "longitude"]:
        data[col] = pd.to_numeric(
            data[col],
            errors="coerce"
        )

    return data


st.title("📊 Advanced Analytics")

if not DATA_PATH.exists():
    st.error("Dataset tidak ditemukan.")
    st.code(str(DATA_PATH))
    st.stop()

try:
    df = load_data(DATA_PATH)
except Exception as error:
    st.error(f"Gagal membaca dataset: {error}")
    st.stop()


required = [
    "study_region_label",
    "sensor",
    "acquisition_date",
    "frp"
]

missing = [col for col in required if col not in df.columns]

if missing:
    st.error(f"Kolom dataset tidak lengkap: {missing}")
    st.stop()


# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="analytics-header">
    <h1>Advanced Research Analytics</h1>
    <p>
        Temporal patterns, Fire Radiative Power distributions,
        and satellite sensor comparisons.
    </p>
</div>
""", unsafe_allow_html=True)


# =====================================================
# FILTERS
# =====================================================

st.sidebar.header("Analytics Filters")

regions = sorted(
    df["study_region_label"].dropna().unique().tolist()
)

sensors = sorted(
    df["sensor"].dropna().unique().tolist()
)

selected_regions = st.sidebar.multiselect(
    "Study Region",
    regions,
    default=regions
)

selected_sensors = st.sidebar.multiselect(
    "Satellite Sensor",
    sensors,
    default=sensors
)

valid_dates = df["acquisition_date"].dropna()

if valid_dates.empty:
    st.error("Tidak tersedia tanggal pengamatan yang valid.")
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
        st.warning("Pilih periode tanggal.")
        st.stop()
else:
    start_date = end_date = selected_dates


# =====================================================
# FILTER DATA
# =====================================================

data = df[
    df["study_region_label"].isin(selected_regions)
    & df["sensor"].isin(selected_sensors)
    & df["acquisition_date"].dt.date.between(
        start_date,
        end_date
    )
].copy()

frp_data = data.dropna(subset=["frp"]).copy()

if data.empty:
    st.warning("Tidak ada data untuk kombinasi filter ini.")
    st.stop()


# =====================================================
# OVERVIEW
# =====================================================

st.subheader("Analytical Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Detection Records",
    f"{len(data):,}"
)

c2.metric(
    "Mean FRP",
    f"{frp_data['frp'].mean():.2f} MW"
    if not frp_data.empty else "N/A"
)

c3.metric(
    "Median FRP",
    f"{frp_data['frp'].median():.2f} MW"
    if not frp_data.empty else "N/A"
)

c4.metric(
    "FRP Records",
    f"{len(frp_data):,}"
)


# =====================================================
# SECTION 1: TEMPORAL ANALYSIS
# =====================================================

st.divider()
st.header("1. Temporal Analysis")

st.write(
    "This section examines the temporal distribution "
    "of satellite fire detection records."
)

temporal_data = data.dropna(
    subset=["acquisition_date"]
).copy()

temporal_data["Date"] = (
    temporal_data["acquisition_date"].dt.date
)

temporal_data["Month"] = (
    temporal_data["acquisition_date"]
    .dt.to_period("M")
    .astype(str)
)

daily_counts = (
    temporal_data.groupby("Date")
    .size()
    .reset_index(name="Detections")
)

monthly_counts = (
    temporal_data.groupby("Month")
    .size()
    .reset_index(name="Detections")
)

if not daily_counts.empty:

    st.subheader("Daily Detection Distribution")

    fig_daily = px.line(
        daily_counts,
        x="Date",
        y="Detections",
        markers=True,
        color_discrete_sequence=["#f97316"],
        labels={
            "Date": "Acquisition Date",
            "Detections": "Detection Records"
        }
    )

    fig_daily.update_layout(
        template="plotly_dark",
        hovermode="x unified"
    )

    st.plotly_chart(
        fig_daily,
        use_container_width=True
    )

if not monthly_counts.empty:

    st.subheader("Monthly Detection Distribution")

    fig_monthly = px.bar(
        monthly_counts,
        x="Month",
        y="Detections",
        text="Detections",
        color="Detections",
        color_continuous_scale="Oranges"
    )

    fig_monthly.update_layout(
        template="plotly_dark",
        xaxis_title="Observation Month",
        yaxis_title="Detection Records"
    )

    st.plotly_chart(
        fig_monthly,
        use_container_width=True
    )

if not daily_counts.empty:
    peak_day = daily_counts.loc[
        daily_counts["Detections"].idxmax()
    ]

    st.info(
        f"Highest daily detection count in the selected "
        f"dataset: {peak_day['Date']} "
        f"({peak_day['Detections']:,} records)."
    )


# =====================================================
# SECTION 2: FRP ANALYSIS
# =====================================================

st.divider()
st.header("2. Fire Radiative Power Analysis")

st.write(
    "FRP represents the satellite-derived radiative power "
    "associated with detected active fire pixels."
)

if frp_data.empty:

    st.warning("Tidak tersedia nilai FRP yang valid.")

else:

    frp_left, frp_right = st.columns(2)

    with frp_left:

        st.subheader("FRP Distribution")

        fig_hist = px.histogram(
            frp_data,
            x="frp",
            nbins=40,
            color_discrete_sequence=["#f97316"],
            labels={
                "frp": "Fire Radiative Power (MW)"
            }
        )

        fig_hist.update_layout(
            template="plotly_dark",
            yaxis_title="Detection Records"
        )

        st.plotly_chart(
            fig_hist,
            use_container_width=True
        )

    with frp_right:

        st.subheader("FRP by Region")

        fig_box = px.box(
            frp_data,
            x="study_region_label",
            y="frp",
            color="study_region_label",
            points=False,
            color_discrete_sequence=[
                "#f97316",
                "#ef4444"
            ],
            labels={
                "study_region_label": "Study Region",
                "frp": "FRP (MW)"
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

    st.subheader("FRP Statistical Summary")

    frp_summary = (
        frp_data.groupby("study_region_label")["frp"]
        .agg(
            Count="count",
            Mean="mean",
            Median="median",
            Minimum="min",
            Maximum="max",
            Standard_Deviation="std"
        )
        .reset_index()
    )

    st.dataframe(
        frp_summary.round(2),
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        "FRP distributions may be right-skewed. "
        "Extreme values are not automatically considered errors."
    )


# =====================================================
# SECTION 3: SENSOR COMPARISON
# =====================================================

st.divider()
st.header("3. Satellite Sensor Comparison")

st.write(
    "Compare detection record counts and FRP statistics "
    "across the available satellite sensors."
)

sensor_summary = (
    data.groupby("sensor")
    .agg(
        Detection_Records=("sensor", "size"),
        Mean_FRP=("frp", "mean"),
        Median_FRP=("frp", "median")
    )
    .reset_index()
)

sensor_left, sensor_right = st.columns(2)

with sensor_left:

    st.subheader("Detection Records by Sensor")

    fig_sensor_count = px.bar(
        sensor_summary,
        x="sensor",
        y="Detection_Records",
        color="sensor",
        text="Detection_Records",
        color_discrete_sequence=[
            "#f97316",
            "#ef4444",
            "#fbbf24"
        ]
    )

    fig_sensor_count.update_layout(
        template="plotly_dark",
        showlegend=False,
        xaxis_title="Sensor",
        yaxis_title="Detection Records"
    )

    st.plotly_chart(
        fig_sensor_count,
        use_container_width=True
    )

with sensor_right:

    st.subheader("Mean FRP by Sensor")

    fig_sensor_frp = px.bar(
        sensor_summary,
        x="sensor",
        y="Mean_FRP",
        color="sensor",
        text_auto=".2f",
        color_discrete_sequence=[
            "#f97316",
            "#ef4444",
            "#fbbf24"
        ]
    )

    fig_sensor_frp.update_layout(
        template="plotly_dark",
        showlegend=False,
        xaxis_title="Sensor",
        yaxis_title="Mean FRP (MW)"
    )

    st.plotly_chart(
        fig_sensor_frp,
        use_container_width=True
    )


st.subheader("Sensor Statistical Summary")

st.dataframe(
    sensor_summary.round(2),
    use_container_width=True,
    hide_index=True
)


# =====================================================
# SECTION 4: REGION-SENSOR COMPARISON
# =====================================================

st.divider()
st.header("4. Regional Sensor Comparison")

region_sensor = (
    data.groupby(
        ["study_region_label", "sensor"]
    )
    .size()
    .reset_index(name="Detections")
)

fig_comparison = px.bar(
    region_sensor,
    x="study_region_label",
    y="Detections",
    color="sensor",
    barmode="group",
    text="Detections",
    color_discrete_sequence=[
        "#f97316",
        "#ef4444",
        "#fbbf24"
    ]
)

fig_comparison.update_layout(
    template="plotly_dark",
    xaxis_title="Study Region",
    yaxis_title="Detection Records",
    legend_title="Sensor"
)

st.plotly_chart(
    fig_comparison,
    use_container_width=True
)


# =====================================================
# SECTION 5: ANALYTICAL INTERPRETATION
# =====================================================

st.divider()
st.header("5. Analytical Interpretation")

st.markdown("#### Temporal Findings")

if not daily_counts.empty:

    st.write(
        f"- The highest daily count in the current filter "
        f"was {peak_day['Detections']:,} records on "
        f"{peak_day['Date']}."
    )

if not monthly_counts.empty:

    peak_month = monthly_counts.loc[
        monthly_counts["Detections"].idxmax()
    ]

    st.write(
        f"- The month with the highest number of records "
        f"was {peak_month['Month']} with "
        f"{peak_month['Detections']:,} records."
    )

st.markdown("#### FRP Findings")

if not frp_data.empty:

    mean_value = frp_data["frp"].mean()
    median_value = frp_data["frp"].median()

    if mean_value > median_value:
        st.write(
            "- The mean FRP exceeds the median FRP, "
            "which is consistent with a right-skewed "
            "distribution."
        )
    elif mean_value < median_value:
        st.write(
            "- The mean FRP is lower than the median "
            "in the selected records."
        )
    else:
        st.write(
            "- The mean and median FRP are approximately equal."
        )

st.markdown("#### Sensor Findings")

if not sensor_summary.empty:

    highest_sensor = sensor_summary.loc[
        sensor_summary["Detection_Records"].idxmax()
    ]

    st.write(
        f"- {highest_sensor['sensor']} has the largest "
        f"number of detection records in the current filter."
    )

st.warning(
    "These interpretations are descriptive and exploratory. "
    "Differences in detection counts and FRP across sensors "
    "do not independently establish differences in actual "
    "wildfire occurrence or intensity."
)


# =====================================================
# DOWNLOAD
# =====================================================

st.divider()
st.subheader("Download Analytical Dataset")

csv = data.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download Filtered Analytics CSV",
    data=csv,
    file_name="FIRELENS_advanced_analytics.csv",
    mime="text/csv"
)


# =====================================================
# LIMITATIONS
# =====================================================

with st.expander("Methodological Considerations"):

    st.write("""
    - Satellite detections are not equivalent to unique wildfire events.
    - Cross-sensor deduplication has not been performed.
    - Sensor detection characteristics and confidence schemes differ.
    - FRP is a satellite-derived measurement and is not equivalent
      to burned area or total fire damage.
    - Temporal patterns describe observed records, not necessarily
      the complete occurrence of all fires.
    - Results depend on the selected study regions and observation period.
    - Statistical comparisons are descriptive, not causal.
    """)


st.markdown("---")

st.caption(
    "FIRELENS V3 | Advanced Analytics | Exploratory Research"
)
