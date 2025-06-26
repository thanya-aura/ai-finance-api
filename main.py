from fastapi import FastAPI, UploadFile, File
import pandas as pd
from io import BytesIO
from utils import analyze_cashflow

app = FastAPI()

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_excel(BytesIO(contents))
    result = analyze_cashflow(df)
    return result
