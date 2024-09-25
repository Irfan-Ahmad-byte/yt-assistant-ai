# api_gateway/config.py
from dataclasses import dataclass
from dotenv import load_dotenv, find_dotenv
import os
import json

load_dotenv(find_dotenv())


@dataclass
class Config:
    API_KEY = os.getenv("API_KEY")
    TOKEN = os.getenv("TOKEN")
    ORIGINS = json.loads(os.getenv("ORIGINS"))
    DATABASE_URL = os.getenv("DATABASE_URL")