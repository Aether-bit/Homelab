import subprocess
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Ping check run at: {timestamp}\n")

hosts = [
    ("8.8.8.8", "Google DNS"),
    ("1.1.1.1", "Cloudflare DNS"),
    ("192.168.1.1", "Local Gateway"),
    ("10.0.0.1", "Internal Network"),
    ("172.16.0.1", "Private Range"),
]

for ip, hostname in hosts:
    result = subprocess.run(["ping", "-c", "1", ip], capture_output=True)
    if result.returncode == 0:
        print(f"{hostname} ({ip}) - UP")
    else:
        print(f"{hostname} ({ip}) - DOWN")
