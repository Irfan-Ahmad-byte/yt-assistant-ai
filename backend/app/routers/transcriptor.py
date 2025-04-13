from fastapi import APIRouter
from fastapi.responses import JSONResponse
from random import random

from pydantic import BaseModel

from app.executors.agent import get_answer
from app.executors.vector_store import create_neo4j_vector_store
from app.executors.yt_transcribe import get_transcription
from app.workers.manage_transcript import store_transcript



app = APIRouter()

class Transcribe(BaseModel):
    url: str


@app.post("/transcribe")
def upload_file(data: Transcribe):
    text = get_transcription(data.model_dump_json("url"))
    # generate a unique random id
    id = int(random()*100000)
    t = store_transcript(id, text)
    return JSONResponse(content={"transcription": text, "id": id})