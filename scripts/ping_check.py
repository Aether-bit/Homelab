import subprocess
import platform
import re
import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if platform.system() == "Windows":
    ping_flag = "-n"
else:
    ping_flag = "-c"

hosts = []
with open("hosts.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line:
            parts = line.split(" ", 1)
            hosts.append((parts[0], parts[1]))

with open("logs/ping_results.txt", "w") as f:
    f.write(f"Ping check run at: {timestamp}\n\n")
    for ip, hostname in hosts:
        result = subprocess.run(["ping", ping_flag, "1", ip], capture_output=True, text=True)
        if result.returncode == 0:
            match = re.search(r"time[=<]([\d.]+)", result.stdout)
            ms = match.group(1) + "ms" if match else "unknown"
            line = f"{hostname} ({ip}) - UP [{ms}]"
        else:
            line = f"{hostname} ({ip}) - DOWN"
        print(line)
        f.write(line + "\n")
