import mysql.connector
from mysql.connector import MySQLConnection
from config import DB_CONFIG


def get_connection() -> MySQLConnection:
    return mysql.connector.connect(**DB_CONFIG)

def execute(query: str, params: tuple = (), fetch: str = None) -> MySQLConnection:
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params)
        if fetch == "one":
            return cursor.fetchone()
        elif fetch == "all":
            return cursor.fetchall()
        conn.commit()
        return cursor.lastrowid
    finally:
        conn.close()