from fastapi import APIRouter, HTTPException, Query
from sqlalchemy import func, or_
from app.db.database import SessionLocal, WordMeaning


router = APIRouter()


@router.get("/dictionary/words")
async def get_similar_spellings(word: str, page: int = Query(default=1, ge=1), limit: int = Query(default=10, le=100)):
    try:
        with SessionLocal() as session:
            offset = (page - 1) * limit

            query = session.query(WordMeaning.number, WordMeaning.meaning)
            query = query.filter(WordMeaning.words == word).group_by(WordMeaning.number, WordMeaning.meaning)
            query = query.offset(offset).limit(limit)
            results = query.all()

            similar_spellings = []

            for idx, result in enumerate(results):
                similar_spellings.append({
                    "id": idx + 1,
                    "meaning_no": result.number,
                    "meanings": [result.meaning]
                })

            response = {
                "similar_spellings": similar_spellings,
                "word": word
            }

            return response
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/dictionary/all_words")
async def get_all_words(page: int = Query(default=1, ge=1), limit: int = Query(default=10, le=100)):
    try:
        with SessionLocal() as session:
            offset = (page - 1) * limit

            query = session.query(WordMeaning.words.distinct())
            query = query.offset(offset).limit(limit)
            all_words = query.all()

            all_responses = []
            for word_tuple in all_words:
                word = word_tuple[0]
                similar_spellings = []

                query = session.query(WordMeaning.number, WordMeaning.meaning)
                query = query.filter(WordMeaning.words == word).group_by(WordMeaning.number, WordMeaning.meaning)
                results = query.all()

                for idx, result in enumerate(results):
                    similar_spellings.append({
                        "id": idx + 1,
                        "meaning_no": result.number,
                        "meanings": [result.meaning]
                    })

                response = {
                    "word": word,
                    "similar_spellings": similar_spellings,

                }
                all_responses.append(response)

            return all_responses
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/dictionary/words_by_letter")
async def get_words_by_letter(letter: str, page: int = Query(default=1, ge=1), limit: int = Query(default=10, le=100)):
    try:
        if len(letter) != 1 or not letter.isalpha():
            raise HTTPException(status_code=400, detail="Invalid input. Please provide a single letter.")

        with SessionLocal() as session:
            offset = (page - 1) * limit

            query = session.query(WordMeaning.words).filter(or_(WordMeaning.words.like(f"{letter}%"), WordMeaning.words.like(f"{letter.upper()}%")))
            query = query.distinct().offset(offset).limit(limit)
            words = query.all()

            responses = []
            for word_tuple in words:
                word = word_tuple[0]
                similar_spellings = []

                query = session.query(WordMeaning.number, WordMeaning.meaning)
                query = query.filter(WordMeaning.words == word).group_by(WordMeaning.number, WordMeaning.meaning)
                results = query.all()

                for idx, result in enumerate(results):
                    similar_spellings.append({
                        "id": idx + 1,
                        "meaning_no": result.number,
                        "meaning": result.meaning,
                    })

                response = {
                    "word": word,
                    "similar_spellings": similar_spellings,

                }
                responses.append(response)

            return responses
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


# word_details_page_response
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

            for index, row in enumerate(details):

                similar_spellings.append({
                    "id": index + 1,
                    "meaning_no": row.number,
                    "meaning": row.meaning,
                    "ipa": row.ipa,
                    "pos": row.pos,
                    "spelling": row.spelling,
                    "language": row.root_lang,
                    "sentence": row.sentence,
                    "source": row.source,
                })

            response = {
                "word": word,
                "similar_spellings": similar_spellings,
            }

            return response
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
