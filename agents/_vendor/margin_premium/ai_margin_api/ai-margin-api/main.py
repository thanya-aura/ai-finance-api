from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import your API routers
from agents.premium.premium_router import router as premium_router
from agents.plus.plus_router import router as plus_router
# from agents.standard.standard_router import router as standard_router  # Uncomment when ready

app = FastAPI(
    title="AI Margin API",
    description="API for margin analysis with Standard, Plus, and Premium tiers.",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(premium_router, prefix="/premium", tags=["Premium"])
app.include_router(plus_router, prefix="/plus", tags=["Plus"])
# app.include_router(standard_router, prefix="/standard", tags=["Standard"])  # Uncomment when used

@app.get("/")
def root():
    return {
        "status": "API is running",
        "message": "Welcome to the AI Margin API"
    }
