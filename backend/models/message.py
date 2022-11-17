#!/usr/bin/env python
from pydantic import BaseModel
from typing import Union

######################
### MODEL: Message ###
######################
class Message(BaseModel):
    id: Union[str, None]
    sender: str
    text: str