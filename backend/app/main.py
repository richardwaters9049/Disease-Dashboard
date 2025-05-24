from fastapi import FastAPI
from .routers import reports
from fastapi.middleware.cors import CORSMiddleware

# Initialise FastAPI app with some basic metadata
app = FastAPI(
    title="LSTM Outbreak Tracker API",
    description="An API to record and view disease outbreaks for tropical medicine research.",
    version="1.0.0",
)

# Allow Cross-Origin requests from any domain (you may restrict in prod)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register router for disease reports under /api/reports/
app.include_router(reports.router, prefix="/api/reports", tags=["Reports"])


# Root endpoint to confirm API is running
@app.get("/")
def read_root():
    return {"message": "Welcome to the LSTM Outbreak Tracker API"}
