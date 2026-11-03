# FIRELENS V3 — Technical Documentation

## 1. System Description

FIRELENS V3 is an interactive web-based analytical platform developed using Python and Streamlit.

The system provides an interface for exploring satellite-based wildfire detection records in Riau and Central Kalimantan, Indonesia, during the period of August–October 2024.

The application is designed for exploratory analysis, visualization, and research interpretation.

## 2. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Interactive web application framework |
| Pandas | Data processing and manipulation |
| Plotly | Interactive data visualization |
| OpenStreetMap | Geographic basemap used in map visualization |

## 3. Project Directory Structure

```text
FIRELENS/
│
├── app.py
├── app_v2_backup.py
├── final_system_check.py
├── README.md
├── TECHNICAL_DOCUMENTATION.md
├── FIRELENS_V3_system_test_report.csv
│
├── assets/
│
├── data/
│   └── processed/
│       └── regional_detections_exploratory.csv
│
└── pages/
    ├── 2_Geographic_Analysis.py
    ├── 3_Advanced_Analytics.py
    ├── 4_Data_Quality.py
    └── 5_Research_Insights.py
```

## 4. Application Modules

### 4.1 Main Dashboard — app.py

The main dashboard provides an overview of the research dataset and its key findings.

Main functions:
- Dataset overview and key performance indicators.
- Regional detection comparison.
- Satellite sensor distribution.
- Monthly detection visualization.
- Research insights and methodological limitations.

### 4.2 Geographic Analysis

File: `pages/2_Geographic_Analysis.py`

Main functions:
- Interactive geographical visualization.
- Regional filtering.
- Sensor filtering.
- Date filtering.
- Geographic coordinate exploration.
- CSV data export.

The map visualization uses an OpenStreetMap basemap.

### 4.3 Advanced Analytics

File: `pages/3_Advanced_Analytics.py`

Main functions:
- Daily and monthly detection analysis.
- FRP distribution visualization.
- Statistical summaries.
- Sensor comparisons.
- Regional and sensor-based comparisons.
- Analytical interpretation and CSV export.

### 4.4 Data Quality

File: `pages/4_Data_Quality.py`

Main functions:
- Missing-value assessment.
- Coordinate validation.
- FRP validation.
- Region and sensor completeness checks.
- Exact duplicate detection.
- Data quality reporting.

The module reports diagnostic results without automatically deleting records.

### 4.5 Research Insights and Methodology

File: `pages/5_Research_Insights.py`

Main functions:
- Research background and objectives.
- Dataset profile.
- Key research findings.
- Methodological explanation.
- Research limitations.
- Future research directions.
- Research conclusion.

## 5. Data Input

The application reads the processed dataset from:

`data/processed/regional_detections_exploratory.csv`

The principal analytical fields include:

- study_region_label
- sensor
- acquisition_date
- latitude
- longitude
- frp

The dataset contains 12,809 detection records.

## 6. Application Execution

### Requirements

- Python installed on the computer.
- Required Python packages installed.
- FIRELENS project directory available locally.

### Running the application

Open Command Prompt and navigate to the project directory:

```cmd
cd C:\Users\user\Downloads\FIRELENS
```

Start the application:

```cmd
streamlit run app.py
```

Streamlit will display the local application address in the terminal.

Open the displayed address in a web browser.

### Stopping the application

Return to Command Prompt and press:

`Ctrl + C`

## 7. System Testing

The system was checked using:

`python final_system_check.py`

The recorded test results include:

| Test item | Result |
|---|---|
| Main application file | PASS |
| Backup application file | PASS |
| Four analytical page files | PASS |
| Dataset availability | PASS |
| Dataset readability | PASS |
| Total records | 12,809 |
| Missing values | 0 |
| Exact duplicate rows | 0 |
| System report generation | PASS |

The test report is saved as:

`FIRELENS_V3_system_test_report.csv`

These results represent the checks performed by the system-check script, not a guarantee that every analytical assumption or research conclusion is correct.

## 8. Operational Considerations

1. Keep the original dataset as a backup.
2. Do not modify the dataset without documenting the changes.
3. Ensure the processed CSV remains in the expected directory.
4. Internet access is required for online basemap tiles.
5. Review analytical outputs whenever the dataset is updated.
6. Interpret satellite detections as observations, not automatically as unique wildfire events.

## 9. Current System Status

FIRELENS V3 has successfully passed its recorded basic system checks.

All six expected application files were found, the dataset was readable, and the system test report was generated successfully.

The five dashboard sections have also been tested individually during development.

Further testing should include a complete user-interface review, filter interaction checks, CSV export verification, and validation of analytical interpretations.

---

**Document:** FIRELENS V3 Technical Documentation  
**Project:** Satellite-Based Wildfire Detection Analysis  
**Version:** 3.0