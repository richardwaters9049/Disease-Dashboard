from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List

from .. import models, schemas
from ..database import SessionLocal, engine

# Create API router specifically for disease report functionality
router = APIRouter()


# Dependency that creates a database session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/", response_model=schemas.DiseaseReportOut, status_code=status.HTTP_201_CREATED
)
def create_report(report: schemas.DiseaseReportCreate, db: Session = Depends(get_db)):
    """
    Accept a disease report via POST request and store it in the PostgreSQL database.
    Validates request body using Pydantic and persists it using SQLAlchemy.
    """
    # Convert the validated Pydantic schema into an SQLAlchemy model
    db_report = models.DiseaseReport(**report.dict())

    # Persist to database
    db.add(db_report)
    db.commit()
    db.refresh(db_report)  # Get auto-generated fields like ID and timestamp

    return db_report


@router.get("/", response_model=List[schemas.DiseaseReportOut])
def get_all_reports(db: Session = Depends(get_db)):
    """
    Retrieve all disease reports from the database, ordered by newest first.
    Useful for frontend dashboards, analytics, and data visualisation.
    """
    # Query all reports from DB, sort by report_date DESC (most recent first)
    reports = (
        db.query(models.DiseaseReport)
        .order_by(desc(models.DiseaseReport.report_date))
        .all()
    )

    # FastAPI + Pydantic will auto-convert to JSON using DiseaseReportOut schema
    return reports
