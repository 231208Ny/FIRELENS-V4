# FIRELENS — Data preparation (first pass)

## Input data
- `data/raw/modis.csv`: NASA FIRMS MODIS C6.1, Indonesia, 2024-08-01 to 2024-10-31
- `data/raw/viirs.csv`: NASA FIRMS J1 VIIRS C2, Indonesia, 2024-08-01 to 2024-10-31

## Output
- `data/processed/fire_events_harmonized.csv`
- `data/processed/data_quality_summary.csv`

## Important scientific decisions
1. The two sensors are standardized into common column names.
2. `confidence_raw` is preserved as text and `confidence_scheme` records its meaning:
   MODIS numeric confidence is not directly comparable with VIIRS categorical confidence.
3. `satellite` is preserved. MODIS contains Terra and Aqua; VIIRS contains N20.
4. No cross-sensor deduplication is performed. A fire may be detected by both sensors,
   and detections are not automatically equivalent to unique fire events.
5. `detection_record_id` identifies a row in this processed dataset only; it is not
   a unique real-world fire identifier.
6. The `type_code_raw` field is retained without assigning meanings until the exact
   product documentation is checked.

## Run the script
From the FIRELENS root folder:
```bash
python scripts/harmonize_firms.py
```
Install dependencies if needed:
```bash
python -m pip install pandas
```
