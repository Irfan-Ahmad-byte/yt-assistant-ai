from app.config.config import Config
from app.executors.chain import vectorstore
from langchain.docstore.document import Document
from langchain_openai import OpenAIEmbeddings
from typing import List


def load_documents(doc: str) -> List[Document]:
    embeddings = OpenAIEmbeddings(openai_api_key=Config.OPENAI_API_KEY)
    docs = vectorstore.from_documents(doc, embeddings)
    return docs