from fastapi import Request
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.executors.agent import get_answer



app = APIRouter()



@app.get("/ask")
def create_user(query: str):
    return StreamingResponse(get_answer(query), media_type="text/plain")