from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.executors.agent import get_answer



app = APIRouter()



@app.get("/ask")
def ask(id: int, query: str):
    return StreamingResponse(get_answer(id, query), media_type="text/plain")