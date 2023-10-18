from fastapi import APIRouter, Query
from fastapi import HTTPException, Path
from sqlalchemy import or_

from app.db.database import SessionLocal, WordMeaning

router = APIRouter()

@router.get("/dictionary/words")
async def get_words(letter: str = Query(None, description="A single letter"), page: int = Query(default=1, ge=1), limit: int = Query(default=10, le=500)):
    try:
        print(letter)
        if letter is not None and (len(letter) != 1 or not letter.isalpha()):
            raise HTTPException(status_code=400, detail="Invalid input. Please provide a single letter.")

        with SessionLocal() as session:
            offset = (page - 1) * limit

            query = session.query(WordMeaning.id, WordMeaning.words)
            if letter is not None:
                query = query.filter(
                    or_(
                        WordMeaning.words.like(f"{letter}%"),
                        WordMeaning.words.like(f"{letter.upper()}%")
                    )
                )
            query = query.distinct().offset(offset).limit(limit)
            words = query.all()
            print(words)
            responses = [{"id": word.id, "word": word.words} for word in words]
            return responses


    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


# TODO: This details should be fetched by word_id (when db schema will be done)
@router.get("/dictionary/word")
async def get_word_details(word: str, page: int = Query(default=1, ge=1), limit: int = Query(default=10, le=100)):
    try:
        with SessionLocal() as session:
            offset = (page - 1) * limit

            # Query details for the specified word with pagination
            query = session.query(WordMeaning).filter(WordMeaning.words == word)
            query = query.offset(offset).limit(limit)
            details = query.all()

            similar_spellings = []

            ipa = ""
            for index, row in enumerate(details):
                if not len(ipa):
                    ipa = row.ipa
                similar_spellings.append({
                    "id": row.id,
                    "meaning_no": row.number,
                    "meaning": row.meaning,
                    "pos": row.pos,
                    "spelling": row.spelling,
                    "language": row.root_lang,
                    "sentence": row.sentence,
                    "source": row.source,
                })

            response = {
                "word": word,
                "similar_spellings": similar_spellings,
                "ipa": ipa
            }

            return response
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
