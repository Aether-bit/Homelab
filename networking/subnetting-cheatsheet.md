# Subnetting Cheatsheet

Quick-reference for IPv4 subnetting using the block-size method. Built for Network+ and real infrastructure work.

## The 3-step process

Given any IP + CIDR, follow these three steps every time:

1. **Host bits** = `32 - N`
2. **Block size** = `2^(host bits)`
3. **Usable hosts** = `block size - 2`

## The powers-of-2 ladder

Memorise this — you'll use it constantly.

| Power | Value |
|-------|-------|
| 2^1 | 2 |
| 2^2 | 4 |
| 2^3 | 8 |
| 2^4 | 16 |
| 2^5 | 32 |
| 2^6 | 64 |
| 2^7 | 128 |
| 2^8 | 256 |
| 2^9 | 512 |
| 2^10 | 1024 |
| 2^12 | 4096 |

## CIDR reference table

| CIDR | Host bits | Block size | Usable hosts |
|------|-----------|------------|--------------|
| /24 | 8 | 256 | 254 |
| /25 | 7 | 128 | 126 |
| /26 | 6 | 64 | 62 |
| /27 | 5 | 32 | 30 |
| /28 | 4 | 16 | 14 |
| /29 | 3 | 8 | 6 |
| /30 | 2 | 4 | 2 |

Don't memorise the table — derive it from the 3-step process.

## Finding which subnet an IP lives in

Given an IP and CIDR like `192.168.1.100/27`:

1. **Block size** for /27 = 32
2. **List block boundaries** in the interesting octet, counting up by block size:
   `.0 .32 .64 .96 .128 .160 .192 .224`
3. **Find the largest boundary ≤ the host octet** — that's the network start
4. Apply the formulas:
   - **Network** = block start
   - **Broadcast** = `start + block size - 1`
   - **Usable** = `network + 1` → `broadcast - 1`

### Worked example: `192.168.1.100/27`

- Block size: 32
- Boundaries: 0, 32, 64, 96, 128…
- .100 falls in the **.96 block**
- Network: `192.168.1.96`
- Broadcast: `192.168.1.127` (96 + 32 − 1)
- Usable: `192.168.1.97 – 192.168.1.126`

### Worked example: `172.16.5.200/28`

- Block size: 16
- Boundaries: 0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, **192**, 208…
- .200 falls in the **.192 block**
- Network: `172.16.5.192`
- Broadcast: `172.16.5.207` (192 + 16 − 1)
- Usable: `172.16.5.193 – 172.16.5.206`

## Reserved addresses (per subnet)

Every subnet sacrifices two addresses:

- **Network address** — all host bits zero. Identifies the network itself. Never assigned to a host.
- **Broadcast address** — all host bits one. Sends to every host on the subnet. ARP and DHCP Discover use this.

That's why usable hosts = `block size - 2`.

## The pattern to internalise

> **An IP address is 32 bits split into network and host portions. The CIDR `/N` says the first N bits are network. Everything else follows from that.**

## Common mistakes

- **Treating the mask value as the block size.** For /27 the mask is `255.255.255.224`. The 224 is the mask, not the block size. Block size = 256 − 224 = 32.
- **Forgetting to subtract 2.** Total addresses vs usable hosts are different numbers.
- **Bracketing usable range outside the block.** Usable always sits *inside* network and broadcast: `network+1 → broadcast−1`.
- **Confusing block boundaries between CIDRs.** /26 boundaries are 0, 64, 128, 192. /27 boundaries are 0, 32, 64, 96, 128, 160, 192, 224. Don't mix them up.
