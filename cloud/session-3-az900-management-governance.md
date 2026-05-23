# Session 3 — AZ-900 Management & Governance
Part of Phase 2: studying for the Microsoft AZ-900 (Azure Fundamentals) certification.

## Cost management
Cloud cost is something you forecast and watch, not set once and forget.

**Forecast before you build:**
- **Pricing Calculator** — estimate the monthly bill for *new* Azure services you plan to build. Pick services, configure, get an estimate.
- **TCO Calculator** (Total Cost of Ownership) — compare your *existing on-premises* costs against running the same workload in Azure. A migration-justification tool.

Trap: both are calculators. Pricing = planning a new cloud build. TCO = comparing existing on-prem vs cloud.

**Watch after you build:**
- **Microsoft Cost Management** — shows *actual* spend on resources already running. Home of **budgets** and **alerts** (get pinged when spend crosses a threshold).

**Tags** — free key-value labels on resources (e.g. `department:finance`, `env:production`). Used to slice the bill and group resources for policy.

## Identity & access
**Microsoft Entra ID** (formerly Azure AD) — Azure's identity directory: users, groups, apps. The front door to everything.

- **Authentication (AuthN)** — proving *who you are*. Logging in.
- **Authorization (AuthZ)** — what you're *allowed to do* once you're in.
- Order: authenticate first, then authorize.

**MFA (Multi-Factor Authentication)** — requires two of three *different factor types*:
- something you **know** (password)
- something you **have** (phone, security key)
- something you **are** (fingerprint, face)

Two of the *same* type (e.g. password + security question) is NOT real MFA — both are "something you know".

**Passwordless** (security key, Windows Hello, Authenticator app) is stronger because it bundles factor types in one step: a thing you *have*, unlocked by a thing you *know* or *are*.

**RBAC (Role-Based Access Control)** — assign a *role* (a bundle of permissions) to a user/group at a *scope* (where it applies). Governs what *people* can do.

**Zero Trust** — "never trust, always verify." Don't assume someone is safe just because they're inside the network. MFA and RBAC implement it.

## Governance & compliance
**The hierarchy** (top → bottom):
- **Management group** — a container for multiple subscriptions.
- **Subscription** — a billing and access boundary.
- **Resource group** — a folder for resources that share a lifecycle.
- **Resource** — the actual thing (e.g. the VM).

Anything applied at a level **flows downward (inheritance)** — set a policy or RBAC role at the management group and everything beneath inherits it.

**Azure Policy** — rules about what *resources* are allowed to be (e.g. "VMs only in UK South", "every resource must have a department tag"). Policy is **resource-based**, not group-based. It is *scoped* — but within that scope it applies to everyone regardless of role.

RBAC vs Policy: **RBAC = what a person can do. Policy = what a resource can be.** RBAC might let you create a VM; Policy can still reject the one you tried to create.

**Resource locks** — protection against accidents:
- **Delete lock** — can read and modify, can't delete.
- **Read-only lock** — can read, can't modify or delete.

A lock stops even an Owner.

## Monitoring & service health
- **Azure Monitor** — how are *my resources* performing? Metrics and logs from your own resources.
- **Azure Service Health** — is *Azure itself* having problems? Outages, planned maintenance for the regions/services you use.
- **Azure Advisor** — proactive recommendations across cost, security, reliability and performance.

Trap: Monitor vs Service Health. Monitor = my resources. Service Health = Azure's platform.

## Triage notes — wording to keep exact
- **Elasticity** is the cloud *benefit* (scale up *and down*); **OpEx** is the *payment model*. Don't swap them.
- **Azure Policy is resource-based**, not group-based. RBAC = people, Policy = resources.
- A Reader role being blocked lower down is due to **inheritance** — scope flows downward.
