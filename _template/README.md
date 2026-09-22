# SEC-XXX: <Title naming the counterintuitive finding, not the service>

## Status: <Resolved | In Progress> — <YYYY-MM-DD> · <Lab validated | Lab pending>

- **MITRE ATT&CK:** <TXXXX.XXX — Technique name>
- **Services:** <IAM, CloudTrail, GuardDuty, EventBridge, Lambda, ...>
- **Lab cost:** ~$<X.XX>/hour, ~$<X.XX>/day
- **Blast radius:** <what the lab creates that looks malicious, and why it is safe in a dedicated account>

## Objective

One paragraph: which technique is simulated, which signal detects it, which action contains it, and
what the scenario proves that is not obvious from the documentation.

## Threat Scenario — <Industry descriptor>

Why this matters commercially for that kind of organization: what the attacker gains, what the
business loses, and which compliance obligation is in play. No customer names.

## Environment

- **Architecture:** <what is deployed, with placeholder identifiers>
- **Attacker position:** <what the adversary starts with — a leaked key, a compromised pod, an unauthenticated internet client>
- **Assumed breach boundary:** <what is taken as already compromised, and what is not>

## Attack Simulation

The exact steps that produce the malicious activity, reproducible verbatim.

```bash
# commands, with placeholders for identifiers
```

- **Expected observable:** <the API calls, packets or requests this generates>
- **Time to generate:** <how long before the signal should exist>

## Detection

- **Signal source:** <CloudTrail management events | GuardDuty | VPC Flow Logs | Resolver query logs>
- **Key fields:** <the exact fields the rule keys on and why those and not others>
- **Rule:** see [`detections/`](detections/)
- **Measured latency:** <detection delay observed in the lab, not the documented delay>
- **False-positive profile:** <what legitimate activity looks identical, how often it occurs in a real organization, and the additional field that separates them>
- **Blind spots:** <what this detection cannot see, including the evasion that defeats it>

## Response

- **Containment action:** <revoke, quarantine, isolate, lock down>
- **Automated:** <yes, through EventBridge to Lambda | no, and why a human must decide>
- **Deliberately not done:** <the action that was avoided and the blast radius that justified it>
- **Recovery:** <how to return to a clean state and confirm the adversary lost access>

## Evidence

Captured output proving the attack occurred, the detection fired and the response executed. Kept in
[`lab/evidence/`](lab/evidence/), sanitized, with timestamps and regions preserved.

```
<decisive log excerpt, not a full dump>
```

## Hardening — what would have prevented this

- **Preventive control:** <the SCP, boundary, policy condition or network control>
- **Cost:** <operational and financial>
- **Residual risk:** <what remains even with the control in place>
- **Why organizations skip it:** <the honest reason — cost, friction, or a legitimate workflow it breaks>

## Reusable Takeaways

1. <Transferable lesson, stated so it is useful without this scenario's context>
2. <...>

## Lab

```bash
cd lab
python deploy_lab.py deploy   --profile <your-aws-profile>
python deploy_lab.py test     --profile <your-aws-profile>
python deploy_lab.py status   --profile <your-aws-profile>
python deploy_lab.py teardown --profile <your-aws-profile>
```

Run only in a dedicated lab account. `teardown` removes everything `deploy` created; verify with
`status` that nothing remains.

## References

1. <Public AWS documentation URL>
2. <MITRE ATT&CK technique URL>
3. <Public research or blog post>
