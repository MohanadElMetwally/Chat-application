from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

client = MongoClient('mongodb://localhost:27017')

def get_db() -> Database:
    return client['sessions_db']

def get_collection() -> Collection:
    database = get_db()
    return database['sessions_collection']