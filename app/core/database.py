import mysql.connector
from mysql.connector import MySQLConnection
from config import DB_CONFIG


def get_connection() -> MySQLConnection:
    return mysql.connector.connect(**DB_CONFIG)


def execute(query: str, params: tuple = (), fetch: str = None):
    """
    Pomocnik do wykonywania zapytań.
    fetch: None | 'one' | 'all'
    Zwraca lastrowid przy INSERT/UPDATE, dane przy SELECT.
    """
    conn = get_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute(query, params)
        if fetch == "one":
            return cur.fetchone()
        if fetch == "all":
            return cur.fetchall()
        conn.commit()
        return cur.lastrowid
    finally:
        conn.close()