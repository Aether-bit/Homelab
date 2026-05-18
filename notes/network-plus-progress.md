# Network+ Study Progress

Currently working through Network+. Finding it fairly straightforward so far.

## ✅ Confident — likely pass

- TCP & UDP Ports Quiz
- Subnetting Quiz
- IPv4 Addressing Quiz
- IPv6 Addressing Quiz
- Routing Technologies Quiz
- DHCP Quiz
- DNS Quiz
- OSI Reference Model Quiz
- Switching Technologies Quiz
- Network Protocols Quiz
- Basic Networking Device Commands Quiz
- Troubleshooting Methodology Quiz
- Basic Network Security Concepts Quiz
- Common Attack Types Quiz
- Wireless Networking Quiz
- Cloud Computing Concepts Quiz
- Network Cabling Quiz
- Cable Connectors Quiz
- Network Documentation Quiz

## 🔴 Not yet covered

- Networking Appliances Quiz
- Network Designs Quiz
- Infrastructure as Code (IaC) Quiz
- Physical Installations Quiz
- 802.3 Standards Quiz
- Network Monitoring Quiz
- Disaster Recovery (DR) Concepts Quiz
- Network Access & Management Methods Quiz
- Cabling Issues Troubleshooting Quiz
- Physical Interface Issues Troubleshooting Quiz
- Hardware Issues Troubleshooting Quiz
- Network Services Troubleshooting Quiz
- Common Performance Issues Troubleshooting Quiz
- Software Troubleshooting Tools Quiz
- Hardware Troubleshooting Tools Quiz

## Notes for myself

### OSI Layers
**PDNTSPA** (bottom up) or *Please Do Not Throw Sausage Pizza Away*
Physical → Data Link → Network → Transport → Session → Presentation → Application

Quick layer ID:
- Has IP → L3
- Has port → L4
- Talks to humans → L7

### Subnetting
- Host bits = `32 - N`
- Block size = `2^(host bits)`
- Usable hosts = block size − 2
- Network = block start. Broadcast = start + block size − 1. Usable = network+1 → broadcast−1.

### Routing
- No `via` = ARP destination directly
- `via X` = ARP the router (X)

### Transport
- DNS = UDP first, TCP fallback
- DHCP must be UDP (no IP yet, broadcasts)
- SSH/HTTP/HTTPS = TCP

### Routing protocols
- Inside company → OSPF
- Between companies / internet → BGP
- RIP max hop = 15

### VLAN
- L2 separation. Need L3 to cross VLANs.
- Access port = one VLAN, untagged. Trunk = multiple VLANs, 802.1Q tagged.
- VLAN ID = 12-bit, 1–4094 usable.

### IPv6
- 128 bit. 8 groups of 4 hex digits, colons.
- Drop leading zeros. One `::` only (longest run of zeros).
- `::1` = loopback. `fe80:` = link-local. `2xxx:`/`3xxx:` = global unicast. `fc/fd` = unique local private.
- No ARP — uses NDP. No broadcast — uses multicast.
- `/64` = standard subnet.

### Security
- **CIA**: Confidentiality (encryption), Integrity (hashing), Availability (backup/redundancy)
- IDS = detect, IPS = prevent (blocks)
- Stateful firewall remembers connections.

### Attacks
- Whaling = phishing the CEO. Spear phishing = targeted. Vishing = phone. Smishing = SMS.
- ARP spoofing enables MITM.
- DDoS = many attackers. DoS = one.
- Worm spreads itself, virus needs a host file + user.

### Wireless
- 2.4 GHz = long range, slow, crowded. 5 GHz = short, fast. 6 GHz = newest, empty.
- 2.4 GHz non-overlapping channels: 1, 6, 11.
- WPA2 = AES. WPA3 = newest. WEP = dead.
- PSK = home (one password). 802.1X + RADIUS = enterprise.
- WiFi 6 = 802.11ax. WiFi 7 = 802.11be.

### Cloud
- IaaS = VMs (you do OS up). PaaS = platform (you bring code). SaaS = finished app.
- Shared responsibility: provider = hardware/datacentre. You = data + accounts. Middle depends on model.
- Public / Private / Hybrid / Community deployment.

### Cabling
- Copper max 100m (Cat8 = 30m).
- Cat5e = 1G. Cat6 = 1G (10G short). Cat6a = 10G. Cat8 = 25–40G.
- Same device type = crossover. Different = straight-through.
- T568B = modern standard.
- Single-mode fibre = long-haul (km). Multi-mode = short (~500m). LC connector common in data centres.

### Documentation
- IPAM = IP address management. SLA = uptime promise. AUP = user rules. Baseline = "normal" snapshot to compare against.

## Update log

- **2026-05-18** — Big push. Added: OSI, switching/VLANs/STP, network protocols, device commands, troubleshooting methodology, IPv6, security/CIA, attack types, wireless, cloud, cabling, documentation. ~20% → ~55% confident coverage.
- **2026-05-17** — Networking deep-dive: L2 vs L3, NAT, DHCP DORA, DNS resolution, ARP, packet flow capstone (`ssh debian` walkthrough).
