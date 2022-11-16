#!/usr/bin/env python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from models.message import Message
import services.db_service as db
import services.conf_service as conf

#########################
### MAIN: Application ###
#########################

# FastAPI
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get root
@app.get("/")
async def get_root():
    return {"Hello": conf.APPLICATION}

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
