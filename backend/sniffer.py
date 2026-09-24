from scapy.all import sniff, IP

def packet_callback(pkt):
    if IP in pkt:
        print(f"Source: {pkt[IP].src} -> Destination: {pkt[IP].dst}")

print("Packet Sniffer started... Press Ctrl+C to stop")

sniff(prn=packet_callback, store=0)

