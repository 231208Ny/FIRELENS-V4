import pandas as pd
from pathlib import Path

# =====================================
# 1. PROJECT PATHS
# =====================================

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = (
    BASE_DIR / "data" / "processed"
    / "regional_detections_exploratory.csv"
)

OUTPUT_DIR = BASE_DIR / "data" / "processed"

# =====================================
# 2. LOAD DATA
# =====================================

df = pd.read_csv(DATA_FILE)

print("FINAL DATA QUALITY ASSESSMENT")
print("================================")
print("Total input records:", len(df))

# =====================================
# 3. PREPARE COLUMNS
# =====================================

df["latitude"] = pd.to_numeric(
    df["latitude"], errors="coerce"
)

df["longitude"] = pd.to_numeric(
    df["longitude"], errors="coerce"
)

df["frp"] = pd.to_numeric(
    df["frp"], errors="coerce"
)

df["acquisition_date_parsed"] = pd.to_datetime(
    df["acquisition_date"],
    errors="coerce"
)

time_numeric = pd.to_numeric(
    df["acquisition_time_hhmm"], errors="coerce"
)

# Validate HHMM format, e.g. 656 = 06:56
valid_time = (
    time_numeric.notna()
    & (time_numeric >= 0)
    & (time_numeric <= 2359)
    & (time_numeric % 100 < 60)
    & (time_numeric % 1 == 0)
)

# =====================================
# 4. QUALITY CHECKS
# =====================================

checks = {}

# Duplicate detection IDs
checks["duplicate_detection_id"] = (
    df["detection_record_id"].duplicated(keep=False)
)

# Invalid geographic coordinates
checks["invalid_coordinates"] = (
    df["latitude"].isna()
    | df["longitude"].isna()
    | ~df["latitude"].between(-90, 90)
    | ~df["longitude"].between(-180, 180)
)

# Missing FRP
checks["missing_frp"] = df["frp"].isna()

# Non-positive FRP
checks["non_positive_frp"] = (
    df["frp"].notna() & (df["frp"] <= 0)
)

# Invalid acquisition date
checks["invalid_date"] = (
    df["acquisition_date_parsed"].isna()
)

# Invalid acquisition time
checks["invalid_time"] = ~valid_time

# Sensor and satellite consistency
valid_combinations = (
    ((df["sensor"] == "MODIS") &
     (df["satellite"].isin(["Aqua", "Terra"])))
    |
    ((df["sensor"] == "VIIRS") &
     (df["satellite"] == "N20"))
)

checks["sensor_satellite_mismatch"] = ~valid_combinations

# =====================================
# 5. GENERATE SUMMARY
# =====================================

summary = []

for check_name, condition in checks.items():

    affected = int(condition.sum())

    summary.append({
        "quality_check": check_name,
        "affected_records": affected,
        "percentage": round(
            affected / len(df) * 100, 2
        ),
        "status": (
            "PASS" if affected == 0
            else "REVIEW REQUIRED"
        )
    })

summary_df = pd.DataFrame(summary)

print("\nQUALITY CHECK RESULTS")
print("================================")

print(summary_df.to_string(index=False))

# =====================================
# 6. COLLECT FLAGGED RECORDS
# =====================================

flagged = pd.DataFrame(
    False, index=df.index, columns=["flagged"]
)

for check_name, condition in checks.items():
    flagged.loc[condition, "flagged"] = True

flagged_df = df.loc[flagged["flagged"]].copy()

flagged_df["quality_issues"] = ""

for check_name, condition in checks.items():

    affected_indices = df.index[condition]

    for index in affected_indices:
        existing = flagged_df.at[index, "quality_issues"]

        if existing:
            flagged_df.at[index, "quality_issues"] = (
                existing + "; " + check_name
            )
        else:
            flagged_df.at[index, "quality_issues"] = (
                check_name
            )

# =====================================
# 7. SAVE REPORTS
# =====================================

summary_file = (
    OUTPUT_DIR / "final_data_quality_summary.csv"
)

flagged_file = (
    OUTPUT_DIR / "final_data_quality_flagged_records.csv"
)

summary_df.to_csv(summary_file, index=False)
flagged_df.to_csv(flagged_file, index=False)

# =====================================
# 8. FINAL SUMMARY
# =====================================

print("\n================================")
print("FINAL ASSESSMENT SUMMARY")
print("================================")

print("Total records:", len(df))
print("Flagged records:", len(flagged_df))
print(
    "Records without flagged issues:",
    len(df) - len(flagged_df)
)

print("\nSaved files:")
print(summary_file)
print(flagged_file)

print("\nAssessment completed.")
print("No records were automatically deleted.")
