from pydantic import BaseSettings


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
