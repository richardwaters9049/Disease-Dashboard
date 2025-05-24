from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import SessionLocal, engine

# Create API router specific to disease reports
router = APIRouter()


# Dependency that provides a new DB session for each request
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
    Accept a disease report via POST request and store it in the database.
    Returns the stored report with an assigned ID and timestamp.
    """
    # Create SQLAlchemy model instance from validated Pydantic schema
    db_report = models.DiseaseReport(**report.dict())

    # Add the report to the session and commit to DB
    db.add(db_report)
    db.commit()
    db.refresh(db_report)  # Refresh to get the auto-generated ID and timestamp

    return db_report
