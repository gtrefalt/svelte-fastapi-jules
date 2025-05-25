from fastapi import FastAPI
from typing import Dict

app = FastAPI()

@app.get("/")
async def read_root() -> Dict[str, str]:
    return {"message": "Hello from FastAPI backend!"}

@app.get("/api/data")
async def get_data() -> Dict[str, str]:
    return {"message": "This is some data from FastAPI", "source": "Python backend"}

# To run this app (from the backend directory, with .venv activated):
# uvicorn main:app --reload
