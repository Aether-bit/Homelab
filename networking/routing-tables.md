# Linux Routing Tables

How the Linux kernel decides where to send a packet.

## The mental model

Every Linux host has a **routing table**. When the kernel has a packet with a destination IP, it walks the table top to bottom and picks the **most specific match**. That rule tells it:

- Which interface to send out of (`dev`)
- Which next-hop IP to send to (`via`) — if any
- Which source IP to stamp on the packet (`src`)

View it with:

```bash
ip route
```

## Reading a routing table

Example output:

```
default via 192.168.1.254 dev wlan0 proto dhcp src 192.168.1.193 metric 600
192.168.1.0/24 dev wlan0 proto kernel scope link src 192.168.1.193 metric 600
192.168.122.0/24 dev virbr0 proto kernel scope link src 192.168.122.1 linkdown
```

| Line | Meaning |
|------|---------|
| Line 1 | Anything not matched by a more specific rule → send to router 192.168.1.254 via wlan0 |
| Line 2 | Anything 192.168.1.x → directly reachable on wlan0, no router needed |
| Line 3 | Anything 192.168.122.x → directly reachable on virbr0 (VM network), currently `linkdown` because no VM is running |

## The two route types

Every route is one of two patterns:

| Has `via`? | Meaning | What the kernel does |
|------------|---------|----------------------|
| **No** (just `dev`) | Destination is on a local network | ARP for the destination's MAC, send the frame directly |
| **Yes** (`via X`) | Destination is remote | ARP for X's MAC, send the frame to the router |

That's the whole model.

## Field reference

- `default` — matches anything (0.0.0.0/0). The catch-all.
- `via X` — next-hop router IP. Only present for remote networks.
- `dev INTERFACE` — physical or virtual interface to send out of.
- `src X` — source IP to stamp on outgoing packets.
- `proto kernel` — route was auto-added by the kernel (e.g. for a directly attached subnet).
- `proto dhcp` — route was added by the DHCP client.
- `scope link` — destination is on the directly attached link.
- `metric N` — priority when multiple routes match (lower wins).
- `linkdown` — interface exists but has no active link.

## What happens during `ssh debian`

Concrete walkthrough using the table above and `debian` resolving to 192.168.122.50:

1. **Hostname resolution** — `~/.ssh/config` checked for alias options, then `/etc/hosts` (then DNS) for IP lookup. Result: 192.168.122.50.
2. **Routing table lookup** — kernel matches 192.168.122.50 against the table. Most specific match: line 3, `192.168.122.0/24 dev virbr0`.
3. **No `via`** — destination is directly reachable. Kernel needs the MAC of 192.168.122.50.
4. **ARP** — kernel broadcasts "who has 192.168.122.50?" on virbr0. The VM replies with its MAC. Cached in `ip neigh`.
5. **Frame built and sent** — Ethernet frame with VM's MAC as destination, sent via virbr0.
6. **Bridge forwards** — virbr0 is a software switch, delivers the frame to the VM's virtual NIC.
7. **VM stack processes** — TCP/IP stack receives, sees TCP port 22, hands to sshd.
8. **Key exchange + auth** — Diffie-Hellman establishes encryption first, then key/password auth.
9. **Shell allocated** — sshd attaches a PTY and gives you a shell prompt.

## Useful commands

```bash
ip route              # show routing table
ip route get 8.8.8.8  # show which rule would match a destination
ip neigh              # show ARP cache (who has which MAC)
ss -tunlp             # show listening sockets (what's on port 22?)
```

## The takeaway

L3 forwarding on Linux is just: **match against the table, ARP for the right MAC, send the frame**. Everything more complex (policy routing, multiple tables, dynamic routing protocols) is variations on this skeleton.
