from pymongo import MongoClient
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

username = quote_plus(os.getenv("MONGO_USERNAME"))
password = quote_plus(os.getenv("MONGO_PASSWORD"))

MONGO_URI = "mongodb+srv://deepikasidral:deepika@cluster0.7vcfybt.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)

db = client["heart_disease_db"]

users_collection = db["users"]
predictions_collection = db["predictions"]