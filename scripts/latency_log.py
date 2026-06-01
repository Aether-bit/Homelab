import subprocess
import platform
import re
from datetime import datetime
import time

if platform.system() == "Windows":
    ping_flag = "-n"
else:
    ping_flag = "-c"

target_ip = "8.8.8.8"
runs = 10
interval = 2  # seconds between each ping

results = []

print(f"Pinging {target_ip} {runs} times, every {interval} seconds...\n")

for i in range(runs):
    timestamp = datetime.now().strftime("%H:%M:%S")
    result = subprocess.run(["ping", ping_flag, "1", target_ip], capture_output=True, text=True)
    if result.returncode == 0:
        match = re.search(r"time[=<]([\d.]+)", result.stdout)
        ms = float(match.group(1)) if match else None
        line = f"[{timestamp}] {target_ip} - {ms}ms"
        results.append(ms)
    else:
        line = f"[{timestamp}] {target_ip} - TIMEOUT"
    print(line)
    time.sleep(interval)

if results:
    avg = sum(results) / len(results)
    high = max(results)
    low = min(results)
    summary = f"\nAverage: {avg:.1f}ms | High: {high}ms | Low: {low}ms"
    print(summary)

    with open("latency_log.txt", "w") as f:
        f.write(summary + "\n")
