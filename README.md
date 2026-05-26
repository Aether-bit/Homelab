# Home Lab

A personal lab I'm using to learn cloud and DevOps engineering hands-on,
while studying toward CompTIA Network+, Security+, and Microsoft Azure
certifications.

This repo is a working notebook: setup steps, configuration notes, things that
broke, and how I fixed them. It's part of how I'm proving to myself (and
hopefully a future employer) that I can do the work, not just talk about it.

## Direction

I'm working toward a Cloud / DevOps Engineer role. The lab starts with solid
Linux and networking fundamentals, then builds upward into virtualisation,
infrastructure as code, containers, CI/CD, and Azure.

See [roadmap.md](roadmap.md) for my certification path and skills roadmap.

## Host

- **OS:** CachyOS (Arch-based Linux), daily-driven
- **Shell:** Fish
- **Hardware:** Custom desktop, 12th-gen Intel, 16GB RAM, NVMe SSD
- **Hypervisor:** KVM / QEMU with virt-manager

## Current setup

Currently running 2 to 3 concurrent Linux guests for hands-on practice:

- Debian server (general Linux admin practice)
- Ubuntu server (package management, services)

VMs are provisioned with cloud-init (see `vms/`) using static IPs and
key-only SSH. Disks are thin-provisioned qcow2 with save/resume, so the box
stays usable for normal daily work alongside the lab.

## What I'm practising now

- Linux installation, configuration, and administration
- User and permission management (sudo, groups, file permissions)
- Package management (apt, pacman)
- SSH between host and guests, key-based authentication
- Network troubleshooting basics (ping, traceroute, ss, dig)
- Beginning system hardening (firewall rules, fail2ban, disabling root login)

## Roadmap toward Cloud / DevOps

- **Infrastructure as code** — Terraform for provisioning, Ansible for
  configuration management, replacing manual VM setup with reproducible codes
- **Containers** — Docker done: fundamentals, volumes, Compose (sessions 4-5); Kubernetes next
- **CI/CD** — GitHub Actions pipelines, starting with linting and testing
  the configs and scripts in this repo
- **Cloud (Azure)** — working toward AZ-900, then AZ-104; deploying the
  lab patterns here into Azure rather than only local VMs
- **Scripting** — Bash and Python for automation tasks

## Repo layout

- `docs/` — focused writeups, e.g. a full SSH connection walkthrough and
  VM build notes
- `notes/` — running study notes and lab journal entries
- `networking/` — reference material: subnetting, routing tables, ports
- `configs/` — reusable config such as my homelab SSH config
- `vms/` — per-VM cloud-init provisioning files

## Why this exists

I'm an entry-level candidate. A home lab on a CV is meaningless without
evidence, so this repo is the evidence. If you're a hiring manager reading
this: Hello. Happy to talk through any of it.
