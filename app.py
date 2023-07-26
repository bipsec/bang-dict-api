import os
import csv
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

data_file_path = os.path.join("data", "demo_data.csv")
df = pd.read_csv(data_file_path)


# print(df)


@app.route('/dictionary/all_words', methods=['GET'])
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
