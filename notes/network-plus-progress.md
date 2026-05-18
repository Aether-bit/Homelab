# Network+ Study Progress

Currently working through Network+. Finding it fairly straightforward so far.

## ✅ Confident — likely pass

- TCP & UDP Ports Quiz
- Subnetting Quiz
- IPv4 Addressing Quiz
- Routing Technologies Quiz
- DHCP Quiz
- DNS Quiz

## 🟡 Partial — touched but needs a top-up

- OSI Reference Model Quiz — L2/L3 solid, L4–L7 shaky
- Switching Technologies Quiz — bridges/MAC tables yes, VLANs/STP/trunk ports no
- Network Protocols Quiz — ARP/ICMP yes, OSPF/BGP/EIGRP no
- Basic Networking Device Commands Quiz — Linux (`ip route`, `ip neigh`, `ss`) yes, Cisco IOS no
- Troubleshooting Methodology Quiz — diagnostic instincts yes, formal CompTIA 7-step methodology no

## 🔴 Not yet covered

- Networking Appliances Quiz
- Cloud Computing Concepts Quiz
- Wireless Networking Quiz
- 802.3 Standards Quiz
- Network Cabling Quiz
- Cable Connectors Quiz
- Network Designs Quiz
- Infrastructure as Code (IaC) Quiz
- IPv6 Addressing Quiz
- Physical Installations Quiz
- Network Documentation Quiz
- Network Monitoring Quiz
- Disaster Recovery (DR) Concepts Quiz
- Network Access & Management Methods Quiz
- Basic Network Security Concepts Quiz
- Common Attack Types Quiz
- Cabling Issues Troubleshooting Quiz
- Physical Interface Issues Troubleshooting Quiz
- Hardware Issues Troubleshooting Quiz
- Network Services Troubleshooting Quiz
- Common Performance Issues Troubleshooting Quiz
- Software Troubleshooting Tools Quiz
- Hardware Troubleshooting Tools Quiz

## Notes for myself

- 7 OSI Layers: **PDNTSPA** — Physical, Data, Network, Transport, Session, Presentation, Application
- L3 routing rule: no `via` = ARP destination directly; `via X` = ARP the router
- Subnetting block size = `2^(32-N)`; usable hosts = block size − 2
- DNS = UDP first, TCP fallback. DHCP must be UDP (no IP yet). SSH/HTTP/HTTPS = TCP.

## Update log

- **2026-05-18** — Patched L3 routing tables and TCP/UDP port weak spots; locked in subnetting fluency for /25–/30 using the block-size method.
- **2026-05-17** — Networking deep-dive: L2 vs L3, NAT, DHCP DORA, DNS resolution, ARP, packet flow capstone (`ssh debian` walkthrough).
