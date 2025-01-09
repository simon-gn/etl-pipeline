from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
DB_URL = os.getenv("DB_URL")


def get_db_connection():
    """Return a SQLAlchemy database engine."""
    return create_engine(DB_URL)
