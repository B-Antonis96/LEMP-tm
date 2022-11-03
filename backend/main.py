#!/usr/bin/env python
from fastapi import FastAPI
import uvicorn
from models.message import Message
import services.db_service as db
import services.conf_service as conf

#########################
### MAIN: Application ###
#########################

# FastAPI
app = FastAPI()

# Get root
@app.get("/")
async def get_root():
    info = conf.APPLICATION
    return {"Hello": info if info else "root"}

# Get messages
@app.get("/messages/")
async def get_messages():
    return db.get_messages()

# Post message
@app.post("/messages/")
async def post_message(message: Message):
    return db.insert_message(message)

# Main app run
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
