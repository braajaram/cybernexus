from scapy.all import sniff, IP, TCP
from collections import defaultdict
import time
import sqlite3

connections = defaultdict(list)
last_alert_time = {}


def save_alert(source_ip, destination_ip, protocol):
    connection = sqlite3.connect("cybershield.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO alerts
        (timestamp, source_ip, alert_type, destination_ip, protocol)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            time.ctime(),
            source_ip,
            "Suspicious activity",
            destination_ip,
            protocol
        )
    )

    connection.commit()
    connection.close()


def detect_scan(pkt):

    if IP in pkt and TCP in pkt:

        source_ip = pkt[IP].src
        destination_ip = pkt[IP].dst
        protocol = "TCP"

        current_time = time.time()

        connections[source_ip] = [
            t for t in connections[source_ip]
            if current_time - t < 10
        ]

        connections[source_ip].append(current_time)

        if len(connections[source_ip]) > 20:

            # Avoid repeated alerts for the same IP
            if (
                source_ip not in last_alert_time
                or current_time - last_alert_time[source_ip] > 30
            ):

                print(
                    f"⚠️ ALERT: {source_ip} → "
                    f"{destination_ip} | {protocol}"
                )

                with open("alerts.log", "a") as file:
                    file.write(
                        f"{time.ctime()} | "
                        f"{source_ip} | "
                        f"{destination_ip} | "
                        f"{protocol} | "
                        f"Suspicious activity\n"
                    )

                save_alert(
                    source_ip,
                    destination_ip,
                    protocol
                )

                last_alert_time[source_ip] = current_time

            connections[source_ip].clear()


print("🛡️ CyberNexus IDS started...")
print("Monitoring network traffic...")

sniff(prn=detect_scan, store=0)