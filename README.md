# global_stats: Global Cardiovascular Bayesian Analysis
**E156 Micro-Paper Research Pipeline

**Live Dashboard:** [https://mahmood726-cyber.github.io/global_stats/](https://mahmood726-cyber.github.io/global_stats/)**

## E156 Protocol (Timestamped: 2026-04-08)
1. **OA-Inflow:** IHME GBD 2019, WHO GHO, World Bank WDI, ClinicalTrials.gov (Open Access only).
2. **Determinism:** Bayesian Hierarchical Intercept Model with fixed seed (156).
3. **TruthCert:** v1.2 Protocol; SHA256 evidence locators for all posterior estimates.
4. **Validation:** 100% pass on pytest ingestion suite; R-based regional variance analysis.
5. **Dashboard:** Interactive HTML served via GitHub Pages.
6. **Integrity:** Failed-closed if data locator hash mismatch.
7. **Paper:** 7-sentence micro-paper (156 words max) in `rewrite-workbook.txt`.

## Technical Stack
- **Data Ingestion:** Python (Pandas, Requests)
- **Statistical Modeling:** R (brms/Stan simulation)
- **Visualization:** HTML5/CSS3 (GitHub Pages compatible)
- **Certification:** TruthCert v1.2

## Structure
- `/data/` (Excluded from Git; raw and processed datasets)
- `/pipelines/` - Python data fetchers
- `/models/` - R Bayesian hierarchical logic
- `/dashboard/` - Interactive results dashboard
- `/tests/` - Offline-first validation suite

## Usage
1. `pip install -r requirements.txt`
2. `python pipelines/ingest_data.py`
3. `Rscript models/hierarchical_model.R`
4. Open `dashboard/index.html`

## License
Open Access / MIT License
