from pymongo import mongo_client

from .settings import ENV


CLIENT = mongo_client.MongoClient(ENV.DATABASE_URL)
DB = CLIENT[ENV.MAIN_DATABASE]
