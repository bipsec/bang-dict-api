from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pathlib import Path
import csv
from app.api import dictionary, ipa

from app.db.database import SessionLocal, Base
# from app.db.models import WordMeaning, Base
from app.db.database import get_db, WordMeaning

app = FastAPI()

# Including API Router
app.include_router(dictionary.router)
app.include_router(ipa.router)

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


@app.post("/load-csv/")
async def load_csv_to_db(db: Session = Depends(get_db)):
    csv_path = Path("app/data/bangla_dictionary.csv")
    if not csv_path.exists():
        raise HTTPException(status_code=404, detail="CSV file not found")

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            # if any(value is None or value.strip() == '' for value in row.values()):
            #     continue


            try:
                # Ensure that the keys in 'row' match the model column names
                word_meaning = WordMeaning(
                    pageNo=row["pageNo"],
                    words=row['word'],
                    number=row["number"],
                    spelling=row['pronunciation'],
                    meaning=row['meaning'],
                    pos=row["pos"],
                    ipa=row['IPA'],
                    root_lang=row['language'],
                    type=row['class'],
                    sentence=row['sentence'],
                    source=row['source'],
                    audio=row["Audio"]
                )
                db.add(word_meaning)
            except Exception as e:
                # Handle any exceptions here (e.g., data type mismatch)
                db.rollback()
                print(f"Error: {str(e)}")
        db.commit()

    return {"message": "CSV data loaded successfully"}
