from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from io import BytesIO
from .plus_agent import analyze_plus_margin

router = APIRouter()

@router.post("/analyze")
async def analyze_plus(file: UploadFile = File(...)):
    """
    Endpoint: /plus/analyze
    - Accepts an Excel or CSV file with Revenue and Profit
    - Returns margin analysis using PLUS-tier logic
    """
    filename = file.filename.lower()

    if not filename.endswith((".csv", ".xlsx")):
        raise HTTPException(status_code=400, detail="Only .csv or .xlsx files are supported.")

    try:
        contents = await file.read()
        df = pd.read_excel(BytesIO(contents)) if filename.endswith(".xlsx") else pd.read_csv(BytesIO(contents))
        result = analyze_plus_margin(df)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
