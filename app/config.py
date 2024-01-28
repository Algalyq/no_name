from typing import Any

from pydantic import BaseSettings
from pymongo import MongoClient
from urllib.parse import quote_plus

class Config(BaseSettings):
    CORS_ORIGINS: list[str] = ["*"]
    CORS_HEADERS: list[str] = ["*"]
    CORS_METHODS: list[str] = ["*"]

    MONGOHOST: str = "localhost"
    MONGOPORT: str = "8000"
    MONGOUSER: str = "aa"
    MONGOPASSWORD: str = "123"
    MONGODATABASE: str = "Cluster0"
    MONGO_URL: str = "mongodb+srv://algalyq:2003720an@cluster0.bosxgra.mongodb.net/?retryWrites=true&w=majority"

# environmental variables
env = Config()
mongo_url = "mongodb+srv://algalyq:2003720an@cluster0.bosxgra.mongodb.net/?retryWrites=true&w=majority"

# FastAPI configurations
fastapi_config: dict[str, Any] = {
    "title": "API test",
}

    
# MongoDB connection
client = MongoClient(mongo_url)

# MongoDB database
database = client[env.MONGODATABASE]