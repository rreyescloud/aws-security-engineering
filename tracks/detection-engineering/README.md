# Detection Engineering

Turning AWS control-plane and service signals into detections that fire on a real attack, with a
stated latency and a stated false-positive profile.

## Scope

- **Signal sources** — CloudTrail (management and data events), GuardDuty findings, Security Hub,
  CloudTrail Lake queries, VPC Flow Logs, Route 53 Resolver query logs.
- **Rule delivery** — EventBridge patterns, GuardDuty and Security Hub custom insights, Lambda
  responders, CloudTrail Lake SQL for retrospective hunting.
- **What a finished detection includes** — the technique it catches, the exact event fields it
  keys on, measured detection latency, the false-positive profile, and what it cannot see.

## Published scenarios

None yet.

## Planned

- **Leaked access key used from an unexpected network** (T1078.004) — key exfiltrated to a
  non-corporate ASN, detection on the `sourceIPAddress` and `userAgent` pair, automatic session
  revocation, false positives from third-party SaaS integrations.
- **New credentials attached to an existing principal** (T1098.001) — `CreateAccessKey` and
  `CreateLoginProfile` against a principal that is not the caller, with the self-service
  exception that generates most of the noise.
- **CloudTrail tampering** (T1562.008) — `StopLogging`, `DeleteTrail` and trails redirected to a
  foreign bucket; why the detection must survive the loss of the signal it depends on.
- **Enumeration burst after credential compromise** (T1580) — distinguishing an attacker's
  discovery sweep from a legitimate inventory tool by call diversity rather than call volume.

## Detection quality bar

A rule that only fires in the lab is not a detection. Each scenario must answer: what legitimate
activity looks identical, how often that happens in a real organization, and what additional
field separates the two.
