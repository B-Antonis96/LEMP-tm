#!/usr/bin/env python
import os

#######################
### SERVICE: Config ###
#######################

# Environment variables
APPLICATION = os.getenv('APPLICATION')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DATABASE = os.getenv('DB_DATABASE')

# Environments list
envs: list[str | None] = [APPLICATION, 
                          DB_HOST, 
                          DB_PORT, 
                          DB_USER, 
                          DB_PASSWORD, 
                          DB_DATABASE]

# Checking if every environment variable is declared
# Else raise custom exception
class EnvError(Exception):
    pass
for env in envs:
    if env is None:
        raise EnvError(f"{env} is not declared! (null)")
