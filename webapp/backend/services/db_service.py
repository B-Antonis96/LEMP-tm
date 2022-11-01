#!/usr/bin/env python
import mysql.connector
from mysql.connector import MySQLConnection, CMySQLConnection
from models.message import Message
from models.user import User
import conf_service as conf

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
            port = conf.DB_PORT,
            user = conf.DB_USER,
            password = conf.DB_PASSWORD,
            database = conf.DB_DATABASE
        )
    except Exception as ex:
        raise ex

# Get all entries from table
def get_all_entries(table: str):
    try:
        with __open_connection() as db_con:
            with db_con.cursor(buffered=True) as cursor:
                cursor.execute(f"SELECT * FROM {table}")
                data = cursor.fetchall()
                db_con.close()
                if data:
                    return data
                else:
                    return None
    except Exception as ex:
        raise ex


# Get User entry with UID
def get_user(uid: str) -> User | None:
    try:
        with __open_connection() as db_con:
            with db_con.cursor(buffered=True) as cursor:
                cursor.execute(f"SELECT * FROM {user_table} WHERE 'uid' = {uid}")
                data = cursor.fetchone()
                db_con.close()
                return User(uid=data['uid'], name=data['name']) if data else None
    except Exception as ex:
        raise ex

# Get all Message entries
def get_messages():
    return get_all_entries(user_table)

# Insert entry into "Messages"
def insert_message(message: Message) -> str:
    try:
        with __open_connection() as db_con:
            with db_con.cursor(buffered=True) as cursor:
                cursor.execute(
                        f"INSERT INTO {message_table} (sender, text) VALUES (%s, %s)", 
                        (f"{message.sender}", f"{message.text}")
                    )
                db_con.commit()
                db_con.close()
                return "Message sent!"
    except Exception as ex:
        raise ex
