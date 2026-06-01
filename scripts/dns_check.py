import subprocess
import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

domains = [
    "google.com",
    "cloudflare.com",
    "bbc.co.uk",
]

with open("logs/dns_results.txt", "w") as f:
    f.write(f"DNS check run at: {timestamp}\n\n")
    for domain in domains:
        result = subprocess.run(["nslookup", domain], capture_output=True, text=True)
        status = "RESOLVING" if result.returncode == 0 else "FAILED"
        line = f"{domain} - {status}"
        print(line)
        f.write(line + "\n")
