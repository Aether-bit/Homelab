# TCP vs UDP — Common Ports

How to reason about which transport protocol fits a given service, plus the Network+ port table.

## The decision rule

Ask: **does this protocol need every byte, in order, reliably?**

- **Yes** → TCP. Connection-oriented, ordered, retransmitting. Think "phone call."
- **No** (or it can't afford the setup cost) → UDP. Fire-and-forget. Think "shouting across the room."

## TCP fits when…

- A session needs every byte (SSH, file transfers, web pages)
- Order matters (streaming video over TCP, email)
- Reliability is more important than latency

## UDP fits when…

- Each message is small and self-contained (DNS queries, NTP)
- You don't yet have an IP (DHCP — TCP needs two known IPs to connect)
- Low latency beats reliability (voice, video, gaming)
- Retransmission would hurt more than help (NTP — a stale packet is worse than a missing one)

## Common ports

| Port | Service | TCP/UDP | Why |
|------|---------|---------|-----|
| 20/21 | FTP | TCP | File transfer needs reliability |
| 22 | SSH | TCP | Shell session needs every byte in order |
| 23 | Telnet | TCP | Same as SSH but unencrypted |
| 25 | SMTP | TCP | Email transfer needs reliability |
| 53 | DNS | UDP (TCP fallback) | Tiny queries, TCP setup overhead too costly |
| 67/68 | DHCP | UDP | No IP yet, must broadcast |
| 69 | TFTP | UDP | Simple file transfer, tolerates loss |
| 80 | HTTP | TCP | Web pages need complete byte streams |
| 110 | POP3 | TCP | Email retrieval |
| 123 | NTP | UDP | Tiny periodic packets, retransmit hurts accuracy |
| 143 | IMAP | TCP | Email retrieval |
| 161 | SNMP | UDP | Network monitoring, small messages |
| 389 | LDAP | TCP | Directory queries |
| 443 | HTTPS | TCP | Encrypted web (HTTP/3 uses QUIC over UDP) |
| 445 | SMB | TCP | File sharing |
| 514 | Syslog | UDP | Log shipping, can tolerate loss |
| 636 | LDAPS | TCP | Encrypted LDAP |
| 989/990 | FTPS | TCP | Encrypted FTP |
| 993 | IMAPS | TCP | Encrypted IMAP |
| 995 | POP3S | TCP | Encrypted POP3 |
| 3389 | RDP | TCP | Remote desktop session |

## Edge cases worth knowing

- **DNS** is UDP first, TCP as fallback (large responses, zone transfers, DNSSEC).
- **HTTP/3** runs over **QUIC**, which is built on UDP. For Network+, HTTP is still TCP — but the real-world picture is shifting.
- **DHCP** must be UDP because the client has no IP when it sends Discover. TCP requires two known IPs to establish a connection.

## Mental shortcut for the exam

If you can't remember a specific port's transport:

- **Anything that's a "session"** (SSH, RDP, HTTP, FTP, SMB, email) → TCP
- **Anything that's a "single small message"** (DNS, DHCP, NTP, SNMP, Syslog, TFTP) → UDP

That gets you 90% of the table without rote memorisation.
