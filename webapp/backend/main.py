#!/usr/bin/env python
from typing import Union
from fastapi import FastAPI
from models.message import Message
import services.db_service as db
import services.conf_service as conf

# FastAPI
app = FastAPI()

# Get root
@app.get("/")
async def get_root():
    app = conf.APPLICATION
    return {"Hello": "root" if app is None else app}

# Get messages
@app.get("/messages/")
async def get_messages():
    return db.get_all_entries("messages")

# Get message
@app.get("/messages/{message_id}")
async def get_message(message_id: int, q: Union[str, None] = None):
    return {"message_id": message_id, "q": q}

# Post target
@app.post("/messages/")
async def post_message(message: Message):
    return db.insert_message(message)




@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}