## Step 2 — Write the cloud-init config

cloud-init configures the VM on first boot: user, SSH key, hostname,
packages. The config lives in this repo at `vms/<vm-name>/user-data.yaml`.

The actual config for `debian-lab-1`:

    #cloud-config
    hostname: debian-lab-1
    users:
      - name: kieran
        sudo: ALL=(ALL) NOPASSWD:ALL
        shell: /bin/bash
        ssh_authorized_keys:
          - ssh-ed25519 AAAA...key... kieran@cachyos-homelab
    package_update: true
    packages:
      - vim
      - htop
      - curl

What each part does:

- `hostname` — the VM's hostname, set on first boot.
- `users` — creates the `kieran` login user. No password is set, which
  means **password login is impossible** — key-only by design.
- `sudo: ALL=(ALL) NOPASSWD:ALL` — passwordless sudo for this user.
  Convenient for a lab; in production you would require a password.
- `ssh_authorized_keys` — the host's **public** key, dropped into the
  VM's `~/.ssh/authorized_keys`. This is what makes `ssh debian` work
  without a password. The private key never leaves the host.
- `package_update: true` + `packages` — refresh the package index and
  install a basic toolset on first boot.

`ubuntu-lab-1` is the same file with `hostname: ubuntu-lab-1` and `tmux`
added to the package list.

> Note: this config does **not** set networking. libvirt's DHCP proved
> unreliable in this lab, so static IPs are set *inside* each VM after
> first boot — systemd-networkd on Debian, netplan on Ubuntu. See the
> troubleshooting section.
