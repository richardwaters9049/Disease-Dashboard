from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# Schema for validating incoming POST request data for disease reports
class DiseaseReportCreate(BaseModel):
    disease_name: str = Field(..., example="Malaria")
    patient_age: int = Field(..., ge=0, example=35)
    location: str = Field(..., example="Kampala, Uganda")
    latitude: float = Field(..., example=0.3476)
    longitude: float = Field(..., example=32.5825)
    symptoms: str = Field(..., example="Fever, chills, vomiting")


# Schema for formatting the API's response output
class DiseaseReportOut(DiseaseReportCreate):
    id: int  # Report ID
    report_date: datetime  # Time the report was created

    class Config:
        orm_mode = True  # Tells Pydantic to read data from SQLAlchemy models
