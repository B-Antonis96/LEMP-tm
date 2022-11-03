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

### Messages ###
# Get all Message entries
def get_messages():
    try:
        with __open_connection() as db_con:
            with db_con.cursor(buffered=True) as cursor:
                cursor.execute(f"SELECT * FROM {message_table}")
                data = cursor.fetchall()
                db_con.close()
                if data:
                    messages: list[Message] = []
                    for mssg in data:
                        messages.append(Message(sender=mssg[1], text=mssg[2]))
                    return messages
                else:
                    return f"No entries for {message_table} found!"
    except Exception as ex:
        raise ex

# Insert entry into "Messages"
def insert_message(message: Message):
    try:
        with __open_connection() as db_con:
            with db_con.cursor(buffered=True) as cursor:
                cursor.execute(
                    f"INSERT INTO {message_table} (sender, text) VALUES (%s, %s)" , 
                    (f"{message.sender}", f"{message.text}")
                )
                db_con.commit()
                db_con.close()
                return "Message send!"
    except Exception as ex:
        raise ex
