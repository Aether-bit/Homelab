import subprocess
import platform
import socket
import re
import os
import time
from datetime import datetime

os.makedirs(os.path.join(os.path.dirname(__file__), "logs"), exist_ok=True)
os.chdir(os.path.dirname(__file__))

if platform.system() == "Windows":
    ping_flag = "-n"
    trace_cmd = "tracert"
else:
    ping_flag = "-c"
    trace_cmd = "traceroute"

def ping_check():
    print("\nPing Check\n")
    ip = input("Enter target IP: ")
    label = input("Enter a label: ")

    result = subprocess.run(["ping", ping_flag, "5", ip], capture_output=True, text=True)
    
    print(result.stdout)
    
    loss_match = re.search(r"(\d+)% packet loss", result.stdout)
    loss = loss_match.group(1) + "%" if loss_match else "unknown"

    if result.returncode == 0:
        match = re.search(r"time[=<]([\d.]+)", result.stdout)
        ms = match.group(1) + "ms" if match else "unknown"
        summary = f"{label} ({ip}) - UP [{ms}] [Loss: {loss}]"
    else:
        summary = f"{label} ({ip}) - DOWN [Loss: {loss}]"
    
    print(summary)

    with open("logs/ping_results.txt", "w") as f:
        f.write(f"Ping check run at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(result.stdout + "\n")
        f.write(summary + "\n")
    
def dns_check():
    print("\nDNS Check\n")
    domain = input("Enter domain to look up: ")
    dns_server = input("Enter DNS server to query (default 8.8.8.8): ") or "8.8.8.8"
    
    result = subprocess.run(["nslookup", domain, dns_server], capture_output=True, text=True)
    status = "RESOLVING" if result.returncode == 0 else "FAILED"
    line = f"{domain} via {dns_server} - {status}"
    print(line)
    print(result.stdout)
    
    with open("logs/dns_results.txt", "w") as f:
        f.write(f"DNS check run at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(line + "\n\n")
        f.write(result.stdout)

def traceroute_check():
    target = input("\nEnter IP or domain to trace: ")
    print(f"\nTracing route to {target}...\n")
    result = subprocess.run([trace_cmd, target], capture_output=True, text=True)
    print(result.stdout)
    with open("logs/traceroute_results.txt", "w") as f:
        f.write(f"Traceroute at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(result.stdout)

def port_check():
    print("\nPort Check\n")
    ip = input("Enter target IP: ")
    port = int(input("Enter port number: "))
    name = input("Enter a label (e.g. 'Customer SMTP'): ")
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((ip, port))
    sock.close()
    status = "OPEN" if result == 0 else "CLOSED"
    line = f"{name} ({ip}:{port}) - {status}"
    print(line)
    
    with open("logs/port_results.txt", "w") as f:
        f.write(f"Port check run at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(line + "\n")

def latency_log():
    target = input("\nEnter IP to monitor (default 8.8.8.8): ") or "8.8.8.8"
    runs = 10
    interval = 2
    results = []
    print(f"\nPinging {target} {runs} times...\n")
    with open("logs/latency_log.txt", "w") as f:
        f.write(f"Latency log at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for i in range(runs):
            ts = datetime.now().strftime("%H:%M:%S")
            result = subprocess.run(["ping", ping_flag, "1", target], capture_output=True, text=True)
            if result.returncode == 0:
                match = re.search(r"time[=<]([\d.]+)", result.stdout)
                ms = float(match.group(1)) if match else None
                line = f"[{ts}] {ms}ms"
                results.append(ms)
            else:
                line = f"[{ts}] TIMEOUT"
            print(line)
            f.write(line + "\n")
        if results:
            summary = f"\nAverage: {sum(results)/len(results):.1f}ms | High: {max(results)}ms | Low: {min(results)}ms"
            print(summary)
            f.write(summary + "\n")

def reverse_dns():
    ip = input("\nEnter IP to look up: ")
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        print(f"{ip} -> {hostname}")
    except socket.herror:
        print(f"{ip} -> No PTR record found")

def network_info():
    print("\nNetwork interfaces:\n")
    result = subprocess.run(["ip", "addr"] if platform.system() != "Windows" else ["ipconfig", "/all"], capture_output=True, text=True)
    print(result.stdout)
    with open("logs/network_info.txt", "w") as f:
        f.write(f"Network info at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(result.stdout)

while True:
    print("\n=== NOC Toolkit ===")
    print("1. Ping Check")
    print("2. DNS Check")
    print("3. Traceroute")
    print("4. Port Check")
    print("5. Latency Monitor")
    print("6. Reverse DNS Lookup")
    print("7. Network Interface Info")
    print("0. Exit")

    choice = input("\nSelect: ")

    if choice == "1":
        ping_check()
    elif choice == "2":
        dns_check()
    elif choice == "3":
        traceroute_check()
    elif choice == "4":
        port_check()
    elif choice == "5":
        latency_log()
    elif choice == "6":
        reverse_dns()
    elif choice == "7":
        network_info()
    elif choice == "0":
        print("Exiting.")
        break
    else:
        print("Invalid option.")
