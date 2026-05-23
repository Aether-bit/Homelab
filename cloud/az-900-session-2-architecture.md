# AZ-900 Session 2 — Azure Architecture & Services

Part of Phase 2: studying for the Microsoft AZ-900 (Azure Fundamentals)
certification. Covers Domain 2 — Azure architecture and core services.

## Physical hierarchy — where things run

Biggest to smallest:

- **Region** — a geographic area of Azure datacentres (e.g. UK South).
  Choose for latency and data-residency law.
- **Availability Zone (AZ)** — a physically separate datacentre within a
  region (own power, cooling, networking). 3+ per region. Surviving a
  datacentre failure means spreading a workload across zones.
- **Region pair** — every region is paired with another in the same
  geography (UK South <-> UK West). Replication crosses the pair; Azure
  won't apply a planned update to both halves at once. Survives a
  whole-region failure.
- **Datacentre** — the physical building. Never picked directly.

Protection ladder: AZ survives a datacentre failure -> region pair
survives a whole-region failure.

Pairs stay in the same geography because of data-residency law —
replication must not move data outside its legal jurisdiction.

## Management hierarchy — how things are organised

Biggest to smallest:

- **Management group** — container for multiple subscriptions.
- **Subscription** — a billing and access boundary. Can have many
  (Prod, Dev, per-client), each its own invoice and access wall.
- **Resource group** — a folder for resources that belong together.
  Delete the group, everything in it goes.
- **Resource** — the actual thing (VM, storage account, VNet).

Inheritance flows **down** the hierarchy. Set high = applies broadly.

## Compute — four ways to run code

Work spectrum, most to least: VM -> ACI -> AKS -> App Service -> Functions.

- **Virtual Machine (VM)** — a full computer; you manage OS and up. IaaS.
- **Azure Container Instances (ACI)** — a single container, no host to
  manage. Lighter and faster to start than a VM.
- **Azure Kubernetes Service (AKS)** — managed Kubernetes; many
  containers across a cluster, scaling and healing handled.
- **App Service** — hand Azure your code, it runs it. No OS/patching. PaaS.
- **Azure Functions** — serverless; code runs only when triggered, then
  stops. Good for short, intermittent tasks. Bad for constant or
  long-running workloads.

Term watch: IaaS (a *service* you rent) vs IaC (Infrastructure as
*Code* — Terraform/Ansible). Different things.

## Storage

Most storage lives in a **storage account**.

- **Blob storage** — Binary Large OBject. Unstructured data (images,
  video, backups, logs). Default home for files.
- **File storage** — a managed file share, mounted like a network drive.
- **Queue storage** — small messages in a line; decouples app components.
- **Table storage** — cheap store for structured non-relational data.

Access tiers (match to access pattern):

- **Hot** — frequent access. Higher storage cost, cheap reads.
- **Cool** — infrequent. Cheaper storage, pricier reads.
- **Archive** — rarely touched, long retention. Cheapest storage; slow
  and costly to retrieve.

Redundancy:

- **LRS** (Locally Redundant Storage) — copies within one datacentre.
- **GRS** (Geo-Redundant Storage) — copies to the paired region.

## Networking

- **Virtual Network (VNet)** — your own private network in Azure. Every
  VM lives in one.
- **Subnet** — a VNet sliced into segments to organise and control traffic.
- **Network Security Group (NSG)** — allow/deny traffic rules attached to
  a subnet or VM. The cloud equivalent of ufw.
- **Public vs private IP** — private works only inside the VNet; public
  is internet-reachable.

Connecting a VNet to your own network (hybrid):

- **VPN Gateway** — encrypted tunnel over the public internet. Cheaper,
  quicker; performance varies.
- **ExpressRoute** — a private, dedicated connection that never touches
  the public internet. Faster, consistent, pricier.

A VPN tunnel makes the public internet *safe* (encrypted) but not
*private* (still shared). ExpressRoute is genuinely private.
