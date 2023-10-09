import os
from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy import func, or_
from sqlalchemy.orm import Session
import soundfile as sf

from app.db.database import SessionLocal, Base, get_db, WordMeaning, AudioData
from app.scripts.audio import AudioHelper

from pathlib import Path
import csv

router = APIRouter()


@router.post("/load_audio/")
async def load_csv_to_db(db: Session = Depends(get_db)):
    audio_dir = Path("app/data/audio_dir/audio50-100k/")
    if not audio_dir.exists():
        raise HTTPException(status_code=404, detail="Audio directory not found")

    for filename in os.listdir(audio_dir):
        if filename.endswith(".wav"):  # Adjust the file extension as needed
            file_path = audio_dir / filename

            try:
                # Use your AudioHelper or any method to get audio duration, type, and content
                duration = AudioHelper.get_audio_duration(file_path)
                audio_type = AudioHelper.get_audio_type(file_path)
                audio_content = AudioHelper.get_audio_content(file_path)

                if duration is not None and audio_type is not None and audio_content is not None:
                    audio_data = AudioData(
                        filename=filename,
                        duration=duration,
                        audio_type=audio_type,
                        audio_file=audio_content
                    )
                    db.add(audio_data)
            except Exception as e:
                db.rollback()
                print(f"Error: {str(e)}")

    db.commit()
    return {"message": "Audio files loaded successfully into the database"}
