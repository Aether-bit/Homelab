import subprocess
import platform
import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if platform.system() == "Windows":
    trace_cmd = "tracert"
else:
    trace_cmd = "traceroute"

targets = [
    ("8.8.8.8", "Google DNS"),
    ("1.1.1.1", "Cloudflare DNS"),
]

with open("logs/traceroute_results.txt", "w") as f:
    f.write(f"Traceroute check run at: {timestamp}\n\n")
    for ip, hostname in targets:
        print(f"Tracing route to {hostname} ({ip})...")
        f.write(f"--- {hostname} ({ip}) ---\n")
        result = subprocess.run([trace_cmd, ip], capture_output=True, text=True)
        print(result.stdout)
        f.write(result.stdout + "\n")
