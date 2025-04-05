from pymongo import MongoClient

client = MongoClient(!!! STRING AQUI !!!)

db = client.library_db

collection_name = db["user"]

