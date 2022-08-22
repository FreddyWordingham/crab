from fastapi.templating import Jinja2Templates
from pydantic import BaseSettings
import os


class Environment(BaseSettings):
    DATABASE_URL: str
    CLIENT_ORIGIN: str
    MAIN_DATABASE: str

    class Config:
        env_prefix = ""
        case_sentive = False
        env_file = "./../.env"
        env_file_encoding = "utf-8"


ENV = Environment()


APP_DIR = "app"
TEMPLATES_DIR = os.path.join(APP_DIR, "templates")

TEMPLATES = Jinja2Templates(directory=TEMPLATES_DIR)
