
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# =====================================================
# FIRELENS V3 - DATA QUALITY & VALIDATION
# =====================================================

st.set_page_config(
    page_title="Data Quality | FIRELENS",
    page_icon="🛡️",
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

    .quality-header {
        background: linear-gradient(120deg, #172554, #14532d);
        padding: 25px;
        border-radius: 16px;
        margin-bottom: 20px;
    }

    .quality-header h1 {
        color: white;
        font-size: 34px;
    }

    .quality-header p {
        color: #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)


# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data(path):
    raw = pd.read_csv(path)

    data = raw.copy()

    data["acquisition_date"] = pd.to_datetime(
        data["acquisition_date"],
        errors="coerce"
    )

    for col in ["latitude", "longitude", "frp"]:
        data[col] = pd.to_numeric(
            data[col],
            errors="coerce"
        )

    return raw, data


st.title("🛡️ Data Quality & Validation")

if not DATA_PATH.exists():
    st.error("Dataset tidak ditemukan.")
    st.code(str(DATA_PATH))
    st.stop()

try:
    raw, df = load_data(DATA_PATH)

except Exception as error:
    st.error(f"Gagal membaca dataset: {error}")
    st.stop()


# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="quality-header">
    <h1>Data Quality Assessment</h1>
    <p>
        Dataset integrity, completeness, consistency,
        and validation diagnostics.
    </p>
</div>
""", unsafe_allow_html=True)


# =====================================================
# HISTORICAL VALIDATION SUMMARY
# =====================================================

st.header("1. Previous Validation Assessment")

st.write(
    """
    The previously recorded FIRELENS validation assessment
    reported seven checks passed, zero flagged findings,
    and no automatic data removal.
    """
)

a, b, c = st.columns(3)

a.metric("Previous Checks Passed", "7 / 7")

b.metric("Previously Flagged Findings", "0")

c.metric("Automatic Data Removal", "None")

st.info(
    "These figures summarize the earlier validation assessment. "
    "They are not automatically inferred from the new diagnostics below."
)


# =====================================================
# REQUIRED COLUMNS
# =====================================================

st.divider()
st.header("2. Dataset Structure")

required_columns = [
    "study_region_label",
    "sensor",
    "acquisition_date",
    "latitude",
    "longitude",
    "frp"
]

missing_columns = [
    col for col in required_columns
    if col not in raw.columns
]

if missing_columns:
    st.error(
        "Required columns are missing: "
        + ", ".join(missing_columns)
    )
    st.stop()

s1, s2, s3 = st.columns(3)

s1.metric("Total Records", f"{len(raw):,}")

s2.metric("Total Columns", len(raw.columns))

s3.metric(
    "Missing Required Columns",
    len(missing_columns)
)

with st.expander("View dataset columns"):
    st.write(raw.columns.tolist())


# =====================================================
# SEVEN LIVE DIAGNOSTIC CHECKS
# =====================================================

st.divider()
st.header("3. Live Data Quality Diagnostics")

st.caption(
    "Seven reproducible checks are calculated from the current CSV. "
    "These checks are separate from the historical validation assessment."
)

total = len(df)

if total == 0:
    st.error("Dataset tidak memiliki baris data.")
    st.stop()


# Check 1: Date validity

valid_dates = df["acquisition_date"].notna().sum()
invalid_dates = total - valid_dates

# Check 2: Coordinate completeness

coordinate_missing = (
    df["latitude"].isna()
    | df["longitude"].isna()
).sum()

# Check 3: Coordinate ranges

coordinate_range_invalid = (
    (
        df["latitude"].notna()
        & ~df["latitude"].between(-90, 90)
    )
    |
    (
        df["longitude"].notna()
        & ~df["longitude"].between(-180, 180)
    )
).sum()

# Check 4: FRP validity

frp_missing = df["frp"].isna().sum()

frp_negative = (
    df["frp"].notna()
    & (df["frp"] < 0)
).sum()

# Check 5: Region completeness

region_missing = (
    df["study_region_label"].isna()
    | (
        df["study_region_label"]
        .astype("string")
        .str.strip()
        .eq("")
        .fillna(True)
    )
).sum()

# Check 6: Sensor completeness

sensor_missing = (
    df["sensor"].isna()
    | (
        df["sensor"]
        .astype("string")
        .str.strip()
        .eq("")
        .fillna(True)
    )
).sum()

# Check 7: Exact duplicate rows

duplicate_rows = raw.duplicated().sum()


# =====================================================
# CHECK RESULTS
# =====================================================

def get_status(problem_count):
    return "PASS" if problem_count == 0 else "REVIEW"


checks = [
    {
        "Check": "Date Validity",
        "Description": "Records with valid acquisition dates",
        "Issue Count": int(invalid_dates),
        "Status": get_status(invalid_dates)
    },
    {
        "Check": "Coordinate Completeness",
        "Description": "Records missing latitude or longitude",
        "Issue Count": int(coordinate_missing),
        "Status": get_status(coordinate_missing)
    },
    {
        "Check": "Coordinate Range",
        "Description": "Coordinates outside valid geographic ranges",
        "Issue Count": int(coordinate_range_invalid),
        "Status": get_status(coordinate_range_invalid)
    },
    {
        "Check": "FRP Validity",
        "Description": "Missing or negative FRP values",
        "Issue Count": int(frp_missing + frp_negative),
        "Status": get_status(frp_missing + frp_negative)
    },
    {
        "Check": "Region Completeness",
        "Description": "Records without a study-region label",
        "Issue Count": int(region_missing),
        "Status": get_status(region_missing)
    },
    {
        "Check": "Sensor Completeness",
        "Description": "Records without a sensor label",
        "Issue Count": int(sensor_missing),
        "Status": get_status(sensor_missing)
    },
    {
        "Check": "Exact Duplicate Rows",
        "Description": "Identical complete rows in the CSV",
        "Issue Count": int(duplicate_rows),
        "Status": (
            "INFO" if duplicate_rows > 0 else "PASS"
        )
    }
]

checks_df = pd.DataFrame(checks)

passed = (checks_df["Status"] == "PASS").sum()
review = (checks_df["Status"] == "REVIEW").sum()
info = (checks_df["Status"] == "INFO").sum()

p1, p2, p3 = st.columns(3)

p1.metric("Passed Checks", f"{passed}/7")

p2.metric("Checks Requiring Review", int(review))

p3.metric("Informational Findings", int(info))


# =====================================================
# VALIDATION TABLE
# =====================================================

st.subheader("Validation Results")

st.dataframe(
    checks_df,
    use_container_width=True,
    hide_index=True
)

st.caption(
    "PASS = no issue detected by the specified check. "
    "REVIEW = one or more records require inspection. "
    "INFO = informational result, not automatically an error."
)


# =====================================================
# MISSING VALUE ANALYSIS
# =====================================================

st.divider()
st.header("4. Missing Value Analysis")

missing_summary = pd.DataFrame({
    "Column": raw.columns,
    "Missing Values": [
        raw[col].isna().sum()
        for col in raw.columns
    ]
})

missing_summary["Missing Percentage"] = (
    missing_summary["Missing Values"]
    / max(total, 1) * 100
)

missing_summary = missing_summary.sort_values(
    "Missing Percentage",
    ascending=False
)

left, right = st.columns(2)

with left:

    st.subheader("Missing Value Summary")

    st.dataframe(
        missing_summary.round(2),
        use_container_width=True,
        hide_index=True
    )

with right:

    st.subheader("Missing Value Distribution")

    missing_plot = missing_summary[
        missing_summary["Missing Values"] > 0
    ]

    if not missing_plot.empty:

        fig_missing = px.bar(
            missing_plot,
            x="Column",
            y="Missing Values",
            color="Missing Percentage",
            color_continuous_scale="Oranges",
            text="Missing Values"
        )

        fig_missing.update_layout(
            template="plotly_dark",
            xaxis_title="Dataset Column",
            yaxis_title="Missing Records"
        )

        st.plotly_chart(
            fig_missing,
            use_container_width=True
        )

    else:
        st.success("No missing values detected in the dataset.")


# =====================================================
# DATA RANGE ANALYSIS
# =====================================================

st.divider()
st.header("5. Data Range Assessment")

range_left, range_right = st.columns(2)

with range_left:

    st.subheader("Geographic Coordinate Range")

    coordinate_summary = pd.DataFrame({
        "Variable": ["Latitude", "Longitude"],
        "Minimum": [
            df["latitude"].min(),
            df["longitude"].min()
        ],
        "Maximum": [
            df["latitude"].max(),
            df["longitude"].max()
        ]
    })

    st.dataframe(
        coordinate_summary.round(5),
        use_container_width=True,
        hide_index=True
    )

with range_right:

    st.subheader("FRP Range")

    frp_summary = pd.DataFrame({
        "Statistic": [
            "Minimum",
            "Maximum",
            "Mean",
            "Median",
            "Standard Deviation"
        ],
        "FRP (MW)": [
            df["frp"].min(),
            df["frp"].max(),
            df["frp"].mean(),
            df["frp"].median(),
            df["frp"].std()
        ]
    })

    st.dataframe(
        frp_summary.round(3),
        use_container_width=True,
        hide_index=True
    )


# =====================================================
# DUPLICATE ASSESSMENT
# =====================================================

st.divider()
st.header("6. Duplicate Record Assessment")

st.metric(
    "Exact Duplicate Rows",
    f"{duplicate_rows:,}"
)

if duplicate_rows > 0:
    st.warning(
        "Identical rows were detected. Inspect them before deciding "
        "whether removal is appropriate."
    )
else:
    st.success(
        "No exact duplicate complete rows were detected."
    )

st.caption(
    "This check only identifies identical complete rows. "
    "It does not identify repeated detections of the same fire "
    "across different sensors or acquisition times."
)


# =====================================================
# DATA QUALITY INTERPRETATION
# =====================================================

st.divider()
st.header("7. Data Quality Interpretation")

if review == 0:

    st.success(
        "No issues were detected by the seven live checks. "
        "This does not establish that every satellite detection "
        "is accurate or represents a unique fire."
    )

else:

    st.warning(
        f"{review} live check(s) require further inspection. "
        "Review the validation table and missing-value summary."
    )

st.markdown("""
**Important methodological considerations:**

- Missing coordinates can prevent a record from appearing on a map.
- Valid coordinate ranges do not establish geographic accuracy.
- Missing FRP values do not automatically invalidate every other
  attribute in a detection record.
- Exact duplicate rows are not the same as cross-sensor duplicates.
- Outlying FRP values are not automatically data errors.
- Data quality checks cannot independently verify the physical
  occurrence or severity of a wildfire.
""")


# =====================================================
# DOWNLOAD REPORT
# =====================================================

st.divider()
st.header("8. Export Data Quality Report")

report_csv = checks_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Validation Results",
    data=report_csv,
    file_name="FIRELENS_data_quality_report.csv",
    mime="text/csv"
)


# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption(
    "FIRELENS V3 | Data Quality & Validation | Exploratory Research"
)
