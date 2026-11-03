
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# =====================================================
# FIRELENS V3 - RESEARCH INSIGHTS & METHODOLOGY
# =====================================================

st.set_page_config(
    page_title="Research Insights | FIRELENS",
    page_icon="📚",
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

    .research-header {
        background: linear-gradient(120deg, #172554, #7c2d12);
        padding: 28px;
        border-radius: 16px;
        margin-bottom: 25px;
    }

    .research-header h1 {
        color: white;
        font-size: 36px;
    }

    .research-header p {
        color: #e2e8f0;
    }

    .research-card {
        background: #172033;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px;
        min-height: 150px;
    }

    .research-card h4 {
        color: #fb923c;
    }

    .research-card p {
        color: #cbd5e1;
    }

    .section-label {
        color: #fb923c;
        font-size: 13px;
        font-weight: bold;
        letter-spacing: 2px;
    }
</style>
""", unsafe_allow_html=True)


# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)

    df["acquisition_date"] = pd.to_datetime(
        df["acquisition_date"],
        errors="coerce"
    )

    for col in ["latitude", "longitude", "frp"]:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    return df


st.title("📚 Research Insights & Methodology")

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
    "frp",
    "latitude",
    "longitude"
]

missing = [col for col in required if col not in df.columns]

if missing:
    st.error(f"Kolom dataset tidak lengkap: {missing}")
    st.stop()


# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="research-header">
    <div class="section-label">FIRELENS RESEARCH DOCUMENTATION</div>
    <h1>Research Insights & Methodology</h1>
    <p>
        Connecting satellite detection records with
        analytical findings, scientific interpretation,
        and methodological transparency.
    </p>
</div>
""", unsafe_allow_html=True)


# =====================================================
# SECTION 1: RESEARCH BACKGROUND
# =====================================================

st.header("1. Research Background")

st.write("""
Wildfires are an important environmental concern because
they can affect ecosystems, air quality, biodiversity,
and human activities.

Satellite-based active fire products provide a way to
observe fire-related thermal anomalies across large
geographic areas.

FIRELENS is an exploratory research platform that examines
satellite-based fire detection records from MODIS and VIIRS
in Riau and Central Kalimantan, Indonesia.

The platform combines geographic, temporal, and Fire
Radiative Power (FRP) analyses to identify patterns
within the available observation records.
""")


# =====================================================
# SECTION 2: RESEARCH OBJECTIVES
# =====================================================

st.header("2. Research Objectives")

objectives = [
    "Examine the geographic distribution of satellite fire detection records.",
    "Identify temporal patterns across the observation period.",
    "Explore the distribution and statistical characteristics of FRP.",
    "Compare detection records and FRP characteristics across satellite sensors.",
    "Assess dataset completeness, consistency, and basic validity.",
    "Develop an interactive platform for exploratory wildfire data analysis."
]

for i, objective in enumerate(objectives, 1):
    st.markdown(f"**{i}.** {objective}")


# =====================================================
# SECTION 3: DATASET PROFILE
# =====================================================

st.divider()
st.header("3. Research Dataset Profile")

region_counts = (
    df["study_region_label"]
    .value_counts()
    .reset_index()
)

region_counts.columns = ["Study Region", "Records"]

sensor_counts = (
    df["sensor"]
    .value_counts()
    .reset_index()
)

sensor_counts.columns = ["Sensor", "Records"]

frp = df["frp"].dropna()

dates = df["acquisition_date"].dropna()

k1, k2, k3, k4 = st.columns(4)

k1.metric("Total Records", f"{len(df):,}")

k2.metric(
    "Study Regions",
    df["study_region_label"].nunique()
)

k3.metric(
    "Sensors",
    df["sensor"].nunique()
)

k4.metric(
    "Mean FRP",
    f"{frp.mean():.2f} MW" if not frp.empty else "N/A"
)

if not dates.empty:
    st.write(
        f"**Available observation dates:** "
        f"{dates.min().date()} to {dates.max().date()}"
    )

left, right = st.columns(2)

with left:
    st.subheader("Records by Study Region")

    fig_region = px.bar(
        region_counts,
        x="Study Region",
        y="Records",
        color="Study Region",
        text="Records",
        color_discrete_sequence=["#f97316", "#ef4444"]
    )

    fig_region.update_layout(
        template="plotly_dark",
        showlegend=False
    )

    st.plotly_chart(
        fig_region,
        use_container_width=True
    )

with right:
    st.subheader("Records by Sensor")

    fig_sensor = px.pie(
        sensor_counts,
        names="Sensor",
        values="Records",
        hole=0.5,
        color_discrete_sequence=[
            "#f97316",
            "#ef4444",
            "#fbbf24"
        ]
    )

    fig_sensor.update_layout(template="plotly_dark")

    st.plotly_chart(
        fig_sensor,
        use_container_width=True
    )


# =====================================================
# SECTION 4: KEY RESEARCH FINDINGS
# =====================================================

st.divider()
st.header("4. Key Research Findings")

st.markdown("""
The following findings summarize the previously completed
FIRELENS analytical assessment. They should be interpreted
within the scope of the selected dataset and observation period.
""")

findings = [
    {
        "title": "Geographic Distribution",
        "description": (
            "The exploratory dataset contains 12,809 detection "
            "records. Central Kalimantan contributes 10,030 "
            "records, while Riau contributes 2,779 records."
        )
    },
    {
        "title": "Temporal Concentration",
        "description": (
            "September 2024 recorded the highest monthly "
            "detection activity in Central Kalimantan, with "
            "6,911 records. The highest daily count was "
            "762 records on 14 September 2024."
        )
    },
    {
        "title": "Riau Temporal Pattern",
        "description": (
            "Riau recorded 1,054 detections in August, "
            "687 in September, and 1,038 in October 2024. "
            "Its highest daily count was 223 records "
            "on 27 October 2024."
        )
    },
    {
        "title": "Fire Radiative Power",
        "description": (
            "The mean FRP was 14.03 MW in Central Kalimantan "
            "and 11.09 MW in Riau. The median values were "
            "8.09 MW and 5.43 MW, respectively."
        )
    },
    {
        "title": "Satellite Sensor Comparison",
        "description": (
            "MODIS Aqua recorded the highest mean FRP in both "
            "study regions, while VIIRS N20 contributed the "
            "largest detection record count in the earlier "
            "sensor comparison."
        )
    },
    {
        "title": "Data Quality",
        "description": (
            "The previous validation assessment recorded "
            "seven checks passed, zero flagged findings, "
            "and no automatic data removal."
        )
    }
]

for finding in findings:
    with st.container(border=True):
        st.markdown(f"### {finding['title']}")
        st.write(finding["description"])


# =====================================================
# SECTION 5: SCIENTIFIC INTERPRETATION
# =====================================================

st.divider()
st.header("5. Scientific Interpretation")

st.subheader("5.1 Geographic Interpretation")

st.write("""
The larger number of satellite detection records in
Central Kalimantan indicates a greater representation
of detections from this region within the assembled dataset.

However, record counts alone cannot establish that
the region experienced a proportionally greater number
of unique wildfire events.

Differences in observation coverage, satellite overpasses,
detection characteristics, and geographic sampling should
also be considered.
""")

st.subheader("5.2 Temporal Interpretation")

st.write("""
The concentration of detection records in September 2024
in Central Kalimantan indicates a period of elevated
satellite-observed detection activity within the study dataset.

Riau shows a different monthly distribution, with relatively
high record counts in August and October.

These temporal patterns describe the available satellite
records. They do not independently explain the environmental
or human factors responsible for fire occurrence.
""")

st.subheader("5.3 FRP Interpretation")

st.write("""
Mean FRP values exceeding median FRP values are consistent
with a right-skewed distribution, in which a smaller number
of high-FRP observations can increase the arithmetic mean.

Higher FRP values should not automatically be interpreted
as larger burned areas or greater total environmental damage.
FRP is a measure of radiative power associated with
satellite-observed active fire pixels.
""")

st.subheader("5.4 Sensor Interpretation")

st.write("""
Differences in detection counts and FRP statistics across
MODIS and VIIRS sensors may reflect differences in sensor
characteristics, spatial resolution, observation timing,
and detection algorithms.

Therefore, sensor comparisons should be treated as
descriptive rather than as direct measurements of
differences in actual wildfire occurrence.
""")


# =====================================================
# SECTION 6: METHODOLOGY
# =====================================================

st.divider()
st.header("6. Research Methodology")

st.markdown("#### Research Design")

st.write("""
This project uses a quantitative exploratory data analysis
approach based on satellite-derived active fire detection records.
The analysis focuses on geographic distribution, temporal
patterns, FRP characteristics, and sensor comparisons.
""")

st.markdown("#### Data Source")

st.write("""
The dataset is based on NASA FIRMS active fire information
from MODIS and VIIRS satellite instruments.

The study focuses on two Indonesian regions:
Riau and Central Kalimantan.
""")

st.markdown("#### Observation Period")

st.write("""
1 August 2024 – 31 October 2024.
""")

st.markdown("#### Analytical Workflow")

workflow = [
    ("01", "Data Acquisition", "Collect satellite detection records."),
    ("02", "Data Preprocessing", "Standardize and harmonize relevant fields."),
    ("03", "Data Quality Assessment", "Evaluate completeness and basic validity."),
    ("04", "Geographic Analysis", "Explore the spatial distribution of detections."),
    ("05", "Temporal Analysis", "Examine daily and monthly detection patterns."),
    ("06", "FRP Analysis", "Describe FRP distributions and statistics."),
    ("07", "Sensor Comparison", "Compare MODIS and VIIRS detection records."),
    ("08", "Analytical Synthesis", "Interpret findings and document limitations.")
]

for number, title, description in workflow:
    st.markdown(
        f"**{number} — {title}**  \n{description}"
    )

st.markdown("#### Analytical Techniques")

st.write("""
- Descriptive statistics.
- Frequency distributions.
- Daily and monthly aggregation.
- Geographic point mapping.
- FRP histograms and boxplots.
- Sensor-based grouping and comparison.
- Basic data validation diagnostics.
""")


# =====================================================
# SECTION 7: LIMITATIONS
# =====================================================

st.divider()
st.header("7. Research Limitations")

limitations = [
    (
        "Detection Records vs. Unique Events",
        "Individual satellite detections do not necessarily "
        "represent unique wildfire events."
    ),
    (
        "Cross-Sensor Duplication",
        "No cross-sensor deduplication was performed. "
        "Multiple records may represent overlapping observations."
    ),
    (
        "Geographic Boundaries",
        "The study uses exploratory geographic bounding areas "
        "rather than authoritative provincial boundary polygons."
    ),
    (
        "Sensor Differences",
        "MODIS and VIIRS have different sensor characteristics "
        "and confidence assessment schemes."
    ),
    (
        "FRP Interpretation",
        "FRP should not be treated as a direct measure of "
        "burned area, total fire damage, or total emissions."
    ),
    (
        "Causal Explanation",
        "Spatial and temporal patterns alone cannot establish "
        "the causes of wildfire occurrence."
    ),
    (
        "Observation Coverage",
        "Satellite records are influenced by observation timing, "
        "cloud conditions, and detection limitations."
    )
]

for title, description in limitations:
    with st.expander(title):
        st.write(description)


# =====================================================
# SECTION 8: FUTURE RESEARCH
# =====================================================

st.divider()
st.header("8. Recommendations for Future Research")

recommendations = [
    "Integrate authoritative administrative boundary datasets.",
    "Apply a carefully documented cross-sensor matching procedure.",
    "Incorporate rainfall, temperature, humidity, and drought indicators.",
    "Compare active fire detections with burned-area products.",
    "Explore land-cover and peatland characteristics.",
    "Validate selected observations using independent information sources.",
    "Extend the observation period to investigate interannual patterns."
]

for i, item in enumerate(recommendations, 1):
    st.markdown(f"**{i}.** {item}")


# =====================================================
# SECTION 9: CONCLUSION
# =====================================================

st.divider()
st.header("9. Research Conclusion")

st.write("""
FIRELENS provides an exploratory analytical framework for
examining satellite-based wildfire detection records in
Riau and Central Kalimantan during August–October 2024.

The findings reveal differences in geographic record
distribution, temporal concentration, FRP characteristics,
and satellite sensor representation across the two study regions.

The results demonstrate the value of combining geographic,
temporal, statistical, and data quality analyses in an
integrated research platform.

Nevertheless, the findings should be interpreted within
the limitations of satellite detection records. Further
research using authoritative boundaries, environmental
variables, burned-area information, and independent
validation data would strengthen future assessments.
""")


# =====================================================
# EXPORT RESEARCH SUMMARY
# =====================================================

st.divider()
st.header("10. Research Documentation")

research_summary = """
FIRELENS - RESEARCH SUMMARY

Research Title:
Satellite-Based Wildfire Detection Analysis in Riau
and Central Kalimantan, Indonesia.

Observation Period:
1 August 2024 - 31 October 2024.

Dataset:
12,809 exploratory satellite detection records.

Study Regions:
Central Kalimantan: 10,030 records.
Riau: 2,779 records.

Central Kalimantan:
September 2024: 6,911 records.
Highest daily count: 762 on 14 September 2024.
Mean FRP: 14.03 MW.
Median FRP: 8.09 MW.

Riau:
August 2024: 1,054 records.
September 2024: 687 records.
October 2024: 1,038 records.
Highest daily count: 223 on 27 October 2024.
Mean FRP: 11.09 MW.
Median FRP: 5.43 MW.

Sensor Findings:
MODIS Aqua recorded the highest mean FRP in both regions.
VIIRS N20 contributed the largest detection record count
in the previous sensor comparison.

Previous Data Quality Assessment:
7 checks passed.
0 flagged findings.
No automatic data removal.

Research Limitations:
- Detection records are not unique wildfire events.
- No cross-sensor deduplication.
- Geographic areas are exploratory approximations.
- Sensor characteristics and confidence schemes differ.
- FRP is not equivalent to burned area or total damage.
- Spatial and temporal proximity cannot prove event identity.

Research Approach:
Quantitative exploratory data analysis.
"""

st.download_button(
    label="Download Research Summary TXT",
    data=research_summary,
    file_name="FIRELENS_research_summary.txt",
    mime="text/plain"
)


# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption(
    "FIRELENS V3 | Research Insights & Methodology | "
    "Satellite-Based Wildfire Detection Analysis"
)
