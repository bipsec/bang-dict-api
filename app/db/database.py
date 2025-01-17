from sqlalchemy import create_engine, Boolean, Column, ForeignKey, Integer, String, Float, LargeBinary
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from app.core.config import get_settings
from app.db.models import Base

settings = get_settings()

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,
    pool_size=5,
    max_overflow=0
)

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:ariake@db:5432/postgres"


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Initialize the database tables here
Base.metadata.create_all(bind=engine)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
