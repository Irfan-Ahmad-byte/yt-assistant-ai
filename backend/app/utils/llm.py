

from langchain_openai import ChatOpenAI
from app.config.config import Config



def get_llm():
    return ChatOpenAI(temperature=0, model_name=Config.MODEL, openai_api_key=Config.OPENAI_API_KEY)