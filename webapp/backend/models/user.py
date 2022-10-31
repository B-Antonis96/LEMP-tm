#!/usr/bin/env python
from pydantic import BaseModel

###################
### MODEL: User ###
###################
class User(BaseModel):
    uid: str
    name: str