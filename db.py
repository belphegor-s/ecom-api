import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

connection = MongoClient(str(os.getenv("MONGOURI")))