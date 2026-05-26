# DevOps / Cloud Engineering Roadmap

My structured learning path toward a Cloud / DevOps Engineer role. Based on
the standard DevOps roadmap, worked through section by section. Updated as I
go — each completed item is backed by notes and commits in this repo.

**Legend:** ✅ Done · 🔄 In progress · 📋 Planned

---

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

---

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

---

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

---

*This roadmap is a living document — last updated 2026-05-26.*
