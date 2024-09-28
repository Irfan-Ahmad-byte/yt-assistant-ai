from fastapi import Depends, HTTPException
from fastapi import APIRouter
from fastapi.responses import JSONResponse, PlainTextResponse



app = APIRouter()



@app.post("/users/")
def create_user():
    return {"message": "User has been created successfully."}
