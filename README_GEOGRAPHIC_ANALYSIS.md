# FIRELENS — Geographic Analysis (Exploratory)

## Tujuan
Mengeksplorasi persebaran catatan deteksi aktif NASA FIRMS pada dua area studi:
- Riau
- Kalimantan Tengah

## Input yang dibutuhkan
Salin file hasil harmonisasi ke:
`data/processed/fire_events_harmonized.csv`

Script ini mengharapkan kolom:
`latitude`, `longitude`, `acquisition_date`, `sensor`, `satellite`,
`frp`, dan `detection_record_id`.

## Cara menjalankan
1. Letakkan folder `scripts` dan `data` di dalam project FIRELENS yang sudah ada.
2. Pastikan file harmonisasi tersedia di `data/processed/`.
3. Install dependensi:
   `python -m pip install pandas matplotlib`
4. Dari folder utama project, jalankan:
   `python scripts/geographic_analysis.py`

## File keluaran
- `regional_detections_exploratory.csv`
- `daily_activity_by_region_sensor.csv`
- `regional_sensor_summary.csv`
- `regional_summary_exploratory.csv`
- `regional_sensor_comparison.png`
- Grafik aktivitas harian terpisah untuk masing-masing area studi.

## Batasan metodologis — wajib dibaca
Penyaringan saat ini memakai bounding box koordinat perkiraan:
- Riau: latitude -1.5 sampai 2.0; longitude 100.0 sampai 104.5
- Kalimantan Tengah: latitude -3.5 sampai -0.5; longitude 110.0 sampai 115.5

Bounding box bukan batas administratif resmi. Karena itu, hasilnya adalah
**hasil eksplorasi area**, bukan jumlah resmi deteksi per provinsi. Untuk
analisis final/publikasi, ganti dengan polygon batas provinsi resmi dan
lakukan point-in-polygon spatial join.

Jumlah baris merupakan detection records, bukan jumlah kejadian kebakaran unik.
Deteksi MODIS dan VIIRS tidak dideduplikasi lintas sensor. Confidence MODIS
dan VIIRS juga memakai skema berbeda sehingga tidak boleh dibandingkan langsung.
