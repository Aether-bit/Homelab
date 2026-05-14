# Session 2 — Building VMs (the long way)

## Goal

Get a working VM running on the CachyOS desktop, SSH-able from the host,
with the workflow documented and reproducible.

## End state

- libvirt + virt-manager stack working on CachyOS
- Two Linux VMs:
  - debian-lab-1 (Debian 13, 192.168.122.50)
  - ubuntu-lab-1 (Ubuntu 24.04 LTS, 192.168.122.51)
- Both built from cloud images + cloud-init (no installer clicking)
- Both with persistent static IP (Debian via systemd-networkd, Ubuntu via netplan)
- Both reachable via SSH key auth using aliases (`ssh debian`, `ssh ubuntu`)
- All configs versioned in this repo
- `docs/build-vms.md` documents the full workflow for rebuilding

## The route taken

Started with the traditional approach: Debian netinst ISO, click through
the installer. Hit a wall of issues:

- DHCP autoconfig failed in the installer. Diagnosed as UFW blocking
  forwarded traffic on virbr0. Added explicit ufw rules but still hit
  asymmetric rule problems.
- Tried manual network config in the installer. Then hit "Bad archive
  mirror" — couldn't resolve packages even with valid network config.

After hours of fighting the installer, pivoted to **cloud images + cloud-init**.
This is the modern approach: pre-installed disk image, configured declaratively
via a YAML file. Much closer to how real cloud/production infrastructure works.

Cloud image approach hit its own issues:

- `virt-install` defaulted to `qemu:///session` (user libvirt) instead of
  `qemu:///system` — they have completely separate networks.
- File permissions: system-libvirt runs as a different user, so disk and
  seed.iso need explicit read permissions plus directory traversal (`+x`)
  on parent dirs.
- DHCP still failed even with cloud-init. tcpdump showed packets reaching
  virbr0 but dnsmasq never seeing them.
- Root cause turned out to be virbr0 in `NO-CARRIER` state — no tap
  interface attached to the bridge. `net-destroy && net-start` had left
  bridge state confused. Restarting the VM forced re-attachment.
- Even after that, libvirt DHCP didn't deliver leases. Worked around by
  setting static IPs inside the VMs.

## Lessons

- **Cloud images > installers**, every time. Configuration as code, faster,
  reproducible, no clicking.
- **"DHCP doesn't work"** is almost never about DHCP. It's firewall,
  bridge state, or socket binding. tcpdump on the bridge interface is
  the single most useful diagnostic.
- **libvirt has two separate instances** — `qemu:///session` (user) and
  `qemu:///system` (root). Mixing them up causes endless confusion.
  Always be explicit with `--connect`.
- **UFW + libvirt on Arch-based distros is painful out of the box**.
  Default INPUT chain processing eats DHCP packets before user rules
  see them. For a lab, easiest path is to skip UFW and use static IPs.
- **Bridge networking is the layer below firewalls** — if `bridge link`
  shows nothing attached, no amount of firewall fiddling will help.
- **Knowing when to abandon an approach** is a real skill. 
  Three hours fighting the installer wasted; cloud images
  would have worked first try.

  ## Tooling learned

- `virt-install` — CLI VM creation, much faster than the GUI wizard
- `virsh` — libvirt management (`list`, `start`, `destroy`, `undefine`,
  `net-dhcp-leases`, `net-destroy`, `net-start`)
- `cloud-localds` — builds the cloud-init seed ISO
- `tcpdump -i virbr0 'port 67 or port 68'` — watching DHCP traffic
- `ss -ulnp` — see UDP listeners (confirming dnsmasq is bound)
- `iptables -L -v -n --line-numbers` — packet counts per rule
- `networkctl` — systemd-networkd's state inspector
- `netplan` — Ubuntu's networking abstraction
- `bridge link` — see what's attached to a Linux bridge
- `ssh ~/.ssh/config` aliases — never type a raw IP again

  ## TODO next session

- Get internet working from inside the VMs (DNS + outbound route)
- Properly fix libvirt DHCP, or document why we're skipping it
- Configure VM-to-VM SSH (try `ssh debian` from inside `ubuntu`)
- Look at snapshots so I can break and restore quickly
- Maybe add a third VM (something other than Debian/Ubuntu? Alpine? Fedora?)
