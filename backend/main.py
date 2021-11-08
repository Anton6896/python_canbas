from typing import Optional

from fastapi import FastAPI

server = FastAPI()
# uvicorn backend.main:server --reload


@server.get("/")
def read_root():
    return {"Hello": "World"}


@server.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


# requirements.txt