import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import WordMeaning
from database import SessionLocal


def load_csv_to_database(csv_file_path, session: Session, table_name):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    try:
        # Iterate through each row in the DataFrame and add it to the database
        for _, row in df.iterrows():
            word_meaning = WordMeaning(
                pageNo=row["pageNo"],
                words=row['word'],
                number=row["number"],
                spelling=row['pronunciation'],
                meaning=row['meaning'],
                pos=row["pos"],
                ipa=row['IPA [B]'],
                root_lang=row['language'],
                type=row['class'],
                sentence=row['sentence'],
                source=row['source']
            )
            session.add(word_meaning)

        # Commit the changes to the database
        session.commit()
        print(f"Data from {csv_file_path} loaded into {table_name} table successfully.")
    except Exception as e:
        # Handle any exceptions here (e.g., data type mismatch)
        session.rollback()
        print(f"Error: {str(e)}")


# Example usage:
csv_file_path = '/home/bip/PycharmProjects/pythonProject/bang-dict-api/app/data/demo_data.csv'
table_name = 'word_meaning'  # Replace with your table name
db = SessionLocal()
# Assuming you have a Session instance (db) already created using your database connection
load_csv_to_database(csv_file_path, db, table_name)
