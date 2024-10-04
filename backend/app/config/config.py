# api_gateway/config.py
from dataclasses import dataclass
from dotenv import load_dotenv, find_dotenv
import os
import json

load_dotenv(find_dotenv())


@dataclass
class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    API_KEY = os.getenv("API_KEY", "")
    TOKEN = os.getenv("TOKEN", "")
    ORIGINS = json.loads(os.getenv("ORIGINS", "*"))
    MODEL = os.getenv("MODEL", "gpt-3.5-turbo")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
    NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")
