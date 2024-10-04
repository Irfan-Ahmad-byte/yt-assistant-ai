from fastapi import Request
from langchain_core.callbacks import BaseCallbackHandler

class StreamHandler(BaseCallbackHandler):
    def __init__(self, request: Request, initial_text=""):
        self.request = request

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.request.send_push_promise(token)