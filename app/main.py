from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import dictionary

app = FastAPI()


# Demo api testing
@app.get("/")
async def root():
    return {"message": "Welcome to Bangla Dictionary API. It provides data for Bangla Dictionary Web Application."}


# Including API Router
app.include_router(dictionary.router)


# Configure CORS middleware to allow requests from all origins
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])
