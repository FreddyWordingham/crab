from fastapi import FastAPI

from .database import DB


app = FastAPI()


@app.get("/")
async def homepage():
    return "Hello, world!"
