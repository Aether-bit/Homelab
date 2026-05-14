# Homelab

Notes, configs, and projects as I learn infrastructure engineering.

## Current state

Running on CachyOS desktop (16GB RAM, 12th gen i9, RTX 4070).

Two Linux VMs on libvirt:
- **debian-lab-1** (192.168.122.50) — Debian 13
- **ubuntu-lab-1** (192.168.122.51) — Ubuntu 24.04 LTS

Both provisioned via cloud-init, reachable from host via SSH aliases.

## Layout

- `configs/` — host configuration files (SSH config, etc.)
- `docs/` — workflow documentation
- `notes/` — session notes and lessons learned
- `vms/` — cloud-init configs per VM

## Building from scratch

See `docs/build-vms.md`.

## Background

- CompTIA A+ certified, studying Network+
- Daily-driving CachyOS, fish shell
- Targeting infrastructure / cloud engineering roles
