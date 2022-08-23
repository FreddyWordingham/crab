from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
import json

from .database import DB
from .settings import TEMPLATES


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
async def homepage(request: Request):
    return TEMPLATES.TemplateResponse("pages/index.html", {"request": request})


@app.get("/db")
async def get_all():
    return DB.collection.find()


@app.post("/db")
async def add_new(request: Request):
    record: dict = await request.json()
    record = json.loads(record)

    try:
        ans = DB.collection.insert_one(record)
    except Exception as err:
        raise HTTPException(
            status_code=404, detail=f'Failed to add new record: "{err}"'
        )

    return f"{ans.inserted_id}"
