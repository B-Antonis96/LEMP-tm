#!/usr/bin/env python
import mysql.connector
from mysql.connector import Error, MySQLConnection, CMySQLConnection
from models.message import Message

# Connection settings
connection_string = {
    "host": "localhost",
    "user": "lemp",
    "password": "lemp",
    "db": "lemp"
}

# Try connect to database
def __open_connection() -> CMySQLConnection | MySQLConnection:
    try:
        return mysql.connector.connect(**connection_string)
    except Exception as e:
        raise e

# Get all entries from table
def get_all_entries(table: str):
    try:
        db_con = __open_connection()
        cursor = db_con.cursor(buffered=True)
        cursor.execute(f"SELECT * FROM {table}")
        data = cursor.fetchall()
        db_con.close()
        if data:
            return data
        else:
            return f"No {table} yet..."
    except Exception as e:
        return str(e)

# Get all Message entries
def get_messages():
    return get_all_entries("messages")

# Get message entry
def get_message():
    pass

# Insert entry into "Messages"
def insert_message(message: Message) -> str:
    try:
        db_con = __open_connection()
        cursor = db_con.cursor(buffered=True)
        cursor.execute(
                "INSERT INTO messages (sender, text) VALUES (%s, %s)", 
                (f"{message.sender}", f"{message.text}")
            )
        db_con.commit()
        db_con.close()
        return "Message sent!"
    except Exception as e:
        return str(e)
