import subprocess
import platform
import socket
import re
import os
import time
from datetime import datetime

os.makedirs(os.path.join(os.path.dirname(__file__), "logs"), exist_ok=True)
os.chdir(os.path.dirname(__file__))

ticket = input("Enter ticket reference (or press Enter to skip): ") or "NO-REF"
print(f"\nTicket: {ticket}\n")

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
        f.write(f"Ticket: {ticket} | Ping check run at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
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
        f.write(f"Ticket: {ticket} | DNS check run at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(line + "\n\n")
        f.write(result.stdout)

def dns_propagation():
    print("\nDNS Propagation Check\n")
    domain = input("Enter domain to check: ")
    
    servers = [
        ("8.8.8.8", "Google"),
        ("1.1.1.1", "Cloudflare"),
        ("9.9.9.9", "Quad9"),
        ("208.67.222.222", "OpenDNS"),
        ("84.2.42.42", "Andrews & Arnold"),
    ]
    
    results = []
    
    for server_ip, server_name in servers:
        result = subprocess.run(["nslookup", domain, server_ip], capture_output=True, text=True)
        ip_match = re.search(r'Address:\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', result.stdout)
        resolved = ip_match.group(1) if ip_match else "FAILED"
        line = f"{server_name:<20} ({server_ip}) -> {resolved}"
        print(line)
        results.append(line)
    
    with open("logs/dns_propagation.txt", "w") as f:
        f.write(f"Ticket: {ticket} | DNS propagation check at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"Domain: {domain}\n\n")
        f.write("\n".join(results))

def traceroute_check():
    target = input("\nEnter IP or domain to trace: ")
    print(f"\nTracing route to {target}...\n")

    result = subprocess.run([trace_cmd, target], capture_output=True, text=True)
    lines = result.stdout.splitlines()

    import urllib.request
    import json

    output_lines = []

    for line in lines:
        hop_match = re.match(r'\s*(\d+)', line)
        if not hop_match:
            continue

        hop = hop_match.group(1)

        if '* * *' in line:
            output_lines.append(f"{hop:<4} * * *  timeout")
            print(output_lines[-1])
            continue

        ip_match = re.search(r'(\d{1,3}\.){3}\d{1,3}', line)
        ms_match = re.search(r'([\d.]+) ms', line)

        ip = ip_match.group(0) if ip_match else "unknown"
        ms = ms_match.group(1) + "ms" if ms_match else "unknown"

        try:
            url = f"https://ipinfo.io/{ip}/json"
            req = urllib.request.urlopen(url, timeout=2)
            data = json.loads(req.read())
            org = data.get("org", "Unknown")
        except:
            org = "Lookup failed"

        formatted = f"{hop:<4} {ip:<20} {ms:<12} [{org}]"
        output_lines.append(formatted)
        print(formatted)

    with open("logs/traceroute_results.txt", "w") as f:
        f.write(f"Ticket: {ticket} | Traceroute at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("\n".join(output_lines))

def port_check():
    print("\nPort Check\n")
    ip = input("Enter target IP: ")
    port = int(input("Enter port number: "))
    name = input("Enter a label: ")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((ip, port))
    sock.close()
    status = "OPEN" if result == 0 else "CLOSED"
    line = f"{name} ({ip}:{port}) - {status}"
    print(line)

    with open("logs/port_results.txt", "w") as f:
        f.write(f"Ticket: {ticket} | Port check run at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(line + "\n")

def latency_log():
    target = input("\nEnter IP to monitor (default 8.8.8.8): ") or "8.8.8.8"
    runs = 10
    interval = 2
    results = []
    print(f"\nPinging {target} {runs} times...\n")
    with open("logs/latency_log.txt", "w") as f:
        f.write(f"Ticket: {ticket} | Latency log at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
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
        f.write(f"Ticket: {ticket} | Network info at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(result.stdout)

def subnet_calc():
    print("\nSubnet Calculator\n")
    try:
        import ipaddress
        network = input("Enter IP and subnet (e.g. 192.168.1.0/24): ")
        net = ipaddress.IPv4Network(network, strict=False)
        print(f"\nNetwork:    {net.network_address}")
        print(f"Broadcast:  {net.broadcast_address}")
        print(f"Subnet mask:{net.netmask}")
        print(f"Usable IPs: {net.num_addresses - 2}")
        print(f"First host: {list(net.hosts())[0]}")
        print(f"Last host:  {list(net.hosts())[-1]}")
    except ValueError as e:
        print(f"Invalid input: {e}")

while True:
    print("\n=== NOC Toolkit ===")
    print(f"Ticket: {ticket}")
    print("1. Ping Check")
    print("2. DNS Check")
    print("3. Traceroute")
    print("4. Port Check")
    print("5. Latency Monitor")
    print("6. Reverse DNS Lookup")
    print("7. Network Interface Info")
    print("8. Subnet Calculator")
    print("9. DNS Propagation Check")
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
    elif choice == "8":
        subnet_calc()
    elif choice == "9":
        dns_propagation()
    elif choice == "0":
                print("Exiting.")
                if platform.system() == "Windows":
                    input("\nPress Enter to close...")
                break
    else:
        print("Invalid option.")
