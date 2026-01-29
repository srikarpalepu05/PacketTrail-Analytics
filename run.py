from packettrail.db import initialize_db
from packettrail.ingest import ingest_csv
from packettrail.report import generate_report

initialize_db()
ingest_csv("data/sample_traffic.csv")
generate_report()
