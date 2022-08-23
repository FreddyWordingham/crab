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


@app.get("/db")
async def get_all():
    return DB.collection.find()


@app.post("/db")
async def add_new():
    # record: dict = await request.json()
    # record = json.loads(record)
    # print(record)

    DB.collection.insert_one({"test": "test"})
    return "Doine"
