import subprocess

ips = ["8.8.8.8", "1.1.1.1", "192.168.1.1", "10.0.0.1", "172.16.0.1"]

for ip in ips:
    result = subprocess.run(["ping", "-c", "1", ip], capture_output=True)
    if result.returncode == 0:
        print(f"{ip} - UP")
    else:
        print(f"{ip} - DOWN")
