from fastapi import FastAPI
from fastapi.responses import FileResponse
import sqlite3
import os

app = FastAPI(title="CyberNexus")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE = os.path.join(BASE_DIR, "cybershield.db")

FRONTEND_FILE = os.path.join(
    BASE_DIR,
    "..",
    "frontend",
    "index.html"
)


@app.get("/")
def home():
    return FileResponse(FRONTEND_FILE)


@app.get("/alerts")
def get_alerts():

    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            timestamp,
            source_ip,
            destination_ip,
            protocol,
            alert_type
        FROM alerts
        ORDER BY id DESC
    """)

    alerts = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return {
        "total_alerts": len(alerts),
        "alerts": alerts
    }