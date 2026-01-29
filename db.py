import sqlite3

def get_connection():
    return sqlite3.connect("traffic.db")

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS traffic (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip_address TEXT,
        port INTEGER,
        bytes_transferred INTEGER
    )
    """)

    conn.commit()
    conn.close()
