# DevOps / Cloud Engineering Roadmap

Career target: **Cloud Engineer / DevOps Engineer**, building up from an
entry-level role.

A living document — two parts: the certification path, and the underlying
skills roadmap. Each completed skill is backed by notes and commits in this
repo. Last updated 2026-05-26.

---

# Part 1 — Certification Path

## Current position

- **AZ-900 (Azure Fundamentals)** — booked for 29 May 2026. The foundation
  cert: proves you can name and reason about cloud concepts. First piece of
  outside validation on top of the homelab work.
- **Homelab** — built and documented (git, virtualisation, Linux, Docker).
  Already demonstrates the "show the work" instinct.

## The path after AZ-900

AZ-900 is the only pure "fundamentals" cert needed. Everything after it is
**role-based**, and the two career targets split slightly.

### Next step (both targets): AZ-104 — Azure Administrator

The natural follow-on — where you stop *describing* Azure and start *doing*
it: identities, storage, virtual networks, VMs, monitoring. A real step up
in difficulty, hands-on and scenario-heavy. This is the cert that moves you
off entry-level, because it maps to a job employers recognise. For a Cloud
Engineer target, this is the spine.

### Then the fork

- **DevOps Engineer** → **AZ-400 (DevOps Engineer Expert)** — CI/CD
  pipelines, infrastructure as code, release management. Prerequisite:
  AZ-104 or AZ-204. Path: AZ-900 → AZ-104 → AZ-400.
- **Cloud Engineer** → AZ-104 may be enough cert-wise for a while; deepen
  with hands-on work rather than stacking another exam immediately.

## Realistic sequence

1. **AZ-900** — pass it (29 May 2026).
2. **Hands-on cloud project** — add something real to the repo
   (e.g. Terraform-provisioned Azure resources).
3. **AZ-104** — the role-based step up.
4. **Decide DevOps vs Cloud Engineer** and specialise (AZ-400 if DevOps).

Key principle: **don't exam-stack.** Alternate certs with visible projects.
A candidate with AZ-104 *and* a Terraform-built project beats a candidate
with three certs and nothing to show.

---

# Part 2 — Skills Roadmap

The certs above don't test everything. This is the underlying skill set,
worked through section by section against a standard DevOps roadmap.

**Legend:** ✅ Done · 🔄 In progress · 📋 Planned

## Foundations

### Linux & Operating System
- ✅ File permissions & ownership
- ✅ Process management
- ✅ systemd / services
- ✅ Package management
- ✅ User & group management
- 🔄 Shell, text processing (grep/sed/awk), SSH
- 📋 Filesystem hierarchy deep-dive

### Networking
- ✅ TCP/IP model, IP addressing & subnets
- ✅ TCP vs UDP, NAT, routing
- 🔄 DNS, ports, firewalls (nftables)
- 📋 HTTP/HTTPS internals, load balancers

### Version Control (Git)
- ✅ Core workflow — add, commit, push, pull
- 🔄 Branching, merging, pull requests
- 📋 Conflict resolution, history rewriting

## Core DevOps

### Containers — Docker
- ✅ Container fundamentals, images & layers
- ✅ Volumes & port mapping
- ✅ Docker Compose, multi-service stacks
- 🔄 Dockerfile authoring, debugging, image management

### CI/CD
- 📋 Pipelines & "pipeline as code"
- 📋 GitHub Actions
- 📋 Build / test / deploy stages
- 📋 Artifacts & pipeline secrets

### Infrastructure as Code
- 📋 Terraform — declarative infra, state
- 📋 Ansible — configuration management
- 📋 Idempotency, providers & modules

### Kubernetes / Orchestration
- 📋 Pods, nodes & clusters
- 📋 Deployments & services
- 📋 kubectl, self-healing & scaling
- 📋 ConfigMaps, Secrets, Ingress

## Cloud & Operations

### Cloud Platforms
- ✅ Cloud fundamentals, the major providers
- ✅ IAM, regions & availability zones, cost models
- 🔄 Compute, object storage, cloud networking (VPC)
- 📋 Managed services, serverless

### Monitoring & Observability
- ✅ Logging fundamentals, why monitoring matters
- 🔄 Metrics, alerting, observability concepts
- 📋 Prometheus & Grafana

### Security
- ✅ Least privilege
- 🔄 Secrets management
- 📋 TLS / certificates
