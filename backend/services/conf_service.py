#!/usr/bin/env python
import os

#######################
### SERVICE: Config ###
#######################

# Environment variables
application = os.getenv('APPLICATION')
APPLICATION = application if application else 'LEMP-tm'
db_host = os.getenv('DB_HOST')
DB_HOST = db_host if db_host else 'localhost'
db_user = os.getenv('DB_USER')
DB_USER = db_user if db_user else 'lemp'
db_password = os.getenv('DB_PASSWORD')
DB_PASSWORD = db_password if db_password else 'lemp'
db_database = os.getenv('DB_DATABASE')
DB_DATABASE = db_database if db_database else 'lemp'