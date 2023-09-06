from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pathlib import Path
import csv
from app.api import dictionary
from app.db.database import SessionLocal, Base
from app.db.models import WordMeaning, Base
from app.db.database import get_db

app = FastAPI()

# Including API Router
app.include_router(dictionary.router)

# CORS settings
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to Bangla Dictionary API. It provides data for Bangla Dictionary Web Application."}



