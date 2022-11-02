#!/usr/bin/env python
import mysql.connector
from mysql.connector import MySQLConnection, CMySQLConnection
from models.message import Message
import services.conf_service as conf

#########################
### SERVICE: Database ###
#########################

# Declarations
user_table: str = "users"
message_table: str = "messages"

#########################
### PRIVATE FUNCTIONS ###

# Try connect to database
def __open_connection() -> CMySQLConnection | MySQLConnection:
    try:
        return mysql.connector.connect(
            host = conf.DB_HOST,
            port = "3306",
            user = conf.DB_USER,
            password = conf.DB_PASSWORD,
            database = conf.DB_DATABASE
        )
    except Exception as ex:
        raise ex

# Get all entries from table
def __get_all_entries(table: str):
    try:
        with __open_connection() as db_con:
            with db_con.cursor(buffered=True) as cursor:
                cursor.execute(f"SELECT * FROM {table}")
                data = cursor.fetchall()
                db_con.close()
                if data:
                    return data
                else:
                    return f"No entries for {table} found!"
    except Exception as ex:
        raise ex

# Insert entry into database
def __insert_entry(operation: str, *params: str):
    try:
        with __open_connection() as db_con:
            with db_con.cursor(buffered=True) as cursor:
                cursor.execute(
                    operation , 
                    (params) 
                )
                db_con.commit()
                db_con.close()
                return True
    except Exception as ex:
        raise ex

########################
### PUBLIC FUNCTIONS ###

### Messages ###
# Get all Message entries
def get_messages():
    data = __get_all_entries(message_table)
    messages: list[Message] = []
    for mssg in data:
        messages.append(Message(mssg))
    return messages

# Insert entry into "Messages"
def insert_message(message: Message):
    if __insert_entry(f"INSERT INTO {message_table} (sender, text) VALUES (%s, %s)", \
    f"{message.sender}", f"{message.text}") is True:
        return "Message send!"
    
