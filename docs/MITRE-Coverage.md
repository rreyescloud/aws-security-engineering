# MITRE ATT&CK Coverage

Techniques from the [Enterprise matrix, Cloud platforms](https://attack.mitre.org/matrices/enterprise/cloud/)
that this repository targets. A technique counts as covered only when a published scenario
simulates it, detects it and shows the evidence.

**Covered:** none yet — the repository is a scaffold.

## Targeted backlog

- **T1078.004 — Valid Accounts: Cloud Accounts** — use of a leaked long-lived access key from an
  unexpected network. Planned in `detection-engineering`.
- **T1098.001 — Account Manipulation: Additional Cloud Credentials** — attacker attaches a new
  access key or login profile to an existing principal. Planned in `detection-engineering`.
- **T1548.005 — Abuse Elevation Control Mechanism: Temporary Elevated Cloud Access** — privilege
  escalation through `iam:PassRole` and role chaining. Planned in `identity-guardrails`.
- **T1562.008 — Impair Defenses: Disable or Modify Cloud Logs** — CloudTrail stopped, deleted or
  reconfigured to a foreign bucket. Planned in `detection-engineering`.
- **T1580 — Cloud Infrastructure Discovery** — mass enumeration of resources following a
  credential compromise. Planned in `detection-engineering`.
- **T1530 — Data from Cloud Storage** — bucket policy opened to the world, followed by bulk read.
  Planned in `incident-response`.
- **T1496 — Resource Hijacking** — cryptomining in a compromised container workload. Planned in
  `incident-response`.
- **T1048 — Exfiltration Over Alternative Protocol** — DNS tunneling out of a private subnet, and
  the Route 53 Resolver DNS Firewall control that stops it. Planned in `network-edge-security`.
- **T1190 — Exploit Public-Facing Application** — web exploitation against an application behind
  WAF, and the rule engineering that blocks it without breaking legitimate traffic. Planned in
  `network-edge-security`.
- **T1041 — Exfiltration Over C2 Channel** — egress to an attacker-controlled endpoint through a
  centralized inspection path, allowlist bypass attempts included. Planned in
  `network-edge-security`.

AI and LLM specific techniques are tracked separately against MITRE ATLAS in the
[ai-labs](https://github.com/rreyescloud/ai-labs) repository.
