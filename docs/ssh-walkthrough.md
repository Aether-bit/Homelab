# SSH Connection Walkthrough

What actually happens when I type `ssh debian` and get a shell on the VM.
Written as a capstone exercise after the networking deep-dive.

## Setup

The VM has to be running first:

    sudo virsh start debian-lab-1

The VM has a static IP of `192.168.122.50`. I've aliased it to `debian` so
I can type `ssh debian` instead of the full IP.

## Step by step

1. **Typing `ssh debian`.** The SSH client starts but doesn't yet know what
   "debian" means. It needs to resolve that name to an IP.

2. **Name resolution.** The alias lives in `~/.ssh/config` as a `Host debian`
   block, which also holds the IP and user. This is SSH-specific config and
   sits above the OS-level path (`/etc/hosts`, then DNS).

3. **Routing decision (L3).** The kernel checks the routing table (`ip route`)
   to pick an interface. `192.168.122.50` is on a directly attached subnet via
   `virbr0`, so it's local. Same subnet means no gateway and no routing hop.

4. **ARP for the MAC.** Before building the first frame the kernel needs the
   destination MAC. It broadcasts an ARP request ("who has 192.168.122.50"),
   gets the reply, and builds the frame.

5. **Frame travels.** Because it's the same subnet, the frame does NOT go
   through a router. It goes host -> virbr0 (the bridge) -> straight to the
   VM's virtual NIC.

6. **Transport layer.** SSH runs over TCP on port 22. The VM receives the
   frame and processes it up the stack.

7. **Key exchange and auth.** `sshd` sets up an encrypted channel first (key
   exchange), then authenticates me. With key auth, it checks my public key
   against `~/.ssh/authorized_keys` on the VM. Password is the fallback.
   On a first-ever connection there's also host key verification, where the
   VM proves its identity to me and the fingerprint is saved to
   `~/.ssh/known_hosts`.

8. **Shell.** Auth succeeds and `sshd` spawns a shell inside a pseudo-terminal
   (PTY). I'm now in.

## Key takeaways

- Same subnet = no router. Frames cross the bridge, not a router. Routers
  only come in when crossing subnets.
- `~/.ssh/config` (SSH aliases) is separate from OS name resolution
  (`/etc/hosts` -> DNS).
- Key auth checks `authorized_keys`; the host key check is the reverse
  direction (server proving itself to the client).
