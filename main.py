from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
import pandas as pd
from io import BytesIO
import os

from utils import analyze_cashflow  # your core logic
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Finance API",
    description="Project Cashflow Analyzer",
    version="2.0"
)

# ✅ CORS Middleware (if you use this with web frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Health Check Route
@app.get("/", response_class=HTMLResponse)
async def health_check():
    return "<h3>✅ AI Finance API is running. Visit <a href='/docs'>/docs</a> to test the API.</h3>"

# ✅ Upload & Analyze Cashflow
@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    if not file.filename.endswith((".xls", ".xlsx")):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an Excel (.xls or .xlsx) file.")

    try:
        contents = await file.read()
        df = pd.read_excel(BytesIO(contents))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to read Excel file: {str(e)}")

    try:
        result = analyze_cashflow(df)
        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing cashflow: {str(e)}")

# ✅ Download Excel Template
@app.get("/download-template")
async def download_template():
    template_path = "data/sample_cf.xlsx"
    if not os.path.exists(template_path):
        raise HTTPException(status_code=404, detail="Template file not found.")
    return FileResponse(
        path=template_path,
        media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        filename="sample_cf.xlsx"
    )


