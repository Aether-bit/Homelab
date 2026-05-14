# Session 2 — Cloud image VM, the long way round

## End state
SSH'd into a Debian 13 VM from CachyOS host using:
- libvirt + virt-manager stack on CachyOS
- Debian generic cloud qcow2 image
- cloud-init seed ISO (user-data.yaml with SSH key, user, password, packages)
- virt-install --import to create the VM without an installer
- ed25519 SSH key for passwordless authentication

## The journey
Started with the Debian netinst ISO. Hit DHCP failures (UFW), then
apt mirror failures (likely related). Decided to switch to the cloud-image
approach — closer to how real infrastructure is actually deployed anyway.

Hit a cascade of issues:
- session vs system libvirt confusion (virt-install --connect qemu:///system)
- file permissions for system libvirt to access disks
- VM created with --graphics none so no display to see what was happening
- DHCP requests reaching virbr0 but dnsmasq never logging them
- Eventually traced to virbr0 being in NO-CARRIER state — no tap device
  attached. net-destroy && net-start left the bridge in weird state.
- Restart of the VM forced reattachment and brought virbr0 back to UP
- DHCP still didn't work (not chased further) — set static 192.168.122.50
  manually inside VM
- SSH from host worked immediately once bridge was healthy

## Real lessons
- Cloud images + cloud-init > clicking through installers. Always. This is
  how production works.
- libvirt has two separate "instances": session (user) and system (root).
  They have separate networks, separate VMs, separate everything. Mixing
  them up causes endless confusion.
- "DHCP isn't working" is rarely a DHCP problem. It's usually firewall,
  bridge state, or socket binding. tcpdump on the bridge interface is the
  single most useful diagnostic.
- UFW on Arch-based distros doesn't play nice with libvirt out of the box.
  Needs explicit rules for virbr0 inbound DHCP (port 67/udp), and the
  default INPUT chain processing can swallow packets before user rules see them.
- When all else fails: destroy the VM and restart it. Bridge attachment
  is recreated cleanly.

## TODO next session
- Figure out why DHCP doesn't work from cloud-init even with bridge healthy
- Properly configure UFW to coexist with libvirt (or accept that it doesn't
  and run without it on the lab desktop)
- Make the VM survive a reboot with netowrking still working
- Setup SSH config alias so I can just "ssh debian-lab-1" instead of typing the IP
