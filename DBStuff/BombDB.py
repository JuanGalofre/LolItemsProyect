from sqlalchemy import create_engine
from Models.CentralModels import Base 
import SessionAdmin

DATABASE_URL = SessionAdmin.generate_database_url()

# Create engine
engine = create_engine(DATABASE_URL)

# Drop and recreate tables
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

print("Database reset complete.")
