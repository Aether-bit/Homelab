# Troubleshooting: Docker containers had no network access

/ Date: 2026-05-21 /

## Symptom

Containers could not reach the internet. `apt-get update` inside any
container hung on every mirror with `Ign:` / `Temporary failure resolving`.
Image builds failed at the `apt` step.

## Diagnosis

Worked through it layer by layer rather than guessing:

1. **Host internet** — `ping 8.8.8.8` from the host worked. Host was fine.
2. **Container DNS** — `/etc/resolv.conf` in a container showed the correct
   nameservers. DNS config was being applied.
3. **DNS vs connectivity** — a raw TCP test by IP returned a failure. This
   proved the problem was not DNS — the container could not reach the
   internet at all, even by IP.
4. **NAT** — Docker's MASQUERADE rule was present and correct, but with a
   `0 packets` counter — traffic was not even reaching it.
5. **IP forwarding** — `net.ipv4.ip_forward` was `1`. Not the cause.
6. **nftables** — `nft list ruleset` revealed the cause: a native nftables
   `inet filter` table with an empty `forward` chain set to `policy drop`.

## Root cause

The host firewall is native nftables (`/etc/nftables.conf`), with the
`forward` chain defaulting to `policy drop` and no accept rules. Docker writes
its rules via the iptables compatibility layer into separate tables. Forwarded
container packets hit the nftables `forward` chain first and were dropped
before ever reaching Docker's rules.

## Fix

`/etc/nftables.conf` includes `/etc/nftables.d/*.nft`, so a drop-in file was
added rather than editing the main ruleset:

    # /etc/nftables.d/docker.nft
    add rule inet filter forward iifname "docker0" accept
    add rule inet filter forward oifname "docker0" accept

These allow traffic in from and out to Docker's `docker0` bridge through the
`forward` chain. Confirmed persistent by restarting `nftables` and re-testing.

## Note

This is a lab-grade fix — it broadly accepts all `docker0` forward traffic,
acceptable on a personal lab box but looser than a hardened production host
would want.

## Update 2026-05-26 - Compose bridge not covered

Docker Compose creates its own bridge per project (br-<hash>), not docker0, so the original docker0-only nftables rule did not cover Compose traffic - same policy drop symptom returned.

Fix: generalised the drop-in to a br-* wildcard so all current and future Compose networks are covered.

Final /etc/nftables.d/docker.nft:

    add rule inet filter forward iifname "docker0" accept
    add rule inet filter forward oifname "docker0" accept
    add rule inet filter forward iifname "br-*" accept
    add rule inet filter forward oifname "br-*" accept
