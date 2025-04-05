from pymongo import MongoClient
import dotenv, os

dotenv.load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))

db = client.library_db

collection_name = db["user"]

