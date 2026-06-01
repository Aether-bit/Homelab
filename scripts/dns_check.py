import subprocess
import platform
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

domains = [
    "google.com",
    "cloudflare.com",
    "bbc.co.uk",
]

with open("dns_results.txt", "w") as f:
    f.write(f"DNS check run at: {timestamp}\n\n")
    for domain in domains:
        result = subprocess.run(["nslookup", domain], capture_output=True, text=True)
        if result.returncode == 0:
            line = f"{domain} - RESOLVING"
        else:
            line = f"{domain} - FAILED"
        print(line)
        f.write(line + "\n")
