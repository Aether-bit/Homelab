# virt-manager setup on CachyOS

## What I installed
- qemu-full, virt-manager, virt-viewer, libvirt, edk2-ovmf, swtpm
- (dnsmasq already present, bridge-utils deprecated on Arch — not needed)

## Setup steps
1. Verified VT-x enabled: `grep -E 'vmx|svm' /proc/cpuinfo`
2. Installed the stack with pacman
3. Enabled libvirtd: `sudo systemctl enable --now libvirtd.service`
4. Added user to libvirt group: `sudo usermod -aG libvirt kieran`
5. Rebooted to pick up group membership
6. Verified `default` virtual network active: `sudo virsh net-list --all`

## Gotcha I hit
Logging out and back in didn't pick up the new group membership on KDE.
A reboot fixed it. Worth remembering for next time.

## Next
Create first Debian VM (ISO downloading: debian-13.4.0-amd64-netinst.iso)
