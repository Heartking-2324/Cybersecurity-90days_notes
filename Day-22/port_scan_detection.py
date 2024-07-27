from scapy.all import *

def detect_port_scan(packet):
    if packet.haslayer(TCP):
        # Check for SYN and ACK flags
        if packet[TCP].flags == 'S' or packet[TCP].flags == 'SA':
            # Check for unusual port numbers
            if packet[TCP].dport < 1024 or packet[TCP].sport < 1024:
                print(f"Port scan detected from {packet[IP].src} to {packet[IP].dst}")

# Start sniffing network traffic
sniff(prn=detect_port_scan)
