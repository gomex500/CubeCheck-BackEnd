from http import client
from pymongo import MongoClient
from src.configs.config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client['cubecheck']

def collections(collection):
    collection = db[collection]
    return collection