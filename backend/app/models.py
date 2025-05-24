from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from .database import Base


# This SQLAlchemy model defines the structure of the 'disease_reports' table
# Each instance of DiseaseReport corresponds to a row in the database
class DiseaseReport(Base):
    __tablename__ = "disease_reports"  # Table name in PostgreSQL

    # Primary key ID column (auto-incremented)
    id = Column(Integer, primary_key=True, index=True)

    # Disease name e.g., 'Malaria'
    disease_name = Column(String, nullable=False)

    # Patient's age in years
    patient_age = Column(Integer, nullable=False)

    # Location name, e.g., 'Kampala, Uganda'
    location = Column(String, nullable=False)

    # Latitude and Longitude for geolocation mapping
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    # Symptom description, e.g., 'Fever, chills'
    symptoms = Column(String, nullable=False)

    # Timestamp when the report is submitted
    report_date = Column(DateTime(timezone=True), server_default=func.now())
