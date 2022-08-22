from fastapi import FastAPI, Request

from .database import DB
from .settings import ENV, TEMPLATES


app = FastAPI()


@app.get("/")
async def homepage(request: Request):
    return TEMPLATES.TemplateResponse("pages/index.html", {"request": request})


@app.get("/db/{collection}")
async def get_all(collection: str):
    return DB[collection].find()


@app.post("/db/{collection}")
async def add_new(request: Request, collection: str):
    record = await request.json()
    return DB[collection].insert_one(record)
