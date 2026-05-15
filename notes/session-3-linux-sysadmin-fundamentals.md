# Session 3 — Linux sysadmin fundamentals

## Goal

Understand what we actually did in sessions 1 and 2, not just copy-paste it.
Sessions 1 and 2 were "make it work." This one was "know why it worked."

## What I covered

### Users and groups

- Every action on Linux is done by some user. There's no "no user" — even
  background services run as a specific user identity.
- Users are entries in `/etc/passwd`. The kernel only cares about UIDs
  (numbers), not usernames. Names are a display convenience.
- `/etc/passwd` is world-readable on purpose (so UID → name lookups work
  for everyone). `/etc/shadow` is root-only and holds the password hashes.
  Splitting them was a 90s security fix.
- Groups are collections of users. A user has one primary group and any
  number of supplementary groups.
- `usermod -aG <group> <user>` adds a user to a supplementary group.
  The `-a` is critical — without it, `-G` *replaces* all groups, which is
  catastrophic (you can lose `wheel` and your ability to sudo).
- Group changes don't apply to existing sessions — your shell loaded its
  group list at login. Reboot or fresh login to pick up changes. On KDE,
  logging out doesn't always work cleanly; reboot is the reliable answer.
- `sudo` lets you run commands as another user (usually root). It reads
  `/etc/sudoers`. The line `%wheel ALL=(ALL:ALL) ALL` is why being in
  the `wheel` group matters.

### File permissions

- Three categories: owner, group, other. Three permissions each: read,
  write, execute.
- Symbolic form: `rwxr-xr--`. Octal form: `754`. r=4, w=2, x=1, added per
  category. Three digits total, one per category.
- **For files**: r=read content, w=modify content, x=run as program.
- **For directories**: r=list contents (`ls`), w=create/delete/rename
  files inside, x=traverse into (`cd`). This is the gotcha — directory
  "execute" means "you're allowed through this door."
- `chmod a+r` = add read for all. `chmod 600` = owner rw, no one else.
  `chmod 700` = owner rwx, no one else (private executables/directories).
- `chown user:group` = change ownership. Needs root unless you already
  own the file.
- SSH refuses to use keys unless `~/.ssh/` is 700 and the private key
  is 600. Same paranoia as `/etc/shadow`.

This is why we needed `chmod a+x` on `/home/kieran`, `/home/kieran/vms`,
and `/home/kieran/vms/debian-lab-1` yesterday — every directory in the
path to the disk file needed traversal permission for libvirt-qemu.

### systemctl and services

- systemd is pid 1, the first thing after the kernel. systemctl is how
  you talk to it.
- A service has two independent states:
  - **Active vs inactive** — running right now or not
  - **Enabled vs disabled** — will start at boot or not
- Four useful combinations: active+enabled (healthy), active+disabled
  (temporary), inactive+enabled (will come up on next boot),
  inactive+disabled (dormant).
- Failed is different from inactive(dead). Failed = crashed.
  inactive(dead) = stopped cleanly or hasn't started yet.
- `start`, `stop`, `enable`, `disable`, `restart`, `reload`. `--now` does
  start+enable in one go.
- `reload` re-reads config without dropping connections (gentler).
  Not all services support it. `reload-or-restart` handles that.
- Unit files live in `/usr/lib/systemd/system/` (distro-shipped, don't
  edit) and `/etc/systemd/system/` (your local overrides).

### journalctl

- Replaced the old `/var/log/*` text files with a unified structured
  journal.
- Useful flags:
  - `-u <unit>` — filter to one service
  - `-e` — jump to end (most recent)
  - `-f` — follow live (like tail -f)
  - `--since "10 minutes ago"` — time filter
  - `-p err` — severity filter (err or worse)
  - `--no-pager` — print to terminal instead of opening less
- Without `/var/log/journal/` existing, logs are in tmpfs and vanish on
  reboot. Most modern distros enable persistence by default.

### The ip command

Three independent concepts:

- **Link** — an interface (cable). Physical or virtual.
- **Address** — an IP assigned to a link.
- **Route** — a rule about where to send packets.

Interfaces have two states layered: admin (UP/DOWN, set by software) and
carrier (LOWER_UP/NO-CARRIER, set by reality). Both must be good for
traffic to flow.

CIDR notation: `/24` = 24 network bits, 8 host bits, 256 addresses.
Standard home-network size.

Runtime commands (`ip addr add`) change in-memory state only. Config
files (netplan, systemd-networkd) are what persist across reboots.

When we saw `linkdown` on the virbr0 route yesterday, that was the route
existing but its underlying interface being DOWN — which is why nothing
worked even though the route was technically there.

### $PATH

- Shell finds executables by searching `$PATH` in order, first match wins
- `which <command>` shows which executable would run
- `/usr/bin` (most programs), `/usr/sbin` (admin commands), `/usr/local/bin`
  (locally installed)
- `sudo` has its own PATH which sometimes causes "command not found"
  oddness

## Things that finally clicked

1. **Why we had to chmod all the way up to /home/kieran** — directories
   need execute permission for traversal, not just the disk file
   itself. Each directory in the path is a door.

2. **Why "log out and back in" didn't work for group changes on KDE** —
   the session lingers in the background. Group membership is loaded
   when the session starts and stays cached. Reboot is the reliable fix.

3. **Active vs enabled** — I was treating these as synonyms before. They
   are completely independent. A service can be running right now but
   not configured to start on boot, or configured to start on boot but
   currently stopped. The combinations matter.

4. **Static IPs with `ip addr add` were lies** — I thought we'd "set"
   the IPs in session 2, but those commands only affect in-memory state.
   The IPs survived only because we wrote netplan/networkd configs after.
   Without those config files, the next reboot would have wiped everything.

## Things I'm still fuzzy on

1. **NAT and forwarding** — I get that my VMs have a default route to
   192.168.122.1 but I'm not 100% clear on how (or whether) packets get
   forwarded out to the actual internet via wlan0. We touched on it but
   it's still hazy. Tomorrow's networking session should cover this.

2. **Severity levels in journalctl** — I understand `err`, `warning`,
   `info` intuitively but the difference between `crit`, `alert`, and
   `emerg` is fuzzy. Probably rarely matters in practice but worth
   knowing properly.


## Commands I now actually understand from sessions 1 and 2

| Command | What I now understand it does |
|---------|-------------------------------|
| `sudo usermod -aG libvirt $USER` | As root, append libvirt to kieran's supplementary groups. The `-a` prevents replacing all other groups (which would lose wheel and break sudo). |
| `sudo systemctl enable --now libvirtd.service` | Tell systemd to start libvirtd now AND mark it to auto-start every boot. Two operations in one. |
| `sudo chown -R kieran:kieran ~/vms/debian-lab-1/` | Recursively reset ownership of all files in that directory to user kieran, group kieran. Needed because libvirt-qemu had taken ownership during a failed VM creation. |
| `chmod a+r disk.qcow2` | Add read permission for all categories (owner, group, other). Specifically so libvirt-qemu (which is in "other" from my perspective) could read the VM disk. |
| `chmod a+x /home/kieran/vms` | Add traversal permission on the directory for everyone. Without this, libvirt-qemu can't walk through the directory to reach the disk inside. |
| `sudo virsh net-dhcp-leases default` | Ask libvirt's default network for its current DHCP lease table. Empty output = no VM has been given an IP. |
| `sudo ip addr add 192.168.122.50/24 dev enp1s0` | Manually assign an IP to the VM's NIC. Runtime only — doesn't persist across reboot. We needed netplan/networkd configs for persistence. |
| `sudo systemctl status libvirtd` | Show me what state libvirtd is in: is it loaded, is it active, is it enabled, when did it start, and what are its most recent log lines. |
| `sudo journalctl -u libvirtd -f` | Tail libvirtd's logs live so I can see what it's doing while I trigger something from the VM side. |
| `ssh debian` | SSH config alias for `ssh -i ~/.ssh/id_ed25519 kieran@192.168.122.50`. Defined in `~/.ssh/config`. Saves typing and reduces typos. |

## Next session

Topic C — Linux networking proper. Bridges, NAT, DNS, what actually
happens when a packet leaves my machine. Should resolve my "how do
packets get out of the VM to the internet" question.
