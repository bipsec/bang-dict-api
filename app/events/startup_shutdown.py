from fastapi import FastAPI
from app.db.database import database


async def startup_event():
    # Initialize the database connection
    await database.connect()


async def shutdown_event():
    # Close the database connection
    await database.disconnect()


def register_events(app: FastAPI):
    app.add_event_handler("startup", startup_event)
    app.add_event_handler("shutdown", shutdown_event)
