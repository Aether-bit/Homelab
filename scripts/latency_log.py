import subprocess
import platform
import re
import os
from datetime import datetime
import time

os.makedirs("logs", exist_ok=True)

if platform.system() == "Windows":
    ping_flag = "-n"
else:
    ping_flag = "-c"

target_ip = "8.8.8.8"
runs = 10
interval = 2

results = []

print(f"Pinging {target_ip} {runs} times, every {interval} seconds...\n")

with open("logs/latency_log.txt", "w") as f:
    for i in range(runs):
        ts = datetime.now().strftime("%H:%M:%S")
        result = subprocess.run(["ping", ping_flag, "1", target_ip], capture_output=True, text=True)
        if result.returncode == 0:
            match = re.search(r"time[=<]([\d.]+)", result.stdout)
            ms = float(match.group(1)) if match else None
            line = f"[{ts}] {target_ip} - {ms}ms"
            results.append(ms)
        else:
            line = f"[{ts}] {target_ip} - TIMEOUT"
        print(line)
        f.write(line + "\n")

    if results:
        avg = sum(results) / len(results)
        summary = f"\nAverage: {avg:.1f}ms | High: {max(results)}ms | Low: {min(results)}ms"
        print(summary)
        f.write(summary + "\n")
