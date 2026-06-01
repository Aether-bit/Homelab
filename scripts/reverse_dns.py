import socket
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

ips = [
    "8.8.8.8",
    "1.1.1.1",
    "62.172.102.70",
    "192.168.1.1",
]

with open("reverse_dns_results.txt", "w") as f:
    f.write(f"Reverse DNS lookup at: {timestamp}\n\n")
    for ip in ips:
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            line = f"{ip} -> {hostname}"
        except socket.herror:
            line = f"{ip} -> No PTR record found"
        print(line)
        f.write(line + "\n")
