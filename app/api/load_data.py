from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy import func, or_
from app.db.database import SessionLocal, WordMeaning, IPA, AudioData, PosTagger, Sentence
from sqlalchemy.orm import Session
from app.db.database import SessionLocal, Base, get_db, WordMeaning

from pathlib import Path
import csv

router = APIRouter()


@router.post("/load_bangla_dictionary/")
async def load_csv_to_db(db: Session = Depends(get_db)):
    csv_path = Path("app/data/bangla_dictionary_updated.csv")

    if not csv_path.exists():
        raise HTTPException(status_code=404, detail="CSV file not found")

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            try:
                word_meaning = WordMeaning(
                    number=row["number"],
                    words=row['word'],
                    meaning=row['meaning'],
                    pageNo=row["pageNo"],
                    spelling=row['pronunciation'],
                    pos=row["pos"],
                    ipa=row['IPA'],
                    root_lang=row['language'],
                    type=row['class'],
                    sentence=row['sentence'],
                    source=row['source'],
                )
                db.add(word_meaning)
            except Exception as e:
                db.rollback()
                print(f"Error: {str(e)}")
        db.commit()

    return {"message": "CSV data loaded successfully"}


@router.post("/load_ipa/")
async def load_csv_to_db(db: Session = Depends(get_db)):
    csv_path = Path("app/data/bangla_dictionary.csv")
    if not csv_path.exists():
        raise HTTPException(status_code=404, detail="CSV file not found")

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            try:
                word_meaning = IPA(
                    words=row['word'],
                    ipa=row['IPA'],
                )
                db.add(word_meaning)
            except Exception as e:
                db.rollback()
                print(f"Error: {str(e)}")
        db.commit()

    return {"message": "CSV data loaded successfully for IPA"}


@router.post("/load_pos/")
async def load_csv_to_db(db: Session = Depends(get_db)):
    csv_path = Path("app/data/bangla_dictionary.csv")
    if not csv_path.exists():
        raise HTTPException(status_code=404, detail="CSV file not found")

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            try:
                word_meaning = PosTagger(
                    words=row['word'],
                    pos=row['pos'],
                )
                db.add(word_meaning)
            except Exception as e:
                db.rollback()
                print(f"Error: {str(e)}")
        db.commit()

    return {"message": "CSV data loaded successfully for POS"}


@router.post("/load_sentence/")
async def load_csv_to_db(db: Session = Depends(get_db)):
    csv_path = Path("app/data/bangla_dictionary.csv")
    if not csv_path.exists():
        raise HTTPException(status_code=404, detail="CSV file not found")

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            try:
                word_meaning = Sentence(
                    words=row["word"],
                    sentence=row['sentence'],
                )
                db.add(word_meaning)
            except Exception as e:
                db.rollback()
                print(f"Error: {str(e)}")
        db.commit()

    return {"message": "CSV data loaded successfully for Sentence"}
