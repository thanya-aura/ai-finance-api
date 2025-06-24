
# AI Finance API – Cashflow Analyzer

## Endpoints:
- `POST /analyze/`: Upload an Excel file with `Date`, `Planned`, and `Actual` columns to get variance analysis.
- `GET /download-template/`: Download a sample Excel template.

## Run Locally:
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Deploy on Render:
- Runtime: Python 3.10
- Start Command:
```
uvicorn main:app --host 0.0.0.0 --port 10000
```
