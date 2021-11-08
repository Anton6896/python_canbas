from typing import Optional

from fastapi import FastAPI

server = FastAPI()
# uvicorn backend.main:server --reload


@server.get("/")
def read_root():
    return {"Hello": "World"}
