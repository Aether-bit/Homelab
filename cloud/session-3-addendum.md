# Session 3 Addendum — AZ-900 Exam Status & Revision Gaps

## Exam status

- **Exam:** AZ-900 — Microsoft Azure Fundamentals
- **Status:** Booked / pending
- **Date:** Friday, 29 May 2026, 12:30 BST
- **Location:** Verhoef Training, 11 Kingsmead Square, Bath BA1 2AB (in-person test centre)
- **Cost:** £76.80 (£64 exam + £12.80 tax)

### Exam format

- 65 minutes, ~40–60 questions, passing score 700/1000 (~70%).
- Mostly single-answer multiple choice, plus multiple-response, drag-and-drop, and short case-study questions.
- No labs — entirely question-based. No negative marking, so attempt every question.
- Result shown immediately after finishing.

### Readiness

- Scored **86%** on the official Microsoft practice assessment (target is 80%+) — already over the pass line.
- Practice assessment was single-answer only; drag-and-drop and multiple-response formats not yet rehearsed.

### Day-of checklist

- Bring photo ID matching the name exactly: **Kieran David John Mott**.
- Arrive early.

## Revision gaps — topics missed in the practice assessment

These came up in the practice exam and weren't covered in the three teaching sessions. Aim for a confident one-line definition of each.

**Compute / management plane**
- **ARM (Azure Resource Manager)** — the deployment and management layer underneath everything; every action (portal, CLI, PowerShell) goes through ARM. Also enables **ARM templates** — declarative JSON for infrastructure as code. Azure's control plane.
- **Azure Functions** — serverless compute. Small piece of code that runs only when *triggered* (HTTP request, timer, file upload); pay only for execution time. The extreme end of PaaS.
- **Azure Arc** — extends Azure management *outward* to non-Azure resources: on-prem servers, other clouds, Kubernetes clusters. Manage them with Azure tools (Policy, monitoring) as if they were Azure resources. Hybrid / multi-cloud management.

**Networking**
- **VNet peering** — connects two virtual networks so resources talk *privately*, as if on one network. Traffic stays on Microsoft's backbone, never the public internet.
- **Service endpoints** — extend a VNet's private identity to an Azure PaaS service (e.g. storage, SQL), so that service can be locked to accept traffic *only* from your VNet. Secures PaaS to your network.

**Identity**
- **Microsoft Entra Domain Services** — managed traditional domain services (domain join, group policy, LDAP, Kerberos) *without* running your own domain controllers. Bridge for legacy apps needing old-style Active Directory. Different from plain Entra ID (modern cloud identity) — Domain Services adds the legacy AD capabilities.

**Service health**
- **Health advisories** — one of the three notification types inside **Azure Service Health**: service issues (active outages), planned maintenance (scheduled work), and health advisories (changes needing your attention, e.g. a feature deprecation).

### Trap-level summary

ARM = control plane under everything · Functions = serverless code · Arc = manage non-Azure stuff · Peering = VNet-to-VNet private link · Service endpoints = lock PaaS to your VNet · Entra Domain Services = managed legacy AD · Health advisories = a Service Health notification type.

## Revision plan for the week

1. Read the 7 gap topics above until each has a confident one-line definition.
2. Re-check the 3 triage wording patches in `session-3-az900-management-governance.md` (elasticity vs OpEx, Policy = resource-based, inheritance).
3. Do one more free practice exam mid-week — ideally one including drag-and-drop and multiple-response questions.
4. Light re-read of all three `cloud/` session notes the night before.
