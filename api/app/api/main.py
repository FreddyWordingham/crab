from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
import json

from .database import DB
from .settings import ENV, TEMPLATES


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
async def homepage(request: Request):
    return TEMPLATES.TemplateResponse(
        "pages/index.html", {"request": request, "MAIN_DATABASE": ENV.MAIN_DATABASE}
    )


@app.get("/db/{collection}")
async def get_all(collection: str):
    return DB[collection].find()


@app.post("/db/{collection}")
async def add_new(request: Request, collection: str):
    record: dict = await request.json()
    record = json.loads(record)
    print(record)

    return DB[collection].insert_one(record)
