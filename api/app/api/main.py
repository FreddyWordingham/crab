from fastapi import FastAPI

from .database import DB
from .settings import ENV


app = FastAPI()


@app.get("/")
async def homepage():
    return ENV.MAIN_DATABASE
