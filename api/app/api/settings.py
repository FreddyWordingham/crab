from fastapi.templating import Jinja2Templates
import os
import pymongo


APP_DIR = "app"
STATIC_DIR = os.path.join(APP_DIR, "static")
TEMPLATES_DIR = os.path.join(APP_DIR, "templates")

TEMPLATES = Jinja2Templates(directory=TEMPLATES_DIR)

CLIENT = pymongo.MongoClient(
    "mongodb://mongodb_container:27017/", username="root", password="rootpassword"
)
