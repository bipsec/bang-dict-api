from sqlalchemy import create_engine, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db:5432/postgres"
Base = declarative_base()

engine = create_engine(SQLALCHEMY_DATABASE_URL)


class WordMeaning(Base):
    __tablename__ = "word_meaning"

    id = Column(Integer, primary_key=True, index=True)
    pageNo = Column(String, unique=False, index=True)
    words = Column(String, unique=False, index=True)
    number = Column(String, unique=False, nullable=True, index=True)
    spelling = Column(String, nullable=True, index=True)
    meaning = Column(String, nullable=True, index=True)
    pos = Column(String, nullable=True, unique=False, index=True)
    ipa = Column(String, unique=False, nullable=True, index=True)
    root_lang = Column(String, nullable=True, index=True)
    type = Column(String, unique=False, nullable=True, index=True)
    sentence = Column(String, unique=False, nullable=True, index=True)
    source = Column(String, index=True)
    audio = Column(String, nullable=True, index=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Initialize the database tables here
Base.metadata.create_all(bind=engine)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
