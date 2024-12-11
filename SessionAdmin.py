from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv






def generate_database_url()->str:
    load_dotenv(".env")
    DB_NAME = os.getenv("DB_NAME")
    DB_PORT = os.getenv("DB_PORT")
    DB_HOST = os.getenv("DB_HOST")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_USER = os.getenv("DB_USER")
    return "postgresql+psycopg2://"+DB_USER+":"+DB_PASSWORD+"@"+DB_HOST+":"+DB_PORT+"/"+DB_NAME

def generate_session():  
    DATABASE_URL =  generate_database_url()

    # Create an engine that will communicate with the database
    engine = create_engine(DATABASE_URL, echo=True)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()
    
    return session

def try_save_and_close_session(session):
    try:
        session.commit()
    except Exception as e:
        session.rollback() 
        print(f"Error occurred: {e}")
    finally:
        session.close()  # Close the session