from pymongo import mongo_client
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
CLIENT = mongo_client.MongoClient(ENV.DATABASE_URL)
DB = CLIENT[ENV.MAIN_DATABASE]

print(ENV.DATABASE_URL)
print(ENV.CLIENT_ORIGIN)
print(ENV.MAIN_DATABASE)

DB.nsad.insert_one({"test": "test"})

print(DB.nsad.count())
