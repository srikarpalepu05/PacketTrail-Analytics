import sqlite3


conn = sqlite3.connect("traffic.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS traffic_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip_address TEXT,
    port INTEGER,
    bytes_transferred INTEGER
)
""")

# Simulated traffic data
sample_data = [
    ("192.168.1.10", 80, 2048),
    ("192.168.1.15", 443, 5096),
    ("10.0.0.5", 22, 1024),
    ("192.168.1.10", 8080, 3072),
    ("10.0.0.8", 3306, 4096)
]

cursor.executemany(
    "INSERT INTO traffic_logs (ip_address, port, bytes_transferred) VALUES (?, ?, ?)",
    sample_data
)

# Query for analysis
cursor.execute("""
SELECT ip_address, SUM(bytes_transferred) as total_bytes
FROM traffic_logs
GROUP BY ip_address
ORDER BY total_bytes DESC
""")

results = cursor.fetchall()

print("High-usage IP addresses:")
for row in results:
    print(row)

conn.commit()
conn.close()
