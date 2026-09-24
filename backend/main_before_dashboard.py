from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
import sqlite3
import os
import re

app = FastAPI(title="CyberNexus")

# -----------------------------
# Paths
# -----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE = os.path.join(
    BASE_DIR,
    "cybershield.db"
)

# frontend folder is INSIDE backend
FRONTEND_FILE = os.path.join(
    BASE_DIR,
    "frontend",
    "index.html"
)

# -----------------------------
# WAF Patterns
# -----------------------------

WAF_PATTERNS = [
    r"('|--|;)",
    r"\bOR\b\s+\d+\s*=\s*\d+",
    r"<script.*?>",
    r"javascript:",
    r"onerror\s*="
]


def detect_waf_threat(text):
    for pattern in WAF_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return True

    return False


# -----------------------------
# WAF Middleware
# -----------------------------

@app.middleware("http")
async def waf_middleware(request: Request, call_next):

    query_text = str(request.query_params)

    if detect_waf_threat(query_text):
        return JSONResponse(
            status_code=403,
            content={
                "status": "blocked",
                "message": "Suspicious request detected by CyberNexus WAF"
            }
        )

    response = await call_next(request)

    return response


# -----------------------------
# Home / Dashboard
# -----------------------------

@app.get("/")
def home():

    return FileResponse(FRONTEND_FILE)


# -----------------------------
# Alerts API
# -----------------------------

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

    alerts = [
        dict(row)
        for row in cursor.fetchall()
    ]

    connection.close()

    return {
        "total_alerts": len(alerts),
        "alerts": alerts
    }