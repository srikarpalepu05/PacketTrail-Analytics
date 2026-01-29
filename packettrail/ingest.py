import csv
from packettrail.db import get_connection

def ingest_csv(path):
    conn = get_connection()
    cursor = conn.cursor()

    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                "INSERT INTO traffic (ip_address, port, bytes_transferred) VALUES (?, ?, ?)",
                (row["ip_address"], int(row["port"]), int(row["bytes"]))
            )

    conn.commit()
    conn.close()
