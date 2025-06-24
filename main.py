
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import pandas as pd
from processor import analyze_cashflow

app = FastAPI()

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...)):
    df = pd.read_excel(file.file)
    result = analyze_cashflow(df)
    return result.to_dict(orient="records")

@app.get("/download-template/")
async def download_template():
    return FileResponse(
        path="sample_cf.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename="sample_cf.xlsx"
    )
