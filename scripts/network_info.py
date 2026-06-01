import subprocess
import platform
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"Network interface info at: {timestamp}\n")

if platform.system() == "Windows":
    result = subprocess.run(["ipconfig", "/all"], capture_output=True, text=True)
else:
    result = subprocess.run(["ip", "addr"], capture_output=True, text=True)

print(result.stdout)

with open("network_info.txt", "w") as f:
    f.write(f"Network interface info at: {timestamp}\n\n")
    f.write(result.stdout)
