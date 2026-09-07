import mysql.connector
from mysql.connector import Error


def db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Reynolds@08",
            database="newproject1"
        )
        return conn
    except Error as e:
        print(e)
        return None
