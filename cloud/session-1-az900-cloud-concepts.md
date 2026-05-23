# Session 1 — AZ-900 Cloud Concepts

Part of Phase 2: studying for the Microsoft AZ-900 (Azure Fundamentals) certification.

## What is cloud computing?

Renting someone else's computers over the internet instead of owning your own. You pay for what you use and hand it back when you're done. The provider (e.g. Microsoft Azure) owns the datacentres, power, cooling and hardware — you just rent a slice.

## CapEx vs OpEx

This is about *how you pay*, not about owning vs renting.

- **CapEx (capital expenditure)** — one big upfront purchase. You own the asset; it loses value over time.
- **OpEx (operational expenditure)** — ongoing pay-as-you-go running cost. No asset owned.

Cloud is **OpEx**.

## The four cloud benefits

- **Scalability / elasticity** — scale up *and* down on demand. Rent 100 servers for one busy day, 5 the rest of the year. No paying for idle hardware.
- **High availability** — is the service up *right now*. Measured as an uptime percentage (e.g. 99.9%).
- **Reliability** — can the service *recover from a failure*. It breaks, then heals itself (e.g. fails over to another datacentre).
- **Predictability** — lets you forecast two things: **performance** and **cost**.

**Availability vs reliability** — the easy trap. Availability = "is it up, yes/no". Reliability = "something broke, then it recovered". If there's a failure-then-recovery story, it's reliability.

**Redundancy → reliability** — redundancy is the *mechanism* (spare servers/datacentres you build). Reliability is the *benefit* it produces. Cause → effect, not the reverse.

## Service models — what you rent

Control goes *down* and convenience goes *up* as you move along this list.

- **IaaS (Infrastructure as a Service)** — rent raw infrastructure: a VM, storage, networking. You manage the OS and everything above it. *"I just need a VM, I'll handle the rest."*
- **PaaS (Platform as a Service)** — rent a ready platform. Microsoft manages the OS, runtime and infrastructure; you supply only **code and data**. *"Here's my code, you run it."*
- **SaaS (Software as a Service)** — rent finished software. You manage nothing but your own usage. *"I just log in and use it."* (Gmail, Office 365.)

Homelab tie-in: a homelab VM is the on-premises equivalent of IaaS — you manage the OS upward.

## Deployment models — where it lives / who shares it

- **Public** — shared provider hardware. Cheapest, most scalable, least control. OpEx.
- **Private** — dedicated hardware for one organisation. More control and privacy, but CapEx and upkeep.
- **Hybrid** — public and private joined, working as one. Choose per workload. E.g. a hospital keeps regulated patient records private but runs its scalable public-facing booking site on public cloud.

Core trade-off: **control/privacy vs cost/scalability.**

Homelab tie-in: the homelab itself is a private cloud; connecting it to Azure to run workloads across both makes it hybrid.
