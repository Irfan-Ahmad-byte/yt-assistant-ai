# api_gateway/handlers/authentication.py

from typing import Annotated
from fastapi import Header, HTTPException

from fastapi import HTTPException, Depends, Header
from fastapi.security import APIKeyHeader
from app.config.config import Config

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


async def get_api_key(api_key_header: str = Depends(api_key_header)):
    if api_key_header is None or api_key_header != Config.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return api_key_header


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != Config.TOKEN:
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    return x_token