import sqlite3

connection = sqlite3.connect("cybershield.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    source_ip TEXT,
    alert_type TEXT,
    destination_ip TEXT,
    protocol TEXT
)
""")

connection.commit()
connection.close()

print("✅ Database created successfully!")
print("✅ Alerts table is ready!")