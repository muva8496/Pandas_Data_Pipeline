# Agricultural Data Pipeline (24-Month Sales & Market Intelligence)

A modular, production-grade Python and Pandas data pipeline designed to ingest, clean, transform, and aggregate multi-year agricultural sales transactions and market pricing data.

---

## 🏗️ Project Architecture
This project follows a strict **Modular ETL (Extract, Transform, Load)** design pattern, separating concerns into independent, testable components:

```text
Pandas_pipeline/
│
├── .gitignore             # Ensures raw and processed data remain local
├── README.md              # Project documentation
├── requirements.txt       # Project dependencies (pandas, numpy)
│
├── data/                  # Local directory (Ignored by Git)
│   ├── raw/               # 24 months of raw sales & reference CSVs
│   └── processed/         # Cleaned, aggregated master output files
│
└── src/                   # Source Code
    ├── __init__.py
    ├── ingest.py          # Dynamic file loading and directory scanning
    ├── clean.py           # Schema enforcement, type coercion, and null handling
    ├── transform.py       # Business logic calculations & tiering
    └── pipeline.py        # Master orchestrator script


