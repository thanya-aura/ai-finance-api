from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
from io import BytesIO

from processors.single_cf import process_single_cf
from processors.enterprise_cf import process_enterprise_cf
from processors.custom_cf import process_custom_cf

app = FastAPI(title="AI Finance CF API", version="1.0")

@app.post("/analyze")
async def analyze(file: UploadFile = File(...), agent_type: str = "single_cf"):
    if not file.filename.endswith((".xls", ".xlsx")):
        raise HTTPException(status_code=400, detail="Invalid file type")

    df = pd.read_excel(BytesIO(await file.read()))

    if agent_type == "single_cf":
        return process_single_cf(df)
    elif agent_type == "enterprise_cf":
        return process_enterprise_cf(df)
    elif agent_type == "custom_cf":
        return process_custom_cf(df)
    else:
        raise HTTPException(status_code=400, detail="Unknown agent type")
