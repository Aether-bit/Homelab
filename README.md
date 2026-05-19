# Home Lab

A personal lab I'm using to learn IT infrastructure hands-on while studying toward CompTIA Network+ and Security+.

This repo is a working notebook: setup steps, configuration notes, things that broke, and how I fixed them. It's part of how I'm proving to myself (and hopefully a future employer) that I can do the work, not just talk about it.

## Host

- **OS:** CachyOS (Arch-based Linux), daily-driven
- **Shell:** Fish
- **Hardware:** Custom desktop, 12th-gen Intel, 16GB RAM, NVMe SSD, RTX 4070
- **Hypervisor:** KVM / QEMU with virt-manager

## Current setup

Currently running 2 to 3 concurrent Linux guests for hands-on practice:

- Debian server (general Linux admin practice)
- Ubuntu server (package management, services)

Using thin-provisioned qcow2 disks and VM save/resume so the box stays usable for normal daily work alongside the lab.

## What I'm practising

- Linux installation and post-install configuration
- User and permission management (sudo, groups, file permissions)
- Package management (apt, pacman)
- SSH between host and guests, key-based auth
- Basic system hardening (UFW, fail2ban, disabling root login)
- Network troubleshooting basics (ping, traceroute, ss, dig)

## What's next

- Windows Server guest for Active Directory practice
- Ansible for configuration management (configuring guests from playbooks rather than by hand)
- Documenting each step properly as it happens

## Notes

The `notes/` folder has my running study notes for Network+ and lab journal entries as I go.

## Why this exists

I'm an entry-level candidate. A home lab on a CV is meaningless without evidence, so this repo is the evidence. If you're a hiring manager reading this: hello. Happy to talk through any of it.
