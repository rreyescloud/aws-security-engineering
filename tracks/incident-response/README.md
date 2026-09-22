# Incident Response & Forensics

End-to-end handling of cloud incidents: containment first, evidence preserved, timeline
reconstructed, root cause stated, preventive control proposed.

## Scope

- **Containment** — session revocation, key deactivation, instance and ENI isolation, bucket
  policy lockdown, blast-radius decisions and what containment breaks.
- **Evidence acquisition** — EBS snapshots for offline analysis, memory considerations,
  CloudTrail Lake queries, VPC Flow Logs, S3 access logs, ALB and CloudFront logs.
- **Reconstruction** — assembling a defensible timeline from multiple log sources with clock and
  delivery-latency caveats stated explicitly.
- **Post-incident** — the preventive control, its cost, and what residual risk remains.

## Published scenarios

None yet.

## Planned

- **Public bucket, bulk read** (T1530) — bucket policy opened by a legitimate principal, followed
  by anonymous bulk download; scoping what was actually read versus what was exposed, and why
  those two numbers differ.
- **Cryptomining in a compromised container workload** (T1496) — detection through cost and
  network signals rather than the process tree, containment without destroying evidence, and
  isolating a node while keeping the cluster serving.
- **Compromised CI/CD credential** — a build role used outside the pipeline, containment when the
  credential is required for production deploys, and rotation under time pressure.

## Playbook bar

Each playbook states the decision that has to be made in the first five minutes, who can make it,
and the cost of getting it wrong in either direction. Containment that nobody is authorized to
execute is not a playbook.
