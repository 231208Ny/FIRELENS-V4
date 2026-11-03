
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

BASE = Path(__file__).resolve().parent

ZIP_PATH = BASE.parent / "FIRELENS_V4_FINAL_PACKAGE.zip"

# Essential project files
include_paths = [
    "app.py",
    "home.py",
    "requirements.txt",
    "README.md",
    "README_DATA.md",
    "README_GEOGRAPHIC_ANALYSIS.md",
    "TECHNICAL_DOCUMENTATION.md",
    "FIRELENS_FINAL_RESEARCH_REPORT.md",
    "FIRELENS_FINAL_RESEARCH_REPORT_REVISED.md",
    "FIRELENS_final_analytical_synthesis.md",
    "FIRELENS_V3_system_test_report.csv",
    "pages",
    "data/processed",
    "assets",
    "scripts",
    "research_outputs",
]

# Additional analytical scripts
include_files = [
    "analyze_cluster_time.py",
    "analyze_daily_frp.py",
    "analyze_peak_day_sensors.py",
    "check_daily_frp.py",
    "check_frp_distribution.py",
    "final_data_quality_assessment.py",
    "final_system_check.py",
    "generate_research_visuals.py",
    "harmonize_firms.py",
    "inspect_dependencies.py",
    "inspect_extreme_frp.py",
    "inspect_spatial_cluster.py",
    "create_validated_results.py",
    "update_final_report.py",
]

excluded_parts = {
    "__pycache__",
    ".git",
    ".venv",
    "venv",
    "backup_pages",
    "backup",
}

included = set()
missing = []

def add_file(file):
    if not file.is_file():
        return

    relative_parts = file.relative_to(BASE).parts

    if any(part in excluded_parts for part in relative_parts):
        return

    if file.suffix == ".pyc":
        return

    included.add(file)

# Collect project folders and essential files
for item in include_paths:
    path = BASE / item

    if not path.exists():
        missing.append(item)
        continue

    if path.is_file():
        add_file(path)
    else:
        for file in path.rglob("*"):
            add_file(file)

# Collect additional analytical scripts
for item in include_files:
    path = BASE / item

    if path.exists():
        add_file(path)

# Validate essential files
required_files = [
    "app.py",
    "home.py",
    "requirements.txt",
    "pages/1_Public_Mode.py",
    "pages/2_Geographic_Analysis.py",
    "pages/3_Advanced_Analytics.py",
    "pages/4_Data_Quality.py",
    "pages/5_Research_Insights.py",
    "pages/6_Research_Mode.py",
    "data/processed/regional_detections_exploratory.csv",
]

missing_required = [
    item for item in required_files
    if not (BASE / item).is_file()
]

if missing_required:
    print("ERROR: Required project files are missing:")
    for item in missing_required:
        print("-", item)

    raise RuntimeError("Packaging cancelled.")

if not included:
    raise RuntimeError("No project files found.")

# Create ZIP package
with ZipFile(ZIP_PATH, "w", ZIP_DEFLATED) as archive:
    for file in sorted(included):
        archive.write(file, file.relative_to(BASE))

print("\n======================================")
print(" FIRELENS V4 FINAL PACKAGE CREATED")
print("======================================")
print("ZIP:", ZIP_PATH)
print("Files included:", len(included))
print("ZIP size:", f"{ZIP_PATH.stat().st_size:,}", "bytes")
print("Required files validated: YES")
print("Original project preserved: YES")

if missing:
    print("\nOptional paths not found:")
    for item in missing:
        print("-", item)
