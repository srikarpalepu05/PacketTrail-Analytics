from packettrail.db import get_connection

def high_usage_ips(limit=5):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT ip_address, SUM(bytes_transferred) AS total_bytes
    FROM traffic
    GROUP BY ip_address
    ORDER BY total_bytes DESC
    LIMIT ?
    """, (limit,))

    results = cursor.fetchall()
    conn.close()
    return results

def non_standard_ports():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT DISTINCT port
    FROM traffic
    WHERE port NOT IN (80, 443, 22)
    """)

    results = cursor.fetchall()
    conn.close()
    return results
