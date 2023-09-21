from fastapi import APIRouter, HTTPException
import pandas as pd
import pathlib

router = APIRouter()

data_path = pathlib.Path(__file__).absolute().parents[1] / "data" / "demo_data.csv"

# Load the CSV data into a DataFrame
data = pd.read_csv(data_path)
data = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

data = data.fillna('')


@router.get("/dictionary/words")
async def get_similar_spellings(word: str):
    try:
        filtered_data = data[data["word"] == word]
        print(filtered_data)

        grouped_data = filtered_data.groupby(["number", "meaning"])["word"].count().reset_index()

        similar_spellings = []
        for idx, row in grouped_data.iterrows():
            similar_spellings.append({
                "id": idx + 1,
                "meaning_no": row["number"],
                "meanings": [row["meaning"]]
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
async def get_all_words():
    all_words = data["word"].unique().tolist()
    all_responses = []
    for word in all_words:
        similar_spellings = []
        filtered_data = data[data["word"] == word]
        grouped_data = filtered_data.groupby(["number", "meaning"])["word"].count().reset_index()
        for idx, row in grouped_data.iterrows():
            similar_spellings.append({
                "id": idx + 1,
                "meaning_no": row["number"],
                "meanings": [row["meaning"]]
            })

        response = {
            "similar_spellings": similar_spellings,
            "word": word
        }
        all_responses.append(response)

    return all_responses


@router.get("/dictionary/words_by_letter")
async def get_words_by_letter(letter: str):
    if len(letter) != 1 or not letter.isalpha():
        raise HTTPException(status_code=400, detail="Invalid input. Please provide a single letter.")

    filtered_data = data[data["word"].str.startswith(letter, na=False)]

    responses = []
    for word in filtered_data["word"].unique():
        similar_spellings = []
        word_data = filtered_data[filtered_data["word"] == word]
        grouped_data = word_data.groupby(["number", "meaning"])["word"].count().reset_index()
        for idx, row in grouped_data.iterrows():
            similar_spellings.append({
                "id": idx + 1,
                "meaning_no": row["number"],
                "meaning": row["meaning"],
            })

        response = {
            "similar_spellings": similar_spellings,
            "word": word
        }
        responses.append(response)

    return responses


# this should be the actual response while searching after words
@router.get("/dictionary/word")
async def get_word_details(word: str):
    details = data[data["word"] == word]
    similar_spellings = []
    ipa = ""
    pronunciation = ""
    details.reset_index(drop=True, inplace=True)
    for index, row in details.iterrows():
        if row["pronunciation"]:
            ipa = row["pronunciation"]
        similar_spellings.append({
            "id": index + 1,
            "meaning_no": row["number"],
            "meaning": row["meaning"],
            "pos": row["pos"],
            "language": row["language"],
            "sentence": row["sentence"],
            "source": row["source"],
        })

    response = {
        "word": word,
        "similar_spellings": similar_spellings,
        "pronunciation": pronunciation
    }

    return response
