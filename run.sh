#!/bin/bash

# Run migrations (if applicable)
# Uncomment the following line if you need to run database migrations
# python app/db/migrate.py

# Start the FastAPI app with Uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload --workers 4
