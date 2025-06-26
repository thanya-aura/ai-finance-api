from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from io import BytesIO
from utils import analyze_cashflow

app = FastAPI(
    title="AI Finance Cashflow API",
    description="Upload Excel and get variance, red flags, and analysis.",
    version="1.0.0"
)

# Optional: CORS settings (required if calling from web or external UI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for security in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root path (health check)
@app.get("/")
def read_root():
    return {"status": "AI Finance API is running", "version": "1.0.0"}

# Analyze route
@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_excel(BytesIO(contents))
        result = analyze_cashflow(df)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"File processing error: {str(e)}")
