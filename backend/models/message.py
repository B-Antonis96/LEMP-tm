#!/usr/bin/env python
from pydantic import BaseModel

######################
### MODEL: Message ###
######################
class Message(BaseModel):
    sender: str
    text: str