import subprocess
import platform
import re
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if platform.system() == "Windows":
    ping_flag = "-n"
else:
    ping_flag = "-c"

hosts = [
    ("8.8.8.8", "Google DNS"),
    ("1.1.1.1", "Cloudflare DNS"),
    ("192.168.1.1", "Local Gateway"),
    ("10.0.0.1", "Internal Network"),
    ("172.16.0.1", "Private Range"),
]

with open("ping_results.txt", "w") as f:
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
