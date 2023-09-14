from http import client
from pymongo import MongoClient
from src.configs.config import MONGO_URI

#inicializando conexion con mongo
client = MongoClient(MONGO_URI)
db = client['cubecheck']

#funcio apar obtener una collection
def collections(collection):
    collection = db[collection]
    return collection