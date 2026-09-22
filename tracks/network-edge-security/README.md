# Network & Edge Security

Controlling what reaches the workload and, more importantly, what the workload can reach. Built on
production experience with centralized inspection, TLS inspection and edge protection in
multi-account organizations.

## Scope

- **Egress control** — centralized inspection with Network Firewall, domain allowlists, TLS
  inspection and its certificate constraints, the asymmetric-routing failure modes of multi-AZ
  inspection paths.
- **DNS** — Route 53 Resolver DNS Firewall against exfiltration and command-and-control, query
  logging as a detection source, split-horizon pitfalls.
- **Edge** — WAF rule engineering against real exploitation traffic, rate-based rules, bot
  control, Shield Advanced and the Anti-DDoS managed rule group, Firewall Manager at scale.
- **Segmentation** — Transit Gateway route table design as a security boundary, RAM sharing scope,
  and the difference between a segmentation diagram and enforced segmentation.

## Published scenarios

None yet.

## Planned

- **DNS tunneling out of a private subnet** (T1048) — exfiltration through recursive DNS while all
  other egress is blocked, detection in Resolver query logs, and the DNS Firewall rule that stops
  it without breaking legitimate resolution.
- **Egress to attacker-controlled infrastructure** (T1041) — beaconing through a centralized
  inspection path, including SNI and HTTP-host mismatch attempts to slip past an allowlist.
- **Web exploitation behind WAF** (T1190) — building a rule set that blocks the exploitation
  attempt while the managed rules alone do not, with the false-positive cost measured against
  legitimate traffic.
- **Segmentation that is not enforced** — a spoke reaching another spoke that the architecture
  diagram says it cannot, through an inspection path that fails open.

## Relationship to the networking portfolio

Diagnostic networking case work, including the Network Firewall and Shield cases this track builds
on, lives in [AWS-NET](https://github.com/rreyescloud/AWS-NET). This track is the adversarial view
of the same infrastructure: not why traffic broke, but whether the control actually holds.
