from app.database import engine
from app import models

# This script creates all database tables based on SQLAlchemy models
if __name__ == "__main__":
    print("Creating database tables...")
    models.Base.metadata.create_all(bind=engine)
    print("Done.")
