from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

# Load the CSV data into a DataFrame
data = pd.read_csv("app/data/demo_data.csv")


@app.get("/dictionary/words/")
async def get_similar_spellings(word: str):
    try:
        # Filter the rows where the word matches the input word
        filtered_data = data[data["word"] == word]

        # Group the data by 'number' and 'meaning' columns
        grouped_data = filtered_data.groupby(["number", "meaning"])["word"].count().reset_index()

        # Convert the grouped data to the desired JSON format
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
        # Log the error for debugging purposes
        print("Error:", e)
        # Raise an HTTPException with a 500 status code to indicate a server error
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.get("/dictionary/all_words/")
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
