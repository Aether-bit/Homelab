import socket
import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

targets = [
    ("8.8.8.8", 53, "Google DNS"),
    ("1.1.1.1", 53, "Cloudflare DNS"),
    ("8.8.8.8", 443, "Google HTTPS"),
    ("192.168.1.1", 80, "Local Gateway HTTP"),
]

with open("logs/port_results.txt", "w") as f:
    f.write(f"Port check run at: {timestamp}\n\n")
    for ip, port, name in targets:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((ip, port))
        sock.close()
        status = "OPEN" if result == 0 else "CLOSED"
        line = f"{name} ({ip}:{port}) - {status}"
        print(line)
        f.write(line + "\n")
