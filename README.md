# AWS Security Engineering — Detection, Response and Guardrails

Every scenario in this repository is a **closed loop**: simulate the technique against real AWS
infrastructure, detect it, contain it automatically, and prove all three with captured evidence.
No theory without a deployed lab behind it, and no claim without the log that backs it.

Scenarios come from patterns observed while supporting enterprise AWS workloads — multi-account
organizations, centralized inspection, regulated industries. Customer identities, account IDs and
case references are never published; see [Conventions](docs/Conventions.md).

## Skill → artifact

- **Detection engineering** — CloudTrail / GuardDuty / Security Hub signals turned into rules with
  a proven true positive and a documented false-positive profile → [`tracks/detection-engineering/`](tracks/detection-engineering/)
- **Incident response & forensics** — containment playbooks, credential revocation, host isolation,
  evidence acquisition, timeline reconstruction → [`tracks/incident-response/`](tracks/incident-response/)
- **Identity & guardrails** — least privilege generation, SCPs with tests that prove what they
  block, permission boundaries, policy-as-code in CI → [`tracks/identity-guardrails/`](tracks/identity-guardrails/)
- **Network & edge security** — egress control, DNS exfiltration defense, TLS inspection, WAF rule
  engineering, multi-account segmentation → [`tracks/network-edge-security/`](tracks/network-edge-security/)
- **Infrastructure as code & CI security** — every lab is deployable and destroyable from code;
  the pipeline scans IaC and blocks secrets → [`.github/workflows/ci.yml`](.github/workflows/ci.yml)

Deeper networking background, including WAF, Shield and Network Firewall case work:
[AWS-NET portfolio](https://github.com/rreyescloud/AWS-NET).

## Status

Scaffold. No scenarios published yet — tracks are created with their scope defined, and each
`README.md` lists the planned scenarios so the backlog is visible rather than implied.

## Structure

```
tracks/
└── <track>/
    ├── README.md                     scope, threat coverage, planned scenarios
    └── scenarios/
        └── SEC-XXX_snake_case_name/
            ├── README.md             the closed loop: attack, detect, respond, evidence
            ├── architecture.drawio   what gets deployed
            ├── lab/
            │   ├── deploy_lab.py     deploy | status | test | teardown
            │   └── evidence/         captured logs and findings
            └── detections/           rule definitions (EventBridge, Security Hub, Sigma)
docs/
├── Conventions.md                    scenario format, id scheme, sanitization rules
├── Learning-Plan.md                  the twelve-week plan each scenario comes from
└── MITRE-Coverage.md                 which ATT&CK techniques are covered, and by what
_template/                            copy this to start a scenario
```

## Running a lab

Each scenario is self-contained and priced. Labs are tagged, cost-capped and designed to be torn
down the same day.

```bash
cd tracks/<track>/scenarios/SEC-XXX_name/lab
python deploy_lab.py deploy   --profile <your-aws-profile>
python deploy_lab.py test     --profile <your-aws-profile>
python deploy_lab.py teardown --profile <your-aws-profile>
```

Run these only in a dedicated lab account. Several scenarios intentionally create detectable
malicious-looking activity, and some deliberately misconfigure a control before hardening it.

## About

**Rreyes Cloud** — Networking & Security Solutions on AWS
