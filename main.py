from fastapi import FastAPI, UploadFile, File, HTTPException, Query
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
import pandas as pd
from io import BytesIO
import os
from utils import analyze_cashflow
from utils.session_store import update_stored_data

app = FastAPI(
    title="AI Finance API",
    description="Project Cashflow Analyzer",
    version="2.0"
)

# ✅ Health Check Route
@app.get("/", response_class=HTMLResponse)
async def health_check():
    return "<h3>✅ AI Finance API is running. Visit /docs for API interface.</h3>"

# ✅ File Upload and Cashflow Analysis
@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    mode: str = Query("replace", enum=["replace", "append"], description="Choose whether to replace or append the uploaded data.")
):
    if not file.filename.endswith((".xls", ".xlsx")):
        raise HTTPException(status_code=400, detail="Invalid file type. Upload an Excel file (.xls or .xlsx).")

    contents = await file.read()
    try:
        df = pd.read_excel(BytesIO(contents))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to read Excel file: {str(e)}")

    try:
        updated_df = update_stored_data(df, mode=mode)
        result = analyze_cashflow(updated_df)
        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing cashflow: {str(e)}")

# ✅ Template File Download
@app.get("/download-template")
async def download_template():
    template_path = "templates/sample_cf.xlsx"
    if not os.path.exists(template_path):
        raise HTTPException(status_code=404, detail="Template file not found.")
    return FileResponse(
        template_path,
        media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        filename="sample_cf.xlsx"
    )

