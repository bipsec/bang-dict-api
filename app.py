import os
import csv
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

data_file_path = os.path.join("data", "demo_data.csv")
df = pd.read_csv(data_file_path)


# print(df)
@app.route('/dictionary', methods=['GET'])
def get_word_details():
    word = request.args.get('word')
    if not word:
        return "Word parameter not found"

    # Filter rows where the 'word' column matches the input word
    filtered_df = df[df['word'] == word]
    if filtered_df.empty:
        return "Word parameter not found"

    # Create the response dictionary
    response = {
        'word': word,
        'similar_spellings': []
    }
    # Create a dictionary to store meanings based on meaning_no
    meaning_dict = {}

    # Iterate through the filtered DataFrame and construct the response
    for idx, row in filtered_df.iterrows():
        meaning = row['meaning']
        meaning_no = row['number']

        if meaning_no in meaning_dict:
            meaning_dict[meaning_no]["meanings"].append(meaning)
        else:
            meaning_dict[meaning_no] = {
                'id': len(meaning_dict) + 1,
                'meaning_no': meaning_no,
                'meanings': [meaning]
            }

    # Append the meanings to the response similar_spellings list
    response['similar_spellings'] = list(meaning_dict.values())

    return jsonify(response)


@app.route('/dictionary/words', methods=['GET'])
def get_words_from_letter():
    letter = request.args.get('letter')
    if not letter:
        return "letter parameter not found"

    words = df[df['word'].str.startswith(letter)]['word'].tolist()

    response = {
        "letter": letter,
        "words": words
    }
    return jsonify(response)


@app.route('/dictionary/all-words', methods=['GET'])
def get_all_word_details():
    # Create a dictionary to store all word details
    all_word_details = {}

    # Iterate through the entire DataFrame and construct the response for each word
    for _, row in df.iterrows():
        word = row['word']
        meaning = row['meaning']
        meaning_no = row['number']

        # Check if the word exists in the dictionary
        if word in all_word_details:
            word_entry = next(
                (entry for entry in all_word_details[word]['similar_spellings'] if entry['meaning_no'] == meaning_no),
                None)

            if word_entry:
                # If meaning_no exists, append the meaning to its 'meanings' list
                word_entry['meanings'].append(meaning)
            else:
                # If meaning_no doesn't exist, create a new entry
                new_entry = {
                    'id': len(all_word_details[word]['similar_spellings']) + 1,
                    'meaning_no': meaning_no,
                    'meanings': [meaning]
                }
                all_word_details[word]['similar_spellings'].append(new_entry)
        else:
            # If the word doesn't exist, create a new entry
            all_word_details[word] = {
                'word': word,
                'similar_spellings': [{
                    'id': 1,
                    'meaning_no': meaning_no,
                    'meanings': [meaning]
                }]
            }

    return jsonify(list(all_word_details.values()))


if __name__ == '__main__':
    app.run(debug=True)
